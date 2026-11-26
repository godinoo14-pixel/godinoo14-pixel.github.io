from gen import build
S = dict(dir="gastoluz", name="GastoLuz", logo="Gasto<span>Luz</span>", acc="#0b7285",
         base="https://gastoluz.es/", domain="gastoluz.es",
         tools=[("consumo-electrodomesticos", "Consumo de electrodomésticos", "Cuánto gasta al mes cada aparato de tu casa.", "Electrodomésticos"),
                ("coste-aire-acondicionado", "Coste del aire acondicionado", "Lo que pagas por encender el aire o la bomba de calor.", "Aire acondicionado"),
                ("potencia-contratada", "¿Qué potencia contratar?", "Calcula los kW que necesitas y evita pagar de más.", "Potencia"),
                ("calculadora-kwh", "Calculadora de vatios a kWh", "Pasa vatios a kWh y a euros.", ""),
                ("coste-calefaccion-electrica", "Coste de la calefacción eléctrica", "Radiador, calefactor o estufa: cuánto cuesta el invierno.", ""),
                ("ahorro-led", "Ahorro al cambiar a LED", "Cuánto ahorras sustituyendo bombillas antiguas.", "")],
         home_title="Precio de la luz hoy y calculadoras de consumo eléctrico | GastoLuz",
         home_desc="Precio de la luz hoy por horas (PVPC), simulador de tu factura y cuánto gastan tus electrodomésticos, la calefacción o el aire. Calcula y ahorra en tu recibo.",
         home_h1="Calcula cuánto gastas en luz",
         home_intro='<p class="lead">Descubre qué aparatos disparan tu factura, qué potencia necesitas contratar y cuánto puedes ahorrar. Cambia el precio del kWh por el de tu factura para un resultado exacto.</p>',
         home_extra='<h2>Dónde ver el precio del kWh</h2><p>En tu factura aparece el <b>término de energía</b> en €/kWh (a veces dividido en punta, llano y valle) y el <b>término de potencia</b> en €/kW y día. Nuestras calculadoras usan 0,15 €/kWh como referencia, pero puedes poner el tuyo en cada una.</p>')

APP = [("Frigorífico", 150, 24, "Funciona a ciclos: equivale a unas 8 h reales al día"), ("Horno", 2000, 0.5, ""), ("Lavadora (ciclo 40 °C)", 900, 1, ""),
       ("Secadora", 2500, 1, ""), ("Lavavajillas", 1500, 1, ""), ("Vitrocerámica / inducción", 1800, 1, ""), ("Microondas", 1000, 0.2, ""),
       ("Termo eléctrico", 1500, 3, ""), ("Televisor", 100, 4, ""), ("Ordenador de sobremesa", 200, 4, ""), ("Portátil", 60, 6, ""),
       ("Plancha", 2000, 0.3, ""), ("Secador de pelo", 1800, 0.2, ""), ("Freidora de aire", 1500, 0.5, ""), ("Cafetera", 1200, 0.1, ""), ("Consola", 150, 2, "")]
opts = "".join(f'<option value="{w}|{h}">{n}</option>' for n, w, h, _ in APP)

