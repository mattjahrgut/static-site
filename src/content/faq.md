# Frequently Asked Questions

## How do I add new pages?

1. Create a new Markdown file in `src/content/`
2. Add it to the pages array in `build.js`
3. Run `npm run build`

## How do I add a new blog post?

1. Create a new Markdown file in `src/content/` (e.g., `blog-post-3.md`)
2. Add it to the pages array in `build.js` with template: 'blog'
3. Run `npm run build`

## How do I customize the styling?

Edit the CSS file at `src/assets/css/style.css`. The build process will copy it to the output directory.

## How do I add JavaScript?

Place your JavaScript files in `src/assets/js/` and they'll be copied to the output directory.

## Can I use this for a real website?

Absolutely! This setup is perfect for:
- Personal blogs
- Documentation sites
- Portfolio websites
- Small business sites

## How do I deploy this?

You can deploy the contents of the `dist/` folder to any static hosting service like:
- GitHub Pages
- Netlify
- Vercel
- AWS S3
- Any web server

## Do I need to know programming?

Basic knowledge of HTML, CSS, and Markdown is helpful, but the setup is designed to be as simple as possible.
