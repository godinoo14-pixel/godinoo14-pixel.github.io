from gen import build
S = dict(dir="gastoluz", name="GastoLuz", logo="Gasto<span>Luz</span>", acc="#0b7285",
         base="https://godinoo14-pixel.github.io/gastoluz/",
         tools=[("consumo-electrodomesticos", "Consumo de electrodomésticos", "Cuánto gasta al mes cada aparato de tu casa.", "Electrodomésticos"),
                ("coste-aire-acondicionado", "Coste del aire acondicionado", "Lo que pagas por encender el aire o la bomba de calor.", "Aire acondicionado"),
                ("potencia-contratada", "¿Qué potencia contratar?", "Calcula los kW que necesitas y evita pagar de más.", "Potencia"),
                ("calculadora-kwh", "Calculadora de vatios a kWh", "Pasa vatios a kWh y a euros.", ""),
                ("coste-calefaccion-electrica", "Coste de la calefacción eléctrica", "Radiador, calefactor o estufa: cuánto cuesta el invierno.", ""),
                ("ahorro-led", "Ahorro al cambiar a LED", "Cuánto ahorras sustituyendo bombillas antiguas.", "")],
         home_title="GastoLuz | Calcula el consumo eléctrico de tu casa y cuánto pagas",
         home_desc="Calculadoras de consumo eléctrico: electrodomésticos, aire acondicionado, calefacción, potencia contratada, vatios a kWh y ahorro LED.",
         home_h1="Calcula cuánto gastas en luz",
         home_intro='<p class="lead">Descubre qué aparatos disparan tu factura, qué potencia necesitas contratar y cuánto puedes ahorrar. Cambia el precio del kWh por el de tu factura para un resultado exacto.</p>',
         home_extra='<h2>Dónde ver el precio del kWh</h2><p>En tu factura aparece el <b>término de energía</b> en €/kWh (a veces dividido en punta, llano y valle) y el <b>término de potencia</b> en €/kW y día. Nuestras calculadoras usan 0,15 €/kWh como referencia, pero puedes poner el tuyo en cada una.</p>')

APP = [("Frigorífico", 150, 24, "Funciona a ciclos: equivale a unas 8 h reales al día"), ("Horno", 2000, 0.5, ""), ("Lavadora (ciclo 40 °C)", 900, 1, ""),
       ("Secadora", 2500, 1, ""), ("Lavavajillas", 1500, 1, ""), ("Vitrocerámica / inducción", 1800, 1, ""), ("Microondas", 1000, 0.2, ""),
       ("Termo eléctrico", 1500, 3, ""), ("Televisor", 100, 4, ""), ("Ordenador de sobremesa", 200, 4, ""), ("Portátil", 60, 6, ""),
       ("Plancha", 2000, 0.3, ""), ("Secador de pelo", 1800, 0.2, ""), ("Freidora de aire", 1500, 0.5, ""), ("Cafetera", 1200, 0.1, ""), ("Consola", 150, 2, "")]
opts = "".join(f'<option value="{w}|{h}">{n}</option>' for n, w, h, _ in APP)

P = []
P.append(("consumo-electrodomesticos", "Consumo de electrodomésticos: cuánto gasta cada aparato | GastoLuz",
"Calcula cuánto consume y cuánto cuesta al día, al mes y al año cualquier electrodoméstico según su potencia y horas de uso.",
"""<p class="lead">Elige un aparato (o pon su potencia en vatios), las horas de uso y el precio del kWh.</p>
<div class="card"><label for="ap">Electrodoméstico</label><select id="ap" onchange="pre()">""" + opts + """</select>
<div class="row"><div><label for="w">Potencia (W)</label><input id="w" inputmode="decimal"></div><div><label for="h">Horas de uso al día</label><input id="h" inputmode="decimal"></div>
<div><label for="p">Precio kWh (€)</label><input id="p" inputmode="decimal" value="0,15"></div><div><label for="f">Factor de uso (%)</label><input id="f" inputmode="decimal" value="100"></div></div>
<button onclick="calc()">Calcular consumo</button><div class="res" id="r"></div></div>
<p class="note">La potencia viene en la etiqueta o en el manual. El frigorífico y otros aparatos con termostato no funcionan a plena potencia todo el tiempo: para ellos usa un factor de uso del 30-40 %.</p>
<h2>Los aparatos que más gastan</h2><p>Los que producen calor son los que más consumen: secadora, horno, termo eléctrico, calefactores y vitrocerámica. El frigorífico gasta poco por hora pero está encendido todo el año, por eso suele ser uno de los mayores consumos de la casa. Programar lavadora y lavavajillas en horas valle puede reducir mucho su coste.</p>""",
[("¿Cuánto gasta un frigorífico al mes?", "Un frigorífico moderno consume entre 20 y 40 kWh al mes, unos 3-6 € con el kWh a 0,15 €. Los antiguos pueden gastar el doble."),
 ("¿Cómo paso vatios a kWh?", "Multiplica los vatios por las horas de uso y divide entre 1.000. Un aparato de 2.000 W durante 1 hora consume 2 kWh.")],
None, """function pre(){const [w,h]=document.getElementById('ap').value.split('|');document.getElementById('w').value=w;document.getElementById('h').value=h;document.getElementById('f').value=(w==150&&h==24)?35:100;}
function calc(){const k=v('w')*v('h')*v('f')/100/1000,p=v('p');show('r','Coste al mes:<b class="big">'+eur(k*p*30.4)+'</b>Al día: '+nf(k,2)+' kWh ('+eur(k*p)+') · Al año: '+nf(k*365,0)+' kWh (<b>'+eur(k*p*365)+'</b>)');}pre();"""))

