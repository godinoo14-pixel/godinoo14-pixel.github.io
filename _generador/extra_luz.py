from gen import amz, ext
CNMC = ext("https://comparador.cnmc.gob.es/", "Comparador oficial de tarifas (CNMC)")
ENCH = amz("enchufe medidor consumo electrico", "Enchufe medidor de consumo")
S['aff'] = {
    "index": ENCH + CNMC,
    "consumo-electrodomesticos": ENCH + amz("regleta con interruptor", "Regletas con interruptor") + CNMC,
    "coste-aire-acondicionado": amz("aire acondicionado portatil", "Aires acondicionados") + amz("ventilador techo", "Ventiladores de techo"),
    "potencia-contratada": CNMC + ENCH,
    "calculadora-kwh": ENCH,
    "coste-calefaccion-electrica": amz("radiador bajo consumo termostato", "Radiadores con termostato") + amz("burlete puerta", "Burletes para puertas y ventanas"),
    "ahorro-led": amz("bombillas led e27", "Bombillas LED E27") + amz("bombillas led gu10", "Bombillas LED GU10"),
    "coste-cargar-coche-electrico": amz("cargador coche electrico wallbox", "Cargadores Wallbox") + CNMC,
    "calculadora-placas-solares": amz("kit placa solar autoconsumo", "Kits solares de autoconsumo") + amz("placa solar balcon", "Placas solares de balcón"),
    "coste-ducha-termo": amz("alcachofa ducha ahorro agua", "Alcachofas de ahorro") + amz("temporizador termo electrico", "Temporizadores para termo"),
}
S['tools'] += [("coste-cargar-coche-electrico", "Coste de cargar un coche eléctrico", "Cuánto cuesta una carga en casa y en la calle.", ""),
               ("calculadora-placas-solares", "Calculadora de placas solares", "Ahorro anual y amortización del autoconsumo.", ""),
               ("coste-ducha-termo", "Coste de una ducha con termo eléctrico", "Lo que pagas por cada ducha y al mes.", "")]

P.append(("coste-cargar-coche-electrico", "¿Cuánto cuesta cargar un coche eléctrico? Calculadora | GastoLuz",
"Calcula cuánto cuesta cargar tu coche eléctrico en casa o en un cargador público según la batería, el porcentaje y el precio del kWh.",
"""<p class="lead">Calcula el coste de una carga completa o parcial y compárala entre casa y cargador público.</p>
<div class="card"><div class="row"><div><label for="b">Batería útil (kWh)</label><input id="b" inputmode="decimal" value="60"></div><div><label for="pe">Pérdidas de carga (%)</label><input id="pe" inputmode="decimal" value="10"></div>
<div><label for="d">Desde (%)</label><input id="d" inputmode="numeric" value="20"></div><div><label for="h">Hasta (%)</label><input id="h" inputmode="numeric" value="80"></div>
<div><label for="pc">Precio kWh en casa (€)</label><input id="pc" inputmode="decimal" value="0,12"></div><div><label for="pp">Precio kWh cargador público (€)</label><input id="pp" inputmode="decimal" value="0,49"></div></div>
<button onclick="calc()">Calcular</button><div class="res" id="r"></div></div>
<p class="note">Pon tu tarifa: con discriminación horaria, cargar de madrugada (periodo valle) es lo más barato. En la calle, los cargadores rápidos suelen ser los más caros.</p>
<h2>Cómo se calcula</h2><p>Energía = batería × (hasta − desde) / 100, más un 8-12 % de pérdidas en la carga. Multiplicada por el precio del kWh te da el coste. Una carga del 20 % al 80 % de una batería de 60 kWh son 36 kWh útiles, unos 40 kWh de la red.</p>""",
[("¿Cuánto cuesta llenar un coche eléctrico en casa?", "Con una batería de 60 kWh y el kWh a 0,12 €, una carga completa ronda los 8 €, contando pérdidas."),
 ("¿Por qué no se carga siempre al 100 %?", "Para cuidar la batería, la mayoría de fabricantes recomiendan cargar al 80 % en el día a día y llegar al 100 % solo antes de viajes largos.")],
None,
"""function calc(){const k=v('b')*(v('h')-v('d'))/100*(1+v('pe')/100);
show('r','Energía de la red:<b class="big">'+nf(k,1)+' kWh</b>En casa: <b>'+eur(k*v('pc'))+'</b> · En cargador público: <b>'+eur(k*v('pp'))+'</b><br>Ahorras '+eur(k*(v('pp')-v('pc')))+' por carga en casa');}"""))

