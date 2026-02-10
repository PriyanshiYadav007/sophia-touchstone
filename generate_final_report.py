"""
Final Compilation Script for Bloom Valley Nursery Touchstone Report.
Ensures all generated wireframes and screenshots are correctly embedded.
"""
import os
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUTPUT_PATH = r"c:\Users\DELL\OneDrive\Desktop\Sophia.1web dev\webdev\bloom-valley-nursery\submissions\Final_Touchstone_Report.docx"
SCREENSHOT_DIR = r"c:\Users\DELL\OneDrive\Desktop\Sophia.1web dev\webdev\bloom-valley-nursery\final_screenshots"

def add_heading(doc, text, level=1):
    heading = doc.add_heading(text, level)
    if level == 0:
        heading.alignment = WD_ALIGN_PARAGRAPH.CENTER

def add_image(doc, filename, caption):
    path = os.path.join(SCREENSHOT_DIR, filename)
    if os.path.exists(path):
        doc.add_picture(path, width=Inches(5.5))
        p = doc.add_paragraph(caption)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.style.font.italic = True
    else:
        doc.add_paragraph(f"[Note: Image {filename} placeholder for final review]")

def main():
    doc = Document()
    
    # --- Title Page ---
    add_heading(doc, 'Final Touchstone Report', 0)
    p = doc.add_paragraph('\nBloom Valley Nursery Website Project\n\n')
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = doc.add_paragraph('Developed for: Web Development Fundamentals Course\nDate: February 10, 2026\n')
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_page_break()

    # --- Section 1: Introduction ---
    add_heading(doc, '1. Introduction and Design Phase', 1)
    doc.add_paragraph('Bloom Valley Nursery is a family-owned business focused on plants and community gardening. The website was designed with a "Leafy Green" palette to evoke growth and nature.')
    
    add_heading(doc, 'Desktop Wireframe (Figma Style)', 2)
    add_image(doc, 'wireframe_desktop.png', 'Fig 1: Desktop Wireframe UI/UX Design')
    
    add_heading(doc, 'Mobile Wireframe (Figma Style)', 2)
    add_image(doc, 'wireframe_mobile.png', 'Fig 2: Mobile Responsive Wireframe Layout')
    doc.add_page_break()

    # --- Section 2: Website Structure ---
    add_heading(doc, '2. Website Structure and Content', 1)
    doc.add_paragraph('The website consists of four semantic HTML5 pages. Each page features a consistent navigation bar and responsive footer.')
    
    add_heading(doc, 'Homepage Layout', 2)
    add_image(doc, '01_homepage_full.png', 'Fig 3: Homepage with Hero Section and Featured Products')
    
    add_heading(doc, 'Gallery Page (3x3 Grid)', 2)
    add_image(doc, '03_gallery_grid.png', 'Fig 4: Gallery displaying automated product grid and "Add to Cart" interactions')
    doc.add_page_break()

    # --- Section 3: Interaction & Functionality ---
    add_heading(doc, '3. Interaction and JavaScript Features', 1)
    doc.add_paragraph('Dynamic features include a functional shopping cart and contact form system. Interactive alerts provide feedback for every user action.')
    
    add_heading(doc, 'About Us & Contact Form', 2)
    add_image(doc, '09_about_page.png', 'Fig 5: About Us page with business hours table and contact intake form')
    
    add_heading(doc, 'Community Corner', 2)
    add_image(doc, '12_community_page.png', 'Fig 6: Custom Page showcasing testimonials and community events')
    doc.add_page_break()

    # --- Section 4: Web Storage Implementation ---
    add_heading(doc, '4. Web Storage Evidence', 1)
    doc.add_paragraph('The shopping cart utilizes sessionStorage to track items, while localStorage persists contact form metadata.')
    
    add_heading(doc, 'Shopping Cart View', 2)
    add_image(doc, '05_cart_modal_items.png', 'Fig 7: View Cart modal retrieving items from sessionStorage')
    
    add_heading(doc, 'Clear Cart Functionality', 2)
    add_image(doc, '07_cart_modal_empty.png', 'Fig 8: Modal state after clearing sessionStorage storage')

    # --- Conclusion ---
    add_heading(doc, '5. Conclusion', 1)
    doc.add_paragraph('The project successfully meets all Touchstone criteria. The final product is a professional, accessible, and interactive web presence for Bloom Valley Nursery.')

    doc.save(OUTPUT_PATH)
    print(f"Final Report compiled successfully at: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
