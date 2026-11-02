#!/usr/bin/env python3
"""Numeria — generador del sitio estático de calculadoras financieras.
Uso:  python3 build.py   → genera /dist listo para subir (Cloudflare Pages / Netlify).
Añadir una calculadora = añadir un dict a PAGES (+ su lógica en src/app.js).
Las páginas también pueden venir de content/*.json (pipeline de automatización)."""
import json, os, shutil, datetime, html, glob

CONFIG = {
    "domain": "https://godinoo14-pixel.github.io",       # cambia por tu dominio
    "brand": "Numeria",
    "adsense_client": "",                          # "ca-pub-XXXXXXXXXXXXXXXX" (vacío = huecos de prueba)
    "cf_analytics_token": "",                      # Cloudflare Web Analytics (sin cookies)
    "contact_email": "hola@numeria.app",
    "owner": "Juan Pedro Godino Moreno",
    "aff": {                                       # sustituye al aprobarte en cada programa
        "inversion": "#AFILIADO-INVERSION",        # bróker / roboadvisor
        "cuenta": "#AFILIADO-CUENTA-REMUNERADA",
        "hipoteca": "#AFILIADO-HIPOTECA",          # comparador / bróker hipotecario (lead)
        "prestamo": "#AFILIADO-PRESTAMO",
    },
}
TODAY = datetime.date.today().isoformat()
D = CONFIG["domain"]

def ad(slot):
    c = CONFIG["adsense_client"]
    if not c: return f'<div class="ad-slot">Espacio publicitario ({slot})</div>'
    return (f'<div class="ad-slot live"><ins class="adsbygoogle" style="display:block" data-ad-client="{c}" data-ad-slot="{slot}" '
            f'data-ad-format="auto" data-full-width-responsive="true"></ins><script>(adsbygoogle=window.adsbygoogle||[]).push({{}});</script></div>')

def cta(kind, title, text, btn):
    return (f'<div class="cta"><p><b>{title}</b>{text}</p><a class="btn" href="{CONFIG["aff"][kind]}" rel="sponsored nofollow noopener" '
            f'target="_blank" onclick="window.gtag&&gtag(\'event\',\'afiliado\',{{tipo:\'{kind}\'}})">{btn}</a></div>')

def faqs_block(faqs):
    return '<section class="card"><h2>Preguntas frecuentes</h2>' + "".join(
        f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs) + "</section>"

def field(id_, label, value, hint="", step="any", mode="decimal"):
    h = f' <span class="hint">{hint}</span>' if hint else ""
    return f'<div><label for="{id_}">{label}{h}</label><input id="{id_}" type="number" inputmode="{mode}" step="{step}" value="{value}"></div>'

def calc(id_, fields, chart=False, note=""):
    ch = f'<div class="chart" id="{id_}-chart"></div>' if chart else ""
    nt = f'<p class="note">{note}</p>' if note else ""
    return f'<section class="card calc" id="{id_}"><div class="grid">{"".join(fields)}</div><div class="res" id="{id_}-out"></div>{ch}{nt}</section>'

