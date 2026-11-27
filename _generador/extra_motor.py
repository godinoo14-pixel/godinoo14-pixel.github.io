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

P.append(("equivalencia-neumaticos", "Equivalencia de neumáticos: calculadora de medidas y velocímetro | CocheCuentas",
"¿Puedo montar otra medida de rueda? Compara dos neumáticos (205/55 R16 y 225/45 R17, o una medida de invierno): diferencia de diámetro, error del velocímetro y el margen del ±3 %.",
"""<p class="lead">Compara la medida original con la que quieres montar. Tienes los datos en el flanco: por ejemplo 205/55 R16.</p>
<div class="card"><b>Medida original</b><div class="row"><div><label for="a1">Ancho (mm)</label><input id="a1" inputmode="numeric" value="205"></div><div><label for="b1">Perfil (%)</label><input id="b1" inputmode="numeric" value="55"></div></div><label for="c1">Llanta (pulgadas)</label><input id="c1" inputmode="numeric" value="16">
<b style="display:block;margin-top:16px">Medida nueva</b><div class="row"><div><label for="a2">Ancho (mm)</label><input id="a2" inputmode="numeric" value="225"></div><div><label for="b2">Perfil (%)</label><input id="b2" inputmode="numeric" value="45"></div></div><label for="c2">Llanta (pulgadas)</label><input id="c2" inputmode="numeric" value="17">
<button onclick="calc()">Comparar</button><div class="res" id="r" aria-live="polite"></div></div>
<p class="note">Orientativo. Para montar una medida distinta a la de la ficha técnica debe estar homologada para tu coche (ficha técnica o certificado del fabricante); si no, puede ser motivo de rechazo en la ITV.</p>
<h2>Cómo se calcula el diámetro</h2><p>Diámetro = llanta × 25,4 + 2 × (ancho × perfil / 100). Un 205/55 R16 mide unos 632 mm. La regla habitual es no superar un 3 % de diferencia con la medida original para no alterar el velocímetro, el ABS ni el control de estabilidad.</p>
<table><tr><th>Medida</th><th>Diámetro</th><th>Frente a 205/55 R16</th></tr>
<tr><td>205/55 R16</td><td>632 mm</td><td>—</td></tr><tr><td>215/55 R16</td><td>643 mm</td><td>+1,7 %</td></tr>
<tr><td>225/45 R17</td><td>634 mm</td><td>+0,4 %</td></tr><tr><td>205/60 R16</td><td>652 mm</td><td>+3,2 %</td></tr><tr><td>195/65 R15</td><td>634 mm</td><td>+0,4 %</td></tr></table>
<h2>Neumáticos de invierno, all season y cadenas</h2><p>Si en invierno vas a la montaña o vives en zona de nieve, mira el flanco: los neumáticos marcados con <b>M+S</b> (barro y nieve) o con el símbolo del <b>copo de nieve en la montaña (3PMSF)</b> son neumáticos de invierno o all season. Cuando la DGT activa la señal de <b>«cadenas o neumáticos especiales obligatorios»</b>, estos neumáticos sirven en lugar de las cadenas; con neumáticos de verano tienes que montar cadenas o fundas textiles homologadas.</p>
<p>Un truco habitual es montar en invierno una llanta una pulgada más pequeña con un perfil más alto (por ejemplo, 205/55 R16 en vez de 225/45 R17): el neumático es más barato, agarra mejor en nieve y el diámetro casi no cambia. Compruébalo en la calculadora y asegúrate de que la medida está homologada para tu coche. Antes de un viaje largo, revisa también la presión en frío y que el dibujo tenga al menos 1,6 mm, el mínimo legal (en invierno conviene bastante más).</p>
<p>Si sales de viaje estas fiestas, calcula el <a href="coste-viaje-coche.html">coste del viaje en coche</a>, mira la <a href="distancia-frenado.html">distancia de frenado con lluvia, nieve o hielo</a> y busca las <a href="gasolineras-baratas.html">gasolineras más baratas</a> de tu ruta.</p>""",
[("¿Qué significa 205/55 R16?", "205 es el ancho en milímetros, 55 el perfil (altura del flanco en % del ancho) y R16 el diámetro de la llanta en pulgadas."),
 ("¿Puedo poner neumáticos más anchos?", "Solo si la medida figura en la ficha técnica u homologación del vehículo. Además el diámetro total debe ser similar para que el velocímetro marque bien."),
 ("¿Los neumáticos de invierno sustituyen a las cadenas?", "Sí. Cuando la señal obliga a llevar cadenas o neumáticos especiales, los neumáticos de invierno o all season marcados con M+S o con el símbolo del copo de nieve en la montaña (3PMSF) son válidos en lugar de las cadenas."),
 ("¿Cuál es la profundidad mínima del dibujo de un neumático?", "1,6 mm en las ranuras principales. Por debajo es motivo de multa y de rechazo en la ITV, y en mojado o con nieve se recomienda cambiarlos bastante antes, hacia los 3-4 mm.")],
None,
"""function dm(a,b,c){return c*25.4+2*a*b/100;}
function calc(){const d1=dm(v('a1'),v('b1'),v('c1')),d2=dm(v('a2'),v('b2'),v('c2')),p=(d2-d1)/d1*100,ok=Math.abs(p)<=3;
if(!(d1>0&&d2>0)){show('r','Escribe ancho, perfil y llanta de las dos medidas.');return;}
show('r','Diferencia de diámetro:<b class="big" style="color:'+(ok?'#2f9e44':'#e03131')+'">'+(p>0?'+':'')+nf(p,2)+' %</b>Original: '+nf(d1,0)+' mm · Nueva: '+nf(d2,0)+' mm<br>Cuando el velocímetro marca 100 km/h, vas realmente a <b>'+nf(100*d2/d1,1)+' km/h</b><br>'+(ok?'Dentro del margen habitual del ±3 %.':'Fuera del margen del ±3 %: no recomendable.'));}
document.querySelectorAll('.card input').forEach(x=>x.addEventListener('input',()=>calc()));"""))

P.append(("renting-vs-compra", "Renting o comprar coche: ¿qué sale más barato? Calculadora 2026 | CocheCuentas",
"Renting o compra: compara el coste total de cada opción en los mismos años, con valor de reventa, seguro, mantenimiento, impuestos y, si financias, los intereses. Te decimos cuál sale más barato y por cuánto.",
"""<p class="lead">Compara cuánto te cuesta de verdad cada opción durante el mismo número de años, incluyendo lo que recuperas al vender el coche y los intereses si lo financias.</p>
<div class="card"><b>Compra</b><div class="row"><div><label for="pc">Precio del coche (€)</label><input id="pc" inputmode="decimal" value="25000"></div>
<div><label for="vr">Valor de reventa al final (%)</label><input id="vr" inputmode="decimal" value="50"></div>
<div><label for="sg">Seguro (€/año)</label><input id="sg" inputmode="decimal" value="500"></div><div><label for="mt">Mantenimiento + neumáticos (€/año)</label><input id="mt" inputmode="decimal" value="500"></div>
<div><label for="im">Impuesto + ITV (€/año)</label><input id="im" inputmode="decimal" value="120"></div><div><label for="n">Años</label><input id="n" inputmode="numeric" value="4"></div>
<div><label for="ti">Si lo financias: TIN (%; 0 si pagas al contado)</label><input id="ti" inputmode="decimal" value="0"></div><div><label for="ef">Entrada si financias (€)</label><input id="ef" inputmode="decimal" value="5000"></div></div>
<b style="display:block;margin-top:16px">Renting</b><div class="row"><div><label for="cr">Cuota mensual con IVA (€)</label><input id="cr" inputmode="decimal" value="420"></div><div><label for="en">Entrada / fianza no recuperable (€)</label><input id="en" inputmode="decimal" value="0"></div></div>
<button onclick="calc()">Comparar</button><div class="res" id="r" aria-live="polite"></div></div>
<h2>Cómo se compara</h2><p><b>Coste de comprar</b> = precio − valor de reventa + (seguro + mantenimiento + impuestos) × años + intereses de la financiación. <b>Coste del renting</b> = cuota × 12 × años + entrada. La pérdida de valor del coche (la depreciación) es el gran gasto oculto de comprar: un coche nuevo suele perder entre el 40 y el 50 % en cuatro años.</p>
<p><b>Ejemplo:</b> un coche de 25.000 € que a los 4 años vale la mitad cuesta, comprado al contado, 12.500 € de depreciación más 4.480 € de seguro, mantenimiento e impuestos: <b>16.980 €</b>, unos 354 € al mes. Un renting de 420 € al mes cuesta 20.160 € en esos 4 años: comprar sale 3.180 € más barato. Si financias 20.000 € al 8 % TIN a 4 años, los intereses suman unos 3.440 € y la diferencia prácticamente desaparece.</p>
<h2>Qué incluye normalmente el renting</h2><p>La cuota suele incluir seguro a todo riesgo, mantenimiento, neumáticos, impuesto de circulación y asistencia. A cambio, el coche nunca es tuyo y hay penalización si te pasas de kilómetros o cancelas antes. Comprar sale mejor cuanto más tiempo te quedes el coche; el renting gana si cambias de coche cada pocos años, si vas a financiar a un tipo alto o si eres autónomo y puedes deducir parte de la cuota.</p>
<p>Afina los datos con la <a href="depreciacion-coche.html">calculadora de depreciación</a>, la <a href="cuota-financiacion-coche.html">cuota y TAE de la financiación</a> o el <a href="coste-anual-coche.html">coste anual de mantener un coche</a>, y comprueba <a href="que-coche-me-puedo-permitir.html">qué coche te puedes permitir</a> con tu sueldo.</p>""",
[("¿El renting es tirar el dinero?", "No necesariamente: al comprar también pierdes dinero por depreciación. Lo justo es comparar el coste total de ambas opciones en el mismo periodo, como hace esta calculadora."),
 ("¿Qué pasa si me paso de kilómetros en un renting?", "Se paga un importe por cada km extra, normalmente unos céntimos por km. Ajusta bien el kilometraje al contratar."),
 ("¿Qué es mejor, renting o financiar un coche?", "Depende del tipo de interés y de cuánto tiempo vayas a quedarte el coche. Con un TIN alto y un plazo corto, el renting suele salir parecido o más barato; si te quedas el coche 7 años o más, comprar casi siempre gana porque dejas de pagar cuota y el coche sigue siendo tuyo."),
 ("¿Puedo cancelar un renting antes de tiempo?", "Sí, pero con penalización: suele ser un porcentaje (a menudo el 50 %) de las cuotas que quedan por pagar. Por eso conviene elegir un plazo que vayas a cumplir.")],
None,
"""function calc(){const n=Math.max(1,v('n')),c=v('pc'),rev=c*v('vr')/100,ti=v('ti'),pr=Math.max(0,c-v('ef'));let it=0,cu=0;
if(ti>0&&pr>0){const i=ti/1200,m=n*12;cu=pr*i/(1-Math.pow(1+i,-m));it=cu*m-pr;}
const buy=c-rev+(v('sg')+v('mt')+v('im'))*n+it,ren=v('cr')*12*n+v('en'),d=buy-ren;
show('r',(d>0?'Sale más barato el <b>renting</b>':'Sale más barato <b>comprar</b>')+':<b class="big">'+eur(Math.abs(d))+' de diferencia</b>Coste total compra: '+eur(buy)+' ('+eur(buy/n/12)+'/mes)'+(it>0?' · incluye '+eur(it)+' de intereses (cuota de '+eur(cu)+'/mes)':'')+'<br>Coste total renting: '+eur(ren)+' ('+eur(ren/n/12)+'/mes)<br>Al comprar, el coche pierde '+eur(c-rev)+' de valor en '+nf(n,0)+' años: '+eur((c-rev)/n/12)+' al mes.');}
calc();"""))

P.append(("cuota-financiacion-coche", "Calculadora de financiación de coche: cuota, TAE e intereses | CocheCuentas",
"Calcula la cuota mensual al financiar tu coche y su TAE real con comisión de apertura: intereses, coste total y cuota final de la financiación multiopción. Compara ofertas en segundos.",
"""<p class="lead">Calcula la cuota y lo que pagarás en total al financiar tu coche.</p>
<div class="card"><div class="row"><div><label for="p">Precio del coche (€)</label><input id="p" inputmode="decimal" value="20000"></div>
<div><label for="e">Entrada (€)</label><input id="e" inputmode="decimal" value="4000"></div>
<div><label for="t">TIN anual (%)</label><input id="t" inputmode="decimal" value="8,5"></div><div><label for="m">Plazo (meses)</label><input id="m" inputmode="numeric" value="60"></div>
<div><label for="ca">Comisión de apertura (%)</label><input id="ca" inputmode="decimal" value="3"></div><div><label for="vf">Cuota final / valor futuro (€, opcional)</label><input id="vf" inputmode="decimal" value="0"></div></div>
<button onclick="calc()">Calcular cuota</button><div class="res" id="r"></div></div>
<p class="note">Cálculo con sistema francés (cuota constante). Si es una financiación con cuota final (tipo multiopción), pon el importe de esa última cuota.</p>
<h2>Lo que debes mirar antes de firmar</h2><ul><li><b>TAE</b>, no solo el TIN: incluye comisiones y da el coste real.</li><li>Si el descuento del concesionario está condicionado a financiar, y qué pasa si amortizas antes.</li><li>Seguros vinculados (vida, protección de pagos) que encarecen la cuota.</li><li>Comisión por amortización anticipada.</li></ul>
<h2>Cómo calculamos la TAE</h2><p>Buscamos el interés mensual que iguala lo que realmente recibes (importe financiado menos la comisión de apertura) con todas las cuotas que vas a pagar, y lo convertimos a anual: TAE = (1 + i)<sup>12</sup> − 1. Es la cifra que debes usar para comparar ofertas de bancos y concesionarios, porque incluye la comisión. Si dudas de que la cuota encaje en tu economía, mira <a href="que-coche-me-puedo-permitir.html">qué coche te puedes permitir según tu sueldo</a>.</p>""",
[("¿Es mejor financiar en el concesionario o con el banco?", "Depende. El concesionario suele ofrecer descuentos ligados a financiar con su financiera; compara el coste total (precio + intereses + comisiones) de ambas opciones."),
 ("¿Qué es la cuota final o multiopción?", "Una financiación en la que pagas cuotas bajas y al final eliges entre pagar una última cuota grande, devolver el coche o cambiarlo por otro."),
 ("¿Por qué la TAE es mayor que el TIN?", "El TIN solo refleja el interés. La TAE suma además la comisión de apertura y otros gastos obligatorios y los expresa como interés anual. Con un 8,5 % TIN y un 3 % de comisión a 5 años, la TAE sube por encima del 10 %."),
 ("¿Cuánto coche me puedo permitir con mi sueldo?", "Como referencia, que el coste total del coche (cuota y gastos de uso) no pase del 15-20 % de tus ingresos netos. Calcúlalo con nuestra calculadora de qué coche me puedo permitir.")],
None,
"""function calc(){const cap=v('p')-v('e'),i=v('t')/100/12,n=Math.max(1,Math.round(v('m'))),fv=v('vf'),com=cap*v('ca')/100;
const q=i? (cap-fv/Math.pow(1+i,n))*i/(1-Math.pow(1+i,-n)) : (cap-fv)/n,tot=q*n+fv+com;
const pv=r=>{let x=0;for(let k=1;k<=n;k++)x+=q/Math.pow(1+r,k);return x+fv/Math.pow(1+r,n);};let lo=0,hi=0.1;for(let k=0;k<100;k++){const mi=(lo+hi)/2;pv(mi)>cap-com?lo=mi:hi=mi;}const tae=Math.pow(1+lo,12)-1;
show('r','Cuota mensual:<b class="big">'+eur(q)+'</b>Importe financiado: '+eur(cap)+' · Comisión: '+eur(com)+'<br>TAE aproximada: <b>'+nf(tae*100,2)+' %</b> (TIN '+nf(v('t'),2)+' %)<br>Intereses: <b>'+eur(q*n+fv-cap)+'</b> · Total a pagar (con entrada): <b>'+eur(tot+v('e'))+'</b>');}"""))

# --- Historial por matrícula (datos oficiales de etiqueta + fecha por serie de letras + ITV) ---
INFORME_URL = "https://www.carvertical.com/es"   # cambiar por el enlace de afiliado cuando lo tengas
S['tools'].insert(1, ("historial-coche-matricula", "Historial de un coche por matrícula", "Fecha de matriculación, antigüedad, etiqueta DGT y próxima ITV con solo la matrícula.", "Historial"))
S['aff']["historial-coche-matricula"] = ext(INFORME_URL, "Informe completo con propietarios, km y cargas") + SEG
P.append(("historial-coche-matricula", "Historial de un coche por matrícula gratis: año, etiqueta e ITV | CocheCuentas",
"Escribe la matrícula y consulta gratis la fecha aproximada de matriculación, la antigüedad, la etiqueta DGT oficial y cuándo le toca la ITV a cualquier coche o moto.",
"""<p class="lead">Escribe la matrícula de cualquier coche o moto y te damos al momento lo que se sabe de él. Ideal antes de comprar un coche de segunda mano.</p>
<div class="card"><label for="m">Matrícula</label><input id="m" placeholder="1234 KLM" autocapitalize="characters" autocomplete="off" enterkeyhint="search" onkeydown="if(event.key==='Enter')calc()" style="font-size:1.5rem;letter-spacing:3px;text-transform:uppercase;text-align:center">
<button onclick="calc()">Ver historial</button><p class="note" id="rec" style="margin:10px 0 0"></p><div class="res" id="r"></div></div>
<div class="card" id="inf" style="display:none;border-color:#d9480f"><b style="font-size:1.1rem">¿Quieres ver los propietarios, los kilómetros y si tiene cargas?</b>
<p style="margin:8px 0">El informe completo del vehículo incluye el número de dueños, fechas de cada cambio, kilometraje en las ITV, embargos y si consta como robado. Pídelo antes de pagar un coche usado.</p>
<a class="afl" href=\"""" + INFORME_URL + """\" rel="sponsored nofollow noopener" target="_blank" style="background:#d9480f;color:#fff;border-color:#d9480f">Ver informe completo →</a></div>
<h2>Qué te dice la matrícula de un coche</h2><p>Las matrículas españolas actuales se asignan en orden desde septiembre de 2000, así que sus tres letras indican la fecha aproximada en que el coche se matriculó por primera vez en España. Con esa fecha sabemos su antigüedad y su calendario de ITV. La etiqueta medioambiental sale del registro oficial de la DGT, que actualizamos cada día.</p>
<h2>Calendario de ITV de un turismo particular</h2><table><tr><th>Antigüedad</th><th>Frecuencia</th></tr><tr><td>Menos de 4 años</td><td>Exento</td></tr><tr><td>De 4 a 10 años</td><td>Cada 2 años</td></tr><tr><td>Más de 10 años</td><td>Cada año</td></tr></table>
<p>¿Quieres el calendario completo de tus próximas inspecciones, también para motos y ciclomotores, y saber desde qué día puedes adelantarla sin perder validez? Usa la calculadora de <a href="cuando-pasar-itv.html">cuándo pasar la ITV</a>.</p>
<h2>Qué revisar antes de comprar un coche usado</h2><ul><li>Que la fecha de matriculación cuadre con lo que dice el anuncio.</li><li>Que la ITV esté en vigor y los kilómetros sean coherentes con la antigüedad (unos 15.000 km al año de media).</li><li>Número de propietarios, cargas o embargos: vienen en el informe completo del vehículo.</li><li>La etiqueta medioambiental, si vas a circular por zonas de bajas emisiones.</li></ul>
<p class="note">La fecha es aproximada (margen de pocas semanas) y corresponde a la matriculación en España: un coche importado puede ser más antiguo. La ITV es orientativa; la fecha exacta está en la tarjeta ITV o en la pegatina del parabrisas. Etiqueta: fichero abierto de distintivos ambientales de la DGT.</p>""",
[("¿Cómo saber el año de un coche por la matrícula?", "En las matrículas actuales (1234 BCD) las tres letras avanzan en orden desde el año 2000, así que indican el mes y año aproximados de matriculación. Escríbela arriba y te lo calculamos."),
 ("¿Se pueden ver los propietarios de un coche por la matrícula?", "El número de propietarios, las fechas de cada cambio y si fue particular o empresa vienen en el informe completo del vehículo, que se pide con la matrícula. Aquí tienes el enlace para solicitarlo."),
 ("¿Cada cuánto pasa la ITV un coche?", "Un turismo particular está exento los primeros 4 años, después pasa cada 2 años hasta los 10 y, a partir de ahí, cada año.")],
"Historial de un coche por matrícula",
"""const LET='BCDFGHJKLMNPRSTVWXYZ';
const K=[['BBB',2000+8.5/12],['BDR',2001],['BRT',2002],['CDC',2003],['CRC',2004],['DFF',2005],['DVB',2006],['FKC',2007],['FYY',2008],['GKH',2009],['GSR',2010],['HBG',2011],['HHT',2012],['HNK',2013],['HVF',2014],['JBY',2015],['JKZ',2016],['JVZ',2017],['KGN',2018],['KSS',2019],['LDR',2020],['LMC',2021],['LVV',2022],['MDF',2023],['MMN',2024],['MXP',2025],['NJS',2026],['NRY',2026+8/12]];
const ix=s=>LET.indexOf(s[0])*400+LET.indexOf(s[1])*20+LET.indexOf(s[2]);
function fecha(l){const x=ix(l);for(let i=0;i<K.length-1;i++){const a=ix(K[i][0]),b=ix(K[i+1][0]);if(x>=a&&x<b)return K[i][1]+(K[i+1][1]-K[i][1])*(x-a)/(b-a);}return x>=ix(K[K.length-1][0])?K[K.length-1][1]:null;}
const MES=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'];
const fm=f=>{const y=Math.floor(f);return MES[Math.min(11,Math.floor((f-y)*12))]+' de '+y;};
const E={1:['B','#f59f00'],2:['C','#37b24d'],3:['ECO','#2f9e44'],4:['0 EMISIONES','#1c7ed6'],5:['SIN ETIQUETA','#868e96']};E[6]=E[1];E[7]=E[2];E[8]=E[3];E[9]=E[4];
function itv(f,moto){const now=new Date(),t=now.getFullYear()+now.getMonth()/12,a=t-f;let n;
if(moto){n=a<4?f+4:f+4+2*Math.ceil((a-4)/2);}else if(a<4)n=f+4;else if(a<10){n=f+4+2*Math.ceil((a-4)/2);if(n>f+10)n=f+10;}else{n=f+Math.ceil(a);}
return a<4?'Exento hasta aprox. <b>'+fm(n)+'</b> (primera ITV)':'Próxima aprox. <b>'+fm(n)+'</b>'+(a>=10&&!moto?' (anual)':' (cada 2 años)');}
async function calc(){const raw=document.getElementById('m').value.toUpperCase().replace(/[^A-Z0-9]/g,'');
if(!raw){document.getElementById('r').style.display='none';return;}
show('r','Buscando '+raw+'…');let v=0,m,f=null,prov=false;
try{if(m=raw.match(/^(\\d{4})([B-DF-HJ-NP-TV-Z]{3})$/)){f=fecha(m[2]);const r=await fetch('dgt/m/'+m[2]+'.bin');if(r.ok){const b=new Uint8Array(await r.arrayBuffer());const n=+m[1],x=b[n>>1]||0;v=n&1?x>>4:x&15;}}
else if(m=raw.match(/^([A-Z]{1,2})(\\d{3,})([A-Z]*)$/)){prov=!(m[1]=='C'&&m[3].length==3);const r=await fetch('dgt/o/'+m[1]+m[2].slice(0,2)+'.txt');if(r.ok){const k=m[2].slice(2)+m[3]+':';const l=(await r.text()).split('\\n').find(x=>x.startsWith(k));if(l)v=+l.slice(k.length);}}
else{show('r','Escribe una matrícula válida, por ejemplo <b>1234 KLM</b>.');return;}}
catch(e){show('r','No hemos podido consultar ahora mismo. Inténtalo de nuevo en unos segundos.');return;}
if(!E[v]){show('r','No encontramos la matrícula <b>'+raw+'</b> en el registro de la DGT. Revisa que esté bien escrita.');document.getElementById('inf').style.display='none';return;}
const moto=v>=6,now=new Date(),t=now.getFullYear()+now.getMonth()/12;const a=f!==null?t-f:(prov?27:null);
let h='<div class="ficha"><div class="pegatina" style="background:'+E[v][1]+'">'+(v==5?'SIN<br>ETIQ.':E[v][0].replace(' EMISIONES',''))+'</div><div><div class="placa">'+raw.replace(/^(\\d{4})([A-Z]{3})$/,'$1 $2')+'</div><div class="note">'+(moto?'Moto o ciclomotor':'Coche, furgoneta u otro vehículo')+' · Etiqueta DGT oficial: <b>'+E[v][0]+'</b></div></div></div><table>';
if(f!==null){h+='<tr><td>Matriculado en España</td><td><b>'+fm(f)+'</b> (aprox.)</td></tr><tr><td>Antigüedad</td><td><b>'+(a<1?Math.max(1,Math.round(a*12))+' meses':Math.floor(a)+' años')+'</b></td></tr><tr><td>ITV</td><td>'+itv(f,moto)+'</td></tr>';
 if(!moto&&a>=1){const km=Math.round(a*15000/1000)*1000;h+='<tr><td>Km normales para su edad</td><td>Unos <b>'+km.toLocaleString('es-ES')+' km</b> (media de 15.000 km/año)</td></tr>';}}
else if(prov){h+='<tr><td>Matriculado</td><td><b>Antes de septiembre de 2000</b> (matrícula provincial)</td></tr><tr><td>ITV</td><td>Cada año</td></tr>';}
h+='</table>';
let av=[];if(v==5)av.push('No tiene etiqueta: puede tener prohibida la entrada en zonas de bajas emisiones de muchas ciudades.');
if(a!==null&&a>=10&&!moto)av.push('Tiene más de 10 años: debe pasar la ITV cada año. Pide al vendedor la tarjeta ITV y las facturas de mantenimiento.');
if(f!==null&&a<4)av.push('Coche casi nuevo: puede seguir en garantía del fabricante. Pide el libro de mantenimiento sellado.');
av.push('Antes de pagar, comprueba los propietarios, los kilómetros registrados en las ITV y que no tenga embargos ni conste como robado.');
h+='<div class="avisos"><b>Si vas a comprarlo:</b><ul>'+av.map(x=>'<li>'+x+'</li>').join('')+'</ul></div>';
const txt='La matrícula '+raw+' tiene etiqueta '+E[v][0]+(f!==null?' y es de '+fm(f):'')+'. Consulta la tuya gratis: '+location.href.split('#')[0];
h+='<div class="share" style="margin:12px 0 0"><a href="https://wa.me/?text='+encodeURIComponent(txt)+'" rel="noopener" target="_blank">Compartir por WhatsApp</a><a href="#" onclick="otra();return false">Consultar otra</a></div>';
show('r',h);document.getElementById('inf').style.display='block';guarda(raw);}
function guarda(p){try{let l=JSON.parse(localStorage.getItem('hist')||'[]').filter(x=>x!=p);l.unshift(p);l=l.slice(0,5);localStorage.setItem('hist',JSON.stringify(l));pinta();}catch(e){}}
function pinta(){try{const l=JSON.parse(localStorage.getItem('hist')||'[]');const c=document.getElementById('rec');if(!c)return;c.innerHTML=l.length?'Últimas consultas: '+l.map(p=>'<a href="#" data-p="'+p+'" onclick="usar(this.dataset.p);return false">'+p+'</a>').join(' '):'';}catch(e){}}
function otra(){document.getElementById('m').value='';document.getElementById('r').style.display='none';document.getElementById('inf').style.display='none';document.getElementById('m').focus();}
function usar(p){document.getElementById('m').value=p;calc();}
try{const q=new URLSearchParams(location.search).get('m');if(q)document.getElementById('m').value=q;}catch(e){}
pinta();"""))

