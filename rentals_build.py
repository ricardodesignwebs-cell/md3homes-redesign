"""Datos y plantillas de la seccion de rentas (portal Buildium de MD3)."""
import html

BLD = "https://md3homes.managebuilding.com/Resident"
APPLY = BLD + "/rental-application/new"
RES_LOGIN = BLD + "/portal/login"
MGR_LOGIN = "https://md3homes.managebuilding.com/manager/"
REGISTER = BLD + "/PublicPages/FirstTime.aspx"
DOCS = BLD + "/PublicPages/DocumentsSearch.aspx"
BLD_FILE = BLD + "/api/public/files/download?fileName="

BAVEL_PHOTOS = """80c26ba61b884d898a098b6c2d4967cd 7fe66322c95f407198879ba05a2ffcdc
1e2f805b5af4492f8c5e3b41bf727372 51f59dc9cde64568bec0ff5cc325873e b904891ce95e4f94a805b57b1dd56eb6
4a722c5e76964b5bacb2e2b1f6dd0323 b6e924140b7d424dbf4ce29cce803e11 7f53537b7a4a4d4a9c7c9f5ebae30abd
76b8288a97b84445a140c8c1cab37126 35fcceefe6b44314979bd682e3f44a38 31a370eea3264c959e2b375eecdd72e0
f3e60e34625b4ac39c7c445a3f658669 338a939081c747adb79f4a56c7e162e2 8728441c6ff646d7952a1bc66fcccd3c
00e48b15c5e741eabeb942ecfe664145 58777379b6494660905f51bbc4004fb0 a9894a07f60f4045a4a05a4856d78a9e
225ce41802af49efadb0e78049c1df40 45922247ac2e476389ed2c96f96b2c34 e79444c5e3164d8e979c8a92d97d5b14
bf2a46da32604315b70cc00566513791 245f9355493849a4b9d7ae93630ab4bf cde1b566833b45889e883ab38c422629
d61a4459ae42476f9a30fba34af38776 c5ee25a0a09342d489729c97d6289a3d f336646f547a4f84942b97525fc05b2d
7ed45f9f879a492f953ab897eeffc131 8340bc19403b4855ba716fbe1dc1cebc b5c847c4275c489cbc086163dd3a78af
73e92dfaeb3947c5a8188aa76d9f0c68 a9cc8f946b454682ba0de771f8d60bc2 932eb16447da47209c62764e933d3f66
4a645bd8ef4b4c928d5f98af1d938909 ae7e87acd25c47329f54fce39bf0dded d291659ce458499f8f67cc585e818df3
4b5d6f51d89f47918d1b54ff5769d4ae 87fced48882e4eab9e8813157ae76d4d 562978f1a41b428f8d773d444282b52d
ab3ace6cf08543b581da85da55f4a2c6 ca544dacc1ef47d98e4a6fe0ed76770f"""

KILIMANJARO_PHOTOS = """d70fb23a9c404121af2f74b8fdf2357c.png e75581a4de4a433e9223a65e3fd7bba1.jpeg
702e9cc9a8e74426920dc09c0ec0c86d.jpeg 812c095f2ba74832963a00d1a8764634.jpg
4cbb260948b94bb79abb2f48b807c69f.jpg 2186bcb0c2354661ac43c6a9fc8bf0ac.jpeg
b878e5a104864299ac819d79497c79e6.jpg ea70469465d54bed8585978c0c4dbb32.jpeg
2b0dd67b40764c6fada88d444c677e07.jpg 3fa831c5f94f4efa88bd9f6ea729043e.jpg
ab9b56f4f11d4a3ca7158b440cc5bb1a.jpeg 17c0aa0297ed497ea57dadef5346e6d4.jpeg"""

