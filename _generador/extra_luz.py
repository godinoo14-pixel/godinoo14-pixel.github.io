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

P.append(("coste-cargar-coche-electrico", "Cuánto cuesta cargar un coche eléctrico en casa: por carga y cada 100 km | GastoLuz",
"Calcula cuánto cuesta cargar tu coche eléctrico en casa o en la calle: por carga, cada 100 km y al mes, con el precio de la luz por horas de hoy y la franja más barata para enchufarlo.",
"""<p class="lead">Pon la batería, cuánto quieres cargar y la potencia de tu enchufe. Calculamos el coste en casa con el precio de la luz de hoy (y la franja horaria más barata), en un cargador público y por cada 100 km.</p>
<div class="card"><div class="row"><div><label for="b">Batería útil (kWh)</label><input id="b" inputmode="decimal" value="60"></div><div><label for="pe">Pérdidas de carga (%)</label><input id="pe" inputmode="decimal" value="10"></div>
<div><label for="d">Desde (%)</label><input id="d" inputmode="numeric" value="20"></div><div><label for="h">Hasta (%)</label><input id="h" inputmode="numeric" value="80"></div>
<div><label for="kw">Potencia de carga en casa</label><select id="kw"><option value="2.3">Enchufe normal (2,3 kW)</option><option value="3.7">Wallbox 3,7 kW</option><option value="7.4" selected>Wallbox 7,4 kW</option><option value="11">Wallbox trifásico 11 kW</option></select></div>
<div><label for="co">Consumo del coche (kWh/100 km)</label><input id="co" inputmode="decimal" value="16"></div>
<div><label for="pc">Precio kWh en casa (€, si no usas el PVPC de hoy)</label><input id="pc" inputmode="decimal" value="0,12"></div><div><label for="pp">Precio kWh cargador público (€)</label><input id="pp" inputmode="decimal" value="0,49"></div>
<div><label for="km">Kilómetros al mes</label><input id="km" inputmode="numeric" value="1000"></div></div>
<p class="note" id="pn">Cargando el precio de la luz por horas de hoy…</p>
<button onclick="calc()">Calcular</button><div class="res" id="r" aria-live="polite"></div></div>
<p class="note">Con discriminación horaria o tarifa regulada (PVPC), cargar de madrugada es lo más barato. En la calle, los cargadores rápidos suelen ser los más caros.</p>
<h2>Cómo se calcula</h2><p><b>Energía de la red</b> = batería × (hasta − desde) ÷ 100 × (1 + pérdidas). Las pérdidas en la carga van del 8 al 15 %: más con el enchufe normal y con frío. Multiplicada por el precio del kWh te da el coste. Una carga del 20 % al 80 % de una batería de 60 kWh son 36 kWh útiles, unos 40 kWh de la red: <b>4,75 €</b> en casa a 0,12 €/kWh y <b>19,40 €</b> en un cargador público a 0,49 €/kWh.</p>
<table><tr><th>Consumo del coche</th><th>Casa (0,12 €/kWh)</th><th>Casa (0,20 €/kWh)</th><th>Cargador público (0,49 €/kWh)</th></tr>
<tr><td>14 kWh/100 km (utilitario)</td><td>1,85 €</td><td>3,08 €</td><td>7,55 €</td></tr><tr><td>17 kWh/100 km (compacto)</td><td>2,24 €</td><td>3,74 €</td><td>9,16 €</td></tr><tr><td>21 kWh/100 km (SUV grande)</td><td>2,77 €</td><td>4,62 €</td><td>11,32 €</td></tr></table>
<p class="note">Coste cada 100 km con un 10 % de pérdidas de carga. Un coche de gasolina que gaste 6 l/100 km a 1,55 €/l cuesta 9,30 € cada 100 km.</p>
<p>Compara con lo que gastarías en combustible en el <a href="https://cochecuentas.es/electrico-vs-gasolina.html">comparador eléctrico vs gasolina</a> de CocheCuentas, mira el <a href="precio-luz-hoy.html">precio de la luz hoy por horas</a> y comprueba si necesitas subir tu <a href="potencia-contratada.html">potencia contratada</a> para instalar un wallbox.</p>""",
[("¿Cuánto cuesta llenar un coche eléctrico en casa?", "Con una batería de 60 kWh y el kWh a 0,12 €, una carga completa ronda los 8 €, contando pérdidas. Con la tarifa regulada (PVPC) y cargando de madrugada suele salir parecido o más barato."),
 ("¿Por qué no se carga siempre al 100 %?", "Para cuidar la batería, la mayoría de fabricantes recomiendan cargar al 80 % en el día a día y llegar al 100 % solo antes de viajes largos."),
 ("¿Cuánto tarda en cargar un coche eléctrico en un enchufe normal?", "A 2,3 kW, recuperar 40 kWh lleva unas 17 horas. Con un wallbox de 7,4 kW, unas 5,5 horas: cabe de sobra en la madrugada, cuando la luz es más barata."),
 ("¿Cuánto sube la factura de la luz con un coche eléctrico?", "Con 1.000 km al mes y un consumo de 16 kWh/100 km son unos 176 kWh con pérdidas: entre 21 y 35 € al mes según el precio del kWh. Si instalas un wallbox quizá necesites más potencia contratada.")],
None,
"""let HP=null;
function win(n){let best=null;for(let h0=0;h0<24;h0++){let s=0,rem=n,t=0;while(rem>0){const f=Math.min(1,rem);s+=HP[(h0+t)%24]*f;rem-=f;t++;}const avg=s/n;if(!best||avg<best[1])best=[h0,avg];}return best;}
function calc(){const k=v('b')*(v('h')-v('d'))/100*(1+v('pe')/100),kw=parseFloat(document.getElementById('kw').value),hr=k/kw,co=v('co'),pp=v('pp');
if(k<=0){show('r','Revisa la batería y los porcentajes de carga.');return;}
let pc=v('pc'),tx='';if(HP){const w=win(Math.min(24,Math.max(1,hr)));pc=w[1]*1.0511*1.21;tx=' (PVPC de hoy en la franja más barata: empezando a las <b>'+String(w[0]).padStart(2,'0')+':00</b>, con impuestos)';}
const ckm=co*(1+v('pe')/100)/100,mes=v('km')*ckm;
show('r','Coste de la carga en casa:<b class="big">'+eur(k*pc)+'</b>'+nf(k,1)+' kWh de la red a '+nf(pc,3)+' €/kWh'+tx+'<br>Tiempo de carga a '+nf(kw,1)+' kW: <b>'+nf(hr,1)+' h</b> · En cargador público: <b>'+eur(k*pp)+'</b> (ahorras '+eur(k*(pp-pc))+' cargando en casa)<br>Cada 100 km: <b>'+eur(ckm*100*pc)+'</b> en casa · Al mes ('+nf(v('km'),0)+' km): <b>'+eur(mes*pc)+'</b> en casa o '+eur(mes*pp)+' en la calle');}
fetch('pvpc.json',{cache:'no-store'}).then(r=>r.json()).then(j=>{const kk=Object.keys(j.dias).sort(),d=new Date(),t=d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0'),H=j.dias[t]||j.dias[kk[kk.length-1]];if(!H||H.length<24)throw 0;HP=[];H.forEach(x=>{HP[x[0]]=x[1];});
document.getElementById('pn').innerHTML='Precio en casa: tarifa regulada (PVPC) de Red Eléctrica hora a hora, con impuesto eléctrico e IVA. Si tienes otra tarifa, escribe tu precio y pulsa <a href="#" onclick="HP=null;calc();return false">usar mi precio</a>.';calc();}).catch(()=>{document.getElementById('pn').textContent='Usamos el precio que escribas: pon el de tu factura (término de energía con impuestos).';calc();});
calc();"""))

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

