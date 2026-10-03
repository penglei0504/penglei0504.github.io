---
permalink: /
title: "Lei Peng"
author_profile: true
projects_ui: true
redirect_from: 
  - /about/
  - /about.html
---

<p><a href="{{ site.baseurl }}/files/Lei-Peng-CV.pdf" class="btn btn--primary">Download CV (PDF)</a></p>


I hold a Ph.D. in Electrical and Computer Engineering from Michigan State University, where I am a Research Assistant. My research focuses on electromagnetic sensing and nondestructive evaluation, with applications in metal additive manufacturing, pipeline inspection, and railway infrastructure.

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

{% include project-cards.html projects=featured_projects limit=6 %}

[View all projects]({{ site.baseurl }}/projects/)
{% endif %}

## Publications

My publications focus on electromagnetic sensing, sensor arrays, and nondestructive evaluation. Recent work includes flexible MFL arrays for bent-pipe inspection and a shape-reconstruction technique using flexible differential inductive sensor arrays, accepted in September 2026.

[Full publication list]({{ site.baseurl }}/publications/) · [Google Scholar]({{ site.author.googlescholar }})

## Academic Service

I have served as a reviewer for {{ site.data.academic_service.journals.size }} journals, including *Engineering Applications of Artificial Intelligence*, *IEEE Transactions on Instrumentation and Measurement*, and *NDT&E International*, and for {{ site.data.academic_service.conferences.size }} conferences.

[Full reviewer service]({{ site.baseurl }}/cv/#academic-service)
