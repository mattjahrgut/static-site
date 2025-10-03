const fs = require('fs-extra');
const path = require('path');
const { marked } = require('marked');

// Configure marked for better HTML output
marked.setOptions({
  breaks: true,
  gfm: true
});

// Read template file
function readTemplate(templateName) {
  return fs.readFileSync(path.join(__dirname, 'src', 'templates', `${templateName}.html`), 'utf8');
}

// Convert markdown to HTML
function markdownToHtml(markdown) {
  return marked(markdown);
}

// Process a markdown file and generate HTML
async function processFile(inputPath, outputPath, templateName, title) {
  try {
    const markdown = await fs.readFile(inputPath, 'utf8');
    const content = markdownToHtml(markdown);
    const template = readTemplate(templateName);
    
    const html = template
      .replace('{{title}}', title)
      .replace('{{content}}', content);
    
    await fs.ensureDir(path.dirname(outputPath));
    await fs.writeFile(outputPath, html);
    console.log(`Generated: ${outputPath}`);
  } catch (error) {
    console.error(`Error processing ${inputPath}:`, error.message);
  }
}

// Copy static assets
async function copyAssets() {
  const assetsDir = path.join(__dirname, 'src', 'assets');
  const distAssetsDir = path.join(__dirname, 'dist', 'assets');
  
  if (await fs.pathExists(assetsDir)) {
    await fs.copy(assetsDir, distAssetsDir);
    console.log('Copied assets to dist/');
  }
}

// Main build function
async function build() {
  console.log('Building static site...');
  
  // Clean dist directory
  await fs.remove('dist');
  await fs.ensureDir('dist');
  
  // Define pages to process
  const pages = [
    { input: 'src/content/index.md', output: 'dist/index.html', template: 'page', title: 'Home' },
    { input: 'src/content/about.md', output: 'dist/about.html', template: 'page', title: 'About' },
    { input: 'src/content/faq.md', output: 'dist/faq.html', template: 'page', title: 'FAQ' },
    { input: 'src/content/blog.md', output: 'dist/blog.html', template: 'page', title: 'Blog' },
    { input: 'src/content/blog-post-1.md', output: 'dist/blog-post-1.html', template: 'blog', title: 'My First Blog Post' },
    { input: 'src/content/blog-post-2.md', output: 'dist/blog-post-2.html', template: 'blog', title: 'Learning Web Development' }
  ];
  
  // Process each page
  for (const page of pages) {
    if (await fs.pathExists(page.input)) {
      await processFile(page.input, page.output, page.template, page.title);
    }
  }
  
  // Copy assets
  await copyAssets();
  
  console.log('Build complete!');
}

// Run build if this file is executed directly
if (require.main === module) {
  build().catch(console.error);
}

module.exports = { build };