def layout(p):
    head_ads = (f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={CONFIG["adsense_client"]}" crossorigin="anonymous"></script>'
                if CONFIG["adsense_client"] else "")
    cf = (f'<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon=\'{{"token":"{CONFIG["cf_analytics_token"]}"}}\'></script>'
          if CONFIG["cf_analytics_token"] else "")
    lds = [{"@context": "https://schema.org", "@type": "WebApplication" if p.get("tool") else "WebPage", "name": p["h1"],
            "url": f'{D}/{p["slug"]}', "applicationCategory": "FinanceApplication", "operatingSystem": "Web", "inLanguage": "es",
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}}]
    if p.get("faqs"):
        lds.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": html.unescape(a)}} for q, a in p["faqs"]]})
    ld = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in lds)
    crumbs = "" if p["slug"] == "" else f'<div class="crumbs"><a href="/">Inicio</a> › {p["short"]}</div>'
    lead = f'<p>{p["lead"]}</p>' if p.get("lead") else ""
    body = p["body"] + (faqs_block(p["faqs"]) if p.get("faqs") else "") + (related(p["slug"]) if p.get("tool") else "")
    return f"""<!doctype html><html lang="es" data-cur="EUR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{p["title"]}</title>
<meta name="description" content="{p["desc"]}"><link rel="canonical" href="{D}/{p["slug"]}">
<meta property="og:title" content="{p["title"]}"><meta property="og:description" content="{p["desc"]}"><meta property="og:type" content="website">
<meta name="theme-color" content="#0f1b2d"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/style.css">{head_ads}{ld}</head><body>
<header class="top"><div class="wrap"><a class="logo" href="/">Nume<span>ria</span></a><nav class="main">
<a href="/calculadora-interes-compuesto">Interés compuesto</a><a href="/calculadora-hipoteca">Hipoteca</a><a href="/calculadora-prestamo">Préstamo</a><a href="/calculadora-independencia-financiera">FIRE</a></nav></div></header>
<section class="hero"><div class="wrap">{crumbs}<h1>{p["h1"]}</h1>{lead}</div></section>
<main><div class="wrap">{body}</div></main>
<footer><div class="wrap"><p><a href="/sobre-nosotros">Sobre nosotros</a><a href="/aviso-legal">Aviso legal</a><a href="/privacidad">Privacidad y cookies</a><a href="mailto:{CONFIG["contact_email"]}">Contacto</a></p>
<p>© {datetime.date.today().year} {CONFIG["brand"]}. Herramientas con fines informativos; no constituyen asesoramiento financiero. Rentabilidades pasadas no garantizan rentabilidades futuras. Algunos enlaces son de afiliado: si contratas a través de ellos podemos recibir una comisión sin coste para ti.</p></div></footer>
<script src="/app.js" defer></script><script src="/tools.js" defer></script>{cf}</body></html>"""

TOOLS = [("📈","calculadora-interes-compuesto","Interés compuesto","Cuánto crecerá tu dinero con aportaciones mensuales."),
         ("🏠","calculadora-hipoteca","Hipoteca","Cuota, intereses y cuánto pesa en tu sueldo."),
         ("💳","calculadora-prestamo","Préstamo y TAE","El coste real de un préstamo personal."),
         ("🎯","calculadora-ahorro","Objetivo de ahorro","Cuánto ahorrar al mes para llegar a tu meta."),
         ("🔥","calculadora-independencia-financiera","Independencia financiera","Cuándo podrías vivir de tus inversiones.")]

def related(slug):
    tools = [p for p in PAGES if p.get("tool") and p["slug"] not in ("", slug)]
    i = next((k for k, p in enumerate(tools) if p["slug"] > slug), 0)
    pick = (tools[i:] + tools[:i])[:6]   # vecinos distintos en cada página → enlazado interno repartido
    items = "".join(f'<a class="tool" href="/{p["slug"]}"><b>{p["short"]}</b><span>{p["desc"][:90]}…</span></a>' for p in pick)
    return f'<h2 style="margin:8px 0 14px">Otras calculadoras</h2><div class="tools">{items}</div>'

# ------------------------------------------------------------------ PÁGINAS
PAGES = []
P = lambda **k: PAGES.append(dict(tool=True, **k))

