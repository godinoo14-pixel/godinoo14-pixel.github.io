#!/usr/bin/env python3
"""Genera un borrador de página SEO con IA a partir de una palabra clave.
Uso:  ANTHROPIC_API_KEY=... python3 automation/nueva_pagina.py "calculadora regla 50 30 20"
Crea content/<slug>.json como BORRADOR (draft=true). Revísalo, pon draft=false y ejecuta build.py.
Regla de oro: nada se publica sin revisión humana (calidad = aprobación de AdSense y posiciones)."""
import json, os, re, sys, urllib.request

MODEL = "claude-sonnet-5-5"
PROMPT = """Eres redactor SEO experto en finanzas personales en español neutro.
Palabra clave principal: "{kw}".
Devuelve SOLO un JSON con estas claves:
slug (kebab-case, sin tildes), short (2-3 palabras), title (<=60 caracteres), desc (<=155 caracteres),
h1, lead (1 frase), body_html (600-900 palabras en HTML simple: <article class="card"> con <h2>, <h3>, <p>, <ul>, <table>;
explica la fórmula, un ejemplo numérico correcto y consejos prácticos; sin promesas de rentabilidad),
faqs (lista de 3-5 pares [pregunta, respuesta]).
No inventes datos legales ni cifras oficiales; si dependen del país, dilo."""

def slugify(s):
    s = s.lower()
    for a, b in zip("áéíóúñü", "aeiounu"): s = s.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")

def main(kw):
    key = os.environ["ANTHROPIC_API_KEY"]
    req = urllib.request.Request("https://api.anthropic.com/v1/messages", method="POST",
        headers={"x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json"},
        data=json.dumps({"model": MODEL, "max_tokens": 4000,
                         "messages": [{"role": "user", "content": PROMPT.format(kw=kw)}]}).encode())
    txt = json.load(urllib.request.urlopen(req))["content"][0]["text"]
    data = json.loads(txt[txt.find("{"): txt.rfind("}") + 1])
    data["slug"] = slugify(data.get("slug") or kw)
    data["draft"] = True
    os.makedirs("content", exist_ok=True)
    path = f"content/{data['slug']}.json"
    json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("Borrador creado:", path)

if __name__ == "__main__":
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    main(" ".join(sys.argv[1:]))