P = []
P.append(("consumo-electrodomesticos", "Consumo de electrodomésticos: cuánto gasta cada aparato al mes | GastoLuz",
"Calcula cuánto consume y cuánto cuesta al día, al mes y al año cada electrodoméstico: frigorífico, horno, lavadora, termo, secadora o radiador, según su potencia y las horas de uso.",
"""<p class="lead">Elige un aparato (o pon su potencia en vatios), las horas de uso y el precio del kWh.</p>
<div class="card"><label for="ap">Electrodoméstico</label><select id="ap" onchange="pre()">""" + opts + """</select>
<div class="row"><div><label for="w">Potencia (W)</label><input id="w" inputmode="decimal"></div><div><label for="h">Horas de uso al día</label><input id="h" inputmode="decimal"></div>
<div><label for="p">Precio kWh (€)</label><input id="p" inputmode="decimal" value="0,15"></div><div><label for="f">Factor de uso (%)</label><input id="f" inputmode="decimal" value="100"></div></div>
<button onclick="calc()">Calcular consumo</button><div class="res" id="r"></div></div>
<p class="note">La potencia viene en la etiqueta o en el manual. El frigorífico y otros aparatos con termostato no funcionan a plena potencia todo el tiempo: para ellos usa un factor de uso del 30-40 %, o calcula la nevera con el dato de su etiqueta en la <a href="consumo-frigorifico.html">calculadora de consumo del frigorífico</a>.</p>
<h2>Los aparatos que más gastan</h2><p>Los que producen calor son los que más consumen: secadora, horno, termo eléctrico, calefactores y vitrocerámica. El frigorífico gasta poco por hora pero está encendido todo el año, por eso suele ser uno de los mayores consumos de la casa. Programar lavadora y lavavajillas en horas valle puede reducir mucho su coste.</p>
<table><tr><th>Aparato (uso típico)</th><th>kWh al mes</th><th>€ al mes (0,15 €/kWh)</th></tr>
<tr><td>Frigorífico combi A++ (encendido siempre)</td><td>25-35</td><td>3,75-5,25 €</td></tr><tr><td>Lavadora a 40 °C, 4 lavados/semana</td><td>15</td><td>2,25 €</td></tr>
<tr><td>Horno, 30 min al día</td><td>30</td><td>4,50 €</td></tr><tr><td>Termo de 80 l, una familia</td><td>120-180</td><td>18-27 €</td></tr></table>
<p class="note">Valores orientativos: calcula los tuyos arriba con la potencia de tu aparato.</p>
<p>Para los que más gastan tenemos calculadoras específicas: <a href="consumo-secadora.html">secadora</a>, <a href="coste-ducha-termo.html">termo eléctrico</a>, <a href="coste-calefaccion-electrica.html">radiadores</a>, <a href="coste-aire-acondicionado.html">aire acondicionado</a> y <a href="consumo-freidora-aire.html">freidora de aire u horno</a>. Y si quieres saber a qué hora ponerlos, mira el <a href="precio-luz-hoy.html">precio de la luz hoy por horas</a>.</p>""",
[("¿Cuánto gasta un frigorífico al mes?", "Un combi actual consume entre 12 y 20 kWh al mes (150-250 kWh al año según su etiqueta), unos 2-4 € con el kWh a 0,18 €. Los de hace 15-20 años pueden gastar el doble o el triple: calcula el tuyo en la calculadora de consumo del frigorífico."),
 ("¿Cómo paso vatios a kWh?", "Multiplica los vatios por las horas de uso y divide entre 1.000. Un aparato de 2.000 W durante 1 hora consume 2 kWh."),
 ("¿Qué electrodoméstico gasta más luz en casa?", "Los que calientan: termo eléctrico, calefacción eléctrica, secadora y horno. En una casa sin calefacción eléctrica, el termo y el frigorífico suelen ser los mayores consumos del año.")],
None, """function pre(){const [w,h]=document.getElementById('ap').value.split('|');document.getElementById('w').value=w;document.getElementById('h').value=h;document.getElementById('f').value=(w==150&&h==24)?35:100;}
function calc(){const k=v('w')*v('h')*v('f')/100/1000,p=v('p');show('r','Coste al mes:<b class="big">'+eur(k*p*30.4)+'</b>Al día: '+nf(k,2)+' kWh ('+eur(k*p)+') · Al año: '+nf(k*365,0)+' kWh (<b>'+eur(k*p*365)+'</b>)');}pre();"""))

