(() => {
  const form = document.getElementById('filters');
  if (form) {
    const cards = [...document.querySelectorAll('#lgrid .lcard')];
    const count = document.getElementById('rcount');
    const empty = document.getElementById('rempty');
    const apply = () => {
      const f = new FormData(form);
      const q = (f.get('q') || '').trim().toLowerCase();
      let n = 0;
      cards.forEach(c => {
        const d = c.dataset;
        const ok = (!q || d.q.includes(q))
          && (!f.get('type') || d.type === f.get('type'))
          && (!f.get('max') || +d.rent <= +f.get('max'))
          && (!f.get('beds') || +d.beds >= +f.get('beds'))
          && (!f.get('baths') || +d.baths >= +f.get('baths'));
        c.hidden = !ok;
        if (ok) n++;
      });
      count.textContent = n === 1 ? '1 rental available' : `${n} rentals available`;
      empty.hidden = n !== 0;
    };
    form.addEventListener('input', apply);
    form.addEventListener('reset', () => setTimeout(apply));
    const q0 = new URLSearchParams(location.search).get('q');
    if (q0) { form.q.value = q0; apply(); }
  }

  const photos = window.LISTING_PHOTOS;
  const box = document.getElementById('lightbox');
  if (!photos || !box) return;
  const img = document.getElementById('lbimg');
  const cap = document.getElementById('lbcap');
  let i = 0, opener = null;
  const show = (n) => {
    i = (n + photos.length) % photos.length;
    img.src = photos[i];
    cap.textContent = `${i + 1} / ${photos.length}`;
  };
  const open = (n, el) => {
    opener = el; show(n); box.hidden = false;
    document.body.style.overflow = 'hidden';
    box.querySelector('.close').focus();
  };
  const close = () => {
    box.hidden = true; document.body.style.overflow = '';
    if (opener) opener.focus();
  };
  document.querySelectorAll('.gallery [data-i], .gthumbs [data-i]').forEach(b =>
    b.addEventListener('click', () => open(+b.dataset.i, b)));
  box.querySelector('.close').addEventListener('click', close);
  box.querySelector('.prev').addEventListener('click', () => show(i - 1));
  box.querySelector('.next').addEventListener('click', () => show(i + 1));
  box.addEventListener('click', (e) => { if (e.target === box) close(); });
  let x0 = null;
  box.addEventListener('touchstart', (e) => { x0 = e.touches[0].clientX; }, { passive: true });
  box.addEventListener('touchend', (e) => {
    if (x0 === null) return;
    const dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 40) show(dx < 0 ? i + 1 : i - 1);
    x0 = null;
  });
  document.addEventListener('keydown', (e) => {
    if (box.hidden) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft') show(i - 1);
    if (e.key === 'ArrowRight') show(i + 1);
  });
})();
