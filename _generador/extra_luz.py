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
"Cuánto cuesta cargar tu coche eléctrico en casa o en la calle: por carga, cada 100 km y al mes, con el precio de la luz de hoy y la hora más barata para enchufarlo.",
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
"Calcula cuánto cuesta una ducha con termo eléctrico en luz y agua, y lo que gasta tu casa al mes. En invierno el agua llega más fría y el gasto sube: compara invierno y verano con el precio de hoy.",
"""<p class="lead">Calcula lo que pagas en luz y agua por cada ducha y al mes. Elige la época del año: en invierno el agua de la red llega más fría y el termo tiene que trabajar más.</p>
<div class="card"><div class="row"><div><label for="ep">Época del año</label><select id="ep"><option value="10">Invierno (agua fría a unos 10 °C)</option><option value="15">Primavera u otoño (unos 15 °C)</option><option value="20">Verano (unos 20 °C)</option><option value="">Escribo yo la temperatura</option></select></div>
<div><label for="tf">Agua fría (°C)</label><input id="tf" inputmode="decimal" value="10"></div>
<div><label for="m">Minutos por ducha</label><input id="m" inputmode="decimal" value="8"></div><div><label for="q">Caudal de la ducha (litros/min)</label><input id="q" inputmode="decimal" value="9"></div>
<div><label for="tc">Temperatura de la ducha (°C)</label><input id="tc" inputmode="decimal" value="38"></div><div><label for="ef">Rendimiento del termo (%)</label><input id="ef" inputmode="decimal" value="85"></div>
<div><label for="p">Precio de la luz (€/kWh con impuestos)</label><input id="p" inputmode="decimal" value="0,18"></div><div><label for="pa">Precio del agua (€/m³)</label><input id="pa" inputmode="decimal" value="2"></div>
<div><label for="n">Duchas al mes (toda la casa)</label><input id="n" inputmode="numeric" value="90"></div></div>
<p class="note" id="pnt">Pon el precio del kWh de tu factura, con impuestos.</p>
<div class="res" id="r" aria-live="polite"></div></div>
<h2>Cómo se calcula el coste de una ducha</h2><p>Calentar un litro de agua un grado necesita 1,163 Wh. Por eso: <b>kWh = litros × (temperatura de la ducha − temperatura del agua fría) × 1,163 ÷ 1.000 ÷ rendimiento</b>. Los litros son los minutos por el caudal: una ducha de 8 minutos con una alcachofa de 9 L/min gasta 72 litros. Al coste de la luz se suma el del agua (precio del m³ de tu recibo, con alcantarillado y depuración).</p>
<table><tr><th>Ducha de 8 min a 38 °C (72 L)</th><th>kWh</th><th>Luz</th><th>Luz + agua</th></tr>
<tr><td>Invierno (agua a 10 °C)</td><td>2,76</td><td>0,50 €</td><td>0,64 €</td></tr>
<tr><td>Primavera u otoño (15 °C)</td><td>2,27</td><td>0,41 €</td><td>0,55 €</td></tr>
<tr><td>Verano (20 °C)</td><td>1,77</td><td>0,32 €</td><td>0,46 €</td></tr></table>
<p class="note">Con la luz a 0,18 €/kWh, el agua a 2 €/m³ y un termo con un 85 % de rendimiento. La temperatura del agua de la red varía según la ciudad y la época; si quieres afinar, mídela con un termómetro en el grifo de agua fría.</p>
<p><b>Ejemplo:</b> en una casa de tres personas que se duchan a diario (90 duchas al mes), en invierno las duchas cuestan unos 45 € de luz y 13 € de agua al mes; en verano, la luz baja a unos 29 €. A eso hay que sumarle las pérdidas del termo, que mantiene el agua caliente todo el día: un termo de 80 litros bien aislado pierde del orden de 1 kWh al día, otros 5 € al mes.</p>
<h2>Cómo ahorrar en agua caliente</h2><ul><li>Una alcachofa de bajo caudal (6 L/min en vez de 9-12) reduce el gasto alrededor de un tercio sin notar mucho la diferencia.</li><li>Con tarifa PVPC o de discriminación horaria, programa el termo con un temporizador para que caliente en horas valle (de 0 a 8 h y fines de semana). Mira las horas más baratas en el <a href="precio-luz-hoy.html">precio de la luz hoy</a>.</li><li>Baja el termostato a unos 55-60 °C: es suficiente para la ducha y reduce pérdidas. No lo bajes mucho más de forma permanente, para evitar la proliferación de legionela.</li><li>Cada minuto menos de ducha ahorra unos 9 litros y, en invierno, unos 6 céntimos.</li></ul>
<p>Si quieres ver el peso del termo frente al resto de la casa, usa la <a href="consumo-electrodomesticos.html">calculadora de consumo de electrodomésticos</a> o <a href="calcular-factura-luz.html">calcula tu factura de la luz</a>. Para la calefacción, compara el <a href="coste-calefaccion-electrica.html">radiador eléctrico</a> con la <a href="estufa-butano-vs-electrica.html">estufa de butano</a>.</p>""",
[("¿Cuánto gasta un termo eléctrico al mes?", "Para una familia de 3-4 personas es habitual entre 25 y 55 € al mes solo en luz, contando las duchas y las pérdidas del termo. En invierno puede costar más de la mitad que en verano porque el agua entra más fría."),
 ("¿Cuánto cuesta una ducha de 10 minutos con termo eléctrico?", "Con una alcachofa de 9 L/min (90 litros) a 38 °C, unos 3,4 kWh en invierno: algo más de 60 céntimos de luz a 0,18 €/kWh, más unos 18 céntimos de agua."),
 ("¿Es mejor dejar el termo siempre encendido o apagarlo?", "Con un buen aislamiento, lo más eficiente suele ser programarlo para que caliente en las horas más baratas y que mantenga el agua el resto del día. Encenderlo y apagarlo varias veces al día no ahorra mucho porque tiene que recalentar toda el agua."),
 ("¿Por qué gasto más luz en invierno con el termo?", "Porque el agua de la red llega más fría: si entra a 10 °C en vez de a 20 °C, el termo tiene que subirla 28 grados en lugar de 18 para una ducha a 38 °C, más de un 50 % de energía extra.")],
