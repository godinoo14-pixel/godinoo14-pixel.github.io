# Numeria: red de calculadoras financieras

Sitio estático y rápido, sin servidor ni base de datos. Coste: solo el dominio (unos 10–15 €/año).

## Estructura
- `build.py`: genera la web en `/dist`. Arriba está `CONFIG` (dominio, AdSense, analítica y enlaces de afiliado).
- `src/`: estilos (`style.css`) y lógica de las calculadoras (`app.js`).
- `content/*.json`: páginas extra generadas con IA. Las marcadas como `draft: true` no se publican.
- `automation/nueva_pagina.py`: crea un borrador de página a partir de una palabra clave.

## Ponerla online (unos 20 minutos)
1. **Dominio**: compra `numeria.app` o el que esté libre en Cloudflare Registrar. Si es otro, cámbialo en `CONFIG["domain"]`.
2. **GitHub**: crea un repo privado y sube esta carpeta.
3. **Cloudflare Pages**: conecta el repo y configura:
   - Build command: `python3 build.py`
   - Output: `dist`
   
   A partir de ahí, cada cambio que subas se publica solo.
4. **Analítica**: en Cloudflare, activa Web Analytics y pega el token en `cf_analytics_token`. No usa cookies.
5. **Google Search Console**: verifica el dominio y envía `https://tu-dominio/sitemap.xml`.

## Monetización (requiere tu registro)
| Servicio | Para qué | Cuándo |
|---|---|---|
| Google AdSense | Anuncios | Con el sitio online y unas 15–20 páginas útiles. Pega tu `ca-pub-…` en `adsense_client` y se rellenan solos los anuncios y `ads.txt`. |
| AdSense › Privacidad y mensajes | Banner de consentimiento certificado (obligatorio en la UE) | Al aprobarte. Es gratuito. |
| Awin / Admitad / Tradedoubler | Afiliación de bancos, cuentas, préstamos y brókers | Ya. Sustituye los `#AFILIADO-…` en `CONFIG["aff"]`. |
| Programas de bróker / roboadvisor | CPA por cuenta abierta | Ya, si tienen programa de afiliados oficial (no confundir con "invita a un amigo"). |

## Rutina de crecimiento (unos 30 minutos a la semana)
1. `python3 automation/nueva_pagina.py "palabra clave"` (necesita `ANTHROPIC_API_KEY`).
2. Revisa el JSON (cifras, ejemplo y tono) y cambia `draft` a `false`.
3. `git push`: Cloudflare publica y el sitemap se actualiza solo.
