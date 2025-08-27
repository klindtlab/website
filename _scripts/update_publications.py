#!/usr/bin/env python3
"""
Script to fetch publications from Google Scholar and update Jekyll site
"""

import requests
from bs4 import BeautifulSoup
import re
import yaml
import os
from datetime import datetime

def fetch_google_scholar_publications(scholar_id):
    """
    Fetch publications from Google Scholar profile
    Replace with actual scraping or API calls
    """
    
    # Note: Google Scholar doesn't have an official API
    # For production, consider using:
    # 1. scholarly library: pip install scholarly
    # 2. serpapi: https://serpapi.com/google-scholar-api
    # 3. Manual maintenance of publications
    
    try:
        from scholarly import scholarly
        
        # Search for the author
        author = scholarly.search_author_id(scholar_id)
        author = scholarly.fill(author)
        
        publications = []
        
        for pub in author['publications']:
            pub_filled = scholarly.fill(pub)
            
            # Extract publication info
            publication = {
                'title': pub_filled.get('bib', {}).get('title', ''),
                'authors': pub_filled.get('bib', {}).get('author', ''),
                'journal': pub_filled.get('bib', {}).get('venue', ''),
                'year': pub_filled.get('bib', {}).get('pub_year', ''),
                'abstract': pub_filled.get('bib', {}).get('abstract', ''),
                'citations': pub_filled.get('num_citations', 0),
                'url': pub_filled.get('pub_url', ''),
            }
            
            # Try to extract DOI if available
            if 'eprint_url' in pub_filled:
                publication['pdf'] = pub_filled['eprint_url']
            
            publications.append(publication)
        
        return publications
        
    except ImportError:
        print("scholarly library not found. Install with: pip install scholarly")
        return []
    except Exception as e:
        print(f"Error fetching from Google Scholar: {e}")
        return []

def create_publication_files(publications, output_dir):
    """
    Create individual publication markdown files
    """
    
    os.makedirs(output_dir, exist_ok=True)
    
    for i, pub in enumerate(publications):
        # Create filename from title
        filename = re.sub(r'[^\w\s-]', '', pub['title'].lower())
        filename = re.sub(r'[-\s]+', '-', filename)
        filename = f"{pub.get('year', 'unknown')}-{filename[:50]}.md"
        
        filepath = os.path.join(output_dir, filename)
        
        # Create frontmatter
        frontmatter = {
            'layout': 'publication',
            'title': pub['title'],
            'authors': pub['authors'],
            'journal': pub['journal'],
            'year': pub['year'],
            'abstract': pub['abstract'],
            'citations': pub['citations'],
            'url': pub['url'],
        }
        
        if 'pdf' in pub:
            frontmatter['pdf'] = pub['pdf']
        
        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('---\n')
            yaml.dump(frontmatter, f, default_flow_style=False, allow_unicode=True)
            f.write('---\n\n')
            if pub['abstract']:
                f.write(f"{pub['abstract']}\n")

def update_publications_yaml(publications, yaml_file):
    """
    Update publications data file
    """
    
    # Sort publications by year (newest first)
    publications.sort(key=lambda x: int(x.get('year', 0)), reverse=True)
    
    with open(yaml_file, 'w', encoding='utf-8') as f:
        yaml.dump(publications, f, default_flow_style=False, allow_unicode=True)

def main():
    # Configuration
    SCHOLAR_ID = "EpT-nUAAAAAJ"  # David Klindt's Google Scholar ID
    PUBLICATIONS_DIR = "_publications"
    DATA_FILE = "_data/publications.yml"
    
    print("Fetching publications from Google Scholar...")
    publications = fetch_google_scholar_publications(SCHOLAR_ID)
    
    if publications:
        print(f"Found {len(publications)} publications")
        
        # Create publication files
        create_publication_files(publications, PUBLICATIONS_DIR)
        
        # Update data file
        os.makedirs("_data", exist_ok=True)
        update_publications_yaml(publications, DATA_FILE)
        
        print("Publications updated successfully!")
    else:
        print("No publications found or error occurred")

if __name__ == "__main__":
    main()