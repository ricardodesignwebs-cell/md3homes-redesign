"""Genera la propuesta MD3 Homes: actualiza la home (index.html) y crea las
11 subpaginas y la seccion de rentas con el contenido real de md3homes.com.
"""
import html
import pathlib
import re

import rentals_build as rb

ROOT = pathlib.Path(__file__).parent
HOME = ROOT / "index.html"
ASSETS = ROOT / "assets"
IMG = "https://md3homes.com/images/site/"
PORTAL = ("https://md3homes.managebuilding.com/Resident/PublicPages/"
          "Home.aspx?ReturnUrl=%2fresident")
ES = "https://md3homes.com/index.php/es/?view=article&amp;id=19:comprar&amp;catid=11"

GROUPS = {
    "buy": ("Buy", "#buy"),
    "sell": ("Sell", "#sell"),
    "rent": ("Rent", "#rent"),
}

PAGES = [
    dict(slug="how-to-buy", group="buy", title="How to Buy",
         img="HowToBuy_157857926.jpg",
         alt="An agent showing a Florida home to buyers",
         lead="We specialize in helping people find their dream homes in Florida. "
              "Our extensive knowledge allows us to guide you through the entire "
              "process of purchasing houses, condos, villas, townhomes, commercial "
              "properties, and vacant land.",
         body=["Homebuilders are currently offering incentives, making it a great "
               "time to consider factors such as location, size, number of bedrooms, "
               "outdoor space, schools, commute, and accessibility.",
               "Before buying a home, it's essential to assess your finances to "
               "determine your eligibility and decide whether you need financing or "
               "will pay with cash. We can help you find your dream home and guide "
               "you through the entire process."]),
    dict(slug="investment-properties", group="buy", title="Investment Properties",
         img="InvestmentProperties_18291798.jpg",
         alt="Investment property in Florida",
         lead="Investment properties offer excellent opportunities for homeownership "
              "and real estate investments.",
         body=["Our dependable agents can guide you through the process, assist you "
               "with financing options, and provide top-notch property management "
               "services."]),
    dict(slug="full-service", group="buy", title="Full Service",
         img="FullService_45834733.jpg",
         alt="Full service real estate team at work",
         lead="We help you find properties for building, inventory development, or "
              "resale.",
         body=["We manage sale contracts, financing, and legal procedures. We also "
               "offer property management for rentals."]),
    dict(slug="international-buyers", group="buy", title="International Buyers",
         img="InternationalBuyers_275862450.jpg",
         alt="International buyers investing in Florida property",
         lead="MD3 Homes assists international buyers investing in Florida with "
              "tailored financing options.",
         body=["Florida is a popular destination for investors worldwide due to its "
               "stunning beaches, world-class golf courses, shopping centers, and "
               "popular theme parks.",
               "We handle the administration of financing options, property "
               "maintenance, and searches for the right property owner."]),
    dict(slug="foreclosure-and-short-sale", group="buy",
         title="Foreclosure and Short-Sale",
         img="Foreclosure_7302677.jpg",
         alt="Foreclosure and short sale property",
         lead="Foreclosure and short-sale homes can provide a great opportunity in "
              "the current real estate market, as they offer competitive rates.",
         body=["However, it's important to note that short sales are intended for "
               "serious buyers who are willing to invest time and effort in the "
               "process.",
               "This can be a lengthy procedure that demands patience, perseverance, "
               "and flexibility, and may take several months to complete, as it "
               "requires approval from the lender."]),

    dict(slug="how-to-sell", group="sell", title="How to Sell",
         img="HowToSell_196912259.jpg",
         alt="Homeowner preparing to sell a property",
         lead="To determine a property's price, it is important to consider the "
              "location, size, amenities, condition, and market value.",
         body=["MD3 HOMES agents provide expert evaluation and exclusive "
               "representation."]),
    dict(slug="determining-the-market-price", group="sell",
         title="Determining The Market Price",
         img="DeterminingThePrice_83838610.jpg",
         alt="Determining the market price of a home",
         lead="After determining the property's price, the Real Estate Agent will "
              "draft a contract that gives them the sole authority to represent the "
              "property owner and search for prospective buyers.",
         body=["The property will then be listed on the Multiple Listing Service "
               "(MLS), a platform exclusively available to Real Estate Agents."]),
    dict(slug="the-process", group="sell", title="The Process",
         img="TheProcess_169389551.jpg",
         alt="Buyer and agent reviewing the sale process",
         lead="Buyers who are interested in purchasing a property typically make an "
              "offer through a Real Estate Agent.",
         body=["This offer will be in writing and if both parties agree, they will "
               "schedule a day to inspect the property. During the inspection, they "
               "will review any improvements needed in the house and discuss the "
               "conditions of the sale.",
               "Finally, they will agree on a convenient closing date for both "
               "parties. To avoid misunderstandings, all negotiations will be made "
               "in writing."]),

    dict(slug="who-is-eligible-to-rent", group="rent",
         title="Who is Eligible to Rent?",
         img="WhoIsElegibleToRent_196127592.jpg",
         alt="Tenants applying to rent a home",
         lead="To rent a property through MD3 HOMES, you must be 18 years old and "
              "have a valid ID.",
         body=["You can start the application process by visiting our website, but "
               "please note that there is an application fee."]),
    dict(slug="rental-process", group="rent", title="Rental Process",
         img="RentalProcess_120842997.jpg",
         alt="Signing a lease agreement",
         lead="If your application is approved, you will be required to pay a "
              "non-refundable security deposit to reserve the property.",
         body=["This deposit is essential to secure the property for you. Once the "
               "deposit has been paid, our team will prepare a contract, and you can "
               "schedule an appointment to sign the lease agreement and receive the "
               "keys to your new home.",
               "We assist with applications and documentation, and we offer "
               "high-quality properties of various sizes. All properties are cleaned "
               "and maintained by our top-rated team."]),
    dict(slug="property-management", group="rent", title="Property Management",
         img="PropertyManagement_11561255.jpg",
         alt="Property management services in Florida",
         lead="Our Florida property management services help rental property owners "
              "with maintenance, tenant screening, rent collection, and property "
              "buying/selling.",
         body=["We also assist investors who live far away from their rental "
               "properties."],
         extra=dict(title="Services Include", img="ServicesInclude_195835741.jpg",
                    alt="Property management services included",
                    text="Managing a property involves tenant matching, verifying "
                         "rental history, credit and background checks, creating "
                         "lease agreements, and managing payments for tenants and "
                         "landlords.")),
]

