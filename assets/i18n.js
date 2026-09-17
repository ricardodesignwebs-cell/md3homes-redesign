(() => {
  const ES = window.MD3_ES || {};
  const KEY = 'md3-lang';
  const ATTRS = ['placeholder', 'alt', 'aria-label', 'title'];
  const norm = (s) => s.replace(/\s+/g, ' ').trim();

  const word = (s) => ES[s] ?? s;
  // Textos compuestos (numeros, fechas, precios) que no conviene listar uno por uno.
  const RULES = [
    [/^(\d+) — (Buy|Sell|Rent)$/, (m) => `${m[1]} — ${word(m[2])}`],
    [/^More in (Buy|Sell|Rent)$/, (m) => `Más en ${word(m[1]).toLowerCase()}`],
    [/^View photo (\d+)$/, (m) => `Ver foto ${m[1]}`],
    [/^View all (\d+) photos$/, (m) => `Ver las ${m[1]} fotos`],
    [/^(\d+) photos$/, (m) => `${m[1]} fotos`],
    [/^1 rental available$/, () => '1 propiedad disponible'],
    [/^(\d+) rentals available$/, (m) => `${m[1]} propiedades disponibles`],
    [/^(.+) for rent · (.+)$/, (m) => `${word(m[1])} en alquiler · ${m[2]}`],
    [/^(\d+) Bed · ([\d.]+) Bath · Available (.+)$/,
      (m) => `${m[1]} hab. · ${m[2]} baños · Disponible desde el ${word(m[3])}`],
    [/^(Townhome|Duplex unit) · (.+)$/, (m) => `${word(m[1])} · ${m[2]}`],
    [/^\$([\d,]+)\/mo$/, (m) => `$${m[1]}/mes`],
    [/^([\d,]+) sq ft$/, (m) => `${m[1]} pies²`],
  ];

  const tr = (raw) => {
    const k = norm(raw);
    if (!k) return null;
    if (k in ES) return ES[k];
    for (const [re, fn] of RULES) {
      const m = k.match(re);
      if (m) return fn(m);
    }
    if (k.endsWith('…')) {
      const base = k.slice(0, -1);
      const full = Object.keys(ES).find((x) => x.startsWith(base));
      if (full) {
        const t = ES[full];
        return t.length > 125 ? t.slice(0, t.lastIndexOf(' ', 125)) + '…' : t;
      }
    }
    return null;
  };

  const texts = [];
  const attrs = [];
  const skip = (el) => el.closest('script, style, [data-no-i18n]');

  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  for (let n = walker.nextNode(); n; n = walker.nextNode()) {
    if (!n.nodeValue.trim() || skip(n.parentElement)) continue;
    texts.push([n, n.nodeValue]);
  }
  document.querySelectorAll(ATTRS.map((a) => `[${a}]`).join(',')).forEach((el) => {
    if (skip(el)) return;
    ATTRS.forEach((a) => { if (el.hasAttribute(a)) attrs.push([el, a, el.getAttribute(a)]); });
  });
  const title = document.title;

  let lang = 'en';
  window.md3t = (s) => (lang === 'es' ? tr(s) ?? s : s);
  window.md3lang = () => lang;

  const apply = (next) => {
    lang = next === 'es' ? 'es' : 'en';
    const es = lang === 'es';
    for (const [node, orig] of texts) {
      const t = es ? tr(orig) : null;
      node.nodeValue = t == null ? orig : orig.match(/^\s*/)[0] + t + orig.match(/\s*$/)[0];
    }
    for (const [el, a, orig] of attrs) {
      const t = es ? tr(orig) : null;
      el.setAttribute(a, t == null ? orig : t);
    }
    document.title = es ? title.split(' — ').map((p) => tr(p) ?? p).join(' — ') : title;
    document.documentElement.lang = lang;
    document.querySelectorAll('[data-lang-toggle]').forEach((b) => {
      const short = b.dataset.langToggle === 'short';
      b.textContent = es ? (short ? 'EN' : 'English') : (short ? 'ES' : 'Español');
      b.setAttribute('aria-label', es ? 'View in English' : 'Ver en español');
      b.lang = es ? 'en' : 'es';
    });
    try { localStorage.setItem(KEY, lang); } catch (e) { /* storage unavailable */ }
    document.documentElement.classList.remove('i18n-pending');
    document.dispatchEvent(new CustomEvent('md3:lang', { detail: lang }));
  };

  document.querySelectorAll('[data-lang-toggle]').forEach((b) =>
    b.addEventListener('click', () => apply(lang === 'es' ? 'en' : 'es')));

  let initial = 'en';
  try {
    initial = new URLSearchParams(location.search).get('lang')
      || localStorage.getItem(KEY)
      || ((navigator.languages || [navigator.language]).some((l) => /^es/i.test(l)) ? 'es' : 'en');
  } catch (e) { /* storage unavailable */ }
  apply(initial);
})();