P(slug="calculadora-interes-compuesto", short="Interés compuesto",
  title="Calculadora de interés compuesto con aportaciones mensuales (gratis)",
  desc="Calcula cuánto dinero tendrás invirtiendo cada mes con interés compuesto. Incluye gráfico, intereses generados y efecto de la inflación.",
  h1="Calculadora de interés compuesto",
  lead="Descubre cuánto crecerá tu dinero si inviertes una cantidad inicial y aportas cada mes. Con gráfico año a año y ajuste por inflación.",
  body=calc("ic", [field("ic-ini","Capital inicial (€)",1000), field("ic-men","Aportación mensual (€)",200),
                   field("ic-tasa","Rentabilidad anual esperada (%)",6,"orientativa"), field("ic-anos","Años",20,mode="numeric",step="1"),
                   field("ic-inf","Inflación anual estimada (%)",2.5)], chart=True,
               note="Capitalización mensual. No incluye comisiones ni impuestos sobre las ganancias.")
   + cta("inversion","Empieza a invertir con poco dinero"," Compara plataformas de inversión indexada con comisiones bajas.","Ver plataformas") + ad("ic-1") +
   """<article class="card"><h2>Qué es el interés compuesto</h2><p>Es ganar intereses sobre los intereses. Cada año la rentabilidad se aplica sobre todo lo acumulado, no solo sobre lo que aportaste, y por eso el crecimiento se acelera con el tiempo. El factor más poderoso no es la rentabilidad, sino los <strong>años</strong>.</p>
<h3>Fórmula</h3><p>Capital final = C·(1+r)<sup>n</sup> + A·[((1+r)<sup>n</sup> − 1) / r], con r la rentabilidad por periodo, n el número de periodos, C el capital inicial y A la aportación periódica.</p>
<h3>Ejemplo</h3><p>Con 1.000 € iniciales y 200 € al mes durante 20 años al 6 % anual aportas 49.000 € y acabas con unos 96.000 €: casi la mitad son intereses.</p>
<h2>Cómo usar bien esta calculadora</h2><p>Sé prudente con la rentabilidad: prueba escenarios del 3 %, 5 % y 7 % y fíjate en el valor ajustado por inflación, que es lo que tu dinero podrá comprar de verdad.</p></article>""" + ad("ic-2"),
  faqs=[("¿Qué rentabilidad es realista?","Depende del activo. Un depósito ofrece poco más que la inflación; la renta variable global ha dado históricamente más a largo plazo, con caídas fuertes por el camino. Usa varios escenarios."),
        ("¿Cada cuánto se capitaliza?","Esta calculadora capitaliza mensualmente, como ocurre al invertir con aportaciones periódicas."),
        ("¿Incluye impuestos?","No. Las ganancias tributan según la normativa de tu país al venderlas o cobrarlas."),
        ("¿Qué es el valor ajustado por inflación?","Es el capital final expresado en dinero de hoy: lo que podrías comprar con él a precios actuales.")])

P(slug="calculadora-hipoteca", short="Hipoteca",
  title="Calculadora de hipoteca: cuota mensual, intereses y esfuerzo",
  desc="Calcula la cuota de tu hipoteca, los intereses totales y qué porcentaje de tu sueldo supone. Con cuadro de amortización anual.",
  h1="Calculadora de hipoteca",
  lead="Calcula la cuota mensual, cuánto pagarás de intereses y si la hipoteca es asumible con tus ingresos.",
  body=calc("hip", [field("hip-precio","Precio de la vivienda (€)",250000), field("hip-entrada","Ahorro aportado (€)",50000),
                    field("hip-tin","Tipo de interés anual (%)",2.9), field("hip-anos","Plazo (años)",30,mode="numeric",step="1"),
                    field("hip-ingresos","Ingresos netos mensuales del hogar (€)",3500,"opcional")], chart=True,
               note="Sistema de amortización francés. No incluye impuestos de compra, notaría ni seguros vinculados.")
   + cta("hipoteca","Compara hipotecas de varios bancos"," Un bróker hipotecario puede conseguirte mejor tipo sin que tengas que ir banco por banco.","Comparar hipotecas") + ad("hip-1") +
   """<article class="card"><h2>Cómo se calcula la cuota</h2><p>Con el sistema francés pagas siempre la misma cuota. Al principio casi todo son intereses y, con los años, va ganando peso el capital: lo verás en el gráfico.</p>
<h3>La regla del 35 %</h3><p>Los bancos suelen exigir que la cuota no supere el 30–35 % de los ingresos netos. Por encima de eso, el riesgo de no poder pagar crece y es más difícil que te aprueben.</p>
<h3>Cuánto ahorro necesitas</h3><p>Normalmente se financia hasta el 80 % del valor de tasación, así que necesitas el 20 % restante más los gastos e impuestos de compra, que pueden sumar otro 10 % aproximadamente.</p></article>""" + ad("hip-2"),
  faqs=[("¿Fijo, variable o mixto?","Con fijo la cuota no cambia; con variable depende del índice de referencia; el mixto combina un periodo fijo inicial con uno variable. La elección depende de tu tolerancia al riesgo y del diferencial ofrecido."),
        ("¿Me conviene un plazo más largo?","Baja la cuota pero aumenta mucho el total de intereses. Prueba 20, 25 y 30 años en la calculadora para comparar."),
        ("¿Qué gastos no incluye?","Impuestos de la compraventa, notaría, registro, tasación y seguros vinculados.")])

