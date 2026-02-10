# Touchstone Task 3.1: Implementing Dynamic Features With JavaScript

**Name:** [Your Name]
**Date:** February 9, 2026

---

## JavaScript File Link
**File:** script.js (External JavaScript file located in the bloom-valley-nursery folder)

---

## JavaScript Functionality Description

### Subscribe Feature (All Pages)
The Subscribe feature is implemented in the footer section of every webpage. When a user enters their email address and clicks the "Subscribe" button, the following occurs:

**Implementation:**
```javascript
const subscribeForm = document.getElementById('subscribe-form');
subscribeForm.addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Thank you for subscribing.');
    emailInput.value = '';
});
```

**Functionality:**
1. An event listener is attached to the subscribe form's submit event
2. The default form submission behavior is prevented using `e.preventDefault()`
3. An alert window displays the message: **"Thank you for subscribing."**
4. The email input field is cleared after successful subscription

The HTML5 `required` attribute on the email input ensures that users must enter a valid email format before the alert is triggered.

---

### Gallery Page: Add to Cart Button
Each product on the Gallery page has an "Add to Cart" button that triggers an alert when clicked.

**Implementation:**
```javascript
function addToCart(itemName, itemPrice) {
    // Store item in sessionStorage (for Task 3.2)
    sessionStorage.setItem(itemName, JSON.stringify({
        name: itemName,
        price: itemPrice,
        quantity: 1
    }));
    alert('Item added to the cart.');
}
```

**Functionality:**
1. The button calls the `addToCart()` function with the product name and price as parameters
2. An alert window displays the message: **"Item added to the cart."**
3. The item data is stored in sessionStorage for the shopping cart functionality (implemented in Task 3.2)

---

### Gallery Page: Clear Cart Button
The "Clear Cart" button inside the shopping cart modal clears all items from the cart.

**Implementation:**
```javascript
clearCartBtn.addEventListener('click', function() {
    sessionStorage.clear();
    alert('Cart cleared.');
    displayCartItems();
});
```

**Functionality:**
1. An event listener is attached to the Clear Cart button's click event
2. All items in sessionStorage are cleared
3. An alert window displays the message: **"Cart cleared."**
4. The cart display is updated to show an empty cart

---

### Gallery Page: Process Order Button
The "Process Order" button inside the shopping cart modal processes the customer's order.

**Implementation:**
```javascript
processOrderBtn.addEventListener('click', function() {
    if (sessionStorage.length > 0) {
        alert('Thank you for your order.');
        sessionStorage.clear();
        displayCartItems();
        cartModal.classList.remove('active');
    } else {
        alert('Your cart is empty. Please add items before processing an order.');
    }
});
```

**Functionality:**
1. An event listener is attached to the Process Order button's click event
2. If the cart contains items, an alert window displays: **"Thank you for your order."**
3. All items in sessionStorage are cleared after the order is processed
4. The modal window closes automatically
5. If the cart is empty, a different message alerts the user to add items first

---

### About Us Page: Form Submission
The contact form on the About Us page includes a Submit button that triggers an alert when the form is submitted.

**Implementation:**
```javascript
contactForm.addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Collect form data
    const formData = {
        name: document.getElementById('customer-name').value,
        email: document.getElementById('customer-email').value,
        address: document.getElementById('customer-address').value,
        phone: document.getElementById('customer-phone').value,
        message: document.getElementById('customer-message').value,
        isCustomOrder: document.getElementById('custom-order').checked
    };

    // Save to localStorage (for Task 3.2)
    localStorage.setItem('latestOrder', JSON.stringify(formData));
    
    alert('Thank you for your message.');
    contactForm.reset();
});
```

**Functionality:**
1. An event listener is attached to the contact form's submit event
2. The default form submission behavior is prevented
3. Form data is collected into a JavaScript object
4. The data is saved to localStorage (implemented in Task 3.2)
5. An alert window displays: **"Thank you for your message."**
6. The form is reset to clear all input fields

HTML5 form validation ensures that required fields (Name, Email, Message) are filled before submission. If validation fails, the browser's default validation messages appear instead of the alert.

---

## Screenshots Required for Task 3.1:
1. **Subscribe alert** - Screenshot showing the "Thank you for subscribing." alert
2. **Add to Cart alert** - Screenshot showing the "Item added to the cart." alert
3. **Clear Cart alert** - Screenshot showing the "Cart cleared." alert
4. **Process Order alert** - Screenshot showing the "Thank you for your order." alert
5. **Form Submit alert** - Screenshot showing the "Thank you for your message." alert
6. **Form validation** - Screenshot showing HTML5 validation error (e.g., empty required field)

---

## Issues Encountered
I did not encounter any significant issues while implementing the JavaScript functionality. All event listeners are properly attached and all alert messages display correctly. The `e.preventDefault()` method successfully prevents default form submissions and page reloads.

All JavaScript components function as intended.
