---
abstract: The modelling framework of neural algorithmic reasoning (Veličković & Blundell,
  2021) postulates that a continuous neural network may learn to emulate the discrete
  reasoning steps of a symbolic algorithm. We investigate the underlying hypothesis
  in the most simple conceivable scenario – the addition of real numbers. Our results
  show that two layer neural networks fail to learn the structure of the task, despite
  containing multiple solutions of the true function within their hypothesis class.
  Growing the network’s width leads to highly complex error regions in the input space.
  Moreover, we find that the network fails to generalise with increasing severity
  i) in the training domain, ii) outside of the training domain but within its convex
  hull, and iii) outside the training domain’s convex hull. This behaviour can be
  emulated with Gaussian process regressors that use radial basis function kernels
  of decreasing length scale. Classical results establish an equivalence between Gaussian
  processes and infinitely wide neural networks. We demonstrate a tight linkage between
  the scaling of a network weights’ standard deviation and its effective length scale
  on a sinusoidal regression problem, suggesting simple modifications to control the
  length scale of the function learned by a neural network and, thus, its smoothness.
  This has important applications for the different generalisation scenarios suggested
  above, but it also suggests a partial remedy to the brittleness of neural network
  predictions as exposed by adversarial examples. We demonstrate the gains in adversarial
  robustness that our modification achieves on a standard classification problem of
  handwritten …
authors: David Klindt
citations: 4
journal: ''
layout: publication
scholar_url: https://openreview.net/forum?id=JnsGy9uWtI
title: Controlling neural network smoothness for neural algorithmic reasoning
year: 2023
---

The modelling framework of neural algorithmic reasoning (Veličković & Blundell, 2021) postulates that a continuous neural network may learn to emulate the discrete reasoning steps of a symbolic algorithm. We investigate the underlying hypothesis in the most simple conceivable scenario – the addition of real numbers. Our results show that two layer neural networks fail to learn the structure of the task, despite containing multiple solutions of the true function within their hypothesis class. Growing the network’s width leads to highly complex error regions in the input space. Moreover, we find that the network fails to generalise with increasing severity i) in the training domain, ii) outside of the training domain but within its convex hull, and iii) outside the training domain’s convex hull. This behaviour can be emulated with Gaussian process regressors that use radial basis function kernels of decreasing length scale. Classical results establish an equivalence between Gaussian processes and infinitely wide neural networks. We demonstrate a tight linkage between the scaling of a network weights’ standard deviation and its effective length scale on a sinusoidal regression problem, suggesting simple modifications to control the length scale of the function learned by a neural network and, thus, its smoothness. This has important applications for the different generalisation scenarios suggested above, but it also suggests a partial remedy to the brittleness of neural network predictions as exposed by adversarial examples. We demonstrate the gains in adversarial robustness that our modification achieves on a standard classification problem of handwritten …
