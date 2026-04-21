// ═══════════════════════════════════════════════
//  ME GUSTA SUCRE — main.js
// ═══════════════════════════════════════════════

/* ── i18n ── */
function getLang() {
  const params = new URLSearchParams(window.location.search);
  const lang = params.get('lang');
  if (lang && ['en', 'es', 'fr'].includes(lang)) {
    localStorage.setItem('mgs_lang', lang);
    return lang;
  }
  return localStorage.getItem('mgs_lang') || 'en';
}

function setLang(lang) {
  localStorage.setItem('mgs_lang', lang);
  applyTranslations(lang);
  // Update active state on lang buttons
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.lang === lang);
  });
}

function applyTranslations(lang) {
  if (typeof translations === 'undefined') return;
  const t = translations[lang] || translations.en;
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.dataset.i18n;
    const parts = key.split('.');
    let val = t;
    for (const p of parts) { val = val?.[p]; }
    if (val !== undefined && val !== null) el.textContent = val;
  });
  document.querySelectorAll('[data-i18n-html]').forEach(el => {
    const key = el.dataset.i18nHtml;
    const parts = key.split('.');
    let val = t;
    for (const p of parts) { val = val?.[p]; }
    if (val !== undefined && val !== null) el.innerHTML = val;
  });
  document.documentElement.lang = lang;
}

// Init i18n on page load
document.addEventListener('DOMContentLoaded', () => {
  const lang = getLang();
  applyTranslations(lang);
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.lang === lang);
    btn.addEventListener('click', () => setLang(btn.dataset.lang));
  });
});

/* ── Navbar scroll ── */
const navbar = document.getElementById('navbar');
if (navbar) {
  const onScroll = () => {
    if (window.scrollY > 60) {
      navbar.classList.add('scrolled');
      document.body.classList.add('scrolled-past');
    } else {
      navbar.classList.remove('scrolled');
      document.body.classList.remove('scrolled-past');
    }
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

/* ── Mobile menu toggle ── */
const menuBtn = document.getElementById('menu-btn');
const mobileMenu = document.getElementById('mobile-menu');
if (menuBtn && mobileMenu) {
  menuBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
  });
  // Close on link click
  mobileMenu.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => mobileMenu.classList.add('hidden'));
  });
}

/* ── Fade-up on scroll ── */
const fadeEls = document.querySelectorAll('.fade-up');
if (fadeEls.length) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => entry.target.classList.add('visible'), i * 80);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
  fadeEls.forEach(el => observer.observe(el));
}

/* ── Animated counters ── */
function animateCounter(el) {
  const target = parseInt(el.dataset.target, 10);
  const suffix = el.dataset.suffix || '';
  const duration = 1800;
  const start = performance.now();
  const step = (now) => {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    el.textContent = Math.floor(eased * target) + suffix;
    if (progress < 1) requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
}

const counterEls = document.querySelectorAll('.counter');
if (counterEls.length) {
  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        counterObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });
  counterEls.forEach(el => counterObserver.observe(el));
}

/* ── Parallax hero ── */
const heroSection = document.querySelector('.hero-section');
if (heroSection) {
  window.addEventListener('scroll', () => {
    const y = window.scrollY;
    const parallax = heroSection.querySelector('.hero-kenburns');
    if (parallax) parallax.style.transform = `scale(1.08) translateY(${y * 0.3}px)`;
  }, { passive: true });
}

/* ── Active nav link ── */
const currentPage = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav-link').forEach(link => {
  const href = link.getAttribute('href') || '';
  if (href === currentPage || (currentPage === '' && href === 'index.html')) {
    link.classList.add('nav-active');
  }
});

/* ── Lightbox Logic ── */
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');
const lightboxClose = document.getElementById('lightbox-close');
const lightboxCaption = document.getElementById('lightbox-caption');

if (lightbox && lightboxImg) {
  document.querySelectorAll('.expandable').forEach(img => {
    img.style.cursor = 'zoom-in';
    img.addEventListener('click', () => {
      // Set properties
      lightboxImg.src = img.src;
      if (lightboxCaption) {
        lightboxCaption.textContent = img.getAttribute('data-caption') || '';
      }
      
      // Show overlay
      lightbox.classList.remove('hidden');
      lightbox.classList.add('flex');
      
      // Animate entry
      setTimeout(() => {
        lightboxImg.classList.replace('scale-95', 'scale-100');
        if (lightboxCaption) {
          lightboxCaption.classList.remove('opacity-0', 'translate-y-4');
          lightboxCaption.classList.add('opacity-100', 'translate-y-0');
        }
      }, 50);
    });
  });

  const closeLightbox = () => {
    lightboxImg.classList.replace('scale-100', 'scale-95');
    if (lightboxCaption) {
      lightboxCaption.classList.remove('opacity-100', 'translate-y-0');
      lightboxCaption.classList.add('opacity-0', 'translate-y-4');
    }
    
    setTimeout(() => {
      lightbox.classList.remove('flex');
      lightbox.classList.add('hidden');
    }, 300);
  };

  if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox || e.target === lightboxCaption) closeLightbox();
  });
}
