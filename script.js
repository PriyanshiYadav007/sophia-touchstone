/* ============================================
   Bloom Valley Nursery - JavaScript
   Touchstone 3.1: Alerts
   Touchstone 3.2: Web Storage
   ============================================ */

// ============================================
// Subscribe Feature (All Pages)
// ============================================
document.addEventListener('DOMContentLoaded', function() {
    // Subscribe button functionality
    const subscribeForm = document.getElementById('subscribe-form');
    if (subscribeForm) {
        subscribeForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const emailInput = document.getElementById('subscribe-email');
            if (emailInput && emailInput.value) {
                alert('Thank you for subscribing.');
                emailInput.value = '';
            }
        });
    }

    // ============================================
    // Shopping Cart Feature (Gallery Page)
    // ============================================
    
    // View Cart Modal
    const viewCartBtn = document.getElementById('view-cart-btn');
    const cartModal = document.getElementById('cart-modal');
    const closeModal = document.getElementById('close-modal');
    const clearCartBtn = document.getElementById('clear-cart-btn');
    const processOrderBtn = document.getElementById('process-order-btn');

    // Open cart modal
    if (viewCartBtn) {
        viewCartBtn.addEventListener('click', function() {
            displayCartItems();
            cartModal.classList.add('active');
        });
    }

    // Close modal with X button
    if (closeModal) {
        closeModal.addEventListener('click', function() {
            cartModal.classList.remove('active');
        });
    }

    // Close modal when clicking outside
    if (cartModal) {
        cartModal.addEventListener('click', function(e) {
            if (e.target === cartModal) {
                cartModal.classList.remove('active');
            }
        });
    }

    // Clear Cart button
    if (clearCartBtn) {
        clearCartBtn.addEventListener('click', function() {
            sessionStorage.clear();
            alert('Cart cleared.');
            displayCartItems();
        });
    }

    // Process Order button
    if (processOrderBtn) {
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
    }

    // ============================================
    // Contact Form (About Us Page)
    // ============================================
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form values
            const formData = {
                name: document.getElementById('customer-name').value,
                email: document.getElementById('customer-email').value,
                address: document.getElementById('customer-address').value,
                phone: document.getElementById('customer-phone').value,
                message: document.getElementById('customer-message').value,
                isCustomOrder: document.getElementById('custom-order').checked,
                timestamp: new Date().toISOString()
            };

            // Save to localStorage (Touchstone 3.2)
            const existingOrders = JSON.parse(localStorage.getItem('customerOrders') || '[]');
            existingOrders.push(formData);
            localStorage.setItem('customerOrders', JSON.stringify(existingOrders));
            
            // Also save as single latest order for easy access
            localStorage.setItem('latestOrder', JSON.stringify(formData));

            // Show confirmation alert
            alert('Thank you for your message.');
            
            // Reset form
            contactForm.reset();
        });
    }
});

// ============================================
// Add to Cart Function
// ============================================
function addToCart(itemName, itemPrice) {
    // Create item object
    const item = {
        name: itemName,
        price: itemPrice,
        quantity: 1,
        addedAt: new Date().toISOString()
    };

    // Check if item already exists in cart
    const existingItem = sessionStorage.getItem(itemName);
    if (existingItem) {
        const parsedItem = JSON.parse(existingItem);
        parsedItem.quantity += 1;
        sessionStorage.setItem(itemName, JSON.stringify(parsedItem));
    } else {
        sessionStorage.setItem(itemName, JSON.stringify(item));
    }

    // Show alert (Touchstone 3.1)
    alert('Item added to the cart.');
}

// ============================================
// Display Cart Items Function
// ============================================
function displayCartItems() {
    const cartItemsContainer = document.getElementById('cart-items');
    const cartTotalElement = document.getElementById('cart-total');
    
    if (!cartItemsContainer || !cartTotalElement) return;

    // Clear current display
    cartItemsContainer.innerHTML = '';
    let total = 0;

    // Check if cart is empty
    if (sessionStorage.length === 0) {
        cartItemsContainer.innerHTML = '<p style="text-align: center; color: #666;">Your cart is empty.</p>';
        cartTotalElement.textContent = '$0.00';
        return;
    }

    // Loop through sessionStorage and display items
    for (let i = 0; i < sessionStorage.length; i++) {
        const key = sessionStorage.key(i);
        const item = JSON.parse(sessionStorage.getItem(key));
        
        const itemDiv = document.createElement('div');
        itemDiv.className = 'cart-item';
        
        const itemTotal = item.price * item.quantity;
        total += itemTotal;
        
        itemDiv.innerHTML = `
            <span class="item-name">${item.name} (x${item.quantity})</span>
            <span class="item-price">$${itemTotal.toFixed(2)}</span>
        `;
        
        cartItemsContainer.appendChild(itemDiv);
    }

    // Update total
    cartTotalElement.textContent = '$' + total.toFixed(2);
}

// ============================================
// Clear Form Function (About Us Page)
// ============================================
function clearContactForm() {
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.reset();
    }
}

// ============================================
// Utility Functions
// ============================================

// Get all cart items as array
function getCartItems() {
    const items = [];
    for (let i = 0; i < sessionStorage.length; i++) {
        const key = sessionStorage.key(i);
        items.push(JSON.parse(sessionStorage.getItem(key)));
    }
    return items;
}

// Get cart total
function getCartTotal() {
    let total = 0;
    for (let i = 0; i < sessionStorage.length; i++) {
        const key = sessionStorage.key(i);
        const item = JSON.parse(sessionStorage.getItem(key));
        total += item.price * item.quantity;
    }
    return total;
}

// Get all customer orders from localStorage
function getCustomerOrders() {
    return JSON.parse(localStorage.getItem('customerOrders') || '[]');
}
