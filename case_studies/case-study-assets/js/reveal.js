/* ==========================================================================
   Wolfpack case studies — scroll reveal + scroll-spy. No dependencies.

   Copied byte for byte from sm3-assets/js/reveal.js, which was copied from
   hire/assets/js/reveal.js. Only this header comment differs. Copying rather
   than rewriting is the point: the reveal timing and the scroll-spy behavior
   are supposed to be identical across every long-form page in this repo, and
   a rewrite is how two pages quietly stop matching. Shared by every case study
   in case_studies/.

   Two non-negotiables, both load-bearing:

   1. The `.js` class is added HERE, and the hidden initial state in the
      stylesheets is scoped to it. With JavaScript off, broken, or blocked,
      every element renders visible and the page is complete. A document that
      requires JS to be readable is a broken document.

   2. prefers-reduced-motion: reduce means the observers never attach at all.
      The CSS also neutralises the transitions, so this is belt and braces.
   ========================================================================== */

(function () {
  'use strict';

  var reduced = window.matchMedia &&
                window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // No IntersectionObserver (or motion declined) → leave the page in its
  // final, fully-visible state. Never add `.js` in that case.
  if (reduced || !('IntersectionObserver' in window)) return;

  var root = document.documentElement;
  root.classList.add('js');

  /* ---- Reveal ---------------------------------------------------------- */

  var revealables = document.querySelectorAll('.reveal');

  // Stagger is per-parent, so each section counts from zero. A single running
  // index across the page would leave late sections with absurd delays.
  var seen = new Map();
  revealables.forEach(function (el) {
    var parent = el.parentNode;
    var n = seen.get(parent) || 0;
    seen.set(parent, n + 1);
    el.style.setProperty('--d', Math.min(n, 6) * 60 + 'ms');
  });

  var revealObserver = new IntersectionObserver(function (entries, obs) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-in');
      obs.unobserve(entry.target);   // fires once; no re-animation on scroll-back
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -8% 0px' });

  revealables.forEach(function (el) { revealObserver.observe(el); });

  /* ---- Scroll-spy ------------------------------------------------------ */

  var links = Array.prototype.slice.call(
    document.querySelectorAll('.nav__links a[href^="#"]')
  );
  if (!links.length) return;

  var byId = {};
  var targets = [];
  links.forEach(function (link) {
    var id = link.getAttribute('href').slice(1);
    var section = document.getElementById(id);
    if (!section) return;
    byId[id] = link;
    targets.push(section);
  });

  function setCurrent(id) {
    links.forEach(function (link) { link.removeAttribute('aria-current'); });
    if (byId[id]) byId[id].setAttribute('aria-current', 'true');
  }

  // Track visibility ratios rather than reacting to each crossing: with long
  // sections, several are on screen at once and "most visible wins" is the
  // only reading that matches what the eye is actually on.
  var ratios = {};
  var spyObserver = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      ratios[entry.target.id] = entry.isIntersecting ? entry.intersectionRatio : 0;
    });

    var best = null, bestRatio = 0;
    Object.keys(ratios).forEach(function (id) {
      if (ratios[id] > bestRatio) { bestRatio = ratios[id]; best = id; }
    });
    if (best) setCurrent(best);
  }, {
    threshold: [0, 0.15, 0.35, 0.6, 0.85],
    rootMargin: '-58px 0px -45% 0px'   // -58px clears the sticky nav
  });

  targets.forEach(function (section) { spyObserver.observe(section); });
}());
