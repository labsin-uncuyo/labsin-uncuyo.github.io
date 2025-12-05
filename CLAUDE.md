# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static website for LABSIN (Laboratorio de Sistemas Inteligentes / Intelligent Systems Laboratory), a research laboratory at the National University of Cuyo, Argentina. The site is hosted on GitHub Pages and is available at labsin.org.

## Architecture

### Bilingual Structure
The website is fully bilingual (English/Spanish) with two main HTML files:
- `index.html` - English version (default for non-Spanish speakers)
- `es.html` - Spanish version
- Language detection: `index.html` includes JavaScript that auto-redirects Spanish-speaking users to `es.html` based on browser language settings (lines 12-17)

### Single-Page Application (SPA)
Both HTML files are structured as single-page applications with:
- Smooth scrolling navigation to sections via anchor links
- JavaScript-based navigation using jQuery (see `js/main.js`)
- Sections: Home, About, Research Lines, Projects, Team, Contact

### Key Sections
1. **Home** (`#section-home`) - Hero section with background image
2. **About** (`#section-about`) - Laboratory mission and goals
3. **Research Lines** (`#section-research-lines`) - Three main R+D areas: Data Science, Optimization, Intelligent Agents
4. **Projects** (`#section-research-projects`) - Current research projects with descriptions and images
5. **Team** (`#section-team`) - Team members with photos, bios, and social links
6. **Contact** (`#section-contact`) - Contact information and footer

### Navigation System
- Fixed header with logo that changes on scroll (white/colored versions)
- Desktop navigation: Horizontal menu in header
- Mobile navigation: Hamburger menu that clones the main navigation
- Smooth scroll implemented via jQuery and custom JavaScript in `js/main.js`

## Tech Stack

### Frontend Libraries (all in `js/`)
- jQuery 3.3.1 (core library)
- Bootstrap 4 (CSS framework)
- AOS (Animate On Scroll) - entrance animations
- Owl Carousel - if needed for sliders
- Stellar.js - parallax scrolling effects
- Magnific Popup - lightbox/modal functionality

### CSS Structure
- Bootstrap 4 grid system and utilities (`css/bootstrap.min.css`)
- Custom styles in `css/style.css`
- Icon fonts: Flaticon (`fonts/flaticon/`) and Icomoon (`fonts/icomoon/`)
- Font Awesome (`css/all.css`) for social media icons

### Assets
- `images/` - Team photos, project images, logos (SVG and raster formats)
- `fonts/` - Custom icon fonts (Flaticon, Icomoon)
- CNAME file points to `labsin.org` domain

## Development Workflow

### Testing the Site Locally
Since this is a static site, you can:
1. Open `index.html` or `es.html` directly in a browser
2. Or serve with a simple HTTP server:
   ```bash
   python -m http.server 8000
   # or
   python3 -m http.server 8000
   ```
   Then navigate to http://localhost:8000

### Making Changes

**Updating Content:**
- Both `index.html` and `es.html` must be updated for consistency
- Team members: Update the `#section-team` section in both files
- Projects: Update the `#section-research-projects` section in both files
- Images: Add to `images/` directory and reference in HTML

**Styling Changes:**
- Custom styles: Edit `css/style.css`
- Avoid modifying vendor CSS files in `css/bootstrap/` or minified files

**JavaScript Changes:**
- Main custom JavaScript is in `js/main.js`
- Avoid modifying vendor JavaScript files (jquery, bootstrap, etc.)

### Git Workflow
- Main branch: `master` (for PRs and production)
- Current branch: `develop` (for development work)
- The site is deployed via GitHub Pages from the repository

### Deployment
Changes pushed to the repository are automatically deployed via GitHub Pages to labsin.org.

## Important Notes

### Content Synchronization
When updating content, **always update both HTML files** (`index.html` and `es.html`) to maintain language parity. The two files have identical structure but different text content.

### Image Management
- Team photos should be added to `images/` directory
- Use consistent naming: lowercase, descriptive names (e.g., `firstname.jpg`, `project-name.png`)
- Current naming convention for team: first name or nickname in lowercase (e.g., `harpo.jpg`, `kike.jpg`)

### Social Media Links
Team member profiles include links to:
- ResearchGate (class: `profile-link-rg`)
- LinkedIn (class: `profile-link-lin`)
- GitHub (class: `profile-link-gh`)
- Twitter (class: `profile-link-tw`)

### Responsive Design
The site uses Bootstrap 4's responsive grid system:
- Mobile breakpoints are handled automatically
- Mobile menu is cloned from desktop navigation via JavaScript
- Test responsive behavior at different breakpoints

## Common Tasks

### Adding a New Team Member
1. Add team member photo to `images/` directory (use `.jpg` or `.jpeg`)
2. Update both `index.html` and `es.html` in the `#section-team` section
3. Follow the existing HTML structure for team member cards
4. Include appropriate social media links using Font Awesome icons

### Adding a New Project
1. Add project image to `images/` directory if needed
2. Update both `index.html` and `es.html` in the `#section-research-projects` section
3. Follow the existing project card structure

### Updating Google Analytics
The site uses Google Analytics (ID: UA-153082860-1). The tracking code is in the `<head>` section of both HTML files (lines 19-27 in `index.html`, lines 12-20 in `es.html`).