# --- Gasolineras más baratas (datos del Ministerio, carb/ lo genera el workflow) ---
S['tools'].insert(2, ("gasolineras-baratas", "Gasolineras más baratas cerca de ti", "Precios de hoy de todas las gasolineras de España, ordenadas por precio y distancia.", "Gasolineras"))
S['aff']["gasolineras-baratas"] = amz("soporte movil coche", "Soporte de móvil para el coche") + amz("compresor aire coche portatil", "Compresor para neumáticos")
P.append(("gasolineras-baratas", "Gasolineras más baratas cerca de mí: precio gasolina y diésel hoy | CocheCuentas",
"Encuentra las gasolineras más baratas cerca de ti con los precios oficiales de hoy de gasolina 95, diésel, gasolina 98 y GLP en toda España. Cuánto ahorras por depósito.",
"""<p class="lead">Precios de hoy de las más de 11.000 gasolineras de España, con datos oficiales del Ministerio. Usa tu ubicación o elige tu provincia.</p>
<div class="card"><div class="row"><div><label for="cb">Combustible</label><select id="cb" onchange="pinta()"><option value="5">Gasolina 95</option><option value="6">Diésel (gasóleo A)</option><option value="7">Gasolina 98</option><option value="8">GLP (autogás)</option></select></div>
<div><label for="pv">Provincia</label><select id="pv" onchange="carga(this.value)"><option>Cargando…</option></select></div></div>
<div class="row"><div><label for="mu">Municipio (opcional)</label><input id="mu" placeholder="Ej.: Málaga" oninput="pinta()"></div><div><label for="km">Distancia máxima</label><select id="km" onchange="pinta()"><option value="5">5 km</option><option value="10" selected>10 km</option><option value="25">25 km</option><option value="1000">Toda la provincia</option></select></div></div>
<button onclick="ubica()">Usar mi ubicación</button><p class="note" id="info" style="margin:10px 0 0"></p><div id="lst" style="margin-top:12px"></div></div>
<h2>Cuánto se ahorra eligiendo bien la gasolinera</h2><p>Entre la gasolinera más cara y la más barata de una misma ciudad puede haber más de 20 céntimos por litro. En un depósito de 50 litros son 10 euros, y en un año, cientos. Las gasolineras automáticas y las de supermercado suelen ser las más baratas; las de autopista, las más caras.</p>
<h2>Trucos para gastar menos combustible</h2><ul><li>Reposta antes de entrar en autopista o autovía.</li><li>Mira el precio el lunes: muchas gasolineras bajan precios a principio de semana.</li><li>Lleva los neumáticos a la presión correcta: un neumático bajo aumenta el consumo.</li><li>Calcula lo que gastas con la <a href="coste-por-km.html">calculadora de coste por kilómetro</a>.</li></ul>
<p class="note">Fuente: Ministerio para la Transición Ecológica y el Reto Demográfico, Geoportal de gasolineras (precios comunicados por las estaciones de servicio). Actualizamos los datos dos veces al día.</p>""",
[("¿Dónde está la gasolinera más barata cerca de mí?", "Pulsa en «Usar mi ubicación» y te mostramos las gasolineras más baratas en el radio que elijas, ordenadas por precio y con la distancia hasta cada una."),
 ("¿De dónde salen los precios?", "Del Geoportal de gasolineras del Ministerio para la Transición Ecológica, donde todas las estaciones de servicio de España están obligadas a comunicar sus precios."),
 ("¿Cuánto ahorro por depósito?", "Junto a cada gasolinera indicamos cuánto te ahorras en un depósito de 50 litros respecto al precio medio de tu provincia.")],
"Gasolineras más baratas cerca de ti",
"""let IDX=null,DAT=[],POS=null,PROV=null;
const NB=['Gasolina 95','Diésel','Gasolina 98','GLP'];
const eu=x=>x.toLocaleString('es-ES',{minimumFractionDigits:3,maximumFractionDigits:3})+' €/l';
function dist(a,b,c,d){const R=6371,r=Math.PI/180,x=(c-a)*r,y=(d-b)*r,h=Math.sin(x/2)**2+Math.cos(a*r)*Math.cos(c*r)*Math.sin(y/2)**2;return 2*R*Math.asin(Math.sqrt(h));}
async function carga(p){PROV=p;document.getElementById('lst').textContent='Cargando gasolineras…';try{const r=await fetch('carb/p'+p+'.json');DAT=await r.json();}catch(e){DAT=[];document.getElementById('lst').textContent='No hemos podido cargar los precios. Inténtalo en unos minutos.';return;}pinta();}
function pinta(){if(!DAT.length)return;const c=+document.getElementById('cb').value,mu=document.getElementById('mu').value.trim().toLowerCase(),km=+document.getElementById('km').value;
let L=DAT.filter(e=>e[c]).map(e=>({e,d:POS?dist(POS[0],POS[1],e[3],e[4]):null}));
if(mu)L=L.filter(x=>x.e[2].toLowerCase().includes(mu));if(POS&&km<1000)L=L.filter(x=>x.d<=km);
const med=L.length?L.reduce((a,x)=>a+x.e[c],0)/L.length:0;L.sort((a,b)=>a.e[c]-b.e[c]||((a.d||0)-(b.d||0)));
document.getElementById('info').innerHTML=L.length?(L.length+' gasolineras · precio medio de '+NB[c-5]+': <b>'+eu(med)+'</b>'+(IDX?' · media en España: '+eu(IDX.medias[['g95','gA','g98','glp'][c-5]]||0)+' · datos del '+IDX.fecha:'')):'No hay gasolineras con ese combustible y filtros. Amplía la distancia o quita el municipio.';
document.getElementById('lst').innerHTML=L.slice(0,25).map((x,i)=>{const e=x.e,ah=(med-e[c])*50;return '<div class="tool" style="margin-bottom:8px"><div style="display:flex;justify-content:space-between;gap:10px"><div><b>'+(i+1)+'. '+e[0]+'</b><p>'+e[1]+', '+e[2]+(x.d!==null?' · <b>'+x.d.toFixed(1).replace('.',',')+' km</b>':'')+'</p><p class="note">'+e[9]+'</p></div><div style="text-align:right;white-space:nowrap"><b style="font-size:1.3rem;color:'+(i<3?'#2f9e44':'#1d2433')+'">'+eu(e[c])+'</b><p class="note">'+(ah>0.5?'Ahorras '+ah.toFixed(2).replace('.',',')+' € por depósito':'')+'</p><a href="https://www.google.com/maps/dir/?api=1&destination='+e[3]+','+e[4]+'" target="_blank" rel="noopener">Cómo llegar</a></div></div></div>';}).join('');}
function ubica(){if(!navigator.geolocation){document.getElementById('info').textContent='Tu navegador no permite usar la ubicación. Elige tu provincia.';return;}
document.getElementById('info').textContent='Buscando tu ubicación…';navigator.geolocation.getCurrentPosition(p=>{POS=[p.coords.latitude,p.coords.longitude];let b=null;IDX.provincias.forEach(v=>{const dd=dist(POS[0],POS[1],v[2],v[3]);if(!b||dd<b[1])b=[v[0],dd];});document.getElementById('pv').value=b[0];carga(b[0]);},()=>{document.getElementById('info').textContent='No hemos podido obtener tu ubicación. Elige tu provincia.';},{timeout:10000});}
fetch('carb/index.json').then(r=>r.json()).then(j=>{IDX=j;const s=document.getElementById('pv');s.innerHTML=j.provincias.map(p=>'<option value="'+p[0]+'"'+(p[0]=='28'?' selected':'')+'>'+p[1]+'</option>').join('');carga(s.value);}).catch(()=>{document.getElementById('lst').textContent='No hemos podido cargar los precios. Inténtalo en unos minutos.';});"""))

# --- Última matrícula (dgt/ultima.json lo genera el workflow a partir del fichero de la DGT) ---
S['tools'].append(("ultima-matricula", "¿Por qué letra van las matrículas?", "Última matrícula asignada en España, ritmo de matriculaciones y cuándo llegará la siguiente letra.", ""))
S['aff']["ultima-matricula"] = amz("portamatriculas coche", "Portamatrículas") + SEG
P.append(("ultima-matricula", "Última matrícula en España: ¿por qué letra van las matrículas hoy? | CocheCuentas",
"Consulta por qué letra van las matrículas en España hoy, la última serie asignada según el registro de la DGT, cuántas matrículas se asignan al mes y cuándo llegará la siguiente letra.",
"""<p class="lead">La serie de letras más reciente que aparece en el registro de vehículos de la DGT, actualizada cada día.</p>
<div class="card" id="um">Cargando…</div>
<h2>Cómo avanzan las matrículas en España</h2><p>Desde septiembre de 2000 las matrículas siguen un orden único para todo el país: cuatro números del 0000 al 9999 y tres letras que empiezan en BBB. Cuando una serie llega al 9999, pasa a la siguiente combinación de letras. No se usan vocales ni las letras Ñ y Q, para evitar confusiones y palabras malsonantes.</p>
<h2>¿De qué año es un coche por su matrícula?</h2><p>Como el orden es correlativo, las letras indican la fecha aproximada de matriculación. Consulta cualquier matrícula en nuestra herramienta de <a href="historial-coche-matricula.html">historial de un coche por matrícula</a> y te diremos su año, su etiqueta y su próxima ITV.</p>
<p class="note">Fuente: fichero abierto de distintivos ambientales del parque de vehículos de la DGT. Mostramos la serie más alta con vehículos registrados en el último fichero publicado; puede ir uno o dos días por detrás de la última placa entregada.</p>""",
[("¿Por qué letra van las matrículas?", "Arriba tienes la última serie registrada en el fichero oficial de la DGT, que actualizamos cada día."),
 ("¿Cuándo llegará la letra P a las matrículas?", "Lo estimamos arriba según el ritmo de matriculaciones del último año. Depende de cuántos coches se vendan, así que la fecha puede adelantarse o retrasarse unos meses."),
 ("¿Qué letras no se usan en las matrículas?", "No se usan las vocales (A, E, I, O, U) ni las letras Ñ y Q.")],
"¿Por qué letra van las matrículas?",
"""const LET='BCDFGHJKLMNPRSTVWXYZ';const ix=s=>LET.indexOf(s[0])*400+LET.indexOf(s[1])*20+LET.indexOf(s[2]);const sx=i=>LET[Math.floor(i/400)]+LET[Math.floor(i/20)%20]+LET[i%20];
const Y=[['BBB',2000],['BDR',2001],['BRT',2002],['CDC',2003],['CRC',2004],['DFF',2005],['DVB',2006],['FKC',2007],['FYY',2008],['GKH',2009],['GSR',2010],['HBG',2011],['HHT',2012],['HNK',2013],['HVF',2014],['JBY',2015],['JKZ',2016],['JVZ',2017],['KGN',2018],['KSS',2019],['LDR',2020],['LMC',2021],['LVV',2022],['MDF',2023],['MMN',2024],['MXP',2025],['NJS',2026]];
fetch('dgt/ultima.json',{cache:'no-store'}).then(r=>r.json()).then(u=>{const cur=ix(u.serie),pm=(ix('NJS')-ix('MXP'))/12;const nl=LET[LET.indexOf(u.serie[0])+1];const nxt=nl+'BB';const meses=(ix(nxt)-cur)/pm;const f=new Date();f.setMonth(f.getMonth()+Math.round(meses));
document.getElementById('um').innerHTML='<p>Última matrícula registrada en la DGT</p><div class="placa" style="font-size:2rem">'+(u.numero!==null?String(u.numero).padStart(4,'0')+' ':'')+u.serie+'</div><p class="note">Dato del fichero de la DGT del '+u.fecha+'</p>'+
'<table><tr><td>Matrículas al mes (último año)</td><td><b>unas '+Math.round(pm*10000).toLocaleString('es-ES')+'</b> ('+pm.toFixed(1).replace('.',',')+' series de letras)</td></tr><tr><td>Llegada de la letra '+nl+' ('+nxt+')</td><td><b>'+f.toLocaleDateString('es-ES',{month:'long',year:'numeric'})+'</b> (estimación)</td></tr></table>'+
'<h3>Primera serie de cada año</h3><table><tr><th>Año</th><th>Letras</th></tr>'+Y.slice().reverse().map(y=>'<tr><td>'+y[1]+'</td><td>'+y[0]+'</td></tr>').join('')+'</table>';}).catch(()=>{document.getElementById('um').textContent='No hemos podido cargar el dato. Inténtalo en unos minutos.';});"""))

# --- Impuesto de matriculación (IEDMT) ---
S['tools'].insert(5, ("impuesto-matriculacion", "Impuesto de matriculación", "Cuánto pagarás al matricular un coche nuevo o importado según su CO2 y tu comunidad.", ""))
S['aff']["impuesto-matriculacion"] = SEG + amz("portamatriculas coche", "Portamatrículas")
P.append(("impuesto-matriculacion", "Impuesto de matriculación 2026: calculadora por CO2 y comunidad | CocheCuentas",
"Calcula el impuesto de matriculación de tu coche nuevo o importado: tramos de CO2 WLTP, tipos de cada comunidad, Canarias, familia numerosa y coches usados de importación.",
"""<p class="lead">Mete el precio, las emisiones de CO2 y tu comunidad, y te decimos qué tramo te toca y cuánto pagarás en el modelo 576.</p>
<div class="card"><label for="t">¿Qué vas a matricular?</label><select id="t" onchange="modo();calc()"><option value="n">Coche nuevo comprado en España</option><option value="u">Coche usado importado (valor de tablas de Hacienda)</option></select>
<div class="row"><div id="bn"><label for="pr">Precio sin IVA (€)</label><input id="pr" inputmode="decimal" value="28000"></div>
<div id="bu1" style="display:none"><label for="vt">Valor de tablas del modelo nuevo (€)</label><input id="vt" inputmode="decimal" value="35000"></div>
<div id="bu2" style="display:none"><label for="an">Antigüedad (años desde la 1.ª matriculación)</label><input id="an" inputmode="decimal" value="4"></div>
<div><label for="co">Emisiones CO2 WLTP (g/km)</label><input id="co" inputmode="numeric" value="135"></div>
<div><label for="ca">Comunidad donde lo matriculas</label><select id="ca">
<option value="g">Aragón, Castilla y León, Castilla-La Mancha, Extremadura, Galicia, Madrid, La Rioja</option>
<option value="16.9">Andalucía</option>
<option value="16">Asturias, Baleares, Cataluña o Comunidad Valenciana</option><option value="15.9">Región de Murcia</option><option value="15">Cantabria</option>
<option value="c">Canarias</option><option value="0">Ceuta o Melilla</option></select></div>
<div><label class="chk" style="margin-top:34px"><input type="checkbox" id="fn"><span>Familia numerosa (5 a 9 plazas)</span></label></div></div>
<button onclick="calc()">Calcular impuesto</button><div class="res" id="r"></div></div>
<p class="note">El CO2 WLTP viene en la ficha técnica (casilla V.7) o en la ficha del modelo del concesionario. Los eléctricos puros y los coches de hasta 120 g/km pagan 0 €. Navarra y País Vasco tienen su propia Hacienda foral: confirma allí los tipos.</p>
<h2>Tramos y tipos en 2026</h2><table><tr><th>CO2 WLTP</th><th>Península y Baleares</th><th>Canarias</th></tr>
<tr><td>Hasta 120 g/km</td><td>0 %</td><td>0 %</td></tr><tr><td>Más de 120 y menos de 160</td><td>4,75 %</td><td>3,75 %</td></tr>
<tr><td>De 160 a menos de 200</td><td>9,75 %</td><td>8,75 %</td></tr><tr><td>200 g/km o más</td><td>14,75 %*</td><td>13,75 %</td></tr></table>
<p class="note">* En el último tramo, Andalucía aplica el 16,9 %; Asturias, Baleares, Cataluña y la Comunitat Valenciana aplican el 16 %, Murcia el 15,9 % y Cantabria el 15 %. En Ceuta y Melilla el tipo es 0 %. Fuente: artículo 70 de la Ley 38/1992 de Impuestos Especiales y leyes autonómicas de tributos cedidos.</p>
<h2>Cómo se calcula</h2><p>Impuesto = base imponible × tipo del tramo. En un <b>coche nuevo</b>, la base es el precio de venta sin IVA (incluidos extras y transporte, descontados los descuentos que aparezcan en factura). En un <b>coche usado importado</b> se paga sobre su valor de mercado: Hacienda toma el precio medio del modelo nuevo (Orden de precios medios de venta) y le aplica un porcentaje según los años: 100 % el primer año, 84 % hasta 2, 67 % hasta 3, 56 % hasta 4, 47 % hasta 5, 39 % hasta 6, 34 % hasta 7, 28 % hasta 8, 24 % hasta 9, 19 % hasta 10, 17 % hasta 11, 13 % hasta 12 y 10 % a partir de 12 años.</p>
<p><b>Ejemplo:</b> un SUV de gasolina de 28.000 € sin IVA y 135 g/km cae en el tramo del 4,75 %: paga 1.330 € de impuesto de matriculación. Si emitiera 118 g/km pagaría 0 €; por eso, al elegir versión, unos pocos gramos de CO2 pueden ahorrarte más de mil euros.</p>
<h2>Quién no paga o paga menos</h2><ul><li>Coches de hasta 120 g/km y eléctricos: 0 %.</li><li>Familias numerosas: base reducida al 50 % en vehículos de 5 a 9 plazas (con reconocimiento previo de Hacienda, modelo 05).</li><li>Personas con discapacidad, taxis, autoescuelas y empresas de alquiler: exentos con reconocimiento previo.</li><li>Traslado de residencia desde el extranjero: exento si cumples los requisitos de residencia y uso previo.</li><li>Coches de segunda mano ya matriculados en España: no pagan este impuesto, pagan el de transmisiones (ITP) al cambiar de dueño.</li></ul>
<p class="note">Se declara con el <a href="https://sede.agenciatributaria.gob.es/Sede/procedimientoini/GE03.shtml" rel="noopener" target="_blank">modelo 576 de la Agencia Tributaria</a> antes de matricular en la DGT. En un coche nuevo normalmente lo gestiona el concesionario y va incluido en el precio final.</p>""",
[("¿Cuánto es el impuesto de matriculación de un coche?", "Depende de sus emisiones de CO2 WLTP: 0 % hasta 120 g/km, 4,75 % por encima de 120 y por debajo de 160, 9,75 % de 160 a 199 y 14,75 % desde 200 g/km (entre el 15 % y el 16,9 % en Andalucía, Asturias, Baleares, Cantabria, Cataluña, Murcia y Comunitat Valenciana), aplicado sobre el precio sin IVA."),
 ("¿Los coches eléctricos pagan impuesto de matriculación?", "No. Los eléctricos puros y, en general, cualquier coche con 120 g/km de CO2 o menos tributan al 0 %."),
 ("¿Un coche de segunda mano paga impuesto de matriculación?", "Solo si viene del extranjero y se matricula por primera vez en España. Si ya tenía matrícula española, al comprarlo pagas el impuesto de transmisiones patrimoniales (ITP), no el de matriculación."),
 ("¿Cómo se calcula el impuesto de matriculación de un coche importado?", "Sobre el valor de mercado que fija Hacienda: el precio medio del modelo nuevo multiplicado por el porcentaje de su antigüedad (por ejemplo, 47 % con 4 a 5 años), y a ese valor se le aplica el tipo de su tramo de CO2.")],
"Calculadora del impuesto de matriculación",
"""const DEP=[100,84,67,56,47,39,34,28,24,19,17,13,10];
function modo(){const u=document.getElementById('t').value=='u';document.getElementById('bn').style.display=u?'none':'';document.getElementById('bu1').style.display=u?'':'none';document.getElementById('bu2').style.display=u?'':'none';}
function calc(){const u=document.getElementById('t').value=='u',co=v('co'),ca=document.getElementById('ca').value;
let base,txt='';if(u){const a=v('an'),i=a<=1?0:Math.min(12,Math.ceil(a)-1),p=DEP[i];base=v('vt')*p/100;txt='Valor fiscal: '+eur(v('vt'))+' × '+p+' % = <b>'+eur(base)+'</b><br>';}else base=v('pr');
if(document.getElementById('fn').checked){base/=2;txt+='Base reducida al 50 % por familia numerosa.<br>';}
const b=co<=120?0:co<160?1:co<200?2:3;let T=[0,4.75,9.75,14.75];if(ca=='c')T=[0,3.75,8.75,13.75];else if(ca=='0')T=[0,0,0,0];else if(ca!='g')T=[0,4.75,9.75,parseFloat(ca)];
const t=T[b],imp=base*t/100,TR=['hasta 120 g/km','de 121 a 159 g/km','de 160 a 199 g/km','200 g/km o más'];
let sig='';if(b>0&&ca!='0'){const lim=[0,120,159,199][b];sig='<br>Con '+lim+' g/km bajarías al tramo del '+nf(T[b-1])+' %: pagarías '+eur(base*T[b-1]/100)+' ('+eur(imp-base*T[b-1]/100)+' menos).';}
show('r','Impuesto de matriculación:<b class="big">'+eur(imp)+'</b>'+txt+'Tramo: <b>'+TR[b]+'</b> → tipo del <b>'+nf(t)+' %</b> sobre '+eur(base)+sig);}"""))

