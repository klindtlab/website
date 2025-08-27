---
abstract: Neural system identification aims at learning the response function of neurons
  to arbitrary stimuli using experimentally recorded data, but typically does not
  leverage normative principles such as efficient coding of natural environments.
  Visual systems, however, have evolved to efficiently process input from the natural
  environment. Here, we present a normative network regularization for system identification
  models by incorporating, as a regularizer, the efficient coding hypothesis, which
  states that neural response properties of sensory representations are strongly shaped
  by the need to preserve most of the stimulus information with limited resources.
  Using this approach, we explored if a system identification model can be improved
  by sharing its convolutional filters with those of an autoencoder which aims to
  efficiently encode natural stimuli. To this end, we built a hybrid model to predict
  the responses of retinal neurons to noise stimuli. This approach did not only yield
  a higher performance than the “stand-alone” system identification model, it also
  produced more biologically plausible filters, meaning that they more closely resembled
  neural representation in early visual systems. We found these results applied to
  retinal responses to different artificial stimuli and across model architectures.
  Moreover, our normatively regularized model performed particularly well in predicting
  responses of direction-of-motion sensitive retinal neurons. The benefit of natural
  scene statistics became marginal, however, for predicting the responses to natural
  movies. In summary, our results indicate that efficiently encoding environmental
  inputs can improve system …
authors: Yongrong Qiu and David Klindt and Klaudia P Szatko and Dominic Gonschorek
  and Larissa Hoefling and Timm Schubert and Laura Busse and Matthias Bethge and Thomas
  Euler
citations: 11
journal: ''
layout: publication
scholar_url: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011037
title: Efficient coding of natural scenes improves neural system identification
year: 2023
---

Neural system identification aims at learning the response function of neurons to arbitrary stimuli using experimentally recorded data, but typically does not leverage normative principles such as efficient coding of natural environments. Visual systems, however, have evolved to efficiently process input from the natural environment. Here, we present a normative network regularization for system identification models by incorporating, as a regularizer, the efficient coding hypothesis, which states that neural response properties of sensory representations are strongly shaped by the need to preserve most of the stimulus information with limited resources. Using this approach, we explored if a system identification model can be improved by sharing its convolutional filters with those of an autoencoder which aims to efficiently encode natural stimuli. To this end, we built a hybrid model to predict the responses of retinal neurons to noise stimuli. This approach did not only yield a higher performance than the “stand-alone” system identification model, it also produced more biologically plausible filters, meaning that they more closely resembled neural representation in early visual systems. We found these results applied to retinal responses to different artificial stimuli and across model architectures. Moreover, our normatively regularized model performed particularly well in predicting responses of direction-of-motion sensitive retinal neurons. The benefit of natural scene statistics became marginal, however, for predicting the responses to natural movies. In summary, our results indicate that efficiently encoding environmental inputs can improve system …