P.append(("coste-aire-acondicionado", "¿Cuánto gasta el aire acondicionado? Calculadora | GastoLuz",
"Calcula cuánto cuesta tener encendido el aire acondicionado o la bomba de calor por hora, al día y al mes según frigorías y eficiencia.",
"""<p class="lead">Calcula el coste de tu aire acondicionado a partir de sus frigorías (o kW de frío) y su eficiencia.</p>
<div class="card"><div class="row"><div><label for="fr">Frigorías</label><input id="fr" inputmode="numeric" value="3000"></div>
<div><label for="e">Eficiencia (EER/SEER)</label><input id="e" inputmode="decimal" value="3,5"></div>
<div><label for="h">Horas al día</label><input id="h" inputmode="decimal" value="6"></div><div><label for="d">Días al mes</label><input id="d" inputmode="numeric" value="30"></div>
<div><label for="c">Carga media (%)</label><input id="c" inputmode="decimal" value="60"></div><div><label for="p">Precio kWh (€)</label><input id="p" inputmode="decimal" value="0,15"></div></div>
<button onclick="calc()">Calcular</button><div class="res" id="r"></div></div>
<p class="note">Un equipo inverter no trabaja al 100 % todo el tiempo: una vez alcanzada la temperatura baja el ritmo. Una carga media del 50-70 % es realista.</p>
<h2>Cómo gastar menos con el aire</h2><ul><li>Pon el termostato a 25-26 °C: cada grado menos sube el consumo alrededor de un 7 %.</li><li>Limpia los filtros cada mes en verano.</li><li>Baja persianas y toldos en las horas de sol.</li><li>Usa el modo «eco» o «sleep» por la noche.</li></ul>""",
[("¿Cuánto gasta un aire de 3.000 frigorías por hora?", "Con una eficiencia de 3,5, a plena potencia consume alrededor de 1 kW por hora, unos 0,15 €/h con el kWh a 0,15 €. En uso real (inverter) suele ser menos."),
 ("¿Cuántas frigorías necesito?", "Como referencia, unas 100 frigorías por m² en zonas calurosas: una habitación de 25 m² necesita unas 2.500 frigorías.")],
None, """function calc(){const kw=v('fr')*1.163/1000/(v('e')||1)*v('c')/100,p=v('p'),h=v('h');
show('r','Coste al mes:<b class="big">'+eur(kw*h*v('d')*p)+'</b>Por hora: '+eur(kw*p)+' ('+nf(kw,2)+' kW) · Al día: '+eur(kw*h*p));}"""))

PW = [("Frigorífico", 200, 1), ("Iluminación", 200, 1), ("TV y ordenador", 300, 1), ("Vitrocerámica / inducción", 2500, 1), ("Horno", 2000, 0),
      ("Lavadora", 2000, 1), ("Lavavajillas", 1800, 0), ("Secadora", 2500, 0), ("Microondas", 1000, 1), ("Termo eléctrico", 1500, 0),
      ("Aire acondicionado", 1200, 0), ("Calefactor / radiador", 2000, 0), ("Plancha", 2000, 0), ("Cargador coche eléctrico", 3700, 0)]