# --- Estufa de butano vs calefacción eléctrica vs bomba de calor (precio bombona: BOE-A-2026-23896; precio luz: pvpc.json) ---
S['tools'].insert(3, ("estufa-butano-vs-electrica", "Butano, radiador o bomba de calor", "Qué calefacción sale más barata con el precio de la bombona y de la luz de hoy.", "Butano vs luz"))
S['aff']["estufa-butano-vs-electrica"] = amz("detector monoxido de carbono", "Detectores de monóxido de carbono") + amz("radiador bajo consumo termostato", "Radiadores con termostato") + amz("termometro higrometro digital", "Termómetros de habitación")
P.append(("estufa-butano-vs-electrica", "Estufa de butano o eléctrica: ¿qué calefacción es más barata? | GastoLuz",
"Compara lo que cuesta calentarte con estufa de butano (bombona a 19,55 €), radiador eléctrico o aire acondicionado con bomba de calor, con el precio de la luz de hoy. Coste por hora, mes e invierno.",
"""<p class="lead">Indica cuánto calor necesitas y cuántas horas enciendes la calefacción. Te decimos lo que cuesta con <b>estufa de butano</b>, con <b>radiador o calefactor eléctrico</b> y con <b>bomba de calor</b> (aire acondicionado en modo calor), con el precio oficial de la bombona y el de la luz de hoy.</p>
<div class="card"><div class="row"><div><label for="kw">Calor necesario (kW)</label><input id="kw" inputmode="decimal" value="2,5"></div>
<div><label for="h">Horas al día</label><input id="h" inputmode="decimal" value="5"></div>
<div><label for="d">Días de calefacción en el invierno</label><input id="d" inputmode="numeric" value="120"></div>
<div><label for="bo">Precio de la bombona de 12,5 kg (€)</label><input id="bo" inputmode="decimal" value="19,55"></div>
<div><label for="p">Precio de la luz (€/kWh, con impuestos)</label><input id="p" inputmode="decimal" value="0,15"></div>
<div><label for="sc">Rendimiento de la bomba de calor (SCOP)</label><input id="sc" inputmode="decimal" value="3,5"></div></div>
<p class="note" id="pn">Como referencia, una habitación o salón de 20-25 m² necesita unos 2-2,5 kW; una estufa de butano típica da 4,2 kW al máximo y unos 1,5-2,5 kW en las posiciones intermedias.</p>
<button onclick="calc()">Comparar calefacciones</button><div class="res" id="r" aria-live="polite"></div></div>
<h2>Cuánto cuesta cada kWh de calor</h2><p>Una bombona de butano de 12,5 kg cuesta <b>19,55 €</b> desde el 17 de noviembre de 2026 (precio máximo regulado, revisado cada dos meses por la <a href="https://www.boe.es/boe/dias/2026/11/16/pdfs/BOE-A-2026-23896.pdf" rel="noopener" target="_blank">Resolución de 12 de noviembre de 2026 publicada en el BOE</a>; la próxima revisión es el tercer martes de enero). El butano da unos <b>12,7 kWh de calor por kilo</b>, es decir, unos 159 kWh por bombona. Como la estufa suelta en la habitación todo el calor de la combustión, cada kWh de calor sale a unos <b>0,12 €</b>.</p>
<p>Un radiador, calefactor, acumulador o panel eléctrico convierte 1 kWh de luz en 1 kWh de calor, así que paga el precio del kWh tal cual: entre 0,10 y 0,40 € según la hora con la tarifa regulada (<a href="precio-luz-hoy.html">mira el precio de la luz hoy</a>). Una <b>bomba de calor</b> (el aire acondicionado en modo calor) saca de 3 a 4 kWh de calor por cada kWh de luz, por eso suele ser la opción más barata.</p>
<p><b>Fórmulas:</b> butano = kWh de calor ÷ 12,7 × precio de la bombona ÷ 12,5. Eléctrico = kWh × precio de la luz. Bomba de calor = kWh × precio de la luz ÷ SCOP.</p>
<table><tr><th>2,5 kW · 5 h al día</th><th>Al día</th><th>Al mes</th></tr>
<tr><td>Estufa de butano (19,55 €)</td><td>1,54 €</td><td>46,18 €</td></tr>
<tr><td>Radiador eléctrico (0,15 €/kWh)</td><td>1,88 €</td><td>56,25 €</td></tr>
<tr><td>Bomba de calor (SCOP 3,5)</td><td>0,54 €</td><td>16,07 €</td></tr></table>
<p>Con 12,5 kWh de calor al día gastas casi 1 kg de butano: una bombona te dura unos <b>13 días</b>. El butano compensa frente al radiador cuando la luz pasa de unos 0,12 €/kWh, sobre todo en las horas punta de la tarde; si puedes usar el radiador en las horas valle, la diferencia se reduce o se invierte.</p>
<h2>Seguridad con la estufa de butano</h2><ul><li>Ventila la habitación: deja una rendija abierta y no la uses en dormitorios mientras duermes ni en baños.</li><li>Un <b>detector de monóxido de carbono</b> cuesta menos que una bombona y avisa a tiempo.</li><li>Revisa la goma y el regulador: tienen fecha de caducidad impresa.</li><li>La combustión suelta vapor de agua: si ves condensación en los cristales, ventila más.</li></ul>
<p>Calcula también el <a href="coste-calefaccion-electrica.html">coste de tu radiador eléctrico</a>, el del <a href="coste-aire-acondicionado.html">aire acondicionado con bomba de calor</a> o la <a href="potencia-contratada.html">potencia que necesitas</a> si enciendes varios aparatos a la vez.</p>""",
[("¿Qué es más barato, una estufa de butano o un radiador eléctrico?", "Con la bombona a 19,55 €, el calor del butano sale a unos 0,12 € por kWh. Un radiador eléctrico cuesta lo que pagues por el kWh de luz: si pagas más de 0,12-0,13 €/kWh con impuestos, el butano es más barato; en horas valle, el radiador puede salir mejor."),
 ("¿Cuánto dura una bombona de butano en una estufa?", "Depende de la potencia: al máximo (unos 4,2 kW) una estufa gasta alrededor de 0,33 kg por hora y la bombona dura unas 38 horas. En potencia media (unos 2 kW) dura unas 80 horas."),
 ("¿Cuánto cuesta la bombona de butano ahora?", "19,55 € la bombona de 12,5 kg, desde el 17 de noviembre de 2026. El precio máximo lo revisa el Ministerio cada dos meses y se publica en el BOE; la próxima revisión será el tercer martes de enero de 2027."),
 ("¿Es más barato calentar con aire acondicionado?", "Casi siempre. Una bomba de calor da de 3 a 4 kWh de calor por cada kWh de luz, así que calentar con ella cuesta entre la mitad y un tercio que con butano o con radiadores eléctricos.")],
"Estufa de butano o calefacción eléctrica: ¿qué sale más barato?",
"""function calc(){const kw=v('kw'),h=v('h'),dd=v('d'),bo=v('bo'),p=v('p'),sc=v('sc')||3.5,e=kw*h;
if(e<=0){show('r','Indica la potencia de calor y las horas al día.');return;}
const kg=e/12.7,cb=kg*bo/12.5,ce=e*p,cp=e*p/sc,o=[['Estufa de butano',cb],['Radiador o calefactor eléctrico',ce],['Bomba de calor (aire acondicionado)',cp]].sort((a,b)=>a[1]-b[1]);
let t='<div style="overflow-x:auto"><table style="font-size:.9rem"><tr><th>Sistema</th><th>Hora</th><th>Mes</th><th>Invierno</th></tr>'+o.map(x=>'<tr><td>'+x[0]+'</td><td>'+eur(x[1]/h)+'</td><td>'+eur(x[1]*30)+'</td><td><b>'+eur(x[1]*dd)+'</b></td></tr>').join('')+'</table></div>';
const eq=bo/12.5/12.7;
show('r','Lo más barato: <b>'+o[0][0].toLowerCase()+'</b><b class="big">'+eur(o[0][1]*dd)+' en el invierno</b>'+t+'Necesitas '+nf(e,1)+' kWh de calor al día: '+nf(kg,2)+' kg de butano, así que una bombona te dura <b>'+nf(12.5/kg,0)+' días</b> ('+nf(dd*kg/12.5,1)+' bombonas en el invierno).<br>El butano sale más barato que el radiador cuando la luz pasa de <b>'+nf(eq,3)+' €/kWh</b>.');}
fetch('pvpc.json',{cache:'no-store'}).then(r=>r.json()).then(j=>{const k=Object.keys(j.dias).sort(),d=new Date(),t=d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0'),H=j.dias[t]||j.dias[k[k.length-1]];if(!H||H.length<20)return;
const m=H.reduce((a,x)=>a+x[1],0)/H.length*1.0511*1.21;document.getElementById('p').value=m.toFixed(3).replace('.',',');document.getElementById('pn').innerHTML='Precio de la luz: media de hoy de la tarifa regulada (PVPC, Red Eléctrica) con impuesto eléctrico e IVA. Si tienes tarifa de mercado libre, pon el precio de tu factura. Una habitación de 20-25 m² necesita unos 2-2,5 kW.';calc();}).catch(()=>{});
calc();"""))

