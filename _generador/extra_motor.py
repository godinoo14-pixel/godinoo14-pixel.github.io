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
