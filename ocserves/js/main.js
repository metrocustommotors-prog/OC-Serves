/* OC Serves — site interactions */

document.addEventListener('DOMContentLoaded', function () {

  /* ---- Mobile navigation ---- */
  var toggle = document.querySelector('.nav-toggle');
  var links  = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      links.classList.toggle('open');
      toggle.textContent = links.classList.contains('open') ? '✕' : '☰';
    });
    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        links.classList.remove('open');
        toggle.textContent = '☰';
      });
    });
  }

  /* ---- Scroll reveal ---- */
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  document.querySelectorAll('.in-view').forEach(function (el) {
    io.observe(el);
  });

  /* ---- Intake form ---- */
  var form = document.getElementById('intake-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var success = document.getElementById('form-success');

      /* Build a mailto fallback so the request reaches docs@ocserves.com
         even without a backend. When hosted, this can be swapped for a
         real form endpoint (Formspree, Netlify Forms, etc.). */
      var data = new FormData(form);
      var lines = [];
      data.forEach(function (val, key) {
        if (val) lines.push(key.replace(/_/g, ' ').toUpperCase() + ': ' + val);
      });
      var body = encodeURIComponent(
        'New service request via ocserves.com\n\n' + lines.join('\n')
      );
      var subject = encodeURIComponent(
        'Service Request — ' + (data.get('firm') || 'New Client')
      );

      if (success) {
        success.style.display = 'block';
        success.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
      window.location.href =
        'mailto:docs@ocserves.com?subject=' + subject + '&body=' + body;
      form.reset();
    });
  }

  /* ---- Current year in footer ---- */
  document.querySelectorAll('.js-year').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
});