# --- Consumo de la secadora (por tipo, carga y hora con el PVPC de pvpc.json) ---
S['tools'].insert(4, ("consumo-secadora", "Consumo de la secadora", "Cuánto cuesta cada secado según el tipo de secadora y la hora a la que la pones.", "Secadora"))
S['aff']["consumo-secadora"] = amz("secadora bomba de calor", "Secadoras con bomba de calor") + amz("tendedero electrico", "Tendederos eléctricos") + amz("deshumidificador", "Deshumidificadores")
P.append(("consumo-secadora", "¿Cuánto gasta una secadora? Coste por ciclo y mejor hora para ponerla | GastoLuz",
"Calcula cuánto consume tu secadora por ciclo, al mes y al año: bomba de calor, condensación o evacuación. Con el precio de la luz por horas de hoy para ver a qué hora te sale más barata.",
"""<p class="lead">Elige tu tipo de secadora y cuántas veces la pones. Te decimos lo que cuesta cada secado y, con el precio de la luz por horas de hoy, a qué hora te sale más barato ponerla.</p>
<div class="card"><div class="row"><div><label for="ti">Tipo de secadora (8 kg)</label><select id="ti" onchange="tipo()"><option value="1.8|3">Bomba de calor</option><option value="4.5|2">Condensación</option><option value="4.8|2">Evacuación</option></select></div>
<div><label for="kw">Consumo por ciclo a carga completa (kWh)</label><input id="kw" inputmode="decimal" value="1,8"></div>
<div><label for="du">Duración del ciclo (horas)</label><input id="du" inputmode="decimal" value="3"></div>
<div><label for="ca">Carga</label><select id="ca"><option value="1">Llena</option><option value="0.6">Media carga</option></select></div>
<div><label for="cs">Secados por semana</label><input id="cs" inputmode="decimal" value="4"></div>
<div><label for="ho">Hora a la que la pones</label><select id="ho"></select></div>
<div><label for="p">Precio de la luz (€/kWh, si no usas el PVPC de hoy)</label><input id="p" inputmode="decimal" value="0,15"></div></div>
<p class="note" id="pn">Cargando el precio de la luz por horas de hoy…</p>
<button onclick="calc()">Calcular coste</button><div class="res" id="r" aria-live="polite"></div></div>
<h2>Cuánto gasta cada tipo de secadora</h2><p>Lo que más cambia el consumo es la tecnología. Las secadoras de <b>bomba de calor</b> reaprovechan el calor del aire y gastan menos de la mitad que las de <b>condensación</b> o <b>evacuación</b>, que calientan el aire con una resistencia. A cambio tardan más en secar.</p>
<table><tr><th>Secadora 8 kg, llena</th><th>kWh/ciclo</th><th>€/ciclo*</th><th>Al año*</th></tr>
<tr><td>Bomba de calor</td><td>1,5 a 2</td><td>0,27 €</td><td>56 €</td></tr><tr><td>Condensación</td><td>4 a 5</td><td>0,68 €</td><td>140 €</td></tr><tr><td>Evacuación</td><td>4,5 a 5</td><td>0,72 €</td><td>150 €</td></tr></table>
<p class="note">* Con la luz a 0,15 €/kWh y 4 secados a la semana. Valores típicos de referencia. El dato exacto está en la etiqueta energética o el manual: si indica kWh por 100 ciclos, divide entre 100; en etiquetas antiguas que dan kWh al año, divide entre 160 ciclos.</p>
<p><b>Fórmula:</b> coste por ciclo = kWh del ciclo × carga × precio medio de la luz durante las horas que funciona. Con la tarifa regulada (PVPC), el mismo secado puede costar el doble a las 20:00 que de madrugada o a mediodía.</p>
<h2>Trucos para gastar menos</h2><ul><li>Centrifuga la ropa en la lavadora a 1.200-1.400 rpm: cuanta menos agua lleve, menos tiempo de secadora.</li><li>Limpia el filtro de pelusa en cada uso y el condensador cada mes.</li><li>Llénala sin apretar: a media carga gasta más por cada kilo de ropa.</li><li>Ponla en las horas más baratas: mira el <a href="precio-luz-hoy.html">precio de la luz hoy por horas</a>.</li></ul>
<p>Compara con el resto de tu casa en el <a href="consumo-electrodomesticos.html">consumo de electrodomésticos</a>, comprueba si cabe en tu <a href="potencia-contratada.html">potencia contratada</a> junto con la calefacción o calcula tu <a href="calcular-factura-luz.html">factura de la luz</a>.</p>""",
[("¿Cuánto gasta una secadora por ciclo?", "Una de bomba de calor de 8 kg gasta entre 1,5 y 2 kWh por ciclo completo, unos 0,27 € con la luz a 0,15 €/kWh. Una de condensación o evacuación, entre 4 y 5 kWh: unos 0,70 € por secado."),
 ("¿Cuánto gasta una secadora al mes?", "Con 4 secados a la semana, unos 4,70 € al mes una de bomba de calor y entre 11,70 y 12,50 € una de condensación o evacuación, con el kWh a 0,15 €."),
 ("¿A qué hora es más barato poner la secadora?", "Con la tarifa regulada (PVPC), en las horas valle de madrugada (de 0 a 8 h) y, muchos días, a mediodía cuando hay mucha producción solar. Las horas más caras suelen ser de 19 a 22 h. Con tarifa de precio fijo da igual la hora.")],
"¿Cuánto gasta una secadora?",
"""let HP=null;const hs=document.getElementById('ho');for(let i=0;i<24;i++)hs.add(new Option(String(i).padStart(2,'0')+':00',i));hs.value=14;
function tipo(){const t=document.getElementById('ti').value.split('|');document.getElementById('kw').value=t[0].replace('.',',');document.getElementById('du').value=t[1];calc();}
function pm(h0,du){let s=0,w=0;for(let t=0;t<du;t+=0.25){const h=Math.floor(h0+t)%24;s+=HP[h];w++;}return s/w*1.0511*1.21;}
function calc(){const e=v('kw')*+document.getElementById('ca').value,du=Math.max(0.5,v('du')),cs=v('cs'),h0=+hs.value;
if(e<=0){show('r','Escribe el consumo por ciclo.');return;}
let pr=v('p'),txt='';if(HP){pr=pm(h0,du);let bh=0,bp=1e9,wh=0,wp=0;for(let h=0;h<24;h++){const x=pm(h,du);if(x<bp){bp=x;bh=h;}if(x>wp){wp=x;wh=h;}}
txt='<br>Hoy, la hora más barata para empezar es a las <b>'+String(bh).padStart(2,'0')+':00</b> ('+eur(e*bp)+' por secado) y la más cara a las '+String(wh).padStart(2,'0')+':00 ('+eur(e*wp)+').';}
const c=e*pr;show('r','Coste por secado:<b class="big">'+eur(c)+'</b>'+nf(e,2)+' kWh a '+nf(pr,3)+' €/kWh'+(HP?' (PVPC de hoy desde las '+String(h0).padStart(2,'0')+':00, con impuestos)':'')+'<br>Al mes: <b>'+eur(c*cs*52/12)+'</b> · Al año: <b>'+eur(c*cs*52)+'</b> ('+nf(e*cs*52,0)+' kWh)'+txt);}
fetch('pvpc.json',{cache:'no-store'}).then(r=>r.json()).then(j=>{const k=Object.keys(j.dias).sort(),d=new Date(),t=d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0'),H=j.dias[t]||j.dias[k[k.length-1]];if(!H||H.length<24)throw 0;HP=[];H.forEach(x=>{HP[x[0]]=x[1];});
document.getElementById('pn').innerHTML='Precio: tarifa regulada (PVPC) de Red Eléctrica hora a hora, con impuesto eléctrico e IVA. Si tienes una tarifa de precio fijo, escribe tu precio arriba y pulsa <a href="#" onclick="HP=null;calc();return false">usar mi precio fijo</a>.';calc();}).catch(()=>{document.getElementById('pn').textContent='Usamos el precio que escribas. Pon el de tu factura (término de energía con impuestos).';calc();});
calc();"""))