# --- Multa por exceso de velocidad (Anexo IV RDL 6/2015 + márgenes Orden ICT/155/2020) ---
S['tools'].insert(6, ("multa-exceso-velocidad", "Multa por exceso de velocidad", "Cuánto te multan y cuántos puntos pierdes, con el margen del radar ya descontado.", ""))
S['aff']["multa-exceso-velocidad"] = amz("navegador gps coche avisador radares", "Navegadores GPS con aviso de límites") + amz("camara coche dashcam", "Cámaras para coche (dashcam)")
P.append(("multa-exceso-velocidad", "Multa por exceso de velocidad: calculadora con margen del radar 2026 | CocheCuentas",
"Calcula la multa y los puntos por exceso de velocidad según la tabla de la DGT: descuenta el margen de error del radar fijo o móvil y te dice si es grave, muy grave o delito.",
"""<p class="lead">Pon el límite de la vía y la velocidad que marcó el radar. Descontamos el margen de error legal y te decimos la multa, los puntos y lo que pagarías con pronto pago.</p>
<div class="card"><div class="row"><div><label for="l">Límite de la vía (km/h)</label><select id="l"><option>20</option><option>30</option><option>40</option><option selected>50</option><option>60</option><option>70</option><option>80</option><option>90</option><option>100</option><option>110</option><option>120</option></select></div>
<div><label for="vm">Velocidad captada por el radar (km/h)</label><input id="vm" inputmode="numeric" value="78"></div></div>
<label for="rt">Tipo de radar</label><select id="rt"><option value="5">Fijo o de tramo (margen 5 km/h o 5 %)</option><option value="7" selected>Móvil: coche, trípode, helicóptero o dron (7 km/h o 7 %)</option><option value="0">Sin margen (velocidad ya corregida en la multa)</option></select>
<label for="vu">Tipo de vía</label><select id="vu"><option value="u">Urbana (dentro de poblado)</option><option value="i">Interurbana (carretera, autovía, autopista)</option></select>
<button onclick="calc()">Calcular multa</button><div class="res" id="r"></div></div>
<p class="note">En la notificación de la multa aparecen la velocidad medida y la «velocidad corregida» tras aplicar el margen: es esta última la que cuenta. Si ya la tienes, elige «Sin margen».</p>
<h2>Tabla de multas por velocidad de la DGT</h2>
<table><tr><th>Exceso sobre el límite</th><th>Vías de 20 a 50 km/h</th><th>Vías de 60 a 120 km/h</th><th>Multa</th><th>Puntos</th></tr>
<tr><td>Grave</td><td>hasta +20</td><td>hasta +30</td><td>100 €</td><td>0</td></tr>
<tr><td>Grave</td><td>+21 a +30</td><td>+31 a +50</td><td>300 €</td><td>2</td></tr>
<tr><td>Grave</td><td>+31 a +40</td><td>+51 a +60</td><td>400 €</td><td>4</td></tr>
<tr><td>Grave</td><td>+41 a +50</td><td>+61 a +70</td><td>500 €</td><td>6</td></tr>
<tr><td>Muy grave</td><td>más de +50</td><td>más de +70</td><td>600 €</td><td>6</td></tr></table>
<p class="note">Fuente: anexo IV del <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722" rel="noopener" target="_blank">texto refundido de la Ley de Tráfico (RDL 6/2015)</a>. Superar el límite en más de 60 km/h en vía urbana o en más de 80 km/h en interurbana es delito (artículo 379 del Código Penal).</p>
<h2>El margen de error de los radares</h2><p>Los cinemómetros tienen un margen de error legal (Orden ICT/155/2020) que se resta a la velocidad medida antes de aplicar la tabla. Para los radares en servicio con verificación periódica es de <b>5 km/h en los fijos y de tramo, y 7 km/h en los móviles, hasta 100 km/h</b>; por encima de 100 km/h se aplica un <b>5 % y un 7 %</b> respectivamente. La velocidad corregida se redondea a la baja.</p>
<p><b>Ejemplo:</b> un radar móvil capta 78 km/h en una calle de 50. Margen: 7 km/h, velocidad corregida 71 km/h, es decir, 21 km/h de exceso. Eso son <b>300 € y 2 puntos</b>, o 150 € si pagas en los 20 días naturales siguientes a la notificación. Si el radar fuera fijo, la velocidad corregida sería 73 km/h y la multa la misma; a 76 km/h medidos con radar móvil (69 corregidos) solo serían 100 € y ningún punto.</p>
<h2>Pronto pago y recursos</h2><p>Pagando en los <b>20 días naturales</b> desde la notificación la multa se reduce a la mitad, pero renuncias a presentar alegaciones y los puntos se pierden igual. Si crees que hay un error (matrícula, señalización o velocidad), puedes alegar en ese mismo plazo en la <a href="https://sede.dgt.gob.es/es/multas/" rel="noopener" target="_blank">sede electrónica de la DGT</a>.</p>
<p>¿La multa viene de un radar de tramo? Ahí cuenta tu velocidad media entre los dos arcos: calcúlala con la <a href="radar-de-tramo.html">calculadora de radar de tramo</a>.</p>
<p>¿Te preocupa lo que gastas en carretera? Mira cuánto ahorras bajando de 120 a 110 con la calculadora de <a href="coste-por-km.html">coste por kilómetro</a> o calcula el <a href="coste-viaje-coche.html">coste de tu viaje</a>.</p>""",
[("¿Cuánto es la multa por ir a 140 en una autovía de 120?", "Con radar fijo se descuenta un 5 % (7 km/h) y queda en 133 km/h; con radar móvil un 7 % (9,8 km/h) y queda en 130. Son 13 o 10 km/h de exceso: 100 € (50 € con pronto pago) y sin pérdida de puntos."),
 ("¿A partir de cuántos km/h te quitan puntos?", "En vías de 60 km/h o más, a partir de 31 km/h por encima del límite (ya descontado el margen del radar). En vías de 50 km/h o menos, a partir de 21 km/h por encima."),
 ("¿Cuál es el margen de error de los radares?", "Para radares en servicio, 5 km/h los fijos y de tramo y 7 km/h los móviles hasta 100 km/h; por encima de 100 km/h, el 5 % y el 7 %. Los radares nuevos en fase de pruebas tienen márgenes menores (3 km/h o 3 % y 5 km/h o 5 %)."),
 ("¿Cuándo es delito el exceso de velocidad?", "Cuando superas el límite en más de 60 km/h en vía urbana o en más de 80 km/h en vía interurbana. Puede castigarse con prisión de 3 a 6 meses o multa, trabajos en beneficio de la comunidad y la retirada del carné de 1 a 4 años.")],
"Calculadora de multas por exceso de velocidad",
"""function calc(){const L=+document.getElementById('l').value,m=v('vm'),mg=+document.getElementById('rt').value,urb=document.getElementById('vu').value=='u';
const marg=mg==0?0:(m>100?m*mg/100:mg),c=Math.floor(m-marg+1e-9),ex=c-L;
if(ex<=0){show('r','Velocidad corregida: <b class="big">'+c+' km/h</b>No superas el límite de '+L+' km/h una vez descontado el margen de '+nf(marg,1)+' km/h: <b>no hay multa</b>.');return;}
const B=L<=50?[20,30,40,50]:[30,50,60,70],F=[[100,0],[300,2],[400,4],[500,6],[600,6]];let i=0;while(i<4&&ex>B[i])i++;
const f=F[i],del=ex>(urb?60:80),vc='Velocidad corregida: <b>'+c+' km/h</b> (margen de '+nf(marg,1)+' km/h) → <b>'+ex+' km/h</b> por encima del límite de '+L+'.';
if(del){show('r','Resultado:<b class="big">Delito contra la seguridad vial</b>'+vc+'<br>Superar el límite en más de '+(urb?60:80)+' km/h en vía '+(urb?'urbana':'interurbana')+' no se sanciona con multa de tráfico sino por la vía penal (art. 379 del Código Penal): prisión de 3 a 6 meses o multa de 6 a 12 meses o trabajos en beneficio de la comunidad, y siempre retirada del carné de 1 a 4 años. No hay pronto pago.');return;}
let h='Multa:<b class="big">'+eur(f[0])+(f[1]?' y '+f[1]+' puntos':' sin puntos')+'</b>'+vc+'<br>Infracción <b>'+(i==4?'muy grave':'grave')+'</b>. Con pronto pago: <b>'+eur(f[0]/2)+'</b>'+(f[1]?' (los puntos se pierden igual)':'')+'.';
if(i<4){const sig=L+B[i]+1,med=mg==0?sig:Math.ceil(sig>100?sig/(1-mg/100):sig+mg);h+='<br>El siguiente tramo ('+eur(F[i+1][0])+') empieza en '+sig+' km/h corregidos'+(mg?', unos '+med+' km/h medidos':'')+'.';}
if(i==4)h+='<br>A partir de '+(L+(urb?61:81))+' km/h corregidos sería delito (art. 379 del Código Penal).';
show('r',h);}"""))

# --- Impuesto de circulación (IVTM, art. 95 RDL 2/2004) y caballos fiscales (anexo V RD 2822/1998) ---
S['tools'].insert(6, ("impuesto-circulacion", "Impuesto de circulación y caballos fiscales", "Calcula los CV fiscales de tu coche y cuánto pagarás de IVTM según tu ayuntamiento.", ""))
S['aff']["impuesto-circulacion"] = SEG + amz("soporte etiqueta dgt parabrisas", "Porta-etiquetas DGT")
P.append(("impuesto-circulacion", "Impuesto de circulación: calculadora con caballos fiscales (IVTM) | CocheCuentas",
"Calcula los caballos fiscales de tu coche a partir de la cilindrada o los kW y cuánto pagarás de impuesto de circulación (IVTM): cuota legal mínima y máxima, coeficiente de tu ayuntamiento y bonificaciones.",
"""<p class="lead">Con la cilindrada y el número de cilindros (o los kW si es eléctrico) calculamos los caballos fiscales con la fórmula oficial y lo que pagarás de impuesto de circulación según el coeficiente de tu ayuntamiento.</p>
<div class="card"><label for="mo">Tipo de motor</label><select id="mo" onchange="modo();calc()"><option value="4">Gasolina o diésel (4 tiempos)</option><option value="2">Motor de 2 tiempos</option><option value="e">Eléctrico</option><option value="c">Ya sé los caballos fiscales</option></select>
<div class="row" id="rc"><div><label for="cc">Cilindrada (cm³)</label><input id="cc" inputmode="numeric" value="1498"></div><div><label for="ci">Número de cilindros</label><input id="ci" inputmode="numeric" value="4"></div></div>
<div id="re" style="display:none"><label for="kw">Potencia efectiva (kW)</label><input id="kw" inputmode="decimal" value="70"><p class="note">Es la potencia máxima sostenida (30 minutos) que figura en la ficha técnica, no la potencia de pico que anuncia la marca.</p></div>
<div id="rf" style="display:none"><label for="cf">Caballos fiscales (CVF)</label><input id="cf" inputmode="decimal" value="11,5"><p class="note">Aparecen en la ficha técnica del vehículo (tarjeta ITV) como potencia fiscal.</p></div>
<div class="row"><div><label for="co">Coeficiente de tu ayuntamiento (1 a 2)</label><input id="co" inputmode="decimal" value="2"></div>
<div><label for="bo">Bonificación de tu ayuntamiento</label><select id="bo"><option value="0">Ninguna</option><option value="50">50 %</option><option value="75">75 % (habitual en eléctricos)</option><option value="100">100 % (históricos)</option></select></div></div>
<button onclick="calc()">Calcular impuesto</button><div class="res" id="r" aria-live="polite"></div></div>
<p class="note">El coeficiente lo fija cada ayuntamiento en su ordenanza fiscal del impuesto sobre vehículos de tracción mecánica: la ley permite entre 1 (cuota mínima) y 2 (el doble). Si en tu ordenanza aparece directamente la tabla en euros, elige la fila de tus caballos fiscales.</p>
<h2>Tarifas mínimas del impuesto de circulación (turismos)</h2>
<table><tr><th>Caballos fiscales</th><th>Cuota mínima (coef. 1)</th><th>Cuota máxima (coef. 2)</th></tr>
<tr><td>Menos de 8</td><td>12,62 €</td><td>25,24 €</td></tr><tr><td>De 8 a 11,99</td><td>34,08 €</td><td>68,16 €</td></tr>
<tr><td>De 12 a 15,99</td><td>71,94 €</td><td>143,88 €</td></tr><tr><td>De 16 a 19,99</td><td>89,61 €</td><td>179,22 €</td></tr><tr><td>20 o más</td><td>112,00 €</td><td>224,00 €</td></tr></table>
<p class="note">Fuente: artículo 95 del <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2004-4214" rel="noopener" target="_blank">texto refundido de la Ley de Haciendas Locales (RDL 2/2004)</a>. Las ordenanzas pueden bonificar hasta el 75 % según el carburante o el motor y hasta el 100 % a los vehículos con 25 años o más.</p>
<h2>Cómo se calculan los caballos fiscales</h2><p>La fórmula oficial está en el anexo V del <a href="https://www.boe.es/buscar/act.php?id=BOE-A-1999-1826" rel="noopener" target="_blank">Reglamento General de Vehículos</a>. Para motores de 4 tiempos: <b>CVF = 0,08 × (0,785 × D² × R)<sup>0,6</sup> × N</b>, donde D es el diámetro del cilindro y R la carrera del pistón en centímetros, y N el número de cilindros. Como 0,785 × D² × R es la cilindrada de cada cilindro, basta con dividir la cilindrada total entre el número de cilindros. En motores de 2 tiempos el coeficiente es 0,11, y en eléctricos <b>CVF = potencia efectiva en kW ÷ 5,152</b>. El resultado se redondea a la baja con dos decimales.</p>
<p><b>Ejemplo:</b> un 1.5 gasolina de 4 cilindros (1.498 cm³) tiene 374,5 cm³ por cilindro: 0,08 × 374,5<sup>0,6</sup> × 4 = <b>11,20 CVF</b>, en el tramo de 8 a 11,99. Paga entre 34,08 € y 68,16 € según el ayuntamiento. El mismo coche con un motor de 1.598 cm³ pasaría a 11,64 CVF y seguiría en el mismo tramo; un 2.0 de 4 cilindros (1.995 cm³) ya tiene 13,30 CVF y paga entre 71,94 € y 143,88 €.</p>
<h2>Quién paga y cuándo</h2><p>Paga quien figure como titular del coche el <b>1 de enero</b>, aunque lo venda en febrero. Solo se prorratea por trimestres en el año de la primera matriculación y en el de la baja definitiva. ¿Vas a comprar? Calcula también el <a href="impuesto-matriculacion.html">impuesto de matriculación</a>, el <a href="coste-anual-coche.html">coste anual real del coche</a> o consulta la <a href="etiqueta-dgt.html">etiqueta DGT por matrícula</a>, que en muchas ciudades da derecho a bonificaciones.</p>""",
[("¿Cuánto se paga de impuesto de circulación?", "Depende de los caballos fiscales y del ayuntamiento. Para turismos, entre 12,62 € y 25,24 € al año con menos de 8 CVF, y entre 112 € y 224 € con 20 CVF o más. La mayoría de coches de 1.2 a 1.6 están en el tramo de 8 a 11,99 CVF: entre 34,08 € y 68,16 €."),
 ("¿Cómo calculo los caballos fiscales de mi coche?", "Con la fórmula del Reglamento General de Vehículos: 0,08 × (cilindrada ÷ cilindros)^0,6 × cilindros para motores de 4 tiempos. En eléctricos se divide la potencia efectiva en kW entre 5,152. También vienen en la ficha técnica."),
 ("¿Los coches eléctricos pagan impuesto de circulación?", "Sí, pero la ley permite a los ayuntamientos bonificar hasta el 75 % según el motor o el carburante, y muchas ciudades, como Madrid o Barcelona, lo aplican a los eléctricos. Revisa la ordenanza fiscal de tu municipio."),
 ("¿Quién paga el impuesto de circulación si vendo el coche?", "El que era titular el 1 de enero paga el año entero. La ley solo prorratea por trimestres en el año de la primera matriculación y en el de la baja definitiva, así que en una venta se suele pactar el reparto entre comprador y vendedor.")],
"Calculadora del impuesto de circulación y los caballos fiscales",
"""function modo(){const m=document.getElementById('mo').value;document.getElementById('rc').style.display=(m=='4'||m=='2')?'':'none';document.getElementById('re').style.display=m=='e'?'':'none';document.getElementById('rf').style.display=m=='c'?'':'none';}
function calc(){const m=document.getElementById('mo').value;let cvf,how='';
if(m=='e'){cvf=v('kw')/5.152;how=nf(v('kw'),1)+' kW ÷ 5,152';}
else if(m=='c'){cvf=v('cf');}
else{const cc=v('cc'),n=Math.max(1,Math.round(v('ci')));cvf=(m=='2'?0.11:0.08)*Math.pow(cc/n,0.6)*n;how=(m=='2'?'0,11':'0,08')+' × ('+nf(cc,0)+' ÷ '+n+')<sup>0,6</sup> × '+n;}
cvf=Math.floor(cvf*100+1e-6)/100;if(!(cvf>0)){show('r','Revisa los datos del motor.');return;}
const T=[[8,12.62,'menos de 8'],[12,34.08,'de 8 a 11,99'],[16,71.94,'de 12 a 15,99'],[20,89.61,'de 16 a 19,99'],[1e9,112,'20 o más']];
let i=0;while(cvf>=T[i][0])i++;const b=T[i][1],co=Math.min(2,Math.max(1,v('co')||1)),bo=+document.getElementById('bo').value,c=b*co*(1-bo/100);
let h='Impuesto de circulación al año:<b class="big">'+eur(c)+'</b>Potencia fiscal: <b>'+nf(cvf,2)+' CVF</b>'+(how?' ('+how+')':'')+' → tramo <b>'+T[i][2]+'</b> caballos fiscales.';
h+='<br>Según el ayuntamiento, entre <b>'+eur(b)+'</b> (coeficiente 1) y <b>'+eur(b*2)+'</b> (coeficiente 2). Con coeficiente '+nf(co,2)+(bo?' y bonificación del '+bo+' %':'')+': '+eur(c)+'.';
if(i<4){const lim=T[i][0];h+='<br>A partir de '+nf(lim,0)+' CVF cambiarías al tramo siguiente ('+eur(T[i+1][1]*co*(1-bo/100))+' con tu coeficiente).';}
show('r',h);}
modo();"""))

# --- ¿Qué coche me puedo permitir? Presupuesto según ingresos, gastos de uso y financiación (combustible: media oficial de carb/index.json) ---
S['tools'].insert(3, ("que-coche-me-puedo-permitir", "¿Qué coche me puedo permitir?", "El precio máximo de coche según tu sueldo, la entrada y lo que cuesta mantenerlo.", "Presupuesto"))
S['aff']["que-coche-me-puedo-permitir"] = SEG + ext("https://www.bde.es/wbe/es/para-ciudadanos/", "Guía del Banco de España sobre préstamos")
P.append(("que-coche-me-puedo-permitir", "¿Qué coche me puedo permitir según mi sueldo? Calculadora | CocheCuentas",
"Calcula el precio máximo de coche que puedes pagar con tu sueldo: cuota máxima, entrada, financiación y gastos reales de seguro, gasolina, mantenimiento e impuesto.",
"""<p class="lead">Pon tus ingresos netos, lo que tienes ahorrado para la entrada y cuánto vas a usar el coche. Te decimos la cuota que puedes asumir y el <b>precio máximo</b> de coche que encaja en tu bolsillo, contando lo que cuesta mantenerlo.</p>
<div class="card"><div class="row"><div><label for="in">Ingresos netos al mes del hogar (€)</label><input id="in" inputmode="decimal" value="2000"></div>
<div><label for="pc">Máximo para el coche, todo incluido (% de ingresos)</label><input id="pc" inputmode="decimal" value="20"></div>
<div><label for="en">Entrada o ahorro disponible (€)</label><input id="en" inputmode="decimal" value="3000"></div>
<div><label for="ti">TIN de la financiación (%)</label><input id="ti" inputmode="decimal" value="8"></div>
<div><label for="pl">Plazo (meses)</label><select id="pl"><option>36</option><option>48</option><option selected>60</option><option>72</option><option>84</option></select></div>
<div><label for="km">Kilómetros al año</label><input id="km" inputmode="numeric" value="12000"></div>
<div><label for="co">Consumo (l/100 km)</label><input id="co" inputmode="decimal" value="6"></div>
<div><label for="cb">Precio del combustible (€/l)</label><input id="cb" inputmode="decimal" value="1,55"></div>
<div><label for="se">Seguro al año (€)</label><input id="se" inputmode="decimal" value="450"></div>
<div><label for="ma">Mantenimiento, ITV y neumáticos al año (€)</label><input id="ma" inputmode="decimal" value="400"></div>
<div><label for="iv">Impuesto de circulación y aparcamiento al año (€)</label><input id="iv" inputmode="decimal" value="80"></div></div>
<p class="note" id="pn">Precio del combustible: media orientativa de gasolina 95.</p>
<button onclick="calc()">Calcular mi presupuesto</button><div class="res" id="r" aria-live="polite"></div></div>
<h2>Cómo se calcula</h2><p>Primero fijamos lo que puedes destinar al coche cada mes: un porcentaje de tus ingresos netos. Muchos asesores financieros recomiendan que el coste <b>total</b> del coche (cuota, combustible, seguro, mantenimiento e impuestos) no supere el <b>15-20 %</b> de lo que entra en casa. Después restamos los gastos de uso y lo que queda es la <b>cuota máxima</b>. Con esa cuota, el TIN y el plazo calculamos el capital que puedes pedir (sistema francés) y le sumamos tu entrada.</p>
<p><b>Fórmulas:</b> cuota máxima = ingresos × % − gastos de uso ÷ 12. Capital = cuota × (1 − (1 + i)<sup>−n</sup>) ÷ i, con i = TIN ÷ 12. Precio máximo = capital + entrada.</p>
<p><b>Ejemplo:</b> con 2.000 € netos y un 20 %, tienes 400 € al mes. Un coche que hace 12.000 km al año gastando 6 l/100 km a 1,55 €/l consume 1.116 € de combustible; con 450 € de seguro, 400 € de mantenimiento y 80 € de impuesto, el uso cuesta unos 170 € al mes. Te quedan 229 € de cuota: a 60 meses y un 8 % TIN puedes financiar unos 11.300 €, así que con 3.000 € de entrada tu tope está en torno a <b>14.300 €</b>. A 84 meses el tope sube, pero pagarás bastante más en intereses.</p>
<table><tr><th>Ingresos netos/mes</th><th>Al coche (20 %)</th><th>Precio máximo orientativo*</th></tr>
<tr><td>1.500 €</td><td>300 €</td><td>≈ 9.400 €</td></tr><tr><td>2.000 €</td><td>400 €</td><td>≈ 14.300 €</td></tr>
<tr><td>2.500 €</td><td>500 €</td><td>≈ 19.200 €</td></tr><tr><td>3.500 €</td><td>700 €</td><td>≈ 29.100 €</td></tr></table>
<p class="note">* Con los gastos de uso del ejemplo (≈ 170 €/mes), 3.000 € de entrada, 60 meses y 8 % TIN.</p>
<h2>Antes de comprar</h2><ul><li>Compara la <b>TAE</b> y el coste total en la <a href="cuota-financiacion-coche.html">calculadora de financiación</a>: las comisiones cambian mucho el resultado.</li>
<li>Calcula lo que perderá de valor con la <a href="depreciacion-coche.html">calculadora de depreciación</a> y revisa el <a href="coste-anual-coche.html">coste anual completo</a>.</li>
<li>Si es de segunda mano, mira su <a href="historial-coche-matricula.html">historial por matrícula</a> y su <a href="etiqueta-dgt.html">etiqueta DGT</a>. Si lo vas a usar poco, quizá te compense el <a href="renting-vs-compra.html">renting</a>.</li></ul>""",
[("¿Qué porcentaje del sueldo debo gastar en el coche?", "Como referencia, el coste total del coche (cuota más gasolina, seguro, mantenimiento e impuestos) no debería pasar del 15-20 % de tus ingresos netos. Si ya pagas hipoteca o alquiler alto, mejor quedarte cerca del 15 %."),
 ("¿Qué coche me puedo permitir con 1.500 € de sueldo?", "Destinando el 20 % (300 € al mes) y con unos 170 € de gastos de uso, te quedan unos 130 € de cuota: a 60 meses y 8 % TIN son unos 6.400 € financiados. Con 3.000 € de entrada, un coche de unos 9.400 €."),
 ("¿Es mejor alargar el plazo para comprar un coche más caro?", "Alargar el plazo baja la cuota pero dispara los intereses y puedes acabar debiendo más de lo que vale el coche. Si necesitas 84 meses para que la cuota encaje, probablemente el coche es demasiado caro para tu presupuesto.")],
"¿Qué coche me puedo permitir según mi sueldo?",
"""function calc(){const ing=v('in'),pre=ing*v('pc')/100,i=v('ti')/100/12,n=+document.getElementById('pl').value,ent=v('en');
const comb=v('km')*v('co')/100*v('cb'),uso=(comb+v('se')+v('ma')+v('iv'))/12,q=pre-uso;
if(ing<=0){show('r','Escribe tus ingresos netos mensuales.');return;}
let h;if(q<=0){h='Con este presupuesto <b>no queda margen para cuota</b>:<b class="big">'+eur(ent)+'</b>Lo que destinas al coche ('+eur(pre)+' al mes) no cubre ni los gastos de uso ('+eur(uso)+' al mes). Busca un coche que puedas pagar al contado con tu ahorro, sube el porcentaje o reduce kilómetros y seguro.';}
else{const cap=i?q*(1-Math.pow(1+i,-n))/i:q*n,pm=cap+ent,int=q*n-cap;
h='Precio máximo de coche:<b class="big">'+eur(Math.floor(pm/100)*100)+'</b>Presupuesto para el coche: <b>'+eur(pre)+'</b> al mes · Gastos de uso: '+eur(uso)+' al mes (combustible '+eur(comb/12)+')<br>Cuota máxima: <b>'+eur(q)+'</b> durante '+n+' meses → puedes financiar '+eur(cap)+' (pagarás '+eur(int)+' de intereses) + '+eur(ent)+' de entrada.';
const al=[36,48,60,72,84].filter(x=>x!=n).map(m=>m+' meses: '+eur(Math.floor(((i?q*(1-Math.pow(1+i,-m))/i:q*m)+ent)/100)*100)).join(' · ');h+='<br><span class="note">Con otros plazos: '+al+'</span>';}
show('r',h);}
fetch('carb/index.json').then(r=>r.json()).then(j=>{if(!j.medias||!j.medias.g95)return;document.getElementById('cb').value=j.medias.g95.toFixed(3).replace('.',',');document.getElementById('pn').innerHTML='Precio del combustible: media de la gasolina 95 en España según el Ministerio para la Transición Ecológica ('+(j.fecha||'').split(' ')[0]+'). Si tu coche es diésel, cámbialo por el de tu <a href="gasolineras-baratas.html">gasolinera</a>.';calc();}).catch(()=>{});
calc();"""))

