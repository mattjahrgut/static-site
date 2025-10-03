#!/usr/bin/env python3
"""
Simple static site generator using Python and markdown library.
No Node.js required!
"""

import os
import shutil
import re
from pathlib import Path

try:
    import markdown
except ImportError:
    print("Installing markdown library...")
    import subprocess
    subprocess.check_call(["pip3", "install", "markdown"])
    import markdown

# Configure markdown
md = markdown.Markdown(extensions=['extra', 'codehilite'])

def read_template(template_name):
    """Read HTML template file."""
    template_path = Path('src/templates') / f'{template_name}.html'
    return template_path.read_text(encoding='utf-8')

def markdown_to_html(markdown_text):
    """Convert markdown to HTML."""
    return md.convert(markdown_text)

def process_file(input_path, output_path, template_name, title):
    """Process a markdown file and generate HTML."""
    try:
        # Read markdown content
        markdown_content = Path(input_path).read_text(encoding='utf-8')
        html_content = markdown_to_html(markdown_content)
        
        # Read template
        template = read_template(template_name)
        
        # Replace placeholders
        html = template.replace('{{title}}', title).replace('{{content}}', html_content)
        
        # Ensure output directory exists
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        
        # Write HTML file
        Path(output_path).write_text(html, encoding='utf-8')
        print(f"Generated: {output_path}")
        
    except Exception as error:
        print(f"Error processing {input_path}: {error}")

def copy_assets():
    """Copy static assets to dist directory."""
    assets_dir = Path('src/assets')
    dist_assets_dir = Path('dist/assets')
    
    if assets_dir.exists():
        if dist_assets_dir.exists():
            shutil.rmtree(dist_assets_dir)
        shutil.copytree(assets_dir, dist_assets_dir)
        print("Copied assets to dist/")

def build():
    """Main build function."""
    print("Building static site...")
    
    # Clean and create dist directory
    if Path('dist').exists():
        shutil.rmtree('dist')
    Path('dist').mkdir()
    
    # Define pages to process
    pages = [
        {'input': 'src/content/index.md', 'output': 'dist/index.html', 'template': 'page', 'title': 'Home'},
        {'input': 'src/content/about.md', 'output': 'dist/about.html', 'template': 'page', 'title': 'About'},
        {'input': 'src/content/faq.md', 'output': 'dist/faq.html', 'template': 'page', 'title': 'FAQ'},
        {'input': 'src/content/blog.md', 'output': 'dist/blog.html', 'template': 'page', 'title': 'Blog'},
        {'input': 'src/content/blog-post-1.md', 'output': 'dist/blog-post-1.html', 'template': 'blog', 'title': 'My First Blog Post'},
        {'input': 'src/content/blog-post-2.md', 'output': 'dist/blog-post-2.html', 'template': 'blog', 'title': 'Learning Web Development'}
    ]
    
    # Process each page
    for page in pages:
        if Path(page['input']).exists():
            process_file(page['input'], page['output'], page['template'], page['title'])
    
    # Copy assets
    copy_assets()
    
    print("Build complete!")
    print("\nTo view your site:")
    print("1. cd dist")
    print("2. python3 -m http.server 8000")
    print("3. Open http://localhost:8000 in your browser")

if __name__ == '__main__':
    build()
