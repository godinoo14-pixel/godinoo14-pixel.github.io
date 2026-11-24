import json, os, html, urllib.parse
# === CONFIGURACIÓN DE MONETIZACIÓN ===
ADSENSE_CLIENT = ""   # p.ej. "ca-pub-1234567890123456" cuando AdSense te apruebe
AMAZON_TAG = ""       # p.ej. "cochecuentas-21" (tu ID de Amazon Afiliados)
def amz(q, label):
    u = "https://www.amazon.es/s?k=" + urllib.parse.quote_plus(q) + ("&tag=" + AMAZON_TAG if AMAZON_TAG else "")
    return f'<a class="afl" href="{u}" rel="sponsored nofollow noopener" target="_blank">{label}</a>'
def ext(u, label):
    return f'<a class="afl" href="{u}" rel="sponsored nofollow noopener" target="_blank">{label}</a>'
NETWORK = [("CocheCuentas", "https://cochecuentas.es/"), ("CalculadoraDías", "https://calculadoradias.es/"), ("GastoLuz", "https://gastoluz.es/")]
OWNER = "Juan Pedro Godino Moreno"
MAIL = 'el correo indicado en el <a href="/aviso-legal.html">aviso legal general del sitio</a>'

def css(acc):
    return """*{box-sizing:border-box}body{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:#1d2433;background:#f6f7fb;line-height:1.6}
a{color:ACC}header{background:#fff;border-bottom:1px solid #e5e7ef}header .w{display:flex;justify-content:space-between;align-items:center;padding:14px 16px;flex-wrap:wrap}
.logo{font-weight:800;font-size:1.25rem;text-decoration:none;color:#1d2433}.logo span{color:ACC}nav a{margin-left:14px;font-size:.92rem;text-decoration:none;color:#4a5165}
.w{max-width:860px;margin:0 auto;padding:0 16px}h1{font-size:1.75rem;line-height:1.25;margin:28px 0 8px}h2{font-size:1.25rem;margin-top:32px}
.lead{color:#4a5165;font-size:1.05rem}.card{background:#fff;border:1px solid #e5e7ef;border-radius:14px;padding:20px;margin:20px 0;box-shadow:0 1px 3px rgba(0,0,0,.04)}
label{display:block;font-weight:600;font-size:.9rem;margin:12px 0 4px}input,select,textarea{width:100%;padding:11px 12px;border:1px solid #cfd3df;border-radius:10px;font-size:1rem;background:#fff;font-family:inherit}
.row{display:grid;grid-template-columns:1fr 1fr;gap:0 14px}@media(max-width:560px){.row{grid-template-columns:1fr}nav a{margin-left:8px;font-size:.85rem}}
button{margin-top:16px;width:100%;padding:13px;border:0;border-radius:10px;background:ACC;color:#fff;font-size:1.05rem;font-weight:700;cursor:pointer}
.res{margin-top:18px;padding:16px;border-radius:12px;background:ACCBG;font-size:1.05rem;display:none}.res b.big{font-size:1.7rem;display:block;color:ACC}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px;margin:20px 0}.tool{background:#fff;border:1px solid #e5e7ef;border-radius:14px;padding:18px;text-decoration:none;color:inherit;display:block}
.tool:hover{border-color:ACC}.tool h3{margin:0 0 6px;color:ACC;font-size:1.05rem}.tool p{margin:0;color:#4a5165;font-size:.92rem}
.ad{margin:22px 0;min-height:90px;border:1px dashed #cfd3df;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#9aa0b0;font-size:.8rem}
.faq details{background:#fff;border:1px solid #e5e7ef;border-radius:10px;padding:12px 14px;margin:8px 0}.faq summary{font-weight:600;cursor:pointer}
.chk{display:flex;align-items:center;gap:8px;margin:6px 0}.chk input[type=checkbox]{width:auto}.chk input[type=number]{width:90px;padding:6px}.chk span{flex:1}
table{width:100%;border-collapse:collapse;font-size:.95rem}td,th{padding:8px;border-bottom:1px solid #e5e7ef;text-align:left}
footer{margin-top:48px;background:#fff;border-top:1px solid #e5e7ef;padding:22px 0;font-size:.85rem;color:#6b7185}footer a{margin-right:12px;color:#6b7185}
#ck{position:fixed;bottom:0;left:0;right:0;background:#1d2433;color:#fff;padding:14px 16px;font-size:.88rem;display:none;z-index:9}#ck button{width:auto;margin:8px 8px 0 0;padding:8px 16px;font-size:.9rem}#ck .no{background:#4a5165}
.note{font-size:.85rem;color:#6b7185}.upd{font-size:.82rem;color:#6b7185;margin:-2px 0 6px}.share{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:18px 0;font-size:.9rem;color:#4a5165}.share a{padding:7px 12px;border-radius:999px;background:#fff;border:1px solid #e5e7ef;text-decoration:none;font-weight:600}.affbox div{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}.afl{display:inline-block;padding:9px 14px;border:1px solid ACC;border-radius:999px;text-decoration:none;font-weight:600;font-size:.92rem}""".replace("ACCBG", acc + "14").replace("ACC", acc)

