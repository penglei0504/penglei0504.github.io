---
permalink: /
title: "Lei Peng, Ph.D."
author_profile: true
projects_ui: true
redirect_from: 
  - /about/
  - /about.html
---

I am a Postdoctoral Research Associate in the Department of Electrical and Computer Engineering at Michigan State University, where I also serve as Lab Manager of Nondestructive Evaluation Lab. I hold a Ph.D. in Electrical and Computer Engineering from Michigan State University. My research focuses on electromagnetic sensing and nondestructive evaluation, with applications in metal additive manufacturing, pipeline inspection, and railway infrastructure.

My work includes flexible and stretchable sensor arrays, in-situ temperature monitoring, and learning-based methods for defect detection and characterization. Before joining MSU in 2021, I studied Electrical and Electronic Engineering at ShanghaiTech University and held research and engineering positions in academia and industry.

## Research Interests

- Electromagnetic sensing and nondestructive evaluation.
- Flexible and stretchable sensor arrays for complex geometries.
- In-situ monitoring of metal additive manufacturing processes.
- Pipeline and rail inspection, including hydrogen pipeline integrity.
- Learning-based defect detection and characterization.

{% assign featured_projects = site.pages | where: "project", true | where: "featured", true | sort: "project_order" %}
{% if featured_projects.size > 0 %}
## Featured Projects

<div class="homepage-featured">
{% include project-cards.html projects=featured_projects limit=6 %}
</div>

[View all projects]({{ site.baseurl }}/projects/)
{% endif %}

## Publications

My publications focus on electromagnetic sensing, sensor arrays, and nondestructive evaluation. Recent work includes flexible MFL arrays for bent-pipe inspection and a shape-reconstruction technique using flexible differential inductive sensor arrays, accepted in September 2026.

[Full publication list]({{ site.baseurl }}/publications/) · [Google Scholar]({{ site.author.googlescholar }})

## Collaborators

<div class="collaborator-logos">
  <div><img src="{{ site.baseurl }}/images/logos/llnl.png" alt="Lawrence Livermore National Laboratory" loading="lazy" decoding="async"></div>
  <div><img src="{{ site.baseurl }}/images/logos/asu.png" alt="Arizona State University" loading="lazy" decoding="async"></div>
  <div><img src="{{ site.baseurl }}/images/logos/msu-smart.png" alt="MSU SMART Lab" loading="lazy" decoding="async"></div>
  <div><img src="{{ site.baseurl }}/images/logos/msu-puma.png" alt="MSU Physical Ultrasonics, Microscopy and Acoustics (PUMA) Lab" loading="lazy" decoding="async"></div>
</div>