BY_SLUG = {p["slug"]: p for p in PAGES}


def group_pages(group):
    return [p for p in PAGES if p["group"] == group]


def sub_items(key):
    items = [(f"{p['slug']}.html", p["title"]) for p in group_pages(key)]
    if key == "rent":
        items.insert(0, ("rentals.html", "Available Rentals"))
    return items


def caret():
    return ('<svg class="car" width="9" height="6" viewBox="0 0 9 6" fill="none" '
            'stroke="currentColor" stroke-width="1.4"><path d="M1 1.5 4.5 4.5 8 1.5"/>'
            '</svg>')


def nav(home, current=None):
    """home: prefijo hacia la home. current: slug activo."""
    out = [f'<nav class="nav" id="nav">',
           f'  <a class="brand" href="{home}"><img src="https://md3homes.com/images/site/all-white-md3-80pxh-FIXED.png" alt="MD3 Homes"></a>',
           '  <ul>']
    for key, (label, anchor) in GROUPS.items():
        subs = "".join(f'<li><a href="{h}">{html.escape(t)}</a></li>'
                       for h, t in sub_items(key))
        out.append(f'    <li><a href="{home}{anchor}">{label} {caret()}</a>'
                   f'<ul class="sub">{subs}</ul></li>')
    for label, anchor in [("Financing", "#financing"), ("About Us", "#about"),
                          ("Contact Us", "#contact")]:
        out.append(f'    <li><a href="{home}{anchor}">{label}</a></li>')
    out += ['  </ul>',
            '  <div class="right">',
            f'    <a class="lang" href="{ES}">ES</a>',
            '    <a class="btn outline" href="rentals.html">MD3 Exclusives</a>',
            '    <a class="btn" href="rentals.html#access">Sign In</a>',
            '    <button class="burger" type="button" id="burger" aria-label="Open menu" aria-expanded="false" aria-controls="mobile"><span></span></button>',
            '  </div>',
            '</nav>']
    return "\n".join(out)


