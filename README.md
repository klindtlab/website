# Klindt Lab Website

A Jekyll-based website for the Klindt Lab NeuroAI research group.

## Features

- **Automatic Publication Updates**: Pulls latest publications from Google Scholar
- **News/Blog System**: Easy-to-update lab news and announcements
- **Team Profiles**: Individual pages for lab members
- **Responsive Design**: Mobile-friendly layout
- **GitHub Pages Ready**: Deploys automatically

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install dependencies**
   ```bash
   bundle install
   ```

3. **Run locally**
   ```bash
   bundle exec jekyll serve
   ```
   
   Visit `http://localhost:4000` to view the site.

## Configuration

### Google Scholar Integration
1. Update `_scripts/update_publications.py` with your Google Scholar ID
2. Install Python dependencies: `pip install -r requirements.txt`
3. Run manually: `python _scripts/update_publications.py`
4. Or wait for the weekly GitHub Action to run automatically

### Adding Team Members
Create a new file in `_team/` directory:

```yaml
---
layout: person
name: "Your Name"
role: "PI" # or "Postdoc", "Graduate", "Undergraduate", "Alumni"
title: "Your Title"
email: "your.email@example.org"
website: "https://yourwebsite.com"
github: "yourgithub"
twitter: "yourtwitter"
image: "/assets/images/team/your-photo.jpg"
---

Your bio content here...
```

### Adding News Posts
Create a new file in `_news/` directory:

```yaml
---
layout: post
title: "Your News Title"
date: 2024-08-27
excerpt: "Brief excerpt of the news item."
---

Your news content here...
```

## Customization

- **Colors**: Edit CSS variables in `assets/css/style.scss`
- **Navigation**: Update `header_pages` in `_config.yml`
- **Contact Info**: Update social links in `_config.yml`

## GitHub Pages Deployment

1. Push to your repository
2. Go to Settings > Pages
3. Select "Deploy from a branch" and choose `main`
4. Your site will be available at `https://username.github.io/repository-name`

## License

MIT License - feel free to use this template for your own lab website.