from gen import build
S = dict(dir="cochecuentas", name="CocheCuentas", logo="Coche<span>Cuentas</span>", acc="#d9480f",
         base="https://cochecuentas.es/", domain="cochecuentas.es",
         tools=[("etiqueta-dgt", "Etiqueta DGT por matrícula", "Escribe la matrícula y te decimos su etiqueta oficial: 0, ECO, C, B o sin etiqueta.", "Etiqueta DGT"),
                ("coste-por-km", "Coste por kilómetro", "Cuánto te cuesta cada km y cada mes en combustible.", "Coste/km"),
                ("electrico-vs-gasolina", "Eléctrico vs gasolina o diésel", "Cuánto ahorras al año pasándote al eléctrico.", "Eléctrico vs"),
                ("coste-anual-coche", "Coste anual real de un coche", "Seguro, impuesto, ITV, mantenimiento, combustible y pérdida de valor.", ""),
                ("depreciacion-coche", "Calculadora de depreciación", "Cuánto valdrá tu coche dentro de X años.", ""),
                ("coste-viaje-coche", "Coste de un viaje en coche", "Combustible y peajes de un trayecto, dividido entre ocupantes.", "")],
         about="<p>CocheCuentas lo crea un asesor comercial y tasador con años de experiencia en concesionarios oficiales y compraventas de vehículos. Las calculadoras nacen de las preguntas que los clientes hacen a diario: cuánto cuesta de verdad un coche, si compensa el eléctrico, cuánto valdrá dentro de unos años o qué etiqueta le corresponde.</p>",
         home_title="Calculadoras de coche gratis: matrícula, etiqueta DGT y gasolineras | CocheCuentas",
         home_desc="Consulta cualquier coche por su matrícula (etiqueta DGT, año e ITV), encuentra la gasolinera más barata y calcula coste por km, impuesto de matriculación y financiación. Gratis.",
         home_h1="Calculadoras para tu coche",
         home_intro='<form class="card" style="border:2px solid #d9480f" onsubmit="var v=this.m.value.toUpperCase().replace(/[^A-Z0-9]/g,\'\');if(v)location.href=\'historial-coche-matricula.html?m=\'+v;return false"><b style="font-size:1.15rem">Consulta cualquier coche por su matrícula</b><p class="note" style="margin:4px 0 0">Etiqueta DGT oficial, año de matriculación, antigüedad y próxima ITV. Gratis y al momento.</p><input name="m" placeholder="1234 KLM" autocapitalize="characters" autocomplete="off" enterkeyhint="search" style="font-size:1.4rem;letter-spacing:3px;text-transform:uppercase;text-align:center;margin-top:12px"><button>Consultar matrícula</button></form><p class="lead">Herramientas gratuitas y rápidas para saber cuánto te cuesta de verdad tu coche, qué etiqueta medioambiental le corresponde y si te compensa cambiarte al eléctrico. Hechas por un profesional del sector del automóvil.</p>',
         home_extra='<h2>¿Por qué calcular el coste real de tu coche?</h2><p>La mayoría de conductores solo piensa en la letra o en el combustible, pero un coche también cuesta seguro, impuesto de circulación, ITV, neumáticos, revisiones y, sobre todo, la pérdida de valor. Sumarlo todo te ayuda a decidir si comprar, mantener o cambiar de coche con números en la mano.</p>')