LISTINGS = [
    dict(slug="rental-2416-bavel-ln",
         address="2416 Bavel Ln - 1", city="Davenport", state="FL", zip="33896",
         kind="Townhome", type_key="condo", rent=1890, beds=3, baths=2.5,
         size=1378, available="Aug 1, 2026", year=None, deposit="$1,890.00",
         detail=BLD + "/PublicPages/apartmentdetail.aspx?listingId=89537&amp;unitid=486811&amp;buildingid=185863",
         description=[
             "Welcome to this beautiful brand-new townhome located between Posner "
             "Park and Posner Reserve, offering the perfect combination of comfort, "
             "style, and convenience. Prime location with easy access to US-27 and "
             "I-4. Community pool, playground, and dog park.",
             "Minutes from Northeast Regional Park. Close to Publix, Walmart, "
             "restaurants, and shopping. Approximately 25–30 minutes to Disney and "
             "35–40 minutes to Downtown Orlando.",
             "The blinds will be installed by August 7. The garage will be painted, "
             "and the garage door opener will also be installed."],
         highlights=["Brand-new townhome", "Community pool", "Playground",
                     "Dog park", "Easy access to US-27 and I-4",
                     "25–30 minutes to Disney"],
         photos=[f + ".jpg" for f in BAVEL_PHOTOS.split()]),
    dict(slug="rental-542-kilimanjaro-dr",
         address="542 Kilimanjaro Dr Unit B", city="Poinciana", state="FL", zip="",
         kind="Duplex unit", type_key="multi", rent=1600, beds=3, baths=2,
         size=1215, available="Dec 11, 2025", year=2023, deposit="$1,600.00",
         detail=BLD + "/PublicPages/apartmentdetail.aspx?listingId=72809&amp;unitid=430176&amp;buildingid=168239",
         description=[
             "Beautiful unit in a duplex building, Unit B, ready to rent, with 3 "
             "bedrooms and 2 full baths — with stainless steel appliances, blinds, "
             "granite counter tops, and laminate wood floor. You must see it."],
         highlights=["Ready to rent", "Stainless steel appliances",
                     "Granite counter tops", "Laminate wood floor", "Blinds",
                     "Built in 2023"],
         photos=KILIMANJARO_PHOTOS.split()),
]

DOCUMENTS = [
    ("Tenant Requirements", "1-TENANT REQUIERMENTS.pdf", "144 KB"),
    ("Notice to Prospect Tenant", "2-NOTICE TO PROSPECT TENANT.pdf", "131 KB"),
    ("Verification of Rent", "3-VERIFICATION OF RENT.pdf", "187 KB"),
    ("Referral", "4-REFFERAL.pdf", "152 KB"),
]


def fmt_baths(b):
    return f"{b:g}"


def photo(name):
    return BLD_FILE + name


def location(l):
    return f"{l['city']}, {l['state']}" + (f" {l['zip']}" if l["zip"] else "")


def arrow():
    return ('<svg width="16" height="10" viewBox="0 0 16 10" fill="none" '
            'stroke="currentColor" stroke-width="1.5"><path d="M1 5h13M10 1l4 4-4 4"/></svg>')


def listing_card(l):
    loc = location(l)
    return f"""<a class="lcard" href="{l['slug']}.html"
      data-type="{l['type_key']}" data-beds="{l['beds']}" data-baths="{l['baths']}"
      data-rent="{l['rent']}" data-q="{html.escape((l['address'] + ' ' + loc).lower())}">
      <div class="lph">
        <img src="{photo(l['photos'][0])}" alt="{html.escape(l['address'])}" loading="lazy">
        <span class="lprice">${l['rent']:,}<small>/mo</small></span>
        <span class="lcount">{len(l['photos'])} photos</span>
      </div>
      <div class="lbody">
        <span class="lkind">{html.escape(l['kind'])} &middot; {html.escape(l['city'])}</span>
        <h3>{html.escape(l['address'])}</h3>
        <p class="lloc">{html.escape(loc)}</p>
        <ul class="lspecs">
          <li><b>{l['beds']}</b> Beds</li>
          <li><b>{fmt_baths(l['baths'])}</b> Baths</li>
          <li><b>{l['size']:,}</b> sq ft</li>
        </ul>
      </div>
    </a>"""


