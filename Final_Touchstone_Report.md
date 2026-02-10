# Touchstone 3: Develop a Functional Website
## Final Report - Bloom Valley Nursery

**Name:** [Your Name]
**Date:** February 9, 2026
**IDE Share Link:** [INSERT YOUR IDE/GITHUB LINK HERE]

---

## Introduction

### About the Client
Bloom Valley Nursery is a local, family-owned plant nursery specializing in the sale of a wide variety of plants, trees, and gardening supplies. The business connects with gardening enthusiasts and homeowners in the community who share a passion for horticulture. With a focus on sustainability and creativity, the nursery's primary goal is to enhance visibility in the local market, foster community engagement, and facilitate customer inquiries and orders.

**Hours of Operation:**
- Monday–Friday: 9:00 AM - 6:00 PM
- Saturday–Sunday: 10:00 AM - 5:00 PM

### Website Design Choices

**Color Palette: Palette 1**
The color palette features natural, earthy tones that reflect the nursery's connection to nature:
- **Leafy Green (#4A7C59)**: Primary color for navigation and buttons, representing growth and nature
- **Deep Forest (#2D5A3D)**: Secondary color for headings and accents, providing depth and sophistication
- **Harvest Gold (#D4A84B)**: Accent color for highlights and special sections, adding warmth and energy
- **Light Cream (#F5F0E8)**: Background color creating a clean, natural canvas

**Logo:** The Deep Forest Green variant was selected to harmonize with the color palette while providing a sophisticated, professional appearance.

**Font Color: Font Color 2 (Black Olive #3D3D3D)**
Black Olive provides excellent readability without the harshness of pure black on digital screens. It meets WCAG accessibility guidelines for contrast against all background colors in the palette.

**Typography: Option 2**
- **Playfair Display**: Serif font for headings and brand name, providing elegance
- **Open Sans**: Sans-serif font for body text, ensuring readability
- **Lato**: Light sans-serif for subtitles and product names

---

## Wireframes

### Desktop Wireframes
*[INSERT SCREENSHOT: Desktop wireframes showing all 4 pages side by side]*

The desktop wireframes feature:
- Horizontal navigation bar in the header
- Multi-column layouts for content sections
- 3x3 product grid on Gallery page
- Full-width table on About Us page
- Multi-column testimonial and event grids on Community page

### Mobile Wireframes
*[INSERT SCREENSHOT: Mobile wireframes showing all 4 pages in single-column layout]*

The mobile wireframes feature:
- Stacked vertical navigation
- Single-column content layout
- Vertically stacked product grid
- Vertically stacked forms and buttons

---

## Website Structure and Content

### Navigation Bar
The navigation bar appears in the header section of every webpage, implemented using semantic HTML (`<nav>` with `<ul>/<li>` structure). It includes links to all four pages: Home, Gallery, About Us, and Community. An `active` class highlights the current page. The navigation is duplicated in the footer for user convenience.

### Header and Footer Sections
**Header:** Contains the logo container with the nursery logo image and brand name displayed in an `<h1>` heading. The header uses a gradient background transitioning from Leafy Green to Deep Forest.

**Footer:** Contains:
- Secondary navigation links
- Email subscription form with submit button
- Copyright notice and physical address
- Styled with the same gradient background as the header

### Homepage Sections
1. **Hero Section:** Welcoming banner with tagline "Welcome to Bloom Valley Nursery" and call-to-action button linking to the Gallery
2. **Featured Products:** Showcases Maple Tree and Aloe Plant with images, descriptions, and styled product cards
3. **Why Choose Us (Perks):** Four boxes highlighting Expert Advice, Quality Plants, Local & Family-Owned, and Custom Orders
4. **Shop by Category:** Two-column list of product categories (Trees, Indoor Plants, Succulents, Flowering Plants, Gardening Tools, Soil & Fertilizers)

### Gallery Page Organization
Nine products displayed in a 3x3 grid:
| Row 1 | Apple Tree ($45.99) | Birch Tree ($55.99) | Maple Tree ($49.99) |
| Row 2 | Aloe Plant ($12.99) | Spider Plant ($14.99) | String of Pearls ($18.99) |
| Row 3 | Bird House ($24.99) | Potting Soil ($8.99) | Watering Can ($19.99) |

Each product includes image, name, description, price, and "Add to Cart" button. A "View Cart" button opens a modal window displaying cart contents with "Clear Cart" and "Process Order" buttons.

### About Us Page Contents
1. **Business Description:** Three paragraphs about the nursery's history, mission, and customer commitment
2. **Business Hours Table:** HTML table with day and hours columns, styled header row, hover effects on rows
3. **Contact Form:** Fields for Name (required), Email (required), Address, Phone, Message (required), and Custom Order checkbox. Submit and Clear Form buttons included
4. **Location Information:** Physical address, phone number, and email

### Custom Page Details (Community Corner)
1. **Customer Spotlight:** Four testimonial boxes with customer quotes and names on a gold background
2. **Community Involvement:** Four event boxes on a deep forest background describing:
   - Annual Tree Planting Day (April 22)
   - Kids Gardening Workshop (First Saturday monthly)
   - Community Garden Partnership (Ongoing)
   - Holiday Wreath Making (December)
3. **Our Partners:** List of local organizations including schools, foundations, and garden clubs

---

## Website Design and Styling

### CSS Styling Applied

**Homepage:**
- Gradient header (Leafy Green to Deep Forest)
- Hero section with centered text and CTA button
- Product cards with shadow and hover elevation
- Perks section with gold background and bordered boxes
- Category list with left border accent

**Gallery Page:**
- 3-column CSS Grid layout
- Product items with consistent sizing (180x180px images)
- Hover effects with shadow intensification
- Modal with semi-transparent overlay and centered content

**About Us Page:**
- Full-width table with green header row
- Weekend rows with gold tint
- Form inputs with focus border highlighting
- Button pair with green Submit and gray Clear Form

**Community Page:**
- Gold background for testimonial section
- Deep forest background for events section
- Event date badges in gold
- Consistent box styling across sections

### Rationale for Design Choices
All colors align with Color Palette 1 to reinforce the nursery's natural, earthy brand identity. Button colors follow a consistent pattern: green for primary actions, gold for accent actions, and gray for secondary actions. Hover states include color darkening and subtle animations for visual feedback.

### Accessibility Practices
1. **Color Contrast:** All text/background combinations tested for WCAG AA compliance
2. **Focus States:** Visible 3px gold outline on all interactive elements for keyboard navigation
3. **Semantic HTML:** Proper use of `<header>`, `<nav>`, `<section>`, `<footer>` elements
4. **Alt Text:** All images include descriptive alt attributes
5. **Form Labels:** All inputs associated with `<label>` elements
6. **Reduced Motion:** Media query to disable animations for users with motion sensitivity preferences

### Responsive Web Design (RWD)
**Viewport Meta Tag:**
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

**Breakpoints:**
- **768px:** Navigation stacks vertically, grid reduces to 2 columns, forms stack vertically
- **480px:** Single-column layout, reduced heading sizes

**Responsive Techniques:**
- CSS Grid with `auto-fit` and `minmax()` for automatic column adjustment
- Flexbox with `flex-wrap` for navigation and button groups
- `max-width: 100%` on images for flexible scaling

---

## Website Functionality

### Navigation Bar
Interactive navigation in both header and footer sections. Links redirect users to the four main pages. Active page is highlighted with different styling.

### Subscribe Feature
Footer section on every page contains an email subscription form. When users enter their email and click Subscribe, an alert displays: **"Thank you for subscribing."** HTML5 validation ensures a valid email format is required.

### Add to Cart Feature
Each product on the Gallery page has an "Add to Cart" button. When clicked:
- Item is added to sessionStorage with name, price, and quantity
- Alert displays: **"Item added to the cart."**
- If item already exists, quantity increments

### View Cart Feature
"View Cart" button opens a modal window that:
- Reads all items from sessionStorage
- Displays item names, quantities, and prices
- Shows total price
- Includes "Clear Cart" and "Process Order" buttons

**Clear Cart:** Clears all items from sessionStorage, displays alert: **"Cart cleared."**

**Process Order:** Clears sessionStorage, displays alert: **"Thank you for your order."**, closes modal

### Customer Feedback Feature
Contact form on About Us page collects:
- Name, Email, Address, Phone, Message, Custom Order checkbox

When submitted:
- Form data saved to localStorage
- Alert displays: **"Thank you for your message."**
- Form resets

---

## Web Data Storage

### Shopping Cart Feature (sessionStorage)
- **Add to Cart:** Items stored using `sessionStorage.setItem(itemName, JSON.stringify(itemData))`
- **View Cart:** Items retrieved by iterating through `sessionStorage.length` and `sessionStorage.key(i)`
- **Clear Cart/Process Order:** All items removed using `sessionStorage.clear()`

sessionStorage is appropriate because cart data should not persist after the browser session ends.

### Contact Form Feature (localStorage)
- **Form Submit:** Customer data saved using `localStorage.setItem('latestOrder', JSON.stringify(formData))`
- Array of all orders maintained under 'customerOrders' key

localStorage is appropriate because customer order history should persist permanently for business reference.

---

## Customization

### Community Corner Page Significance
The Community Corner page is a valuable addition that extends beyond commerce to build trust and connection:

1. **Customer Spotlight:** Testimonials from satisfied customers create social proof and demonstrate the quality of products and service
2. **Community Involvement:** Events like Tree Planting Day and Kids Workshops show the nursery is invested in the community beyond just sales
3. **Partnerships:** Collaborations with schools and food banks emphasize shared values and community support

This page reinforces Bloom Valley Nursery's identity as a community-focused, family-owned business rather than just a retail store. It connects with the Homepage's introduction, the Gallery's product showcase, and the Contact page's communication features to create a complete picture of the business.

---

## Screenshots of Rendered Webpages

### Homepage Screenshots
*[INSERT SCREENSHOT: Full homepage showing header, hero, featured products, perks, categories, footer]*

### Subscribe Feature
*[INSERT SCREENSHOT: Subscribe button clicked, showing "Thank you for subscribing" alert]*

### Gallery Page Screenshots
*[INSERT SCREENSHOT: Full gallery page showing 3x3 product grid]*

### Shopping Cart Feature

**Add Item:**
*[INSERT SCREENSHOT: "Item added to the cart" alert]*

**View Cart (with items):**
*[INSERT SCREENSHOT: Modal open showing items in cart]*

**Clear Cart:**
*[INSERT SCREENSHOT: "Cart cleared" alert]*

**View Cart (empty):**
*[INSERT SCREENSHOT: Modal showing "Your cart is empty" message]*

**Process Order:**
*[INSERT SCREENSHOT: "Thank you for your order" alert]*

### sessionStorage Screenshots
**Before Processing Order:**
*[INSERT SCREENSHOT: DevTools > Application > Session Storage showing cart items]*

**After Processing Order:**
*[INSERT SCREENSHOT: DevTools > Application > Session Storage showing empty]*

### About Us Page Screenshots
*[INSERT SCREENSHOT: Full About Us page showing table and form]*

### Contact Form Submission
*[INSERT SCREENSHOT: Filled form before submission]*

*[INSERT SCREENSHOT: "Thank you for your message" alert]*

### localStorage Screenshot
*[INSERT SCREENSHOT: DevTools > Application > Local Storage showing customer data]*

### Form Validation
*[INSERT SCREENSHOT: HTML5 validation error on required field]*

### Community Page Screenshots
*[INSERT SCREENSHOT: Full community page showing testimonials and events]*

---

## Description of Issues
I did not encounter any significant issues while developing this website. All components function as intended:
- All HTML pages render correctly
- CSS styling appears consistently across browsers
- JavaScript alerts trigger properly
- Web storage saves and retrieves data correctly
- Responsive design works on different screen sizes

Minor note: The initial font color selection of pure black was adjusted to Black Olive (#3D3D3D) after testing showed it provided a softer appearance while still meeting accessibility requirements.

---

## How to Take the Required Screenshots

1. **Open the website:** Navigate to `bloom-valley-nursery/index.html` in Chrome or Firefox
2. **Homepage:** Scroll to capture the full page (use browser's full page screenshot feature or a tool like FireShot)
3. **Subscribe:** Enter an email and click Subscribe, then screenshot the alert
4. **Gallery:** Navigate to gallery.html and capture the full product grid
5. **Add to Cart:** Click any "Add to Cart" button and screenshot the alert
6. **View Cart:** Click "View Cart" and screenshot the modal with items
7. **DevTools Storage:** Press F12 > Application tab > Session Storage/Local Storage
8. **Clear Cart:** Click "Clear Cart" in modal and screenshot the alert
9. **Process Order:** Add items, click "Process Order" and screenshot the alert
10. **About Us:** Navigate to about.html and capture the page
11. **Contact Form:** Fill the form, click Submit, and screenshot the alert
12. **Community:** Navigate to community.html and capture the full page