P = []
P.append(("etiqueta-dgt", "Etiqueta DGT por matrícula: consulta qué distintivo tiene tu coche | CocheCuentas",
"Escribe la matrícula y te decimos al instante la etiqueta medioambiental oficial de tu coche o moto: 0, ECO, C, B o sin etiqueta. Datos oficiales de la DGT actualizados a diario.",
"""<p class="lead">Escribe la matrícula y te decimos al momento la etiqueta medioambiental de tu coche, moto o ciclomotor. Solo la matrícula, nada más.</p>
<div class="card"><label for="m">Matrícula</label><input id="m" placeholder="1234 KLM" autocapitalize="characters" autocomplete="off" enterkeyhint="search" onkeydown="if(event.key==='Enter')calc()" style="font-size:1.5rem;letter-spacing:3px;text-transform:uppercase;text-align:center">
<button onclick="calc()">Ver mi etiqueta</button><div class="res" id="r"></div>
<p class="note" id="fd" style="margin-top:12px">Datos oficiales del registro de la DGT, actualizados cada día.</p></div>
<p class="note">Funciona con todas las matrículas españolas: las actuales (1234 KLM), las provinciales antiguas (MA-1234-BZ) y las de ciclomotor (C-1234-BCD). No guardamos las matrículas que consultas.</p>
<h2>Qué significa cada etiqueta</h2><table><tr><th>Etiqueta</th><th>Turismos y furgonetas ligeras</th></tr>
<tr><td><b>0 emisiones</b></td><td>Eléctricos de batería, de autonomía extendida, híbridos enchufables con 40 km o más de autonomía y pila de combustible.</td></tr>
<tr><td><b>ECO</b></td><td>Enchufables con menos de 40 km, híbridos no enchufables y vehículos de gas que además cumplen los criterios de la C.</td></tr>
<tr><td><b>C</b></td><td>Gasolina matriculados desde enero de 2006 y diésel desde septiembre de 2015.</td></tr>
<tr><td><b>B</b></td><td>Gasolina matriculados desde enero de 2001 y diésel desde 2006.</td></tr>
<tr><td><b>Sin etiqueta</b></td><td>Gasolina anteriores a 2001 y diésel anteriores a 2006.</td></tr></table>
<h2>¿Para qué sirve la etiqueta?</h2><p>Las zonas de bajas emisiones (ZBE) de las ciudades usan el distintivo para decidir quién puede entrar, aparcar o pagar menos en zona regulada. Los vehículos sin etiqueta son los más afectados por las restricciones, y llevar la pegatina en el parabrisas es obligatorio en muchas ciudades para circular por esas zonas.</p>
<p class="note">Fuente de los datos: Dirección General de Tráfico, fichero abierto de distintivos ambientales del parque de vehículos.</p>""",
[("¿Cómo sé qué etiqueta tiene mi coche?", "Escribe la matrícula en esta página y te diremos al instante su distintivo ambiental según el registro oficial de la DGT, que se actualiza cada día."),
 ("¿Desde cuándo tienen etiqueta C los diésel?", "Según la DGT, los turismos diésel matriculados a partir de septiembre de 2015 tienen etiqueta C; los matriculados desde 2006 tienen la B."),
 ("¿Por qué mi coche no tiene etiqueta?", "Porque no cumple las normas de emisiones Euro necesarias: en turismos, suelen ser gasolina anteriores a 2001 y diésel anteriores a 2006."),
 ("¿Dónde se compra la pegatina?", "En oficinas de Correos, talleres autorizados, gestorías y estancos autorizados, presentando el permiso de circulación.")],
"Etiqueta DGT por matrícula",
"""const N={1:['B','#f59f00','Etiqueta amarilla.'],2:['C','#37b24d','Etiqueta verde.'],3:['ECO','#2f9e44','Etiqueta verde y azul.'],4:['0 EMISIONES','#1c7ed6','Etiqueta azul.'],5:['SIN ETIQUETA','#868e96','No tiene derecho a distintivo ambiental. Revisa las zonas de bajas emisiones de tu ciudad.']};
N[6]=N[1];N[7]=N[2];N[8]=N[3];N[9]=N[4];
fetch('dgt/fecha.txt').then(r=>r.ok?r.text():'').then(t=>{if(t)document.getElementById('fd').textContent='Datos oficiales del registro de la DGT, actualizados el '+t.trim()+'.';}).catch(()=>{});
async function calc(){const raw=document.getElementById('m').value.toUpperCase().replace(/[^A-Z0-9]/g,'');
if(!raw){document.getElementById('r').style.display='none';return;}
show('r','Buscando '+raw+'…');let v=0,m;
try{if(m=raw.match(/^(\\d{4})([B-DF-HJ-NP-TV-Z]{3})$/)){const r=await fetch('dgt/m/'+m[2]+'.bin');if(r.ok){const b=new Uint8Array(await r.arrayBuffer());const n=+m[1],x=b[n>>1]||0;v=n&1?x>>4:x&15;}}
else if(m=raw.match(/^([A-Z]{1,2})(\\d{3,})([A-Z]*)$/)){const r=await fetch('dgt/o/'+m[1]+m[2].slice(0,2)+'.txt');if(r.ok){const k=m[2].slice(2)+m[3]+':';const l=(await r.text()).split('\\n').find(x=>x.startsWith(k));if(l)v=+l.slice(k.length);}}
else{show('r','Escribe una matrícula válida, por ejemplo <b>1234 KLM</b>.');return;}}
catch(e){show('r','No hemos podido consultar ahora mismo. Inténtalo de nuevo en unos segundos.');return;}
if(!N[v]){show('r','No encontramos la matrícula <b>'+raw+'</b> en el registro. Revisa que esté bien escrita.');return;}
show('r','La matrícula <b>'+raw+'</b> tiene:<b class="big" style="color:'+N[v][1]+'">'+N[v][0]+'</b>'+N[v][2]);}"""))