# --- Consumo real del coche (método del depósito lleno, varios repostajes) ---
S['tools'].insert(4, ("consumo-real-coche", "Consumo real de tu coche", "Calcula los l/100 km reales con tus repostajes y compáralo con el homologado.", "Consumo real"))
S['aff']["consumo-real-coche"] = amz("lector obd2 bluetooth", "Lectores OBD2 para ver el consumo") + amz("medidor presion neumaticos", "Medidores de presión de neumáticos")
P.append(("consumo-real-coche", "Calcular consumo real de un coche (l/100 km) con tus repostajes | CocheCuentas",
"Calcula el consumo real de tu coche en litros cada 100 km con el método del depósito lleno: uno o varios repostajes, coste por km, km por litro y CO2. Compáralo con el WLTP.",
"""<p class="lead">El ordenador de a bordo suele marcar menos de lo que gastas de verdad. Llena el depósito, apunta los kilómetros y en los siguientes repostajes anota los litros que entran hasta llenar: así sale tu consumo real.</p>
<div class="card"><table id="tb"><tr><th>Km del cuentakilómetros</th><th>Litros hasta llenar</th></tr></table>
<p class="note">Primera fila: el llenado de partida (no hace falta poner litros). Cada fila siguiente: kilómetros al volver a llenar y litros que han entrado. Llena siempre hasta que salte el surtidor.</p>
<button type="button" onclick="fila('','')" style="background:#fff;color:inherit;border:1px solid #cfd3df;margin-top:8px">+ Añadir repostaje</button>
<div class="row"><div><label for="cb">Combustible</label><select id="cb" onchange="pz()"><option value="g95">Gasolina</option><option value="gA">Diésel</option></select></div>
<div><label for="p">Precio por litro (€)</label><input id="p" inputmode="decimal" value="1,55"></div>
<div><label for="wl">Consumo homologado WLTP (l/100 km, opcional)</label><input id="wl" inputmode="decimal" value="5,6"></div></div>
<button onclick="calc()">Calcular consumo real</button><div class="res" id="r" aria-live="polite"></div></div>
<h2>Cómo se calcula el consumo real</h2><p>Con el <b>método del depósito lleno</b>: si llenas el depósito, recorres unos kilómetros y vuelves a llenar, los litros que entran la segunda vez son exactamente lo que has gastado en ese recorrido.</p>
<p><b>Fórmula:</b> consumo (l/100 km) = litros repostados ÷ kilómetros recorridos × 100. Con varios repostajes se suman todos los litros (menos los del llenado de partida) y se dividen entre los kilómetros totales: así se corrigen los pequeños errores de cada llenado.</p>
<p><b>Ejemplo:</b> llenas con el cuentakilómetros en 45.200 km. Vuelves a llenar a los 45.780 (entran 36,2 l), a los 46.390 (38,9 l) y a los 46.950 (35,1 l). Has gastado 110,2 litros en 1.750 km: <b>6,30 l/100 km</b>, un 12 % más que los 5,6 homologados. A 1,55 €/l, cada 100 km te cuestan 9,76 €.</p>
<table><tr><th>Consumo real</th><th>Km con 1 litro</th><th>Coste cada 100 km (1,55 €/l)</th><th>Coste con 15.000 km/año</th></tr>
<tr><td>4,5 l/100 km</td><td>22,2 km</td><td>6,98 €</td><td>1.046 €</td></tr><tr><td>6 l/100 km</td><td>16,7 km</td><td>9,30 €</td><td>1.395 €</td></tr>
<tr><td>7,5 l/100 km</td><td>13,3 km</td><td>11,63 €</td><td>1.744 €</td></tr><tr><td>9 l/100 km</td><td>11,1 km</td><td>13,95 €</td><td>2.093 €</td></tr></table>
<h2>Por qué gastas más que el homologado</h2><ul><li>El ciclo <b>WLTP</b> se mide en laboratorio: en la práctica es normal gastar entre un 10 y un 20 % más, y más aún en ciudad o con frío.</li>
<li>En invierno el motor tarda en calentarse y los trayectos cortos disparan el consumo. Las ruedas con poca presión también suben el gasto.</li>
<li>A 120 km/h un coche gasta bastante más que a 100 km/h, porque la resistencia del aire crece con el cuadrado de la velocidad.</li></ul>
<p>Con tu consumo real ya puedes calcular el <a href="coste-viaje-coche.html">coste de un viaje en coche</a>, tu <a href="coste-por-km.html">coste por kilómetro</a> o si te compensa un <a href="electrico-vs-gasolina.html">coche eléctrico</a>. Y para pagar menos por litro, busca las <a href="gasolineras-baratas.html">gasolineras más baratas cerca de ti</a>.</p>""",
[("¿Cómo calculo el consumo real de mi coche?", "Llena el depósito y pon el cuentakilómetros parcial a cero. En el siguiente repostaje, vuelve a llenar y divide los litros que han entrado entre los kilómetros recorridos y multiplica por 100. Por ejemplo, 36 litros en 580 km son 6,2 l/100 km."),
 ("¿Es fiable el consumo que marca el ordenador de a bordo?", "Sirve como referencia, pero suele marcar entre un 3 y un 10 % menos que el consumo real. El método del depósito lleno con varios repostajes es el más exacto que puedes hacer en casa."),
 ("¿Cuánto es normal gastar más que el consumo homologado?", "Con el ciclo WLTP es habitual gastar entre un 10 y un 20 % más en uso real. Si gastas más de un 30 % por encima, revisa la presión de los neumáticos, los filtros y tu forma de conducir.")],
"Calcula el consumo real de tu coche",
"""const tb=document.getElementById('tb');
function fila(k,l){const r=tb.insertRow();r.innerHTML='<td><input inputmode="numeric" aria-label="Kilómetros" value="'+k+'"></td><td><input inputmode="decimal" aria-label="Litros" value="'+l+'"></td>';}
[['45200',''],['45780','36,2'],['46390','38,9'],['46950','35,1']].forEach(x=>fila(x[0],x[1]));
const num=s=>parseFloat(String(s).replace(/\\./g,'').replace(',','.'));
function calc(){const R=[...tb.querySelectorAll('tr')].slice(1).map(r=>{const i=r.querySelectorAll('input');return [num(i[0].value),parseFloat(String(i[1].value).replace(',','.'))];}).filter(x=>x[0]>0);
if(R.length<2){show('r','Añade al menos el llenado de partida y un repostaje.');return;}
let L=0,t='',ok=true;for(let k=1;k<R.length;k++){const d=R[k][0]-R[k-1][0],l=R[k][1];if(!(d>0)||!(l>0)){ok=false;break;}L+=l;t+='<tr><td>'+nf(R[k-1][0],0)+' → '+nf(R[k][0],0)+' km</td><td>'+nf(d,0)+' km</td><td>'+nf(l/d*100,2)+' l/100 km</td></tr>';}
if(!ok){show('r','Revisa los datos: los kilómetros deben ir aumentando y cada repostaje necesita sus litros.');return;}
const km=R[R.length-1][0]-R[0][0],c=L/km*100,p=v('p'),wl=v('wl'),f=document.getElementById('cb').value=='gA'?2.68:2.31;
let h='Consumo real:<b class="big">'+nf(c,2)+' l/100 km</b>'+nf(L,1)+' litros en '+nf(km,0)+' km · '+nf(km/L,1)+' km por litro<br>Coste: <b>'+eur(c*p)+' cada 100 km</b> ('+nf(c*p,2)+' céntimos por km) · CO<sub>2</sub>: unos '+nf(c*f*10,0)+' g/km';
if(wl>0){const dv=(c/wl-1)*100;h+='<br>Frente al homologado ('+nf(wl,1)+' l/100 km): <b>'+(dv>=0?'+':'')+nf(dv,0)+' %</b>'+(dv>30?'. Es bastante más de lo normal: revisa presiones, filtros y conducción.':dv>=0?'. Dentro de lo habitual en uso real.':'. Muy buena conducción.');}
if(R.length>2)h+='<table><tr><th>Tramo</th><th>Km</th><th>Consumo</th></tr>'+t+'</table>';
show('r',h);}
let MED=null;function pz(){const k=document.getElementById('cb').value;if(MED&&MED[k])document.getElementById('p').value=MED[k].toFixed(3).replace('.',',');calc();}
fetch('carb/index.json').then(r=>r.json()).then(j=>{if(j.medias){MED=j.medias;pz();}}).catch(()=>{});
calc();"""))

# --- Distancia de frenado y de detención según velocidad, firme y tiempo de reacción (física: d = v·t + v²/(2·μ·g)) ---
S['tools'].insert(7, ("distancia-frenado", "Distancia de frenado", "Cuántos metros necesitas para parar según la velocidad, la lluvia, la nieve o el hielo.", ""))
S['aff']["distancia-frenado"] = amz("cadenas nieve textiles coche", "Cadenas de nieve textiles") + amz("neumaticos invierno", "Neumáticos de invierno y all season") + amz("medidor profundidad dibujo neumatico", "Medidor de dibujo del neumático")
P.append(("distancia-frenado", "Distancia de frenado: calculadora con lluvia, nieve y hielo | CocheCuentas",
"Calcula cuántos metros necesitas para detener el coche según la velocidad, el tiempo de reacción y el firme (seco, mojado, nieve o hielo), y a qué velocidad chocarías si el obstáculo está más cerca.",
"""<p class="lead">Elige la velocidad y el estado de la carretera. Te decimos los metros que recorres mientras reaccionas, los que necesitas para frenar y, si pones a qué distancia aparece un obstáculo, si te daría tiempo a parar.</p>
<div class="card"><div class="row"><div><label for="ve">Velocidad (km/h)</label><input id="ve" inputmode="numeric" value="120"></div>
<div><label for="fi">Estado de la carretera</label><select id="fi"><option value="0.8">Asfalto seco</option><option value="0.5">Asfalto mojado</option><option value="0.35">Mojado con neumáticos gastados</option><option value="0.2">Nieve compacta</option><option value="0.1">Hielo</option></select></div>
<div><label for="tr">Tiempo de reacción (segundos)</label><select id="tr"><option value="1">1 s: conductor atento</option><option value="1.5">1,5 s: cansado o de noche</option><option value="2.5">2,5 s: mirando el móvil o con alcohol</option></select></div>
<div><label for="ob">Obstáculo a (metros, opcional)</label><input id="ob" inputmode="numeric" value="80"></div></div>
<button onclick="calc()">Calcular distancia</button><div class="res" id="r" aria-live="polite"></div></div>
<h2>Cómo se calcula la distancia de detención</h2><p>La distancia total para parar tiene dos partes. La <b>distancia de reacción</b> es lo que recorres desde que ves el peligro hasta que pisas el freno: a velocidad constante, así que es la velocidad en m/s por el tiempo de reacción. La <b>distancia de frenado</b> depende del cuadrado de la velocidad y del agarre entre neumático y carretera (coeficiente de rozamiento μ).</p>
<p><b>Fórmula:</b> distancia de detención = v × t + v² ÷ (2 × μ × 9,81), con v en metros por segundo (km/h ÷ 3,6). Usamos μ = 0,8 en seco, 0,5 en mojado, 0,35 en mojado con neumáticos al límite, 0,2 en nieve compacta y 0,1 en hielo, valores típicos de un turismo con ABS. Son estimaciones: un coche cargado, una cuesta abajo o unos frenos en mal estado alargan la distancia.</p>
<div style="overflow-x:auto"><table><tr><th>Velocidad</th><th>Reacción (1 s)</th><th>Seco</th><th>Mojado</th><th>Nieve</th><th>Hielo</th></tr>
<tr><td>30 km/h</td><td>8 m</td><td>13 m</td><td>15 m</td><td>26 m</td><td>44 m</td></tr>
<tr><td>50 km/h</td><td>14 m</td><td>26 m</td><td>34 m</td><td>63 m</td><td>112 m</td></tr>
<tr><td>90 km/h</td><td>25 m</td><td>65 m</td><td>89 m</td><td>184 m</td><td>344 m</td></tr>
<tr><td>100 km/h</td><td>28 m</td><td>77 m</td><td>106 m</td><td>224 m</td><td>421 m</td></tr>
<tr><td>120 km/h</td><td>33 m</td><td>104 m</td><td>147 m</td><td>316 m</td><td>600 m</td></tr></table></div>
<p class="note">Distancia total de detención (reacción + frenado) con 1 segundo de reacción.</p>
<p><b>Ejemplo:</b> un peatón cruza a 35 metros en una calle seca. A 60 km/h paras justo a tiempo (34 m). A 70 km/h necesitas 40 m: llegas a él todavía a unos <b>42 km/h</b>. Diez kilómetros por hora de más convierten un susto en un atropello.</p>
<h2>La regla de la autoescuela: (velocidad ÷ 10)²</h2><p>En muchas autoescuelas se enseña un cálculo mental para la distancia total de detención: quita el cero a la velocidad y elévalo al cuadrado. A 50 km/h, 5² = 25 m; a 100 km/h, 10² = 100 m. Para la distancia de reacción se usa (velocidad ÷ 10) × 3: unos 30 m a 100 km/h. Es una buena aproximación en seco con un conductor atento (a 100 km/h nuestra calculadora da 77 m, y 106 m en mojado), pero se queda corta a velocidades altas y con lluvia, nieve o hielo, donde la frenada crece mucho más.</p>
<h2>Qué distancia dejar con el coche de delante</h2><p>La regla práctica que recomienda la DGT es la de los <b>dos segundos</b>: cuando el coche de delante pase por un punto fijo (una señal, un puente), cuenta «mil uno, mil dos»; si llegas a ese punto antes de terminar, vas demasiado cerca. Con lluvia, niebla o de noche, déjalo al menos en el doble, y con nieve o hielo mucho más. En estas fechas, antes de un viaje largo, revisa la profundidad del dibujo de los neumáticos (mínimo legal 1,6 mm) y lleva cadenas si vas a zonas de montaña.</p>
<p>Calcula también lo que te costaría una <a href="multa-exceso-velocidad.html">multa por exceso de velocidad</a>, tu <a href="calculadora-alcoholemia.html">tasa de alcoholemia estimada</a>, el <a href="coste-viaje-coche.html">coste de tu viaje en coche</a> con el precio de hoy del combustible o si una <a href="equivalencia-neumaticos.html">medida de neumático distinta</a> es compatible con tu coche.</p>""",
[("¿Cuántos metros necesita un coche para frenar a 120 km/h?", "En seco y con un conductor atento, unos 104 metros en total: 33 m mientras reacciona y 71 m frenando. Con la carretera mojada pasa a unos 147 metros, y con nieve a más de 300."),
 ("¿Cómo se calcula la distancia de frenado?", "Distancia de frenado = v² ÷ (2 × μ × 9,81), con la velocidad en m/s y μ el agarre del firme (0,8 en seco, 0,5 en mojado). Como depende del cuadrado de la velocidad, si vas el doble de rápido necesitas cuatro veces más metros para frenar."),
 ("¿Cuánto aumenta la distancia de frenado con lluvia?", "Alrededor de un 60 % solo en la parte de frenado, y más si los neumáticos tienen poco dibujo. Con nieve compacta se multiplica por cuatro y en hielo por ocho respecto al asfalto seco."),
 ("¿Qué es la regla de los dos segundos?", "Una forma sencilla de mantener la distancia de seguridad: entre que el coche de delante pasa por un punto y tú llegas a él deben pasar al menos dos segundos. Con lluvia o mala visibilidad, al menos el doble.")],
"Calculadora de distancia de frenado",
"""const FN={'0.8':'en seco','0.5':'en mojado','0.35':'en mojado con neumáticos gastados','0.2':'sobre nieve','0.1':'sobre hielo'};
function det(kmh,mu,t){const s=kmh/3.6;return [s*t,s*s/(2*mu*9.81)];}
function calc(){const kmh=v('ve'),fs=document.getElementById('fi').value,mu=parseFloat(fs),t=parseFloat(document.getElementById('tr').value),ob=v('ob');
if(kmh<=0){show('r','Escribe la velocidad.');return;}
const [dr,df]=det(kmh,mu,t),dt=dr+df,s=kmh/3.6;
let h='Distancia total para detenerte '+FN[fs]+':<b class="big">'+nf(dt,0)+' metros</b>Reacción: <b>'+nf(dr,0)+' m</b> ('+nf(t,1)+' s sin frenar) · Frenada: <b>'+nf(df,0)+' m</b> · Tardas unos '+nf(t+s/(mu*9.81),1)+' s en parar.';
if(fs!='0.8'){const [a,b]=det(kmh,0.8,t);h+='<br>En seco te bastarían '+nf(a+b,0)+' m: necesitas <b>'+nf(dt-a-b,0)+' m más</b>.';}
if(ob>0){if(ob>=dt)h+='<br>Con un obstáculo a '+nf(ob,0)+' m <b>te da tiempo a parar</b>, con '+nf(ob-dt,0)+' m de margen.';
else{const rest=ob-dr,vi=rest<=0?kmh:Math.sqrt(Math.max(0,s*s-2*mu*9.81*rest))*3.6;let vs=kmh;while(vs>0){const [x,y]=det(vs,mu,t);if(x+y<=ob)break;vs--;}
h+='<br>Con un obstáculo a '+nf(ob,0)+' m <b>no te da tiempo a parar</b>: llegarías a él a unos <b>'+nf(vi,0)+' km/h</b>'+(rest<=0?' (ni siquiera habrías empezado a frenar)':'')+'. Para poder detenerte tendrías que ir a '+(vs>0?nf(vs,0)+' km/h o menos':'muy poca velocidad')+'.';}}
h+='<br>Distancia de seguridad mínima con el coche de delante (regla de los 2 s): <b>'+nf(s*2*(fs=='0.8'?1:2),0)+' m</b>'+(fs=='0.8'?'':' (doblada por el mal estado del firme)')+'.';
const mx=Math.max(dt,ob||0),pc=x=>(x/mx*100).toFixed(1)+'%';
h+='<div aria-hidden="true" style="margin-top:12px;position:relative;height:26px;background:#fff;border-radius:6px;overflow:hidden;font-size:.75rem;color:#fff"><div style="position:absolute;left:0;top:0;bottom:0;width:'+pc(dr)+';background:#f08c00;padding:4px 6px;white-space:nowrap">Reacción</div><div style="position:absolute;left:'+pc(dr)+';top:0;bottom:0;width:'+pc(df)+';background:#d9480f;padding:4px 6px;white-space:nowrap;overflow:hidden">Frenada</div>'+(ob>0?'<div title="Obstáculo" style="position:absolute;left:calc('+pc(ob)+' - 3px);top:0;bottom:0;width:3px;background:#1d2433"></div>':'')+'</div>'+(ob>0?'<span class="note">La raya negra marca dónde está el obstáculo.</span>':'');
let tb='<table style="margin-top:10px;font-size:.9rem"><tr><th>Velocidad</th><th>Para en</th>'+(ob>0?'<th>Con obstáculo a '+nf(ob,0)+' m</th>':'')+'</tr>';
[kmh-20,kmh-10,kmh,kmh+10].filter(x=>x>0).forEach(x=>{const [a,b2]=det(x,mu,t),tt=a+b2;let c='';if(ob>0){if(tt<=ob)c='Paras';else{const r2=ob-a,s2=x/3.6;c='Chocas a '+nf(r2<=0?x:Math.sqrt(Math.max(0,s2*s2-2*mu*9.81*r2))*3.6,0)+' km/h';}}
tb+='<tr'+(x==kmh?' style="font-weight:700"':'')+'><td>'+nf(x,0)+' km/h</td><td>'+nf(tt,0)+' m</td>'+(ob>0?'<td>'+c+'</td>':'')+'</tr>';});
h+=tb+'</table>';
show('r',h);}
document.querySelectorAll('.card input,.card select').forEach(e=>e.addEventListener(e.tagName=='SELECT'||e.type=='checkbox'||e.type=='date'?'change':'input',()=>calc()));
calc();"""))