def mobile(home):
    out = ['<div class="mobile" id="mobile">']
    for key, (label, anchor) in GROUPS.items():
        kids = "".join(f'<a href="{h}">{html.escape(t)}</a>'
                       for h, t in sub_items(key))
        out.append(f'  <div class="grp"><a href="{home}{anchor}">{label}</a>'
                   f'<div class="kids">{kids}</div></div>')
    for label, anchor in [("Financing", "#financing"), ("About Us", "#about"),
                          ("Contact Us", "#contact")]:
        out.append(f'  <div class="grp"><a href="{home}{anchor}">{label}</a></div>')
    out += ['  <div class="foot">',
            '    <a class="btn" href="rentals.html#access">Sign In</a>',
            '    <a class="btn outline" href="rentals.html" style="color: var(--ink); border-color: var(--line)">MD3 Exclusives</a>',
            f'    <a class="lbl" href="{ES}">Espa&ntilde;ol</a>',
            '  </div>', '</div>']
    return "\n".join(out)


def footer(home):
    menu = "".join(f'<a href="{home}{a}">{l}</a>' for l, a in
                   [("Buy", "#buy"), ("Sell", "#sell"), ("Rent", "#rent"),
                    ("Financing", "#financing"), ("About Us", "#about"),
                    ("Contact Us", "#contact")])
    return f"""<footer>
  <div class="cols">
    <div>
      <img class="logo" src="https://md3homes.com/images/site/all-white-md3-80pxh-FIXED.png" alt="MD3 Homes">
      <p>Equal Housing Opportunity. Real estate services for local and international clients in Central Florida.</p>
      <div class="socials">
        <a href="https://www.facebook.com/md3homes" target="_blank" rel="noopener" aria-label="Facebook"><img src="https://md3homes.com/images/social/logo-fb-gray_48px.png" alt=""></a>
        <a href="https://www.instagram.com/md3homes/" target="_blank" rel="noopener" aria-label="Instagram"><img src="https://md3homes.com/images/social/logo-Instagram_48px.png" alt=""></a>
        <a href="https://www.twitter.com/md3homes" target="_blank" rel="noopener" aria-label="X"><img src="https://md3homes.com/images/social/logo-x_2023_white_48px.png" alt=""></a>
        <a href="https://www.linkedin.com/in/md3homes/" target="_blank" rel="noopener" aria-label="LinkedIn"><img src="https://md3homes.com/images/social/logo-lin-gray_48px.png" alt=""></a>
      </div>
    </div>
    <div><span class="ttl">Menu</span><div class="links">{menu}</div></div>
    <div>
      <span class="ttl">Main office</span>
      <div class="links">
        <p>6965 Piazza Grande Ave. Suite 413<br>Orlando, FL 32835</p>
        <a href="mailto:info@md3homes.com">info@md3homes.com</a>
        <a href="tel:4075578810">407-557-8810</a>
        <p>Fax: 407-809-4777</p>
      </div>
    </div>
  </div>
  <p class="legal">This material is based on information we consider reliable, but because it has been supplied by third parties, we cannot represent its accuracy or completion and should not be relied on as such. This offering is subject to errors, omissions, change of price or withdrawal without notice.</p>
</footer>"""