P.append(("coste-aire-acondicionado", "¿Cuánto gasta el aire acondicionado en frío y en calor? Calculadora | GastoLuz",
"Calcula cuánto cuesta el aire acondicionado o la bomba de calor por hora, al día y al mes, en verano y para calentar en invierno, según frigorías, eficiencia y precio de la luz.",
"""<p class="lead">Calcula el coste de tu aire acondicionado a partir de sus frigorías (o kW de frío) y su eficiencia.</p>
<div class="card"><div class="row"><div><label for="fr">Frigorías</label><input id="fr" inputmode="numeric" value="3000"></div>
<div><label for="e">Eficiencia (EER/SEER)</label><input id="e" inputmode="decimal" value="3,5"></div>
<div><label for="h">Horas al día</label><input id="h" inputmode="decimal" value="6"></div><div><label for="d">Días al mes</label><input id="d" inputmode="numeric" value="30"></div>
<div><label for="c">Carga media (%)</label><input id="c" inputmode="decimal" value="60"></div><div><label for="p">Precio kWh (€)</label><input id="p" inputmode="decimal" value="0,15"></div></div>
<button onclick="calc()">Calcular</button><div class="res" id="r"></div></div>
<p class="note">Un equipo inverter no trabaja al 100 % todo el tiempo: una vez alcanzada la temperatura baja el ritmo. Una carga media del 50-70 % es realista.</p>
<h2>Cómo gastar menos con el aire</h2><ul><li>Pon el termostato a 25-26 °C: cada grado menos sube el consumo alrededor de un 7 %.</li><li>Limpia los filtros cada mes en verano.</li><li>Baja persianas y toldos en las horas de sol.</li><li>Usa el modo «eco» o «sleep» por la noche.</li></ul>
<h2>Aire acondicionado en modo calor (invierno)</h2><p>Para calentar, pon las frigorías del equipo (su potencia en calor suele ser parecida o algo mayor) y su <b>SCOP</b> en la casilla de eficiencia; suele estar entre 3 y 4,5 en la etiqueta energética. En invierno el termostato a 19-21 °C es suficiente: cada grado de más sube el consumo alrededor de un 7 %. Calentar con bomba de calor cuesta entre la mitad y un tercio que con radiadores eléctricos o con butano: <a href="estufa-butano-vs-electrica.html">compara butano, radiador y bomba de calor</a> con el precio de hoy.</p>""",
[("¿Cuánto gasta el aire acondicionado para calentar?", "Un equipo de 3.000 frigorías con SCOP 3,5 consume alrededor de 1 kW a plena potencia y unos 0,6 kW de media una vez caliente la habitación: con el kWh a 0,15 €, unos 0,09 € por hora, menos de 15 € al mes encendido 5 horas al día."),
 ("¿Cuánto gasta un aire de 3.000 frigorías por hora?", "Con una eficiencia de 3,5, a plena potencia consume alrededor de 1 kW por hora, unos 0,15 €/h con el kWh a 0,15 €. En uso real (inverter) suele ser menos."),
 ("¿Cuántas frigorías necesito?", "Como referencia, unas 100 frigorías por m² en zonas calurosas: una habitación de 25 m² necesita unas 2.500 frigorías.")],
None, """function calc(){const kw=v('fr')*1.163/1000/(v('e')||1)*v('c')/100,p=v('p'),h=v('h');
show('r','Coste al mes:<b class="big">'+eur(kw*h*v('d')*p)+'</b>Por hora: '+eur(kw*p)+' ('+nf(kw,2)+' kW) · Al día: '+eur(kw*h*p));}"""))

PW = [("Frigorífico", 200, 1), ("Iluminación", 200, 1), ("TV y ordenador", 300, 1), ("Vitrocerámica / inducción", 2500, 1), ("Horno", 2000, 0),
      ("Lavadora", 2000, 1), ("Lavavajillas", 1800, 0), ("Secadora", 2500, 0), ("Microondas", 1000, 1), ("Termo eléctrico", 1500, 0),
      ("Aire acondicionado", 1200, 0), ("Calefactor / radiador", 2000, 0), ("Plancha", 2000, 0), ("Cargador coche eléctrico", 3700, 0)]