# --- Calculadora de alcoholemia (fórmula de Widmark) con límites y sanciones de la DGT ---
S['tools'].insert(8, ("calculadora-alcoholemia", "Calculadora de alcoholemia", "Tasa estimada de alcohol en sangre y aire, cuándo bajará y qué multa supone.", ""))
S['aff']["calculadora-alcoholemia"] = amz("alcoholimetro digital", "Alcoholímetros digitales") + ext("https://www.dgt.es/", "Normas y campañas de la DGT")
P.append(("calculadora-alcoholemia", "Calculadora de alcoholemia: tasa de alcohol en aire y sangre | CocheCuentas",
"Estima tu tasa de alcohol en sangre y en aire espirado según lo que has bebido, tu peso y el tiempo pasado, cuánto tardará en bajar y qué multa y puntos supone según la DGT.",
"""<p class="lead">Indica qué has bebido, tu peso y cuánto hace que empezaste. Te damos una estimación de tu tasa de alcohol en sangre y en aire espirado (la que mide el etilómetro de la Guardia Civil) y cuántas horas tardará en bajar.</p>
<div class="card" style="border-left:4px solid #d9480f"><p style="margin:0"><b>Importante:</b> es una estimación matemática. El alcohol afecta muy distinto a cada persona y depende de lo que hayas comido, de tu salud y de la medicación. <b>No la uses para decidir si puedes conducir:</b> si has bebido, no conduzcas. La única tasa segura es 0,0.</p></div>
<div class="card"><div class="row"><div><label for="sx">Sexo</label><select id="sx"><option value="0.68">Hombre</option><option value="0.55">Mujer</option></select></div>
<div><label for="pe">Peso (kg)</label><input id="pe" inputmode="numeric" value="75"></div>
<div><label for="b1">Cañas de cerveza (200 ml, 5 %)</label><input id="b1" type="number" min="0" value="2"></div>
<div><label for="b2">Tercios o latas de cerveza (330 ml, 5 %)</label><input id="b2" type="number" min="0" value="0"></div>
<div><label for="b3">Copas de vino (150 ml, 13 %)</label><input id="b3" type="number" min="0" value="2"></div>
<div><label for="b4">Copas de cava (100 ml, 11,5 %)</label><input id="b4" type="number" min="0" value="0"></div>
<div><label for="b5">Copas o cubatas (60 ml de destilado, 38 %)</label><input id="b5" type="number" min="0" value="0"></div>
<div><label for="b6">Chupitos (30 ml, 40 %)</label><input id="b6" type="number" min="0" value="0"></div>
<div><label for="h">Horas desde la primera copa</label><input id="h" inputmode="decimal" value="2"></div>
<div><label for="cd">Tipo de conductor</label><select id="cd"><option value="g">General</option><option value="n">Novel (menos de 2 años) o profesional</option></select></div></div>
<div class="res" id="r" aria-live="polite"></div></div>
<h2>Cómo se calcula la tasa de alcohol</h2><p>Usamos la <b>fórmula de Widmark</b>, la más empleada en medicina forense: tasa en sangre (g/l) = gramos de alcohol ÷ (peso × r) − 0,15 × horas. El factor r refleja el agua corporal en la que se reparte el alcohol: 0,68 en hombres y 0,55 en mujeres. El hígado elimina de media unos 0,15 g/l por hora, aunque varía entre 0,10 y 0,20. Los gramos de alcohol de una bebida son mililitros × graduación ÷ 100 × 0,8 (la densidad del alcohol).</p>
<p>En España el etilómetro mide el alcohol en <b>aire espirado</b>, en mg/l. La equivalencia legal es dividir la tasa en sangre entre dos: 0,5 g/l en sangre son 0,25 mg/l en aire.</p>
<p><b>Ejemplo:</b> un hombre de 75 kg toma dos cañas (8 g de alcohol cada una) y dos copas de vino (15,6 g cada una): 47,2 g. Su tasa máxima teórica es 47,2 ÷ (75 × 0,68) = 0,93 g/l. Dos horas después, tras eliminar 0,30 g/l, sigue en torno a <b>0,63 g/l en sangre, 0,31 mg/l en aire</b>: por encima del límite general. Necesitaría unas 4 horas más para eliminarlo todo.</p>
<h2>Límites y sanciones en España</h2><table><tr><th>Tasa en aire espirado</th><th>Conductor general</th><th>Novel o profesional</th></tr>
<tr><td>Hasta 0,15 mg/l</td><td>Permitido</td><td>Permitido</td></tr>
<tr><td>0,15 a 0,25 mg/l</td><td>Permitido</td><td>500 € y 4 puntos</td></tr>
<tr><td>0,25 a 0,30 mg/l</td><td>500 € y 4 puntos</td><td>500 € y 4 puntos</td></tr>
<tr><td>0,30 a 0,50 mg/l</td><td>500 € y 4 puntos</td><td>1.000 € y 6 puntos</td></tr>
<tr><td>0,50 a 0,60 mg/l</td><td>1.000 € y 6 puntos</td><td>1.000 € y 6 puntos</td></tr>
<tr><td>Más de 0,60 mg/l</td><td colspan="2">Delito (art. 379 del Código Penal): prisión de 3 a 6 meses o multa o trabajos para la comunidad, y retirada del carné de 1 a 4 años</td></tr></table>
<p class="note">La multa es de 1.000 € también si ya te sancionaron por alcohol en el año anterior. Negarse a la prueba es delito. En septiembre de 2026 el Congreso admitió a trámite una ley para bajar el límite general a 0,2 g/l en sangre (0,1 mg/l en aire); cuando se apruebe actualizaremos esta calculadora.</p>
<h2>Mitos que no bajan la tasa</h2><p>Ni el café, ni una ducha fría, ni los caramelos de menta, ni hacer ejercicio aceleran la eliminación del alcohol: solo el tiempo. Comer antes de beber retrasa la absorción y reduce algo el pico, pero no evita que el alcohol llegue a la sangre. En las comidas y cenas de Navidad, lo más sencillo es elegir quién conduce o volver en taxi o transporte público.</p>
<p>Consulta también qué supone una <a href="multa-exceso-velocidad.html">multa por exceso de velocidad</a>, la <a href="distancia-frenado.html">distancia de frenado</a> según tu velocidad (con alcohol, el tiempo de reacción se dispara) o el <a href="coste-viaje-coche.html">coste de tu viaje de Navidad en coche</a>.</p>""",
[("¿Cuál es la tasa de alcohol permitida para conducir?", "Para conductores en general, 0,5 g/l en sangre o 0,25 mg/l en aire espirado. Para noveles (menos de dos años de carné) y profesionales, 0,3 g/l en sangre o 0,15 mg/l en aire."),
 ("¿Cuánto tarda en bajar el alcohol?", "El hígado elimina de media 0,15 g/l por hora (0,075 mg/l en aire). Una tasa de 0,6 g/l tarda unas 4 horas en desaparecer. Ni el café ni dormir un rato lo aceleran."),
 ("¿Cuánto alcohol tiene una caña?", "Una caña de 200 ml de cerveza al 5 % tiene unos 8 gramos de alcohol, casi una unidad de bebida estándar (10 g). Una copa de vino tiene unos 15 g y un cubata, en torno a 18 g."),
 ("¿Qué multa hay por dar positivo en alcoholemia?", "Entre 0,25 y 0,50 mg/l en aire, 500 € y 4 puntos; más de 0,50 mg/l, 1.000 € y 6 puntos. Por encima de 0,60 mg/l es delito, con retirada del carné de 1 a 4 años.")],
"Calculadora de alcoholemia",
"""const BB=[[200,5],[330,5],[150,13],[100,11.5],[60,38],[30,40]];
function sanc(a,nov){if(a>0.6)return '<b>Delito</b>: prisión de 3 a 6 meses o multa o trabajos para la comunidad, y retirada del carné de 1 a 4 años';
if(a>0.5)return '<b>1.000 € y 6 puntos</b>';if(nov){if(a>0.3)return '<b>1.000 € y 6 puntos</b>';if(a>0.15)return '<b>500 € y 4 puntos</b>';}else if(a>0.25)return '<b>500 € y 4 puntos</b>';return '';}
const hm=x=>{const m=Math.round(x*60);return m<60?m+' min':Math.floor(m/60)+' h'+(m%60?' '+(m%60)+' min':'');};
function calc(){const r=parseFloat(document.getElementById('sx').value),p=v('pe'),t=Math.max(0,v('h')),nov=document.getElementById('cd').value=='n';
let g=0;BB.forEach((b,i)=>{g+=Math.max(0,v('b'+(i+1)))*b[0]*b[1]/100*0.8;});
if(p<30||p>250){show('r','Escribe tu peso en kilos.');return;}if(g<=0){show('r','Indica lo que has bebido.');return;}
const c0=g/(p*r),c=Math.max(0,c0-0.15*t),a=c/2,lim=nov?0.3:0.5;
const tl=Math.max(0,(c0-lim)/0.15-t),t0=Math.max(0,c0/0.15-t),s=sanc(a,nov);
let h='Tasa estimada ahora:<b class="big">'+nf(a,2)+' mg/l en aire</b>'+nf(c,2)+' g/l en sangre · Has tomado '+nf(g,0)+' g de alcohol ('+nf(g/10,1)+' unidades de bebida estándar) · Pico teórico: '+nf(c0,2)+' g/l';
if(c<=0)h+='<br>Según la fórmula, ya habrías eliminado el alcohol. Aun así, cada organismo es distinto.';
else{h+='<br>Límite para ti: '+nf(lim/2,2)+' mg/l en aire. '+(c>lim?'Estarías <b>por encima del límite</b>: '+s+'.':'Estarías por debajo del límite legal, pero el alcohol ya afecta a tus reflejos.');
const rg=(x,y)=>hm(Math.max(0,x/0.2-t))+' y '+hm(Math.max(0,x/0.1-t));
if(c>lim)h+='<br>Para bajar del límite necesitarías, según cada persona, entre <b>'+rg(c0-lim)+'</b> más (media: '+hm(tl)+').';h+='<br>Para eliminarlo del todo: entre <b>'+rg(c0)+'</b> más.';}
let tb='<table style="margin-top:10px;font-size:.9rem"><tr><th>Dentro de</th><th>Sangre</th><th>Aire</th></tr>';[0,1,2,3,4,6].forEach(x=>{const cx=Math.max(0,c0-0.15*(t+x));tb+='<tr><td>'+(x?x+' h':'Ahora')+'</td><td>'+nf(cx,2)+' g/l</td><td>'+(cx/2>lim/2?'<b>'+nf(cx/2,2)+' mg/l</b>':nf(cx/2,2)+' mg/l')+'</td></tr>';});
h+=tb+'</table><span class="note">Estimación orientativa con eliminación media de 0,15 g/l por hora. Si has bebido, no conduzcas.</span>';
show('r',h);}
document.querySelectorAll('.card input,.card select').forEach(e=>e.addEventListener(e.tagName=='SELECT'?'change':'input',()=>calc()));
calc();"""))

# --- Cuándo pasar la ITV: calendario de inspecciones según RD 920/2017 ---
S['tools'].insert(2, ("cuando-pasar-itv", "¿Cuándo me toca pasar la ITV?", "Fecha de tu próxima ITV y las siguientes, para coche, moto o ciclomotor, y desde cuándo puedes adelantarla.", "ITV"))
S['aff']["cuando-pasar-itv"] = amz("kit emergencia coche triangulos v16", "Luz V16 y kit de emergencia") + amz("lampara h7 coche", "Lámparas para faros") + amz("escobillas limpiaparabrisas", "Escobillas limpiaparabrisas")
P.append(("cuando-pasar-itv", "Cuándo pasar la ITV: calcula la fecha de tu próxima ITV | CocheCuentas",
"Cuándo toca pasar la ITV de tu coche, moto o ciclomotor según la fecha de matriculación: próxima inspección, desde qué día puedes adelantarla y calendario de las siguientes.",
"""<p class="lead">Elige el tipo de vehículo y la fecha de primera matriculación (viene en el permiso de circulación). Te decimos cuándo te toca la ITV, desde qué día puedes pasarla sin perder días y las fechas de las siguientes.</p>
<div class="card"><div class="row"><div><label for="t">Tipo de vehículo</label><select id="t"><option value="c">Turismo (coche particular)</option><option value="m">Moto o cuatriciclo (quad)</option><option value="k">Ciclomotor</option></select></div>
<div><label for="a">Fecha de primera matriculación</label><input id="a" type="date" value="2018-03-15"></div>
<div><label for="u">Caducidad de tu ITV actual (opcional)</label><input id="u" type="date"></div>
<div><label for="h">Calcular a fecha de</label><input id="h" type="date" data-today></div></div>
<p class="note">Si alguna vez pasaste la ITV con retraso, las fechas se desplazan: pon la caducidad que aparece en tu tarjeta ITV o en la pegatina del parabrisas y calculamos a partir de ella.</p>
<div class="res" id="r" aria-live="polite"></div></div>
<h2>Cada cuánto se pasa la ITV</h2><table><tr><th>Vehículo</th><th>Primera ITV</th><th>Después</th></tr>
<tr><td>Turismo</td><td>A los 4 años</td><td>Cada 2 años hasta los 10; desde entonces, cada año</td></tr>
<tr><td>Moto y cuatriciclo</td><td>A los 4 años</td><td>Cada 2 años</td></tr>
<tr><td>Ciclomotor</td><td>A los 3 años</td><td>Cada 2 años</td></tr></table>
<p>Los años se cuentan desde la fecha de primera matriculación, según el Real Decreto 920/2017 (resumen oficial en <a href="https://administracion.gob.es/pag_Home/Tu-espacio-europeo/derechos-obligaciones/ciudadanos/vehiculos/itv.html" rel="noopener" target="_blank">administracion.gob.es</a>). Furgonetas, autocaravanas, remolques, taxis y vehículos de alquiler tienen otras frecuencias: consulta tu estación ITV.</p>
<p><b>Ejemplo:</b> un coche matriculado el 15 de marzo de 2018 pasó su primera ITV en 2022 y la siguiente en 2024. Le toca el 15 de marzo de 2026 y el 15 de marzo de 2028, que es su décimo aniversario. A partir de ahí, la pasará cada año: 2029, 2030, 2031…</p>
<h2>Puedes adelantarla 30 días sin perder nada</h2><p>Si pasas la inspección en los 30 días naturales anteriores a la fecha de caducidad, la siguiente se calcula desde la fecha de caducidad, no desde el día que fuiste. Así no pierdes ni un día de validez. Si la pasas tarde, en cambio, el plazo nuevo empieza a contar desde el día de la inspección.</p>
<h2>Qué pasa si circulas con la ITV caducada</h2><ul><li><b>Multa de 200 €</b> si te paran con la ITV caducada; puede ser de 500 € si el resultado de la última inspección fue negativo.</li><li>Si la ITV sale <b>desfavorable</b>, tienes dos meses para reparar y volver; con resultado <b>negativo</b>, el coche solo puede ir al taller o a la estación.</li><li>La ITV caducada no anula el seguro obligatorio, pero un accidente puede complicar la reclamación si el fallo influyó.</li></ul>
<p>Antes de ir, revisa luces, neumáticos (mínimo 1,6 mm de dibujo), limpiaparabrisas, frenos y testigos del cuadro. Lleva el permiso de circulación y la tarjeta ITV. ¿Vas a comprar un coche usado? Mira su <a href="historial-coche-matricula.html">historial por matrícula</a> y su <a href="etiqueta-dgt.html">etiqueta DGT</a>.</p>""",
[("¿Cuándo hay que pasar la primera ITV?", "Un coche particular, a los 4 años de su primera matriculación; las motos y quads, también a los 4 años; los ciclomotores, a los 3 años."),
 ("¿Cada cuánto se pasa la ITV un coche de más de 10 años?", "Cada año. Entre los 4 y los 10 años de antigüedad se pasa cada dos años, y a partir del décimo aniversario de la matriculación, anualmente."),
 ("¿Puedo pasar la ITV antes de que caduque?", "Sí. Si la pasas en los 30 días naturales anteriores a la caducidad, la fecha de la siguiente se mantiene como si la hubieras pasado el último día. Si la adelantas más, la siguiente se cuenta desde el día en que la pases."),
 ("¿Qué multa hay por llevar la ITV caducada?", "200 € por circular con la ITV caducada. Si la última inspección tuvo resultado negativo, la sanción puede llegar a 500 €. No se pierden puntos.")],
"¿Cuándo me toca pasar la ITV?",
"""const pd=id=>{const s=document.getElementById(id).value;if(!s)return null;const [y,m,d]=s.split('-').map(Number);return new Date(y,m-1,d);};
const fmt=d=>d.toLocaleDateString('es-ES',{weekday:'long',day:'numeric',month:'long',year:'numeric'}),fc=d=>d.toLocaleDateString('es-ES',{day:'numeric',month:'short',year:'numeric'});
const iso=d=>d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');document.querySelectorAll('input[type=date][data-today]').forEach(e=>e.value=iso(new Date()));
const dd=(a,b)=>Math.round((Date.UTC(b.getFullYear(),b.getMonth(),b.getDate())-Date.UTC(a.getFullYear(),a.getMonth(),a.getDate()))/864e5);
const addY=(d,n)=>{const x=new Date(d.getFullYear()+n,d.getMonth(),d.getDate());if(x.getDate()!=d.getDate())x.setDate(0);return x;};
function sched(t,m,n){const r=[];if(t=='c'){for(const y of [4,6,8,10])r.push([addY(m,y),y]);for(let y=11;r.length<n+40;y++)r.push([addY(m,y),y]);}else{const f=t=='k'?3:4;for(let y=f;r.length<n+40;y+=2)r.push([addY(m,y),y]);}return r;}
function step(t,m,d){const y=d.getFullYear()-m.getFullYear();return t=='c'&&y>=10?1:2;}
function calc(){const t=document.getElementById('t').value,m=pd('a'),h=pd('h')||new Date(),u=pd('u');if(!m){show('r','Escribe la fecha de primera matriculación.');return;}if(m>h){show('r','La fecha de matriculación tiene que ser anterior a hoy.');return;}
let L;if(u){L=[[u,u.getFullYear()-m.getFullYear()]];for(let i=0;i<8;i++){const p=L[L.length-1][0],s=step(t,m,p);const x=addY(p,s);L.push([x,x.getFullYear()-m.getFullYear()]);}}else L=sched(t,m,8);
const nx=L.find(x=>dd(h,x[0])>=0)||L[L.length-1],pv=L.filter(x=>dd(h,x[0])<0),last=pv[pv.length-1],f=dd(h,nx[0]),ini=new Date(nx[0]);ini.setDate(ini.getDate()-30);
const ant=new Date(h.getFullYear()-(h<new Date(h.getFullYear(),m.getMonth(),m.getDate())?1:0),m.getMonth(),m.getDate()),age=ant.getFullYear()-m.getFullYear();
let r='';if(u&&dd(h,u)<0){show('r','<b>Tu ITV caducó el '+fmt(u)+'.</b><br>Circular así puede costarte una multa de 200 €. Pide cita cuanto antes: como la pasarás tarde, la siguiente se contará desde el día de la inspección.');return;}
r+='Tu próxima ITV:<b class="big">'+fmt(nx[0])+'</b>';
r+=(f==0?'<b>Caduca hoy.</b> ':'Faltan <b>'+f+' días</b>. ')+'Puedes pasarla desde el <b>'+fc(ini)+'</b> sin perder días de validez.';
if(!u&&last&&dd(last[0],h)<=60&&dd(last[0],h)>0)r+='<br><b>Atención:</b> según la matriculación, te tocaba el '+fc(last[0])+'. Si no la has pasado, tu ITV está caducada y te pueden multar con 200 €: pide cita cuanto antes.';
r+='<br>Antigüedad: '+age+' años. ';const tt=t=='c'?'turismo':t=='m'?'moto o cuatriciclo':'ciclomotor';
if(t=='c')r+=age<4?'Hasta los 4 años un turismo no pasa la ITV.':age<10?'De los 4 a los 10 años, un turismo la pasa cada 2 años.':'Con más de 10 años, un turismo la pasa cada año.';else r+='Como '+tt+', la pasa cada 2 años'+(t=='k'?' desde los 3 años.':' desde los 4 años.');
const nxt=L.filter(x=>dd(h,x[0])>=0).slice(0,6);
r+='<table style="margin-top:12px;font-size:.92rem"><tr><th>ITV</th><th>Fecha límite</th><th>Desde</th></tr>'+nxt.map(x=>{const s=new Date(x[0]);s.setDate(s.getDate()-30);return '<tr><td>'+(x[1]>0?'A los '+x[1]+' años':'Actual')+'</td><td><b>'+fc(x[0])+'</b></td><td>'+fc(s)+'</td></tr>';}).join('')+'</table>';
show('r',r);}
document.querySelectorAll('.card input,.card select').forEach(e=>e.addEventListener(e.tagName=='SELECT'?'change':'input',()=>calc()));
calc();"""))

# --- Cuánto cuesta transferir un coche: ITP con el valor fiscal de Hacienda + tasa DGT ---
S['tools'].insert(3, ("transferencia-coche", "¿Cuánto cuesta transferir un coche?", "ITP con el valor fiscal de Hacienda, tasa de la DGT y total del cambio de nombre de un coche usado.", "Transferencia"))
S['aff']["transferencia-coche"] = SEG + ext(INFORME_URL, "Informe del historial antes de comprar") + amz("portadocumentos coche", "Portadocumentos para el coche")
P.append(("transferencia-coche", "Cuánto cuesta transferir un coche: calculadora de ITP y tasa DGT | CocheCuentas",
"Calcula cuánto cuesta el cambio de nombre de un coche de segunda mano: ITP sobre el valor fiscal de Hacienda o el precio de compra, tasa de la DGT de 55,70 € y gestoría. Con ejemplo y tabla por antigüedad.",
"""<p class="lead">Si compras un coche usado a un particular, el cambio de titularidad tiene dos gastos fijos: el <b>impuesto de transmisiones (ITP)</b> que pagas a tu comunidad y la <b>tasa de la DGT</b>. Mete el precio y la antigüedad del coche y te decimos cuánto pagarás en total.</p>
<div class="card"><div class="row"><div><label for="ve">¿A quién se lo compras?</label><select id="ve"><option value="p">A un particular</option><option value="e">A un concesionario o compraventa (con factura)</option></select></div>
<div><label for="tv">Tipo de vehículo</label><select id="tv"><option value="55.70">Coche, furgoneta o moto (tasa 55,70 €)</option><option value="27.85">Ciclomotor (tasa 27,85 €)</option></select></div>
<div><label for="pc">Precio de compra (€)</label><input id="pc" inputmode="decimal" value="8000"></div>
<div><label for="pn">Valor de tablas de Hacienda del modelo nuevo (€)</label><input id="pn" inputmode="decimal" value="22000"></div>
<div><label for="fm">Fecha de primera matriculación</label><input id="fm" type="date" value="2020-03-15"></div>
<div><label for="it">Tipo de ITP de tu comunidad (%)</label><input id="it" inputmode="decimal" value="4"></div>
<div><label for="ge">Gestoría (€, opcional)</label><input id="ge" inputmode="decimal" value="0"></div></div>
<button onclick="calc()">Calcular transferencia</button><div class="res" id="r" aria-live="polite"></div></div>
<p class="note">El valor de tablas es el «precio medio de venta» del modelo nuevo que publica Hacienda cada año en la Orden de precios medios (BOE). Lo encuentras en el programa de valoración de vehículos de la agencia tributaria de tu comunidad o en el propio modelo 620/621. La fecha de primera matriculación está en el permiso de circulación.</p>
<h2>Cómo se calcula el ITP de un coche usado</h2><p>Hacienda no se fía solo del precio que pones en el contrato. Calcula un <b>valor fiscal</b>: el precio medio del modelo nuevo × el porcentaje de su antigüedad. El impuesto se paga sobre la cantidad <b>mayor</b> entre ese valor y el precio de compra: <b>ITP = máx.(precio de compra, valor fiscal) × tipo de tu comunidad</b>. Si declaras un precio por debajo del valor de tablas, lo normal es que te llegue después una liquidación complementaria por la diferencia.</p>
<table><tr><th>Antigüedad</th><th>% del valor nuevo</th><th>Valor fiscal (modelo de 20.000 €)</th><th>ITP al 4 %</th></tr>
<tr><td>Hasta 1 año</td><td>100 %</td><td>20.000 €</td><td>800 €</td></tr>
<tr><td>Más de 1 y hasta 2</td><td>84 %</td><td>16.800 €</td><td>672 €</td></tr>
<tr><td>Más de 4 y hasta 5</td><td>47 %</td><td>9.400 €</td><td>376 €</td></tr>
<tr><td>Más de 7 y hasta 8</td><td>28 %</td><td>5.600 €</td><td>224 €</td></tr>
<tr><td>Más de 10 y hasta 11</td><td>17 %</td><td>3.400 €</td><td>136 €</td></tr>
<tr><td>Más de 12 años</td><td>10 %</td><td>2.000 €</td><td>80 €</td></tr></table>
<p class="note">Porcentajes de la tabla de antigüedad de la Orden de precios medios de venta de Hacienda: 100, 84, 67, 56, 47, 39, 34, 28, 24, 19, 17, 13 y 10 % a partir de 12 años.</p>
<p><b>Ejemplo:</b> compras por 8.000 € un compacto matriculado en marzo de 2020 cuyo modelo nuevo vale 22.000 € en las tablas. Con algo más de 6 años, Hacienda lo valora al 34 %: 7.480 €. Como pagaste más, el ITP se calcula sobre los 8.000 €: al 4 % son 320 €. Sumando la tasa de la DGT (55,70 €), el cambio de nombre te cuesta <b>375,70 €</b>, más la gestoría si no lo haces tú.</p>
<h2>¿Qué tipo de ITP aplica mi comunidad?</h2><p>El tipo general de la ley estatal para vehículos es el 4 %, y es el que ponemos por defecto, pero el ITP está cedido a las comunidades autónomas: varias aplican tipos distintos, y algunas tienen cuotas fijas o rebajas para coches antiguos o de poca cilindrada. Comprueba el tipo en la web de la agencia tributaria de la comunidad donde vives (es la del comprador, no la del vendedor) y escríbelo en la casilla.</p>
<h2>Pasos para hacer la transferencia</h2><ul><li><b>Contrato de compraventa</b> firmado por los dos, con fecha, precio, matrícula y bastidor.</li><li><b>Pago del ITP</b> con el modelo 620 o 621 de tu comunidad en el plazo de un mes desde la compra.</li><li><b>Tasa de la DGT</b> (55,70 € para turismos y motos; 27,85 € para ciclomotores) y solicitud de cambio de titularidad en la sede de la DGT, en una jefatura o con un gestor.</li><li>El vendedor debe <b>notificar la venta</b> a la DGT para que las multas y el impuesto de circulación dejen de llegarle.</li></ul>
<p>¿Necesitas el contrato? Rellena gratis el <a href="contrato-compraventa-coche.html">contrato de compraventa de coche</a> paso a paso, o el de <a href="contrato-senal-coche.html">señal o reserva</a> si aún no pagas todo. Antes de pagar, revisa el <a href="historial-coche-matricula.html">historial del coche por matrícula</a> y cuándo le toca la <a href="cuando-pasar-itv.html">próxima ITV</a>. Si vas a financiarlo, calcula la <a href="cuota-financiacion-coche.html">cuota del préstamo</a>, y mira cuánto <a href="depreciacion-coche.html">valdrá dentro de unos años</a>.</p>""",
[("¿Cuánto cuesta cambiar de nombre un coche de segunda mano?", "La tasa de la DGT (55,70 € en coches y motos) más el ITP, que en la mayoría de los casos es un porcentaje (el 4 % por defecto en la ley estatal) del precio de compra o del valor fiscal de Hacienda, el que sea mayor. En un coche de unos 8.000 € suele salir entre 350 y 400 € en total, más la gestoría si la usas."),
 ("¿Quién paga la transferencia del coche, el comprador o el vendedor?", "Salvo pacto en contrario, el ITP lo paga el comprador, que es quien adquiere el coche. La tasa de la DGT también la suele pagar el comprador, aunque se puede acordar otra cosa en el contrato."),
 ("¿Si compro en un concesionario pago ITP?", "No. Si el vendedor es un profesional que te da factura, la venta lleva IVA (ya incluido en el precio) y no pagas ITP. Solo pagas la tasa de la DGT, que muchas veces el concesionario incluye en el precio."),
 ("¿Qué pasa si pongo en el contrato un precio más bajo?", "El ITP se calcula sobre el mayor entre el precio declarado y el valor de tablas de Hacienda. Si declaras menos que ese valor, la comunidad puede reclamarte la diferencia con intereses.")],
"¿Cuánto cuesta transferir un coche?",
"""const DEP=[100,84,67,56,47,39,34,28,24,19,17,13,10];
function calc(){const e=document.getElementById('ve').value=='e',ta=parseFloat(document.getElementById('tv').value),pc=v('pc'),pn=v('pn'),it=v('it'),ge=v('ge');
const s=document.getElementById('fm').value;let a=0;if(s){const [y,m,d]=s.split('-').map(Number);a=(Date.now()-new Date(y,m-1,d))/31557600000;}if(a<0)a=0;
const i=a<=1?0:Math.min(12,Math.ceil(a)-1),p=DEP[i],vf=pn*p/100,base=Math.max(pc,vf),itp=e?0:base*it/100,tot=itp+ta+ge;
let h='Coste total de la transferencia:<b class="big">'+eur(tot)+'</b>';
if(e)h+='Compra a un profesional: <b>sin ITP</b> (la venta lleva IVA en la factura) · Tasa DGT: '+eur(ta)+(ge>0?' · Gestoría: '+eur(ge):'');
else{h+='ITP: <b>'+eur(itp)+'</b> · Tasa DGT: '+eur(ta)+(ge>0?' · Gestoría: '+eur(ge):'');
h+='<br>Antigüedad: '+nf(a,1)+' años → Hacienda lo valora al <b>'+p+' %</b> del modelo nuevo: valor fiscal '+eur(vf)+'.';
if(pn<=0)h+='<br>Sin valor de tablas, calculamos sobre el precio de compra.';
else if(pc<vf)h+='<br>Tu precio ('+eur(pc)+') es menor que el valor fiscal: el ITP se calcula sobre <b>'+eur(vf)+'</b>. Si lo declaras por el precio, podrían reclamarte '+eur((vf-pc)*it/100)+' más.';
else h+='<br>El precio de compra es mayor que el valor fiscal: el ITP se calcula sobre el precio, <b>'+eur(pc)+'</b>.';}
show('r',h);}
document.querySelectorAll('.card input,.card select').forEach(x=>x.addEventListener(x.tagName=='SELECT'?'change':'input',()=>calc()));
calc();"""))

