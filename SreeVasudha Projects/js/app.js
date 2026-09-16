/* ============================================================
   SHREE VASUDHA PROJECTS — Core JavaScript
   Scroll animations, smooth interactions, and utilities.
   ============================================================ */

'use strict';

document.addEventListener('DOMContentLoaded', () => {

  /* --------------------------------------------------------
     SCROLL REVEAL — IntersectionObserver
     Reveals .reveal elements as they enter the viewport.
     -------------------------------------------------------- */

  const revealElements = document.querySelectorAll(
    '.reveal, .reveal--left, .reveal--right, .reveal--scale, .stagger-children'
  );

  if (revealElements.length > 0 && 'IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            revealObserver.unobserve(entry.target);
          }
        });
      },
      {
        threshold: 0.12,
        rootMargin: '0px 0px -60px 0px',
      }
    );

    revealElements.forEach((el) => revealObserver.observe(el));
  } else {
    /* Fallback: show everything immediately */
    revealElements.forEach((el) => el.classList.add('is-visible'));
  }


  /* --------------------------------------------------------
     NAVBAR — Scroll behaviour
     Adds solid background when scrolled past threshold.
     -------------------------------------------------------- */

  const navbar = document.getElementById('navbar');

  if (navbar) {
    const SCROLL_THRESHOLD = 80;
    let lastKnownScroll = 0;
    let ticking = false;

    const updateNavbar = () => {
      if (lastKnownScroll > SCROLL_THRESHOLD) {
        navbar.classList.add('navbar--scrolled');
      } else {
        navbar.classList.remove('navbar--scrolled');
      }
      ticking = false;
    };

    window.addEventListener('scroll', () => {
      lastKnownScroll = window.scrollY;
      if (!ticking) {
        window.requestAnimationFrame(updateNavbar);
        ticking = true;
      }
    }, { passive: true });

    /* Initial check */
    lastKnownScroll = window.scrollY;
    updateNavbar();
  }


  /* --------------------------------------------------------
     SMOOTH SCROLL — Anchor links
     -------------------------------------------------------- */

  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', (e) => {
      const targetId = anchor.getAttribute('href');
      if (targetId === '#') return;

      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        const navbarHeight = navbar ? navbar.offsetHeight : 0;
        const targetPosition = target.getBoundingClientRect().top + window.scrollY - navbarHeight - 20;

        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth',
        });

        /* Close mobile menu if open */
        const mobileMenu = document.getElementById('mobile-menu');
        if (mobileMenu && mobileMenu.classList.contains('is-open')) {
          mobileMenu.classList.remove('is-open');
          document.body.style.overflow = '';
        }
      }
    });
  });


  /* --------------------------------------------------------
     MOBILE MENU TOGGLE
     -------------------------------------------------------- */

  const menuToggle = document.getElementById('menu-toggle');
  const mobileMenu = document.getElementById('mobile-menu');

  if (menuToggle && mobileMenu) {
    menuToggle.addEventListener('click', () => {
      const isOpen = mobileMenu.classList.toggle('is-open');
      menuToggle.classList.toggle('is-active');
      menuToggle.setAttribute('aria-expanded', isOpen);
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });
  }

  const mobileDropdownToggles = document.querySelectorAll('.mobile-menu__dropdown-toggle');
  mobileDropdownToggles.forEach(toggle => {
    toggle.addEventListener('click', (e) => {
      e.preventDefault();
      const parent = toggle.closest('.mobile-menu__dropdown');
      parent.classList.toggle('is-active');
      const expanded = toggle.getAttribute('aria-expanded') === 'true' || false;
      toggle.setAttribute('aria-expanded', !expanded);
    });
  });


  /* --------------------------------------------------------
     COUNTER ANIMATION
     Animates numbers from 0 to target on scroll.
     -------------------------------------------------------- */

  const counters = document.querySelectorAll('[data-count]');

  if (counters.length > 0 && 'IntersectionObserver' in window) {
    const counterObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            animateCounter(entry.target);
            counterObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.5 }
    );

    counters.forEach((counter) => counterObserver.observe(counter));
  }

  function animateCounter(el) {
    const target = parseInt(el.getAttribute('data-count'), 10);
    const suffix = el.getAttribute('data-suffix') || '';
    const prefix = el.getAttribute('data-prefix') || '';
    const duration = 2000;
    const startTime = performance.now();

    function updateCount(currentTime) {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);

      /* Ease out cubic */
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = Math.round(eased * target);

      el.textContent = prefix + current.toLocaleString() + suffix;

      if (progress < 1) {
        requestAnimationFrame(updateCount);
      }
    }

    requestAnimationFrame(updateCount);
  }


  /* --------------------------------------------------------
     PARALLAX (lightweight)
     Moves .parallax-bg elements on scroll.
     -------------------------------------------------------- */

  const parallaxElements = document.querySelectorAll('.parallax-bg');

  if (parallaxElements.length > 0) {
    let pTicking = false;

    window.addEventListener('scroll', () => {
      if (!pTicking) {
        window.requestAnimationFrame(() => {
          const scrollY = window.scrollY;
          parallaxElements.forEach((el) => {
            const parent = el.closest('.parallax-wrapper');
            if (parent) {
              const rect = parent.getBoundingClientRect();
              if (rect.bottom > 0 && rect.top < window.innerHeight) {
                const speed = parseFloat(el.dataset.speed) || 0.3;
                const yPos = -(scrollY - parent.offsetTop) * speed;
                el.style.transform = `translateY(${yPos}px)`;
              }
            }
          });
          pTicking = false;
        });
        pTicking = true;
      }
    }, { passive: true });
  }


  /* --------------------------------------------------------
     CURRENT YEAR — Footer copyright
     -------------------------------------------------------- */

  const yearEl = document.getElementById('current-year');
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

});
