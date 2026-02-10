# Touchstone Task 2.2: Adding Style to the Webpages Using CSS

**Name:** [Your Name]
**Date:** February 9, 2026

---

## CSS File Link
**File:** styles.css (External CSS file located in the bloom-valley-nursery folder)

---

## CSS Styling Description

### Homepage Styling
The Homepage features a gradient header using `linear-gradient(135deg, #4A7C59, #2D5A3D)` that transitions from Leafy Green to Deep Forest, creating a rich, natural appearance. The hero section uses a semi-transparent overlay over the gradient background to ensure text readability while maintaining visual interest.

The featured products section displays product cards with a cream background (`#F5F0E8`), rounded corners (`border-radius: 12px`), and subtle box shadows that elevate on hover using `transform: translateY(-5px)`. Product images are uniformly sized at 200x200 pixels with `object-fit: cover` for consistent presentation.

The perks section uses Harvest Gold (`#D4A84B`) as the background color to create visual distinction and draw attention. Each perk box has a white background with a green border, creating a clean, card-like appearance.

The categories list uses a two-column grid layout with a left border accent in Leafy Green to add visual hierarchy.

### Gallery Page Styling
The Gallery page displays nine products in a responsive 3-column grid using CSS Grid (`grid-template-columns: repeat(3, 1fr)`). Each product item has consistent styling with:
- Light cream background
- Rounded corners (12px)
- Subtle shadow that intensifies on hover
- Centered text alignment
- Product images at 180x180 pixels

The "View Cart" button is styled with the Harvest Gold accent color and positioned prominently at the top of the gallery. The shopping cart modal uses a fixed position overlay with a semi-transparent black background (`rgba(0, 0, 0, 0.6)`). The modal content has a white background, centered positioning, and a close button (×) in the top-right corner.

All "Add to Cart" buttons use the primary green color with a hover effect that darkens the color and adds a slight upward translation.

### About Us Page Styling
The business hours table is styled with full width and collapsed borders. The header row uses Leafy Green background with white text for contrast. Table rows have a hover effect that highlights the cream background. Weekend rows have a subtle gold tint to differentiate them.

The contact form uses consistent styling throughout:
- Full-width input fields with padding
- 2px border that changes to Leafy Green on focus
- Clear visual hierarchy with bold labels
- Submit button in green, Clear Form button in gray (#777777)
- Both buttons have hover effects matching the site-wide button styles

### Community Page Styling
The Customer Spotlight section uses Harvest Gold (`#D4A84B`) as the background color, creating warmth and drawing attention to customer testimonials. Each testimonial box has a white background with:
- Rounded corners
- Subtle shadow
- Left-aligned text
- Italicized quote text

The Community Involvement section uses Deep Forest (`#2D5A3D`) as the background, creating visual contrast with the gold section above. Event boxes have a semi-transparent white background with light borders. Event dates are displayed as gold badges for quick identification.

The partnerships section returns to a white background with a simple bordered list for clean readability.

---

## Design and Color Rationale
All color choices align with Color Palette 1 selected in Task 1. The consistent use of green tones (Leafy Green and Deep Forest) throughout the site reinforces the nursery's connection to nature. The Harvest Gold accent color adds energy and draws attention to important elements like call-to-action buttons and special sections.

Button colors follow a consistent pattern:
- Primary actions (Submit, Add to Cart, Process Order): Leafy Green
- Accent actions (View Cart, Explore): Harvest Gold
- Secondary/Cancel actions (Clear Form, Clear Cart): Gray (#777777)

All hover states include color darkening and subtle animations to provide visual feedback.

---

## Accessibility Practices

### Color Contrast
All text and background color combinations have been tested for accessibility compliance. The Black Olive font color (#3D3D3D) provides sufficient contrast against light backgrounds (cream, white). White text on green backgrounds passes WCAG AA standards. Colors were verified using the Adobe Color Accessibility Tool (https://color.adobe.com/create/color-accessibility) to ensure they are color-blind safe.

### Focus States
All interactive elements (links, buttons, form inputs) have visible focus states using `outline: 3px solid #D4A84B` (Harvest Gold) with an offset of 2px. This ensures keyboard users can clearly see which element is currently focused.

### Semantic HTML and ARIA
The website uses semantic HTML elements (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) to provide meaningful structure for screen readers. All images include descriptive `alt` attributes, and form inputs are properly associated with label elements using the `for` attribute.

### Reduced Motion
A media query `@media (prefers-reduced-motion: reduce)` is included to disable all animations and transitions for users who have indicated a preference for reduced motion in their system settings.

---

## Responsive Web Design (RWD) Rationale

### Viewport Configuration
The viewport meta tag is included in all HTML pages:
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
This ensures the page width matches the device width and sets the initial zoom level to 1.0, which is essential for proper rendering on mobile devices.

### Breakpoints
Two primary breakpoints are used:

**Tablet (max-width: 768px):**
- Header navigation changes from horizontal to vertical stacking
- Product grid changes from 3 columns to 2 columns
- Hero section text size reduces from 3rem to 2rem
- Form buttons stack vertically
- Footer navigation stacks vertically
- Padding and margins are reduced for better mobile fit

**Mobile (max-width: 480px):**
- Product grid changes to single column
- Heading sizes reduce further (h1: 1.8rem, h2: 1.5rem)
- All content becomes single-column layout

### Flexible Images
All images use `max-width: 100%` and `height: auto` to ensure they scale proportionally within their containers without overflowing.

### CSS Grid and Flexbox
Responsive layouts are achieved using CSS Grid with `grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))` which automatically adjusts the number of columns based on available space. Flexbox is used for navigation and button groups with `flex-wrap: wrap` to allow items to wrap onto new lines on smaller screens.

---

## Screenshots Required for Task 2.2:
1. **Homepage with styling** - Full page showing all styled sections
2. **Gallery page with styling** - Show the styled 3x3 grid and hover effects
3. **About Us page with styling** - Show styled table and form
4. **Community page with styling** - Show styled testimonials (gold) and events (teal)
5. **Button hover state** - Show a button with hover effect applied
6. **Modal window** - Show the shopping cart modal open

---

## Issues Encountered
I initially found that the pure black font color created harsh contrast on screen. After testing with accessibility tools, I switched to Black Olive (#3D3D3D) which provides a softer appearance while maintaining excellent readability and meeting WCAG contrast requirements.

All CSS components now function as intended with no outstanding issues.
