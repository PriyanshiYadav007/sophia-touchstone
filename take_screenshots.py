"""
Take screenshots of all pages and features for Touchstone submissions
"""
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Output directory for screenshots
SCREENSHOT_DIR = r"c:\Users\DELL\OneDrive\Desktop\Sophia.1web dev\webdev\bloom-valley-nursery\screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

BASE_URL = "http://localhost:8080"

def setup_driver():
    """Setup Chrome driver"""
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1920, 1080)
    return driver

def take_screenshot(driver, name, description=""):
    """Take a screenshot and save it"""
    filepath = os.path.join(SCREENSHOT_DIR, f"{name}.png")
    driver.save_screenshot(filepath)
    print(f"[OK] Saved: {name}.png - {description}")
    return filepath

def safe_alert_accept(driver):
    """Safely accept any alert that appears"""
    try:
        time.sleep(0.3)
        alert = driver.switch_to.alert
        alert.accept()
        return True
    except:
        return False

def main():
    driver = setup_driver()
    wait = WebDriverWait(driver, 10)
    
    try:
        # ============================================
        # HOMEPAGE SCREENSHOTS
        # ============================================
        print("\n=== Capturing Homepage ===")
        driver.get(f"{BASE_URL}/index.html")
        time.sleep(2)
        take_screenshot(driver, "01_homepage_full", "Homepage - Full View")
        
        # Scroll to show more sections
        driver.execute_script("window.scrollTo(0, 600)")
        time.sleep(0.5)
        take_screenshot(driver, "02_homepage_featured", "Homepage - Featured Products")
        
        driver.execute_script("window.scrollTo(0, 1200)")
        time.sleep(0.5)
        take_screenshot(driver, "03_homepage_perks", "Homepage - Perks Section")
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(0.5)
        take_screenshot(driver, "04_homepage_footer", "Homepage - Footer with Subscribe")
        
        # Subscribe alert
        try:
            email_input = driver.find_element(By.ID, "subscribe-email")
            email_input.clear()
            email_input.send_keys("test@example.com")
            time.sleep(0.3)
            
            subscribe_btn = driver.find_element(By.ID, "subscribe-btn")
            subscribe_btn.click()
            time.sleep(0.5)
            
            try:
                alert = driver.switch_to.alert
                take_screenshot(driver, "05_subscribe_alert", "Subscribe Alert")
                alert.accept()
            except:
                print("Subscribe alert not captured")
        except Exception as e:
            print(f"Subscribe section error: {e}")
        
        # ============================================
        # GALLERY PAGE SCREENSHOTS
        # ============================================
        print("\n=== Capturing Gallery Page ===")
        driver.get(f"{BASE_URL}/gallery.html")
        time.sleep(2)
        take_screenshot(driver, "06_gallery_full", "Gallery - 3x3 Product Grid")
        
        driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(0.5)
        take_screenshot(driver, "07_gallery_products", "Gallery - Products with Prices")
        
        # Add to Cart alert
        try:
            add_to_cart_btns = driver.find_elements(By.CSS_SELECTOR, ".add-to-cart-btn")
            if add_to_cart_btns:
                add_to_cart_btns[0].click()
                time.sleep(0.5)
                try:
                    alert = driver.switch_to.alert
                    take_screenshot(driver, "08_add_to_cart_alert", "Add to Cart Alert")
                    alert.accept()
                except:
                    print("Add to cart alert not captured")
        except Exception as e:
            print(f"Add to cart error: {e}")
        
        # Add more items for cart demo
        driver.get(f"{BASE_URL}/gallery.html")
        time.sleep(1)
        try:
            add_to_cart_btns = driver.find_elements(By.CSS_SELECTOR, ".add-to-cart-btn")
            for i in range(min(3, len(add_to_cart_btns))):
                add_to_cart_btns[i].click()
                safe_alert_accept(driver)
                time.sleep(0.2)
        except:
            pass
        
        # View Cart modal
        try:
            view_cart_btn = driver.find_element(By.ID, "view-cart-btn")
            view_cart_btn.click()
            time.sleep(0.5)
            take_screenshot(driver, "09_cart_modal_items", "Cart Modal - With Items")
            
            # Clear Cart
            clear_cart_btn = driver.find_element(By.ID, "clear-cart-btn")
            clear_cart_btn.click()
            time.sleep(0.5)
            try:
                alert = driver.switch_to.alert
                take_screenshot(driver, "10_clear_cart_alert", "Clear Cart Alert")
                alert.accept()
            except:
                print("Clear cart alert not captured")
            
            take_screenshot(driver, "11_cart_modal_empty", "Cart Modal - Empty After Clear")
            
            # Close modal
            close_btn = driver.find_element(By.ID, "close-modal")
            close_btn.click()
            time.sleep(0.3)
        except Exception as e:
            print(f"Cart modal error: {e}")
        
        # Add items again for process order
        try:
            add_to_cart_btns = driver.find_elements(By.CSS_SELECTOR, ".add-to-cart-btn")
            for i in range(2):
                add_to_cart_btns[i].click()
                safe_alert_accept(driver)
                time.sleep(0.2)
            
            view_cart_btn = driver.find_element(By.ID, "view-cart-btn")
            view_cart_btn.click()
            time.sleep(0.5)
            
            process_order_btn = driver.find_element(By.ID, "process-order-btn")
            process_order_btn.click()
            time.sleep(0.5)
            try:
                alert = driver.switch_to.alert
                take_screenshot(driver, "12_process_order_alert", "Process Order Alert")
                alert.accept()
            except:
                print("Process order alert not captured")
        except Exception as e:
            print(f"Process order error: {e}")
        
        # ============================================
        # ABOUT US PAGE SCREENSHOTS
        # ============================================
        print("\n=== Capturing About Us Page ===")
        driver.get(f"{BASE_URL}/about.html")
        time.sleep(2)
        take_screenshot(driver, "13_about_full", "About Us - Full View")
        
        driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(0.5)
        take_screenshot(driver, "14_about_hours_table", "About Us - Hours Table")
        
        driver.execute_script("window.scrollTo(0, 800)")
        time.sleep(0.5)
        take_screenshot(driver, "15_about_contact_form", "About Us - Contact Form")
        
        # Fill and submit form
        try:
            driver.find_element(By.ID, "customer-name").send_keys("John Doe")
            driver.find_element(By.ID, "customer-email").send_keys("john@example.com")
            driver.find_element(By.ID, "customer-address").send_keys("123 Main St, Anytown USA")
            driver.find_element(By.ID, "customer-phone").send_keys("555-123-4567")
            driver.find_element(By.ID, "customer-message").send_keys("I would like to order a custom arrangement of succulents.")
            driver.find_element(By.ID, "custom-order").click()
            
            take_screenshot(driver, "16_contact_form_filled", "Contact Form - Filled")
            
            submit_btn = driver.find_element(By.CSS_SELECTOR, ".submit-btn")
            submit_btn.click()
            time.sleep(0.5)
            try:
                alert = driver.switch_to.alert
                take_screenshot(driver, "17_form_submit_alert", "Form Submit Alert")
                alert.accept()
            except:
                print("Form submit alert not captured")
        except Exception as e:
            print(f"Contact form error: {e}")
        
        # ============================================
        # COMMUNITY PAGE SCREENSHOTS
        # ============================================
        print("\n=== Capturing Community Page ===")
        driver.get(f"{BASE_URL}/community.html")
        time.sleep(2)
        take_screenshot(driver, "18_community_full", "Community - Full View")
        
        driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(0.5)
        take_screenshot(driver, "19_community_testimonials", "Community - Customer Testimonials")
        
        driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(0.5)
        take_screenshot(driver, "20_community_events", "Community - Events")
        
        # ============================================
        # BUTTON HOVER EFFECT
        # ============================================
        print("\n=== Capturing Button Hover ===")
        driver.get(f"{BASE_URL}/index.html")
        time.sleep(1)
        
        # Using JavaScript to simulate hover
        try:
            hero_btn = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
            driver.execute_script("""
                arguments[0].style.transform = 'translateY(-3px)';
                arguments[0].style.boxShadow = '0 6px 20px rgba(74, 124, 89, 0.4)';
                arguments[0].style.backgroundColor = '#3d6649';
            """, hero_btn)
            take_screenshot(driver, "21_button_hover", "Button with Hover Effect")
        except Exception as e:
            print(f"Button hover error: {e}")
        
        print(f"\n=== ALL DONE ===")
        print(f"Screenshots saved to: {SCREENSHOT_DIR}")
        print(f"Total: {len(os.listdir(SCREENSHOT_DIR))} screenshots")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