pwh = "".join(f'<label class="chk"><input type="checkbox" {"checked" if c else ""}><span>{n}</span><input type="number" value="{w}"> W</label>' for n, w, c in PW)
P.append(("potencia-contratada", "Qué potencia de luz contratar: calculadora de kW y ahorro | GastoLuz",
"Calcula qué potencia eléctrica necesitas según los aparatos que usas a la vez, si te conviene bajarla o subirla y cuánto ahorras al año en el término de potencia, impuestos incluidos.",
"""<p class="lead">Marca los aparatos que <b>sueles usar a la vez</b> en el momento de más consumo del día y escribe la potencia que tienes ahora (viene en tu factura). Te decimos la potencia que necesitas y cuánto ahorrarías o pagarías de más al año.</p>
<div class="card">""" + pwh + """<div class="row"><div><label for="ka">Potencia contratada ahora (kW)</label><input id="ka" inputmode="decimal" value="5,75"></div>
<div><label for="mg">Margen de seguridad</label><select id="mg"><option value="1.1">10 % (recomendado)</option><option value="1">Ninguno: ajustado al máximo</option><option value="1.2">20 %: prefiero que no salte nunca</option></select></div>
<div><label for="p1">Precio potencia punta (€/kW y día)</label><input id="p1" inputmode="decimal" value="0,10"></div>
<div><label for="p2">Precio potencia valle (€/kW y día)</label><input id="p2" inputmode="decimal" value="0,04"></div></div>
<p class="note">Los precios de ejemplo son orientativos: pon los de tu contrato (en la factura, «término de potencia»). El cálculo incluye el impuesto eléctrico (5,11 %) y el IVA (21 %).</p>
<div class="res" id="r" aria-live="polite"></div></div>
<h2>Cómo calcular la potencia que necesitas</h2><p>La potencia contratada es el máximo de kilovatios que puedes usar <b>a la vez</b>. Si la superas, el interruptor de control de potencia del contador corta la luz («salta el automático») y tienes que apagar algo y volver a subirlo. Por eso no importa cuánto gastas al mes, sino qué aparatos coinciden encendidos: horno, vitrocerámica, lavadora y radiador al mismo tiempo pueden sumar más de 8 kW, mientras que la nevera, la tele y las luces juntas no llegan a 1 kW.</p>
<p><b>Fórmula:</b> potencia necesaria = suma de los vatios de los aparatos simultáneos ÷ 1.000 × margen. Después se elige el escalón inmediatamente superior. El coste anual del término de potencia es kW × 365 días × (precio punta + precio valle), más impuestos.</p>
<table><tr><th>Potencia</th><th>Para qué casa suele bastar</th><th>Coste al año*</th></tr>
<tr><td>3,45 kW</td><td>Piso pequeño con gas o sin calefacción eléctrica; no usar horno y lavadora a la vez</td><td>224 €</td></tr>
<tr><td>4,6 kW</td><td>Piso medio con vitro o inducción, horno y lavadora repartidos</td><td>299 €</td></tr>
<tr><td>5,75 kW</td><td>Casa con aire acondicionado o algún radiador eléctrico</td><td>374 €</td></tr>
<tr><td>6,9 kW o más</td><td>Calefacción eléctrica, bomba de calor o cargador de coche eléctrico</td><td>448 €</td></tr></table>
<p class="note">*Con 0,10 €/kW·día en punta y 0,04 €/kW·día en valle, impuesto eléctrico e IVA incluidos. Cada kW de más cuesta unos 65 € al año con estos precios.</p>
<p><b>Ejemplo:</b> una familia tiene 5,75 kW. En su peor momento coinciden la vitrocerámica (2.500 W), el frigorífico, las luces, la tele y el microondas: unos 4,2 kW. Con un 10 % de margen necesita 4,6 kW. Bajando de 5,75 a 4,6 kW ahorra unos <b>75 € al año</b>, solo con no poner la lavadora mientras cocina.</p>
<h2>Potencia distinta de día y de noche</h2><p>Con la tarifa 2.0TD puedes contratar dos potencias: una para punta y llano (de 8:00 a 24:00 los días laborables) y otra para el valle (de 0:00 a 8:00 y todo el fin de semana y festivos). Si cargas un <a href="coste-cargar-coche-electrico.html">coche eléctrico</a> por la noche, sube solo la potencia de valle, que es mucho más barata, y mantén baja la de punta.</p>
<p>Antes de cambiar, revisa en tu área de cliente de la distribuidora tu curva de consumo: muchas muestran la potencia máxima que has alcanzado cada mes. Calcula tu recibo completo con la <a href="calcular-factura-luz.html">calculadora de la factura de la luz</a> y mira qué aparatos pesan más en la <a href="consumo-electrodomesticos.html">de consumo de electrodomésticos</a>.</p>""",
[("¿Cuánta potencia necesita un piso normal?", "Un piso medio sin calefacción eléctrica suele ir bien con 3,45 a 4,6 kW si no coinciden horno, vitro y lavadora. Con aire acondicionado o radiadores eléctricos, 5,75 kW o más."),
 ("¿Cuánto ahorro bajando la potencia contratada?", "Cada kW menos ahorra el precio del término de potencia por 365 días, más impuestos: con 0,14 €/kW·día entre punta y valle, unos 65 € al año."),
 ("¿Qué pasa si contrato menos potencia de la que necesito?", "Que el interruptor de control de potencia del contador cortará la luz cuando enciendas a la vez aparatos que superen esa potencia. No hay recargo en la factura: solo el corte, que se arregla apagando algo y volviendo a subir el interruptor."),
 ("¿Cuesta dinero cambiar la potencia?", "Bajarla suele costar poco o nada; subirla puede tener costes de derechos de acceso y extensión, que dependen de los kW que añadas. Además, la distribuidora puede no aceptar un nuevo cambio hasta que pasen 12 meses del anterior, así que conviene calcularlo bien.")],
"¿Qué potencia de luz contratar?", """const T=[2.3,3.45,4.6,5.75,6.9,8.05,9.2,10.35,11.5,14.49];
function calc(){let w=0,ev=false;document.querySelectorAll('.chk').forEach(l=>{const c=l.querySelector('[type=checkbox]'),n=l.querySelector('[type=number]');if(c.checked){w+=parseFloat(n.value)||0;if(/coche/i.test(l.textContent))ev=true;}});
const mg=parseFloat(document.getElementById('mg').value),kw=w/1000,r=T.find(t=>t>=kw*mg-1e-9)||T[T.length-1],ka=v('ka'),pk=(v('p1')+v('p2'))*365*1.0511269632*1.21;
if(kw<=0){show('r','Marca al menos un aparato.');return;}
let h='Potencia recomendada:<b class="big">'+nf(r,2)+' kW</b>Aparatos a la vez: '+nf(kw,2)+' kW'+(mg>1?' (+'+nf((mg-1)*100,0)+' % de margen)':'')+' · Término de potencia con '+nf(r,2)+' kW: <b>'+eur(r*pk)+' al año</b>';
if(ka>0){const d=(ka-r)*pk;if(d>1)h+='<br>Con tus '+nf(ka,2)+' kW pagas potencia de más: bajando a '+nf(r,2)+' kW ahorrarías <b>'+eur(d)+' al año</b> ('+eur(d/12)+' al mes).';
else if(d<-1)h+='<br>Con tus '+nf(ka,2)+' kW es probable que salte el automático si usas todo eso a la vez. Subir a '+nf(r,2)+' kW costaría <b>'+eur(-d)+' más al año</b>; la alternativa gratuita es no encender esos aparatos al mismo tiempo.';
else h+='<br>Tu potencia actual ('+nf(ka,2)+' kW) es la adecuada.';}
if(ev)h+='<br>Como cargas un coche eléctrico, plantéate contratar esta potencia solo en valle (noche) y una más baja en punta.';
show('r',h);}
document.querySelectorAll('.card input,.card select').forEach(e=>e.addEventListener(e.type=='checkbox'||e.tagName=='SELECT'?'change':'input',()=>calc()));
calc();"""))

