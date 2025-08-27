---
layout: home
title: "Welcome to Klindt Lab"
---

<div class="hero-section">
  <div class="hero-content">
    <div class="hero-text">
      <h1>NeuroAI Research at Klindt Lab</h1>
      <p class="hero-description">We explore the fascinating intersection of neuroscience and artificial intelligence, developing computational models to understand how the brain processes information and how AI systems can be inspired by neural mechanisms.</p>
      <div class="hero-buttons">
        <a href="{{ '/research/' | relative_url }}" class="btn btn-primary">Our Research</a>
        <a href="{{ '/team/' | relative_url }}" class="btn btn-secondary">Meet the Team</a>
      </div>
    </div>
    <div class="hero-image">
      <img src="{{ site.baseurl }}/assets/images/team/summer2025.jpeg" alt="Klindt Lab Team" class="team-photo">
      <p class="photo-caption">The Klindt Lab Team</p>
    </div>
  </div>
</div>

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