def page_html(p):
    group_label, anchor = GROUPS[p["group"]]
    siblings = [s for s in group_pages(p["group"]) if s["slug"] != p["slug"]]
    idx = group_pages(p["group"]).index(p) + 1

    body = "\n      ".join(f"<p>{html.escape(t)}</p>" for t in p["body"])

    extra = ""
    if p.get("extra"):
        e = p["extra"]
        extra = f"""
<section class="chapter flip">
  <div class="grid">
    <figure class="media rv" style="margin-top:0;margin-bottom:0">
      <img src="{IMG}{e['img']}" alt="{html.escape(e['alt'])}">
    </figure>
    <div class="txt rv">
      <h2>{html.escape(e['title'])}</h2>
      <p class="lead">{html.escape(e['text'])}</p>
    </div>
  </div>
</section>"""

    sib_cards = "\n    ".join(
        f"""<a class="scard" href="{s['slug']}.html">
      <div class="ph"><img src="{IMG}{s['img']}" alt="{html.escape(s['alt'])}"></div>
      <h3>{html.escape(s['title'])}</h3>
      <p>{html.escape(s['lead'][:120])}{'&hellip;' if len(s['lead']) > 120 else ''}</p>
    </a>""" for s in siblings)

    of = "of3" if len(siblings) <= 3 else "of5"

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(p['title'])} &mdash; MD3 Homes</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,700&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css">
<link rel="stylesheet" href="assets/pages.css">
</head>
<body class="inner">

{nav('index.html', p['slug'])}

{mobile('index.html')}

<header class="phead">
  <nav class="crumbs" aria-label="Breadcrumb">
    <a href="index.html">Home</a>
    <span>/</span>
    <a href="index.html{anchor}">{group_label}</a>
    <span>/</span>
    <span class="here">{html.escape(p['title'])}</span>
  </nav>
  <span class="idx">{idx:02d} &mdash; {group_label}</span>
  <h1>{html.escape(p['title'])}</h1>
</header>

<figure class="pshot rv">
  <img src="{IMG}{p['img']}" alt="{html.escape(p['alt'])}">
</figure>

<section class="pbody">
  <div class="grid">
    <p class="plead rv">{html.escape(p['lead'])}</p>
    <div class="ptext rv">
      {body}
    </div>
  </div>
</section>
{extra}

<section class="chapter siblings">
  <div class="shead rv">
    <span class="lbl">More in {group_label}</span>
  </div>
  <div class="subgrid {of} rv">
    {sib_cards}
  </div>
</section>

<section class="contact">
  <div class="grid">
    <div class="left rv">
      <span class="lbl">Contact Us</span>
      <h2 style="margin-top:18px">How do we get in touch</h2>
      <p class="lead">It is in our best interest we keep in contact in the event you may need any further assistance. Please don't hesitate to reach out to us.</p>
      <p style="margin-top:34px"><a class="btn" href="mailto:info@md3homes.com">Send an Email</a></p>
    </div>
    <div class="right rv">
      <div class="item"><span>Main office</span><p>6965 Piazza Grande Ave. Suite 413<br>Orlando, FL 32835</p></div>
      <div class="item"><span>Sales &amp; information</span><a href="tel:4075578810">407-557-8810</a></div>
      <div class="item"><span>Email</span><a href="mailto:info@md3homes.com">info@md3homes.com</a></div>
      <div class="item"><span>Fax</span><p>407-809-4777</p></div>
    </div>
  </div>
</section>

{footer('index.html')}

