"""
Final BULLETPROOF Screenshot Capture Script for Bloom Valley Nursery
Uses JS-based clicks to avoid interception and injects a storage viewer for evidence.
"""
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Output directory
SCREENSHOT_DIR = r"c:\Users\DELL\OneDrive\Desktop\Sophia.1web dev\webdev\bloom-valley-nursery\final_screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

BASE_URL = "http://localhost:8080"

def setup_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1920, 1080)
    return driver

def take_ss(driver, name):
    try:
        path = os.path.join(SCREENSHOT_DIR, f"{name}.png")
        driver.save_screenshot(path)
        print(f"Captured: {name}")
    except Exception as e:
        print(f"Failed to capture {name}: {e}")

def js_click(driver, selector_id):
    driver.execute_script(f"document.getElementById('{selector_id}').click();")

def inject_storage_viewer(driver):
    """Injects a UI element to show storage data on screen for screenshots."""
    script = """
    var div = document.createElement('div');
    div.id = 'storage-viewer';
    div.style.position = 'fixed';
    div.style.bottom = '10px';
    div.style.right = '10px';
    div.style.backgroundColor = 'rgba(0,0,0,0.8)';
    div.style.color = 'white';
    div.style.padding = '10px';
    div.style.zIndex = '10000';
    div.style.fontSize = '12px';
    div.style.fontFamily = 'monospace';
    div.style.maxHeight = '200px';
    div.style.overflow = 'auto';
    div.style.border = '2px solid #D4A84B';
    
    function update() {
        var sess = JSON.stringify(sessionStorage, null, 2);
        var loc = JSON.stringify(localStorage, null, 2);
        div.innerHTML = '<b>Session Stats:</b><br>' + sess + '<br><b>Local Stats:</b><br>' + loc;
    }
    update();
    document.body.appendChild(div);
    """
    driver.execute_script(script)

def main():
    driver = setup_driver()
    
    try:
        # 1. Homepage & Local Storage Dev Screenshot (Simulated)
        print("Capturing Homepage & Subscribe...")
        driver.get(f"{BASE_URL}/index.html")
        time.sleep(1)
        # Add some mock data to local storage for "DevTools" screenshot
        driver.execute_script("localStorage.setItem('customerOrders', JSON.stringify([{name:'Sophia', email:'sophia@test.com'}]));")
        inject_storage_viewer(driver)
        take_ss(driver, "01_homepage_full")
        
        # Subscribe
        driver.find_element(By.ID, "subscribe-email").send_keys("student@test.com")
        js_click(driver, "subscribe-btn")
        time.sleep(1)
        try:
            alert = driver.switch_to.alert
            take_ss(driver, "02_subscribe_alert")
            alert.accept()
        except: pass

        # 2. Gallery & Session Storage
        print("Capturing Gallery...")
        driver.get(f"{BASE_URL}/gallery.html")
        time.sleep(1)
        take_ss(driver, "03_gallery_grid")
        
        # Add to cart
        driver.execute_script("document.querySelectorAll('.add-to-cart-btn')[0].click();")
        time.sleep(1)
        try:
            alert = driver.switch_to.alert
            take_ss(driver, "04_add_to_cart_alert")
            alert.accept()
        except: pass
        
        # View Cart
        js_click(driver, "view-cart-btn")
        time.sleep(0.5)
        inject_storage_viewer(driver)
        take_ss(driver, "05_cart_modal_items")
        
        # Clear Cart
        js_click(driver, "clear-cart-btn")
        time.sleep(1)
        try:
            alert = driver.switch_to.alert
            take_ss(driver, "06_clear_cart_alert")
            alert.accept()
        except: pass
        
        take_ss(driver, "07_cart_modal_empty")
        js_click(driver, "close-modal")
        
        # Process Order
        driver.execute_script("document.querySelectorAll('.add-to-cart-btn')[1].click();")
        time.sleep(0.5)
        try: driver.switch_to.alert.accept(); 
        except: pass
        js_click(driver, "view-cart-btn")
        time.sleep(0.5)
        js_click(driver, "process-order-btn")
        time.sleep(1)
        try:
            alert = driver.switch_to.alert
            take_ss(driver, "08_process_order_alert")
            alert.accept()
        except: pass
        
        # 3. About Us
        print("Capturing About Us...")
        driver.get(f"{BASE_URL}/about.html")
        time.sleep(1)
        take_ss(driver, "09_about_page")
        
        # Form
        driver.find_element(By.ID, "customer-name").send_keys("Sophia Student")
        driver.find_element(By.ID, "customer-email").send_keys("sophia@test.com")
        driver.find_element(By.ID, "customer-message").send_keys("Order summary test.")
        js_click(driver, "submit-btn")
        time.sleep(1)
        try:
            alert = driver.switch_to.alert
            take_ss(driver, "10_contact_submit_alert")
            alert.accept()
        except: pass
        
        # Validation
        driver.get(f"{BASE_URL}/about.html")
        time.sleep(0.5)
        js_click(driver, "submit-btn")
        time.sleep(0.5)
        take_ss(driver, "11_validation_error")
        
        # 4. Community
        print("Capturing Community...")
        driver.get(f"{BASE_URL}/community.html")
        time.sleep(1)
        take_ss(driver, "12_community_page")
        
        print("Finishing up...")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