"¿Cuánto cuesta una ducha con termo eléctrico?",
"""let HM=null;
document.getElementById('ep').addEventListener('change',()=>{const x=document.getElementById('ep').value;if(x)document.getElementById('tf').value=x;calc();});
function calc(){const l=v('m')*v('q'),dt=v('tc')-v('tf'),pr=HM||v('p');if(l<=0||dt<=0){show('r','Revisa los minutos, el caudal y que la ducha esté más caliente que el agua fría.');return;}
const kwh=l*dt*1.163/1000/((v('ef')||100)/100),cl=kwh*pr,ca=l/1000*v('pa'),t=cl+ca,n=v('n');
let h='Coste por ducha:<b class="big">'+eur(t)+'</b>Luz: '+eur(cl)+' ('+nf(kwh,2)+' kWh a '+nf(pr,3)+' €/kWh'+(HM?', PVPC de hoy':'')+') · Agua: '+eur(ca)+' ('+nf(l,0)+' L)<br>Al mes: <b>'+eur(t*n)+'</b> ('+eur(cl*n)+' de luz) · Al año: '+eur(t*n*12);
if(v('q')>6){const s6=(v('q')-6)*v('m')*(dt*1.163/1000/((v('ef')||100)/100)*pr+v('pa')/1000)*n;h+='<br>Con una alcachofa de 6 L/min ahorrarías unos <b>'+eur(s6)+' al mes</b>.';}
show('r',h);}
fetch('pvpc.json',{cache:'no-store'}).then(r=>r.json()).then(j=>{const kk=Object.keys(j.dias).sort(),d=new Date(),t=d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0'),H=j.dias[t]||j.dias[kk[kk.length-1]];if(!H||H.length<24)throw 0;
const pv=H.filter(x=>x[0]<8).reduce((s,x)=>s+x[1],0)/8*1.0511*1.21,pm=H.reduce((s,x)=>s+x[1],0)/H.length*1.0511*1.21;window.PV=pv;window.PM=pm;
document.getElementById('pnt').innerHTML='Tarifa regulada (PVPC) de Red Eléctrica hoy, con impuestos: media del día <b>'+nf(pm,3)+' €/kWh</b>; si el termo calienta de 0 a 8 h, <b>'+nf(pv,3)+' €/kWh</b>. <a href="#" onclick="HM=window.PV;calc();return false">Calcular con el termo de noche</a> · <a href="#" onclick="HM=window.PM;calc();return false">con la media de hoy</a> · <a href="#" onclick="HM=null;calc();return false">usar mi precio</a>';calc();}).catch(()=>{document.getElementById('pnt').textContent='Usamos el precio que escribas: pon el de tu factura con impuestos.';calc();});
document.querySelectorAll('.card input,.card select').forEach(e=>e.addEventListener(e.tagName=='SELECT'?'change':'input',()=>calc()));
calc();"""))

