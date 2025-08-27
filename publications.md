---
layout: page
title: Publications
permalink: /publications/
---

# Publications

*Publications are automatically updated from Google Scholar*

{% assign years = site.publications | map: 'year' | uniq | sort | reverse %}

{% for year in years %}
## {{ year }}

{% for pub in site.publications %}
  {% if pub.year == year %}
  ### {{ pub.title }}
  **{{ pub.authors }}**  
  {% if pub.journal %}*{{ pub.journal }}* ({{ pub.year }}){% endif %}
  
  {% if pub.abstract %}
  <details>
  <summary>Abstract</summary>
  {{ pub.abstract }}
  </details>
  {% endif %}
  
  {% if pub.citations %}**Citations**: {{ pub.citations }}{% endif %}
  
  **Links**: 
  {% if pub.url %}[Google Scholar]({{ pub.url }}){% endif %}
  {% if pub.pdf %} • [PDF]({{ pub.pdf }}){% endif %}
  {% if pub.doi %} • [DOI](https://doi.org/{{ pub.doi }}){% endif %}
  {% if pub.arxiv %} • [arXiv](https://arxiv.org/abs/{{ pub.arxiv }}){% endif %}
  {% if pub.code %} • [Code]({{ pub.code }}){% endif %}
  
  ---
  {% endif %}
{% endfor %}
{% endfor %}

{% if site.publications.size == 0 %}
No publications found. Publications will be automatically updated from Google Scholar.

To set up automatic updates:
1. Find your Google Scholar profile ID
2. Update `SCHOLAR_ID` in `_scripts/update_publications.py`
3. Run the update script or wait for the weekly GitHub Action
{% endif %}