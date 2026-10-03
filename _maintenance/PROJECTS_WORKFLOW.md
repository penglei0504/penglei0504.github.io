# Maintaining Projects and academic information

`My_CV/` and `My_project/` are local reference folders. Preserve original bytes and filenames. Do not stage these folders automatically: GitHub Pages can publish ordinary root folders. Commit only reviewed website-facing outputs. This workflow does not change deployment settings.

## Current source inventory

On 2026-10-03, two documented project folders were published through website-facing copies:

- `My_project/1/1.docx`: In-line Robotic Platform for Intelligent Pipeline Inspection (`/projects/in-line-robotic-pipeline-inspection/`).
- `My_project/2/2.docx`: Wireless Portable TMR Array for Eddy Current Imaging (`/projects/wireless-portable-tmr-array/`).

Both are featured. The source Word documents remain authoritative. Preserve their section order and future-work wording. Match `[imgN]` and `[videoN]` directly to filenames in the same folder; preserve placement and group adjacent image placeholders. The manifest records these mappings, cover choices, hashes, and output files. Project 1's unreferenced `img2.png` and `img3.png` were intentionally not copied. No publication relationships were supplied.

Both videos were copied unchanged: Project 1 is 3,134,174 bytes; Project 2 is 15,654,908 bytes. Both are H.264 MP4 with audio, 1280 × 720, embedded with controls and no autoplay or loop. Covers are 800-pixel-wide JPEG derivatives; Project 2's large microscope photographs have 2000-pixel-wide website derivatives. All original source files remain unchanged.

The existing Research section (`_portfolio/`, `/portfolio/`) remains for funded programs. Concrete builds belong to Projects (`_pages/projects/`, `/projects/`). Do not copy funded programs into Projects without evidence of a specific implementation and Lei's contribution.

## Source convention

Existing source structures are accepted; do not rename or reorganize them. For new material, one folder per project is convenient:

```text
My_project/
  descriptive-project-name/
    README.md
    cover.jpg
    images/
    media/
```

A Word document is also accepted in place of a README; read it completely and follow its media placeholders. The README can provide the official title, short summary, overview, prototype, implementation/setup, results, personal contributions, and captions. Identify the preferred cover and public media. Include related publication URLs only with explicit evidence of the relationship. Omit unsupported sections rather than filling them with guesses. Root-level material is allowed but its project association must be established before use.

## Updating from source

Ask: **Update my Projects page from My_project/.**

1. Run `python scripts/project_inventory.py` to compare source hashes with `_data/project_sources.json`. This command reads files only and does not install packages. New, changed, unchanged, and missing source groups are reported. An empty source folder does not authorize deleting website content.
2. Read only new/changed material and relevant existing project pages. Inspect images before choosing covers or writing captions. Ask about unknown contributions, image rights, or ambiguous associations when needed; do not invent facts.
3. Add/update one detail file per project at `_pages/projects/<stable-slug>.md`. Preserve its permalink and unrelated project files. Jekyll already includes `_pages/`; no collection/deployment configuration change is needed.
4. Copy approved media to `images/projects/<slug>/` or `files/projects/<slug>/`. Keep source files untouched. Preserve aspect ratio; use a reasonable card-sized derivative (usually 640–960 pixels wide) and larger detail images only when useful. Never enlarge images merely to meet a target. Inspect GIFs before converting them. Provide useful alt text and factual captions.
5. Review video size and browser compatibility before copying. The inventory flags files above 20 MiB for review; this is a conservative project policy, not a statement of GitHub limits. Do not commit large originals or use Git LFS automatically. Prefer an owner-provided external video link when appropriate. Never upload media to another host without authorization.
6. Set `featured: true` on up to six representative, documented projects. The homepage and Projects categories/cards discover pages automatically. Do not edit either listing for each new project.
7. Update that group's manifest entry only after review. Preserve other manifest records. Store the inventory's `files` hash mapping and the generated detail/media paths, plus any evidence for publication relationships.
8. Run `python -B _maintenance/verify_site.py` using an existing Python environment with PyYAML (on this computer: `D:\anaconda3\python.exe`). It checks front matter, routes, navigation, includes and media paths without building Jekyll. Review the diff and commit/push only when authorized. Never stage `My_CV/` or `My_project/` automatically.

## Detail page metadata

This is a schema example, not a publishable project. Replace every placeholder with supported source information; omit optional fields when unknown.

```yaml
---
layout: project
title: "Source-supported title"
permalink: /projects/stable-slug/
project: true
projects_ui: true
author_profile: true
summary: "One or two factual sentences."
project_order: 10
featured: true
project_category: "Sensors & Instrumentation"
cover: /images/projects/stable-slug/cover.jpg
cover_alt: "Description of the visible prototype"
cover_caption: "Optional source-supported caption"
show_cover: false # Omit/true to show a hero; false when the cover also appears at a source placeholder
media:
  - type: image
    src: /images/projects/stable-slug/setup.jpg
    alt: "Description of the setup"
    caption: "Optional factual caption"
  - type: video
    src: /files/projects/stable-slug/demo.mp4
    mime: video/mp4
    caption: "Demonstration"
  - type: external-video
    url: https://example.org/provided-video
    label: Watch demonstration
related_publications:
  - title: "Title of an explicitly related publication"
    url: /publication/existing-permalink
---
```

`project_category` is optional; omit it rather than supplying an empty string. Use only justified categories (for example Sensors & Instrumentation, Electronics, Embedded Systems, AI / Software, Personal Engineering Projects, or Research Projects). Categories appear only when used. `project_order` controls order; keep existing orders stable when adding a project. Images and GIFs use `type: image`; local videos use `type: video`; external videos are ordinary links, not autoplaying embeds.

Write supported sections in the Markdown body: Overview, System / Prototype, Experimental Setup / Implementation, Results / Demonstration, Key Contributions. For images beside a section, use Markdown figures or `{% include project-media.html items=page.setup_media %}` with a matching metadata list. Use `gallery=true` on the media include for adjacent image groups; images link to their larger website-facing copy. The layout adds the general Media and Related Publications sections only if data exists.

## Source manifest format

Each key is a folder relative to `My_project/` (or `.` for root files):

```json
{"version": 1, "projects": {"source-folder": {"files": {"README.md": "sha256-value"}, "outputs": ["_pages/projects/stable-slug.md", "images/projects/stable-slug/cover.jpg"], "publication_evidence": []}}}
```

Deleted source files are reported, never automatically deleted from the website. Validate and review publication evidence before writing links; matching topics alone are insufficient.

## Academic updates

Use the latest clearly identified CV in `My_CV/`; report conflicting versions instead of choosing solely by filename. Update `_publications/` while preserving existing full author lists and permalinks. Distinguish published, accepted, and under-review work; never put status text in a DOI field or invent dates. Update `_data/academic_service.yml` for reviewer changes: both homepage counts and detailed web-CV lists read this data. Keep homepage publication highlights concise and revisit their wording when status changes.

The currently downloadable `files/Lei-Peng-CV.pdf` is the earlier supplied PDF, not an export of the new Word CV. Replace it only with an approved current PDF or an explicitly requested, verified conversion. Do not infer doctoral graduation from the latest CV's `Ph. D` wording while its date range still ends in `Present`.
