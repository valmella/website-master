// carrito.js
let cart = JSON.parse(localStorage.getItem("cart")) || [];

function updateCart() {
    const cartList = document.getElementById('cart-list');
    const cartTotal = document.getElementById('cart-total');
    cartList.innerHTML = ''; // Limpiar la lista de productos

    let total = 0;
    cart.forEach(item => {
        const li = document.createElement('li');
        li.className = 'list-group-item d-flex justify-content-between align-items-center';
        li.innerHTML = `${item.nombre} - $${item.precio}`;
        total += item.precio;
        cartList.appendChild(li);
    });

    cartTotal.textContent = total;
    document.getElementById('cart-count').textContent = cart.length;
}

function clearCart() {
    cart = [];
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCart();
}

function checkout() {
    // Lógica para realizar la compra
    alert("Compra confirmada.");
    cart = [];
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCart();
}

updateCart(); // Actualizar el carrito al cargar la página
