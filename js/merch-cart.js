/**
 * merch-cart.js — Me Gusta Sucre WhatsApp Mini-Cart
 * Allows users to add/remove items and send a consolidated WhatsApp order.
 */

const WHATSAPP_NUMBER = '59173425725';

// Price map — keyed by product prefix
const PRICES = {
  'tee':        18,
  'tote':       22,
  'mug':        12,
  'hoodie':     35,
  'book':       15,   // books $15–$17; we show 15 as reference
  'coupon':      0,   // variable; shown as "custom"
};

function getPrice(id) {
  for (const key of Object.keys(PRICES)) {
    if (id === key || id.startsWith(key + '-')) return PRICES[key];
  }
  return 0;
}

let cart = []; // Array of { id, name, qty, price }
const selectedSizes = {}; // { productId: 'M' }

// ─── Toasts ───────────────────────────────────────────────────────────────────
function showToast(productName) {
  const container = document.getElementById('toast-container');
  if (!container) return;
  const lang = document.documentElement.getAttribute('data-lang') || 'en';
  const t    = window.translations?.[lang]?.merchandising || {};
  const addedText = t.toastAdded || 'Added';

  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.innerHTML = `<div class="toast-icon">✓</div><span>${productName} — <span style="color:#b09a80;font-weight:400">${addedText}</span></span>`;
  container.appendChild(toast);

  setTimeout(() => toast.classList.add('show'), 10);
  setTimeout(() => {
    toast.classList.remove('show');
    setTimeout(() => toast.remove(), 300);
  }, 3000);
}

// ─── Size Selection ───────────────────────────────────────────────────────────

function selectSize(productId, size, btnEl) {
  selectedSizes[productId] = size;
  const picker = document.getElementById('size-' + productId);
  if (picker) {
    picker.querySelectorAll('.size-btn').forEach(b => b.classList.remove('selected'));
    btnEl.classList.add('selected');
  }
  const err = document.getElementById('size-err-' + productId);
  if (err) err.style.display = 'none';
}

function addToCartWithSize(productId) {
  const size = selectedSizes[productId];
  if (!size) {
    const err = document.getElementById('size-err-' + productId);
    if (err) err.style.display = 'block';
    return;
  }
  const btn  = document.querySelector('[data-product="' + productId + '"]');
  const base = btn ? btn.getAttribute('data-name') : productId;
  const name = base + ' \u2014 ' + size;
  addToCart(productId + '-' + size, name, getPrice(productId));
}

// ─── Book Selection ───────────────────────────────────────────────────────────

function addToCartWithBook() {
  const sel = document.getElementById('picker-book-select');
  if (!sel || !sel.value) {
    const err = document.getElementById('size-err-book');
    if (err) err.style.display = 'block';
    return;
  }
  const bookId    = sel.value;
  const bookLabel = sel.options[sel.selectedIndex].text;
  const err = document.getElementById('size-err-book');
  if (err) err.style.display = 'none';
  addToCart('book-' + bookId, bookLabel, getPrice('book'));
}

// ─── Coupon (Business + Amount) ───────────────────────────────────────────────

function addToCartWithCoupon() {
  const business = selectedSizes['coupon'];
  const amount   = selectedSizes['couponamount'];
  const err      = document.getElementById('size-err-coupon');
  if (!business || !amount) {
    if (err) err.style.display = 'block';
    return;
  }
  if (err) err.style.display = 'none';
  const name  = 'Me Gusta Gift Coupon \u2014 ' + business + ' \u00b7 ' + amount;
  const price = parseInt(amount.replace('$', ''), 10) || 0;
  addToCart('coupon-' + business + '-' + amount, name, price);
}

// ─── DOM Refs ─────────────────────────────────────────────────────────────────
const fab        = document.getElementById('cart-fab');
const fabCount   = document.getElementById('cart-fab-count');
const modal      = document.getElementById('cart-modal');
const modalList  = document.getElementById('cart-modal-list');
const modalEmpty = document.getElementById('cart-modal-empty');
const modalTotal = document.getElementById('cart-modal-total');
const sendBtn    = document.getElementById('cart-send-btn');

// ─── Core Cart Logic ──────────────────────────────────────────────────────────

function addToCart(id, name, price = 0) {
  const existing = cart.find(i => i.id === id);
  if (existing) {
    existing.qty++;
  } else {
    cart.push({ id, name, qty: 1, price });
  }
  updateUI();
  animateBtn(id.split('-')[0]);
  showToast(name);
}

function removeFromCart(id) {
  const idx = cart.findIndex(i => i.id === id);
  if (idx === -1) return;
  if (cart[idx].qty > 1) {
    cart[idx].qty--;
  } else {
    cart.splice(idx, 1);
  }
  updateUI();
}

function deleteFromCart(id) {
  cart = cart.filter(i => i.id !== id);
  updateUI();
}

function getTotalQty() {
  return cart.reduce((sum, i) => sum + i.qty, 0);
}

function getTotalPrice() {
  return cart.reduce((sum, i) => sum + i.qty * i.price, 0);
}

// ─── UI Updates ───────────────────────────────────────────────────────────────

