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

P.append(("coste-ducha-termo", "¿Cuánto cuesta una ducha con termo eléctrico? Luz y agua | GastoLuz",
"Calcula cuánto cuesta cada ducha con termo eléctrico en luz y agua y lo que gasta tu familia al mes. En invierno, con el agua más fría, el gasto sube: compruébalo aquí.",
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

# --- Calculadora de la factura de la luz ---
S['tools'].insert(1, ("calcular-factura-luz", "Calcula tu factura de la luz", "Desglose completo: potencia, energía, impuesto eléctrico, contador e IVA.", "Factura"))
S['aff']["calcular-factura-luz"] = CNMC + ENCH
P.append(("calcular-factura-luz", "Calcular factura de la luz: simulador con impuestos 2026 | GastoLuz",
"Calcula tu factura de la luz paso a paso: término de potencia, energía, bono social, impuesto eléctrico, alquiler del contador e IVA. Comprueba si tu recibo está bien.",
"""<p class="lead">Copia los datos de tu contrato o de tu última factura y verás el recibo desglosado línea a línea, como lo calcula tu compañía.</p>
<div class="card"><div class="row"><div><label for="kw">Potencia contratada (kW)</label><input id="kw" inputmode="decimal" value="3,45"></div>
<div><label for="d">Días de la factura</label><input id="d" inputmode="numeric" value="30"></div>
<div><label for="p1">Precio potencia punta (€/kW·día)</label><input id="p1" inputmode="decimal" value="0,10"></div>
<div><label for="p2">Precio potencia valle (€/kW·día)</label><input id="p2" inputmode="decimal" value="0,04"></div>
<div><label for="e">Consumo (kWh)</label><input id="e" inputmode="decimal" value="270"></div>
<div><label for="pe">Precio medio de la energía (€/kWh)</label><input id="pe" inputmode="decimal" value="0,15"></div>
<div><label for="bs">Financiación bono social (€/día)</label><input id="bs" inputmode="decimal" value="0,02469"></div>
<div><label for="ct">Alquiler del contador (€/día)</label><input id="ct" inputmode="decimal" value="0,02663"></div></div>
<label for="iv">Impuesto indirecto</label><select id="iv"><option value="21">Península y Baleares: IVA 21 %</option><option value="10">IVA reducido 10 % (solo si el Gobierno lo activa)</option><option value="0">Canarias, vivienda hasta 10 kW: IGIC 0 %</option><option value="3">Canarias, resto: IGIC 3 %</option><option value="1">Ceuta y Melilla: IPSI 1 %</option></select>
<button onclick="calc()">Calcular factura</button><div class="res" id="r"></div></div>
<p class="note">Los precios de potencia y energía de ejemplo son orientativos: pon los de tu contrato (vienen en la factura, en «Detalle de la factura»). Si el contador es tuyo, pon 0 en el alquiler. Con tarifa PVPC, usa el precio medio del kWh que aparece en tu factura o mira el <a href="precio-luz-hoy.html">precio de la luz hoy</a>.</p>
<h2>Cómo se calcula la factura de la luz</h2><ol><li><b>Término de potencia</b> = kW × días × (precio punta + precio valle).</li><li><b>Término de energía</b> = kWh consumidos × precio del kWh.</li><li><b>Financiación del bono social</b> = importe diario × días.</li><li><b>Impuesto especial sobre la electricidad</b> = 5,11269632 % de la suma de los tres anteriores (con un mínimo de 1 € por cada 1.000 kWh).</li><li><b>Alquiler del contador</b> = importe diario × días (el regulado para un contador digital monofásico es 0,02663 €/día, unos 0,81 € al mes).</li><li><b>IVA</b> = 21 % de todo lo anterior, impuesto eléctrico incluido.</li></ol>
<p><b>Ejemplo:</b> 3,45 kW, 30 días y 270 kWh a 0,15 €/kWh. Potencia: 3,45 × 30 × 0,14 = 14,49 €. Energía: 40,50 €. Bono social: 0,74 €. Impuesto eléctrico: 2,85 €. Contador: 0,80 €. IVA: 12,47 €. <b>Total: 71,85 €</b>, es decir, unos 0,27 € por cada kWh consumido cuando se suman todos los costes.</p>
<h2>Cómo pagar menos</h2><ul><li>Si la potencia pesa mucho en tu factura, comprueba si puedes <a href="potencia-contratada.html">bajar la potencia contratada</a>: cada kW menos ahorra unos 50 € al año con estos precios.</li><li>Mira qué aparatos gastan más con la <a href="consumo-electrodomesticos.html">calculadora de consumo de electrodomésticos</a>.</li><li>Compara ofertas en el <a href="https://comparador.cnmc.gob.es/" rel="noopener" target="_blank">comparador oficial de la CNMC</a> usando tu consumo real.</li></ul>""",
[("¿Cómo se calcula la factura de la luz?", "Se suman el término de potencia (kW × días × precio), el de energía (kWh × precio) y la financiación del bono social; sobre eso se aplica el impuesto eléctrico del 5,11 %, se añade el alquiler del contador y, al total, el IVA del 21 %."),
 ("¿Qué IVA tiene la luz ahora?", "En la península y Baleares, el 21 %. En la primavera de 2026 el Real Decreto-ley 7/2026 lo bajó temporalmente al 10 % (y el impuesto eléctrico al 0,5 %) para contratos de hasta 10 kW; las facturas emitidas desde el 1 de junio de 2026 vuelven al 21 % y al 5,11 %. Canarias paga IGIC y Ceuta y Melilla, IPSI."),
 ("¿Cuánto es el impuesto eléctrico?", "El 5,11269632 % de la suma de potencia, energía y bono social, con un mínimo de 1 € por cada 1.000 kWh consumidos en viviendas."),
 ("¿Cuánto se paga por el alquiler del contador?", "El precio regulado de un contador digital monofásico de alquiler es de 0,02663 € al día, unos 0,81 € al mes más IVA. Si el contador es de tu propiedad, no pagas alquiler.")],
"Calculadora de la factura de la luz",
"""function calc(){const d=v('d'),pot=v('kw')*d*(v('p1')+v('p2')),en=v('e')*v('pe'),bs=v('bs')*d,b1=pot+en+bs,iee=Math.max(b1*0.0511269632,v('e')*0.001),ct=v('ct')*d,b2=b1+iee+ct,t=+document.getElementById('iv').value,iva=b2*t/100,tot=b2+iva;
const L=[['Término de potencia',pot],['Término de energía',en],['Financiación bono social',bs],['Impuesto eléctrico (5,11 %)',iee],['Alquiler del contador',ct],['Impuesto indirecto ('+nf(t)+' %)',iva]];
const km=v('e')>0?' · '+nf(tot/v('e'),3)+' € por kWh con todo incluido':'';
show('r','Total de la factura:<b class="big">'+eur(tot)+'</b>'+nf(d,0)+' días'+km+'<table>'+L.map(x=>'<tr><td>'+x[0]+'</td><td style="text-align:right">'+eur(x[1])+'</td><td style="text-align:right;color:#6b7185">'+nf(x[1]/tot*100,0)+' %</td></tr>').join('')+'</table>');}"""))

# --- Consumo de la freidora de aire frente al horno ---
S['tools'].insert(3, ("consumo-freidora-aire", "Freidora de aire vs horno", "Cuánto gasta la airfryer, el horno o el microondas en cada receta.", ""))
S['aff']["consumo-freidora-aire"] = amz("freidora de aire", "Freidoras de aire") + amz("papel freidora de aire", "Papel y moldes para airfryer") + ENCH
P.append(("consumo-freidora-aire", "Consumo de la freidora de aire: cuánto gasta frente al horno | GastoLuz",
"Calcula cuánto gasta tu freidora de aire en cada receta y compárala con el horno y el microondas, con el precio de la luz de hoy. Ejemplo con patatas, pollo y bizcocho.",
"""<p class="lead">Elige la receta o pon tus tiempos y verás lo que cuesta cocinarla en la freidora de aire, en el horno y en el microondas, con el precio medio de la luz de hoy.</p>
<div class="card"><label for="rc">Receta</label><select id="rc" onchange="rec()"><option value="15,20,8">Patatas fritas (400 g)</option><option value="22,35,0">Muslos de pollo</option><option value="10,15,3">Verduras asadas</option><option value="35,40,0">Bizcocho</option><option value="12,15,6">Recalentar comida</option><option value="0,0,0">Personalizado</option></select>
<div class="row"><div><label for="ta">Minutos en freidora de aire</label><input id="ta" inputmode="numeric" value="15"></div>
<div><label for="pa">Potencia de la freidora (W)</label><input id="pa" inputmode="numeric" value="1500"></div>
<div><label for="th">Minutos en el horno (sin precalentar)</label><input id="th" inputmode="numeric" value="20"></div>
<div><label for="ph">Potencia del horno (W)</label><input id="ph" inputmode="numeric" value="2200"></div>
<div><label for="tm">Minutos en microondas (0 si no sirve)</label><input id="tm" inputmode="numeric" value="8"></div>
<div><label for="pr">Precio de la luz (€/kWh)</label><input id="pr" inputmode="decimal" value="0,15"></div></div>
<label class="chk"><input type="checkbox" id="pc" checked><span>Precalentar el horno 10 minutos</span></label>
<label for="vs">Veces a la semana</label><input id="vs" inputmode="numeric" value="3">
<button onclick="calc()">Comparar consumo</button><div class="res" id="r"></div></div>
<p class="note" id="pn">El precio por defecto es orientativo. Con tarifa regulada (PVPC) usamos la media de hoy publicada por Red Eléctrica; con tarifa fija, pon el precio del kWh de tu contrato.</p>
<h2>Cómo calculamos el consumo</h2><p>Consumo (kWh) = potencia (W) × minutos ÷ 60 ÷ 1.000 × <b>factor de uso</b>. Ni la freidora ni el horno tiran de toda su potencia todo el rato: la resistencia se apaga y se enciende para mantener la temperatura. Con medidas de enchufe, una freidora de aire trabaja de media alrededor del <b>80 %</b> del tiempo y un horno ya caliente en torno al <b>60 %</b>; el precalentado sí va a plena potencia. El microondas consume prácticamente su potencia nominal de entrada (usamos 1.000 W a máxima potencia).</p>
<table><tr><th>Aparato</th><th>Potencia típica</th><th>Por qué gasta lo que gasta</th></tr>
<tr><td>Freidora de aire</td><td>1.400 – 1.800 W</td><td>Cesta pequeña: calienta poco aire y no necesita precalentar.</td></tr>
<tr><td>Horno eléctrico</td><td>2.000 – 3.000 W</td><td>Calienta 50-70 litros de cavidad y pierde calor por la puerta.</td></tr>
<tr><td>Microondas</td><td>800 – 1.200 W</td><td>Calienta el agua del alimento, no el aire: es lo más barato para recalentar.</td></tr></table>
<p><b>Ejemplo:</b> unas patatas en la freidora de 1.500 W durante 15 minutos gastan 1,5 × 0,25 × 0,8 = 0,30 kWh, unos 4,5 céntimos a 0,15 €/kWh. En un horno de 2.200 W con 10 minutos de precalentado y 20 de cocción: 0,37 + 0,44 = 0,81 kWh, unos 12 céntimos. Haciéndolo 3 veces por semana, la freidora ahorra unos 12 € al año. No es una fortuna, pero en raciones pequeñas la airfryer gasta menos de la mitad que el horno.</p>
<h2>Cuándo compensa cada uno</h2><ul><li><b>Raciones para 1-3 personas</b>: freidora de aire, siempre.</li><li><b>Mucha cantidad o bandejas grandes</b>: el horno, porque en la freidora tendrías que hacer varias tandas.</li><li><b>Recalentar</b>: el microondas, aunque la freidora deja mejor textura en rebozados y pizza.</li><li>Cocina en las <a href="precio-luz-hoy.html">horas más baratas del día</a> si tienes PVPC y mide tus aparatos reales con un enchufe medidor. Para ver el resto de la casa, usa la calculadora de <a href="consumo-electrodomesticos.html">consumo de electrodomésticos</a>.</li></ul>""",
[("¿Cuánto gasta una freidora de aire por hora?", "Una de 1.500 W gasta como máximo 1,5 kWh en una hora; como el termostato la apaga a ratos, en la práctica son unos 1,2 kWh, unos 18 céntimos a 0,15 €/kWh. Una receta normal de 15-20 minutos cuesta entre 4 y 6 céntimos."),
 ("¿Qué gasta más, el horno o la freidora de aire?", "El horno. Tiene más potencia, una cavidad mucho mayor que calentar y suele necesitar precalentado. Para la misma receta en cantidad pequeña, la freidora de aire gasta entre la mitad y un tercio."),
 ("¿Gasta mucho una freidora de aire en la factura de la luz?", "No. Usándola a diario 20 minutos son unos 0,4 kWh al día, unos 12 kWh al mes: menos de 2 € al mes a 0,15 €/kWh."),
 ("¿Es más barato el microondas que la freidora de aire?", "Para recalentar sí, porque tarda menos y calienta directamente el alimento. Para cocinar o dorar, la freidora es la opción más eficiente.")],
"Consumo de la freidora de aire frente al horno",
"""function rec(){const x=document.getElementById('rc').value.split(',').map(Number);if(x[0]){document.getElementById('ta').value=x[0];document.getElementById('th').value=x[1];document.getElementById('tm').value=x[2];}calc();}
function calc(){const p=v('pr'),w=v('vs')*52,a=v('pa')*v('ta')/60/1000*0.8,h=(document.getElementById('pc').checked?v('ph')*10/60/1000:0)+v('ph')*v('th')/60/1000*0.6,m=1000*v('tm')/60/1000;
const R=[['Freidora de aire',a],['Horno',h]];if(v('tm')>0)R.push(['Microondas',m]);const mn=Math.min(...R.map(x=>x[1]));
const c=x=>nf(x*p*100,1)+' cént.';
show('r','Freidora de aire:<b class="big">'+c(a)+' por receta</b>'+(h>0?'Gasta un <b>'+nf((1-a/h)*100,0)+' % menos</b> que el horno: ahorras <b>'+eur((h-a)*p*w)+' al año</b> cocinando '+nf(v('vs'),0)+' veces por semana.':'')+'<table><tr><th>Aparato</th><th>kWh</th><th>Por receta</th><th>Al año</th></tr>'+R.map(x=>'<tr><td>'+(x[1]==mn?'<b>'+x[0]+'</b>':x[0])+'</td><td>'+nf(x[1],2)+'</td><td>'+c(x[1])+'</td><td>'+eur(x[1]*p*w)+'</td></tr>').join('')+'</table>');}
fetch('pvpc.json',{cache:'no-store'}).then(r=>r.json()).then(j=>{const k=Object.keys(j.dias).sort(),d=new Date(),t=d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0'),H=j.dias[t]||j.dias[k[k.length-1]];if(!H||!H.length)return;const av=H.reduce((s,x)=>s+x[1],0)/H.length;document.getElementById('pr').value=av.toFixed(3).replace('.',',');document.getElementById('pn').innerHTML='Precio: media del PVPC de '+(j.dias[t]?'hoy':'último día disponible')+' según Red Eléctrica ('+av.toFixed(3).replace('.',',')+' €/kWh, impuestos aparte). Si tienes tarifa fija, cambia el precio por el de tu contrato. <a href="precio-luz-hoy.html">Ver precio por horas</a>.';calc();}).catch(()=>{});"""))

# --- Consumo de las luces de Navidad con el PVPC de las horas en que se encienden ---
S['tools'].insert(2, ("consumo-luces-navidad", "Consumo de las luces de Navidad", "Lo que cuestan tus guirnaldas y adornos al día y en toda la Navidad, con el precio de la luz por horas.", ""))
S['aff']["consumo-luces-navidad"] = amz("luces navidad led temporizador", "Luces LED con temporizador") + amz("enchufe temporizador programable", "Enchufes con temporizador") + ENCH
P.append(("consumo-luces-navidad", "Consumo de las luces de Navidad: cuánto gastan al día y al mes | GastoLuz",
"Calcula cuánto cuestan tus luces de Navidad LED o tradicionales con el precio de la luz de las horas en que las enciendes (PVPC de hoy), por día y en toda la temporada.",
"""<p class="lead">Pon cuántos adornos tienes, a qué hora los enciendes y cuántas horas. Calculamos el coste con el precio real de esas horas (PVPC de hoy, impuestos incluidos) y lo que ahorras con LED y temporizador.</p>
<div class="card"><b>Tus luces</b><p class="note" style="margin:2px 0 6px">Cantidad · vatios de cada uno (mira la etiqueta del transformador o la caja)</p><div id="it"></div>
<div class="row"><div><label for="hi">Hora de encendido</label><select id="hi"></select></div>
<div><label for="hh">Horas encendidas al día</label><input id="hh" inputmode="decimal" value="5"></div>
<div><label for="dd">Días de Navidad</label><input id="dd" inputmode="numeric" value="37"></div>
<div><label for="ta">Tarifa</label><select id="ta" onchange="calc()"><option value="p">PVPC (precio por horas)</option><option value="f">Precio fijo</option></select></div></div>
<label for="pf">Precio fijo del kWh si no tienes PVPC (€/kWh, sin impuestos)</label><input id="pf" inputmode="decimal" value="0,13">
<button onclick="calc()">Calcular coste</button><div class="res" id="r" aria-live="polite"></div>
<p class="note" id="pn">Precio PVPC: cargando el de hoy de Red Eléctrica…</p></div>
<h2>Cuánto consumen los adornos más habituales</h2><table><tr><th>Adorno</th><th>Potencia típica</th><th>5 h al día durante 37 días</th></tr>
<tr><td>Guirnalda LED de 100 luces</td><td>4 – 6 W</td><td>≈ 0,9 kWh</td></tr>
<tr><td>Guirnalda de bombillitas incandescentes (100)</td><td>35 – 45 W</td><td>≈ 7,4 kWh</td></tr>
<tr><td>Cortina LED de balcón o ventana</td><td>15 – 30 W</td><td>≈ 4,1 kWh</td></tr>
<tr><td>Figura o reno luminoso LED</td><td>20 – 40 W</td><td>≈ 5,6 kWh</td></tr>
<tr><td>Proyector LED o láser de fachada</td><td>5 – 10 W</td><td>≈ 1,4 kWh</td></tr></table>
<h2>Cómo se calcula</h2><p>Consumo (kWh) = vatios totales × horas ÷ 1.000. Con <b>PVPC</b> el precio cambia cada hora, así que sumamos hora a hora el precio publicado por Red Eléctrica para las horas en que tienes las luces encendidas, y añadimos el impuesto eléctrico (5,11 %) y el IVA (21 %). Las luces de Navidad suelen encenderse al anochecer, que coincide con las horas más caras del día, por eso el coste por kWh sale mayor que la media diaria.</p>
<p><b>Ejemplo:</b> un árbol con 2 guirnaldas LED (5 W cada una) y una cortina LED en el balcón (24 W) suman 34 W. Encendidas 5 horas al día son 0,17 kWh: con un precio de 0,30 €/kWh en esas horas, unos 6 céntimos al día con impuestos y <b>poco más de 2 € en toda la Navidad</b>. Si fueran guirnaldas incandescentes de 40 W, solo esas dos costarían unas cuatro veces más.</p>
<h2>Trucos para que no se note en la factura</h2><ul><li><b>Pásate al LED</b>: gasta hasta un 90 % menos que las bombillitas de toda la vida y apenas se calienta.</li><li><b>Usa temporizador</b>: dejarlas encendidas toda la noche multiplica el gasto por cuatro o cinco sin que nadie las vea.</li><li>Comprueba que las de exterior tengan protección <b>IP44</b> o superior y no conectes muchas guirnaldas en cadena a la misma regleta.</li></ul>
<p>Mira a qué horas está más cara la luz en el <a href="precio-luz-hoy.html">precio de la luz hoy por horas</a>, calcula el resto de la casa con el <a href="consumo-electrodomesticos.html">consumo de electrodomésticos</a> o compara bombillas con el <a href="ahorro-led.html">ahorro al cambiar a LED</a>. Y si este invierno usas radiadores, revisa el <a href="coste-calefaccion-electrica.html">coste de la calefacción eléctrica</a>.</p>""",
[("¿Cuánto gastan las luces de Navidad al mes?", "Muy poco si son LED: un árbol con un par de guirnaldas de 5 W encendidas 5 horas al día gasta unos 1,5 kWh al mes: alrededor de 50 céntimos con impuestos. Con guirnaldas incandescentes de 40 W el gasto se multiplica por ocho."),
 ("¿Cuánto consume una tira de luces LED de Navidad?", "Una guirnalda LED de 100 luces consume entre 4 y 6 W, es decir, unos 0,005 kWh por hora: alrededor de 2 céntimos por cada 10 horas encendida."),
 ("¿Gasta más dejar las luces de Navidad encendidas toda la noche?", "Sí: el consumo es proporcional a las horas. Pasar de 5 a 24 horas al día multiplica el gasto casi por cinco. Un enchufe con temporizador evita olvidos."),
 ("¿Las luces de Navidad suben mucho la factura de la luz?", "Con LED, normalmente menos de 3 € en toda la temporada. Lo que de verdad sube la factura en invierno es la calefacción eléctrica y el termo, no los adornos.")],
"Calculadora del consumo de las luces de Navidad",
"""const IT=[['Guirnalda LED (100 luces)',2,5],['Guirnalda incandescente (100 luces)',0,40],['Cortina LED de balcón o ventana',1,24],['Figura luminosa LED',0,30],['Proyector LED de fachada',0,8],['Otros adornos',0,10]];
document.getElementById('it').innerHTML=IT.map((x,i)=>'<div class="chk"><input type="number" min="0" id="q'+i+'" value="'+x[1]+'" aria-label="Cantidad de '+x[0]+'" oninput="calc()"><span>'+x[0]+'</span><input type="number" min="0" id="w'+i+'" value="'+x[2]+'" aria-label="Vatios de '+x[0]+'" oninput="calc()" style="width:76px"> W</div>').join('');
const hs=document.getElementById('hi');for(let h=0;h<24;h++)hs.insertAdjacentHTML('beforeend','<option value="'+h+'"'+(h==18?' selected':'')+'>'+String(h).padStart(2,'0')+':00</option>');hs.onchange=calc;
let HP=null;const TX=1.0511269632*1.21;
function pr(ini,hrs){if(document.getElementById('ta').value=='f'||!HP)return v('pf');let s=0,n=0;for(let k=0;k<Math.ceil(hrs);k++){const w=Math.min(1,hrs-k);s+=HP[(ini+k)%24]*w;n+=w;}return n?s/n:v('pf');}
function calc(){let W=0,Wi=0;IT.forEach((x,i)=>{const q=v('q'+i),w=v('w'+i);W+=q*w;if(i==0)Wi+=q*40;else if(i==2)Wi+=q*150;else Wi+=q*w;});
const ini=+hs.value,h=Math.min(24,v('hh')),d=v('dd'),p=pr(ini,h)*TX,kd=W*h/1000,cd=kd*p,ct=cd*d;
if(W<=0){show('r','Añade al menos un adorno con sus vatios.');return;}
const p24=pr(0,24)*TX,c24=W*24/1000*p24*d,cin=Wi*h/1000*p*d;
let t='Toda la Navidad ('+nf(d,0)+' días):<b class="big">'+eur(ct)+'</b>'+nf(W,0)+' W en total · '+nf(kd,3)+' kWh al día · <b>'+eur(cd)+' al día</b> a '+nf(p,3)+' €/kWh con impuestos.';
if(c24>ct*1.05)t+='<br>Si las dejaras encendidas las 24 horas: '+eur(c24)+' (<b>'+eur(c24-ct)+' más</b>). Un temporizador lo evita.';
if(Wi>W*1.05)t+='<br>Con guirnaldas y cortinas incandescentes en vez de LED pagarías unos '+eur(cin)+': el LED te ahorra <b>'+eur(cin-ct)+'</b>.';
show('r',t);}
fetch('pvpc.json',{cache:'no-store'}).then(r=>r.json()).then(j=>{const k=Object.keys(j.dias).sort(),d=new Date(),t=d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0'),H=j.dias[t]||j.dias[k[k.length-1]];if(!H||H.length<24)return;HP=[];H.forEach(x=>{HP[x[0]]=x[1];});
document.getElementById('pn').innerHTML='Precio PVPC de '+(j.dias[t]?'hoy':'último día disponible')+' por horas según Red Eléctrica. Con tarifa de precio fijo, elige «Precio fijo» y pon el de tu contrato. <a href="precio-luz-hoy.html">Ver todas las horas</a>.';calc();}).catch(()=>{document.getElementById('pn').textContent='No se ha podido cargar el PVPC de hoy: usamos el precio fijo indicado.';});"""))
