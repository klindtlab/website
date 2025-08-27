---
abstract: While the impressive performance of modern neural networks is often attributed
  to their capacity to efficiently extract task-relevant features from data, the mechanisms
  underlying this rich feature learning regime remain elusive, with much of our theoretical
  understanding stemming from the opposing lazy regime. In this work, we derive exact
  solutions to a minimal model that transitions between lazy and rich learning, precisely
  elucidating how unbalanced layer-specific initialization variances and learning
  rates determine the degree of feature learning. Our analysis reveals that they conspire
  to influence the learning regime through a set of conserved quantities that constrain
  and modify the geometry of learning trajectories in parameter and function space.
  We extend our analysis to more complex linear models with multiple neurons, outputs,
  and layers and to shallow nonlinear networks with piecewise linear activation functions.
  In linear networks, rapid feature learning only occurs from balanced initializations,
  where all layers learn at similar speeds. While in nonlinear networks, unbalanced
  initializations that promote faster learning in earlier layers can accelerate rich
  learning. Through a series of experiments, we provide evidence that this unbalanced
  rich regime drives feature learning in deep finite-width networks, promotes interpretability
  of early layers in CNNs, reduces the sample complexity of learning hierarchical
  data, and decreases the time to grokking in modular arithmetic. Our theory motivates
  further exploration of unbalanced initializations to enhance efficient feature learning.
authors: Daniel Kunin and Allan Raventós and Clémentine Dominé and Feng Chen and David
  Klindt and Andrew Saxe and Surya Ganguli
citations: 23
journal: ''
layout: publication
scholar_url: https://proceedings.neurips.cc/paper_files/paper/2024/hash/94074dd5a072d28ff75a76dabed43767-Abstract-Conference.html
title: 'Get rich quick: exact solutions reveal how unbalanced initializations promote
  rapid feature learning'
year: 2024
---

While the impressive performance of modern neural networks is often attributed to their capacity to efficiently extract task-relevant features from data, the mechanisms underlying this rich feature learning regime remain elusive, with much of our theoretical understanding stemming from the opposing lazy regime. In this work, we derive exact solutions to a minimal model that transitions between lazy and rich learning, precisely elucidating how unbalanced layer-specific initialization variances and learning rates determine the degree of feature learning. Our analysis reveals that they conspire to influence the learning regime through a set of conserved quantities that constrain and modify the geometry of learning trajectories in parameter and function space. We extend our analysis to more complex linear models with multiple neurons, outputs, and layers and to shallow nonlinear networks with piecewise linear activation functions. In linear networks, rapid feature learning only occurs from balanced initializations, where all layers learn at similar speeds. While in nonlinear networks, unbalanced initializations that promote faster learning in earlier layers can accelerate rich learning. Through a series of experiments, we provide evidence that this unbalanced rich regime drives feature learning in deep finite-width networks, promotes interpretability of early layers in CNNs, reduces the sample complexity of learning hierarchical data, and decreases the time to grokking in modular arithmetic. Our theory motivates further exploration of unbalanced initializations to enhance efficient feature learning.
