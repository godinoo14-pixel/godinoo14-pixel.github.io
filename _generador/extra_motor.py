from gen import amz, ext
# --- Afiliación por página ---
SEG = ext("https://www.rastreator.com/seguros-de-coche.aspx", "Comparar seguros de coche")
S['aff'] = {
    "index": SEG + amz("accesorios coche", "Accesorios de coche en Amazon"),
    "etiqueta-dgt": amz("soporte etiqueta dgt parabrisas", "Porta-etiquetas DGT") + SEG,
    "coste-por-km": amz("compresor aire coche portatil", "Compresor para neumáticos") + amz("medidor presion neumaticos", "Medidor de presión"),
    "electrico-vs-gasolina": amz("cargador coche electrico wallbox", "Cargadores Wallbox") + amz("cable carga tipo 2", "Cables tipo 2"),
    "coste-anual-coche": SEG + amz("kit mantenimiento coche", "Kits de mantenimiento"),
    "depreciacion-coche": amz("cera coche", "Productos para cuidar la pintura") + amz("fundas asientos coche", "Fundas de asiento"),
    "coste-viaje-coche": amz("soporte movil coche", "Soporte de móvil") + amz("nevera portatil coche 12v", "Neveras 12 V"),
    "equivalencia-neumaticos": amz("compresor aire coche portatil", "Compresor portátil") + amz("medidor profundidad dibujo neumatico", "Medidor de dibujo"),
    "renting-vs-compra": SEG,
    "cuota-financiacion-coche": SEG + amz("accesorios coche", "Accesorios de coche"),
}
S['tools'] += [("equivalencia-neumaticos", "Equivalencia de neumáticos", "¿Puedo montar otra medida? Diferencia de diámetro y velocímetro.", ""),
               ("renting-vs-compra", "Renting vs compra", "Qué te sale más barato: renting o comprar el coche.", ""),
               ("cuota-financiacion-coche", "Cuota de financiación de un coche", "Cuota mensual, intereses y coste total del préstamo.", "")]

P.append(("equivalencia-neumaticos", "Calculadora de equivalencia de neumáticos | CocheCuentas",
"Compara dos medidas de neumático: diferencia de diámetro, error del velocímetro y si la equivalencia es aceptable (±3 %).",
"""<p class="lead">Compara la medida original con la que quieres montar. Tienes los datos en el flanco: por ejemplo 205/55 R16.</p>
<div class="card"><b>Medida original</b><div class="row"><div><label for="a1">Ancho (mm)</label><input id="a1" inputmode="numeric" value="205"></div><div><label for="b1">Perfil (%)</label><input id="b1" inputmode="numeric" value="55"></div></div><label for="c1">Llanta (pulgadas)</label><input id="c1" inputmode="numeric" value="16">
<b style="display:block;margin-top:16px">Medida nueva</b><div class="row"><div><label for="a2">Ancho (mm)</label><input id="a2" inputmode="numeric" value="225"></div><div><label for="b2">Perfil (%)</label><input id="b2" inputmode="numeric" value="45"></div></div><label for="c2">Llanta (pulgadas)</label><input id="c2" inputmode="numeric" value="17">
<button onclick="calc()">Comparar</button><div class="res" id="r"></div></div>
<p class="note">Orientativo. Para montar una medida distinta a la de la ficha técnica debe estar homologada para tu coche (ficha técnica o certificado del fabricante); si no, puede ser motivo de rechazo en la ITV.</p>
<h2>Cómo se calcula el diámetro</h2><p>Diámetro = llanta × 25,4 + 2 × (ancho × perfil / 100). Un 205/55 R16 mide unos 632 mm. La regla habitual es no superar un 3 % de diferencia con la medida original para no alterar el velocímetro, el ABS ni el control de estabilidad.</p>""",
[("¿Qué significa 205/55 R16?", "205 es el ancho en milímetros, 55 el perfil (altura del flanco en % del ancho) y R16 el diámetro de la llanta en pulgadas."),
 ("¿Puedo poner neumáticos más anchos?", "Solo si la medida figura en la ficha técnica u homologación del vehículo. Además el diámetro total debe ser similar para que el velocímetro marque bien.")],
None,
"""function dm(a,b,c){return c*25.4+2*a*b/100;}
function calc(){const d1=dm(v('a1'),v('b1'),v('c1')),d2=dm(v('a2'),v('b2'),v('c2')),p=(d2-d1)/d1*100,ok=Math.abs(p)<=3;
show('r','Diferencia de diámetro:<b class="big" style="color:'+(ok?'#2f9e44':'#e03131')+'">'+(p>0?'+':'')+nf(p,2)+' %</b>Original: '+nf(d1,0)+' mm · Nueva: '+nf(d2,0)+' mm<br>Cuando el velocímetro marca 100 km/h, vas realmente a <b>'+nf(100*d2/d1,1)+' km/h</b><br>'+(ok?'Dentro del margen habitual del ±3 %.':'Fuera del margen del ±3 %: no recomendable.'));}"""))