def rentals_body():
    cards = "\n    ".join(listing_card(l) for l in LISTINGS)
    docs = "\n      ".join(
        f"""<a class="doc" href="{DOCS}" target="_blank" rel="noopener">
        <span class="dico" aria-hidden="true">PDF</span>
        <span class="dname">{html.escape(t)}<small>{html.escape(f)}</small></span>
        <span class="dsize">{s}</span>
      </a>""" for t, f, s in DOCUMENTS)
    return f"""<header class="phead rhead">
  <nav class="crumbs" aria-label="Breadcrumb">
    <a href="index.html">Home</a><span>/</span>
    <a href="index.html#rent">Rent</a><span>/</span>
    <span class="here">Available Rentals</span>
  </nav>
  <span class="idx">MD3 Exclusives</span>
  <h1>Available Rentals</h1>
</header>

<section class="rsearch" aria-label="Rental search">
  <form class="filters" id="filters" onsubmit="return false">
    <label class="f wide"><span>Zip or city</span><input type="search" name="q" placeholder="e.g. Davenport or 33896"></label>
    <label class="f"><span>Type</span>
      <select name="type">
        <option value="">All types</option>
        <option value="condo">Condo / Townhome</option>
        <option value="multi">Multi-Family</option>
        <option value="single">Single-Family</option>
      </select>
    </label>
    <label class="f"><span>Max rent</span>
      <select name="max">
        <option value="">Any</option>
        <option value="1000">$1,000</option><option value="1250">$1,250</option>
        <option value="1500">$1,500</option><option value="1750">$1,750</option>
        <option value="2000">$2,000</option>
      </select>
    </label>
    <label class="f"><span>Bedrooms</span>
      <select name="beds">
        <option value="">Any</option><option value="1">1+</option>
        <option value="2">2+</option><option value="3">3+</option><option value="4">4+</option>
      </select>
    </label>
    <label class="f"><span>Bathrooms</span>
      <select name="baths">
        <option value="">Any</option><option value="1">1+</option>
        <option value="2">2+</option><option value="2.5">2.5+</option><option value="3">3+</option>
      </select>
    </label>
    <button class="btn ghostreset" type="reset">Clear</button>
  </form>
  <p class="rcount" id="rcount" aria-live="polite">{len(LISTINGS)} rentals available</p>
</section>

<section class="rlist">
  <div class="lgrid" id="lgrid">
    {cards}
  </div>
  <div class="rempty" id="rempty" hidden>
    <h3>No rentals match your search</h3>
    <p>Try a different city or clear the filters.</p>
  </div>
</section>

<section class="access" id="access">
  <div class="ahead rv">
    <span class="lbl">Portal access</span>
    <h2>Residents, owners and applicants</h2>
  </div>
  <div class="acards">
    <div class="acard rv">
      <span class="anum">01</span>
      <h3>Resident Sign In</h3>
      <p>Tenants, board members, and association members.</p>
      <div class="aacts">
        <a class="btn" href="{RES_LOGIN}" target="_blank" rel="noopener">Sign in here</a>
        <a class="alink" href="{REGISTER}" target="_blank" rel="noopener">First time? Register online</a>
      </div>
    </div>
    <div class="acard rv">
      <span class="anum">02</span>
      <h3>Management Sign In</h3>
      <p>Property managers, rental owners, and vendors.</p>
      <div class="aacts">
        <a class="btn" href="{MGR_LOGIN}" target="_blank" rel="noopener">Sign in here</a>
      </div>
    </div>
    <div class="acard dark rv">
      <span class="anum">03</span>
      <h3>Rental Application</h3>
      <p>Interested in one of our properties?</p>
      <div class="aacts">
        <a class="btn light" href="{APPLY}" target="_blank" rel="noopener">Apply online</a>
        <a class="alink" href="who-is-eligible-to-rent.html">Who is eligible to rent?</a>
      </div>
    </div>
  </div>

  <div class="docs rv">
    <div class="dhead">
      <h3>Documents</h3>
    </div>
    <div class="dlist">
      {docs}
    </div>
  </div>
</section>"""


