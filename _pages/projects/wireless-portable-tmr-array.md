---
layout: "project"
title: "Wireless Portable TMR Array for Eddy Current Imaging"
permalink: "/projects/wireless-portable-tmr-array/"
project: true
projects_ui: true
author_profile: true
summary: "A compact wireless eddy current imaging probe combining a 64-element bare-die TMR array with excitation, acquisition, embedded control, and battery power."
project_order: 20
featured: true
project_category: "Sensors & Instrumentation"
cover: "/images/projects/wireless-portable-tmr-array/cover.jpg"
cover_alt: "Enclosed wireless TMR array probe."
show_cover: false
sensor_media: [{"type": "image", "src": "/images/projects/wireless-portable-tmr-array/tmr-sensor-detail.jpg", "alt": "Close-up of TMR sensing elements and bond wires."}, {"type": "image", "src": "/images/projects/wireless-portable-tmr-array/tmr-array-interconnections.jpg", "alt": "TMR array and its interconnections."}]
probe_media: [{"type": "image", "src": "/images/projects/wireless-portable-tmr-array/wireless-probe.jpg", "alt": "Enclosed wireless TMR array probe."}]
demonstration_media: [{"type": "video", "src": "/files/projects/wireless-portable-tmr-array/demonstration.mp4", "mime": "video/mp4", "poster": "/images/projects/wireless-portable-tmr-array/cover.jpg"}]
---

## Motivation

High-sensitivity and high-resolution eddy current imaging is increasingly important for the detection and characterization of small defects in conductive structures. Conventional coil-based eddy current probes are widely used, but achieving a high-density sensing array can become challenging because the spatial resolution is directly constrained by the physical dimensions of the sensing coils. In addition, conventional probes often rely on external signal generators, data acquisition systems, and wired connections, which can increase the size and complexity of the overall inspection setup.

These limitations are particularly important for field inspection, where compact size, portability, wireless operation, and dense spatial sampling can significantly improve inspection flexibility. To address these challenges, a compact wireless eddy current imaging probe was developed using a high-density array of tunnel magnetoresistance (TMR) sensors. The system combines magnetic field sensing, excitation generation, signal conditioning, embedded data acquisition, wireless communication, and battery power within a fully integrated portable platform.

## High-Density TMR Array for Eddy Current Imaging

{% include project-media.html items=page.sensor_media gallery=true %}

The sensing core of the probe consists of a 64-element bare-die TMR sensor array. Each sensing element has a footprint of only approximately 0.5 mm × 0.5 mm, enabling a densely distributed magnetic sensing array within a very small area. The compact sensor dimensions provide a strong foundation for high-spatial-resolution eddy current imaging.

Unlike conventional inductive coils, TMR sensors directly measure magnetic field variations and maintain high sensitivity at relatively low frequencies. This characteristic is particularly attractive for low-frequency eddy current testing, where increased electromagnetic penetration depth is often required while the induced magnetic field variations may become relatively weak. The high magnetic sensitivity of the TMR elements therefore enables the probe to capture spatial variations in the eddy-current-induced magnetic field with a dense sensor arrangement.

By combining the 64 sensing elements with multiplexed signal acquisition, the probe can generate high-resolution magnetic field maps and eddy current images for defect visualization. The architecture also avoids the need to construct a large number of miniature receiving coils, making it possible to achieve a much higher sensing density within a compact probe footprint.

## Fully Integrated Portable and Wireless Probe

{% include project-media.html items=page.probe_media %}

Rather than operating as a sensor array connected to multiple external instruments, the probe was designed as a self-contained embedded NDE system. A microcontroller-based architecture coordinates sensor multiplexing, excitation control, data acquisition, signal processing, and wireless communication. The integrated electronics include a multiplexer network, analog filtering and amplification circuits, programmable excitation generation, embedded analog-to-digital acquisition, wireless communication, power management, and battery supply.

These modules are integrated directly into the probe, substantially reducing dependence on external instrumentation. Even with the battery and complete electronic system included, the overall probe is only approximately 10 cm × 5 cm × 5 cm, making the system compact and portable. Wireless communication further removes the requirement for continuous signal cables between the probe and the host computer, allowing acquired array data and imaging results to be transferred remotely.

This highly integrated architecture transforms the TMR array from an individual sensing component into a complete portable eddy current imaging instrument, combining sensor design, analog electronics, embedded control, data acquisition, and wireless communication within a single platform.

{% include project-media.html items=page.demonstration_media %}

## Robotic Integration and Intelligent Inspection

Future development could further incorporate edge AI and onboard intelligent processing. Rather than transmitting all raw 64-channel measurements to an external computer, embedded processing hardware could perform image reconstruction, defect detection, noise suppression, and feature extraction directly on the probe or robotic platform. Combined with automated motion control, this could enable real-time defect localization and adaptive scanning, where the inspection system automatically performs more detailed measurements around suspicious regions.

Ultimately, the platform could evolve into a compact intelligent electromagnetic imaging system that combines high-density TMR sensing, low-frequency eddy current inspection, wireless instrumentation, robotic deployment, and edge intelligence. Such an architecture provides a promising pathway toward portable and autonomous high-resolution NDE for pipelines, industrial components, and structures with limited inspection access.
