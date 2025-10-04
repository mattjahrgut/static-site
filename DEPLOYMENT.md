# GitHub Pages Deployment Guide

This guide will help you deploy your cat blog to GitHub Pages with automatic builds.

## Prerequisites

- GitHub account
- Your repository already pushed to GitHub

## Step 1: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** tab
3. Scroll down to **Pages** section
4. Under **Source**, select **GitHub Actions**
5. Click **Save**

## Step 2: Push Your Code

Make sure all your files are committed and pushed to GitHub:

```bash
git add .
git commit -m "Add GitHub Pages deployment"
git push origin main
```

## Step 3: Monitor the Build

1. Go to the **Actions** tab in your repository
2. You should see a workflow run called "Deploy to GitHub Pages"
3. Click on it to monitor the build process
4. The build will:
   - Install Python dependencies
   - Run your build script
   - Deploy the `dist/` folder to GitHub Pages

## Step 4: Access Your Site

Once the workflow completes successfully:
1. Go to **Settings** → **Pages**
2. Your site will be available at: `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME`
3. It may take a few minutes for the first deployment

## How It Works

The GitHub Actions workflow:
- **Triggers** on every push to the `main` branch
- **Installs** Python and markdown library
- **Builds** your site using `python3 build.py`
- **Deploys** the `dist/` folder to GitHub Pages

## Custom Domain (Optional)

To use a custom domain:
1. Add a `CNAME` file to your `src/assets/` folder with your domain
2. Update the build script to copy it to `dist/`
3. Configure your domain's DNS to point to GitHub Pages

## Troubleshooting

**Build fails?**
- Check the Actions tab for error messages
- Ensure all files are committed
- Verify Python dependencies are correct

**Site not updating?**
- Wait 5-10 minutes for GitHub Pages to update
- Check if the workflow completed successfully
- Clear your browser cache

**Custom domain issues?**
- Verify DNS settings
- Check the CNAME file is in the root of your site
- Wait for DNS propagation (up to 24 hours)

## File Structure

Your deployed site will have:
```
https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/
├── index.html          # Homepage
├── about.html          # About page
├── blog.html           # Blog listing
├── blog-post-*.html    # Individual blog posts
├── faq.html            # FAQ page
└── assets/
    └── css/
        └── style.css   # Your styles
```

## Automatic Updates

Every time you:
1. **Push changes** to the main branch
2. **Add new blog posts**
3. **Update content**

The site will automatically rebuild and deploy! 🐱✨