P.append(("calculadora-placas-solares", "Calculadora de placas solares: ahorro y amortización | GastoLuz",
"Calcula cuántas placas solares necesitas, cuánto ahorrarás al año con autoconsumo y en cuántos años se amortiza la instalación.",
"""<p class="lead">Estima la producción, el ahorro y la amortización de una instalación de autoconsumo en tu vivienda.</p>
<div class="card"><div class="row"><div><label for="c">Consumo anual (kWh)</label><input id="c" inputmode="numeric" value="4000"></div><div><label for="kp">Potencia instalada (kWp)</label><input id="kp" inputmode="decimal" value="3"></div>
<div><label for="hs">Producción por kWp (kWh/año)</label><input id="hs" inputmode="numeric" value="1500"></div><div><label for="au">Autoconsumo directo (%)</label><input id="au" inputmode="decimal" value="40"></div>
<div><label for="p">Precio kWh que pagas (€)</label><input id="p" inputmode="decimal" value="0,15"></div><div><label for="ex">Compensación excedentes (€/kWh)</label><input id="ex" inputmode="decimal" value="0,06"></div>
<div><label for="ci">Coste instalación (€/kWp)</label><input id="ci" inputmode="decimal" value="1300"></div><div><label for="wp">Potencia por placa (W)</label><input id="wp" inputmode="numeric" value="450"></div></div>
<button onclick="calc()">Calcular</button><div class="res" id="r"></div></div>
<p class="note">Producción orientativa en España: unos 1.300 kWh por kWp al año en el norte y hasta 1.700 en el sur. El autoconsumo directo sube si pones lavadora, lavavajillas o termo durante las horas de sol.</p>
<h2>Cómo dimensionar la instalación</h2><p>Una regla sencilla: divide tu consumo anual entre la producción por kWp de tu zona. Con 4.000 kWh al año y 1.500 kWh por kWp, unos 2,7 kWp bastan para cubrir el consumo, es decir, unas 6 placas de 450 W. Mira también si tu ayuntamiento bonifica el IBI o el ICIO por instalar autoconsumo.</p>""",
[("¿Cuántas placas solares necesito para una casa?", "Para un consumo típico de 3.000-4.500 kWh al año suelen bastar entre 5 y 8 placas de 400-450 W, según la zona y la orientación."),
 ("¿En cuántos años se amortizan?", "En una vivienda con buen autoconsumo suele estar entre 5 y 9 años, y las placas duran más de 25.")],
None,
"""function calc(){const kp=v('kp'),pr=kp*v('hs'),c=v('c'),au=Math.min(pr*v('au')/100,c),exd=pr-au,ah=au*v('p')+Math.min(exd*v('ex'),(c-au)*v('p')),inv=kp*v('ci');
show('r','Ahorro estimado al año:<b class="big">'+eur(ah)+'</b>Producción: '+nf(pr,0)+' kWh/año · Placas: <b>'+Math.ceil(kp*1000/v('wp'))+'</b> · Inversión: '+eur(inv)+'<br>Amortización: <b>'+(ah>0?nf(inv/ah,1)+' años':'—')+'</b> · Cubre el '+nf(Math.min(100,pr/c*100),0)+' % de tu consumo');}"""))

P.append(("coste-ducha-termo", "¿Cuánto cuesta una ducha con termo eléctrico? Calculadora | GastoLuz",
"Calcula cuánto cuesta cada ducha con termo eléctrico en luz y agua, y el gasto mensual de toda la familia.",
"""<p class="lead">Calcula lo que pagas en luz y agua por cada ducha y al mes.</p>
<div class="card"><div class="row"><div><label for="m">Minutos por ducha</label><input id="m" inputmode="decimal" value="8"></div><div><label for="q">Caudal (litros/min)</label><input id="q" inputmode="decimal" value="9"></div>
<div><label for="tf">Agua fría (°C)</label><input id="tf" inputmode="decimal" value="15"></div><div><label for="tc">Temperatura de la ducha (°C)</label><input id="tc" inputmode="decimal" value="38"></div>
<div><label for="p">Precio kWh (€)</label><input id="p" inputmode="decimal" value="0,15"></div><div><label for="pa">Precio agua (€/m³)</label><input id="pa" inputmode="decimal" value="2"></div>
<div><label for="n">Duchas al mes (toda la casa)</label><input id="n" inputmode="numeric" value="90"></div><div><label for="ef">Rendimiento del termo (%)</label><input id="ef" inputmode="decimal" value="85"></div></div>
<button onclick="calc()">Calcular</button><div class="res" id="r"></div></div>
<h2>Cómo ahorrar en agua caliente</h2><ul><li>Una alcachofa de bajo caudal (6 L/min) reduce el gasto alrededor de un tercio.</li><li>Programa el termo para que caliente en horas valle.</li><li>Baja el termostato a 55-60 °C: suficiente y con menos pérdidas.</li><li>Cada minuto menos de ducha se nota en la factura.</li></ul>""",
[("¿Cuánto gasta un termo eléctrico al mes?", "Para una familia de 3-4 personas es habitual entre 15 y 35 € al mes solo en luz, según duchas, temperatura y tarifa."),
 ("¿Es mejor dejar el termo siempre encendido?", "Con un buen aislamiento, lo más eficiente suele ser programarlo para que caliente en las horas más baratas en lugar de mantenerlo siempre a máxima temperatura.")],
None,
"""function calc(){const l=v('m')*v('q'),kwh=l*(v('tc')-v('tf'))*1.163/1000/(v('ef')/100||1),cl=kwh*v('p'),ca=l/1000*v('pa'),t=cl+ca,n=v('n');
show('r','Coste por ducha:<b class="big">'+eur(t)+'</b>Luz: '+eur(cl)+' ('+nf(kwh,2)+' kWh) · Agua: '+eur(ca)+' ('+nf(l,0)+' L)<br>Al mes: <b>'+eur(t*n)+'</b> · Al año: '+eur(t*n*12));}"""))