JS_BASE = """const eur=n=>n.toLocaleString('es-ES',{style:'currency',currency:'EUR'});
const nf=(n,d=2)=>n.toLocaleString('es-ES',{maximumFractionDigits:d});
const v=id=>parseFloat(String(document.getElementById(id).value).replace(',','.'))||0;
function show(id,h){const r=document.getElementById(id);r.innerHTML=h;r.style.display='block';}
(function(){let s=null;try{s=localStorage.getItem('ck')}catch(e){}const b=document.getElementById('ck');if(!s)b.style.display='block';
function set(x){try{localStorage.setItem('ck',x)}catch(e){}b.style.display='none';}
document.getElementById('cka').onclick=()=>set('1');document.getElementById('ckr').onclick=()=>set('0');})();
"""

def page(site, slug, title, desc, body, faqs=(), h1=None, extra_js=""):
    base = site['base']
    url = base + ("" if slug == "index" else slug + ".html")
    is_tool = slug not in ("index", "aviso-legal", "privacidad", "cookies", "404", "sobre-nosotros")
    ld = [{"@context": "https://schema.org", "@type": "WebPage", "name": title, "description": desc, "url": url, "inLanguage": "es-ES", "dateModified": "2026-11-24"}]
    if slug == "index":
        ld.append({"@context": "https://schema.org", "@type": "WebSite", "name": site['name'], "url": base, "inLanguage": "es-ES"})
    else:
        ld.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": site['name'], "item": base},
            {"@type": "ListItem", "position": 2, "name": (h1 or title.split(' | ')[0]), "item": url}]})
    if is_tool:
        ld.append({"@context": "https://schema.org", "@type": "WebApplication", "name": (h1 or title.split(' | ')[0]), "url": url,
                   "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any", "inLanguage": "es-ES",
                   "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}})
    if faqs:
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]})
    faqh = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    faqh = f'<h2>Preguntas frecuentes</h2><div class="faq">{faqh}</div>' if faqs else ""
    rel = ""
    if slug not in ("index", "aviso-legal", "privacidad", "cookies", "404"):
        rel = '<h2>Otras calculadoras</h2><div class="grid">' + "".join(
            f'<a class="tool" href="{t[0]}.html"><h3>{t[1]}</h3><p>{t[2]}</p></a>' for t in site['tools'] if t[0] != slug) + '</div>'
    a = site.get('aff', {}).get(slug)
    aff = f'<div class="card affbox"><b>Te puede interesar</b><div>{a}</div><p class="note">Enlaces patrocinados: si compras a través de ellos podemos recibir una comisión sin coste para ti.</p></div>' if a else ''
    net = ' · '.join(f'<a href="{u}">{n}</a>' for n, u in NETWORK if n != site['name'])
    upd = '<p class="upd">Actualizado: noviembre de 2026 · Gratis y sin registro</p>' if is_tool else ''
    q = urllib.parse.quote
    share = (f'<div class="share"><span>¿Te ha sido útil? Compártela:</span>'
             f'<a href="https://wa.me/?text={q(title.split(" | ")[0] + " " + url)}" rel="noopener" target="_blank">WhatsApp</a>'
             f'<a href="https://t.me/share/url?url={q(url)}&text={q(title.split(" | ")[0])}" rel="noopener" target="_blank">Telegram</a>'
             f'<a href="https://twitter.com/intent/tweet?url={q(url)}&text={q(title.split(" | ")[0])}" rel="noopener" target="_blank">X</a></div>') if is_tool else ''
    navl = "".join(f'<a href="{t[0]}.html">{t[3]}</a>' for t in site['tools'][:3])
    e = html.escape
    return f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{url}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:type" content="website"><meta property="og:url" content="{url}">
