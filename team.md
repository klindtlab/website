---
layout: page
title: Team
permalink: /team/
---

<style>
.team-photo {
  width: 150px !important;
  height: 150px !important;
  max-width: 150px !important;
  max-height: 150px !important;
  min-width: 150px !important;
  min-height: 150px !important;
  border-radius: 50% !important;
  object-fit: cover !important;
  object-position: center !important;
  margin-bottom: 1rem !important;
  border: 3px solid white !important;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1) !important;
  display: block !important;
  margin-left: auto !important;
  margin-right: auto !important;
}
</style>

# Lab Members

## Principal Investigator

<div class="team-grid">
{% for member in site.team %}
  {% if member.role == "PI" %}
  <div class="team-member">
    {% if member.image %}
      <img src="{{ member.image | relative_url }}" alt="{{ member.name }}" class="team-photo">
    {% endif %}
    <h3><a href="{{ member.url | relative_url }}">{{ member.name }}</a></h3>
    <p class="member-title">{{ member.title }}</p>
    <p class="member-email">{{ member.email }}</p>
    
    <div class="member-links">
      {% if member.website %}
        <a href="{{ member.website }}" target="_blank" class="member-link">Website</a>
      {% endif %}
      {% if member.github %}
        <a href="https://github.com/{{ member.github }}" target="_blank" class="member-link">GitHub</a>
      {% endif %}
      {% if member.twitter %}
        <a href="https://twitter.com/{{ member.twitter }}" target="_blank" class="member-link">Twitter</a>
      {% endif %}
    </div>
  </div>
  {% endif %}
{% endfor %}
</div>

## Postdoctoral Researchers

<div class="team-grid">
{% for member in site.team %}
  {% if member.role == "Postdoc" %}
  <div class="team-member">
    {% if member.image %}
      <img src="{{ member.image | relative_url }}" alt="{{ member.name }}" class="team-photo">
    {% endif %}
    <h3><a href="{{ member.url | relative_url }}">{{ member.name }}</a></h3>
    <p class="member-title">{{ member.title }}</p>
    <p class="member-email">{{ member.email }}</p>
    
    <div class="member-links">
      {% if member.website %}
        <a href="{{ member.website }}" target="_blank" class="member-link">Website</a>
      {% endif %}
      {% if member.github %}
        <a href="https://github.com/{{ member.github }}" target="_blank" class="member-link">GitHub</a>
      {% endif %}
    </div>
  </div>
  {% endif %}
{% endfor %}
</div>

## Staff

<div class="team-grid">
{% for member in site.team %}
  {% if member.role == "Staff" %}
  <div class="team-member">
    {% if member.image %}
      <img src="{{ member.image | relative_url }}" alt="{{ member.name }}" class="team-photo">
    {% endif %}
    <h3><a href="{{ member.url | relative_url }}">{{ member.name }}</a></h3>
    <p class="member-title">{{ member.title }}</p>
    <p class="member-email">{{ member.email }}</p>
    
    <div class="member-links">
      {% if member.website %}
        <a href="{{ member.website }}" target="_blank" class="member-link">Website</a>
      {% endif %}
      {% if member.github %}
        <a href="https://github.com/{{ member.github }}" target="_blank" class="member-link">GitHub</a>
      {% endif %}
    </div>
  </div>
  {% endif %}
{% endfor %}
</div>

## Graduate Students

<div class="team-grid">
{% for member in site.team %}
  {% if member.role == "Graduate" %}
  <div class="team-member">
    {% if member.image %}
      <img src="{{ member.image | relative_url }}" alt="{{ member.name }}" class="team-photo">
    {% endif %}
    <h3><a href="{{ member.url | relative_url }}">{{ member.name }}</a></h3>
    <p class="member-title">{{ member.title }}</p>
    <p class="member-email">{{ member.email }}</p>
  </div>
  {% endif %}
{% endfor %}
</div>

## Undergraduate Students

{% for member in site.team %}
  {% if member.role == "Undergraduate" %}
  ### {{ member.name }}
  {{ member.bio }}
  {% endif %}
{% endfor %}

## Alumni

{% for member in site.team %}
  {% if member.role == "Alumni" %}
  ### {{ member.name }}
  {{ member.bio }}
  
  **Current Position**: {{ member.current_position }}
  {% endif %}
{% endfor %}

---

## Join Us

We are always looking for motivated researchers to join our team. If you're interested in computational neuroscience and NeuroAI research, please get in touch!

**Open Positions:**
- [List any current openings]

**For prospective students and postdocs:**
Please email us with your CV and a brief description of your research interests.