P.append(("renting-vs-compra", "Renting o comprar coche: ¿qué sale más barato? Calculadora | CocheCuentas",
"Compara el coste total de un renting con el de comprar un coche al contado: precio, valor de reventa, seguro, mantenimiento e impuestos.",
"""<p class="lead">Compara cuánto te cuesta de verdad cada opción durante el mismo número de años.</p>
<div class="card"><b>Compra</b><div class="row"><div><label for="pc">Precio del coche (€)</label><input id="pc" inputmode="decimal" value="25000"></div>
<div><label for="vr">Valor de reventa al final (%)</label><input id="vr" inputmode="decimal" value="50"></div>
<div><label for="sg">Seguro (€/año)</label><input id="sg" inputmode="decimal" value="500"></div><div><label for="mt">Mantenimiento + neumáticos (€/año)</label><input id="mt" inputmode="decimal" value="500"></div>
<div><label for="im">Impuesto + ITV (€/año)</label><input id="im" inputmode="decimal" value="120"></div><div><label for="n">Años</label><input id="n" inputmode="numeric" value="4"></div></div>
<b style="display:block;margin-top:16px">Renting</b><div class="row"><div><label for="cr">Cuota mensual con IVA (€)</label><input id="cr" inputmode="decimal" value="420"></div><div><label for="en">Entrada / fianza no recuperable (€)</label><input id="en" inputmode="decimal" value="0"></div></div>
<button onclick="calc()">Comparar</button><div class="res" id="r"></div></div>
<h2>Qué incluye normalmente el renting</h2><p>La cuota suele incluir seguro a todo riesgo, mantenimiento, neumáticos, impuesto de circulación y asistencia. A cambio, el coche nunca es tuyo y hay penalización si te pasas de kilómetros o cancelas antes. Comprar sale mejor cuanto más tiempo te quedes el coche; el renting gana si cambias de coche cada pocos años o eres autónomo y puedes deducirlo.</p>""",
[("¿El renting es tirar el dinero?", "No necesariamente: al comprar también pierdes dinero por depreciación. Lo justo es comparar el coste total de ambas opciones en el mismo periodo, como hace esta calculadora."),
 ("¿Qué pasa si me paso de kilómetros en un renting?", "Se paga un importe por cada km extra, normalmente unos céntimos por km. Ajusta bien el kilometraje al contratar.")],
None,
"""function calc(){const n=v('n'),c=v('pc'),rev=c*v('vr')/100,buy=c-rev+(v('sg')+v('mt')+v('im'))*n,ren=v('cr')*12*n+v('en'),d=buy-ren;
show('r',(d>0?'Sale más barato el <b>renting</b>':'Sale más barato <b>comprar</b>')+':<b class="big">'+eur(Math.abs(d))+' de diferencia</b>Coste total compra: '+eur(buy)+' ('+eur(buy/n/12)+'/mes) · Coste total renting: '+eur(ren)+' ('+eur(ren/n/12)+'/mes)');}"""))

P.append(("cuota-financiacion-coche", "Calculadora de financiación de coche: cuota mensual | CocheCuentas",
"Calcula la cuota mensual de la financiación de tu coche, los intereses totales y el coste final según precio, entrada, TIN y plazo.",
"""<p class="lead">Calcula la cuota y lo que pagarás en total al financiar tu coche.</p>
<div class="card"><div class="row"><div><label for="p">Precio del coche (€)</label><input id="p" inputmode="decimal" value="20000"></div>
<div><label for="e">Entrada (€)</label><input id="e" inputmode="decimal" value="4000"></div>
<div><label for="t">TIN anual (%)</label><input id="t" inputmode="decimal" value="8,5"></div><div><label for="m">Plazo (meses)</label><input id="m" inputmode="numeric" value="60"></div>
<div><label for="ca">Comisión de apertura (%)</label><input id="ca" inputmode="decimal" value="3"></div><div><label for="vf">Cuota final / valor futuro (€, opcional)</label><input id="vf" inputmode="decimal" value="0"></div></div>
<button onclick="calc()">Calcular cuota</button><div class="res" id="r"></div></div>
<p class="note">Cálculo con sistema francés (cuota constante). Si es una financiación con cuota final (tipo multiopción), pon el importe de esa última cuota.</p>
<h2>Lo que debes mirar antes de firmar</h2><ul><li><b>TAE</b>, no solo el TIN: incluye comisiones y da el coste real.</li><li>Si el descuento del concesionario está condicionado a financiar, y qué pasa si amortizas antes.</li><li>Seguros vinculados (vida, protección de pagos) que encarecen la cuota.</li><li>Comisión por amortización anticipada.</li></ul>""",
[("¿Es mejor financiar en el concesionario o con el banco?", "Depende. El concesionario suele ofrecer descuentos ligados a financiar con su financiera; compara el coste total (precio + intereses + comisiones) de ambas opciones."),
 ("¿Qué es la cuota final o multiopción?", "Una financiación en la que pagas cuotas bajas y al final eliges entre pagar una última cuota grande, devolver el coche o cambiarlo por otro.")],
None,
"""function calc(){const cap=v('p')-v('e'),i=v('t')/100/12,n=Math.max(1,Math.round(v('m'))),fv=v('vf'),com=cap*v('ca')/100;
const q=i? (cap-fv/Math.pow(1+i,n))*i/(1-Math.pow(1+i,-n)) : (cap-fv)/n,tot=q*n+fv+com;
show('r','Cuota mensual:<b class="big">'+eur(q)+'</b>Importe financiado: '+eur(cap)+' · Comisión: '+eur(com)+'<br>Intereses: <b>'+eur(q*n+fv-cap)+'</b> · Total a pagar (con entrada): <b>'+eur(tot+v('e'))+'</b>');}"""))