def listing_body(l):
    loc = location(l)
    ph = l["photos"]
    thumbs = "".join(
        f'<button type="button" class="gthumb" data-i="{i}" aria-label="View photo {i + 1}">'
        f'<img src="{photo(p)}" alt="" loading="lazy"></button>'
        for i, p in enumerate(ph))
    side = "".join(
        f'<button type="button" class="gcell" data-i="{i}" aria-label="View photo {i + 1}">'
        f'<img src="{photo(ph[i])}" alt=""></button>'
        for i in range(1, min(5, len(ph))))
    facts = [("Rent", f"${l['rent']:,}/mo"), ("Bedrooms", l["beds"]),
             ("Bathrooms", fmt_baths(l["baths"])), ("Size", f"{l['size']:,} sq ft"),
             ("Available", l["available"])]
    if l["year"]:
        facts.append(("Year built", l["year"]))
    facts.append(("Security deposit", l["deposit"]))
    facts_html = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in facts)
    desc = "".join(f"<p>{html.escape(t)}</p>" for t in l["description"])
    hl = "".join(f"<li>{html.escape(h)}</li>" for h in l["highlights"])
    others = "\n    ".join(listing_card(o) for o in LISTINGS if o is not l)
    data = ",".join(f'"{photo(p)}"' for p in ph)
    subject = html.escape("Inquiry: " + l["address"]).replace(" ", "%20")

    return f"""<header class="phead lhead">
  <nav class="crumbs" aria-label="Breadcrumb">
    <a href="index.html">Home</a><span>/</span>
    <a href="rentals.html">Rentals</a><span>/</span>
    <span class="here">{html.escape(l['address'])}</span>
  </nav>
  <div class="ltop">
    <div>
      <span class="idx">{html.escape(l['kind'])} for rent &middot; {html.escape(l['city'])}</span>
      <h1>{html.escape(l['address'])}</h1>
      <p class="lloc big">{html.escape(loc)}</p>
    </div>
    <div class="lprice-big">${l['rent']:,}<small>/month</small></div>
  </div>
</header>

<section class="gallery" aria-label="Photos">
  <button type="button" class="gmain" data-i="0" aria-label="Open photo gallery">
    <img src="{photo(ph[0])}" alt="{html.escape(l['address'])}">
  </button>
  <div class="gside">{side}</div>
  <button type="button" class="gall" data-i="0">View all {len(ph)} photos</button>
</section>

<section class="ldetail">
  <div class="lmain">
    <ul class="lspecs big">
      <li><b>{l['beds']}</b> Beds</li>
      <li><b>{fmt_baths(l['baths'])}</b> Baths</li>
      <li><b>{l['size']:,}</b> sq ft</li>
    </ul>

    <div class="lblock rv">
      <span class="lbl">Description</span>
      <div class="ldesc">{desc}</div>
    </div>

    <div class="lblock rv">
      <span class="lbl">Highlights</span>
      <ul class="hl">{hl}</ul>
    </div>

    <div class="lblock rv">
      <span class="lbl">Details &amp; lease terms</span>
      <dl class="facts">{facts_html}</dl>
    </div>

    <div class="lblock rv">
      <span class="lbl">All photos</span>
      <div class="gthumbs">{thumbs}</div>
    </div>
  </div>

  <aside class="lside">
    <div class="lbox">
      <div class="lbox-price">${l['rent']:,}<small>/month</small></div>
      <p class="lbox-sub">{l['beds']} Bed &middot; {fmt_baths(l['baths'])} Bath &middot; Available {l['available']}</p>
      <a class="btn full" href="{APPLY}" target="_blank" rel="noopener">Apply for this property</a>
      <a class="btn full ghost" href="mailto:info@md3homes.com?subject={subject}">Contact us about this property</a>
      <a class="lcall" href="tel:4075578810">or call <b>(407) 557-8810</b></a>
      <hr>
      <a class="alink" href="{l['detail']}" target="_blank" rel="noopener">View map on the resident portal</a>
    </div>
  </aside>
</section>

<section class="rlist more">
  <div class="shead"><span class="lbl">More rentals</span></div>
  <div class="lgrid">
    {others}
  </div>
</section>

<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Photo viewer" hidden>
  <button type="button" class="lbx close" aria-label="Close">&times;</button>
  <button type="button" class="lbx prev" aria-label="Previous photo">&lsaquo;</button>
  <figure><img id="lbimg" alt=""><figcaption id="lbcap"></figcaption></figure>
  <button type="button" class="lbx next" aria-label="Next photo">&rsaquo;</button>
</div>
<script>window.LISTING_PHOTOS = [{data}];</script>"""


def featured_home():
    cards = "\n    ".join(listing_card(l) for l in LISTINGS)
    return f"""<!-- featured-rentals -->
<section class="chapter featured">
  <div class="fhead rv">
    <div>
      <span class="idx">MD3 Exclusives</span>
      <h2>Featured Rentals</h2>
    </div>
    <a class="more" href="rentals.html">See all rentals {arrow()}</a>
  </div>
  <div class="lgrid rv">
    {cards}
  </div>
</section>
<!-- /featured-rentals -->"""


RENTALS_JS = r"""(() => {
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
"""