P(slug="calculadora-prestamo", short="Préstamo y TAE",
  title="Calculadora de préstamos personales: cuota, intereses y TAE real",
  desc="Calcula la cuota mensual de un préstamo, los intereses totales y la TAE real incluyendo la comisión de apertura.",
  h1="Calculadora de préstamo y TAE",
  lead="Antes de firmar, calcula cuánto te cuesta de verdad el préstamo: cuota, intereses, comisiones y TAE.",
  body=calc("pre", [field("pre-imp","Importe (€)",10000), field("pre-tin","TIN anual (%)",7.5),
                    field("pre-meses","Plazo (meses)",48,mode="numeric",step="1"), field("pre-com","Comisión de apertura (%)",2)],
               note="La TAE se calcula a partir de la cuota y la comisión. No incluye seguros vinculados.")
   + cta("prestamo","Compara préstamos sin compromiso"," Consultar ofertas no afecta a tu historial si no firmas.","Ver préstamos") + ad("pre-1") +
   """<article class="card"><h2>TIN y TAE: la diferencia que te cuesta dinero</h2><p>El TIN es el interés puro. La TAE suma comisiones y gastos y lo expresa como interés anual: es la cifra que permite comparar dos préstamos. Un préstamo con TIN bajo y comisión alta puede salir más caro que otro con TIN algo mayor y sin comisiones.</p>
<h3>Trucos para pagar menos</h3><ul><li>Pide la oferta por escrito con la TAE y el importe total adeudado.</li><li>Evita seguros vinculados que no necesites.</li><li>Si puedes, amortiza anticipadamente para reducir intereses.</li></ul></article>""" + ad("pre-2"),
  faqs=[("¿Qué es el importe total adeudado?","Lo que devolverás en total: capital, intereses y comisiones. Es la mejor cifra para ver el coste real."),
        ("¿Por qué mi TAE sale más alta que el TIN?","Porque la comisión de apertura reduce el dinero que recibes realmente mientras sigues pagando intereses por el total.")])

P(slug="calculadora-ahorro", short="Objetivo de ahorro",
  title="Calculadora de ahorro: cuánto ahorrar al mes para tu objetivo",
  desc="Calcula cuánto necesitas ahorrar cada mes para conseguir una meta (entrada de piso, viaje, colchón) en el plazo que elijas.",
  h1="¿Cuánto tengo que ahorrar al mes?",
  lead="Fija una meta y un plazo y descubre la cantidad mensual que necesitas, teniendo en cuenta la rentabilidad de tus ahorros.",
  body=calc("ah", [field("ah-obj","Objetivo (€)",30000), field("ah-ini","Ya tengo ahorrado (€)",2000),
                   field("ah-anos","Plazo (años)",5,step="0.5"), field("ah-tasa","Rentabilidad anual de tus ahorros (%)",2)])
   + cta("cuenta","Haz que tus ahorros trabajen"," Compara cuentas remuneradas y depósitos sin comisiones.","Ver cuentas") + ad("ah-1") +
   """<article class="card"><h2>Cómo conseguir tu objetivo</h2><p>Automatiza: programa una transferencia el día que cobras a una cuenta separada. Lo que no ves, no lo gastas. Si el objetivo es a menos de 3 años, prioriza la seguridad (cuenta remunerada o depósito) frente a la rentabilidad.</p>
<h3>Metas habituales</h3><ul><li><strong>Fondo de emergencia:</strong> de 3 a 6 meses de gastos.</li><li><strong>Entrada de una vivienda:</strong> en torno al 20 % del precio más gastos de compra.</li><li><strong>Coche o viaje:</strong> mejor ahorrar antes que financiar.</li></ul></article>""" + ad("ah-2"),
  faqs=[("¿Dónde guardo el dinero mientras ahorro?","Para plazos cortos, en productos sin riesgo y líquidos como cuentas remuneradas o depósitos con garantía de depósitos."),
        ("¿Y si no llego a la cantidad mensual?","Alarga el plazo o reduce el objetivo; prueba combinaciones en la calculadora hasta encontrar una cifra sostenible.")])

