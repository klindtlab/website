---
layout: home
title: "Welcome to Klindt Lab"
---

# NeuroAI Research at Klindt Lab

We explore the fascinating intersection of neuroscience and artificial intelligence, developing computational models to understand how the brain processes information and how AI systems can be inspired by neural mechanisms.

## Latest News

{% for post in site.news limit:3 %}
- **{{ post.date | date: "%B %d, %Y" }}**: [{{ post.title }}]({{ post.url }})
{% endfor %}

[View all news →](news.html)

## Research Highlights

Our research focuses on:
- Neural circuit modeling
- Machine learning inspired by neuroscience
- Computational theories of perception
- Deep learning interpretability

[Learn more about our research →](research.html)

## Recent Publications

{% for pub in site.publications limit:5 %}
- {{ pub.title }} ({{ pub.year }}) - {{ pub.journal }}
{% endfor %}

[View all publications →](publications.html)