---
abstract: The rapid advancement of generative AI enables highly realistic synthetic
  videos, posing significant challenges for content authentication and raising urgent
  concerns about misuse. Existing detection methods often struggle with generalization
  and capturing subtle temporal inconsistencies. We propose ReStraV(Representation
  Straightening Video), a novel approach to distinguish natural from AI-generated
  videos. Inspired by the "perceptual straightening" hypothesis -- which suggests
  real-world video trajectories become more straight in neural representation domain
  -- we analyze deviations from this expected geometric property. Using a pre-trained
  self-supervised vision transformer (DINOv2), we quantify the temporal curvature
  and stepwise distance in the model's representation domain. We aggregate statistics
  of these measures for each video and train a classifier. Our analysis shows that
  AI-generated videos exhibit significantly different curvature and distance patterns
  compared to real videos. A lightweight classifier achieves state-of-the-art detection
  performance (e.g., 97.17% accuracy and 98.63% AUROC on the VidProM benchmark), substantially
  outperforming existing image- and video-based methods. ReStraV is computationally
  efficient, it is offering a low-cost and effective detection solution. This work
  provides new insights into using neural representation geometry for AI-generated
  video detection.
authors: Christian Internò and Robert Geirhos and Markus Olhofer and Sunny Liu and
  Barbara Hammer and David Klindt
citations: 0
journal: ''
layout: publication
scholar_url: https://arxiv.org/abs/2507.00583
title: AI-Generated Video Detection via Perceptual Straightening
year: 2025
---

The rapid advancement of generative AI enables highly realistic synthetic videos, posing significant challenges for content authentication and raising urgent concerns about misuse. Existing detection methods often struggle with generalization and capturing subtle temporal inconsistencies. We propose ReStraV(Representation Straightening Video), a novel approach to distinguish natural from AI-generated videos. Inspired by the "perceptual straightening" hypothesis -- which suggests real-world video trajectories become more straight in neural representation domain -- we analyze deviations from this expected geometric property. Using a pre-trained self-supervised vision transformer (DINOv2), we quantify the temporal curvature and stepwise distance in the model's representation domain. We aggregate statistics of these measures for each video and train a classifier. Our analysis shows that AI-generated videos exhibit significantly different curvature and distance patterns compared to real videos. A lightweight classifier achieves state-of-the-art detection performance (e.g., 97.17% accuracy and 98.63% AUROC on the VidProM benchmark), substantially outperforming existing image- and video-based methods. ReStraV is computationally efficient, it is offering a low-cost and effective detection solution. This work provides new insights into using neural representation geometry for AI-generated video detection.