P(slug="calculadora-independencia-financiera", short="Independencia financiera",
  title="Calculadora FIRE: ¿cuándo podrás vivir de tus inversiones?",
  desc="Calcula cuántos años te faltan para la independencia financiera (FIRE) según tus gastos, ahorro mensual y rentabilidad, con la regla del 4 %.",
  h1="Calculadora de independencia financiera (FIRE)",
  lead="Calcula el capital que necesitas para vivir de tus inversiones y cuántos años tardarás en conseguirlo.",
  body=calc("fire", [field("fi-gasto","Gasto mensual que quieres cubrir (€)",2000), field("fi-ahorro","Ahorro/inversión mensual (€)",800),
                     field("fi-cap","Capital invertido actual (€)",15000), field("fi-tasa","Rentabilidad anual real (%)",5,"descontada la inflación"),
                     field("fi-retiro","Tasa de retiro segura (%)",4)],
               note="Modelo simplificado con rentabilidad constante. En la realidad los mercados fluctúan.")
   + cta("inversion","Invierte de forma indexada y automática"," Compara roboadvisors y brókers con aportaciones periódicas.","Comparar opciones") + ad("fi-1") +
   """<article class="card"><h2>Qué es el movimiento FIRE</h2><p>FIRE (Financial Independence, Retire Early) consiste en ahorrar e invertir una parte alta de los ingresos para alcanzar un capital que cubra tus gastos indefinidamente.</p>
<h3>La regla del 4 %</h3><p>Proviene de estudios históricos sobre carteras de acciones y bonos: retirar alrededor del 4 % anual del capital inicial resistió la mayoría de periodos de 30 años. Por eso el objetivo suele ser 25 veces tus gastos anuales. Para horizontes más largos, muchos prefieren el 3–3,5 %.</p>
<h3>Las dos palancas</h3><p>Ganar más y gastar menos. Reducir gastos tiene doble efecto: aumenta tu ahorro y baja el capital que necesitas.</p></article>""" + ad("fi-2"),
  faqs=[("¿Qué rentabilidad uso?","Una rentabilidad real (descontada la inflación), porque el gasto objetivo está en euros de hoy. Un 4–5 % es una hipótesis habitual para carteras de renta variable diversificada, sin garantías."),
        ("¿Es lo mismo que jubilarse?","No necesariamente: muchos lo usan para trabajar en lo que quieren, reducir jornada o emprender sin presión económica.")])

# Fase 2: calculadoras del motor genérico
import tools_pages
tools_pages.register(P, field, ad, cta)

# Páginas generadas por la automatización (content/*.json)
for fp in sorted(glob.glob("content/*.json")):
    d = json.load(open(fp, encoding="utf-8"))
    if d.get("draft"): continue          # los borradores no se publican hasta revisarlos
    P(slug=d["slug"], short=d["short"], title=d["title"], desc=d["desc"], h1=d["h1"], lead=d.get("lead",""),
      body=d["body_html"] + ad(d["slug"][:10]), faqs=[tuple(x) for x in d.get("faqs", [])])