P.append(("calculadora-kwh", "Pasar vatios a kWh y euros: calculadora de consumo eléctrico | GastoLuz",
"Convierte vatios (W) a kilovatios hora (kWh) y calcula cuánto te cuesta en euros cualquier aparato según las horas que lo usas. Con ejemplos y la fórmula explicada.",
"""<p class="lead">Convierte la potencia de cualquier aparato en energía consumida y euros.</p>
<div class="card"><div class="row"><div><label for="w">Potencia (W)</label><input id="w" inputmode="decimal" value="1000"></div>
<div><label for="h">Horas</label><input id="h" inputmode="decimal" value="1"></div></div>
<label for="p">Precio kWh (€)</label><input id="p" inputmode="decimal" value="0,15"><button onclick="calc()">Convertir</button><div class="res" id="r"></div></div>
<h2>W, kW y kWh: la diferencia</h2><p>El <b>vatio (W)</b> mide potencia: lo que «pide» un aparato en un momento. El <b>kilovatio (kW)</b> son 1.000 vatios. El <b>kilovatio hora (kWh)</b> mide energía: lo que consume un aparato de 1 kW funcionando durante una hora. En la factura pagas la potencia en kW y la energía en kWh.</p>""",
[("¿Cuántos kWh son 1.000 W?", "1.000 W durante 1 hora son 1 kWh. Durante media hora, 0,5 kWh."),
 ("¿Cuánto cuesta un kWh?", "Depende de tu tarifa y de la hora. Mira el término de energía en tu factura; esta calculadora usa 0,15 € como referencia.")],
None, """function calc(){const k=v('w')*v('h')/1000;show('r','Energía consumida:<b class="big">'+nf(k,3)+' kWh</b>Coste: <b>'+eur(k*v('p'))+'</b> · Potencia: '+nf(v('w')/1000,3)+' kW');}"""))

