(function () {
  var WA = '573013291994';
  document.documentElement.classList.add('js');

  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  // Barra de navegación
  var nav = document.querySelector('.nav');
  var onScroll = function () { nav.classList.toggle('scrolled', window.scrollY > 20); };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  var menu = document.querySelector('.menu');
  var burger = document.querySelector('.burger');
  burger.addEventListener('click', function () {
    var open = menu.classList.toggle('open');
    burger.setAttribute('aria-expanded', open);
  });

  // Aparición al hacer scroll (una sola vez)
  var items = document.querySelectorAll('.rv, .portrait');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target;
        // filas escalonadas dentro de listas
        el.querySelectorAll(':scope > .row, :scope > li').forEach(function (c, i) { c.style.transitionDelay = (i * 0.07) + 's'; });
        el.classList.add('in');
        io.unobserve(el);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // Clics a WhatsApp e Instagram como eventos de Analytics
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a || !window.gtag) return;
    if (a.href.indexOf('wa.me') > -1) { gtag('event', 'click_whatsapp', { page: location.pathname }); gtag('event', 'generate_lead', { method: 'whatsapp', page: location.pathname }); }
    else if (a.href.indexOf('instagram.com') > -1) gtag('event', 'click_instagram', { page: location.pathname });
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
    if (window.gtag) gtag('event', 'generate_lead', { form_name: 'contacto', servicio: f.get('servicio') });
    window.open('https://wa.me/' + WA + '?text=' + encodeURIComponent(msg.trim()), '_blank', 'noopener');
  });
})();
