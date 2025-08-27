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
  <div class="publication-item">
    <h3><a href="{{ pub.url | relative_url }}">{{ pub.title }}</a></h3>
    <p class="authors">{{ pub.authors }}</p>
    {% if pub.journal %}
      <p class="journal"><em>{{ pub.journal }}</em> ({{ pub.year }})</p>
    {% endif %}
    
    {% if pub.abstract %}
    <details class="abstract-toggle">
      <summary>Abstract</summary>
      <p>{{ pub.abstract }}</p>
    </details>
    {% endif %}
    
    {% if pub.citations %}
      <p class="citations"><strong>Citations</strong>: {{ pub.citations }}</p>
    {% endif %}
    
    <div class="pub-links">
      {% if pub.scholar_url %}
        <a href="{{ pub.scholar_url }}" target="_blank">Google Scholar</a>
      {% endif %}
      {% if pub.pdf %}
        <a href="{{ pub.pdf }}" target="_blank">PDF</a>
      {% endif %}
      {% if pub.doi %}
        <a href="https://doi.org/{{ pub.doi }}" target="_blank">DOI</a>
      {% endif %}
      {% if pub.arxiv %}
        <a href="https://arxiv.org/abs/{{ pub.arxiv }}" target="_blank">arXiv</a>
      {% endif %}
      {% if pub.code %}
        <a href="{{ pub.code }}" target="_blank">Code</a>
      {% endif %}
    </div>
  </div>
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