pwh = "".join(f'<label class="chk"><input type="checkbox" {"checked" if c else ""}><span>{n}</span><input type="number" value="{w}"> W</label>' for n, w, c in PW)
P.append(("potencia-contratada", "¿Qué potencia de luz contratar? Calculadora de kW | GastoLuz",
"Calcula la potencia eléctrica que necesitas contratar según los aparatos que usas a la vez y deja de pagar potencia de más.",
"""<p class="lead">Marca los aparatos que <b>sueles usar a la vez</b> en el momento de más consumo del día.</p>
<div class="card">""" + pwh + """<label for="p">Precio de la potencia (€/kW y año)</label><input id="p" inputmode="decimal" value="30">
<button onclick="calc()">Calcular potencia</button><div class="res" id="r"></div></div>
<p class="note">Si «salta el ICP» (el interruptor general) a menudo, necesitas más potencia o repartir mejor el uso. Si nunca salta, quizá puedas bajarla y ahorrar.</p>
<h2>Cómo ahorrar en el término de potencia</h2><p>Pagas la potencia todos los días aunque no la uses. Bajar un tramo (por ejemplo, de 5,75 a 4,6 kW) puede ahorrar decenas de euros al año. Con la tarifa 2.0TD puedes contratar potencias distintas en punta y en valle: si cargas un coche eléctrico por la noche, sube solo la del periodo valle.</p>""",
[("¿Cuánta potencia necesita un piso normal?", "Un piso medio sin calefacción eléctrica suele ir bien con 3,45 a 4,6 kW. Con aire acondicionado, horno y vitro a la vez, 5,75 kW o más."),
 ("¿Cuesta dinero cambiar la potencia?", "Bajar potencia suele ser gratis o barato; subirla puede tener costes de derechos de acometida. Consulta con tu comercializadora.")],
None, """const T=[2.3,3.45,4.6,5.75,6.9,8.05,9.2,10.35,11.5,14.49];
function calc(){let w=0;document.querySelectorAll('.chk').forEach(l=>{const c=l.querySelector('[type=checkbox]'),n=l.querySelector('[type=number]');if(c.checked)w+=parseFloat(n.value)||0;});
const kw=w/1000,r=T.find(t=>t>=kw*1.1)||T[T.length-1];show('r','Potencia recomendada:<b class="big">'+nf(r,2)+' kW</b>Consumo simultáneo: '+nf(kw,2)+' kW (+10 % de margen) · Coste aprox. del término de potencia: <b>'+eur(r*v('p'))+'/año</b>');}"""))

P.append(("calculadora-kwh", "Calculadora de vatios a kWh y euros | GastoLuz",
"Convierte vatios (W) a kilovatios hora (kWh) y calcula cuánto cuesta en euros según las horas de uso.",
"""<p class="lead">Convierte la potencia de cualquier aparato en energía consumida y euros.</p>
<div class="card"><div class="row"><div><label for="w">Potencia (W)</label><input id="w" inputmode="decimal" value="1000"></div>
<div><label for="h">Horas</label><input id="h" inputmode="decimal" value="1"></div></div>
<label for="p">Precio kWh (€)</label><input id="p" inputmode="decimal" value="0,15"><button onclick="calc()">Convertir</button><div class="res" id="r"></div></div>
<h2>W, kW y kWh: la diferencia</h2><p>El <b>vatio (W)</b> mide potencia: lo que «pide» un aparato en un momento. El <b>kilovatio (kW)</b> son 1.000 vatios. El <b>kilovatio hora (kWh)</b> mide energía: lo que consume un aparato de 1 kW funcionando durante una hora. En la factura pagas la potencia en kW y la energía en kWh.</p>""",
[("¿Cuántos kWh son 1.000 W?", "1.000 W durante 1 hora son 1 kWh. Durante media hora, 0,5 kWh."),
 ("¿Cuánto cuesta un kWh?", "Depende de tu tarifa y de la hora. Mira el término de energía en tu factura; esta calculadora usa 0,15 € como referencia.")],
None, """function calc(){const k=v('w')*v('h')/1000;show('r','Energía consumida:<b class="big">'+nf(k,3)+' kWh</b>Coste: <b>'+eur(k*v('p'))+'</b> · Potencia: '+nf(v('w')/1000,3)+' kW');}"""))

