(function () {
  var WA = '573013291994';
  document.documentElement.classList.add('js');

  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  // Barra de navegación
  var nav = document.querySelector('.nav');
  var onScroll = function () { if (nav) nav.classList.toggle('scrolled', window.scrollY > 20); };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  var menu = document.querySelector('.menu');
  var burger = document.querySelector('.burger');
  if (menu && burger) {
  burger.addEventListener('click', function () {
    var open = menu.classList.toggle('open');
    burger.setAttribute('aria-expanded', open);
  });
  var closeMenu = function () { menu.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); };
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && menu.classList.contains('open')) { closeMenu(); burger.focus(); } });
  menu.addEventListener('click', function (e) { if (e.target.closest('a')) closeMenu(); });
  }

  // Índice del artículo: cerrado por defecto en móvil
  var tocM = document.querySelector('.toc-m');
  if (tocM && window.matchMedia('(max-width:1020px)').matches) tocM.removeAttribute('open');

  // Aparición al hacer scroll (una sola vez)
  var items = document.querySelectorAll('.rv, .portrait');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target;
        // filas escalonadas dentro de listas
        el.querySelectorAll(':scope > .row, :scope > li, :scope > .bigrow, :scope > div, :scope > .gcards > .gcard, :scope > .team > li').forEach(function (c, i) { c.style.transitionDelay = Math.min(i * 0.08, 0.64) + 's'; });
        el.classList.add('in');
        io.unobserve(el);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    items.forEach(function (el) { io.observe(el); });
    if (performance.now() < 2400) document.documentElement.classList.add('motion-ready');
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // Clics a WhatsApp e Instagram como eventos de Analytics
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var dl = window.dataLayer = window.dataLayer || [];
    if (a.href.indexOf('wa.me') > -1) {
      var loc = a.classList.contains('wa-float') ? 'flotante' : a.classList.contains('nav-cta') ? 'menu' :
        a.closest('.hero, .page-hero, .hx, .svc-hero') ? 'hero' : a.closest('.mid-cta') ? 'blog-medio' : a.closest('.art-cta') ? 'blog-final' :
        a.closest('.closing') ? 'cierre' : a.closest('footer') ? 'pie' : 'contenido';
      dl.push({ event: 'click_whatsapp', page: location.pathname, cta_location: loc });
      dl.push({ event: 'generate_lead', method: 'whatsapp', page: location.pathname, cta_location: loc });
    }
    else if (a.href.indexOf('instagram.com') > -1) dl.push({ event: 'click_instagram', page: location.pathname });
  });

  // Formulario -> WhatsApp
  var form = document.getElementById('leadForm');
  if (form) form.addEventListener('submit', function (e) {
    e.preventDefault();
    var f = new FormData(form);
    var msg = 'Hola Sebastián, soy ' + f.get('nombre') +
      (f.get('empresa') ? ' de ' + f.get('empresa') : '') +
      (f.get('pais') ? ' (' + f.get('pais') + ')' : '') +
      '. Me interesa: ' + f.get('servicio') + '. ' + (f.get('mensaje') || '');
    (window.dataLayer = window.dataLayer || []).push({ event: 'generate_lead', method: 'formulario_whatsapp', form_name: form.dataset.name || 'contacto', page: location.pathname, servicio: f.get('servicio') });
    window.open('https://wa.me/' + WA + '?text=' + encodeURIComponent(msg.trim()), '_blank', 'noopener');
  });
})();