P.append(("coste-por-km", "Coste por kilómetro de tu coche: calculadora de gasolina y diésel | CocheCuentas",
"¿Cuánto te cuesta cada kilómetro? Pon el consumo de tu coche y el precio del litro y verás el gasto en combustible por km, al mes y al año. Gratis y al instante.",
"""<p class="lead">Mete el consumo de tu coche, el precio del combustible y los kilómetros que haces y verás cuánto gastas por km, al mes y al año.</p>
<div class="card"><div class="row"><div><label for="c">Consumo (L/100 km)</label><input id="c" inputmode="decimal" value="6,5"></div>
<div><label for="p">Precio del litro (€)</label><input id="p" inputmode="decimal" value="1,55"></div></div>
<label for="k">Kilómetros al año</label><input id="k" inputmode="numeric" value="15000"><button onclick="calc()">Calcular</button><div class="res" id="r"></div></div>
<h2>Cómo se calcula</h2><p>Coste por km = consumo ÷ 100 × precio del litro. Si tu coche gasta 6,5 litros a los 100 km y el litro cuesta 1,55 €, cada kilómetro te sale a unos 0,10 €. El consumo real suele ser entre un 10 % y un 25 % mayor que el homologado, sobre todo en ciudad, así que usa el que marca tu ordenador de a bordo.</p>
<h2>Trucos para gastar menos</h2><ul><li>Revisa la presión de los neumáticos cada mes.</li><li>Conduce en marchas largas y anticipa las frenadas.</li><li>Quita la baca o el cofre si no lo usas.</li><li>Compara precios de gasolineras: la diferencia puede superar los 15 céntimos por litro.</li></ul>""",
[("¿Cuánto cuesta un kilómetro en coche de media?", "Solo en combustible, un turismo medio de gasolina gasta entre 0,08 y 0,12 € por km. Contando seguro, mantenimiento y depreciación, el coste total suele estar entre 0,25 y 0,45 € por km."),
 ("¿Cómo sé el consumo real de mi coche?", "Llena el depósito, pon el parcial a cero y, en el siguiente repostaje, divide los litros repostados entre los km recorridos y multiplica por 100.")],
None,
"""function calc(){const c=v('c'),p=v('p'),k=v('k'),km=c/100*p;
show('r','Coste por km:<b class="big">'+nf(km,3)+' €</b>Al mes: <b>'+eur(km*k/12)+'</b> · Al año: <b>'+eur(km*k)+'</b> · Litros/año: '+nf(c/100*k,0));}"""))

