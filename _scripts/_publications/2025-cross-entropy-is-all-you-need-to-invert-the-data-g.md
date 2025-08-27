---
abstract: Supervised learning has become a cornerstone of modern machine learning,
  yet a comprehensive theory explaining its effectiveness remains elusive. Empirical
  phenomena, such as neural analogy-making and the linear representation hypothesis,
  suggest that supervised models can learn interpretable factors of variation in a
  linear fashion. Recent advances in self-supervised learning, particularly nonlinear
  Independent Component Analysis, have shown that these methods can recover latent
  structures by inverting the data generating process. We extend these identifiability
  results to parametric instance discrimination, then show how insights transfer to
  the ubiquitous setting of supervised learning with cross-entropy minimization. We
  prove that even in standard classification tasks, models learn representations of
  ground-truth factors of variation up to a linear transformation. We corroborate
  our theoretical contribution with a series of empirical studies. First, using simulated
  data matching our theoretical assumptions, we demonstrate successful disentanglement
  of latent factors. Second, we show that on DisLib, a widely-used disentanglement
  benchmark, simple classification tasks recover latent structures up to linear transformations.
  Finally, we reveal that models trained on ImageNet encode representations that permit
  linear decoding of proxy factors of variation. Together, our theoretical findings
  and experiments offer a compelling explanation for recent observations of linear
  representations, such as superposition in neural networks. This work takes a significant
  step toward a cohesive theory that accounts for the unreasonable effectiveness of
  …
authors: Patrik Reizinger and Alice Bizeul and Attila Juhos and Julia E Vogt and Randall
  Balestriero and Wieland Brendel and David Klindt
citations: 7
journal: ''
layout: publication
title: Cross-Entropy Is All You Need To Invert the Data Generating Process
url: https://arxiv.org/abs/2410.21869
year: 2025
---

Supervised learning has become a cornerstone of modern machine learning, yet a comprehensive theory explaining its effectiveness remains elusive. Empirical phenomena, such as neural analogy-making and the linear representation hypothesis, suggest that supervised models can learn interpretable factors of variation in a linear fashion. Recent advances in self-supervised learning, particularly nonlinear Independent Component Analysis, have shown that these methods can recover latent structures by inverting the data generating process. We extend these identifiability results to parametric instance discrimination, then show how insights transfer to the ubiquitous setting of supervised learning with cross-entropy minimization. We prove that even in standard classification tasks, models learn representations of ground-truth factors of variation up to a linear transformation. We corroborate our theoretical contribution with a series of empirical studies. First, using simulated data matching our theoretical assumptions, we demonstrate successful disentanglement of latent factors. Second, we show that on DisLib, a widely-used disentanglement benchmark, simple classification tasks recover latent structures up to linear transformations. Finally, we reveal that models trained on ImageNet encode representations that permit linear decoding of proxy factors of variation. Together, our theoretical findings and experiments offer a compelling explanation for recent observations of linear representations, such as superposition in neural networks. This work takes a significant step toward a cohesive theory that accounts for the unreasonable effectiveness of …
