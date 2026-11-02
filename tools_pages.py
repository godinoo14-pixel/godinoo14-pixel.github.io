"""Calculadoras de la fase 2 (motor genérico src/tools.js). Se registran desde build.py."""

def sel(id_, label, opts):
    o = "".join(f'<option value="{v}"{" selected" if i == 0 else ""}>{t}</option>' for i, (v, t) in enumerate(opts))
    return f'<div><label for="{id_}">{label}</label><select id="{id_}">{o}</select></div>'

def register(P, field, ad, cta):
    def tool(tid, slug, short, title, desc, h1, lead, fields, article, faqs, aff=None, note=""):
        calc = (f'<section class="card calc" data-tool="{tid}"><div class="grid">{"".join(fields)}</div>'
                f'<div class="res"></div>{f"<p class=note>{note}</p>" if note else ""}</section>')
        c = cta(*aff) if aff else ""
        P(slug=slug, short=short, title=title, desc=desc, h1=h1, lead=lead, faqs=faqs,
          body=calc + ad(f"{tid}-1") + c + f'<article class="card">{article}</article>' + ad(f"{tid}-2"))

    tool("pct", "calculadora-porcentajes", "Porcentajes",
      "Calculadora de porcentajes online: % de una cantidad y variación",
      "Calcula el porcentaje de cualquier cantidad, la variación porcentual entre dos valores y qué porcentaje representa un número de otro.",
      "Calculadora de porcentajes", "Calcula el X % de una cantidad, cuánto ha subido o bajado algo en porcentaje y qué parte representa un valor de otro.",
      [field("pct-p", "Porcentaje (%)", 15), field("pct-n", "De la cantidad", 240), field("pct-a", "Valor A (inicial)", 80, "para la variación"), field("pct-b", "Valor B (final)", 100)],
      """<h2>Cómo calcular un porcentaje</h2><p>Para saber el X % de una cantidad, multiplica la cantidad por X y divide entre 100. El 15 % de 240 es 240 × 15 ÷ 100 = 36.</p>
<h3>Variación porcentual</h3><p>(Valor final − valor inicial) ÷ valor inicial × 100. Si algo pasa de 80 a 100, ha subido un 25 %. Ojo: si después baja de 100 a 80, la bajada es solo del 20 %, porque se calcula sobre una base distinta.</p>
<h3>Qué porcentaje es A de B</h3><p>A ÷ B × 100. Por ejemplo, 80 es el 80 % de 100.</p>""",
      [("¿Cómo sumo un porcentaje a un precio?", "Multiplica por (1 + porcentaje/100). Para sumar un 15 % a 240: 240 × 1,15 = 276."),
       ("¿Por qué subir y bajar el mismo % no deja el valor igual?", "Porque cada porcentaje se aplica sobre una base distinta. Subir un 10 % y luego bajar un 10 % deja el valor un 1 % por debajo.")])

    tool("iva", "calculadora-iva", "IVA",
      "Calculadora de IVA: añadir o quitar IVA (21 %, 10 %, 4 %)",
      "Calcula el precio con IVA o quita el IVA de un importe en segundos. Tipos general (21 %), reducido (10 %) y superreducido (4 %).",
      "Calculadora de IVA", "Añade el IVA a una base imponible o descubre cuánto IVA lleva un precio final.",
      [field("iva-imp", "Importe (€)", 100), sel("iva-tipo", "Tipo de IVA", [("21", "21 % (general)"), ("10", "10 % (reducido)"), ("4", "4 % (superreducido)")]),
       sel("iva-modo", "Quiero…", [("anadir", "Añadir IVA a la base"), ("quitar", "Quitar IVA del precio final")])],
      """<h2>Cómo calcular el IVA</h2><p><strong>Añadir IVA:</strong> base × (1 + tipo). 100 € al 21 % = 121 €.</p><p><strong>Quitar IVA:</strong> precio ÷ (1 + tipo). 121 € ÷ 1,21 = 100 €. El error típico es restar el 21 % al precio final: 121 − 21 % = 95,59 €, lo cual es incorrecto.</p>
<h3>Tipos de IVA en España</h3><table><tr><th>Tipo</th><th>Se aplica a (ejemplos)</th></tr><tr><td>21 %</td><td>La mayoría de bienes y servicios</td></tr><tr><td>10 %</td><td>Hostelería, transporte de viajeros, algunos alimentos</td></tr><tr><td>4 %</td><td>Pan, leche, frutas, libros, medicamentos</td></tr></table>
<p class="disclaimer">Los tipos aplicables a cada producto los fija la normativa; consúltala ante cualquier duda.</p>""",
      [("¿Cómo se quita el IVA de un precio?", "Divide el precio entre 1,21 (o 1,10 / 1,04 según el tipo). No restes el porcentaje directamente."),
       ("¿El IVA se aplica sobre el precio con descuento?", "Sí, la base imponible es el precio después de descuentos.")])

    tool("desc", "calculadora-descuentos", "Descuentos",
      "Calculadora de descuentos: precio final y ahorro (también descuentos dobles)",
      "Calcula el precio final con descuento, cuánto ahorras y el descuento real cuando se aplican dos rebajas seguidas.",
      "Calculadora de descuentos", "Descubre el precio final de una rebaja y el descuento real de las ofertas «−20 % + −10 % adicional».",
      [field("desc-precio", "Precio original (€)", 80), field("desc-d1", "Descuento (%)", 20), field("desc-d2", "Segundo descuento (%)", 10, "opcional")],
      """<h2>Cómo calcular un descuento</h2><p>Precio final = precio × (1 − descuento/100). Un 20 % sobre 80 € deja el precio en 64 €.</p>
<h3>El truco de los descuentos dobles</h3><p>Un «20 % + 10 % adicional» no es un 30 %: el segundo descuento se aplica sobre el precio ya rebajado. 80 € → 64 € → 57,60 €, es decir, un 28 % de descuento real.</p>
<h3>Antes de comprar</h3><p>Compara el precio final con el de otras tiendas, no el porcentaje: un 50 % sobre un precio inflado puede ser peor que un 15 % en otro sitio.</p>""",
      [("¿Se suman dos descuentos?", "No. Se multiplican: (1 − 0,20) × (1 − 0,10) = 0,72, es decir, un 28 % de descuento total.")])

    tool("r503020", "regla-50-30-20", "Regla 50/30/20",
      "Regla 50/30/20: calcula tu presupuesto mensual ideal",
      "Reparte tus ingresos netos con la regla 50/30/20: necesidades, deseos y ahorro. Calculadora gratuita con ejemplo.",
      "Calculadora de la regla 50/30/20", "Reparte tu sueldo neto en necesidades, caprichos y ahorro con el método de presupuesto más sencillo.",
      [field("r503020-ing", "Ingresos netos mensuales (€)", 1800)],
      """<h2>Qué es la regla 50/30/20</h2><p>Es un método de presupuesto que divide tus ingresos netos en tres bloques: <strong>50 % necesidades</strong> (vivienda, suministros, comida, transporte, deudas mínimas), <strong>30 % deseos</strong> (ocio, viajes, suscripciones) y <strong>20 % ahorro</strong> (fondo de emergencia, inversión, amortizar deudas).</p>
<h3>Si los números no te cuadran</h3><p>Con alquileres altos, las necesidades pueden superar el 50 %. En ese caso recorta primero de los deseos y mantén aunque sea un 10 % de ahorro automático. Lo importante es el hábito.</p>
<h3>Cómo aplicarla</h3><ol><li>Calcula tus cifras aquí.</li><li>Programa una transferencia automática del 20 % el día de cobro.</li><li>Revisa tus gastos fijos una vez al año.</li></ol>""",
      [("¿Se calcula sobre el bruto o el neto?", "Sobre el neto: lo que te llega a la cuenta."),
       ("¿Pagar deudas cuenta como ahorro?", "Los pagos mínimos son necesidades; lo que amortices de más puede ir al bloque del 20 %.")],
      aff=("cuenta", "Separa tu 20 % automáticamente", " Una cuenta remunerada aparte hace que el ahorro no se gaste.", "Ver cuentas"))

    tool("cagr", "calculadora-rentabilidad", "Rentabilidad (CAGR)",
      "Calculadora de rentabilidad anual (CAGR) de una inversión",
      "Calcula la rentabilidad total y la rentabilidad anual compuesta (CAGR) de cualquier inversión a partir de su valor inicial, final y años.",
      "Calculadora de rentabilidad anual (CAGR)", "Descubre cuánto ha rentado de verdad una inversión al año, para compararla con otras.",
      [field("cagr-ini", "Valor inicial (€)", 10000), field("cagr-fin", "Valor final (€)", 16000), field("cagr-anos", "Años", 5, step="0.5")],
      """<h2>Rentabilidad total frente a anual</h2><p>Si 10.000 € se convierten en 16.000 € en 5 años, la rentabilidad total es del 60 %, pero no un 12 % anual: por el efecto compuesto, la rentabilidad anual equivalente (CAGR) es del 9,86 %.</p>
<h3>Fórmula</h3><p>CAGR = (valor final ÷ valor inicial)<sup>1/años</sup> − 1.</p>
<h3>Para qué sirve</h3><p>Para comparar inversiones de distinta duración, por ejemplo un piso frente a un fondo indexado o un depósito, en la misma unidad: % al año.</p>""",
      [("¿Incluye dividendos o alquileres cobrados?", "Solo si los sumas al valor final. Para comparar bien, inclúyelos."),
       ("¿Qué es una buena rentabilidad?", "Depende del riesgo. Compárala siempre con la inflación y con alternativas de riesgo similar.")],
      aff=("inversion", "Compara dónde invertir", " Plataformas indexadas con comisiones bajas.", "Ver opciones"))

    tool("r72", "regla-del-72", "Regla del 72",
      "Regla del 72: en cuántos años se duplica tu dinero",
      "Calcula cuántos años tarda en duplicarse una inversión con la regla del 72 y con el cálculo exacto.",
      "Regla del 72: ¿cuándo se duplica tu dinero?", "Divide 72 entre la rentabilidad anual y sabrás, aproximadamente, cuántos años tarda en doblarse tu dinero.",
      [field("r72-tasa", "Rentabilidad anual (%)", 6)],
      """<h2>Cómo funciona</h2><p>Años para duplicar ≈ 72 ÷ rentabilidad anual. Al 6 % tardas unos 12 años; al 9 %, unos 8. Es una aproximación muy buena para tipos entre el 4 % y el 12 %.</p>
<h3>Al revés: la inflación</h3><p>La regla también sirve para lo malo: con un 3 % de inflación, los precios se duplican en unos 24 años, y con una deuda al 24 % TAE, lo que debes se duplica en 3 años si no pagas.</p>""",
      [("¿Por qué 72?", "Porque es un número cercano a 100 × ln(2) ≈ 69,3, ajustado para tipos habituales y fácil de dividir mentalmente.")])

    tool("inf", "calculadora-inflacion", "Inflación",
      "Calculadora de inflación: poder adquisitivo de tu dinero en el futuro",
      "Calcula cuánto valdrá tu dinero en el futuro con la inflación y cuánto necesitarás para mantener tu poder de compra.",
      "Calculadora de inflación y poder adquisitivo", "Mira cuánto poder de compra pierde tu dinero parado y cuánto necesitarás en el futuro para comprar lo mismo.",
      [field("inf-cant", "Cantidad (€)", 10000), field("inf-inf", "Inflación media anual (%)", 3), field("inf-anos", "Años", 10, mode="numeric", step="1")],
      """<h2>Por qué la inflación importa</h2><p>Con un 3 % anual, 10.000 € guardados en un cajón durante 10 años solo comprarán lo que hoy cuestan unos 7.441 €. Para mantener el poder adquisitivo tu dinero tiene que rendir, al menos, lo mismo que la inflación.</p>
<h3>Fórmula</h3><p>Valor futuro necesario = cantidad × (1 + inflación)<sup>años</sup>. Poder de compra futuro = cantidad ÷ (1 + inflación)<sup>años</sup>.</p>""",
      [("¿Qué inflación uso?", "Para planificar a largo plazo es habitual usar entre el 2 % y el 3 %. Para el pasado, consulta el IPC oficial de tu país.")],
      aff=("cuenta", "Que tu dinero no pierda valor", " Compara cuentas remuneradas y depósitos.", "Ver opciones"))

    tool("dep", "calculadora-depositos", "Depósitos",
      "Calculadora de depósitos a plazo fijo: intereses netos",
      "Calcula los intereses brutos y netos de un depósito o cuenta remunerada según la TAE, el plazo y la retención fiscal.",
      "Calculadora de depósitos a plazo fijo", "Calcula cuánto te pagará un depósito o una cuenta remunerada, después de retenciones.",
      [field("dep-cap", "Capital (€)", 20000), field("dep-tae", "TAE (%)", 2.5), field("dep-meses", "Plazo (meses)", 12, mode="numeric", step="1"),
       field("dep-ret", "Retención fiscal (%)", 19, "en España, 19 % a cuenta")],
      """<h2>Cómo se calculan los intereses</h2><p>Intereses brutos = capital × ((1 + TAE)<sup>meses/12</sup> − 1). Sobre ellos el banco aplica una retención a cuenta de impuestos; en España es habitualmente del 19 %, y después se regulariza en la declaración de la renta.</p>
<h3>TAE frente a TIN</h3><p>Compara siempre por TAE, que incluye la frecuencia de pago de intereses. Fíjate también en el importe máximo remunerado y si la oferta es solo para clientes nuevos.</p>
<p class="disclaimer">La fiscalidad depende de tu país y situación; el porcentaje de retención es editable.</p>""",
      [("¿Están garantizados los depósitos?", "En la UE, los depósitos están cubiertos por los fondos de garantía nacionales hasta 100.000 € por titular y entidad."),
       ("¿Qué es mejor, depósito o cuenta remunerada?", "El depósito suele fijar el tipo durante el plazo; la cuenta remunerada da liquidez pero su tipo puede cambiar.")],
      aff=("cuenta", "Compara depósitos y cuentas remuneradas", " Busca la mejor TAE sin comisiones.", "Ver ofertas"))

    tool("amort", "calculadora-amortizacion-anticipada", "Amortización anticipada",
      "Calculadora de amortización anticipada: ¿reducir cuota o plazo?",
      "Calcula cuánto ahorras amortizando tu hipoteca o préstamo y compara reducir la cuota con reducir el plazo.",
      "Amortización anticipada: ¿reducir cuota o plazo?", "Introduce lo que te queda por pagar y cuánto quieres adelantar para ver qué opción te ahorra más intereses.",
      [field("amort-pend", "Capital pendiente (€)", 150000), field("amort-tin", "Tipo de interés (%)", 3), field("amort-anos", "Años restantes", 20, step="0.5"),
       field("amort-amo", "Cantidad a amortizar (€)", 10000)],
      note="Cálculo aproximado con cuota constante (sistema francés). No incluye comisiones por amortización.",
      article="""<h2>Reducir cuota o reducir plazo</h2><p>Si reduces el <strong>plazo</strong>, mantienes la cuota y terminas antes: es la opción que más intereses ahorra. Si reduces la <strong>cuota</strong>, pagas menos cada mes y ganas margen en tu presupuesto, pero ahorras menos intereses.</p>
<h3>¿Amortizar o invertir?</h3><p>Compara el tipo de interés de tu préstamo con la rentabilidad que podrías obtener, después de impuestos y con su riesgo. Antes de amortizar, asegúrate de tener un fondo de emergencia.</p>""",
      faqs=[("¿Hay comisión por amortizar?", "Depende del contrato y del tipo de préstamo; la normativa suele limitarla. Revisa tu escritura o contrato.")],
      aff=("hipoteca", "¿Y si mejoras tu hipoteca?", " Una subrogación puede bajar tu tipo de interés.", "Comparar hipotecas"))

    tool("tarjeta", "calculadora-deuda-tarjeta-credito", "Deuda de tarjeta",
      "Calculadora de deuda de tarjeta de crédito: cuándo terminarás de pagar",
      "Calcula cuántos meses tardarás en pagar la deuda de tu tarjeta de crédito o revolving y cuántos intereses pagarás.",
      "¿Cuánto tardo en pagar mi tarjeta de crédito?", "Las tarjetas revolving pueden convertir una compra pequeña en años de pagos. Calcula tu caso.",
      [field("tarjeta-deuda", "Deuda actual (€)", 3000), field("tarjeta-tae", "TAE (%)", 21), field("tarjeta-pago", "Pago mensual (€)", 100)],
      """<h2>La trampa del pago aplazado</h2><p>Con una cuota baja, la mayor parte de lo que pagas son intereses y la deuda apenas baja. Con 3.000 € al 21 % TAE pagando 100 € al mes tardas unos 3 años y medio y pagas más de 1.000 € de intereses.</p>
<h3>Cómo salir antes</h3><ul><li>Sube la cuota mensual todo lo que puedas.</li><li>Pasa la tarjeta a modo «fin de mes».</li><li>Valora un préstamo personal con TAE más baja para cancelarla.</li></ul>""",
      [("¿Qué es una tarjeta revolving?", "Una tarjeta en la que la deuda se paga a plazos con cuota fija o porcentual y los intereses se suman al capital pendiente.")],
      aff=("prestamo", "Reunifica a un interés más bajo", " Compara préstamos para cancelar deudas caras.", "Comparar préstamos"))

    tool("emerg", "calculadora-fondo-emergencia", "Fondo de emergencia",
      "Calculadora de fondo de emergencia: cuánto necesitas",
      "Calcula el tamaño ideal de tu fondo de emergencia según tus gastos y cuántos meses tardarás en completarlo.",
      "Calculadora de fondo de emergencia", "El primer paso de cualquier plan financiero: el colchón para imprevistos.",
      [field("emerg-gasto", "Gastos fijos mensuales (€)", 1400), field("emerg-meses", "Meses de cobertura", 6, mode="numeric", step="1"),
       field("emerg-ahorro", "Ya tengo (€)", 2000), field("emerg-aporte", "Puedo apartar al mes (€)", 250)],
      """<h2>¿Cuántos meses necesito?</h2><p>La recomendación habitual es de 3 a 6 meses de gastos esenciales. Apunta más alto si eres autónomo, tienes ingresos variables, hijos o una sola fuente de ingresos.</p>
<h3>Dónde guardarlo</h3><p>En un lugar seguro y disponible al instante: una cuenta remunerada separada de la del día a día. No en bolsa: el día que lo necesites puede estar en pérdidas.</p>""",
      [("¿Lo invierto?", "No. Su función es estar disponible y no perder valor nominal. La inversión viene después.")],
      aff=("cuenta", "Guarda tu colchón donde rinda", " Cuentas remuneradas sin comisiones y con disponibilidad inmediata.", "Ver cuentas"))

    tool("hora", "calculadora-precio-hora-freelance", "Precio por hora freelance",
      "Calculadora de tarifa freelance: cuánto cobrar por hora",
      "Calcula tu precio mínimo por hora como freelance o autónomo según el sueldo neto que quieres, gastos, impuestos y horas facturables.",
      "¿Cuánto cobrar por hora como freelance?", "Calcula una tarifa que cubra tu sueldo, tus gastos y tus impuestos, teniendo en cuenta que no todas las horas se facturan.",
      [field("hora-neto", "Ingreso neto anual deseado (€)", 30000), field("hora-gastos", "Gastos anuales del negocio (€)", 4000),
       field("hora-imp", "Impuestos y cuotas sobre facturación (%)", 30), field("hora-horas", "Horas facturables por semana", 25),
       field("hora-semanas", "Semanas de trabajo al año", 46, mode="numeric", step="1")],
      """<h2>El error de calcular con 40 horas</h2><p>Un freelance no factura todas las horas que trabaja: hay administración, búsqueda de clientes, formación y vacaciones. Por eso se calcula con horas <strong>facturables</strong>, normalmente entre 20 y 30 por semana.</p>
<h3>Fórmula</h3><p>Precio/hora = (neto deseado + gastos) ÷ (1 − % impuestos) ÷ (horas facturables × semanas).</p>
<p class="disclaimer">El porcentaje de impuestos y cuotas varía mucho según país y régimen. Ajústalo a tu caso o consulta con un asesor.</p>""",
      [("¿Cobro por hora o por proyecto?", "Usa la tarifa horaria para presupuestar proyectos: estima horas × tarifa y añade un margen para imprevistos.")])

    tool("sueldo", "calculadora-sueldo-bruto-mensual", "Sueldo mensual",
      "Calculadora de sueldo: de anual a mensual (12 o 14 pagas) y por hora",
      "Convierte tu sueldo bruto anual a mensual en 12 o 14 pagas, semanal y por hora.",
      "Sueldo bruto anual a mensual y por hora", "Convierte un salario anual en mensual (12 o 14 pagas), semanal y por hora para comparar ofertas.",
      [field("sueldo-anual", "Sueldo bruto anual (€)", 28000), sel("sueldo-pagas", "Número de pagas", [("14", "14 pagas"), ("12", "12 pagas")]),
       field("sueldo-horas", "Horas por semana", 40)],
      """<h2>12 o 14 pagas</h2><p>Con 14 pagas, el sueldo anual se reparte en 12 mensualidades y 2 pagas extra (normalmente en verano y Navidad). El total anual es el mismo; solo cambia cómo se distribuye.</p>
<h3>Para comparar ofertas</h3><p>Compara siempre el bruto anual, no el mensual. Y calcula el precio por hora: una oferta con más sueldo pero más horas puede pagar menos por hora.</p>""",
      [("¿Cuánto cobraré neto?", "Depende de las retenciones de IRPF y cotizaciones sociales de tu país y situación personal; esta calculadora trabaja en bruto.")])