P.append(("electrico-vs-gasolina", "Coche eléctrico vs gasolina o diésel: ¿cuánto ahorro? | CocheCuentas",
"Compara el coste de recorrer kilómetros con un coche eléctrico frente a uno de gasolina o diésel y calcula tu ahorro anual.",
"""<p class="lead">Calcula cuánto ahorrarías al año en energía cargando un coche eléctrico frente a repostar gasolina o diésel.</p>
<div class="card"><div class="row"><div><label for="ce">Consumo eléctrico (kWh/100 km)</label><input id="ce" inputmode="decimal" value="17"></div>
<div><label for="pe">Precio del kWh (€)</label><input id="pe" inputmode="decimal" value="0,12"></div>
<div><label for="cc">Consumo combustión (L/100 km)</label><input id="cc" inputmode="decimal" value="6,5"></div>
<div><label for="pc">Precio del litro (€)</label><input id="pc" inputmode="decimal" value="1,55"></div></div>
<label for="k">Kilómetros al año</label><input id="k" inputmode="numeric" value="15000"><button onclick="calc()">Comparar</button><div class="res" id="r"></div></div>
<p class="note">Pon el precio del kWh de tu tarifa. Cargando en casa por la noche con tarifa de discriminación horaria suele salir bastante más barato que en cargadores rápidos de carretera.</p>
<h2>Lo que no entra en la cuenta</h2><p>El ahorro en energía es solo una parte. El eléctrico suele tener menos mantenimiento (sin aceite, filtros ni embrague), bonificaciones en el impuesto de circulación en muchos municipios y ventajas en zonas de bajas emisiones. En contra, el precio de compra suele ser mayor y el seguro puede ser algo más caro.</p>""",
[("¿Cuánto cuesta cargar un coche eléctrico en casa?", "Multiplica la capacidad útil de la batería por el precio del kWh. Una batería de 60 kWh a 0,12 €/kWh cuesta unos 7,20 € de 0 a 100 %."),
 ("¿Cuántos km necesito hacer para que compense?", "Cuantos más km hagas, antes recuperas la diferencia de precio de compra. Divide esa diferencia entre el ahorro anual que te da esta calculadora para ver en cuántos años lo amortizas.")],
"Eléctrico vs gasolina: calculadora de ahorro",
"""function calc(){const k=v('k'),e=v('ce')/100*v('pe'),c=v('cc')/100*v('pc'),a=(c-e)*k;
show('r','Ahorro al año con el eléctrico:<b class="big">'+eur(a)+'</b>Eléctrico: '+nf(e,3)+' €/km ('+eur(e*k)+'/año) · Combustión: '+nf(c,3)+' €/km ('+eur(c*k)+'/año)<br>En 5 años: <b>'+eur(a*5)+'</b>');}"""))

P.append(("coste-anual-coche", "¿Cuánto cuesta mantener un coche al año? Calculadora | CocheCuentas",
"Suma seguro, impuesto de circulación, ITV, mantenimiento, neumáticos, combustible, aparcamiento y depreciación para saber el coste real de tu coche.",
"""<p class="lead">Rellena lo que pagas por cada concepto (puedes dejar en 0 lo que no aplique) y verás el coste real anual, mensual y por kilómetro.</p>
<div class="card"><div class="row">
<div><label for="a1">Seguro (€/año)</label><input id="a1" inputmode="decimal" value="450"></div>
<div><label for="a2">Impuesto de circulación (€/año)</label><input id="a2" inputmode="decimal" value="120"></div>
<div><label for="a3">ITV (€/año)</label><input id="a3" inputmode="decimal" value="45"></div>
<div><label for="a4">Revisiones y averías (€/año)</label><input id="a4" inputmode="decimal" value="400"></div>
<div><label for="a5">Neumáticos (€/año)</label><input id="a5" inputmode="decimal" value="150"></div>
<div><label for="a6">Combustible (€/año)</label><input id="a6" inputmode="decimal" value="1500"></div>
<div><label for="a7">Parking, peajes, lavados (€/año)</label><input id="a7" inputmode="decimal" value="300"></div>
<div><label for="a8">Cuota de financiación (€/mes)</label><input id="a8" inputmode="decimal" value="0"></div>
<div><label for="a9">Pérdida de valor (€/año)</label><input id="a9" inputmode="decimal" value="1500"></div>
<div><label for="k">Kilómetros al año</label><input id="k" inputmode="numeric" value="15000"></div></div>
<button onclick="calc()">Calcular coste real</button><div class="res" id="r"></div></div>
<p class="note">¿No sabes cuánto pierde de valor tu coche? Usa la <a href="depreciacion-coche.html">calculadora de depreciación</a>. ¿Y el combustible? Sácalo con la de <a href="coste-por-km.html">coste por km</a>. Y para el impuesto de tu ayuntamiento, usa la del <a href="impuesto-circulacion.html">impuesto de circulación</a>.</p>
<h2>El gasto que nadie cuenta: la depreciación</h2><p>Para muchos coches nuevos o seminuevos, la pérdida de valor es el mayor gasto del año, por encima del combustible. Un coche de 25.000 € puede perder entre 3.000 y 5.000 € solo en su primer año. Por eso comprar un seminuevo de 2-3 años suele ser la opción más eficiente.</p>""",
[("¿Cuánto cuesta de media mantener un coche en España?", "Depende mucho del coche y del uso, pero sumando todos los conceptos y la depreciación es habitual moverse entre 3.000 y 6.000 € al año para un turismo medio."),
 ("¿Sale más barato el renting?", "El renting incluye seguro, mantenimiento e impuestos en la cuota y elimina el riesgo de depreciación. Compara su cuota mensual con el coste mensual que te da esta calculadora.")],
None,
"""function calc(){let t=0;for(let i=1;i<=9;i++){if(i==8)continue;t+=v('a'+i);}t+=v('a8')*12;const k=v('k')||1;
show('r','Coste real al año:<b class="big">'+eur(t)+'</b>Al mes: <b>'+eur(t/12)+'</b> · Por km: <b>'+nf(t/k,3)+' €</b>');}"""))

