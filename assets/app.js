(() => {
  const t = window.md3t || ((s) => s);
  // mobile menu
  const burger = document.getElementById('burger');
  const closeMenu = () => {
    document.body.classList.remove('menu-open');
    burger.setAttribute('aria-expanded', 'false');
    burger.setAttribute('aria-label', t('Open menu'));
  };
  burger.addEventListener('click', () => {
    const open = document.body.classList.toggle('menu-open');
    burger.setAttribute('aria-expanded', String(open));
    burger.setAttribute('aria-label', t(open ? 'Close menu' : 'Open menu'));
  });
  document.querySelectorAll('#mobile a').forEach(a => a.addEventListener('click', closeMenu));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeMenu(); });

  // search tabs (home only)
  const tabs = document.querySelector('.search .tabs');
  if (tabs) {
    tabs.addEventListener('click', (e) => {
      const b = e.target.closest('button'); if (!b) return;
      tabs.querySelectorAll('button').forEach(x => x.setAttribute('aria-pressed', String(x === b)));
    });
    tabs.closest('form').addEventListener('submit', (e) => {
      e.preventDefault();
      const mode = tabs.querySelector('[aria-pressed="true"]').textContent.trim().toLowerCase();
      if (mode === 'buy') { location.href = 'how-to-buy.html'; return; }
      if (mode === 'sell') { location.href = 'how-to-sell.html'; return; }
      const q = e.target.querySelector('input[type="text"]').value.trim();
      location.href = 'rentals.html' + (q ? '?q=' + encodeURIComponent(q) : '');
    });
  }

  // nav background on scroll (home hero only; inner pages have a solid nav)
  const nav = document.getElementById('nav');
  if (!document.body.classList.contains('inner')) {
    const onScroll = () => nav.classList.toggle('solid', window.scrollY > window.innerHeight * 0.75);
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // reveal on scroll
  const io = new IntersectionObserver((entries) => {
    entries.forEach(en => {
      if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
    });
  }, { threshold: 0.05, rootMargin: '0px 0px -6% 0px' });
  document.querySelectorAll('.rv').forEach(el => io.observe(el));
})();
