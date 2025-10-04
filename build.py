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
    subprocess.check_call(["pip3", "install", "-r", "requirements.txt"])
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
    """Process a markdown or HTML file and generate HTML."""
    try:
        # Read content
        content = Path(input_path).read_text(encoding='utf-8')
        
        # Check if it's HTML or Markdown
        if input_path.endswith('.html'):
            # Use HTML content directly
            html_content = content
        else:
            # Convert markdown to HTML
            html_content = markdown_to_html(content)
        
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
    
    # Define static pages
    static_pages = [
        {'input': 'src/content/index.html', 'output': 'dist/index.html', 'template': 'index', 'title': 'Home'},
        {'input': 'src/content/about.md', 'output': 'dist/about.html', 'template': 'page', 'title': 'About'},
        {'input': 'src/content/faq.md', 'output': 'dist/faq.html', 'template': 'page', 'title': 'FAQ'},
        {'input': 'src/content/blog.md', 'output': 'dist/blog.html', 'template': 'page', 'title': 'Blog'}
    ]
    
    # Auto-discover blog posts
    blog_posts = []
    content_dir = Path('src/content')
    if content_dir.exists():
        for file_path in content_dir.glob('blog-post-*.md'):
            # Extract post number and create title
            filename = file_path.stem  # e.g., 'blog-post-1'
            post_num = filename.split('-')[-1]  # e.g., '1'
            
            # Read first line to get the title (remove # and strip)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    first_line = f.readline().strip()
                    if first_line.startswith('#'):
                        title = first_line[1:].strip()
                    else:
                        title = f"Blog Post {post_num}"
            except:
                title = f"Blog Post {post_num}"
            
            blog_posts.append({
                'input': str(file_path),
                'output': f'dist/{filename}.html',
                'template': 'blog',
                'title': title
            })
    
    # Combine all pages
    pages = static_pages + blog_posts
    
    # Generate blog posts list for blog.md
    blog_posts_list = ""
    for post in sorted(blog_posts, key=lambda x: x['input'], reverse=True):  # Sort by filename, newest first
        if Path(post['input']).exists():
            # Extract post number for display
            filename = Path(post['input']).stem
            post_num = filename.split('-')[-1]
            blog_posts_list += f"- [{post['title']}](/{filename}.html) - Cat story #{post_num}\n"
    
    # Process each page
    for page in pages:
        if Path(page['input']).exists():
            # Special handling for blog.md to replace blog posts list
            if page['input'] == 'src/content/blog.md':
                # Read the blog.md content
                content = Path(page['input']).read_text(encoding='utf-8')
                # Replace the placeholder with actual blog posts list
                content = content.replace('{{BLOG_POSTS_LIST}}', blog_posts_list)
                # Convert to HTML
                html_content = markdown_to_html(content)
                # Read template
                template = read_template(page['template'])
                # Replace placeholders
                html = template.replace('{{title}}', page['title']).replace('{{content}}', html_content)
                # Write HTML file
                Path(page['output']).write_text(html, encoding='utf-8')
                print(f"Generated: {page['output']}")
            else:
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