# --- Portada: accesos a lo más buscado en temporada (Navidad e invierno) ---
S['home_intro'] += '<nav class="share" aria-label="Lo más buscado estos días"><span>Lo más buscado estos días:</span><a href="gasolineras-baratas.html">Gasolineras baratas</a><a href="coste-viaje-coche.html">Gasolina del viaje</a><a href="calculadora-alcoholemia.html">Alcoholemia</a><a href="distancia-frenado.html">Frenado con hielo</a><a href="etiqueta-dgt.html">Etiqueta DGT</a></nav>'

# --- Radar de tramo: velocidad media, multa y tiempo mínimo para no ser multado ---
S['tools'].insert(7, ("radar-de-tramo", "Calculadora de radar de tramo", "Tu velocidad media entre dos arcos, si te multan y el tiempo mínimo para pasar el tramo sin sanción.", "Radar de tramo"))
S['aff']["radar-de-tramo"] = amz("navegador gps coche avisador radares", "Navegadores GPS con aviso de radares") + amz("soporte movil coche", "Soportes de móvil para el coche")
P.append(("radar-de-tramo", "Radar de tramo: calculadora de velocidad media y multa | CocheCuentas",
"Calcula tu velocidad media en un radar de tramo con los km y el tiempo entre arcos, con el margen del radar descontado: multa, puntos y tiempo mínimo sin sanción.",
"""<p class="lead">Un radar de tramo no mide la velocidad en un punto: mide cuánto tardas entre dos arcos y calcula tu <b>velocidad media</b>. Pon la longitud del tramo y el tiempo que tardaste y te decimos si te multarían, cuánto y en cuántos minutos tienes que recorrerlo para ir tranquilo.</p>
<div class="card"><div class="row"><div><label for="km">Longitud del tramo (km)</label><input id="km" inputmode="decimal" value="10"></div>
<div><label for="l">Límite del tramo (km/h)</label><select id="l"><option>50</option><option>60</option><option>70</option><option>80</option><option>90</option><option>100</option><option>110</option><option selected>120</option></select></div>
<div><label for="mi">Tiempo: minutos</label><input id="mi" inputmode="numeric" value="4"></div>
<div><label for="se">Tiempo: segundos</label><input id="se" inputmode="numeric" value="30"></div></div>
<button onclick="calc()">Calcular velocidad media</button><div class="res" id="r" aria-live="polite"></div></div>
<p class="note">La longitud de cada tramo suele aparecer en la señal que lo anuncia y en el listado de radares de la DGT. Si no sabes el tiempo exacto, la calculadora te dice el mínimo para no pasar del límite.</p>
<h2>Cómo calcula la multa un radar de tramo</h2><p>Velocidad media = distancia ÷ tiempo. Si recorres 10 km en 4 minutos y 30 segundos (0,075 horas), tu media es de 133,3 km/h. Al ser un cinemómetro fijo, se descuenta el <b>margen de error legal de 5 km/h hasta 100 km/h y del 5 % por encima</b> (Orden ICT/155/2020): 133,3 − 6,7 = 126,6, que se redondea a la baja, <b>126 km/h</b>. En una vía de 120 son 6 km/h de exceso: <b>100 € sin pérdida de puntos</b> (50 € con pronto pago).</p>
<table><tr><th>Tramo de 10 km a 120 km/h</th><th>Velocidad media</th><th>Resultado</th></tr>
<tr><td>5 min 0 s</td><td>120 km/h</td><td>Sin multa</td></tr>
<tr><td>4 min 45 s</td><td>126,3 km/h</td><td>Sin multa (120 km/h corregidos)</td></tr>
<tr><td>4 min 40 s</td><td>128,6 km/h</td><td>122 km/h corregidos: 100 €</td></tr>
<tr><td>4 min 0 s</td><td>150 km/h</td><td>142 km/h corregidos: 100 €</td></tr>
<tr><td>3 min 30 s</td><td>171,4 km/h</td><td>162 km/h corregidos: 300 € y 2 puntos</td></tr></table>
<h2>Lo que conviene saber</h2><ul><li><b>Frenar justo antes del arco no sirve:</b> cuenta la media de todo el tramo, y en muchos tramos el arco también lleva un radar de punto que mide la velocidad instantánea.</li><li><b>Parar dentro del tramo baja la media</b>, pero lo que importa es no superar el límite en ningún punto.</li><li>La multa sigue la misma tabla que cualquier radar: grave a partir de 1 km/h de exceso corregido y pérdida de puntos desde 31 km/h por encima en vías de 60 o más.</li></ul>
<p>Si ya tienes la notificación con la velocidad de un radar de punto, usa la <a href="multa-exceso-velocidad.html">calculadora de multas por exceso de velocidad</a>. ¿Te vas de viaje estas fiestas? Calcula la <a href="coste-viaje-coche.html">gasolina del viaje</a>, busca las <a href="gasolineras-baratas.html">gasolineras más baratas</a> y revisa la <a href="distancia-frenado.html">distancia de frenado con lluvia o hielo</a>.</p>""",
[("¿Cómo se calcula la velocidad en un radar de tramo?", "Se divide la distancia entre los dos arcos por el tiempo que tardas en recorrerla. Por ejemplo, 10 km en 5 minutos son 120 km/h de media. Después se descuenta el margen del radar (5 km/h hasta 100 km/h y 5 % por encima) y se redondea a la baja."),
 ("¿Cuál es el margen de un radar de tramo?", "El mismo que un radar fijo: 5 km/h si la velocidad medida es de hasta 100 km/h y un 5 % si es mayor. En un tramo de 120, la multa empieza a partir de unos 127,4 km/h de media."),
 ("¿Cuánto tiempo hay que tardar en un tramo de 10 km a 120?", "Al menos 5 minutos para ir exactamente a 120 km/h de media. Con el margen del radar no habría multa hasta bajar de unos 4 min 43 s, pero lo seguro es no superar el límite en ningún momento."),
 ("¿Me pueden multar dos veces en el mismo tramo?", "Por la misma infracción de velocidad media, no: el tramo genera una sola denuncia. Pero si el arco tiene además un radar de punto y lo superas allí, es una medición distinta.")],
"Calculadora de radar de tramo",
"""function calc(){const km=v('km'),L=+document.getElementById('l').value,t=(v('mi')*60+v('se'))/3600;
if(km<=0){show('r','Escribe la longitud del tramo en km.');return;}
const tm=km/L*3600,tmin=Math.floor(tm/60)+' min '+Math.round(tm%60)+' s';
if(t<=0){show('r','Para ir a '+L+' km/h de media necesitas al menos <b>'+tmin+'</b> en este tramo.');return;}
const vm=km/t,mg=vm>100?vm*0.05:5,vc=Math.floor(vm-mg+1e-9),ex=vc-L;
const lim=L<=50?[20,30,40,50]:[30,50,60,70],del=L<=50?60:80;
let mu=0,pt=0,g='';if(ex>0){if(ex<=lim[0]){mu=100;}else if(ex<=lim[1]){mu=300;pt=2;}else if(ex<=lim[2]){mu=400;pt=4;}else if(ex<=lim[3]){mu=500;pt=6;}else{mu=600;pt=6;g='muy grave';}}
let h='Tu velocidad media:<b class="big">'+nf(vm,1)+' km/h</b>Con el margen del radar ('+(vm>100?'5 %':'5 km/h')+'): <b>'+vc+' km/h</b> corregidos en una vía de '+L+'.';
if(ex<=0)h+='<br><b>Sin multa.</b>';
else{h+='<br>Exceso de '+ex+' km/h: multa <b>'+mu+' €</b> ('+(mu/2)+' € con pronto pago)'+(pt?' y <b>'+pt+' puntos</b>':', sin perder puntos')+(g?' · infracción muy grave':'')+'.';if(ex>del)h+='<br><b>Atención:</b> superar el límite en más de '+del+' km/h es delito.';}
h+='<br>Tiempo mínimo para ir a '+L+' km/h de media: <b>'+tmin+'</b>.';show('r',h);}
document.querySelectorAll('.card input,.card select').forEach(x=>x.addEventListener(x.tagName=='SELECT'?'change':'input',()=>calc()));
calc();"""))

# =====================================================================
# --- Sección CONTRATOS: compraventa de coche (3 tipos) y señal/reserva, rellenables paso a paso ---
# =====================================================================
CSS_DOC = """<style>.st{border:0;padding:0;margin:0;min-width:0;display:none}.st.on{display:block}.st legend{font-weight:800;font-size:1.1rem;padding:0;margin-bottom:4px}
.pasos{display:flex;gap:4px;margin:0 0 14px}.pasos span{flex:1;height:6px;border-radius:3px;background:#e5e7ef}.pasos span.ok{background:#d9480f}
.navb{display:flex;gap:10px}.navb button{flex:1}.navb .sec{background:#fff;color:#d9480f;border:1px solid #d9480f}
.doc{background:#fff;border:1px solid #e5e7ef;border-radius:8px;padding:22px 18px;font-family:Georgia,'Times New Roman',serif;font-size:.93rem;line-height:1.6;color:#111;text-align:justify;overflow-wrap:anywhere}
.doc h3{text-align:center;font-size:1.05rem;margin:0 0 4px}.doc .sub{text-align:center;margin:0 0 14px;font-style:italic}.doc h4{text-align:center;font-size:.95rem;margin:16px 0 6px;letter-spacing:1px}
.doc .bl{color:#c92a2a;font-family:system-ui,sans-serif;font-size:.85em}.doc .fir{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:40px;text-align:center}.doc .fir div{border-top:1px solid #111;padding-top:6px}
.avisoc{margin:0 0 12px;padding:10px 12px;border-radius:8px;background:#fff4e6;font-size:.9rem}
@media print{body *{visibility:hidden!important}#doc,#doc *{visibility:visible!important}#doc{position:absolute;left:0;top:0;width:100%;border:0;padding:0;font-size:11pt}.doc .bl{color:#111}}@page{margin:2cm}</style>"""

CJS = r"""const $=id=>document.getElementById(id),val=id=>{const e=$(id);return e?String(e.value).trim():'';};
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const B=(s,w)=>s?esc(s):'<span class="bl">'+'_'.repeat(w||18)+'</span>';
const F=s=>{if(!s)return '';const [y,m,d]=s.split('-').map(Number);return new Date(y,m-1,d).toLocaleDateString('es-ES',{day:'numeric',month:'long',year:'numeric'});};
const num=id=>parseFloat(val(id).replace(/\./g,'').replace(',','.'))||0;
const E=n=>n.toLocaleString('es-ES',{minimumFractionDigits:2,maximumFractionDigits:2})+' €';
function letras(x){const U=['','uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez','once','doce','trece','catorce','quince','dieciséis','diecisiete','dieciocho','diecinueve','veinte','veintiuno','veintidós','veintitrés','veinticuatro','veinticinco','veintiséis','veintisiete','veintiocho','veintinueve'],
D=['','','','treinta','cuarenta','cincuenta','sesenta','setenta','ochenta','noventa'],C=['','ciento','doscientos','trescientos','cuatrocientos','quinientos','seiscientos','setecientos','ochocientos','novecientos'];
const ap=s=>s.replace(/veintiuno$/,'veintiún').replace(/ uno$/,' un').replace(/^uno$/,'un');
const c=n=>{if(n==100)return 'cien';let s='';if(n>=100){s=C[Math.floor(n/100)];n%=100;if(n)s+=' ';}if(n<30)s+=U[n];else{s+=D[Math.floor(n/10)];if(n%10)s+=' y '+U[n%10];}return s;};
const ent=n=>{if(n===0)return 'cero';let s='';const mi=Math.floor(n/1e6),ml=Math.floor(n%1e6/1000),r=n%1000;
if(mi)s+=(mi==1?'un millón':ap(c(mi))+' millones')+' ';if(ml)s+=(ml==1?'mil':ap(c(ml))+' mil')+' ';if(r)s+=c(r);return s.trim();};
const e=Math.floor(x+1e-9),ct=Math.round((x-e)*100);const w=ap(ent(e));return (w+(e==1?' euro':(e>=1e6&&e%1e6==0?' de euros':' euros'))+(ct?' con '+ap(c(ct))+' céntimos':'')).toUpperCase();}
const IMP=n=>n>0?'<b>'+E(n)+'</b> ('+letras(n)+')':B('',12)+' euros';
let PASO=0;const ST=[...document.querySelectorAll('.st')];
function paso(n){PASO=Math.max(0,Math.min(ST.length-1,n));ST.forEach((s,i)=>s.classList.toggle('on',i==PASO));
$('pasos').innerHTML=ST.map((s,i)=>'<span class="'+(i<=PASO?'ok':'')+'"></span>').join('');
$('pt').textContent='Paso '+(PASO+1)+' de '+ST.length+': '+ST[PASO].querySelector('legend').textContent;
$('bant').style.visibility=PASO?'visible':'hidden';$('bsig').textContent=PASO==ST.length-1?'Imprimir o guardar en PDF':'Siguiente';}
function sig(){if(PASO==ST.length-1){imprimir();return;}paso(PASO+1);const c=$('pt');if(c&&c.scrollIntoView)c.scrollIntoView({block:'nearest'});}
function imprimir(){calc();window.print();}
function word(nom){calc();const h='<html><head><meta charset="utf-8"><title>'+nom+'</title></head><body style="font-family:Georgia,serif;font-size:11pt;line-height:1.5;text-align:justify">'+$('doc').innerHTML.replace(/<span class="bl">(_+)<\/span>/g,'$1')+'</body></html>';
const a=document.createElement('a');a.href=URL.createObjectURL(new Blob(['﻿',h],{type:'application/msword'}));a.download=nom+'.doc';document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove();},500);}
const iso=d=>d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');
document.querySelectorAll('input[type=date][data-today]').forEach(x=>x.value=iso(new Date()));
"""

def _parte(p, quien):
    return f"""<fieldset class="st"><legend>{quien}</legend>
<div class="row"><div><label for="{p}n" id="{p}nl">Nombre y apellidos</label><input id="{p}n" autocomplete="off"></div>
<div><label for="{p}d" id="{p}dl">DNI o NIE</label><input id="{p}d" autocomplete="off" autocapitalize="characters"></div></div>
<label for="{p}o">Domicilio (calle, número, localidad y provincia)</label><input id="{p}o" autocomplete="off">
<div class="pro" id="{p}rw" style="display:none"><label for="{p}r">Representante de la empresa (nombre, DNI y cargo)</label><input id="{p}r" autocomplete="off"></div></fieldset>"""

VEH = """<fieldset class="st"><legend>Vehículo</legend><div class="row">
<div><label for="ma">Marca</label><input id="ma" autocomplete="off"></div><div><label for="mo">Modelo y versión</label><input id="mo" autocomplete="off"></div>
<div><label for="mt">Matrícula</label><input id="mt" autocomplete="off" autocapitalize="characters" placeholder="1234 KLM"></div><div><label for="bs">Número de bastidor (VIN, 17 caracteres)</label><input id="bs" autocomplete="off" autocapitalize="characters" maxlength="17"></div>
<div><label for="fm">Fecha de primera matriculación</label><input id="fm" type="date"></div><div><label for="km">Kilómetros actuales</label><input id="km" inputmode="numeric"></div></div>
<p class="note">El bastidor y la fecha de primera matriculación vienen en el permiso de circulación y en la ficha técnica. ¿Quieres comprobar el coche antes? Consulta su <a href="historial-coche-matricula.html">historial por matrícula</a>.</p></fieldset>"""

NAVB = """<p class="note" id="pt" style="margin:0 0 6px;font-weight:600"></p><div class="pasos" id="pasos"></div>{steps}
<div class="navb"><button type="button" class="sec" id="bant" onclick="paso(PASO-1)">Anterior</button><button type="button" id="bsig" onclick="sig()">Siguiente</button></div>
<div class="navb"><button type="button" class="sec" onclick="imprimir()">Imprimir o PDF</button><button type="button" class="sec" onclick="word({wn})">Descargar en Word</button></div>"""

