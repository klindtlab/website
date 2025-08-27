---
layout: page
title: News
permalink: /news/
---

# Lab News

{% for post in site.news %}
## {{ post.title }}
*{{ post.date | date: "%B %d, %Y" }}*

{{ post.excerpt }}

[Read more →]({{ post.url }})

---
{% endfor %}

{% if site.news.size == 0 %}
No news posts yet. Check back soon for updates!
{% endif %}