# --- Manta eléctrica, calientacamas, almohadilla y brasero: coste con el PVPC por horas frente a un radiador ---
S['tools'].insert(5, ("consumo-manta-electrica", "Consumo de la manta eléctrica", "Cuánto cuesta la manta, el calientacamas o el brasero frente a un radiador.", ""))
S['aff']["consumo-manta-electrica"] = amz("manta electrica sofa", "Mantas eléctricas") + amz("calientacamas electrico", "Calientacamas") + amz("brasero electrico mesa camilla", "Braseros eléctricos")
P.append(("consumo-manta-electrica", "¿Cuánto gasta una manta eléctrica? Coste por hora y al mes | GastoLuz",
"Calcula cuánto gasta tu manta eléctrica, calientacamas, almohadilla o brasero por hora, al día y al mes con el precio de la luz por horas de hoy, y cuánto ahorras frente a un radiador o calefactor.",
"""<p class="lead">Elige el aparato, cuántas horas lo usas y a qué hora lo enciendes. Te decimos lo que cuesta con el precio real de la luz de esas horas y cuánto ahorras frente a calentar la habitación con un radiador.</p>
<div class="card"><div class="row"><div><label for="ap">Aparato</label><select id="ap" onchange="pre()"><option value="100|60">Manta eléctrica de sofá (100 W)</option><option value="60|50">Calientacamas individual (60 W)</option><option value="120|50">Calientacamas de matrimonio (120 W)</option><option value="100|60">Almohadilla eléctrica (100 W)</option><option value="900|70">Brasero eléctrico de mesa camilla (900 W)</option></select></div>
<div><label for="w">Potencia (W)</label><input id="w" inputmode="decimal" value="100"></div>
<div><label for="f">Uso medio de la potencia (%)</label><input id="f" inputmode="decimal" value="60"></div>
<div><label for="hd">Horas al día</label><input id="hd" inputmode="decimal" value="3"></div>
<div><label for="ho">Hora a la que lo enciendes</label><select id="ho"></select></div>
<div><label for="dm">Días al mes</label><input id="dm" inputmode="numeric" value="30"></div>
<div><label for="rw">Radiador o calefactor para comparar (W)</label><input id="rw" inputmode="decimal" value="1500"></div>
<div><label for="p">Precio de la luz (€/kWh, si no usas el PVPC de hoy)</label><input id="p" inputmode="decimal" value="0,15"></div></div>
<p class="note" id="pn">Cargando el precio de la luz por horas de hoy…</p>
<button onclick="calc()">Calcular coste</button><div class="res" id="r" aria-live="polite"></div></div>
<h2>Cuánto gasta cada aparato</h2><p>Las mantas y calientacamas tienen potencias muy bajas porque calientan tu cuerpo, no el aire de la habitación. Además, con el termostato no funcionan siempre al máximo: en el nivel medio, el consumo real suele quedarse en la mitad o algo más de la potencia de la etiqueta. Por eso ponemos un <b>uso medio</b> del 50-70 %.</p>
<table><tr><th>3 horas al día (0,15 €/kWh)</th><th>kWh al día</th><th>Al día</th><th>Al mes</th></tr>
<tr><td>Manta eléctrica 100 W al 60 %</td><td>0,18</td><td>0,03 €</td><td>0,81 €</td></tr>
<tr><td>Calientacamas 60 W al 50 % (1 h)</td><td>0,03</td><td>0,005 €</td><td>0,14 €</td></tr>
<tr><td>Brasero eléctrico 900 W al 70 %</td><td>1,89</td><td>0,28 €</td><td>8,51 €</td></tr>
<tr><td>Radiador eléctrico 1.500 W al 80 %</td><td>3,6</td><td>0,54 €</td><td>16,20 €</td></tr></table>
<p><b>Fórmula:</b> coste = potencia (W) × uso medio (%) × horas ÷ 1.000 × precio del kWh. Con la tarifa regulada (PVPC), el precio de las 20:00 puede triplicar el de la madrugada, así que la hora a la que la usas también cuenta.</p>
<h2>Manta y calefacción más baja: el mejor combinado</h2><p>No hace falta elegir entre una cosa y otra. Según el <a href="https://www.idae.es/" rel="noopener" target="_blank">IDAE</a>, cada grado de más en el termostato sube el consumo de calefacción alrededor de un 7 %. Si en el sofá te tapas con la manta y bajas la calefacción de 22 a 20 °C, ahorras en torno a un 14 % de lo que gastas en calentar la casa, mientras la manta cuesta menos de un euro al mes. Para la cama, el calientacamas funciona mejor encendido 15-30 minutos antes de acostarte y apagado al meterte.</p>
<h2>Seguridad con la manta eléctrica</h2><ul><li>No la dobles ni la uses arrugada o debajo del cuerpo si el fabricante no lo permite: el cable interior puede dañarse y sobrecalentarse.</li><li>Si la usas en la cama, elige una con <b>apagado automático</b> o desenchúfala antes de dormir.</li><li>No la uses con bebés, ni con personas que no puedan apagarla solas.</li><li>Revísala al empezar el invierno: si ves el cable dañado, quemaduras o zonas que calientan más, cámbiala.</li></ul>
<p>Compara con el coste del <a href="coste-calefaccion-electrica.html">radiador eléctrico</a>, de una <a href="estufa-butano-vs-electrica.html">estufa de butano o la bomba de calor</a>, o revisa el <a href="precio-luz-hoy.html">precio de la luz hoy por horas</a>.</p>""",
[("¿Cuánto gasta una manta eléctrica al mes?", "Una manta de 100 W usada 3 horas al día en nivel medio gasta unos 5,4 kWh al mes: menos de 1 € con la luz a 0,15 €/kWh. Un radiador de 1.500 W las mismas horas cuesta unos 16 €."),
 ("¿Qué gasta más, una manta eléctrica o un calefactor?", "El calefactor, de lejos. Un calefactor de 2.000 W gasta en una hora lo que una manta de 100 W en unas 20 horas o más. La manta calienta solo a quien la usa, no toda la habitación."),
 ("¿Cuánto gasta un brasero eléctrico?", "Uno de 900 W usado a un 70 % de su potencia gasta unos 0,63 kWh por hora: algo menos de 10 céntimos por hora con la luz a 0,15 €/kWh. Unos 8,50 € al mes con 3 horas al día.")],
"¿Cuánto gasta una manta eléctrica?",
"""let HP=null;const hs=document.getElementById('ho');for(let i=0;i<24;i++)hs.add(new Option(String(i).padStart(2,'0')+':00',i));hs.value=20;
function pre(){const t=document.getElementById('ap').value.split('|');document.getElementById('w').value=t[0];document.getElementById('f').value=t[1];calc();}
function pm(h0,du){let s=0,w=0;for(let t=0;t<du;t+=0.25){s+=HP[Math.floor(h0+t)%24];w++;}return s/w*1.0511*1.21;}
function calc(){const kw=v('w')/1000*v('f')/100,hd=Math.min(24,v('hd')),dm=v('dm'),h0=+hs.value,rk=v('rw')/1000*0.8;
if(kw<=0||hd<=0){show('r','Escribe la potencia y las horas de uso.');return;}
let pr=v('p'),tx='';if(HP){pr=pm(h0,hd);let bh=0,bp=1e9;for(let h=0;h<24;h++){const x=pm(h,hd);if(x<bp){bp=x;bh=h;}}tx='<br>Hoy, la franja más barata empieza a las <b>'+String(bh).padStart(2,'0')+':00</b> ('+nf(bp,3)+' €/kWh).';}
const e=kw*hd,c=e*pr,cr=rk*hd*pr,ct=x=>x<1?nf(x*100,1)+' céntimos':eur(x);
let h='Coste al mes:<b class="big">'+eur(c*dm)+'</b>Por hora: <b>'+ct(kw*pr)+'</b> · Al día: <b>'+ct(c)+'</b> · '+nf(e,2)+' kWh al día a '+nf(pr,3)+' €/kWh'+(HP?' (PVPC de hoy desde las '+String(h0).padStart(2,'0')+':00, con impuestos)':'');
h+='<table style="margin-top:10px;font-size:.9rem"><tr><th></th><th>Al día</th><th>Al mes</th><th>Invierno (5 meses)</th></tr><tr><td>Tu aparato</td><td>'+ct(c)+'</td><td><b>'+eur(c*dm)+'</b></td><td>'+eur(c*dm*5)+'</td></tr><tr><td>Radiador '+nf(v('rw'),0)+' W</td><td>'+ct(cr)+'</td><td>'+eur(cr*dm)+'</td><td>'+eur(cr*dm*5)+'</td></tr></table>';
if(cr>c)h+='Usando tu aparato en lugar del radiador ahorras <b>'+eur((cr-c)*dm)+' al mes</b> ('+nf((1-c/cr)*100,0)+' % menos).';
show('r',h+tx);}
fetch('pvpc.json',{cache:'no-store'}).then(r=>r.json()).then(j=>{const k=Object.keys(j.dias).sort(),d=new Date(),t=d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0'),H=j.dias[t]||j.dias[k[k.length-1]];if(!H||H.length<24)throw 0;HP=[];H.forEach(x=>{HP[x[0]]=x[1];});
document.getElementById('pn').innerHTML='Precio: tarifa regulada (PVPC) de Red Eléctrica hora a hora, con impuesto eléctrico e IVA. Si tienes una tarifa de precio fijo, escribe tu precio y pulsa <a href="#" onclick="HP=null;calc();return false">usar mi precio fijo</a>.';calc();}).catch(()=>{document.getElementById('pn').textContent='Usamos el precio que escribas. Pon el de tu factura (término de energía con impuestos).';calc();});
document.querySelectorAll('.card input,.card select').forEach(e=>e.addEventListener(e.tagName=='SELECT'||e.type=='checkbox'||e.type=='date'?'change':'input',()=>calc()));
calc();"""))