P.append(("coste-calefaccion-electrica", "Coste de la calefacción eléctrica: radiador, calefactor y estufa | GastoLuz",
"Calcula cuánto cuesta calentar tu casa con radiadores eléctricos, calefactores o estufas de aceite durante el invierno.",
"""<p class="lead">Calcula el coste mensual y de todo el invierno de tus aparatos de calefacción eléctrica.</p>
<div class="card"><div class="row"><div><label for="n">Número de aparatos</label><input id="n" inputmode="numeric" value="2"></div>
<div><label for="w">Potencia de cada uno (W)</label><input id="w" inputmode="decimal" value="1500"></div>
<div><label for="h">Horas al día</label><input id="h" inputmode="decimal" value="5"></div><div><label for="c">Carga media con termostato (%)</label><input id="c" inputmode="decimal" value="60"></div>
<div><label for="m">Meses de invierno</label><input id="m" inputmode="numeric" value="4"></div><div><label for="p">Precio kWh (€)</label><input id="p" inputmode="decimal" value="0,15"></div></div>
<button onclick="calc()">Calcular</button><div class="res" id="r"></div></div>
<h2>¿Qué calefacción eléctrica es más barata?</h2><p>Todos los radiadores eléctricos convierten la electricidad en calor con un rendimiento parecido: 1.500 W gastan lo mismo sea emisor, aceite o calefactor. Lo que cambia es cómo reparten el calor y lo bien que funciona su termostato. La única forma eléctrica realmente más barata es la <a href="coste-aire-acondicionado.html">bomba de calor</a>, que da 3 o 4 veces más calor por cada kWh.</p>""",
[("¿Cuánto gasta un radiador de 1.500 W?", "A plena potencia, 1,5 kWh por hora: unos 0,23 € con el kWh a 0,15 €. Con termostato, normalmente menos."),
 ("¿Es mejor la bomba de calor?", "Sí: con un rendimiento de 3-4, calienta lo mismo gastando entre un 65 % y un 75 % menos que un radiador eléctrico.")],
None, """function calc(){const kd=v('n')*v('w')*v('h')*v('c')/100/1000,p=v('p'),mes=kd*30.4*p;
show('r','Coste al mes:<b class="big">'+eur(mes)+'</b>Todo el invierno: <b>'+eur(mes*v('m'))+'</b> · '+nf(kd,1)+' kWh/día<br>Con bomba de calor (rendimiento 3,5) sería aprox. '+eur(mes/3.5)+'/mes');}"""))

P.append(("ahorro-led", "Ahorro al cambiar bombillas a LED: calculadora | GastoLuz",
"Calcula cuánto ahorras al año sustituyendo bombillas incandescentes o halógenas por LED y en cuánto tiempo se amortizan.",
"""<p class="lead">Calcula el ahorro anual y el tiempo de amortización de cambiar tus bombillas a LED.</p>
<div class="card"><div class="row"><div><label for="n">Número de bombillas</label><input id="n" inputmode="numeric" value="10"></div>
<div><label for="o">Potencia bombilla actual (W)</label><input id="o" inputmode="decimal" value="60"></div>
<div><label for="l">Potencia LED equivalente (W)</label><input id="l" inputmode="decimal" value="9"></div><div><label for="h">Horas al día</label><input id="h" inputmode="decimal" value="4"></div>
<div><label for="pr">Precio de cada LED (€)</label><input id="pr" inputmode="decimal" value="3"></div><div><label for="p">Precio kWh (€)</label><input id="p" inputmode="decimal" value="0,15"></div></div>
<button onclick="calc()">Calcular ahorro</button><div class="res" id="r"></div></div>
<h2>Equivalencias habituales</h2><table><tr><th>Incandescente</th><th>Halógena</th><th>LED</th></tr><tr><td>40 W</td><td>28 W</td><td>5-6 W</td></tr><tr><td>60 W</td><td>42 W</td><td>8-9 W</td></tr><tr><td>100 W</td><td>70 W</td><td>13-15 W</td></tr></table>
<p>Fíjate en los lúmenes (lm), no en los vatios: una bombilla de 806 lm ilumina como una incandescente de 60 W.</p>""",
[("¿Cuánto se ahorra con LED?", "Alrededor de un 80-85 % respecto a una incandescente y un 75-80 % respecto a una halógena."),
 ("¿Cuánto dura una bombilla LED?", "Entre 15.000 y 25.000 horas, frente a unas 1.000 de una incandescente.")],
None, """function calc(){const n=v('n'),kwh=n*(v('o')-v('l'))*v('h')*365/1000,a=kwh*v('p'),inv=n*v('pr');
show('r','Ahorro al año:<b class="big">'+eur(a)+'</b>'+nf(kwh,0)+' kWh menos · Inversión: '+eur(inv)+' · Se amortiza en <b>'+(a>0?nf(inv/a*12,1)+' meses':'—')+'</b>');}"""))

exec(open("extra_luz.py").read())
build(S, P)