function updateUI() {
  const total = getTotalQty();
  if (total > 0) {
    fab.classList.add('cart-fab--visible');
  } else {
    fab.classList.remove('cart-fab--visible');
    closeModal();
  }
  fabCount.textContent = total;
  renderModalList();
}

function renderModalList() {
  const total      = getTotalQty();
  const totalPrice = getTotalPrice();
  const lang       = document.documentElement.getAttribute('data-lang') || 'en';
  const t          = window.translations?.[lang]?.merchandising || {};

  if (cart.length === 0) {
    modalList.innerHTML = '';
    modalEmpty.style.display = 'block';
    modalTotal.style.display = 'none';
    document.getElementById('cart-contact-form').classList.remove('visible');
    sendBtn.disabled = true;
  } else {
    modalEmpty.style.display = 'none';
    modalTotal.style.display = 'block';
    document.getElementById('cart-contact-form').classList.add('visible');
    sendBtn.disabled = false;

    modalList.innerHTML = cart.map(item => {
      const safeName = item.name.replace(/\\/g, '\\\\').replace(/'/g, "\\'");
      const priceStr = item.price > 0 ? '$' + (item.price * item.qty) : '';
      return `
      <div class="cart-item" data-id="${item.id}">
        <div class="cart-item-controls">
          <button class="cart-qty-btn" onclick="removeFromCart('${item.id}')" title="Remove one">−</button>
          <span class="cart-qty-num">${item.qty}</span>
          <button class="cart-qty-btn" onclick="addToCart('${item.id}', '${safeName}', ${item.price})" title="Add one">+</button>
        </div>
        <span class="cart-item-name">${item.name}</span>
        <div class="cart-item-right">
          <span class="cart-item-price">${priceStr}</span>
          <button class="cart-delete-btn" onclick="deleteFromCart('${item.id}')" title="Remove">✕</button>
        </div>
      </div>`;
    }).join('');

    // Summary bar
    const hasPrices = cart.some(i => i.price > 0);
    modalTotal.innerHTML = `
      <div class="cart-summary">
        <span>${total} item${total !== 1 ? 's' : ''}</span>
        ${hasPrices ? `<span class="cart-summary-total">~$${totalPrice} <span style="font-weight:400;font-size:11px;opacity:0.65">USD</span></span>` : ''}
      </div>
    `;
  }
}

// ─── Modal Open/Close ─────────────────────────────────────────────────────────

function openModal() {
  renderModalList();
  modal.classList.add('cart-modal--open');
  document.getElementById('cart-modal-overlay').classList.add('cart-overlay--open');
}

function closeModal() {
  modal.classList.remove('cart-modal--open');
  document.getElementById('cart-modal-overlay').classList.remove('cart-overlay--open');
}

// ─── WhatsApp Dispatch ────────────────────────────────────────────────────────

function sendOrder() {
  if (cart.length === 0) return;

  const deliverySelect  = document.getElementById('cart-delivery-method');
  const addressInput    = document.getElementById('cart-address');
  const errText         = document.getElementById('cart-form-err');
  const isDelivery      = deliverySelect.value === 'delivery';
  const customerAddress = addressInput.value.trim();

  if (isDelivery && !customerAddress) {
    errText.style.display = 'block';
    return;
  }
  errText.style.display = 'none';

  // ── Build item list ──────────────────────────────────────────────────────
  const totalQty   = getTotalQty();
  const totalPrice = getTotalPrice();
  const hasPrices  = cart.some(i => i.price > 0);

  const itemLines = cart.map(i => {
    const subtotal = i.price > 0 ? ` ($${i.price * i.qty})` : '';
    return `   • ${i.qty}x ${i.name}${subtotal}`;
  }).join('\n');

  const totalLine = hasPrices ? `\n💰 *Estimated Total: ~$${totalPrice} USD*` : '';

  // ── Delivery block ───────────────────────────────────────────────────────
  const methodLine = isDelivery
    ? `🚚 Shipping in Bolivia\n   📍 ${customerAddress}`
    : `🏫 Pickup at Me Gusta Spanish School\n   📍 Audiencia #97, Sucre`;

  // ── Compose message ──────────────────────────────────────────────────────
  const message =
`👋 Hello! I'd like to place an order from *Me Gusta Sucre* 🛍️

━━━━━━━━━━━━━━━━
🛒 *My Order* (${totalQty} item${totalQty !== 1 ? 's' : ''})
━━━━━━━━━━━━━━━━
${itemLines}
${totalLine}

━━━━━━━━━━━━━━━━
📦 *Delivery Method*
━━━━━━━━━━━━━━━━
${methodLine}

━━━━━━━━━━━━━━━━
Please confirm availability and let me know the final total. Thank you! 🙏`;

  window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`, '_blank');
}

// ─── Button animation ─────────────────────────────────────────────────────────

function animateBtn(id) {
  const btn = document.querySelector(`[data-product="${id}"]`);
  if (!btn) return;
  btn.classList.add('btn-added');
  setTimeout(() => btn.classList.remove('btn-added'), 800);
}

// ─── Language Change Listener ─────────────────────────────────────────────────
document.addEventListener('langChanged', () => {
  renderModalList();
});

// ─── Init ─────────────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  updateUI();
});