# --- Precio de la luz hoy (PVPC por horas desde Red Eléctrica; pvpc.json lo actualiza un workflow del repo) ---
S['tools'].insert(0, ("precio-luz-hoy", "Precio de la luz hoy por horas", "PVPC hora a hora, las horas más baratas y las más caras, actualizado a diario.", "Precio luz hoy"))
S['aff']["precio-luz-hoy"] = ENCH + amz("enchufe inteligente programable", "Enchufes programables") + CNMC
P.append(("precio-luz-hoy", "Precio de la luz hoy y mañana por horas (PVPC): horas más baratas | GastoLuz",
"Precio de la luz hoy y mañana hora a hora en la tarifa PVPC, con las horas más baratas y más caras del día y el mejor momento para poner la lavadora. Datos oficiales de Red Eléctrica.",
"""<p class="lead">Precio del kWh en la tarifa regulada PVPC para cada hora, con datos oficiales de Red Eléctrica. El precio de mañana se publica cada tarde, hacia las 20:30.</p>
<div class="card"><div id="tabs" class="share" style="margin:0 0 12px"></div><div id="pv">Cargando precios…</div></div>
<h2>Cómo leer el precio de la luz</h2><p>Si tienes la tarifa regulada (PVPC), el precio que pagas por cada kWh cambia cada hora. En verde están las horas más baratas del día, en amarillo las intermedias y en rojo las más caras. Programar la lavadora, el lavavajillas, la secadora o la carga del coche eléctrico en las horas verdes es la forma más sencilla de bajar la factura sin cambiar de hábitos.</p>
<p>El precio que mostramos es el término de energía del PVPC en €/kWh, con peajes y cargos incluidos, sin impuestos. A tu factura se suman el término de potencia, el impuesto eléctrico, el alquiler del contador y el IVA. Si tienes una tarifa del mercado libre con precio fijo, el precio por horas no te afecta: mira el precio del kWh en tu contrato.</p>
<h2>Por qué la luz suele ser más barata de madrugada y el fin de semana</h2><p>El precio del PVPC suma el mercado mayorista y los peajes y cargos, que tienen tres tramos: <b>punta</b> (de 10:00 a 14:00 y de 18:00 a 22:00), <b>llano</b> (de 8:00 a 10:00, de 14:00 a 18:00 y de 22:00 a 24:00) y <b>valle</b> (de 0:00 a 8:00). Los sábados, domingos y festivos nacionales todas las horas son valle, por eso ese día los precios suelen bajar. En invierno, las horas más caras suelen ser las de la tarde-noche, cuando se juntan calefacción, cocina e iluminación y hay menos producción solar; a mediodía, el sol suele abaratar el mercado.</p>
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
<p>Mira a qué horas está más cara la luz en el <a href="precio-luz-hoy.html">precio de la luz hoy por horas</a>, calcula el resto de la casa con el <a href="consumo-electrodomesticos.html">consumo de electrodomésticos</a> o compara bombillas con el <a href="ahorro-led.html">ahorro al cambiar a LED</a>. Y si este invierno usas radiadores, revisa el <a href="coste-calefaccion-electrica.html">coste de la calefacción eléctrica</a>.</p>
<p>¿Vas a usar el horno para un asado largo? Calcula lo que gasta en la calculadora de <a href="consumo-horno-electrico.html">consumo del horno eléctrico</a> según la temperatura y la hora.</p>""",
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
<p>¿Secas la ropa dentro de casa? Mira cuánto cuesta hacerlo con un <a href="consumo-deshumidificador.html">deshumidificador</a>. Compara con el resto de tu casa en el <a href="consumo-electrodomesticos.html">consumo de electrodomésticos</a>, comprueba si cabe en tu <a href="potencia-contratada.html">potencia contratada</a> junto con la calefacción o calcula tu <a href="calcular-factura-luz.html">factura de la luz</a>.</p>""",
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

# --- Consumo del deshumidificador con PVPC por horas ---
S['tools'].insert(6, ("consumo-deshumidificador", "Consumo del deshumidificador", "Cuánto cuesta al día y al mes, y por litro de agua, con el precio de la luz de hoy.", ""))
S['aff']["consumo-deshumidificador"] = amz("deshumidificador compresor 20 litros", "Deshumidificadores de compresor") + amz("deshumidificador desecante", "Deshumidificadores desecantes") + amz("higrometro digital", "Higrómetros para medir la humedad")
P.append(("consumo-deshumidificador", "¿Cuánto gasta un deshumidificador? Coste al día y al mes | GastoLuz",
"Calcula cuánto gasta tu deshumidificador de compresor o desecante al día y al mes con el precio de la luz por horas de hoy, cuánto cuesta cada litro de agua y si sale más barato que la secadora.",
"""<p class="lead">Elige el tipo de deshumidificador, cuántas horas lo tienes encendido y a qué hora. Te decimos lo que cuesta con el precio real de la luz de esas horas y cuánto pagas por cada litro de agua que saca.</p>
<div class="card"><div class="row"><div><label for="ap">Tipo de deshumidificador</label><select id="ap"><option value="200|10|70">Compresor pequeño (200 W, 10 l/día)</option><option value="300|20|70" selected>Compresor mediano (300 W, 20 l/día)</option><option value="450|30|75">Compresor grande (450 W, 30 l/día)</option><option value="600|10|80">Desecante (600 W, 10 l/día)</option><option value="30|0.3|100">Peltier mini (30 W, 0,3 l/día)</option></select></div>
<div><label for="w">Potencia (W)</label><input id="w" inputmode="decimal" value="300"></div>
<div><label for="l">Capacidad de extracción (litros/día)</label><input id="l" inputmode="decimal" value="20"></div>
<div><label for="f">Tiempo que funciona el motor (%)</label><input id="f" inputmode="decimal" value="70"></div>
<div><label for="hd">Horas encendido al día</label><input id="hd" inputmode="decimal" value="8"></div>
<div><label for="ho">Hora a la que lo enciendes</label><select id="ho"></select></div>
<div><label for="dm">Días al mes</label><input id="dm" inputmode="numeric" value="30"></div>
<div><label for="p">Precio de la luz (€/kWh, si no usas el PVPC de hoy)</label><input id="p" inputmode="decimal" value="0,15"></div></div>
<p class="note" id="pn">Cargando el precio de la luz por horas de hoy…</p>
<div class="res" id="r" aria-live="polite"></div></div>
<h2>Cuánto gasta cada tipo</h2><p>Los deshumidificadores domésticos gastan poco comparados con un radiador: entre 200 y 600 W. Además, con el higrostato puesto (por ejemplo, en el 55 %), el motor se para cuando alcanza esa humedad, así que el consumo real queda por debajo de la potencia de la etiqueta. Por eso pedimos el <b>tiempo que funciona el motor</b>: un 60-80 % es lo habitual en una casa húmeda.</p>
<table><tr><th>8 horas al día (0,15 €/kWh)</th><th>kWh al día</th><th>Al día</th><th>Al mes</th></tr>
<tr><td>Compresor 200 W al 70 %</td><td>1,12</td><td>0,17 €</td><td>5,04 €</td></tr>
<tr><td>Compresor 300 W al 70 %</td><td>1,68</td><td>0,25 €</td><td>7,56 €</td></tr>
<tr><td>Desecante 600 W al 80 %</td><td>3,84</td><td>0,58 €</td><td>17,28 €</td></tr></table>
<p><b>Fórmula:</b> coste = potencia (W) × % de funcionamiento × horas ÷ 1.000 × precio del kWh. El coste por litro es ese importe dividido entre los litros que saca en esas horas.</p>
<h2>¿Compresor o desecante?</h2><p>La capacidad que anuncian los fabricantes de compresor (10, 20 o 30 litros al día) se mide a 30 °C y 80 % de humedad. En una casa en invierno, a 15-18 °C, sacan bastante menos agua, a veces la mitad. Por debajo de unos 15 °C (trasteros, segundas residencias, garajes), los <b>desecantes</b> rinden mejor y además sueltan aire templado, aunque gastan el doble. Para un piso con calefacción, uno de compresor de 12-20 litros suele ser lo más eficiente.</p>
<h2>¿Secar la ropa con deshumidificador o con secadora?</h2><p>Una lavadora de 7 kg centrifugada a 1.200 rpm deja en la ropa unos 3-4 litros de agua. Un deshumidificador de compresor en un cuarto cerrado la seca en unas horas gastando alrededor de 1 kWh, frente a los 2-4 kWh de una secadora de condensación. Tarda más, pero cuesta menos y evita las paredes empañadas y el moho de tender dentro de casa. Compara con el <a href="consumo-secadora.html">consumo de la secadora</a>.</p>
<p>La humedad cómoda en casa está entre el 40 y el 60 %. Por encima del 65-70 % aparecen condensaciones y moho, y la sensación de frío aumenta, así que bajar la humedad también ayuda a no subir tanto la <a href="coste-calefaccion-electrica.html">calefacción eléctrica</a>. Mira las <a href="precio-luz-hoy.html">horas más baratas de la luz hoy</a> para encenderlo.</p>""",
[("¿Cuánto gasta un deshumidificador al mes?", "Uno de compresor de 300 W encendido 8 horas al día, con el motor funcionando el 70 % del tiempo, gasta unos 50 kWh al mes: alrededor de 7,50 € con la luz a 0,15 €/kWh. Uno desecante de 600 W, más del doble."),
 ("¿Gasta mucha luz un deshumidificador?", "Poco comparado con la calefacción: un modelo de compresor gasta lo que una bombilla antigua de 200-300 W. Un radiador eléctrico de 1.500 W gasta cinco veces más en el mismo tiempo."),
 ("¿Es mejor dejar el deshumidificador encendido toda la noche?", "Si tiene higrostato, puedes dejarlo programado en el 50-55 %: se para solo al alcanzarlo. Con tarifa PVPC, la madrugada suele ser la franja más barata."),
 ("¿Qué consume más, un deshumidificador o una secadora?", "La secadora. Secar una lavadora en una secadora de condensación cuesta 2-4 kWh; con un deshumidificador de compresor en un cuarto cerrado, alrededor de 1 kWh, aunque tarda más.")],
"¿Cuánto gasta un deshumidificador?",
"""let HP=null;const hs=document.getElementById('ho');for(let i=0;i<24;i++)hs.add(new Option(String(i).padStart(2,'0')+':00',i));hs.value=22;
document.getElementById('ap').addEventListener('change',()=>{const t=document.getElementById('ap').value.split('|');document.getElementById('w').value=t[0];document.getElementById('l').value=t[1].replace('.',',');document.getElementById('f').value=t[2];calc();});
function pm(h0,du){let s=0,w=0;for(let t=0;t<du;t+=0.25){s+=HP[Math.floor(h0+t)%24];w++;}return s/w*1.0511*1.21;}
function calc(){const fr=Math.min(100,v('f'))/100,kw=v('w')/1000*fr,hd=Math.min(24,v('hd')),dm=v('dm'),h0=+hs.value,lt=v('l')/24*hd*fr;
if(kw<=0||hd<=0){show('r','Escribe la potencia y las horas de uso.');return;}
let pr=v('p'),tx='';if(HP){pr=pm(h0,hd);let bh=0,bp=1e9;for(let h=0;h<24;h++){const x=pm(h,hd);if(x<bp){bp=x;bh=h;}}tx='<br>Hoy, la franja de '+nf(hd,1)+' h más barata empieza a las <b>'+String(bh).padStart(2,'0')+':00</b> ('+nf(bp,3)+' €/kWh): al mes serían '+eur(kw*hd*bp*dm)+'.';}
const e=kw*hd,c=e*pr,ct=x=>x<1?nf(x*100,1)+' céntimos':eur(x);
let h='Coste al mes:<b class="big">'+eur(c*dm)+'</b>Al día: <b>'+ct(c)+'</b> · '+nf(e,2)+' kWh al día a '+nf(pr,3)+' €/kWh'+(HP?' (PVPC de hoy desde las '+String(h0).padStart(2,'0')+':00, con impuestos)':'');
if(lt>0)h+='<br>Saca hasta unos <b>'+nf(lt,1)+' litros al día</b> en condiciones de laboratorio: '+ct(c/lt)+' por litro. En una casa fría saca menos agua y cada litro sale más caro.';
h+='<br>En todo el invierno (5 meses): <b>'+eur(c*dm*5)+'</b>.';
show('r',h+tx);}
fetch('pvpc.json',{cache:'no-store'}).then(r=>r.json()).then(j=>{const k=Object.keys(j.dias).sort(),d=new Date(),t=d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0'),H=j.dias[t]||j.dias[k[k.length-1]];if(!H||H.length<24)throw 0;HP=[];H.forEach(x=>{HP[x[0]]=x[1];});
document.getElementById('pn').innerHTML='Precio: tarifa regulada (PVPC) de Red Eléctrica hora a hora, con impuesto eléctrico e IVA. Si tienes una tarifa de precio fijo, escribe tu precio y pulsa <a href="#" onclick="HP=null;calc();return false">usar mi precio fijo</a>.';calc();}).catch(()=>{document.getElementById('pn').textContent='Usamos el precio que escribas. Pon el de tu factura (término de energía con impuestos).';calc();});
document.querySelectorAll('.card input,.card select').forEach(e=>e.addEventListener(e.tagName=='SELECT'?'change':'input',()=>calc()));
calc();"""))

# --- Consumo del frigorífico: coste con la etiqueta energética y si compensa cambiarlo ---
S['tools'].insert(5, ("consumo-frigorifico", "Consumo del frigorífico", "Lo que cuesta tu nevera al año según su etiqueta energética y si compensa cambiarla por una nueva.", "Frigorífico"))
S['aff']["consumo-frigorifico"] = amz("frigorifico combi clase A", "Frigoríficos combi de clase A") + amz("termometro frigorifico", "Termómetros para nevera") + ENCH
P.append(("consumo-frigorifico", "¿Cuánto gasta un frigorífico? Consumo al año y al mes | GastoLuz",
"Calcula cuánto gasta tu frigorífico o congelador al día, al mes y al año con el kWh/año de su etiqueta energética y el precio de la luz de hoy, y en cuántos años amortizas uno nuevo.",
"""<p class="lead">Busca en la etiqueta energética de tu nevera el consumo en kWh al año (o en la ficha del modelo) y te decimos lo que te cuesta. Si estás pensando en cambiarla, compárala con la nueva y verás cuánto ahorras y en cuántos años se paga.</p>
<div class="card"><div class="row"><div><label for="ap">Tu frigorífico</label><select id="ap"><option value="">Escribo el dato de la etiqueta</option><option value="450">Combi antiguo, de hace 15-20 años (unos 450 kWh/año)</option><option value="300" selected>Combi de hace 10 años, clase A+ antigua (unos 300 kWh/año)</option><option value="230">Combi nuevo de clase E (unos 230 kWh/año)</option><option value="150">Combi nuevo de clase C (unos 150 kWh/año)</option><option value="400">Americano dos puertas (unos 400 kWh/año)</option><option value="200">Congelador vertical (unos 200 kWh/año)</option></select></div>
<div><label for="k">Consumo de la etiqueta (kWh/año)</label><input id="k" inputmode="decimal" value="300"></div>
<div><label for="n">Consumo del frigorífico nuevo (kWh/año, opcional)</label><input id="n" inputmode="decimal" value="150"></div>
<div><label for="pn2">Precio del frigorífico nuevo (€, opcional)</label><input id="pn2" inputmode="decimal" value="600"></div>
<div><label for="p">Precio de la luz (€/kWh con impuestos)</label><input id="p" inputmode="decimal" value="0,18"></div></div>
<p class="note" id="pnt">Pon el precio medio del kWh de tu factura, con impuestos.</p>
<div class="res" id="r" aria-live="polite"></div></div>
<h2>Cómo se calcula lo que gasta la nevera</h2><p>El frigorífico funciona las 24 horas, aunque el compresor se enciende y se apaga solo. Por eso lo más fiable no es multiplicar la potencia (W) por las horas, sino usar el <b>consumo anual de la etiqueta energética</b>, que ya tiene en cuenta esos ciclos. <b>Fórmula:</b> coste al año = kWh/año × precio del kWh con impuestos. Como funciona igual de día que de noche, el precio que cuenta es la <b>media de las 24 horas</b>: con tarifa PVPC puedes calcular con la media de hoy, aunque para un año entero es más fiable el precio medio de tu factura.</p>
<table><tr><th>Consumo de la etiqueta</th><th>Al mes</th><th>Al año (0,18 €/kWh)</th></tr>
<tr><td>150 kWh/año</td><td>2,25 €</td><td>27 €</td></tr>
<tr><td>230 kWh/año</td><td>3,45 €</td><td>41,40 €</td></tr>
<tr><td>300 kWh/año</td><td>4,50 €</td><td>54 €</td></tr>
<tr><td>450 kWh/año</td><td>6,75 €</td><td>81 €</td></tr></table>
<p><b>Ejemplo:</b> cambiar un combi de 300 kWh/año por uno de 150 kWh/año ahorra 150 kWh, unos 27 € al año a 0,18 €/kWh. Si el nuevo cuesta 600 €, el ahorro tardaría más de 20 años en pagarlo: solo compensa cambiar por ahorro cuando el viejo es muy antiguo o está estropeado. Si tienes que comprar uno de todas formas, la diferencia entre una clase alta y una baja sí se nota a lo largo de los 10-15 años que dura.</p>
<h2>¿No encuentras la etiqueta?</h2><p>Desde marzo de 2021 la etiqueta europea va de la A a la G (antes llegaba a A+++), así que un «A+» antiguo equivale hoy a una E o una F. Puedes buscar tu modelo en la base de datos europea <a href="https://eprel.ec.europa.eu/" rel="noopener" target="_blank">EPREL</a>, o medirlo tú: enchufa la nevera a un medidor de consumo 48 horas y multiplica los kWh por 182,5 para tener el dato anual.</p>
<h2>Cómo hacer que gaste menos</h2><ul><li>Pon el frigorífico a unos 4-5 °C y el congelador a -18 °C: cada grado más frío aumenta el consumo.</li><li>Déjale espacio detrás para que ventile y apártalo del horno y del sol.</li><li>Descongela cuando la escarcha pase de unos 3 mm y revisa que la goma de la puerta cierre bien.</li><li>No metas comida caliente y abre la puerta lo justo.</li></ul>
<p>Compara con otros aparatos en la <a href="consumo-electrodomesticos.html">calculadora de consumo de electrodomésticos</a>, revisa tu <a href="calcular-factura-luz.html">factura de la luz</a> o mira el <a href="precio-luz-hoy.html">precio de la luz hoy</a>.</p>""",
[("¿Cuánto gasta un frigorífico al mes?", "Un combi actual consume entre 150 y 250 kWh al año: de 2 a 4 € al mes con la luz a 0,18 €/kWh. Uno de hace 15-20 años puede gastar el doble o el triple."),
 ("¿Cuántos kWh gasta una nevera al día?", "Entre 0,4 y 1,2 kWh al día según su tamaño y antigüedad. Divide entre 365 el consumo anual de la etiqueta: 300 kWh/año son 0,82 kWh al día."),
 ("¿Compensa cambiar el frigorífico viejo por uno nuevo?", "Por ahorro de luz casi nunca, salvo que el viejo sea muy antiguo: pasar de 300 a 150 kWh/año ahorra unos 27 € al año. Si tienes que cambiarlo de todas formas, elegir una clase energética alta sí compensa a lo largo de su vida útil."),
 ("¿Qué gasta más, el frigorífico o el congelador?", "Un congelador vertical independiente gasta parecido a un combi, unos 170-250 kWh al año. Los americanos de dos puertas con dispensador de hielo son los que más gastan, a menudo más de 350 kWh al año.")],
"¿Cuánto gasta un frigorífico?",
"""let HM=null;
document.getElementById('ap').addEventListener('change',()=>{const x=document.getElementById('ap').value;if(x){document.getElementById('k').value=x;}calc();});
function calc(){const k=v('k'),n=v('n'),pn=v('pn2'),pr=HM||v('p');if(k<=0){show('r','Escribe el consumo anual de la etiqueta (kWh/año).');return;}
const y=k*pr,ct=x=>x<1?nf(x*100,1)+' céntimos':eur(x);
let h='Tu frigorífico te cuesta al año:<b class="big">'+eur(y)+'</b>Al mes: <b>'+eur(y/12)+'</b> · al día: '+ct(y/365)+' · '+nf(k/365,2)+' kWh al día a '+nf(pr,3)+' €/kWh'+(HM?' (media del PVPC de hoy con impuestos)':'');
h+='<br>En 10 años: <b>'+eur(y*10)+'</b>.';
if(n>0&&n<k){const s=(k-n)*pr;h+='<br>Con el nuevo ('+nf(n,0)+' kWh/año) pagarías '+eur(n*pr)+' al año: <b>ahorras '+eur(s)+' al año</b> ('+eur(s*10)+' en 10 años).';if(pn>0){const a=pn/s;h+=' El nuevo se pagaría solo con el ahorro en <b>'+(a>30?'más de 30 años':nf(a,1)+' años')+'</b>'+(a>12?': por ahorro no compensa; cámbialo cuando el viejo falle.':': compensa cambiarlo.');}}
else if(n>=k&&n>0)h+='<br>El frigorífico nuevo que has puesto gasta igual o más que el actual.';
show('r',h);}
fetch('pvpc.json',{cache:'no-store'}).then(r=>r.json()).then(j=>{const kk=Object.keys(j.dias).sort(),d=new Date(),t=d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0'),H=j.dias[t]||j.dias[kk[kk.length-1]];if(!H||H.length<24)throw 0;
const pm=H.reduce((s,x)=>s+x[1],0)/H.length*1.0511*1.21;window.PM=pm;
document.getElementById('pnt').innerHTML='Hoy, la media de las 24 horas de la tarifa regulada (PVPC) de Red Eléctrica es <b>'+nf(pm,3)+' €/kWh</b> con impuestos. Cambia mucho de un día a otro y entre invierno y verano, así que para el cálculo anual es mejor el precio medio de tu factura. <a href="#" onclick="HM=window.PM;calc();return false">Calcular con el PVPC de hoy</a> · <a href="#" onclick="HM=null;calc();return false">usar mi precio</a>';calc();}).catch(()=>{document.getElementById('pnt').textContent='Usamos el precio que escribas: pon el de tu factura con impuestos.';calc();});
document.querySelectorAll('.card input,.card select').forEach(e=>e.addEventListener(e.tagName=='SELECT'?'change':'input',()=>calc()));
calc();"""))

# --- Consumo de la placa de inducción y la vitrocerámica: coste con el PVPC de hoy y comparación ---
S['tools'].insert(6, ("consumo-induccion-vitroceramica", "Inducción o vitrocerámica: cuánto gasta", "Lo que cuesta cocinar al día y al mes con tu placa y cuánto ahorras con inducción.", "Placa"))
S['aff']["consumo-induccion-vitroceramica"] = amz("placa induccion 3 zonas", "Placas de inducción") + amz("bateria cocina induccion", "Baterías aptas para inducción") + amz("medidor consumo electrico enchufe", "Medidores de consumo")
P.append(("consumo-induccion-vitroceramica", "¿Cuánto gasta una placa de inducción o una vitrocerámica? | GastoLuz",
"Calcula cuánto gasta tu placa de inducción o vitrocerámica al día y al mes con el precio de la luz de hoy a la hora de comer y de cenar, y cuánto ahorras con inducción.",
"""<p class="lead">Dinos qué placa tienes y cuánto cocinas, y te calculamos lo que gasta al día y al mes (más abajo tienes el gasto de una comida de Navidad). También verás cuánto gastarías con el otro tipo de placa.</p>
<div class="card"><div class="row"><div><label for="ti">Tu placa</label><select id="ti"><option value="i">Inducción</option><option value="v">Vitrocerámica (radiante)</option></select></div>
<div><label for="kw">Potencia de la zona que más usas (kW)</label><input id="kw" inputmode="decimal" value="2"></div>
<div><label for="ni">Nivel medio de uso (% de la potencia)</label><input id="ni" inputmode="decimal" value="60"></div>
<div><label for="mi">Minutos de cocina al día (sumando zonas)</label><input id="mi" inputmode="decimal" value="45"></div>
<div><label for="dm">Días que cocinas al mes</label><input id="dm" inputmode="numeric" value="30"></div>
<div><label for="p">Precio de la luz (€/kWh con impuestos)</label><input id="p" inputmode="decimal" value="0,18"></div></div>
<p class="note" id="pnt">Pon el precio del kWh de tu factura, con impuestos.</p>
<div class="res" id="r" aria-live="polite"></div></div>
<h2>Cómo se calcula lo que gasta la placa</h2><p><b>Consumo (kWh) = potencia de la zona (kW) × nivel de uso × horas</b>, y el coste es ese consumo × precio del kWh. La potencia máxima de una zona va de 1,2 kW en las pequeñas a 3 kW o más en las grandes, pero casi nunca se cocina al máximo: al hervir se usa toda la potencia unos minutos y luego se baja. Por eso el nivel medio de uso suele estar entre el 50 y el 70 %.</p>
<p>La diferencia entre placas está en la <b>eficiencia</b>: la inducción calienta directamente el fondo de la olla y aprovecha aproximadamente el 85 % de la energía, mientras que la vitrocerámica radiante calienta primero el cristal y aprovecha en torno al 70-75 %. Para el mismo guiso, la vitrocerámica gasta alrededor de un 15-20 % más y tarda más en hervir.</p>
<table><tr><th>Uso diario (2 kW al 60 %)</th><th>Inducción al mes</th><th>Vitrocerámica al mes</th></tr>
<tr><td>30 min</td><td>18 kWh · 3,24 €</td><td>21,2 kWh · 3,82 €</td></tr>
<tr><td>45 min</td><td>27 kWh · 4,86 €</td><td>31,9 kWh · 5,74 €</td></tr>
<tr><td>90 min</td><td>54 kWh · 9,72 €</td><td>63,8 kWh · 11,47 €</td></tr></table>
<p class="note">Con la luz a 0,18 €/kWh y 30 días al mes; la vitrocerámica, estimada con un 85 % frente a un 72 % de eficiencia.</p>
<p><b>Ejemplo:</b> una comida de Navidad con un caldo de 2 horas a fuego medio (1,2 kW de media) y 40 minutos más de otras zonas a 1,5 kW gasta unos 3,4 kWh en inducción: algo más de 60 céntimos a 0,18 €/kWh. Cocinar es de lo que menos pesa en la factura; el horno, la calefacción eléctrica y el termo gastan mucho más.</p>
<h2>¿Compensa cambiar la vitrocerámica por inducción?</h2><p>Por ahorro de luz casi nunca: con un uso normal la diferencia es de 1 a 3 € al mes, así que una placa de inducción de 300-400 € tardaría muchos años en pagarse solo con lo que ahorra. Compensa cuando la vitro se estropea o si valoras cocinar más rápido, una limpieza más fácil y que la placa no quede ardiendo. Ten en cuenta que la inducción necesita menaje con fondo magnético (si un imán se pega al fondo, sirve).</p>
<h2>Trucos para gastar menos al cocinar</h2><ul><li>Usa una zona del tamaño de la olla y tápala: hierve antes y gasta menos.</li><li>En vitrocerámica, apaga 5 minutos antes de terminar: el calor residual acaba la cocción.</li><li>La olla exprés reduce el tiempo de legumbres y guisos a menos de la mitad.</li><li>Si tienes tarifa PVPC, la cena suele caer en horas caras; mira el <a href="precio-luz-hoy.html">precio de la luz por horas</a> para lo que puedas adelantar.</li></ul>
<p>Compara con el <a href="consumo-freidora-aire.html">consumo de la freidora de aire y el horno</a>, revisa qué <a href="potencia-contratada.html">potencia necesitas contratar</a> si usas varias zonas a la vez o mira el <a href="consumo-electrodomesticos.html">consumo de todos tus electrodomésticos</a>.</p>""",
[("¿Cuánto gasta una placa de inducción al mes?", "Con unos 45 minutos de cocina al día, entre 25 y 30 kWh al mes: unos 5 € con la luz a 0,18 €/kWh. Una familia que cocina mucho puede llegar a 10 € al mes."),
 ("¿Qué gasta más, la inducción o la vitrocerámica?", "La vitrocerámica: aprovecha en torno al 70-75 % de la energía frente a aproximadamente el 85 % de la inducción, así que para cocinar lo mismo gasta alrededor de un 15-20 % más y tarda más."),
 ("¿Cuántos kW tiene una placa de inducción?", "Cada zona tiene entre 1,2 y 3,7 kW, y la placa completa suele sumar 7 kW o más. Las placas limitan la potencia total, pero si usas varias zonas a la vez junto con el horno puede saltar el automático con 3,45 kW contratados."),
 ("¿Cuánto cuesta cocinar una hora con inducción?", "Una zona de 2 kW al 60 % consume 1,2 kWh en una hora: unos 22 céntimos con la luz a 0,18 €/kWh. A máxima potencia serían 2 kWh, unos 36 céntimos.")],
"¿Cuánto gasta una placa de inducción o una vitrocerámica?",
"""let HM=null;const EF={i:0.85,v:0.72};
function calc(){const t=document.getElementById('ti').value,o=t=='i'?'v':'i',kw=v('kw'),ni=v('ni')/100,mi=v('mi'),dm=v('dm'),pr=HM||v('p');
if(kw<=0||mi<=0){show('r','Escribe la potencia de la zona y los minutos de cocina.');return;}
const kd=kw*ni*mi/60,cd=kd*pr,km=kd*dm,cm=km*pr,ko=km*EF[t]/EF[o],co=ko*pr,N={i:'inducción',v:'vitrocerámica'};
const ct=x=>x<1?nf(x*100,1)+' céntimos':eur(x);
let h='Tu placa de '+N[t]+' gasta al mes:<b class="big">'+eur(cm)+'</b>'+nf(km,1)+' kWh al mes · al día: '+nf(kd,2)+' kWh, '+ct(cd)+' · al año: <b>'+eur(cm*12)+'</b>';
h+='<br>Precio usado: '+nf(pr,3)+' €/kWh'+(HM?' (PVPC de hoy con impuestos)':'')+'.';
h+='<br>Con '+N[o]+' gastarías unos '+eur(co)+' al mes: '+(t=='v'?'<b>ahorrarías '+eur(cm-co)+' al mes</b> ('+eur((cm-co)*12)+' al año) con inducción.':'la inducción te ahorra <b>'+eur(co-cm)+' al mes</b> frente a la vitrocerámica.');
show('r',h);}
fetch('pvpc.json',{cache:'no-store'}).then(r=>r.json()).then(j=>{const kk=Object.keys(j.dias).sort(),d=new Date(),t=d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0'),H=j.dias[t]||j.dias[kk[kk.length-1]];if(!H||H.length<24)throw 0;
const P={};H.forEach(x=>{P[x[0]]=x[1]*1.0511*1.21;});const pc=(P[13]+P[14])/2,pz=(P[20]+P[21])/2;window.PM=(pc+pz)/2;
document.getElementById('pnt').innerHTML='Tarifa regulada (PVPC) de Red Eléctrica hoy, con impuestos: a la hora de comer (13-15 h) <b>'+nf(pc,3)+' €/kWh</b> y a la hora de cenar (20-22 h) <b>'+nf(pz,3)+' €/kWh</b>. <a href="#" onclick="HM=window.PM;calc();return false">Calcular con el PVPC de hoy</a> · <a href="#" onclick="HM=null;calc();return false">usar mi precio</a>';calc();}).catch(()=>{document.getElementById('pnt').textContent='Usamos el precio que escribas: pon el de tu factura con impuestos.';calc();});
document.querySelectorAll('.card input,.card select').forEach(e=>e.addEventListener(e.tagName=='SELECT'?'change':'input',()=>calc()));
calc();"""))

# --- Portada: accesos a lo más buscado en temporada (Navidad e invierno) ---
S['home_intro'] += '<nav class="share" aria-label="Lo más buscado estos días"><span>Lo más buscado estos días:</span><a href="precio-luz-hoy.html">Precio de la luz hoy</a><a href="consumo-luces-navidad.html">Luces de Navidad</a><a href="coste-calefaccion-electrica.html">Radiador eléctrico</a><a href="estufa-butano-vs-electrica.html">Butano o eléctrica</a><a href="consumo-manta-electrica.html">Manta eléctrica</a><a href="consumo-horno-electrico.html">Horno en Navidad</a></nav>'

# --- Cuánto consume un horno eléctrico (con el PVPC de la hora a la que lo enciendes) ---
S['tools'].insert(4, ("consumo-horno-electrico", "Cuánto consume un horno eléctrico", "kWh y euros de cada horneado según potencia, temperatura y la hora del PVPC: del asado de Navidad a una pizza.", "Horno"))
S['aff']["consumo-horno-electrico"] = amz("termometro horno cocina", "Termómetros para horno y asados") + amz("enchufe medidor consumo", "Enchufes medidores de consumo") + amz("freidora de aire grande", "Freidoras de aire grandes")
P.append(("consumo-horno-electrico", "Cuánto consume un horno eléctrico: kWh y coste con la luz de hoy | GastoLuz",
"Calcula cuánto gasta tu horno eléctrico en cada receta según potencia, temperatura y minutos, con el precio PVPC de la hora a la que cocinas. Del asado de Navidad a una pizza.",
"""<p class="lead">Elige la receta o pon la potencia de tu horno, la temperatura y el tiempo. Te decimos los kWh que gasta y cuánto cuesta con el precio de la luz de hoy a la hora a la que vas a cocinar.</p>
<div class="card"><label for="re">Receta (opcional)</label><select id="re"><option value="">Personalizada</option><option value="150,180,1">Cordero o cochinillo asado (2 h 30 min a 180 °C)</option><option value="180,170,1">Pavo relleno de 5 kg (3 h a 170 °C)</option><option value="40,200,1">Besugo o dorada al horno (40 min a 200 °C)</option><option value="60,200,1">Pollo asado (1 h a 200 °C)</option><option value="15,230,1">Pizza (15 min a 230 °C)</option><option value="12,180,1">Galletas o polvorones (12 min a 180 °C)</option><option value="45,180,1">Bizcocho o roscón (45 min a 180 °C)</option></select>
<div class="row"><div><label for="w">Potencia del horno (W)</label><input id="w" inputmode="numeric" value="2500"></div>
<div><label for="t">Temperatura (°C)</label><select id="t"><option>150</option><option>160</option><option>170</option><option selected>180</option><option>200</option><option>220</option><option>230</option><option>250</option></select></div>
<div><label for="mi">Minutos de horneado</label><input id="mi" inputmode="numeric" value="60"></div>
<div><label for="h">Hora a la que lo enciendes</label><select id="h"></select></div>
<div><label for="pc">Precio del kWh (€, si no usas el PVPC)</label><input id="pc" inputmode="decimal" value="0,15"></div>
<div><label for="ve">Veces al mes</label><input id="ve" inputmode="numeric" value="4"></div></div>
<label class="chk"><input type="checkbox" id="pr" checked><span>Precalentar (10 minutos a plena potencia)</span></label>
<label class="chk"><input type="checkbox" id="ai"><span>Con ventilador (aire forzado): permite bajar unos 20 °C</span></label>
<button onclick="calc()">Calcular consumo</button><div class="res" id="r" aria-live="polite"></div></div>
<p class="note" id="pn">Cargando el precio de la luz de hoy por horas…</p>
<h2>Cuánto gasta un horno eléctrico por hora</h2><p>Un horno doméstico tiene entre 2.000 y 3.500 W, pero solo va a plena potencia mientras se calienta. Después el termostato enciende y apaga las resistencias para mantener la temperatura, y cuanto más alta es, más tiempo están encendidas. Por eso calculamos: <b>consumo = potencia × minutos de precalentado + potencia × minutos de horneado × % del tiempo con las resistencias encendidas</b>. Ese porcentaje va del 45 % a 150 °C al 70 % a 250 °C, que es lo que suele medirse con un enchufe medidor en un horno moderno con buen aislamiento. Con ventilador, el aire caliente se reparte mejor y la misma receta se hace con unos 20 °C menos, por lo que gasta algo menos.</p>
<table><tr><th>Receta (horno de 2.500 W, con precalentado)</th><th>Consumo</th><th>A 0,15 €/kWh</th></tr>
<tr><td>Pizza, 15 min a 230 °C</td><td>0,80 kWh</td><td>0,12 €</td></tr>
<tr><td>Pollo asado, 1 h a 200 °C</td><td>1,79 kWh</td><td>0,27 €</td></tr>
<tr><td>Cordero asado, 2 h 30 min a 180 °C</td><td>3,54 kWh</td><td>0,53 €</td></tr>
<tr><td>Pavo de 5 kg, 3 h a 170 °C</td><td>4,02 kWh</td><td>0,60 €</td></tr></table>
<p><b>Ejemplo:</b> el cordero de Nochebuena en un horno de 2.500 W: 10 minutos de precalentado son 0,42 kWh, y 150 minutos a 180 °C, con las resistencias encendidas la mitad del tiempo, otros 3,13 kWh. En total, 3,54 kWh. Con el PVPC, no es lo mismo meterlo a las 14:00 que a las 20:00: la diferencia entre la hora más barata y la más cara del día puede duplicar el coste. Mira el <a href="precio-luz-hoy.html">precio de la luz de hoy por horas</a> para elegir.</p>
<h2>Cómo gastar menos con el horno</h2><ul><li><b>No abras la puerta</b> para mirar: cada vez se escapa una parte del calor y el horno tiene que recuperarlo.</li><li><b>Precalienta solo lo necesario</b>: para asados largos y guisos no hace falta, y apaga 5-10 minutos antes del final, el calor residual termina el plato.</li><li><b>Aprovecha cada encendido</b>: hornea varias bandejas a la vez con ventilador.</li><li>Para raciones pequeñas, la <a href="consumo-freidora-aire.html">freidora de aire gasta bastante menos que el horno</a>, y para cocinar en la placa compara <a href="consumo-induccion-vitroceramica.html">inducción y vitrocerámica</a>.</li></ul>
<p>¿Quieres ver cuánto supone el horno en tu factura junto al resto de aparatos? Súmalos en la calculadora de <a href="consumo-electrodomesticos.html">consumo de electrodomésticos</a>.</p>""",
[("¿Cuánto consume un horno eléctrico en una hora?", "Un horno de 2.500 W a 180-200 °C gasta entre 1,25 y 1,4 kWh en una hora de horneado, más unos 0,4 kWh si precalientas 10 minutos. A 0,15 €/kWh son unos 20 céntimos por hora, más 6 céntimos del precalentado."),
 ("¿Cuánto cuesta hacer un asado de Navidad en el horno?", "Un cordero o un pavo de 2 h 30 min a 3 h en un horno de 2.500 W gasta entre 3,5 y 4 kWh: unos 0,55-0,60 € a 0,15 €/kWh, y algo más si coincide con las horas caras del PVPC por la tarde-noche."),
 ("¿Gasta más el horno que la vitrocerámica?", "Para el mismo plato, normalmente sí: el horno tiene que calentar todo su interior. Para asados grandes no hay alternativa, pero para raciones pequeñas una freidora de aire o el microondas gastan mucho menos."),
 ("¿El horno con ventilador gasta más?", "El ventilador consume muy poco (unos 20-40 W). Como reparte mejor el calor, permite cocinar a unos 20 °C menos y a veces en menos tiempo, así que en conjunto suele gastar menos que el calor convencional.")],
"¿Cuánto consume un horno eléctrico?",
"""let HP=null;const DU={150:.45,160:.47,170:.48,180:.5,200:.55,220:.6,230:.62,250:.7};
const hs=document.getElementById('h');for(let i=0;i<24;i++)hs.add(new Option(String(i).padStart(2,'0')+':00',i));hs.value=14;
document.getElementById('re').addEventListener('change',e=>{const x=e.target.value;if(!x)return;const [m,t,p]=x.split(',');document.getElementById('mi').value=m;document.getElementById('t').value=t;document.getElementById('pr').checked=p=='1';calc();});
function pr(h0,min){let s=0,r=min,t=0;while(r>0){const f=Math.min(60,r);s+=HP[(h0+t)%24]*f;r-=f;t++;}return s/min*1.0511*1.21;}
function calc(){const w=v('w')/1000,mi=v('mi'),T=+document.getElementById('t').value,ai=document.getElementById('ai').checked,pq=document.getElementById('pr').checked;
if(w<=0||mi<=0){show('r','Escribe la potencia y los minutos.');return;}
let Te=T;if(ai){const ks=Object.keys(DU).map(Number);Te=ks.reduce((a,b)=>Math.abs(b-(T-20))<Math.abs(a-(T-20))?b:a,ks[0]);}
const du=DU[Te]||.5,k0=pq?w*10/60:0,k1=w*mi/60*du,k=k0+k1,h0=+hs.value,tot=mi+(pq?10:0);
let p=v('pc'),tx='';if(HP){p=pr(h0,tot);let b=[0,1e9],c=[0,0];for(let i=0;i<24;i++){const q=pr(i,tot);if(q<b[1])b=[i,q];if(q>c[1])c=[i,q];}
tx='<br>Con el PVPC de hoy (impuestos incluidos): a las '+String(h0).padStart(2,'0')+':00, '+nf(p,3)+' €/kWh. Lo más barato, empezando a las <b>'+String(b[0]).padStart(2,'0')+':00</b>: '+eur(k*b[1])+'; lo más caro, a las '+String(c[0]).padStart(2,'0')+':00: '+eur(k*c[1])+'.';}
show('r','Este horneado gasta:<b class="big">'+nf(k,2)+' kWh · '+eur(k*p)+'</b>'+(pq?'Precalentado: '+nf(k0,2)+' kWh · ':'')+'Horneado: '+nf(k1,2)+' kWh (resistencias encendidas el '+Math.round(du*100)+' % del tiempo'+(ai?', con ventilador como a '+Te+' °C':'')+').'+tx+'<br>Al mes ('+nf(v('ve'),0)+' veces): <b>'+eur(k*p*v('ve'))+'</b> · Al año: '+eur(k*p*v('ve')*12));}
document.querySelectorAll('.card input,.card select').forEach(e=>{if(e.id!='re')e.addEventListener(e.tagName=='SELECT'||e.type=='checkbox'?'change':'input',()=>calc());});
fetch('pvpc.json',{cache:'no-store'}).then(r=>r.json()).then(j=>{const kk=Object.keys(j.dias).sort(),d=new Date(),t=d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0'),H=j.dias[t]||j.dias[kk[kk.length-1]];if(!H||H.length<24)throw 0;HP=[];H.forEach(x=>{HP[x[0]]=x[1];});
document.getElementById('pn').innerHTML='Precio: tarifa regulada (PVPC) de Red Eléctrica hora a hora'+(j.dias[t]?' de hoy':' del último día disponible')+', con impuesto eléctrico e IVA. Si tienes otra tarifa, escribe tu precio y pulsa <a href="#" onclick="HP=null;calc();return false">usar mi precio</a>.';calc();}).catch(()=>{document.getElementById('pn').textContent='Usamos el precio que escribas: pon el de tu factura (término de energía con impuestos).';calc();});
calc();"""))
