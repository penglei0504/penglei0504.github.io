"""Read-only source checks. Uses an existing Python environment with PyYAML."""
from collections import defaultdict
import json
from pathlib import Path
import posixpath
import re
import sys
from urllib.parse import unquote, urlsplit
import yaml

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", "_site", "node_modules", "vendor", "My_CV", "My_project", "_maintenance"}


class UniqueLoader(yaml.SafeLoader):
    pass


def construct_mapping(loader, node, deep=False):
    seen = set()
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            continue
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            raise ValueError(f"Duplicate explicit YAML key: {key}")
        seen.add(key)
    loader.flatten_mapping(node)
    return yaml.SafeLoader.construct_mapping(loader, node, deep=deep)


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping)


def main():
    errors, warnings, docs = [], [], {}
    routes = defaultdict(set)
    files = [p for p in ROOT.rglob("*") if p.is_file() and not set(p.relative_to(ROOT).parts) & SKIP]
    config = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
    collections = config["collections"]
    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        try:
            if path.suffix in {".yml", ".yaml"}:
                yaml.load(path.read_text(encoding="utf-8-sig"), Loader=UniqueLoader)
            # VS Code devcontainer files allow JSON with comments (JSONC).
            if path.suffix == ".json" and ".devcontainer" not in path.parts:
                json.loads(path.read_text(encoding="utf-8-sig"))
            if path.suffix not in {".md", ".html", ".scss"}:
                continue
            text = path.read_text(encoding="utf-8-sig")
            if not text.startswith("---"):
                continue
            pieces = re.split(r"^---\s*$", text, maxsplit=2, flags=re.M)
            if len(pieces) != 3:
                raise ValueError("Unclosed front matter")
            data = yaml.load(pieces[1], Loader=UniqueLoader) or {}
            docs[rel] = data
            if data.get("layout") and not (ROOT / "_layouts" / (data["layout"] + ".html")).is_file():
                errors.append(f"{rel}: missing layout {data['layout']}")
            if rel.startswith(("_layouts/", "_includes/", "_drafts/")):
                continue
            route = data.get("permalink")
            collection = path.parent.name.lstrip("_")
            if not route and collection in collections:
                route = f"/{collection}/{path.stem}/"
            if route:
                routes[route.rstrip("/") or "/"].add(rel)
                aliases = data.get("redirect_from", [])
                if isinstance(aliases, str):
                    aliases = [aliases]
                for alias in aliases:
                    routes[alias.rstrip("/") or "/"].add(rel)
        except (ValueError, TypeError, yaml.YAMLError) as error:
            errors.append(f"{rel}: {error}")
    for route, owners in routes.items():
        if len(owners) > 1:
            errors.append(f"Duplicate route {route}: {sorted(owners)}")
    generated = {"/sitemap.xml", "/feed.xml", "/assets/css/main.css"}

    def exists(url):
        target = unquote(urlsplit(url).path)
        return target in generated or (target.rstrip("/") or "/") in routes or (ROOT / target.lstrip("/")).exists()

    nav = yaml.safe_load((ROOT / "_data/navigation.yml").read_text(encoding="utf-8"))["main"]
    if [item["title"] for item in nav] != ["Research", "Projects", "Publications", "Presentations", "Awards", "CV"]:
        errors.append("Unexpected main navigation order")
    for item in nav:
        if not exists(item["url"]):
            errors.append(f"Navigation target missing: {item['url']}")
    checked, dynamic = 0, 0
    for path in files:
        if path.suffix not in {".md", ".html", ".css", ".scss"}:
            continue
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8-sig")
        for name in re.findall(r"{%\s*include\s+([^\s%]+)", text):
            name = name.strip("\"'").lstrip("/")
            if "{{" not in name and not (ROOT / "_includes" / name).is_file():
                errors.append(f"{rel}: missing include {name}")
        text = re.sub(r"{{\s*(?:base_path|site.baseurl)\s*}}", "", text)
        text = re.sub(r"{{\s*site.url\s*}}", config["url"], text)
        refs = re.findall(r"(?:href|src|action)\s*=\s*[\"']([^\"']+)", text)
        refs += re.findall(r"\]\(([^\n)]+)\)", text)
        refs += re.findall(r"url\(\s*[\"']?([^\"')]+)", text)
        for url in refs:
            if "{{" in url or "{%" in url:
                dynamic += 1
                continue
            url = url.strip().split(' "')[0]
            if url.startswith(config["url"]):
                url = url[len(config["url"]):] or "/"
            if not url or url.startswith(("#", "//")) or urlsplit(url).scheme:
                continue
            if not url.startswith("/"):
                base = docs.get(rel, {}).get("permalink", "/" + rel)
                base = base if base.endswith("/") else posixpath.dirname(base)
                if rel.startswith("_sass/"):
                    base = "/assets/css/"
                url = posixpath.normpath(posixpath.join(base, url))
            checked += 1
            if not exists(url):
                issue = f"{rel}: missing local reference {url}"
                # This dormant, pre-existing layout is outside the update scope.
                (warnings if rel == "_layouts/cv-layout.html" and url == "/assets/css/cv-layout.css" else errors).append(issue)
    projects = {rel: data for rel, data in docs.items() if data.get("project") is True}
    project_listing = (ROOT / "_pages/projects.html").read_text(encoding="utf-8")
    # Jekyll's where filter returns its entire input when the value is nil.
    # Prevent categorized cards from being repeated as uncategorized cards.
    if re.search(r'where:\s*[\"\']project_category[\"\']\s*,\s*nil', project_listing):
        errors.append("Projects listing uses where with nil, which repeats categorized projects")
    project_urls = [data["permalink"] for data in projects.values() if data.get("permalink")]
    if len(project_urls) != len(set(project_urls)):
        errors.append("Duplicate project URLs")
    for rel, project in projects.items():
        for field in ["title", "summary", "permalink", "project_order"]:
            if not project.get(field):
                errors.append(f"{rel}: missing project field {field}")
        if project.get("cover") and not exists(project["cover"]):
            errors.append(f"{rel}: missing cover")
        for key, items in project.items():
            if key == "media" or key.endswith("_media"):
                for item in items:
                    if item.get("type") not in {"image", "video", "external-video"}:
                        errors.append(f"{rel}: unsupported media type")
                    if item.get("type") == "external-video":
                        if urlsplit(item.get("url", "")).scheme not in {"http", "https"}:
                            errors.append(f"{rel}: external video must use HTTP(S)")
                    elif not item.get("src") or not exists(item["src"]):
                        errors.append(f"{rel}: missing media file")
                    if item.get("poster") and not exists(item["poster"]):
                        errors.append(f"{rel}: missing video poster")
        for related in project.get("related_publications", []):
            if not exists(related["url"]):
                errors.append(f"{rel}: missing related publication")
    print(json.dumps({"front_matter_files": len(docs), "routes": len(routes), "project_pages": len(projects),
                      "literal_local_links_checked": checked, "dynamic_references_not_rendered": dynamic,
                      "errors": errors, "warnings": warnings}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
