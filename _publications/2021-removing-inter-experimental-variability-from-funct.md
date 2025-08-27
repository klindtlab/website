---
abstract: Integrating data from multiple experiments is common practice in systems
  neuroscience but it requires inter-experimental variability to be negligible compared
  to the biological signal of interest. This requirement is rarely fulfilled; systematic
  changes between experiments can drastically affect the outcome of complex analysis
  pipelines. Modern machine learning approaches designed to adapt models across multiple
  data domains offer flexible ways of removing inter-experimental variability where
  classical statistical methods often fail. While applications of these methods have
  been mostly limited to single-cell genomics, in this work, we develop a theoretical
  framework for domain adaptation in systems neuroscience. We implement this in an
  adversarial optimization scheme that removes inter-experimental variability while
  preserving the biological signal. We compare our method to previous approaches on
  a large-scale dataset of two-photon imaging recordings of retinal bipolar cell responses
  to visual stimuli. This dataset provides a unique benchmark as it contains biological
  signal from well-defined cell types that is obscured by large inter-experimental
  variability. In a supervised setting, we compare the generalization performance
  of cell type classifiers across experiments, which we validate with anatomical cell
  type distributions from electron microscopy data. In an unsupervised setting, we
  remove inter-experimental variability from the data which can then be fed into arbitrary
  downstream analyses. In both settings, we find that our method achieves the best
  trade-off between removing inter-experimental variability and preserving biological
  signal …
authors: Dominic Gonschorek and Larissa Höfling and Klaudia P Szatko and Katrin Franke
  and Timm Schubert and Benjamin Dunn and Philipp Berens and David Klindt and Thomas
  Euler
citations: 12
journal: ''
layout: publication
scholar_url: https://proceedings.neurips.cc/paper_files/paper/2021/hash/1e5eeb40a3fce716b244599862fd2200-Abstract.html
title: Removing inter-experimental variability from functional data in systems neuroscience
year: 2021
---

Integrating data from multiple experiments is common practice in systems neuroscience but it requires inter-experimental variability to be negligible compared to the biological signal of interest. This requirement is rarely fulfilled; systematic changes between experiments can drastically affect the outcome of complex analysis pipelines. Modern machine learning approaches designed to adapt models across multiple data domains offer flexible ways of removing inter-experimental variability where classical statistical methods often fail. While applications of these methods have been mostly limited to single-cell genomics, in this work, we develop a theoretical framework for domain adaptation in systems neuroscience. We implement this in an adversarial optimization scheme that removes inter-experimental variability while preserving the biological signal. We compare our method to previous approaches on a large-scale dataset of two-photon imaging recordings of retinal bipolar cell responses to visual stimuli. This dataset provides a unique benchmark as it contains biological signal from well-defined cell types that is obscured by large inter-experimental variability. In a supervised setting, we compare the generalization performance of cell type classifiers across experiments, which we validate with anatomical cell type distributions from electron microscopy data. In an unsupervised setting, we remove inter-experimental variability from the data which can then be fed into arbitrary downstream analyses. In both settings, we find that our method achieves the best trade-off between removing inter-experimental variability and preserving biological signal …