<script src="assets/app.js"></script>
</body>
</html>
"""


EXTRA_CSS = """
/* ---------- paginas internas ---------- */
body.inner .nav { position: sticky; background: var(--surface); border-bottom-color: var(--line); }
body.inner .nav .brand img { filter: brightness(0) saturate(100%); opacity: .92; }
body.inner .nav > ul > li > a, body.inner .nav .lang { color: var(--ink); }
body.inner .nav .btn.outline { color: var(--accent); border-color: var(--accent); }
body.inner .nav .btn.outline:hover { background: var(--accent); color: #fff; }
body.inner .burger { color: var(--ink); }

.phead { padding: clamp(50px, 7vw, 90px) var(--pad) clamp(34px, 4vw, 52px); }
.crumbs { display: flex; align-items: center; gap: 10px; font-family: var(--mono); font-size: 11px; letter-spacing: .1em; text-transform: uppercase; color: var(--muted); margin-bottom: clamp(28px, 4vw, 46px); flex-wrap: wrap; }
.crumbs a:hover { color: var(--accent); }
.crumbs .here { color: var(--ink); }
.phead .idx { font-family: var(--mono); font-size: 12px; letter-spacing: .2em; color: var(--accent); display: block; margin-bottom: 18px; }
.phead h1 { font-size: clamp(40px, 6.4vw, 96px); max-width: 15ch; }

.pshot { margin: 0; }
.pshot img { width: 100%; height: clamp(280px, 42vw, 560px); object-fit: cover; }

.pbody { padding: clamp(56px, 7vw, 100px) var(--pad); }
.pbody .grid { display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: clamp(28px, 4vw, 60px); }
.plead { grid-column: span 6; font-family: var(--display); font-size: clamp(23px, 2.7vw, 38px); line-height: 1.22; }
.ptext { grid-column: 8 / span 5; display: flex; flex-direction: column; gap: 18px; }
.ptext p { font-size: clamp(15px, 1.2vw, 17px); line-height: 1.75; color: var(--muted); }

.siblings { padding-bottom: clamp(80px, 11vw, 140px); }
.siblings .shead { border-top: 1px solid var(--line); padding-top: 26px; }
.siblings .subgrid { margin-top: clamp(28px, 3vw, 44px); }

@media (max-width: 900px) {
  .pbody .grid { grid-template-columns: minmax(0, 1fr); gap: 26px; }
  .plead, .ptext { grid-column: 1 / -1; }
  .crumbs, .phead .idx { font-size: 11px; }
}
"""


def page_shell(title, body, scripts=("assets/app.js",)):
    tags = "\n".join(f'<script src="{s}"></script>' for s in scripts)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,700&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css">
<link rel="stylesheet" href="assets/pages.css">
</head>
<body class="inner">

{nav('index.html')}

{mobile('index.html')}

{body}

{footer('index.html')}

{tags}
</body>
</html>
"""


PORTAL_RE = (r'href="https://md3homes\.managebuilding\.com/Resident/PublicPages/'
             r'Home\.aspx\?ReturnUrl=%2fresident" target="_blank" rel="noopener"'
             r'( style="[^"]*")?>')


def update_home(src):
    if "assets/pages.css" not in src:
        src = src.replace('<link rel="stylesheet" href="assets/styles.css">',
                          '<link rel="stylesheet" href="assets/styles.css">\n'
                          '<link rel="stylesheet" href="assets/pages.css">')
    if "assets/rentals.js" not in src:
        src = src.replace('<script src="assets/app.js"></script>',
                          '<script src="assets/app.js"></script>\n'
                          '<script src="assets/rentals.js"></script>')

    for p in PAGES:
        src = src.replace(f'<a class="scard" href="#">\n      <div class="ph">'
                          f'<img src="{IMG}{p["img"]}"',
                          f'<a class="scard" href="{p["slug"]}.html">\n      '
                          f'<div class="ph"><img src="{IMG}{p["img"]}"')

    for key, (label, _) in GROUPS.items():
        subs = "".join(f'<li><a href="{h}">{html.escape(t)}</a></li>'
                       for h, t in sub_items(key))
        src = re.sub(rf'(<a href="#{key}">{label} <svg.*?</svg></a>\s*)'
                     rf'<ul class="sub">.*?</ul>',
                     lambda m: m.group(1) + f'<ul class="sub">{subs}</ul>',
                     src, flags=re.S)
        kids = "".join(f'<a href="{h}">{html.escape(t)}</a>'
                       for h, t in sub_items(key))
        src = re.sub(rf'(<div class="grp">\s*<a href="#{key}">{label}</a>\s*)'
                     rf'<div class="kids">.*?</div>',
                     lambda m: m.group(1) + f'<div class="kids">{kids}</div>',
                     src, flags=re.S)

    for text, target in [("Start buying", "how-to-buy.html"),
                         ("Start selling", "how-to-sell.html"),
                         ("See the difference", "who-is-eligible-to-rent.html")]:
        src = src.replace(f'<a class="more" href="#">{text}',
                          f'<a class="more" href="{target}">{text}')

    src = re.sub(PORTAL_RE + "MD3 Exclusives",
                 lambda m: f'href="rentals.html"{m.group(1) or ""}>MD3 Exclusives', src)
    src = re.sub(PORTAL_RE + "Sign In",
                 lambda m: f'href="rentals.html#access"{m.group(1) or ""}>Sign In', src)

    block = rb.featured_home()
    if "<!-- featured-rentals -->" in src:
        src = re.sub(r"<!-- featured-rentals -->.*?<!-- /featured-rentals -->",
                     lambda m: block, src, flags=re.S)
    else:
        src = src.replace('<section class="statement',
                          block + '\n\n<section class="statement', 1)
    return src


def main():
    styles = ASSETS / "styles.css"
    base = styles.read_text(encoding="utf-8")
    marker = "/* ---------- paginas internas ---------- */"
    if marker in base:
        styles.write_text(base[:base.index(marker)].rstrip() + "\n", encoding="utf-8")

    (ASSETS / "pages.css").write_text(
        EXTRA_CSS.strip() + "\n\n"
        + (ASSETS / "rentals.css").read_text(encoding="utf-8"), encoding="utf-8")
    (ASSETS / "rentals.js").write_text(rb.RENTALS_JS, encoding="utf-8")

    HOME.write_text(update_home(HOME.read_text(encoding="utf-8")), encoding="utf-8")

    for p in PAGES:
        (ROOT / f"{p['slug']}.html").write_text(page_html(p), encoding="utf-8")
    (ROOT / "rentals.html").write_text(
        page_shell("Available Rentals &mdash; MD3 Homes", rb.rentals_body(),
                   ("assets/app.js", "assets/rentals.js")), encoding="utf-8")
    for l in rb.LISTINGS:
        title = f"{html.escape(l['address'])}, {html.escape(l['city'])} &mdash; MD3 Homes"
        (ROOT / f"{l['slug']}.html").write_text(
            page_shell(title, rb.listing_body(l),
                       ("assets/app.js", "assets/rentals.js")), encoding="utf-8")

    # cache-busting: ?v=<hash del contenido> en cada CSS/JS compartido
    import hashlib
    names = ["styles.css", "pages.css", "app.js", "rentals.js"]
    ver = hashlib.sha1(b"".join((ASSETS / n).read_bytes() for n in names)).hexdigest()[:8]
    asset_re = re.compile(r'(assets/(?:styles|pages)\.css|assets/(?:app|rentals)\.js)(\?v=\w+)?')
    for page in ROOT.glob("*.html"):
        if page.name == "comparacion.html":
            continue
        text = page.read_text(encoding="utf-8")
        page.write_text(asset_re.sub(lambda m: f"{m.group(1)}?v={ver}", text),
                        encoding="utf-8")

    print(f"OK: {len(PAGES)} paginas + rentals + {len(rb.LISTINGS)} fichas + home (v={ver})")


if __name__ == "__main__":
    main()