P.append(("coste-calefaccion-electrica", "¿Cuánto gasta un radiador eléctrico? Coste de la calefacción | GastoLuz",
"Calcula cuánto gasta tu radiador de aceite, emisor térmico, calefactor o estufa al día, al mes y en todo el invierno con el precio de la luz de hoy, y cuánto ahorrarías con bomba de calor.",
"""<p class="lead">Elige tu aparato, cuántas horas lo enciendes y verás lo que te cuesta al día, al mes y en todo el invierno, con el precio medio de la luz de hoy.</p>
<div class="card"><label for="t">Tipo de aparato</label><select id="t" onchange="tipo()"><option value="1500,1">Emisor térmico o radiador eléctrico (1.500 W)</option><option value="2000,1">Radiador de aceite (2.000 W)</option><option value="2000,1">Calefactor o termoventilador (2.000 W)</option><option value="1200,1">Estufa halógena o de cuarzo (1.200 W)</option><option value="1000,1">Panel o radiador pequeño de baño (1.000 W)</option><option value="1000,3.5">Bomba de calor / aire acondicionado (1.000 W eléctricos)</option></select>
<div class="row"><div><label for="n">Número de aparatos</label><input id="n" inputmode="numeric" value="2"></div>
<div><label for="w">Potencia de cada uno (W)</label><input id="w" inputmode="decimal" value="1500"></div>
<div><label for="h">Horas al día encendido</label><input id="h" inputmode="decimal" value="5"></div><div><label for="c">Carga media con termostato (%)</label><input id="c" inputmode="decimal" value="60"></div>
<div><label for="m">Meses de invierno</label><input id="m" inputmode="numeric" value="4"></div><div><label for="p">Precio kWh (€)</label><input id="p" inputmode="decimal" value="0,15"></div></div>
<input type="hidden" id="cop" value="1"><button onclick="calc()">Calcular</button><div class="res" id="r"></div></div>
<p class="note" id="pn">Precio orientativo. Con tarifa fija, pon el precio del kWh de tu contrato.</p>
<h2>Cómo se calcula</h2><p>Consumo diario (kWh) = aparatos × potencia (W) × horas × carga ÷ 1.000. La <b>carga</b> es el porcentaje del tiempo que la resistencia está encendida: con termostato, una vez que la habitación coge temperatura, el aparato se apaga y enciende y gasta de media entre el 40 % y el 70 % de su potencia (más en casas mal aisladas o con mucho frío fuera). Sin termostato, pon 100 %. Coste = kWh × precio del kWh (energía; la potencia contratada y los impuestos van aparte, puedes verlos en la <a href="calcular-factura-luz.html">calculadora de la factura</a>).</p>
<table><tr><th>Aparato</th><th>Gasto por hora a plena potencia</th><th>Coste por hora a 0,15 €/kWh</th></tr>
<tr><td>Radiador o emisor de 1.500 W</td><td>1,5 kWh</td><td>0,23 €</td></tr><tr><td>Radiador de aceite de 2.000 W</td><td>2 kWh</td><td>0,30 €</td></tr><tr><td>Estufa halógena de 1.200 W</td><td>1,2 kWh</td><td>0,18 €</td></tr><tr><td>Bomba de calor (3.500 W de calor)</td><td>1 kWh</td><td>0,15 €</td></tr></table>
<p><b>Ejemplo:</b> dos emisores de 1.500 W encendidos 5 horas al día con el termostato trabajando al 60 % gastan 9 kWh al día. A 0,15 €/kWh son 1,35 € diarios, unos 41 € al mes y 164 € en cuatro meses de invierno. La misma calefacción con una bomba de calor de rendimiento 3,5 costaría unos 12 € al mes.</p>
<h2>¿Qué calefacción eléctrica es más barata?</h2><p>Todos los radiadores eléctricos convierten la electricidad en calor con el mismo rendimiento: 1.500 W gastan lo mismo sea emisor «de bajo consumo», aceite o calefactor. Lo que cambia es cómo reparten el calor (el aceite y los emisores lo guardan más tiempo; el calefactor calienta rápido pero se enfría pronto) y lo bien que funciona su termostato. La única forma eléctrica realmente más barata es la <a href="coste-aire-acondicionado.html">bomba de calor</a>, que da 3 o 4 veces más calor por cada kWh. Si tienes tarifa PVPC, programa los radiadores en las <a href="precio-luz-hoy.html">horas más baratas de hoy</a> y baja el termostato a 19-20 °C: cada grado menos ahorra en torno a un 7 %.</p>""",
[("¿Cuánto gasta un radiador de 1.500 W?", "A plena potencia, 1,5 kWh por hora: unos 0,23 € con el kWh a 0,15 €. Con termostato suele trabajar el 50-70 % del tiempo, así que la hora real sale por 0,11 – 0,16 €."),
 ("¿Cuánto gasta un radiador de aceite al mes?", "Uno de 2.000 W encendido 6 horas al día con el termostato al 60 % gasta unos 7,2 kWh diarios: alrededor de 33 € al mes a 0,15 €/kWh."),
 ("¿Los emisores térmicos de bajo consumo gastan menos?", "No. Un emisor de 1.500 W consume 1,5 kWh por hora igual que cualquier otro radiador de 1.500 W. Pueden gastar algo menos en la práctica solo si su termostato es más preciso y mantienen mejor el calor."),
 ("¿Es mejor la bomba de calor?", "Sí: con un rendimiento de 3-4, calienta lo mismo gastando entre un 65 % y un 75 % menos que un radiador eléctrico.")],
"¿Cuánto gasta un radiador eléctrico? Calculadora de calefacción", """function tipo(){const x=document.getElementById('t').value.split(',');document.getElementById('w').value=x[0];document.getElementById('cop').value=x[1];calc();}
function calc(){const kd=v('n')*v('w')*v('h')*v('c')/100/1000,p=v('p'),mes=kd*30.4*p,cop=v('cop')||1;
let h='Coste al mes:<b class="big">'+eur(mes)+'</b>Al día: <b>'+eur(kd*p)+'</b> ('+nf(kd,1)+' kWh) · Todo el invierno: <b>'+eur(mes*v('m'))+'</b>';
h+=cop>1?'<br>Con resistencias eléctricas, el mismo calor costaría unos '+eur(mes*cop)+' al mes.':'<br>Con bomba de calor (rendimiento 3,5) sería aprox. <b>'+eur(mes/3.5)+'</b> al mes: ahorrarías '+eur((mes-mes/3.5)*v('m'))+' cada invierno.';
show('r',h);}
fetch('pvpc.json',{cache:'no-store'}).then(r=>r.json()).then(j=>{const k=Object.keys(j.dias).sort(),d=new Date(),t=d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0'),H=j.dias[t]||j.dias[k[k.length-1]];if(!H||!H.length)return;const av=H.reduce((s,x)=>s+x[1],0)/H.length;document.getElementById('p').value=av.toFixed(3).replace('.',',');document.getElementById('pn').innerHTML='Precio: media del PVPC de '+(j.dias[t]?'hoy':'último día disponible')+' según Red Eléctrica ('+av.toFixed(3).replace('.',',')+' €/kWh). Si tienes tarifa fija, pon el precio del kWh de tu contrato. <a href="precio-luz-hoy.html">Ver horas más baratas</a>.';calc();}).catch(()=>{});"""))

