/* ============================================================================
   KISAAN_SATHI — GOVERNMENT PORTAL LAYER
   Hero carousel, accessibility toolbar, portal behaviours.
   Loaded BEFORE app.js so all app logic stays untouched.
   ========================================================================== */
(function () {
  "use strict";

  /* ------------------------------------------------------------------
     1. HERO CAROUSEL — auto-slide, dots, arrows, pause on hover, swipe
  ------------------------------------------------------------------ */
  function initCarousel() {
    const carousel = document.getElementById("govCarousel");
    if (!carousel) return;
    const slides = Array.from(carousel.querySelectorAll(".gov-slide"));
    const dotsWrap = carousel.querySelector(".car-dots");
    let idx = 0, timer = null, AUTOPLAY_MS = 5500;

    if (!slides.length || !dotsWrap) return;

    const dots = slides.map(function (_, i) {
      const b = document.createElement("button");
      b.className = "car-dot" + (i === 0 ? " active" : "");
      b.setAttribute("aria-label", "Slide " + (i + 1));
      b.addEventListener("click", function () { go(i); restart(); });
      dotsWrap.appendChild(b);
      return b;
    });

    function go(i) {
      idx = (i + slides.length) % slides.length;
      slides.forEach(function (s, k) { s.classList.toggle("active", k === idx); });
      dots.forEach(function (d, k) { d.classList.toggle("active", k === idx); });
    }
    function next() { go(idx + 1); }
    function prev() { go(idx - 1); }
    function start() { timer = setInterval(next, AUTOPLAY_MS); }
    function stop() { if (timer) { clearInterval(timer); timer = null; } }
    function restart() { stop(); start(); }

    const prevBtn = carousel.querySelector(".car-prev");
    const nextBtn = carousel.querySelector(".car-next");
    if (prevBtn) prevBtn.addEventListener("click", function () { prev(); restart(); });
    if (nextBtn) nextBtn.addEventListener("click", function () { next(); restart(); });

    carousel.addEventListener("mouseenter", stop);
    carousel.addEventListener("mouseleave", start);

    // Touch swipe
    let touchX = null;
    carousel.addEventListener("touchstart", function (e) { touchX = e.touches[0].clientX; }, { passive: true });
    carousel.addEventListener("touchend", function (e) {
      if (touchX === null) return;
      const dx = e.changedTouches[0].clientX - touchX;
      if (Math.abs(dx) > 40) { (dx < 0 ? next : prev)(); restart(); }
      touchX = null;
    }, { passive: true });

    go(0);
    start();
  }

  /* ------------------------------------------------------------------
     2. ACCESSIBILITY TOOLBAR — font scaling + high contrast (persisted)
  ------------------------------------------------------------------ */
  function initA11y() {
    const root = document.documentElement;
    const savedFont = localStorage.getItem("gov_font_step") || "0";
    const savedContrast = localStorage.getItem("gov_contrast") === "1";

    function applyFont(step) {
      root.classList.remove("gov-font-lg", "gov-font-xl");
      if (step === "1") root.classList.add("gov-font-lg");
      if (step === "2") root.classList.add("gov-font-xl");
      localStorage.setItem("gov_font_step", step);
    }
    function applyContrast(on) {
      document.body.classList.toggle("gov-contrast", on);
      localStorage.setItem("gov_contrast", on ? "1" : "0");
      const btn = document.getElementById("a11yContrast");
      if (btn) btn.setAttribute("aria-pressed", on ? "true" : "false");
    }

    applyFont(savedFont);
    applyContrast(savedContrast);

    const bind = function (id, fn) {
      const el = document.getElementById(id);
      if (el) el.addEventListener("click", fn);
    };
    bind("a11yFontReset", function () { applyFont("0"); });
    bind("a11yFontLg", function () { applyFont("1"); });
    bind("a11yFontXl", function () { applyFont("2"); });
    bind("a11yContrast", function () {
      applyContrast(!document.body.classList.contains("gov-contrast"));
    });
  }

  /* ------------------------------------------------------------------
     3. Portal boot
  ------------------------------------------------------------------ */
  document.addEventListener("DOMContentLoaded", function () {
    document.body.classList.add("gov-theme");
    initCarousel();
    initA11y();

    // Quick services cards scroll to the matching app tab
    document.querySelectorAll(".gov-qs-card[data-target-tab]").forEach(function (card) {
      card.addEventListener("click", function () {
        const tabBtn = document.querySelector(
          '.tab-btn[data-tab="' + card.getAttribute("data-target-tab") + '"]'
        );
        if (tabBtn) tabBtn.click();
        const nav = document.querySelector(".nav-tabs");
        if (nav) nav.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    });
  });
})();