home_cards = "".join(f'<a class="tool" href="/{s}"><i>{i}</i><b>{t}</b><span>{d}</span></a>' for i, s, t, d in TOOLS)
extra = [p for p in PAGES if p.get("tool") and p["slug"] not in {t[1] for t in TOOLS}]
home_cards += "".join(f'<a class="tool" href="/{p["slug"]}"><b>{p["short"]}</b><span>{p["desc"][:90]}…</span></a>' for p in extra)
PAGES.insert(0, dict(slug="", short="Inicio", tool=False,
  title="Numeria — Calculadoras financieras gratis: interés compuesto, hipoteca, préstamos",
  desc="Calculadoras financieras gratuitas y sin registro: interés compuesto, hipoteca, préstamos y TAE, objetivo de ahorro e independencia financiera.",
  h1="Calculadoras para tomar mejores decisiones con tu dinero", lead="Gratis, sin registro y en segundos. Tus datos no salen de tu navegador.",
  body=f'<div class="tools">{home_cards}</div><br>' + ad("home-1") +
  """<article class="card"><h2>Números claros, sin letra pequeña</h2><p>Numeria reúne calculadoras para las decisiones de dinero más habituales: cuánto puedes ahorrar, cuánto te cuesta realmente un préstamo, qué hipoteca puedes permitirte o cuánto necesitas para no depender de un sueldo. Cada herramienta explica la fórmula que utiliza para que puedas comprobar el resultado.</p></article>"""
  + cta("inversion","¿Empiezas a invertir?"," Compara plataformas de inversión con comisiones bajas.","Ver plataformas")))

def legal(slug, h1, text):
    PAGES.append(dict(slug=slug, short=h1, tool=False, title=f"{h1} — {CONFIG['brand']}", desc=f"{h1} de {CONFIG['brand']}.", h1=h1, lead="", body=f'<article class="card">{text}</article>'))
legal("sobre-nosotros","Sobre nosotros",f"<p>{CONFIG['brand']} es un proyecto independiente de {CONFIG['owner']}, con formación en Administración y Dirección de Empresas y en finanzas. Creamos herramientas sencillas para que cualquiera entienda los números de sus decisiones económicas.</p><p>Cada calculadora muestra su fórmula y se revisa periódicamente. Contacto: <a href='mailto:{CONFIG['contact_email']}'>{CONFIG['contact_email']}</a></p>")
legal("aviso-legal","Aviso legal",f"<p>Titular: {CONFIG['owner']}. Contacto: {CONFIG['contact_email']}. [Completa con NIF y domicilio cuando des de alta la actividad.]</p><p>Los resultados son estimaciones con fines informativos y no constituyen asesoramiento financiero, fiscal ni de inversión. Invertir conlleva riesgo de pérdida.</p><p>Este sitio contiene publicidad y enlaces de afiliado; podemos recibir una comisión si contratas a través de ellos, sin coste adicional para ti.</p>")
legal("privacidad","Política de privacidad y cookies",f"<p>Responsable: {CONFIG['owner']} ({CONFIG['contact_email']}).</p><p><strong>Datos:</strong> las calculadoras funcionan en tu navegador; no almacenamos lo que introduces.</p><p><strong>Analítica:</strong> Cloudflare Web Analytics, sin cookies ni identificación de usuarios.</p><p><strong>Publicidad:</strong> Google AdSense puede usar cookies; se solicita tu consentimiento mediante la plataforma de consentimiento certificada de Google antes de usarlas. Más información en <a href='https://policies.google.com/technologies/ads' rel='nofollow'>las políticas de Google</a>.</p><p><strong>Derechos:</strong> acceso, rectificación y supresión escribiendo al correo indicado.</p>")

def build(out="dist"):
    if os.path.exists(out): shutil.rmtree(out)
    os.makedirs(out)
    for p in PAGES:
        with open(os.path.join(out, "index.html" if p["slug"] == "" else f'{p["slug"]}.html'), "w", encoding="utf-8") as f:
            f.write(layout(p))
    for a in ("style.css", "app.js", "tools.js", "favicon.svg"): shutil.copy(os.path.join("src", a), os.path.join(out, a))
    urls = "".join(f'<url><loc>{D}/{p["slug"]}</loc><lastmod>{TODAY}</lastmod></url>' for p in PAGES)
    open(os.path.join(out, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    open(os.path.join(out, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {D}/sitemap.xml\n")
    pub = CONFIG["adsense_client"].replace("ca-", "") or "pub-XXXXXXXXXXXXXXXX"
    open(os.path.join(out, "ads.txt"), "w").write(f"google.com, {pub}, DIRECT, f08c47fec0942fa0\n")
    print(f"OK: {len(PAGES)} páginas en /{out}")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    build()
