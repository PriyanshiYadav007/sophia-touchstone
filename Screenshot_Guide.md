# Screenshot Guide for All Touchstone Submissions

## How to Take Screenshots

### Using Windows
- **Full Screen:** Press `Windows + Shift + S`, then select "Full screen snip"
- **Window Only:** Press `Alt + Print Screen`
- **Custom Area:** Press `Windows + Shift + S`, then draw a rectangle

### Using Browser Full Page Screenshot
- **Chrome:** Press F12 → Ctrl+Shift+P → Type "screenshot" → Select "Capture full size screenshot"
- **Firefox:** Right-click → Take Screenshot → Save full page

### DevTools Screenshots (for Web Storage)
1. Press `F12` to open DevTools
2. Click "Application" tab
3. Expand "Storage" on the left
4. Click "Session Storage" or "Local Storage"
5. Screenshot the panel showing the data

---

## Required Screenshots by Task

### Task 1: Planning & Design
| # | Screenshot | How to Get It |
|---|------------|---------------|
| 1 | Mobile Wireframes | Create in Figma/draw.io, or use ASCII art from walkthrough |
| 2 | Desktop Wireframes | Create in Figma/draw.io, or use ASCII art from walkthrough |

---

### Task 2.1: HTML Pages
| # | Screenshot | How to Get It |
|---|------------|---------------|
| 1 | Homepage rendered | Open index.html → Full page screenshot |
| 2 | Gallery page rendered | Open gallery.html → Full page screenshot |
| 3 | About Us page rendered | Open about.html → Full page screenshot |
| 4 | Community page rendered | Open community.html → Full page screenshot |

---

### Task 2.2: CSS Styling
| # | Screenshot | How to Get It |
|---|------------|---------------|
| 1 | Homepage styled | Open index.html → Full page screenshot |
| 2 | Gallery styled | Open gallery.html → Full page screenshot |
| 3 | About Us styled | Open about.html → Full page screenshot |
| 4 | Community styled | Open community.html → Full page screenshot |
| 5 | Button hover effect | Hover over a button → Screenshot with hover style visible |
| 6 | Shopping cart modal | Click "View Cart" → Screenshot the open modal |

---

### Task 3.1: JavaScript Alerts
| # | Screenshot | How to Get It |
|---|------------|---------------|
| 1 | Subscribe alert | Enter email in footer → Click Subscribe → Screenshot alert |
| 2 | Add to Cart alert | Click any "Add to Cart" button → Screenshot alert |
| 3 | Clear Cart alert | Open cart modal → Click "Clear Cart" → Screenshot alert |
| 4 | Process Order alert | Add item, open cart, click "Process Order" → Screenshot alert |
| 5 | Form Submit alert | Fill contact form → Click Submit → Screenshot alert |
| 6 | Form validation | Leave required field empty → Click Submit → Screenshot validation error |

---

### Task 3.2: Web Storage
| # | Screenshot | How to Get It |
|---|------------|---------------|
| 1 | Add item alert | Click "Add to Cart" → Screenshot alert |
| 2 | View Cart with items | Add items → Click "View Cart" → Screenshot modal |
| 3 | sessionStorage BEFORE clear | F12 → Application → Session Storage → Screenshot |
| 4 | Clear Cart alert | Click "Clear Cart" → Screenshot alert |
| 5 | sessionStorage AFTER clear | F12 → Application → Session Storage → Screenshot (empty) |
| 6 | Process Order alert | Add items → Click "Process Order" → Screenshot |
| 7 | sessionStorage AFTER process | F12 → Application → Session Storage → Screenshot (empty) |
| 8 | Contact form filled | Fill all fields in contact form → Screenshot |
| 9 | Form submit alert | Click Submit → Screenshot "Thank you for your message" alert |
| 10 | localStorage with data | F12 → Application → Local Storage → Screenshot showing customer data |

---

### Final Touchstone Report
Include ALL screenshots from above, organized by section:
1. Wireframes (2)
2. Homepage (2-3)
3. Gallery with shopping cart (5-7)
4. About Us with form (4-5)
5. Community page (1-2)
6. DevTools storage screenshots (4-5)

---

## Quick Checklist

Before submitting, verify:
- [ ] All 4 pages load correctly
- [ ] Navigation works between pages
- [ ] Subscribe shows "Thank you for subscribing" alert
- [ ] Add to Cart shows "Item added to the cart" alert
- [ ] View Cart modal opens and shows items
- [ ] Clear Cart shows "Cart cleared" alert and empties cart
- [ ] Process Order shows "Thank you for your order" alert
- [ ] Contact form shows "Thank you for your message" alert
- [ ] sessionStorage shows cart data in DevTools
- [ ] localStorage shows customer data in DevTools
- [ ] Buttons have hover effects
- [ ] Colors match Color Palette 1
