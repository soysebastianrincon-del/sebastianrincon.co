/* =========================================================
   motion.js — capa de movimiento progresiva (va después de main.js)
   - Nunca oculta contenido: las apariciones siguen en CSS + main.js.
   - Partes vanilla en todas las páginas; partes GSAP solo si gsap y
     ScrollTrigger cargaron (inicio, sobre-mí y servicios). Si el CDN falla, no pasa nada.
   ========================================================= */
(function () {
  'use strict';
  var d = document;
  var mq = function (q) { return !!(window.matchMedia && window.matchMedia(q).matches); };
  var reduce = mq('(prefers-reduced-motion: reduce)');
  var hasIO = 'IntersectionObserver' in window;
  var $ = function (s, c) { return (c || d).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || d).querySelectorAll(s)); };

  /* ---------- 0. Barrido de seguridad: un scroll rápido (tecla Fin, salto de ancla)
     puede saltarse el IntersectionObserver de main.js y dejar bloques ocultos ---------- */
  var sweepT, done = false;
  var sweep = function () {
    if (done) return;
    var pending = $$('.rv:not(.in), .portrait:not(.in)');
    if (!pending.length) { done = true; return; }
    var vh = window.innerHeight;
    pending.forEach(function (el) { if (el.getBoundingClientRect().top < vh) el.classList.add('in'); });
  };
  window.addEventListener('scroll', function () {
    if (done) return;
    clearTimeout(sweepT); sweepT = setTimeout(sweep, 150);
  }, { passive: true });

  /* ---------- 1. Marquesina de logos: pausa fuera de pantalla ---------- */
  var track = $('.logo-track'), row = track && $('.logo-row', track);
  if (row && hasIO) {
    new IntersectionObserver(function (es) {
      row.style.animationPlayState = es[0].isIntersecting ? '' : 'paused';
    }).observe(track);
  }

  /* ---------- 2. Video: se pausa si sale de pantalla ---------- */
  if (hasIO) $$('.reel video, .stmt-video video').forEach(function (v) {
    new IntersectionObserver(function (es) {
      if (!es[0].isIntersecting && !v.paused) v.pause();
    }, { threshold: 0.2 }).observe(v);
  });

  /* ---------- 3. Contadores: cifras del ledger, ROAS de los casos y cifras del video.
     Admite separador de miles con punto (+25.000). El texto real está en el HTML
     y se restaura al final. ---------- */
  var fmt = function (n, dots) { var t = String(n); return dots ? t.replace(/\B(?=(\d{3})+(?!\d))/g, '.') : t; };
  if (!reduce && hasIO && window.requestAnimationFrame) $$('.ledger .val, .figs .val, .score-n, .stmt-figs .count').forEach(function (el) {
    var txt = el.textContent.trim();
    var m = /^(\D*)(\d{1,3}(?:\.\d{3})+|\d{1,5})(\D*)$/.exec(txt);
    if (!m || (m[2].length > 1 && m[2].charAt(0) === '0')) return;
    var dots = m[2].indexOf('.') > -1;
    var n = parseInt(m[2].replace(/\./g, ''), 10);
    if (n < 8) return;
    var io = new IntersectionObserver(function (es) {
      if (!es[0].isIntersecting) return;
      io.disconnect();
      el.style.display = 'inline-block';
      el.style.minWidth = el.getBoundingClientRect().width + 'px'; // sin saltos de maquetación
      el.setAttribute('aria-hidden', 'true');
      var t0 = null, dur = n > 999 ? 1800 : 1400;
      (function step(t) {
        if (t0 === null) t0 = t;
        var p = Math.min((t - t0) / dur, 1), e = 1 - Math.pow(1 - p, 4); // easeOutQuart
        el.textContent = m[1] + fmt(Math.round(n * e), dots) + m[3];
        if (p < 1) requestAnimationFrame(step);
        else { el.textContent = txt; el.removeAttribute('aria-hidden'); }
      })(performance.now());
    }, { threshold: 0.6 });
    io.observe(el);
  });

  /* ---------- 4. Artículos: barra de lectura + índice activo (sin scroll-jacking) ---------- */
  var article = $('.article');
  if (article) {
    var bar = d.createElement('div');
    bar.className = 'read-progress';
    bar.setAttribute('aria-hidden', 'true');
    d.body.appendChild(bar);

    var links = {};
    $$('.toc a[href^="#"]').forEach(function (a) {
      try { links[decodeURIComponent(a.hash.slice(1))] = a; } catch (e) {}
    });
    var heads = $$('h2[id]', article).filter(function (h) { return links[h.id]; });
    var aTop = 0, aLen = 1, marks = [], current = null, ticking = false;

    var measure = function () { // lecturas agrupadas: solo en carga/resize, nunca en scroll
      var y = window.pageYOffset;
      aTop = article.getBoundingClientRect().top + y;
      aLen = Math.max(1, article.offsetHeight - window.innerHeight * 0.5);
      marks = heads.map(function (h) { return h.getBoundingClientRect().top + y - 140; });
      paint();
    };
    var paint = function () {
      ticking = false;
      var y = window.pageYOffset, p = (y - aTop + window.innerHeight * 0.25) / aLen;
      bar.style.transform = 'scaleX(' + (p < 0 ? 0 : p > 1 ? 1 : p).toFixed(4) + ')';
      var i = marks.length - 1;
      while (i >= 0 && marks[i] > y) i--;
      var next = i >= 0 ? links[heads[i].id] : null;
      if (next !== current) {
        if (current) current.removeAttribute('aria-current');
        if (next) next.setAttribute('aria-current', 'true');
        current = next;
      }
    };
    window.addEventListener('scroll', function () {
      if (!ticking) { ticking = true; requestAnimationFrame(paint); }
    }, { passive: true });
    window.addEventListener('resize', measure);
    window.addEventListener('load', measure);
    if ('ResizeObserver' in window) new ResizeObserver(measure).observe(article);
    measure();
  }

  /* ---------- 5. GSAP (opcional): parallax del retrato + marquesina con inercia ---------- */
  var gsap = window.gsap, ST = window.ScrollTrigger;
  if (reduce || !gsap || !ST) return;
  gsap.registerPlugin(ST);
  var mm = gsap.matchMedia();

  mm.add({
    desktop: '(min-width: 1021px) and (prefers-reduced-motion: no-preference)',
    motion: '(prefers-reduced-motion: no-preference)'
  }, function (ctx) {
    var c = ctx.conditions;

    // 5a. Retrato del hero (sobre-mí): deriva lenta dentro del marco (solo escritorio).
    // Se anima <picture>, no <img>, para no pelear con la animación CSS de entrada.
    var pic = $('.hero .portrait picture') || $('.page-hero .portrait picture');
    var hero = pic && pic.closest('.hero, .page-hero');
    if (c.desktop && pic) {
      gsap.fromTo(pic, { yPercent: 0, scale: 1 }, {
        yPercent: 4, scale: 1.08, ease: 'none',
        scrollTrigger: { trigger: hero, start: 'top top', end: 'bottom top', scrub: 0.6 }
      });
      var col = $('.hero-grid > div:first-child');
      if (col) gsap.to(col, {
        y: -40, ease: 'none',
        scrollTrigger: { trigger: hero, start: 'top top', end: 'bottom top', scrub: 0.6 }
      });
    }

    // 5c. Hero de portada: tres planos (foto, texto, video) a distinta velocidad.
    var hx = $('.hx');
    if (c.desktop && hx) {
      var st = function () { return { trigger: hx, start: 'top top', end: 'bottom top', scrub: 0.5 }; };
      gsap.to('.hx-frame picture', { yPercent: 10, scale: 1.06, ease: 'none', scrollTrigger: st() });
      gsap.to('.hx-copy', { y: -70, ease: 'none', scrollTrigger: st() });
    }

    // 5d. Servicios: la caja "Es para ti si" sube un poco más rápido y la foto del
    // escritorio se acerca mientras se lee el texto de al lado.
    var fit = $('.svc-hero .fit');
    if (c.desktop && fit) gsap.to(fit, {
      y: -60, ease: 'none',
      scrollTrigger: { trigger: '.svc-hero', start: 'top top', end: 'bottom top', scrub: 0.5 }
    });
    var ip = $('.intro-frame img');
    if (c.desktop && ip) gsap.fromTo(ip, { scale: 1.14 }, {
      scale: 1, ease: 'none',
      scrollTrigger: { trigger: '.intro-grid', start: 'top bottom', end: 'bottom 60%', scrub: 0.6 }
    });

    // 5e. Cifras enormes de los casos: entran con un leve desplazamiento lateral ligado al scroll.
    if (c.desktop) $$('.score-v').forEach(function (el, i) {
      gsap.fromTo(el, { xPercent: i % 2 ? 4 : 8 }, {
        xPercent: 0, ease: 'none',
        scrollTrigger: { trigger: el, start: 'top bottom', end: 'top 55%', scrub: 0.6 }
      });
    });

    // 5b. Marquesina: acelera con la velocidad del scroll y vuelve suave a su ritmo.
    var anim = row && row.getAnimations ? row.getAnimations()[0] : null;
    if (c.motion && anim) {
      var proxy = { r: 1 };
      var apply = function () { anim.playbackRate = proxy.r; };
      ST.create({
        trigger: track, start: 'top bottom', end: 'bottom top',
        onUpdate: function (self) {
          var r = 1 + Math.min(Math.abs(self.getVelocity()) / 400, 3);
          if (r > proxy.r + 0.15) {
            gsap.killTweensOf(proxy);
            gsap.to(proxy, { r: r, duration: 0.25, ease: 'power2.out', onUpdate: apply })
              .then(function () {
                return gsap.to(proxy, { r: 1, duration: 1.4, ease: 'power3.out', onUpdate: apply });
              });
          }
        }
      });
      return function () { gsap.killTweensOf(proxy); anim.playbackRate = 1; };
    }
  });

  // Fuentes web y la imagen cambian alturas: recalcular una vez al terminar de cargar.
  window.addEventListener('load', function () { ST.refresh(); });
  if (d.fonts && d.fonts.ready) d.fonts.ready.then(function () { ST.refresh(); });
})();
