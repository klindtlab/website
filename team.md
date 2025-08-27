---
layout: page
title: Team
permalink: /team/
---

# Lab Members

## Principal Investigator

{% for member in site.team %}
  {% if member.role == "PI" %}
  ### {{ member.name }}
  **{{ member.title }}**
  
  {{ member.bio }}
  
  **Contact**: {{ member.email }}
  
  {% if member.website %}[Personal Website]({{ member.website }}){% endif %}
  {% if member.twitter %}[Twitter](https://twitter.com/{{ member.twitter }}){% endif %}
  {% if member.github %}[GitHub](https://github.com/{{ member.github }}){% endif %}
  {% endif %}
{% endfor %}

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