P.append(("ahorro-led", "¿Cuánto ahorro con bombillas LED? Calculadora de ahorro al año | GastoLuz",
"Calcula cuánto ahorras al año cambiando bombillas incandescentes o halógenas por LED, cuántos kWh dejas de gastar y en cuántos meses se amortizan.",
"""<p class="lead">Pon cuántas bombillas tienes, su potencia y las horas que están encendidas: te decimos cuánto ahorras al año con LED y en cuántos meses recuperas lo que cuestan.</p>
<div class="card"><div class="row"><div><label for="n">Número de bombillas</label><input id="n" inputmode="numeric" value="10"></div>
<div><label for="o">Potencia bombilla actual (W)</label><input id="o" inputmode="decimal" value="60"></div>
<div><label for="l">Potencia LED equivalente (W)</label><input id="l" inputmode="decimal" value="9"></div><div><label for="h">Horas al día</label><input id="h" inputmode="decimal" value="4"></div>
<div><label for="pr">Precio de cada LED (€)</label><input id="pr" inputmode="decimal" value="3"></div><div><label for="p">Precio kWh (€)</label><input id="p" inputmode="decimal" value="0,15"></div></div>
<button onclick="calc()">Calcular ahorro</button><div class="res" id="r"></div></div>
<h2>Equivalencias habituales</h2><table><tr><th>Incandescente</th><th>Halógena</th><th>LED</th></tr><tr><td>40 W</td><td>28 W</td><td>5-6 W</td></tr><tr><td>60 W</td><td>42 W</td><td>8-9 W</td></tr><tr><td>100 W</td><td>70 W</td><td>13-15 W</td></tr></table>
<p>Fíjate en los lúmenes (lm), no en los vatios: una bombilla de 806 lm ilumina como una incandescente de 60 W.</p>
<h2>Cómo se calcula el ahorro</h2><p>Ahorro anual (kWh) = número de bombillas × (vatios actuales − vatios LED) × horas al día × 365 ÷ 1.000. Multiplicado por el precio del kWh da los euros que dejas de pagar, y dividiendo lo que cuestan las LED entre ese ahorro sale el tiempo de amortización.</p>
<p><b>Ejemplo:</b> 10 bombillas incandescentes de 60 W encendidas 4 horas al día gastan 876 kWh al año. Con LED de 9 W bajan a 131 kWh: ahorras 745 kWh, unos <b>112 € al año</b> a 0,15 €/kWh. Si cada LED cuesta 3 €, los 30 € se recuperan en algo más de <b>3 meses</b>. Cambiando halógenas de 42 W el ahorro es menor (unos 72 € al año), pero la amortización sigue siendo de pocos meses.</p>
<h2>Dónde se nota más</h2><ul><li>En las luces que más horas pasan encendidas: salón, cocina, pasillos y exteriores.</li><li>En los focos halógenos GU10 de techo, que suelen ser muchos y de 35-50 W cada uno.</li><li>En los adornos: las guirnaldas LED gastan hasta un 90 % menos. Calcula cuánto cuestan las tuyas con la calculadora de <a href="consumo-luces-navidad.html">consumo de las luces de Navidad</a>.</li></ul>
<p>Para ver qué más puedes recortar, prueba la calculadora de <a href="consumo-electrodomesticos.html">consumo de electrodomésticos</a> o pasa cualquier potencia a euros con la de <a href="calculadora-kwh.html">vatios a kWh</a>.</p>""",
[("¿Cuánto se ahorra con LED?", "Alrededor de un 80-85 % respecto a una incandescente y un 75-80 % respecto a una halógena. Una sola bombilla de 60 W cambiada por una LED de 9 W, encendida 4 horas al día, ahorra unos 11 € al año a 0,15 €/kWh."),
 ("¿Cuánto dura una bombilla LED?", "Entre 15.000 y 25.000 horas, frente a unas 1.000 de una incandescente. Usada 4 horas al día, una LED puede durar más de 10 años."),
 ("¿Qué bombilla LED equivale a una de 60 W?", "Una LED de unos 806 lúmenes, que suele consumir entre 8 y 9 W. Para sustituir una de 100 W busca unos 1.521 lúmenes (13-15 W)."),
 ("¿Compensa cambiar las halógenas por LED?", "Sí. Una halógena de 42 W cambiada por una LED de 9 W ahorra el 79 % de su consumo y la inversión se recupera en pocos meses si está encendida varias horas al día.")],
None, """function calc(){const n=v('n'),kwh=n*(v('o')-v('l'))*v('h')*365/1000,a=kwh*v('p'),inv=n*v('pr');
show('r','Ahorro al año:<b class="big">'+eur(a)+'</b>'+nf(kwh,0)+' kWh menos · Inversión: '+eur(inv)+' · Se amortiza en <b>'+(a>0?nf(inv/a*12,1)+' meses':'—')+'</b>');}"""))

exec(open("extra_luz.py").read())
build(S, P)
