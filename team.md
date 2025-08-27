---
layout: page
title: Team
permalink: /team/
---

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

{% for member in site.team %}
  {% if member.role == "Postdoc" %}
  ### {{ member.name }}
  {{ member.bio }}
  
  **Email**: {{ member.email }}
  {% endif %}
{% endfor %}

## Graduate Students

{% for member in site.team %}
  {% if member.role == "Graduate" %}
  ### {{ member.name }}
  {{ member.bio }}
  
  **Email**: {{ member.email }}
  {% endif %}
{% endfor %}

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