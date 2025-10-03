# Simple Static Site Generator

A minimal static site generator that converts Markdown to HTML. No complex frameworks required!

## Features

- ✅ Landing page
- ✅ Blog with Markdown support  
- ✅ About and FAQ pages
- ✅ Clean, responsive design
- ✅ Simple build process
- ✅ No Node.js required (uses Python)

## Quick Start

1. **Build the site:**
   ```bash
   python3 build.py
   ```

2. **View your site:**
   ```bash
   cd dist
   python3 -m http.server 8000
   ```
   Then open http://localhost:8000 in your browser.

## Project Structure

```
├── src/
│   ├── content/          # Markdown files
│   ├── templates/        # HTML templates
│   └── assets/           # CSS, JS, images
├── dist/               # Generated HTML (after build)
├── build.py            # Build script
└── package.json        # Project metadata
```

## Adding Content

### New Pages
1. Create a Markdown file in `src/content/`
2. Add it to the pages list in `build.py`
3. Run `python3 build.py`

### New Blog Posts
1. Create a Markdown file in `src/content/`
2. Add it to the pages list in `build.py` with `'template': 'blog'`
3. Run `python3 build.py`

## Customization

- **Styling**: Edit `src/assets/css/style.css`
- **Templates**: Modify files in `src/templates/`
- **Build process**: Customize `build.py`

## Deployment

Upload the contents of the `dist/` folder to any static hosting service:
- GitHub Pages
- Netlify
- Vercel
- AWS S3
- Any web server

## Dependencies

- Python 3 (built-in)
- markdown library (auto-installed)

No Node.js, npm, or complex build tools required!