<meta property="og:site_name" content="{site['name']}"><meta property="og:locale" content="es_ES"><meta name="twitter:card" content="summary">
<meta name="theme-color" content="{site['acc']}"><link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="style.css">
{('<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client='+ADSENSE_CLIENT+'" crossorigin="anonymous"></script>') if ADSENSE_CLIENT else "<!-- AdSense: rellena ADSENSE_CLIENT en gen.py -->"}
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script></head><body>
<header><div class="w"><a class="logo" href="index.html">{site['logo']}</a><nav>{navl}</nav></div></header>
<main class="w"><h1>{h1 or title.split(' | ')[0]}</h1>{upd}{body}{share}
{aff}<div class="ad"><!-- ADSENSE bloque inferior -->Publicidad</div>{faqh}{rel}</main>
<footer><div class="w"><p>© 2026 {site['name']} · Resultados orientativos; no sustituyen asesoramiento profesional.</p>
<p>Más calculadoras gratis: {net}</p><a href="sobre-nosotros.html">Sobre nosotros</a><a href="aviso-legal.html">Aviso legal</a><a href="privacidad.html">Privacidad</a><a href="cookies.html">Cookies</a></div></footer>
<div id="ck">Usamos cookies propias y de terceros (Google) para analítica y publicidad. <a href="cookies.html" style="color:#fff">Más info</a><br><button id="cka">Aceptar</button><button class="no" id="ckr">Rechazar</button></div>
<script>
{JS_BASE}
{extra_js}
if(typeof calc==='function'){{try{{const r=document.getElementById('r');if(r&&r.style.display!=='block')calc();}}catch(e){{}}}}
</script></body></html>"""

def legal(site):
    n = site['name']
    al = f"""<p>En cumplimiento de la Ley 34/2002 de Servicios de la Sociedad de la Información (LSSI-CE) se informa de que el titular de este sitio web es <b>{OWNER}</b>.</p>
<h2>Objeto</h2><p>{n} ofrece calculadoras y herramientas gratuitas de carácter informativo. Los resultados son estimaciones orientativas y no constituyen asesoramiento profesional. El titular no se responsabiliza de decisiones tomadas en base a ellos.</p>
<h2>Propiedad intelectual</h2><p>Los textos, diseño y código de este sitio pertenecen a su titular salvo indicación en contrario. Queda prohibida su reproducción sin autorización.</p>
<h2>Enlaces de afiliado</h2><p>Este sitio puede contener enlaces de afiliado: si compras a través de ellos podemos recibir una comisión sin coste adicional para ti.</p>"""
    pr = f"""<p><b>Responsable:</b> {OWNER}.</p><h2>Qué datos tratamos</h2><p>Las calculadoras funcionan íntegramente en tu navegador: los datos que introduces no se envían ni se guardan en ningún servidor. Solo se tratan datos de navegación a través de herramientas de analítica y publicidad (Google) si das tu consentimiento.</p>
<h2>Base legal</h2><p>Tu consentimiento (art. 6.1.a RGPD), que puedes retirar en cualquier momento borrando las cookies de tu navegador.</p><h2>Derechos</h2><p>Puedes ejercer tus derechos de acceso, rectificación, supresión, oposición, limitación y portabilidad contactando con el responsable. También puedes reclamar ante la Agencia Española de Protección de Datos (aepd.es).</p>"""
    ck = """<p>Este sitio usa cookies técnicas (necesarias para recordar tu elección sobre cookies) y, solo si las aceptas, cookies de terceros:</p>