# --- Precio de la luz hoy (PVPC por horas desde Red Eléctrica; pvpc.json lo actualiza un workflow del repo) ---
S['tools'].insert(0, ("precio-luz-hoy", "Precio de la luz hoy por horas", "PVPC hora a hora, las horas más baratas y las más caras, actualizado a diario.", "Precio luz hoy"))
S['aff']["precio-luz-hoy"] = ENCH + amz("enchufe inteligente programable", "Enchufes programables") + CNMC
P.append(("precio-luz-hoy", "Precio de la luz hoy por horas (PVPC): horas más baratas | GastoLuz",
"Precio de la luz hoy y mañana hora a hora en la tarifa PVPC, con las horas más baratas y más caras del día y el mejor momento para poner la lavadora. Datos oficiales de Red Eléctrica.",
"""<p class="lead">Precio del kWh en la tarifa regulada PVPC para cada hora, con datos oficiales de Red Eléctrica. El precio de mañana se publica cada tarde, hacia las 20:30.</p>
<div class="card"><div id="tabs" class="share" style="margin:0 0 12px"></div><div id="pv">Cargando precios…</div></div>
<h2>Cómo leer el precio de la luz</h2><p>Si tienes la tarifa regulada (PVPC), el precio que pagas por cada kWh cambia cada hora. En verde están las horas más baratas del día, en amarillo las intermedias y en rojo las más caras. Programar la lavadora, el lavavajillas, la secadora o la carga del coche eléctrico en las horas verdes es la forma más sencilla de bajar la factura sin cambiar de hábitos.</p>
<p>El precio que mostramos es el término de energía del PVPC en €/kWh, con peajes y cargos incluidos, sin impuestos. A tu factura se suman el término de potencia, el impuesto eléctrico, el alquiler del contador y el IVA. Si tienes una tarifa del mercado libre con precio fijo, el precio por horas no te afecta: mira el precio del kWh en tu contrato.</p>
<h2>¿Cuánto me cuesta usar un electrodoméstico ahora?</h2><p>Con el precio de esta hora puedes calcular lo que te cuesta cada aparato en la <a href="consumo-electrodomesticos.html">calculadora de consumo de electrodomésticos</a>, el <a href="coste-aire-acondicionado.html">aire acondicionado</a> o la <a href="coste-calefaccion-electrica.html">calefacción eléctrica</a>.</p>
<p class="note">Fuente: Red Eléctrica de España (REE), precios del mercado eléctrico, PVPC. Actualización automática varias veces al día.</p>""",
[("¿A qué hora es más barata la luz hoy?", "Arriba tienes las horas ordenadas por precio: las marcadas en verde son las más baratas del día según el PVPC publicado por Red Eléctrica."),
 ("¿Cuándo se publica el precio de la luz de mañana?", "Red Eléctrica publica el precio PVPC del día siguiente cada tarde, normalmente hacia las 20:30. En cuanto está disponible, aparece aquí en la pestaña de mañana."),
 ("¿Me afecta el precio por horas si estoy en el mercado libre?", "Solo si tu contrato es indexado o tiene precios por tramos. Con un precio fijo por kWh pagas lo mismo a cualquier hora."),
 ("¿Qué es el PVPC?", "El Precio Voluntario para el Pequeño Consumidor es la tarifa regulada de la luz para potencias de hasta 10 kW. Su precio cambia cada hora según el mercado mayorista.")],
"Precio de la luz hoy por horas",
"""let D=null,dia=null;
const fmtD=new Intl.DateTimeFormat('sv-SE',{timeZone:'Europe/Madrid'});
const hNow=()=>Number(new Intl.DateTimeFormat('es-ES',{timeZone:'Europe/Madrid',hour:'2-digit',hourCycle:'h23'}).format(new Date()));
const pr=x=>x.toLocaleString('es-ES',{minimumFractionDigits:4,maximumFractionDigits:4})+' €/kWh';
const hh=h=>String(h).padStart(2,'0')+':00';
function nombre(k){const hoy=fmtD.format(new Date());const m=fmtD.format(new Date(Date.now()+864e5));return k==hoy?'Hoy':k==m?'Mañana':new Date(k+'T12:00').toLocaleDateString('es-ES',{weekday:'long',day:'numeric',month:'long'});}
function tabs(){const t=document.getElementById('tabs');const ks=Object.keys(D.dias).filter(k=>k>=fmtD.format(new Date(Date.now()-864e5)));
t.innerHTML=ks.map(k=>'<a href="#" data-k="'+k+'" onclick="dia=this.dataset.k;pinta();return false" style="'+(k==dia?'background:#0b7285;color:#fff':'')+'">'+nombre(k)+'</a>').join('');}
function pinta(){tabs();const v=D.dias[dia];const ps=v.map(x=>x[1]);const s=[...ps].sort((a,b)=>a-b);const t1=s[Math.floor(s.length/3)],t2=s[Math.floor(2*s.length/3)];
const col=p=>p<t1?'#2f9e44':p<t2?'#f59f00':'#e03131';const avg=ps.reduce((a,b)=>a+b,0)/ps.length;const mx=s[s.length-1];
const esHoy=dia==fmtD.format(new Date());const hn=hNow();const cur=esHoy?v.find(x=>x[0]==hn):null;
let best=null;for(let i=0;i+1<v.length;i++){const c=v[i][1]+v[i+1][1];if(!best||c<best[1])best=[v[i][0],c];}
const mn=v.reduce((a,b)=>b[1]<a[1]?b:a),mxh=v.reduce((a,b)=>b[1]>a[1]?b:a);
let h='';if(cur)h+='<div style="font-size:1.05rem">Ahora ('+hh(cur[0])+' a '+hh((cur[0]+1)%24)+'):<b class="big" style="font-size:2rem;display:block;color:'+col(cur[1])+'">'+pr(cur[1])+'</b></div>';
h+='<table><tr><td>Precio medio</td><td><b>'+pr(avg)+'</b></td></tr><tr><td>Hora más barata</td><td><b style="color:#2f9e44">'+hh(mn[0])+'</b> · '+pr(mn[1])+'</td></tr><tr><td>Hora más cara</td><td><b style="color:#e03131">'+hh(mxh[0])+'</b> · '+pr(mxh[1])+'</td></tr><tr><td>Mejor momento para la lavadora (2 h)</td><td><b>'+hh(best[0])+' a '+hh((best[0]+2)%24)+'</b></td></tr></table>';
h+='<div style="display:flex;align-items:flex-end;gap:2px;height:160px;margin:18px 0 4px">'+v.map(x=>'<div title="'+hh(x[0])+' '+pr(x[1])+'" style="flex:1;height:'+Math.max(6,Math.round(x[1]/mx*100))+'%;background:'+col(x[1])+';border-radius:3px 3px 0 0;'+(cur&&x[0]==cur[0]?'outline:2px solid #1d2433;':'')+'"></div>').join('')+'</div>';
h+='<div style="display:flex;justify-content:space-between;font-size:.75rem;color:#6b7185"><span>00h</span><span>06h</span><span>12h</span><span>18h</span><span>23h</span></div>';
h+='<h3 style="margin-top:20px">Todas las horas</h3><table><tr><th>Hora</th><th>€/kWh</th></tr>'+v.map(x=>'<tr'+(cur&&x[0]==cur[0]?' style="font-weight:700"':'')+'><td><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:'+col(x[1])+';margin-right:8px"></span>'+hh(x[0])+' a '+hh((x[0]+1)%24)+'</td><td>'+pr(x[1])+'</td></tr>').join('')+'</table>';
document.getElementById('pv').innerHTML=h;}
fetch('pvpc.json',{cache:'no-store'}).then(r=>r.json()).then(j=>{D=j;const ks=Object.keys(D.dias).sort();const hoy=fmtD.format(new Date());dia=ks.includes(hoy)?hoy:ks[ks.length-1];pinta();}).catch(()=>{document.getElementById('pv').textContent='No hemos podido cargar los precios. Inténtalo de nuevo en unos minutos.';});"""))
