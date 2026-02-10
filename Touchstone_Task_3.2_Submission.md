# Touchstone Task 3.2: Storing Data With Web Storage

**Name:** [Your Name]
**Date:** February 9, 2026

---

## Web Storage Implementation

### Overview
The website utilizes both **sessionStorage** and **localStorage** to provide persistent data functionality:
- **sessionStorage**: Used for the shopping cart feature (data persists during the browser session)
- **localStorage**: Used for customer contact/order information (data persists permanently)

---

## Shopping Cart Feature (sessionStorage)

### Add to Cart Functionality
When a user clicks the "Add to Cart" button for any product on the Gallery page, the item is stored in sessionStorage.

**Implementation:**
```javascript
function addToCart(itemName, itemPrice) {
    const item = {
        name: itemName,
        price: itemPrice,
        quantity: 1,
        addedAt: new Date().toISOString()
    };

    // Check if item already exists
    const existingItem = sessionStorage.getItem(itemName);
    if (existingItem) {
        const parsedItem = JSON.parse(existingItem);
        parsedItem.quantity += 1;
        sessionStorage.setItem(itemName, JSON.stringify(parsedItem));
    } else {
        sessionStorage.setItem(itemName, JSON.stringify(item));
    }

    alert('Item added to the cart.');
}
```

**Functionality:**
1. When "Add to Cart" is clicked, an item object is created containing the name, price, quantity, and timestamp
2. The function checks if the item already exists in sessionStorage
3. If the item exists, the quantity is incremented
4. If the item is new, it is added to sessionStorage
5. Data is stored as a JSON string using `JSON.stringify()`

---

### View Cart Functionality
When the user clicks the "View Cart" button, a modal window opens displaying all items currently in the shopping cart.

**Implementation:**
```javascript
function displayCartItems() {
    const cartItemsContainer = document.getElementById('cart-items');
    const cartTotalElement = document.getElementById('cart-total');
    
    cartItemsContainer.innerHTML = '';
    let total = 0;

    if (sessionStorage.length === 0) {
        cartItemsContainer.innerHTML = '<p>Your cart is empty.</p>';
        cartTotalElement.textContent = '$0.00';
        return;
    }

    for (let i = 0; i < sessionStorage.length; i++) {
        const key = sessionStorage.key(i);
        const item = JSON.parse(sessionStorage.getItem(key));
        
        const itemTotal = item.price * item.quantity;
        total += itemTotal;
        
        const itemDiv = document.createElement('div');
        itemDiv.className = 'cart-item';
        itemDiv.innerHTML = `
            <span>${item.name} (x${item.quantity})</span>
            <span>$${itemTotal.toFixed(2)}</span>
        `;
        cartItemsContainer.appendChild(itemDiv);
    }

    cartTotalElement.textContent = '$' + total.toFixed(2);
}
```

**Functionality:**
1. The function iterates through all items in sessionStorage using `sessionStorage.length` and `sessionStorage.key(i)`
2. Each item is retrieved using `sessionStorage.getItem(key)` and parsed from JSON
3. Item details (name, quantity, price) are dynamically rendered in the modal window
4. The total price is calculated and displayed at the bottom of the modal

---

### Clear Cart Functionality
When the user clicks the "Clear Cart" button inside the modal, all items are removed from sessionStorage.

**Implementation:**
```javascript
clearCartBtn.addEventListener('click', function() {
    sessionStorage.clear();
    alert('Cart cleared.');
    displayCartItems();
});
```

**Functionality:**
1. `sessionStorage.clear()` removes all items from the session storage
2. An alert confirms the action
3. The cart display is refreshed to show the empty state

---

### Process Order Functionality
When the user clicks the "Process Order" button, the order is finalized and the cart is cleared.

**Implementation:**
```javascript
processOrderBtn.addEventListener('click', function() {
    if (sessionStorage.length > 0) {
        alert('Thank you for your order.');
        sessionStorage.clear();
        displayCartItems();
        cartModal.classList.remove('active');
    }
});
```

**Functionality:**
1. If the cart has items, the order is processed
2. All items are cleared from sessionStorage
3. The modal is closed automatically

---

## Custom Order Feature (localStorage)

### Contact Form Storage
When the user submits the contact form on the About Us page, all form data is saved to localStorage for permanent storage.

**Implementation:**
```javascript
contactForm.addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formData = {
        name: document.getElementById('customer-name').value,
        email: document.getElementById('customer-email').value,
        address: document.getElementById('customer-address').value,
        phone: document.getElementById('customer-phone').value,
        message: document.getElementById('customer-message').value,
        isCustomOrder: document.getElementById('custom-order').checked,
        timestamp: new Date().toISOString()
    };

    // Store as single latest order
    localStorage.setItem('latestOrder', JSON.stringify(formData));
    
    // Also maintain an array of all orders
    const existingOrders = JSON.parse(localStorage.getItem('customerOrders') || '[]');
    existingOrders.push(formData);
    localStorage.setItem('customerOrders', JSON.stringify(existingOrders));

    alert('Thank you for your message.');
    contactForm.reset();
});
```

**Functionality:**
1. When the form is submitted, all input values are collected into a formData object
2. A timestamp is added for record-keeping
3. The latest order is stored in localStorage under the key 'latestOrder'
4. An array of all customer orders is maintained under the key 'customerOrders'
5. Data persists even after the browser is closed and reopened
6. The form is reset after successful submission

---

## sessionStorage vs localStorage

| Feature | sessionStorage | localStorage |
|---------|----------------|--------------|
| Persistence | Browser session only | Permanent (until cleared) |
| Use Case | Shopping cart | Customer orders |
| Capacity | ~5MB | ~5-10MB |
| Scope | Per tab/window | Same origin |

**Rationale:**
- **sessionStorage** is appropriate for the shopping cart because cart items should not persist after the user closes the browser. Each shopping session should start fresh.
- **localStorage** is appropriate for customer orders because the business may need to reference past orders, and the data should persist across browser sessions.

---

## Screenshots Required for Task 3.2:
1. **Add item to cart** - Show the alert after clicking "Add to Cart"
2. **View Cart modal with items** - Show the modal displaying added items
3. **sessionStorage in DevTools** - Open DevTools (F12) > Application > Session Storage to show stored items
4. **Clear Cart** - Show the modal after clearing (empty state)
5. **sessionStorage after clear** - Show empty sessionStorage in DevTools
6. **Process Order** - Show the thank you alert
7. **sessionStorage after process** - Show empty sessionStorage after order is processed
8. **Contact form filled** - Show the form with sample data entered
9. **Form submission alert** - Show "Thank you for your message" alert
10. **localStorage in DevTools** - Open DevTools > Application > Local Storage to show stored customer data

---

## Issues Encountered
I did not encounter any significant issues while implementing the web storage functionality. Both sessionStorage and localStorage work correctly for storing and retrieving JSON data.

All web storage components function as intended.