<table><tr><th>Cookie</th><th>Titular</th><th>Finalidad</th></tr><tr><td>ck (localStorage)</td><td>Propia</td><td>Recordar tu consentimiento</td></tr><tr><td>_ga, _gid</td><td>Google Analytics</td><td>Estadísticas de visitas</td></tr><tr><td>__gads, IDE</td><td>Google AdSense</td><td>Mostrar y medir publicidad</td></tr></table>
<p>Puedes retirar el consentimiento o borrar las cookies desde la configuración de tu navegador. Cómo usa Google los datos: policies.google.com/technologies/partner-sites</p>"""
    return [("aviso-legal", "Aviso legal | " + n, "Aviso legal de " + n, al),
            ("privacidad", "Política de privacidad | " + n, "Política de privacidad de " + n, pr),
            ("cookies", "Política de cookies | " + n, "Política de cookies de " + n, ck)]

def build(site, pages):
    d = site['dir']
    os.makedirs(d, exist_ok=True)
    open(f"{d}/style.css", "w").write(css(site['acc']))
    grid = '<div class="grid">' + "".join(
        f'<a class="tool" href="{t[0]}.html"><h3>{t[1]}</h3><p>{t[2]}</p></a>' for t in site['tools']) + '</div>'
    home = ("index", site['home_title'], site['home_desc'],
            site['home_intro'] + '<div class="ad"><!-- ADSENSE bloque superior -->Publicidad</div>' + grid + site['home_extra'],
            site.get('home_faq', ()), site['home_h1'], "")
    for p in [home] + pages:
        slug, t, ds, b = p[:4]
        faqs = p[4] if len(p) > 4 else ()
        h1 = p[5] if len(p) > 5 else None
        js = p[6] if len(p) > 6 else ""
        open(f"{d}/{slug}.html", "w").write(page(site, slug, t, ds, b, faqs, h1, js))
    for slug, t, ds, b in legal(site):
        open(f"{d}/{slug}.html", "w").write(page(site, slug, t, ds, b))
    open(f"{d}/404.html", "w").write(page(site, "404", "Página no encontrada | " + site['name'], "Página no encontrada",
                                          '<p>Esta página no existe. <a href="index.html">Vuelve al inicio</a>.</p>'))
    letter = site['name'][0]
    open(f"{d}/favicon.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="{site["acc"]}"/><text x="32" y="44" font-family="Arial,sans-serif" font-size="36" font-weight="700" fill="#fff" text-anchor="middle">{letter}</text></svg>')
    about = site.get('about', f"<p>{site['name']} es un proyecto independiente de calculadoras gratuitas en español. Cada herramienta funciona en tu navegador, sin registro y sin guardar tus datos.</p>") + \
        "<h2>Cómo hacemos las calculadoras</h2><p>Partimos de fórmulas conocidas y de fuentes oficiales cuando las hay, explicamos el cálculo en cada página y revisamos las herramientas con regularidad. Los resultados son orientativos: para decisiones importantes, confírmalos con un profesional.</p>" + \
        "<h2>¿Has visto un error?</h2><p>Si algún resultado no te cuadra o echas en falta una calculadora, cuéntanoslo: mejoramos las webs cada semana.</p>"
    open(f"{d}/sobre-nosotros.html", "w").write(page(site, "sobre-nosotros", "Sobre nosotros | " + site['name'], "Quién está detrás de " + site['name'] + " y cómo hacemos nuestras calculadoras.", about, h1="Sobre " + site['name']))
    urls = [site['base']] + [site['base'] + p[0] + ".html" for p in pages] + [site['base'] + "sobre-nosotros.html"]
    open(f"{d}/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"<url><loc>{u}</loc><lastmod>2026-11-23</lastmod></url>\n" for u in urls) + "</urlset>\n")
    open(f"{d}/CNAME", "w").write(site["domain"] + "\n")
    open(f"{d}/.nojekyll", "w").write("")
    open(f"{d}/robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {site['base']}sitemap.xml\n")
    #open(f"{d}/ads.txt", "w").write("google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0\n")
