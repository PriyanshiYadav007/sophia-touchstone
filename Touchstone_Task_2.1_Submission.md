# Touchstone Task 2.1: Creating HTML Pages

**Name:** [Your Name]
**Date:** February 9, 2026

---

## IDE Share Link
*[INSERT YOUR IDE SHARE LINK HERE - e.g., CodePen, GitHub, Replit, or local file path]*

**Local Files Location:** `bloom-valley-nursery/` folder containing:
- index.html
- gallery.html
- about.html
- community.html
- styles.css
- script.js
- images/ (folder with 9 product images)

---

## Webpage Links

| Page | File |
|------|------|
| Homepage | index.html |
| Gallery | gallery.html |
| About Us | about.html |
| Community | community.html |

---

## HTML Components Description

### Navigation Bar
The navigation bar is present in the `<header>` section of every webpage, providing consistent site-wide navigation. It is implemented using semantic HTML with a `<nav>` element containing an unordered list (`<ul>`) of navigation links. Each link (`<a>`) directs users to one of the four main pages: Home, Gallery, About Us, and Community.

The navigation uses the `class="active"` attribute to highlight the current page, providing visual feedback to users about their location within the site. The navigation is duplicated in the footer section to allow users to navigate from any point on the page.

### Header Section
The header section contains the logo container and brand name. The logo is displayed using an `<img>` tag with an `onerror` handler to gracefully hide the image if it fails to load. The brand name "Bloom Valley Nursery" is displayed in an `<h1>` heading, which is semantically appropriate as the primary heading of each page.

### Footer Section
The footer section appears at the bottom of every page and contains three main components:
1. **Secondary Navigation:** A duplicate of the main navigation for user convenience
2. **Subscribe Form:** An email subscription form using `<form>`, `<input type="email">`, and a submit button
3. **Footer Information:** Copyright notice and physical address

The subscribe form uses HTML5 validation with the `required` attribute to ensure users enter a valid email address before submission.

### Homepage Sections
The Homepage (`index.html`) includes the following sections:
- **Hero Section:** A welcoming banner with the nursery's tagline and a call-to-action button linking to the Gallery page
- **Featured Products:** Showcases two highlighted products (Maple Tree and Aloe Plant) using product cards with images, names, and descriptions
- **Perks Section:** Four boxes highlighting the benefits of shopping at Bloom Valley Nursery (Expert Advice, Quality Plants, Local & Family-Owned, Custom Orders)
- **Categories Section:** A two-column list showing the different product categories available (Trees, Indoor Plants, Succulents, Flowering Plants, Gardening Tools, Soil & Fertilizers)

### Gallery Page Organization
The Gallery page (`gallery.html`) displays all nine products in a 3x3 grid layout:

| Row 1 | Apple Tree | Birch Tree | Maple Tree |
|-------|------------|------------|------------|
| Row 2 | Aloe Plant | Spider Plant | String of Pearls |
| Row 3 | Bird House | Potting Soil | Watering Can |

Each product item includes:
- Product image
- Product name (`<h3>`)
- Product description (`<p>`)
- Price display
- "Add to Cart" button

The page also includes:
- A "View Cart" button at the top to open the shopping cart modal
- A modal window (`<div class="modal">`) that displays cart contents with "Clear Cart" and "Process Order" buttons

### About Us Page Contents
The About Us page (`about.html`) includes:

**Business Description:** Three paragraphs describing Bloom Valley Nursery's history, mission, and commitment to customer service.

**Business Hours Table:** An HTML table (`<table>`) with:
- Table header (`<thead>`) with "Day" and "Hours" columns
- Table body (`<tbody>`) with rows for each day of the week
- Weekend rows styled differently with `class="weekend"`

| Day | Hours |
|-----|-------|
| Monday-Friday | 9:00 AM - 6:00 PM |
| Saturday-Sunday | 10:00 AM - 5:00 PM |

**Contact Form:** A comprehensive form with the following fields:
- Name (required, `<input type="text">`)
- Email (required, `<input type="email">`)
- Address (`<input type="text">`)
- Phone Number (`<input type="tel">`)
- Message/Custom Order Details (required, `<textarea>`)
- Custom Order Checkbox (`<input type="checkbox">`)
- Submit and Clear Form buttons

**Location Information:** Physical address, phone number, and email address displayed with emoji icons for visual appeal.

### Custom Page Details (Community)
The Community page (`community.html`) serves as the fourth custom page, featuring:

**Customer Spotlight Section:** Four testimonial boxes displaying customer reviews with:
- Customer quote in italics
- Customer name and description (e.g., "Home Gardener", "Plant Beginner")

**Community Involvement Section:** Four event boxes highlighting local initiatives:
- Annual Tree Planting Day
- Kids Gardening Workshop
- Community Garden Partnership
- Holiday Wreath Making

Each event includes a name, description, and event date/frequency.

**Partnerships Section:** A list of local organizations the nursery collaborates with, including schools, foundations, and garden clubs.

---

## Issues Encountered
I did not encounter any significant issues while developing the HTML pages. All components render correctly and function as intended. The semantic HTML structure provides good accessibility, and all images display properly from the images folder.

---

## Screenshots Required for Task 2.1:
1. **Homepage rendered** - Full page showing header, hero, featured products, perks, categories, footer
2. **Gallery page rendered** - Show the 3x3 product grid with all products visible
3. **About Us page rendered** - Show business hours table and contact form
4. **Community page rendered** - Show testimonials and community involvement sections
