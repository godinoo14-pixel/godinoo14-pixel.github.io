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
"¿Puedo montar otra medida de rueda? Compara dos neumáticos (por ejemplo 205/55 R16 y 225/45 R17): diferencia de diámetro, error del velocímetro y si entra en el ±3 % aceptado.",
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
<h2>Qué distancia dejar con el coche de delante</h2><p>La regla práctica que recomienda la DGT es la de los <b>dos segundos</b>: cuando el coche de delante pase por un punto fijo (una señal, un puente), cuenta «mil uno, mil dos»; si llegas a ese punto antes de terminar, vas demasiado cerca. Con lluvia, niebla o de noche, déjalo al menos en el doble, y con nieve o hielo mucho más. En estas fechas, antes de un viaje largo, revisa la profundidad del dibujo de los neumáticos (mínimo legal 1,6 mm) y lleva cadenas si vas a zonas de montaña.</p>
<p>Calcula también lo que te costaría una <a href="multa-exceso-velocidad.html">multa por exceso de velocidad</a>, el <a href="coste-viaje-coche.html">coste de tu viaje en coche</a> con el precio de hoy del combustible o si una <a href="equivalencia-neumaticos.html">medida de neumático distinta</a> es compatible con tu coche.</p>""",
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
calc();"""))