# ---------- 1) Contrato de compraventa de coche ----------
S['tools'].append(("contrato-compraventa-coche", "Contrato de compraventa de coche", "Modelo rellenable paso a paso: entre particulares, venta a una compraventa o de profesional a particular. Listo para imprimir o en PDF.", "Contrato"))
S['aff']["contrato-compraventa-coche"] = ext(INFORME_URL, "Informe del historial antes de comprar") + SEG + amz("portadocumentos coche", "Portadocumentos para el coche")
_st_cv = ("""<fieldset class="st"><legend>Tipo de contrato</legend>
<label for="t">¿Quién vende y quién compra?</label><select id="t"><option value="pp">Entre particulares</option><option value="pv">Un particular vende a una compraventa o concesionario</option><option value="vp">Una compraventa o concesionario vende a un particular</option></select>
<div class="row"><div><label for="ci">Lugar de la firma (localidad)</label><input id="ci" autocomplete="off"></div><div><label for="fe">Fecha</label><input id="fe" type="date" data-today></div></div>
<label for="ho">Hora de la entrega (desde ella el comprador responde de multas y accidentes)</label><input id="ho" type="time" value="12:00"></fieldset>"""
+ _parte("v", "Vendedor") + _parte("c", "Comprador") + VEH +
"""<fieldset class="st"><legend>Precio y pago</legend><div class="row">
<div><label for="pr">Precio total (€)</label><input id="pr" inputmode="decimal"></div>
<div><label for="fp">Forma de pago</label><select id="fp"><option value="tr">Transferencia bancaria</option><option value="ch">Cheque bancario o conformado</option><option value="ef">Efectivo</option><option value="fi">Financiación (préstamo de una entidad)</option></select></div>
<div><label for="sn">Señal ya entregada (€, opcional)</label><input id="sn" inputmode="decimal" value="0"></div>
<div><label for="gt">Impuestos y tasa de la transferencia a cargo de</label><select id="gt"><option value="c">El comprador (lo habitual)</option><option value="v">El vendedor</option><option value="m">Ambos, a partes iguales</option></select></div></div>
<p class="note">Si compras a un particular pagarás el ITP de tu comunidad y la tasa de la DGT: <a href="transferencia-coche.html">calcula cuánto cuesta la transferencia</a>.</p></fieldset>
<fieldset class="st"><legend>Estado y entrega</legend>
<label for="de">Defectos o daños conocidos (déjalo vacío si no hay)</label><textarea id="de" rows="3" placeholder="Por ejemplo: arañazo en la puerta trasera derecha; aire acondicionado sin carga"></textarea>
<div class="row"><div><label for="iv">ITV en vigor hasta</label><input id="iv" type="date"></div><div><label for="ll">Número de llaves que se entregan</label><input id="ll" inputmode="numeric" value="2"></div></div>
<label class="chk"><input type="checkbox" id="lm" checked><span>Se entrega el libro de mantenimiento o las facturas de revisiones</span></label>
<div class="pro" id="gaw" style="display:none"><label for="ga">Garantía (meses, mínimo 12 por ley)</label><input id="ga" inputmode="numeric" value="12"></div></fieldset>
<fieldset class="st"><legend>Revisar y descargar</legend><p>Revisa el contrato de abajo. Lo que sale <span style="color:#c92a2a">en rojo</span> está sin rellenar. Imprime dos copias (o guárdalo en PDF) y firmad las dos, una para cada parte.</p></fieldset>""")
P.append(("contrato-compraventa-coche", "Contrato de compraventa de coche entre particulares: modelo para rellenar | CocheCuentas",
"Modelo de contrato de compraventa de vehículo para rellenar paso a paso: entre particulares, venta a una compraventa o de concesionario a particular. Con señal, cargas, multas y vicios ocultos. Gratis, en PDF o Word.",
CSS_DOC + """<p class="lead">Rellena los datos paso a paso y el contrato se escribe solo, abajo, mientras escribes. Al final lo imprimes, lo guardas en PDF o lo descargas en Word para editarlo. Elige el tipo: <b>entre particulares</b>, <b>un particular que vende a una compraventa</b> o <b>una compraventa que vende a un particular</b>.</p>
<div class="card">""" + NAVB.format(steps=_st_cv, wn="'contrato-compraventa-'+(val('mt').replace(/\\s/g,'')||'coche')") + """
<div class="res" id="r" style="background:none;padding:0;margin-top:18px"></div></div>
<p class="note">Todo se hace en tu navegador: los nombres, DNI y datos que escribes no se envían ni se guardan en ningún servidor. Es un modelo orientativo basado en la normativa general; para casos especiales (herencias, vehículos con reserva de dominio, empresas) consulta con una gestoría o un abogado.</p>
<h2>Qué tiene que llevar un contrato de compraventa de coche</h2><ul><li><b>Datos completos de las dos partes</b>: nombre, DNI o NIE y domicilio. Si una es empresa, su NIF y quién firma en su nombre.</li><li><b>Identificación del coche</b>: marca, modelo, matrícula, número de bastidor y kilómetros.</li><li><b>Precio y forma de pago</b>, y si ya se ha dado una señal.</li><li><b>Fecha y hora de la entrega</b>: desde ese momento las multas, los accidentes y el seguro son cosa del comprador. Por eso conviene escribir la hora.</li><li><b>Estado del coche y defectos conocidos</b>, que protegen a las dos partes si luego hay una reclamación.</li><li><b>Cargas</b>: el vendedor declara que el coche no tiene embargos ni reservas de dominio. Compruébalo antes con un informe de la DGT.</li></ul>
<h2>Particular, compraventa o concesionario: qué cambia</h2><p><b>Entre particulares</b> no hay garantía de la ley de consumo: el vendedor solo responde de los <b>vicios ocultos</b> (defectos graves que no se podían ver y que ya existían), y la acción para reclamar caduca a los <b>6 meses</b> de la entrega (artículos 1484 y 1490 del Código Civil). El comprador paga el ITP de su comunidad.</p>
<p><b>Si vende una compraventa o un concesionario</b> a un particular, se aplica la ley de consumidores: tiene que dar una garantía de al menos <b>1 año</b> en coches de segunda mano, emitir factura y no puede cobrar más de <b>1.000 € en efectivo</b> (Ley 11/2021). El comprador no paga ITP porque la venta ya lleva sus impuestos. <b>Si un particular vende a una compraventa</b>, el profesional es quien compra: el contrato sirve como justificante y para que conste la hora a partir de la cual el coche deja de ser tuyo.</p>
<h2>Después de firmar</h2><p>El comprador tiene que pedir el <b>cambio de titularidad</b> en la DGT (tasa de 55,70 €) con el contrato, el permiso de circulación y el justificante del ITP. Si eres el vendedor, haz una <b>notificación de venta</b> a la DGT para que conste la fecha y no te lleguen multas del nuevo dueño. Antes de comprar, revisa la <a href="cuando-pasar-itv.html">fecha de la próxima ITV</a>, la <a href="etiqueta-dgt.html">etiqueta DGT</a> y, si pides un préstamo, la <a href="cuota-financiacion-coche.html">cuota de la financiación</a>. ¿Vas a reservar el coche con una señal antes de pagarlo entero? Usa el <a href="contrato-senal-coche.html">contrato de señal o reserva</a>.</p>""",
[("¿Es obligatorio hacer un contrato para vender un coche?", "Para hacer la transferencia en la DGT hace falta un documento que acredite la venta: entre particulares es el contrato de compraventa firmado por los dos; si vende una empresa, vale la factura. Además, el contrato con fecha y hora te protege de multas o accidentes posteriores a la venta."),
 ("¿Quién paga el impuesto al comprar un coche de segunda mano?", "Entre particulares, salvo pacto en contrario, el comprador paga el impuesto de transmisiones (ITP) a su comunidad y la tasa de la DGT. Si compras a un profesional con factura no hay ITP, solo la tasa."),
 ("¿Puedo pagar un coche en efectivo?", "Entre particulares no hay un límite general, aunque es recomendable la transferencia para que quede constancia. Si una de las partes es una empresa o profesional, el pago en efectivo está limitado a 1.000 € (Ley 11/2021)."),
 ("¿Qué pasa si el coche tiene una avería después de comprarlo a un particular?", "Solo puedes reclamar si es un vicio oculto: un defecto grave que ya existía, que no se podía ver al revisarlo y que el contrato no recogía. Tienes 6 meses desde la entrega. Por eso conviene escribir en el contrato los defectos que sí se conocen.")],
"Contrato de compraventa de coche",
CJS + r"""const TT={pp:'ENTRE PARTICULARES',pv:'DE PARTICULAR A PROFESIONAL DE LA COMPRAVENTA DE VEHÍCULOS',vp:'DE PROFESIONAL A CONSUMIDOR'};
function parte(p,rol,pro){const n=val(p+'n'),d=val(p+'d'),o=val(p+'o'),r=val(p+'r');
return pro?'<b>'+B(n,26)+'</b>, con NIF '+B(d,12)+' y domicilio social en '+B(o,30)+', representada en este acto por '+B(r,26)+', como <b>'+rol+'</b>.'
:'D./D.ª <b>'+B(n,26)+'</b>, mayor de edad, con DNI/NIE '+B(d,12)+' y domicilio en '+B(o,30)+', como <b>'+rol+'</b>.';}
function calc(){const t=val('t'),pv=t=='pv',vp=t=='vp';
$('vrw').style.display=vp?'block':'none';$('crw').style.display=pv?'block':'none';$('gaw').style.display=vp?'block':'none';
$('vnl').textContent=vp?'Razón social de la empresa':'Nombre y apellidos';$('vdl').textContent=vp?'NIF de la empresa':'DNI o NIE';
$('cnl').textContent=pv?'Razón social de la empresa':'Nombre y apellidos';$('cdl').textContent=pv?'NIF de la empresa':'DNI o NIE';
const pr=num('pr'),sn=Math.min(num('sn'),pr),fp=val('fp'),bs=val('bs').toUpperCase(),ga=Math.max(12,parseInt(val('ga'))||12),de=val('de'),gt=val('gt');
const FP={tr:'transferencia bancaria a la cuenta del VENDEDOR',ch:'cheque bancario o conformado a nombre del VENDEDOR',ef:'dinero en efectivo',fi:'financiación concedida al COMPRADOR por una entidad financiera, que abonará el importe directamente al VENDEDOR'}[fp];
let av=[];if(bs&&bs.length!=17)av.push('El número de bastidor (VIN) tiene '+bs.length+' caracteres; debería tener 17. Cópialo del permiso de circulación.');
if(fp=='ef'&&t!='pp'&&pr-sn>1000)av.push('Si una de las partes es una empresa, no se pueden pagar más de 1.000 € en efectivo (Ley 11/2021). Elige transferencia o cheque.');
if(vp&&(parseInt(val('ga'))||0)<12)av.push('Un profesional debe dar al menos 12 meses de garantía en un coche usado; el contrato pone 12.');
let h=(av.length?'<div class="avisoc">'+av.join('<br>')+'</div>':'')+'<div class="doc" id="doc"><h3>CONTRATO DE COMPRAVENTA DE VEHÍCULO</h3><p class="sub">'+TT[t]+'</p>';
h+='<p>En '+B(val('ci'),16)+', a '+(F(val('fe'))||B('',16))+', a las '+B(val('ho'),5)+' horas.</p><h4>REUNIDOS</h4>';
h+='<p>De una parte, '+parte('v','VENDEDOR',vp)+'</p><p>De otra parte, '+parte('c','COMPRADOR',pv)+'</p>';
h+='<p>Ambas partes se reconocen mutuamente la capacidad legal necesaria para obligarse en este contrato y</p><h4>ACUERDAN</h4>';
h+='<p><b>PRIMERA. Objeto.</b> El VENDEDOR vende al COMPRADOR, que lo compra, el vehículo marca '+B(val('ma'),12)+', modelo '+B(val('mo'),18)+', matrícula <b>'+B(val('mt').toUpperCase(),10)+'</b>, número de bastidor '+B(bs,20)+', con fecha de primera matriculación '+(F(val('fm'))||B('',14))+' y '+B(val('km'),8)+' kilómetros en el cuentakilómetros, que el VENDEDOR declara reales según su leal saber.</p>';
h+='<p><b>SEGUNDA. Precio y forma de pago.</b> El precio de la compraventa es de '+IMP(pr)+(vp?', impuestos indirectos incluidos, por el que el VENDEDOR emitirá la correspondiente factura':'')+'. ';
if(sn>0)h+='El COMPRADOR entregó con anterioridad '+IMP(sn)+' en concepto de señal, que se descuenta del precio, y abona el resto, '+IMP(pr-sn)+', mediante '+FP+'. ';else h+='El COMPRADOR lo abona mediante '+FP+'. ';
h+=fp=='fi'?'El VENDEDOR no estará obligado a entregar el vehículo hasta haber recibido el precio íntegro.</p>':'El VENDEDOR declara haber recibido el importe a su satisfacción, y este documento sirve como carta de pago.</p>';
h+='<p><b>TERCERA. Estado del vehículo.</b> El COMPRADOR declara haber examinado y probado el vehículo y lo acepta en el estado en que se encuentra. El VENDEDOR declara que no conoce defectos ocultos'+(de?' distintos de los siguientes, que el COMPRADOR conoce y acepta: '+esc(de)+'.':'.')+' La inspección técnica (ITV) está en vigor hasta el '+(F(val('iv'))||B('',14))+'.</p>';
h+='<p><b>CUARTA. Cargas.</b> El VENDEDOR declara que el vehículo es de su propiedad, que está libre de cargas, embargos, reservas de dominio y de cualquier otra limitación que impida su venta, y que está al corriente del pago del Impuesto sobre Vehículos de Tracción Mecánica. Responderá frente al COMPRADOR de cualquier carga, deuda o sanción anterior a la fecha y hora de este contrato.</p>';
h+='<p><b>QUINTA. Entrega y documentación.</b> En este acto el VENDEDOR entrega el vehículo junto con el permiso de circulación, la tarjeta de inspección técnica, '+B(val('ll'),2)+' llave(s)'+($('lm').checked?' y el libro de mantenimiento o las facturas de las revisiones':'')+'.</p>';
h+='<p><b>SEXTA. Responsabilidad desde la entrega.</b> Desde la fecha y hora indicadas en este contrato, el COMPRADOR asume la responsabilidad civil, administrativa y de cualquier otro tipo derivada de la propiedad y la circulación del vehículo, incluidas las sanciones de tráfico, y se obliga a tenerlo asegurado. Las anteriores a ese momento corresponden al VENDEDOR.</p>';
const GT={c:'del COMPRADOR',v:'del VENDEDOR',m:'de ambas partes por mitades'}[gt];
h+='<p><b>SÉPTIMA. Transferencia y gastos.</b> '+(pv?'El COMPRADOR, como profesional de la compraventa de vehículos, realizará los trámites de comunicación de la adquisición ante la Dirección General de Tráfico conforme a la normativa aplicable.':'El COMPRADOR solicitará el cambio de titularidad ante la Dirección General de Tráfico en el plazo de treinta días desde la firma de este contrato.')+' Los impuestos que graven esta compraventa y las tasas de la transferencia serán a cargo '+GT+'. El VENDEDOR podrá notificar la venta a la Dirección General de Tráfico.</p>';
h+='<p><b>OCTAVA. Garantía.</b> '+(vp?'El VENDEDOR, como empresario, responde de las faltas de conformidad del vehículo que se manifiesten en un plazo de <b>'+ga+' meses</b> desde la entrega, conforme al texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios y otras leyes complementarias.':'Al no actuar el VENDEDOR como empresario, no se aplica la garantía de la normativa de consumo. El VENDEDOR responde únicamente de los vicios o defectos ocultos conforme a los artículos 1484 y siguientes del Código Civil, con el plazo de seis meses desde la entrega previsto en su artículo 1490.')+'</p>';
h+='<p><b>NOVENA. Ley aplicable.</b> Este contrato se rige por la legislación española. Para cualquier controversia, las partes se someten a los juzgados y tribunales que resulten competentes conforme a la ley.</p>';
h+='<p>Y en prueba de conformidad, firman este contrato por duplicado y a un solo efecto en el lugar y la fecha indicados.</p>';
h+='<div class="fir"><div>EL VENDEDOR<br><br>Fdo.: '+B(val('vn'),18)+'</div><div>EL COMPRADOR<br><br>Fdo.: '+B(val('cn'),18)+'</div></div></div>';show('r',h);}
document.querySelectorAll('.card input,.card select,.card textarea').forEach(x=>x.addEventListener(x.tagName=='SELECT'||x.type=='checkbox'||x.type=='date'?'change':'input',()=>calc()));
(function(){const q=new URLSearchParams(location.search).get('t');if(q&&['pp','pv','vp'].includes(q))$('t').value=q;})();
paso(0);calc();"""))

# ---------- 2) Contrato de señal o reserva ----------
S['tools'].append(("contrato-senal-coche", "Contrato de señal o reserva de coche", "Reserva un coche con una señal (arras) por escrito: importe, plazo para completar la compra y qué pasa si alguien se echa atrás.", ""))
S['aff']["contrato-senal-coche"] = ext(INFORME_URL, "Informe del historial antes de reservar") + SEG
_st_sn = ("""<fieldset class="st"><legend>Lugar y fecha</legend>
<div class="row"><div><label for="ci">Lugar de la firma (localidad)</label><input id="ci" autocomplete="off"></div><div><label for="fe">Fecha</label><input id="fe" type="date" data-today></div></div>
<label for="t">¿Quién vende?</label><select id="t"><option value="p">Un particular</option><option value="e">Una compraventa o concesionario</option></select></fieldset>"""
+ _parte("v", "Vendedor") + _parte("c", "Comprador") + VEH +
"""<fieldset class="st"><legend>Señal y plazo</legend><div class="row">
<div><label for="pr">Precio total acordado (€)</label><input id="pr" inputmode="decimal"></div>
<div><label for="sn">Importe de la señal (€)</label><input id="sn" inputmode="decimal"></div>
<div><label for="fl">Fecha límite para completar la compra</label><input id="fl" type="date"></div>
<div><label for="fs">Cómo se paga la señal</label><select id="fs"><option value="transferencia bancaria">Transferencia bancaria</option><option value="dinero en efectivo">Efectivo</option><option value="Bizum">Bizum</option></select></div></div>
<label for="ar">Si alguien se echa atrás</label><select id="ar"><option value="pen">Arras penitenciales: el comprador pierde la señal o el vendedor la devuelve doble</option><option value="con">Arras confirmatorias: la señal es un pago a cuenta y se puede exigir la compra</option></select></fieldset>
<fieldset class="st"><legend>Revisar y descargar</legend><p>Revisa el documento. Lo que sale <span style="color:#c92a2a">en rojo</span> está sin rellenar. Firmad dos copias, una para cada parte. Cuando paguéis el resto, haced el <a href="contrato-compraventa-coche.html">contrato de compraventa</a> indicando la señal ya entregada.</p></fieldset>""")
P.append(("contrato-senal-coche", "Contrato de señal o reserva de coche: modelo de arras para rellenar | CocheCuentas",
"Modelo de contrato de señal o reserva para comprar un coche: importe de las arras, fecha límite y qué pasa si el comprador o el vendedor se echan atrás. Rellénalo paso a paso e imprímelo gratis.",
CSS_DOC + """<p class="lead">¿Has encontrado el coche pero aún no puedes pagarlo entero? Deja una señal por escrito. Rellena los datos paso a paso y el documento se escribe solo; al final lo imprimes, lo guardas en PDF o lo descargas en Word.</p>
<div class="card">""" + NAVB.format(steps=_st_sn, wn="'contrato-senal-'+(val('mt').replace(/\\s/g,'')||'coche')") + """
<div class="res" id="r" style="background:none;padding:0;margin-top:18px"></div></div>
<p class="note">Los datos que escribes no salen de tu navegador. Modelo orientativo basado en el Código Civil; si hay mucho dinero en juego o un caso especial, consulta con una gestoría o un abogado.</p>
<h2>Arras penitenciales o confirmatorias: cuál elegir</h2><p>La señal se llama legalmente <b>arras</b>. Con las <b>arras penitenciales</b> (artículo 1454 del Código Civil), cualquiera de los dos puede echarse atrás pagando un precio conocido: si es el comprador, <b>pierde la señal</b>; si es el vendedor, <b>devuelve el doble</b>. Es lo más habitual para reservar un coche, porque todo queda claro desde el principio. Con las <b>arras confirmatorias</b>, la señal es solo un adelanto del precio: si una parte no cumple, la otra puede exigir que se haga la venta o pedir que se anule con indemnización de los daños (artículo 1124). Si el documento no dice qué tipo son, los tribunales suelen considerarlas confirmatorias, por eso conviene escribirlo.</p>
<p><b>Ejemplo:</b> reservas un coche de 9.000 € con 500 € de señal penitencial y diez días para pagar el resto. Si el banco no te concede el préstamo y no compras, pierdes los 500 €. Si en esos diez días el vendedor se lo vende a otro, tiene que devolverte 1.000 €.</p>
<h2>Consejos antes de dar una señal</h2><ul><li>Paga la señal por transferencia o Bizum, para que quede constancia.</li><li>Antes de pagar, comprueba el <a href="historial-coche-matricula.html">historial del coche por matrícula</a> y que el vendedor es el titular que aparece en el permiso de circulación.</li><li>Pon una fecha límite realista: si necesitas financiación, calcula antes la <a href="cuota-financiacion-coche.html">cuota del préstamo</a>.</li><li>Calcula también lo que te costará la <a href="transferencia-coche.html">transferencia del coche</a>, para no llevarte sorpresas.</li></ul>""",
[("¿Cuánto se suele dejar de señal para reservar un coche?", "No hay un importe legal. Entre particulares suele ser una cantidad pequeña, de unos cientos de euros o en torno al 5-10 % del precio. Lo importante es que quede por escrito cuánto es, el plazo para pagar el resto y qué pasa si alguien se echa atrás."),
 ("¿Me devuelven la señal si al final no compro el coche?", "Depende de lo firmado. Con arras penitenciales, si eres tú quien se echa atrás, pierdes la señal. Si es el vendedor quien no cumple, tiene que devolverte el doble. Si el contrato no dice nada, la señal se considera un pago a cuenta y la devolución depende de quién incumplió."),
 ("¿El contrato de señal sirve para hacer la transferencia?", "No. Cuando pagues el resto tienes que firmar el contrato de compraventa (o recibir la factura, si vende una empresa), que es el documento que pide la DGT para el cambio de titularidad.")],
"Contrato de señal o reserva de coche",
CJS + r"""function parte(p,rol,pro){const n=val(p+'n'),d=val(p+'d'),o=val(p+'o'),r=val(p+'r');
return pro?'<b>'+B(n,26)+'</b>, con NIF '+B(d,12)+' y domicilio social en '+B(o,30)+', representada en este acto por '+B(r,26)+', como <b>'+rol+'</b>.'
:'D./D.ª <b>'+B(n,26)+'</b>, mayor de edad, con DNI/NIE '+B(d,12)+' y domicilio en '+B(o,30)+', como <b>'+rol+'</b>.';}
function calc(){const e=val('t')=='e';$('vrw').style.display=e?'block':'none';$('vnl').textContent=e?'Razón social de la empresa':'Nombre y apellidos';$('vdl').textContent=e?'NIF de la empresa':'DNI o NIE';
const pr=num('pr'),sn=num('sn'),pen=val('ar')=='pen',bs=val('bs').toUpperCase();let av=[];
if(sn>pr&&pr>0)av.push('La señal no puede ser mayor que el precio.');if(bs&&bs.length!=17)av.push('El bastidor (VIN) debería tener 17 caracteres.');
if(e&&val('fs')=='dinero en efectivo'&&sn>1000)av.push('Con una empresa, el pago en efectivo está limitado a 1.000 € (Ley 11/2021).');
let h=(av.length?'<div class="avisoc">'+av.join('<br>')+'</div>':'')+'<div class="doc" id="doc"><h3>CONTRATO DE SEÑAL Y RESERVA DE VEHÍCULO</h3><p class="sub">'+(pen?'Arras penitenciales (artículo 1454 del Código Civil)':'Arras confirmatorias')+'</p>';
h+='<p>En '+B(val('ci'),16)+', a '+(F(val('fe'))||B('',16))+'.</p><h4>REUNIDOS</h4><p>De una parte, '+parte('v','VENDEDOR',e)+'</p><p>De otra parte, '+parte('c','COMPRADOR',false)+'</p>';
h+='<p>Ambas partes se reconocen la capacidad legal necesaria para obligarse en este contrato y</p><h4>ACUERDAN</h4>';
h+='<p><b>PRIMERA. Objeto.</b> El VENDEDOR reserva al COMPRADOR, para su futura compraventa, el vehículo marca '+B(val('ma'),12)+', modelo '+B(val('mo'),18)+', matrícula <b>'+B(val('mt').toUpperCase(),10)+'</b>, número de bastidor '+B(bs,20)+', con fecha de primera matriculación '+(F(val('fm'))||B('',14))+' y '+B(val('km'),8)+' kilómetros, por un precio total de '+IMP(pr)+'.</p>';
h+='<p><b>SEGUNDA. Señal.</b> En este acto el COMPRADOR entrega al VENDEDOR, mediante '+esc(val('fs'))+', la cantidad de '+IMP(sn)+' en concepto de señal, de la que este documento sirve como recibo. Esta cantidad se descontará del precio en el momento de la compraventa, de modo que quedarán pendientes '+IMP(Math.max(0,pr-sn))+'.</p>';
h+='<p><b>TERCERA. Plazo.</b> Las partes firmarán el contrato de compraventa y el COMPRADOR pagará el resto del precio, con la entrega del vehículo y su documentación, no más tarde del '+(F(val('fl'))||B('',16))+'.</p>';
h+=pen?'<p><b>CUARTA. Naturaleza de la señal.</b> La señal se entrega como arras penitenciales conforme al artículo 1454 del Código Civil. Si el COMPRADOR desiste de la compra o no la completa en el plazo acordado por causa imputable a él, perderá la cantidad entregada. Si es el VENDEDOR quien desiste o no la completa, deberá devolver al COMPRADOR el doble de la señal recibida.</p>'
:'<p><b>CUARTA. Naturaleza de la señal.</b> La señal se entrega como arras confirmatorias y constituye un pago a cuenta del precio. Si una de las partes incumple, la otra podrá exigir el cumplimiento de la compraventa o su resolución, con la indemnización de daños y perjuicios que corresponda conforme al artículo 1124 del Código Civil.</p>';
h+='<p><b>QUINTA. Conservación del vehículo.</b> Hasta la fecha de la compraventa, el VENDEDOR se compromete a no vender ni reservar el vehículo a terceros, a conservarlo en el mismo estado en que el COMPRADOR lo ha visto y a no hacer con él un uso que aumente de forma apreciable su kilometraje. Si el vehículo sufre un daño en ese tiempo, el COMPRADOR podrá desistir y recuperar íntegramente la señal.</p>';
h+='<p><b>SEXTA. Ley aplicable.</b> Este contrato se rige por la legislación española y, para cualquier controversia, las partes se someten a los juzgados y tribunales competentes conforme a la ley.</p><p>Y en prueba de conformidad, firman este documento por duplicado en el lugar y la fecha indicados.</p>';
h+='<div class="fir"><div>EL VENDEDOR<br><br>Fdo.: '+B(val('vn'),18)+'</div><div>EL COMPRADOR<br><br>Fdo.: '+B(val('cn'),18)+'</div></div></div>';show('r',h);}
document.querySelectorAll('.card input,.card select,.card textarea').forEach(x=>x.addEventListener(x.tagName=='SELECT'||x.type=='checkbox'||x.type=='date'?'change':'input',()=>calc()));
paso(0);calc();"""))

# ---------- Sección "Contratos" en la portada ----------
S['home_extra'] = ('<h2 id="contratos">Contratos para comprar y vender coches</h2><p>Modelos gratuitos que se rellenan paso a paso y se imprimen, se guardan en PDF o se descargan en Word. Los datos no salen de tu navegador.</p><div class="grid">'
 '<a class="tool" href="contrato-compraventa-coche.html?t=pp"><h3>Compraventa entre particulares</h3><p>El contrato para vender o comprar un coche usado a otra persona, con vicios ocultos, cargas y hora de entrega.</p></a>'
 '<a class="tool" href="contrato-compraventa-coche.html?t=pv"><h3>Vender tu coche a una compraventa</h3><p>Particular que vende a una compraventa o concesionario: deja por escrito el precio y la hora desde la que el coche ya no es tuyo.</p></a>'
 '<a class="tool" href="contrato-compraventa-coche.html?t=vp"><h3>Compraventa o concesionario a particular</h3><p>Venta profesional con factura, garantía mínima de 1 año y límite de 1.000 € en efectivo.</p></a>'
 '<a class="tool" href="contrato-senal-coche.html"><h3>Señal o reserva de un coche</h3><p>Reserva el coche con arras por escrito: importe, plazo y qué pasa si alguien se echa atrás.</p></a>'
 '</div>') + S['home_extra']
S['home_intro'] = S['home_intro'].replace('<a href="etiqueta-dgt.html">Etiqueta DGT</a></nav>', '<a href="etiqueta-dgt.html">Etiqueta DGT</a><a href="#contratos">Contratos</a></nav>')

S['nav_extra'] = '<a href="index.html#contratos">Contratos</a>'

