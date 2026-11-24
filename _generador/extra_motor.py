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
pinta();"""))