P.append(("depreciacion-coche", "Depreciación de un coche: calcula cuánto valdrá dentro de X años | CocheCuentas",
"Calcula cuánto valdrá tu coche dentro de 1, 3 o 5 años y cuánto dinero pierde cada año. Hecha por un tasador profesional: útil para vender, comprar o elegir entre nuevo y seminuevo.",
"""<p class="lead">Calcula cuánto valdrá aproximadamente tu coche en el futuro y cuánto valor pierde cada año.</p>
<div class="card"><div class="row"><div><label for="pv">Precio de compra (€)</label><input id="pv" inputmode="decimal" value="25000"></div>
<div><label for="n">Años de propiedad</label><input id="n" inputmode="numeric" value="5"></div>
<div><label for="r1">Pérdida el primer año (%)</label><input id="r1" inputmode="decimal" value="20"></div>
<div><label for="r2">Pérdida años siguientes (% anual)</label><input id="r2" inputmode="decimal" value="12"></div></div>
<button onclick="calc()">Calcular</button><div class="res" id="r"></div></div>
<p class="note">Valores por defecto orientativos para un coche nuevo. Las marcas premium, los eléctricos y los modelos con poca demanda pueden depreciarse más rápido; los SUV y modelos muy demandados, más despacio. Si compras de segunda mano, usa un porcentaje de primer año más bajo (8-12 %).</p>
<h2>Qué hace que un coche pierda menos valor</h2><ul><li>Kilometraje bajo para su edad.</li><li>Libro de mantenimiento sellado en la marca.</li><li>Colores neutros (blanco, gris, negro).</li><li>Etiqueta ECO o 0 y motores con demanda.</li><li>Un solo propietario y sin golpes.</li></ul>""",
[("¿Cuánto pierde un coche nuevo al salir del concesionario?", "Como referencia general, entre un 15 % y un 25 % el primer año, y alrededor de un 40-50 % a los cinco años."),
 ("¿Cuándo es mejor vender el coche?", "La curva se suaviza a partir del tercer o cuarto año. Vender justo antes de grandes mantenimientos (distribución, neumáticos) o del cambio de etiqueta suele ser buena idea.")],
None,
"""function calc(){let x=v('pv');const n=Math.round(v('n')),a=v('r1')/100,b=v('r2')/100;let h='<table><tr><th>Año</th><th>Valor</th><th>Pierde</th></tr>';
for(let i=1;i<=n;i++){const p=x*(i==1?a:b);x-=p;h+='<tr><td>'+i+'</td><td>'+eur(x)+'</td><td>'+eur(p)+'</td></tr>';}
const tot=v('pv')-x;show('r','Valor estimado en '+n+' años:<b class="big">'+eur(x)+'</b>Pérdida total: <b>'+eur(tot)+'</b> ('+nf(tot/v('pv')*100,1)+' %) · '+eur(tot/Math.max(n,1))+'/año'+h+'</table>');}"""))