# --- Autonomía de un coche eléctrico en invierno: pérdida por frío, calefacción y autopista, y paradas para un viaje ---
S['tools'].insert(5, ("autonomia-coche-electrico-invierno", "Autonomía del eléctrico en invierno", "Cuántos km reales hace tu eléctrico con frío, con o sin bomba de calor, y cuántas paradas necesitas en un viaje.", "Eléctrico en invierno"))
S['aff']["autonomia-coche-electrico-invierno"] = amz("cable carga coche electrico tipo 2", "Cables de carga tipo 2") + amz("cargador portatil coche electrico schuko", "Cargadores portátiles") + amz("funda asiento calefactable coche 12v", "Fundas de asiento calefactables")
P.append(("autonomia-coche-electrico-invierno", "Autonomía de un coche eléctrico en invierno: cuántos km pierde con el frío | CocheCuentas",
"Calcula la autonomía real de tu coche eléctrico con frío: pérdida según la temperatura, con bomba de calor o resistencia, en ciudad o autopista, y cuántas paradas para cargar en tu viaje de Navidad.",
"""<p class="lead">Pon la autonomía homologada (WLTP) de tu coche, la temperatura que esperas y cómo vas a conducir. Te damos un rango realista de kilómetros y, si vas de viaje, cuántas veces tendrás que parar a cargar.</p>
<div class="card"><div class="row"><div><label for="w">Autonomía WLTP (km)</label><input id="w" inputmode="numeric" value="400"></div>
<div><label for="t">Temperatura exterior</label><select id="t"><option value="0,5">Más de 15 °C</option><option value="5,10">Entre 10 y 15 °C</option><option value="10,15">Entre 5 y 10 °C</option><option value="10,20" selected>Entre 0 y 5 °C</option><option value="20,30">Entre −5 y 0 °C</option><option value="25,40">Menos de −5 °C</option></select></div>
<div><label for="hp">Calefacción del coche</label><select id="hp"><option value="1">Bomba de calor</option><option value="0">Resistencia eléctrica (sin bomba de calor)</option></select></div>
<div><label for="u">Tipo de trayecto</label><select id="u"><option value="m">Mixto (carretera y ciudad)</option><option value="a" selected>Autopista a 110-120 km/h</option><option value="c">Trayectos cortos en ciudad (coche frío)</option></select></div>
<div><label for="km">Viaje: distancia total (km)</label><input id="km" inputmode="numeric" value="450"></div>
<div><label for="b">Batería al salir (%)</label><input id="b" inputmode="numeric" value="90"></div></div>
<button onclick="calc()">Calcular autonomía</button><div class="res" id="r" aria-live="polite"></div></div>
<p class="note">Estimación orientativa. Cada modelo se comporta distinto: si tu coche muestra el consumo medio en kWh/100 km de tus últimos trayectos con frío, divide la capacidad útil de la batería entre ese consumo para afinar.</p>
<h2>Por qué el frío reduce la autonomía</h2><p>Hay dos causas. La primera es la <b>batería</b>: con frío, la química de las celdas de iones de litio es más lenta, la resistencia interna sube y el coche gasta energía en calentarla; además, la frenada regenerativa se limita hasta que coge temperatura. La segunda es la <b>calefacción</b>: un coche de combustión aprovecha el calor que sobra del motor, pero un eléctrico tiene que producirlo con la batería. Con resistencias eléctricas, cada kW de calor cuesta un kW de batería; una <b>bomba de calor</b> da varios kW de calor por cada kW consumido, y por eso pierde bastante menos autonomía.</p>
<p>Los análisis publicados coinciden en el orden de magnitud: en inviernos moderados la autonomía suele bajar <b>entre un 10 % y un 20 %</b>, y con temperaturas bajo cero <b>entre un 20 % y un 40 %</b>, más en coches sin bomba de calor y en trayectos cortos con el coche frío. En autopista, además, la resistencia del aire crece con el cuadrado de la velocidad: a 120 km/h casi ningún eléctrico llega a su cifra WLTP ni en verano.</p>
<h2>Cómo calculamos el rango</h2><ol><li>Partimos de la autonomía WLTP.</li><li>Restamos la pérdida por frío de la franja de temperatura: la mitad baja del rango si el coche tiene bomba de calor y la mitad alta si calienta con resistencias.</li><li>En trayectos cortos con el coche frío sumamos de 5 a 10 puntos más (calentar el habitáculo y la batería pesa más en pocos kilómetros); en autopista a 110-120 km/h aplicamos de un 15 % a un 25 % menos por la aerodinámica.</li><li>Para el viaje, contamos lo que da tu carga de salida hasta llegar al 10 % y paradas que recargan del 10 % al 80 %, lo habitual en un cargador rápido.</li></ol>
<p><b>Ejemplo:</b> un eléctrico con 400 km WLTP y bomba de calor, a 2 °C por autopista, hace entre unos 255 y 305 km con la batería llena. Para un viaje de 450 km saliendo al 90 %, la primera carga da unos 200 km (pesimista) y cada parada de 10 a 80 % unos 180 km: hacen falta <b>2 paradas</b>.</p>
<h2>Consejos para viajar con frío</h2><ul><li><b>Preacondiciona el coche enchufado</b> antes de salir: calienta habitáculo y batería con la energía de la red, no con la de la batería.</li><li>Usa los <b>asientos y el volante calefactables</b>: gastan mucho menos que calentar todo el aire del habitáculo.</li><li>Si tu coche lo permite, activa el <b>precalentamiento de la batería</b> al poner un cargador rápido en el navegador: cargarás bastante más rápido.</li><li>Revisa la <b>presión de los neumáticos</b>: baja con el frío y sube el consumo.</li><li>Baja a 100-110 km/h si vas justo: a menudo es más rápido que parar una vez más.</li></ul>
<p>Si dudas entre eléctrico y combustión, compara el gasto anual en <a href="electrico-vs-gasolina.html">eléctrico frente a gasolina o diésel</a>. Calcula el coste de la carga en casa en GastoLuz con el <a href="https://gastoluz.es/coste-cargar-coche-electrico.html">coste de cargar un coche eléctrico</a> y, si vas en coche de combustión, la <a href="coste-viaje-coche.html">gasolina del viaje</a>.</p>""",
[("¿Cuánta autonomía pierde un coche eléctrico en invierno?", "En inviernos moderados, entre un 10 % y un 20 %; con temperaturas bajo cero, entre un 20 % y un 40 %. Los coches con bomba de calor están en la parte baja de esos rangos y los que calientan con resistencias, en la alta."),
 ("¿La calefacción gasta mucha batería en un coche eléctrico?", "Con resistencias eléctricas puede consumir varios kW mientras calienta el habitáculo, lo que en trayectos cortos supone una parte grande del consumo. Con bomba de calor el gasto es varias veces menor. Los asientos y el volante calefactables son la forma más eficiente de entrar en calor."),
 ("¿Se carga más despacio un coche eléctrico con frío?", "Sí, en carga rápida: con la batería fría el coche limita la potencia para protegerla. Por eso conviene llegar al cargador con la batería caliente, después de conducir un rato o usando el precalentamiento si el coche lo tiene."),
 ("¿Es mejor dejar el coche eléctrico enchufado cuando hace frío?", "Sí, si vas a preacondicionarlo: así calienta la batería y el habitáculo con energía de la red antes de salir. Además, mantener la carga por encima del 20 % evita sustos, porque con frío la autonomía disponible baja.")],
"Autonomía de un coche eléctrico en invierno",
"""function calc(){const W=v('w'),t=document.getElementById('t').value.split(',').map(Number),hp=document.getElementById('hp').value==='1',u=document.getElementById('u').value;
if(W<=0){show('r','Escribe la autonomía WLTP de tu coche.');return;}
const md=(t[0]+t[1])/2;let lo=hp?t[0]:md,hi=hp?md:t[1];if(u==='c'){lo+=5;hi+=10;}
let fmax=1-lo/100,fmin=1-hi/100;if(u==='a'){fmax*=0.85;fmin*=0.75;}
const rmin=W*fmin,rmax=W*fmax,km=v('km'),b=Math.min(100,Math.max(0,v('b')));
let h='Autonomía real estimada con la batería llena:<b class="big">'+nf(rmin,0)+' – '+nf(rmax,0)+' km</b>Entre un '+nf((1-fmax)*100,0)+' % y un '+nf((1-fmin)*100,0)+' % menos que los '+nf(W,0)+' km WLTP.';
if(km>0){const l1=rmin*Math.max(0,b-10)/100,leg=rmin*0.7,n=km<=l1?0:Math.ceil((km-l1)/leg);
h+='<br>Viaje de '+nf(km,0)+' km saliendo al '+nf(b,0)+' %: la primera carga da para unos <b>'+nf(l1,0)+' km</b> llegando al 10 %. '+(n===0?'<b>Llegas sin parar a cargar</b> (con margen pesimista).':'Necesitarás <b>'+n+' parada'+(n>1?'s':'')+'</b> de carga del 10 % al 80 % (unos '+nf(leg,0)+' km cada una, calculado con la autonomía más baja).');}
show('r',h);}
document.querySelectorAll('.card input,.card select').forEach(x=>x.addEventListener(x.tagName=='SELECT'?'change':'input',()=>calc()));
calc();"""))
# Enlaces internos desde páginas relacionadas
for _k, _t in enumerate(P):
    if _t[0] in ("electrico-vs-gasolina", "coste-viaje-coche", "distancia-frenado"):
        _l = list(_t)
        _l[3] = _l[3] + '<p>¿Viajas en coche eléctrico con frío? Calcula cuántos km pierde y cuántas paradas necesitas con la <a href="autonomia-coche-electrico-invierno.html">autonomía del eléctrico en invierno</a>.</p>'
        P[_k] = tuple(_l)

# --- Mejora (27/11/2026): depreciación del coche con comparación con las tablas de Hacienda, ejemplo y más preguntas ---
for _k, _t in enumerate(P):
    if _t[0] == "depreciacion-coche":
        _l = list(_t)
        _l[1] = "Depreciación de un coche: cuánto valdrá dentro de 1, 3 o 5 años | CocheCuentas"
        _l[2] = "Calcula cuánto valdrá tu coche dentro de 1, 3 o 5 años, cuánto pierde cada año y compáralo con las tablas de Hacienda. Útil para vender, comprar seminuevo o elegir entre nuevo y usado."
        _l[3] = _l[3].replace('<button onclick="calc()">Calcular</button>', '<label for="tp">Punto de partida</label><select id="tp"><option value="20,12">Coche nuevo, marca generalista</option><option value="25,14">Coche nuevo con poca demanda o precio alto</option><option value="10,10">Seminuevo de 1-3 años</option><option value="8,8">Usado de más de 4 años</option><option value="">Personalizado (uso mis porcentajes)</option></select><button onclick="calc()">Calcular</button>', 1) + """
<h2>Cómo se calcula</h2><p>Un coche pierde valor sobre lo que vale cada año, no sobre su precio original: valor del año siguiente = valor actual × (1 − porcentaje de pérdida). Por eso la curva es más pronunciada al principio y se suaviza con el tiempo. El primer año es el más caro porque al matricularlo deja de ser nuevo: se pierden el margen del concesionario, parte de los impuestos y la «prima» de estrenar.</p>
<p><b>Ejemplo:</b> un coche de 25.000 € que pierde un 20 % el primer año y un 12 % los siguientes vale unos 20.000 € al cumplir un año, 17.600 € a los dos, 13.630 € a los cuatro y unos <b>12.000 € a los cinco</b>: ha perdido un 52 %, unos 2.600 € al año. Si lo compras con un año, te ahorras los 5.000 € del primer golpe y el resto de la curva es mucho más suave.</p>
<h2>Valor de mercado y valor fiscal de Hacienda</h2><p>Hacienda no usa el precio de mercado: aplica al precio del coche nuevo de sus tablas un porcentaje fijo según la antigüedad (100 % el primer año, 84 % con más de un año, 67 % con más de 2, 56 % con más de 3, 47 % con más de 4, 39 % con más de 5 y así hasta el 10 % a partir de 12 años). Ese <b>valor fiscal</b> es el que sirve para el impuesto de transmisiones cuando compras un usado a un particular, y suele ser más alto que el de mercado en los primeros años. Calcula lo que pagarás en la <a href="transferencia-coche.html">calculadora de transferencia de coche</a>.</p>
<table><tr><th>Antigüedad</th><th>Tablas de Hacienda (% del valor nuevo)</th><th>Mercado orientativo (20 % y 12 %)</th></tr>
<tr><td>Más de 1 año</td><td>84 %</td><td>80 %</td></tr><tr><td>Más de 2 años</td><td>67 %</td><td>70 %</td></tr><tr><td>Más de 3 años</td><td>56 %</td><td>62 %</td></tr><tr><td>Más de 5 años</td><td>39 %</td><td>48 %</td></tr><tr><td>Más de 8 años</td><td>24 %</td><td>33 %</td></tr></table>
<p class="note">La columna de mercado es orientativa: el precio real depende del modelo, los kilómetros y la demanda. Para vender o comprar, compara anuncios del mismo modelo, año y kilometraje.</p>
<p>Si estás decidiendo qué comprar, calcula también <a href="que-coche-me-puedo-permitir.html">qué coche te puedes permitir</a>, la <a href="cuota-financiacion-coche.html">cuota de la financiación</a>, si te compensa más el <a href="renting-vs-compra.html">renting o comprar</a> y el <a href="coste-anual-coche.html">coste anual completo</a> de tenerlo. Si vas a vender, prepara el <a href="contrato-compraventa-coche.html">contrato de compraventa</a>.</p>"""
        _l[4] = list(_l[4]) + [("¿Cuánto vale mi coche según Hacienda?", "El precio del modelo nuevo en las tablas de Hacienda multiplicado por el porcentaje de su antigüedad: 84 % con más de un año, 67 % con más de 2, 56 % con más de 3, 47 % con más de 4, 39 % con más de 5 y hasta el 10 % a partir de 12 años."),
                               ("¿Qué coches se deprecian menos?", "Los modelos con mucha demanda en el mercado de ocasión, con mantenimiento al día, pocos kilómetros, colores neutros y etiqueta ECO o C con motor fiable. Los que más pierden suelen ser los de precio alto, los de poca demanda y los que quedan desfasados tecnológicamente pronto.")]
        _l[6] = _l[6].replace("function calc(){", "function calc(){const tp=document.getElementById('tp');if(tp&&tp.value){const q=tp.value.split(',');document.getElementById('r1').value=q[0];document.getElementById('r2').value=q[1];}", 1) + "\ndocument.getElementById('tp').addEventListener('change',()=>calc());['r1','r2'].forEach(i=>document.getElementById(i).addEventListener('input',()=>{document.getElementById('tp').value='';}));document.querySelectorAll('#pv,#n,#r1,#r2').forEach(x=>x.addEventListener('input',()=>calc()));"
        P[_k] = tuple(_l)
S['home_intro'] = S['home_intro'].replace('<a href="distancia-frenado.html">Frenado con hielo</a>', '<a href="distancia-frenado.html">Frenado con hielo</a><a href="autonomia-coche-electrico-invierno.html">Eléctrico en invierno</a>', 1)

# --- Nueva (27/11/2026, 13:23): calculadora de anticongelante: proporción con agua, temperatura de protección y litros a cambiar ---
S['tools'].insert(6, ("calculadora-anticongelante", "Calculadora de anticongelante", "Qué proporción de anticongelante y agua necesitas para tu temperatura mínima y cuántos litros cambiar.", "Anticongelante"))
S['aff']["calculadora-anticongelante"] = amz("anticongelante concentrado", "Anticongelante concentrado") + amz("densimetro anticongelante refractometro", "Refractómetros y densímetros de anticongelante") + amz("embudo llenado radiador coche", "Embudos para llenar el radiador")
P.append(("calculadora-anticongelante", "Calculadora de anticongelante: proporción con agua y litros para tu coche | CocheCuentas",
"Calcula cuánto anticongelante y cuánta agua echar al radiador para proteger tu coche hasta -15, -25 o -35 °C, y cuántos litros vaciar si ya tiene mezcla. Tabla de proporciones y punto de congelación.",
"""<p class="lead">Pon la capacidad del circuito de refrigeración, la concentración que tiene ahora y la temperatura más baja que quieres soportar. Te decimos qué mezcla necesitas, cuántos litros vaciar y cuánto anticongelante comprar.</p>
<div class="card"><div class="row"><div><label for="cap">Capacidad del circuito (litros)</label><input id="cap" inputmode="decimal" value="6"></div>
<div><label for="tm">Temperatura mínima a proteger</label><select id="tm"><option value="-10">-10 °C (costa, clima suave)</option><option value="-15">-15 °C</option><option value="-20">-20 °C</option><option value="-25" selected>-25 °C (interior y montaña)</option><option value="-30">-30 °C</option><option value="-35">-35 °C (alta montaña)</option></select></div>
<div><label for="c0">Concentración actual del circuito (%)</label><input id="c0" inputmode="decimal" value="20"></div>
<div><label for="cp">Concentración del producto que añades (%)</label><select id="cp"><option value="100">Concentrado puro (100 %)</option><option value="50">Listo para usar al 50 %</option><option value="30">Listo para usar al 30 %</option></select></div></div>
<button onclick="calc()">Calcular mezcla</button><div class="res" id="r" aria-live="polite"></div></div>
<p class="note">La capacidad del circuito viene en el manual del coche (en un turismo suele estar entre 5 y 9 litros). La concentración actual se mide con un densímetro o un refractómetro de anticongelante; si solo lleva agua, pon 0. Usa siempre el tipo de refrigerante que indica el fabricante.</p>
<h2>Tabla de proporción anticongelante-agua</h2><p>El anticongelante para coches es casi siempre a base de <b>etilenglicol</b>. Mezclado con agua baja el punto de congelación de la mezcla; estos son los valores aproximados para mezclas en volumen:</p>
<table><tr><th>Anticongelante</th><th>Agua</th><th>Protege hasta</th><th>En 6 litros</th></tr>
<tr><td>20 %</td><td>80 %</td><td>-9 °C</td><td>1,2 l + 4,8 l de agua</td></tr><tr><td>30 %</td><td>70 %</td><td>-15 °C</td><td>1,8 l + 4,2 l</td></tr>
<tr><td>40 %</td><td>60 %</td><td>-24 °C</td><td>2,4 l + 3,6 l</td></tr><tr><td>50 %</td><td>50 %</td><td>-37 °C</td><td>3 l + 3 l</td></tr><tr><td>60 %</td><td>40 %</td><td>-52 °C</td><td>3,6 l + 2,4 l</td></tr></table>
<p class="note">Valores orientativos del etilenglicol en agua. Mira la tabla de la etiqueta de tu producto: los refrigerantes con propilenglicol protegen algo menos con la misma proporción.</p>
<h2>Cómo calculamos los litros a cambiar</h2><p>Si el circuito ya tiene algo de anticongelante, no hace falta vaciarlo entero: basta con sacar una parte y sustituirla por concentrado. Con <b>V</b> litros en el circuito, una concentración actual <b>c₀</b>, la deseada <b>c₁</b> y un producto de concentración <b>c<sub>p</sub></b>, los litros a vaciar y reponer son:</p>
<p><b>litros = V × (c₁ − c₀) ÷ (c<sub>p</sub> − c₀)</b></p>
<p><b>Ejemplo:</b> un circuito de 6 litros que protege hasta unos -9 °C (20 %) y quieres llegar a -25 °C (41 %). Vacías 6 × (0,41 − 0,20) ÷ (1 − 0,20) = <b>1,6 litros</b> y añades 1,6 litros de anticongelante concentrado. Con un producto ya mezclado al 50 % tendrías que cambiar 4,2 litros, casi todo el circuito: por eso, para subir mucho la protección, compensa el concentrado.</p>
<h2>Consejos antes de la ola de frío</h2><ul><li><b>No pases del 60 %</b>: con más anticongelante la mezcla vuelve a congelar antes y refrigera peor el motor. Entre el 33 % y el 50 % es lo recomendable en España.</li><li><b>Usa agua destilada o desmineralizada</b> para mezclar, no del grifo: la cal y las sales dañan el circuito.</li><li><b>No mezcles tipos distintos</b> (por ejemplo, orgánicos e inorgánicos): pueden formar lodos. El color no es una norma fiable; guíate por la especificación del manual.</li><li>Rellena siempre con el <b>motor frío</b> y hasta la marca entre MIN y MAX del vaso de expansión.</li><li>El refrigerante también pierde sus aditivos anticorrosión con los años: la mayoría de fabricantes piden cambiarlo cada 4-5 años o entre 60.000 y 150.000 km.</li></ul>
<p>Si vas a viajar por carreteras con nieve o hielo, mira también cuánto aumenta la <a href="distancia-frenado.html">distancia de frenado con hielo</a>, qué <a href="equivalencia-neumaticos.html">neumáticos de invierno y cadenas</a> te sirven y cuánto te cuesta el <a href="coste-viaje-coche.html">combustible del viaje</a>. Si tu coche es eléctrico, calcula su <a href="autonomia-coche-electrico-invierno.html">autonomía con frío</a>.</p>""",
[("¿Qué proporción de anticongelante y agua hay que echar?", "En España lo habitual es entre un 33 % y un 50 % de anticongelante. Al 33 % protege hasta unos -18 °C, suficiente para la mayoría de zonas; al 50 %, hasta unos -37 °C, para montaña y zonas muy frías. Nunca más del 60 %."),
 ("¿Cuántos litros de anticongelante lleva un coche?", "El circuito de refrigeración de un turismo suele tener entre 5 y 9 litros (mira el manual). Para una mezcla al 50 % en 6 litros necesitas 3 litros de concentrado y 3 de agua destilada."),
 ("¿Puedo echar solo agua al radiador?", "Solo en una emergencia y por poco tiempo. El agua sola se congela a 0 °C, puede reventar el radiador o el bloque y no protege contra la corrosión. Después hay que restablecer la proporción de anticongelante."),
 ("¿Cómo sé qué concentración tiene mi refrigerante?", "Con un densímetro de bolas o un refractómetro, que cuestan pocos euros y miden la temperatura de protección en segundos. En el taller lo comprueban gratis en muchas revisiones de invierno.")],
"Calculadora de anticongelante",
"""const TB=[[0,0],[10,-4],[20,-9],[30,-15],[40,-24],[50,-37],[60,-52]];
function pc(c){c=Math.max(0,Math.min(60,c));for(let i=1;i<TB.length;i++)if(c<=TB[i][0]){const a=TB[i-1],b=TB[i];return a[1]+(b[1]-a[1])*(c-a[0])/(b[0]-a[0]);}return -52;}
function cn(t){for(let i=1;i<TB.length;i++)if(t>=TB[i][1]){const a=TB[i-1],b=TB[i];return a[0]+(b[0]-a[0])*(t-a[1])/(b[1]-a[1]);}return 60;}
function calc(){const V=v('cap'),t=+document.getElementById('tm').value,c0=Math.max(0,Math.min(100,v('c0'))),cp=+document.getElementById('cp').value,c1=Math.ceil(cn(t));
if(V<=0){show('r','Escribe la capacidad del circuito.');return;}
let h='Mezcla necesaria:<b class="big">'+c1+' % de anticongelante</b>Protege hasta unos '+nf(pc(c1),0)+' °C. Ahora tu circuito protege hasta unos '+nf(pc(c0),0)+' °C.';
if(c0>=c1)h+='<br><b>No necesitas añadir nada</b>: tu mezcla actual ya protege hasta esa temperatura. Si te falta líquido, rellena con mezcla al '+c1+' %.';
else if(cp<=c1)h+='<br>Con un producto al '+cp+' % no puedes llegar al '+c1+' %: necesitas anticongelante más concentrado.';
else{const x=V*(c1-c0)/(cp-c0);h+='<br>Vacía <b>'+nf(x,1)+' litros</b> del circuito y añade <b>'+nf(x,1)+' litros</b> de anticongelante '+(cp==100?'concentrado':'al '+cp+' %')+'.';}
const pure=V*c1/100;h+='<br>Si vacías y rellenas todo el circuito: <b>'+nf(pure,1)+' l de concentrado + '+nf(V-pure,1)+' l de agua destilada</b>.';
show('r',h);}
calc();"""))
for _k, _t in enumerate(P):
    if _t[0] in ("distancia-frenado", "autonomia-coche-electrico-invierno", "equivalencia-neumaticos"):
        _l = list(_t)
        _l[3] = _l[3] + '<p>Antes de las heladas, comprueba también que el refrigerante aguanta el frío de tu zona con la <a href="calculadora-anticongelante.html">calculadora de anticongelante</a>: proporción con agua y litros a cambiar.</p>'
        P[_k] = tuple(_l)
S['home_intro'] = S['home_intro'].replace('<a href="autonomia-coche-electrico-invierno.html">Eléctrico en invierno</a>', '<a href="calculadora-anticongelante.html">Anticongelante</a>', 1)

# --- Mejora (27/11/2026, 13:23): financiación de coche con ejemplo, tabla de cuotas por cada 10.000 €, multiopción y más FAQ ---
for _k, _t in enumerate(P):
    if _t[0] == "cuota-financiacion-coche":
        _l = list(_t)
        _l[1] = "Calculadora de financiación de coche: cuota mensual, TAE e intereses | CocheCuentas"
        _l[2] = "Calcula la cuota mensual al financiar un coche, la TAE real con comisión de apertura y cuánto pagas de intereses. Tabla de cuotas por cada 10.000 € a 3, 4, 5 y 7 años y financiación con cuota final."
        _l[3] = _l[3].replace('<p class="lead">Calcula la cuota y lo que pagarás en total al financiar tu coche.</p>',
            '<p class="lead">Pon el precio, la entrada, el interés (TIN) y el plazo que te ofrecen. Te decimos la cuota mensual, la TAE real con la comisión de apertura y cuánto pagas en intereses, también si es una financiación con cuota final.</p>', 1)
        _l[3] = _l[3] + """<p><b>Ejemplo:</b> un coche de 20.000 € con 4.000 € de entrada, financiado a 60 meses al 8,5 % TIN con un 3 % de comisión de apertura. Financias 16.000 € y pagas <b>328,26 € al mes</b>; en intereses se van 3.696 € y la comisión suma 480 € más. La TAE resultante sube al <b>10,3 %</b>, casi dos puntos más que el 8,5 % anunciado.</p>
<h2>Cuota por cada 10.000 € financiados</h2><p>Para hacerte una idea rápida, multiplica por el número de decenas de miles que vas a financiar. Cuota mensual y, entre paréntesis, intereses totales (sin comisiones):</p>
<table><tr><th>TIN</th><th>36 meses</th><th>48 meses</th><th>60 meses</th><th>84 meses</th></tr>
<tr><td>5 %</td><td>299,71 € (790 €)</td><td>230,29 € (1.054 €)</td><td>188,71 € (1.323 €)</td><td>141,34 € (1.872 €)</td></tr>
<tr><td>7 %</td><td>308,77 € (1.116 €)</td><td>239,46 € (1.494 €)</td><td>198,01 € (1.881 €)</td><td>150,93 € (2.678 €)</td></tr>
<tr><td>9 %</td><td>318,00 € (1.448 €)</td><td>248,85 € (1.945 €)</td><td>207,58 € (2.455 €)</td><td>160,89 € (3.515 €)</td></tr>
<tr><td>11 %</td><td>327,39 € (1.786 €)</td><td>258,46 € (2.406 €)</td><td>217,42 € (3.045 €)</td><td>171,22 € (4.383 €)</td></tr></table>
<p>Alargar el plazo baja la cuota, pero encarece mucho el total: a 7 años pagas más del doble de intereses que a 3. Y el coche se deprecia mientras tanto; mira <a href="depreciacion-coche.html">cuánto valdrá dentro de unos años</a> para no deber más de lo que vale.</p>
<h2>Financiación con cuota final (multiopción)</h2><p>En estas ofertas una parte del precio, el <b>valor futuro garantizado</b>, se deja para el final. Las cuotas son más bajas porque solo amortizas la diferencia, pero pagas intereses sobre todo el importe durante todo el plazo. Al terminar puedes pagar la cuota final (o refinanciarla), devolver el coche si cumple los kilómetros y el estado pactados o cambiarlo por otro. Escribe esa cuota final en la calculadora para ver la TAE real y compárala con un <a href="renting-vs-compra.html">renting</a> o con la financiación clásica.</p>
<p>Al coste de la cuota súmale el seguro, el <a href="impuesto-circulacion.html">impuesto de circulación</a> y el mantenimiento: calcula el total en <a href="coste-anual-coche.html">cuánto cuesta mantener un coche al año</a>.</p>"""
        _l[4] = list(_l[4]) + [("¿Cuánto pago al mes por financiar 20.000 €?", "Depende del interés y el plazo. A 5 años (60 meses) y un 7 % TIN son unos 396 € al mes; al 9 %, unos 415 €. A 7 años la cuota baja a unos 302 € al 7 %, pero pagas casi 5.400 € de intereses."),
                               ("¿Puedo amortizar antes la financiación del coche?", "Sí. La ley de crédito al consumo permite devolverlo antes en cualquier momento; la entidad puede cobrar una compensación de hasta el 1 % de lo que amortizas si queda más de un año, o del 0,5 % si queda menos. Revisa también si perder un descuento por financiar te obliga a devolverlo.")]
        P[_k] = tuple(_l)