P.append(("coste-viaje-coche", "Calcular gasolina de un viaje: coste en coche y por persona | CocheCuentas",
"Calcula cuánto gastas en gasolina o diésel en un viaje en coche, con el precio medio de hoy del Ministerio, peajes e ida y vuelta, y cuánto paga cada ocupante.",
"""<p class="lead">Calcula el coste de tu viaje y cuánto tiene que poner cada uno.</p>
<div class="card"><div class="row"><div><label for="d">Distancia (km, solo ida)</label><input id="d" inputmode="decimal" value="530"></div>
<div><label for="iv">Trayecto</label><select id="iv"><option value="1">Solo ida</option><option value="2" selected>Ida y vuelta</option></select></div>
<div><label for="cb">Combustible</label><select id="cb" onchange="pz()"><option value="g95">Gasolina 95</option><option value="gA">Diésel (gasóleo A)</option><option value="glp">GLP (autogás)</option></select></div>
<div><label for="c">Consumo (L/100 km)</label><input id="c" inputmode="decimal" value="6"></div>
<div><label for="p">Precio del litro (€)</label><input id="p" inputmode="decimal" value="1,55"></div>
<div><label for="pe">Peajes y parking (€ total)</label><input id="pe" inputmode="decimal" value="0"></div>
<div><label for="o">Ocupantes</label><input id="o" inputmode="numeric" value="2"></div></div>
<button onclick="calc()">Calcular viaje</button><div class="res" id="r"></div></div>
<p class="note" id="pn">Precio orientativo. Mira el de tu zona en <a href="gasolineras-baratas.html">gasolineras más baratas cerca de ti</a>.</p>
<h2>Cómo se calcula el gasto de gasolina de un viaje</h2><p>Litros = kilómetros × consumo ÷ 100. Coste = litros × precio del litro + peajes y parking. Usa el consumo real de tu coche (el del ordenador de a bordo o el que calculas al llenar el depósito), no el homologado: en autopista a 120 km/h suele ser un 10-20 % mayor que la cifra oficial.</p>
<table><tr><th>Tipo de coche</th><th>Consumo real en autopista</th></tr><tr><td>Utilitario de gasolina</td><td>5,5 – 6,5 L/100 km</td></tr><tr><td>Compacto diésel</td><td>4,5 – 5,5 L/100 km</td></tr><tr><td>SUV de gasolina</td><td>6,5 – 8 L/100 km</td></tr><tr><td>Híbrido no enchufable</td><td>5 – 6 L/100 km</td></tr><tr><td>Furgoneta o monovolumen</td><td>7 – 9 L/100 km</td></tr></table>
<h2>Consejos para el viaje</h2><p>En autopista, bajar de 130 a 110 km/h puede reducir el consumo alrededor de un 15 %. Reposta antes de entrar en la autopista: las estaciones de servicio en ruta suelen ser más caras. Y si vais varios, compartir gastos hace el coche casi siempre más barato que el tren o el avión. Respeta los límites: una multa por velocidad puede costar más que el viaje entero (<a href="multa-exceso-velocidad.html">calcula cuánto te multarían</a>).</p>""",
[("¿Cómo se reparten los gastos de un viaje en coche?", "Lo habitual es sumar combustible, peajes y parking y dividirlo entre todos los ocupantes, conductor incluido."),
 ("¿Cuánta gasolina gasta un coche en 100 km?", "Un turismo de gasolina actual gasta entre 5,5 y 7 litros cada 100 km en carretera, y un diésel entre 4,5 y 6. Multiplica por el precio del litro: a 1,50 €/L, 100 km cuestan entre 8 y 10 €."),
 ("¿Cuánto cuesta ir de Madrid a Málaga en coche?", "Son unos 530 km. Con un consumo de 6 L/100 km y el litro a 1,55 €, sale por unos 49 € solo de ida en combustible.")],
None,
"""function calc(){const km=v('d')*v('iv'),l=km*v('c')/100,t=l*v('p')+v('pe'),o=Math.max(1,v('o'));
show('r','Coste total del viaje:<b class="big">'+eur(t)+'</b>Por persona: <b>'+eur(t/o)+'</b> · '+nf(km,0)+' km · '+nf(l,1)+' litros · '+eur(km>0?t/km*100:0)+' cada 100 km');}
let MED=null;function pz(){const k=document.getElementById('cb').value;if(MED&&MED[k]){document.getElementById('p').value=MED[k].toFixed(3).replace('.',',');}calc();}
fetch('carb/index.json').then(r=>r.json()).then(j=>{if(!j.medias)return;MED=j.medias;pz();document.getElementById('pn').innerHTML='Precio: media de las gasolineras de España según el Ministerio para la Transición Ecológica ('+(j.fecha||'').split(' ')[0]+'). Mira el de tu zona en <a href="gasolineras-baratas.html">gasolineras más baratas cerca de ti</a>.';}).catch(()=>{});"""))

exec(open("extra_motor.py").read())
build(S, P)
