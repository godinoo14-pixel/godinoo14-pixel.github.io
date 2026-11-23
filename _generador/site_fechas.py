from gen import build
S = dict(dir="calculadoradias", name="CalculadoraDías", logo="Calculadora<span>Días</span>", acc="#5f3dc4",
         base="https://calculadoradias.es/", domain="calculadoradias.es",
         tools=[("dias-entre-fechas", "Días entre dos fechas", "Días naturales, semanas y meses entre dos fechas.", "Entre fechas"),
                ("dias-habiles", "Calculadora de días hábiles", "Días laborables entre fechas, sin fines de semana ni festivos.", "Días hábiles"),
                ("sumar-dias", "Sumar o restar días a una fecha", "Fecha final de un plazo en días naturales o hábiles.", "Sumar días"),
                ("calcular-edad", "Calculadora de edad exacta", "Edad en años, meses y días, y días hasta tu cumpleaños.", ""),
                ("cuantos-dias-faltan", "¿Cuántos días faltan para…?", "Cuenta atrás para Navidad, verano o cualquier fecha.", ""),
                ("semana-del-ano", "¿En qué semana del año estamos?", "Número de semana ISO de cualquier fecha.", "")],
         home_title="CalculadoraDías | Calculadoras de fechas: días hábiles, días entre fechas, edad",
         home_desc="Calcula días hábiles, días entre dos fechas, plazos, tu edad exacta, cuenta atrás y la semana del año. Gratis y al momento.",
         home_h1="Calculadoras de fechas y plazos",
         home_intro='<p class="lead">Cuenta días naturales y hábiles, calcula plazos, tu edad exacta o cuántos días faltan para cualquier fecha. Todo funciona en tu navegador, sin registros.</p>',
         home_extra='<h2>Días naturales vs días hábiles</h2><p>Los <b>días naturales</b> son todos los del calendario. Los <b>días hábiles</b> excluyen sábados, domingos y festivos (en los procedimientos administrativos en España, los sábados no son hábiles desde la Ley 39/2015). Confundirlos es el error más común al calcular plazos de recursos, entregas o vacaciones.</p>')

DATEJS = """const pd=id=>{const s=document.getElementById(id).value;if(!s)return null;const [y,m,d]=s.split('-').map(Number);return new Date(y,m-1,d);};
const fmt=d=>d.toLocaleDateString('es-ES',{weekday:'long',day:'numeric',month:'long',year:'numeric'});
const iso=d=>d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');
const diff=(a,b)=>Math.round((Date.UTC(b.getFullYear(),b.getMonth(),b.getDate())-Date.UTC(a.getFullYear(),a.getMonth(),a.getDate()))/864e5);
function hol(){const t=(document.getElementById('f')||{value:''}).value;const s=new Set();t.split(/[\\s,;]+/).forEach(x=>{const m=x.match(/^(\\d{1,2})[\\/\\-](\\d{1,2})[\\/\\-](\\d{4})$/);if(m)s.add(m[3]+'-'+m[2].padStart(2,'0')+'-'+m[1].padStart(2,'0'));});return s;}
const today=new Date();document.querySelectorAll('input[type=date][data-today]').forEach(e=>e.value=iso(today));
"""
FEST = """<label for="f">Festivos a excluir (opcional, uno por línea, dd/mm/aaaa)</label><textarea id="f" rows="3" placeholder="06/12/2026&#10;08/12/2026&#10;25/12/2026"></textarea>"""

P = []
P.append(("dias-entre-fechas", "Calcular días entre dos fechas | CalculadoraDías",
"Calcula cuántos días, semanas y meses hay entre dos fechas. Incluye opción de contar el último día.",
"""<p class="lead">Elige dos fechas y te decimos cuántos días naturales hay entre ellas, en semanas y meses.</p>
<div class="card"><div class="row"><div><label for="a">Fecha inicial</label><input id="a" type="date" data-today></div>
<div><label for="b">Fecha final</label><input id="b" type="date" value="2026-12-31"></div></div>
<label class="chk"><input type="checkbox" id="inc"><span>Incluir el día final en la cuenta</span></label>
<button onclick="calc()">Calcular</button><div class="res" id="r"></div></div>
<h2>Cómo se cuentan los días</h2><p>Por defecto se cuenta la diferencia entre las dos fechas: del 1 al 3 de enero hay 2 días. Si marcas «incluir el día final», el resultado será 3. En contratos y reservas de hotel se suele contar como noches (sin incluir), mientras que en vacaciones y bajas laborales se suelen incluir ambos días.</p>""",
[("¿Cuántos días tiene un año?", "365 días, o 366 en los años bisiestos (2028 es el próximo)."),
 ("¿Cuenta el primer día?", "Esta calculadora cuenta la diferencia entre fechas. Marca «incluir el día final» si necesitas contar ambos extremos.")],
None, DATEJS + """function calc(){const a=pd('a'),b=pd('b');if(!a||!b)return;let n=Math.abs(diff(a,b))+(document.getElementById('inc').checked?1:0);
show('r','Entre las dos fechas hay:<b class="big">'+nf(n,0)+' días</b>'+nf(n/7,1)+' semanas · '+nf(n/30.4375,1)+' meses · '+nf(n*24,0)+' horas');}"""))

P.append(("dias-habiles", "Calculadora de días hábiles entre dos fechas | CalculadoraDías",
"Cuenta los días hábiles o laborables entre dos fechas excluyendo fines de semana y los festivos que tú indiques.",
"""<p class="lead">Calcula los días laborables entre dos fechas, ambas incluidas, quitando fines de semana y festivos.</p>
<div class="card"><div class="row"><div><label for="a">Desde</label><input id="a" type="date" data-today></div>
<div><label for="b">Hasta</label><input id="b" type="date" value="2026-12-31"></div></div>
<label for="m">Días no laborables</label><select id="m"><option value="2">Sábados y domingos</option><option value="1">Solo domingos</option></select>""" + FEST + """
<button onclick="calc()">Calcular días hábiles</button><div class="res" id="r"></div></div>
<p class="note">Añade los festivos nacionales, autonómicos y locales de tu zona: los publica cada año el BOE y el boletín de tu comunidad.</p>
<h2>Días hábiles en plazos administrativos</h2><p>Según la Ley 39/2015, cuando un plazo se fija en días se entienden hábiles, excluyendo sábados, domingos y festivos. Si el último día del plazo es inhábil, se pasa al siguiente hábil. Para plazos judiciales, además, agosto es inhábil salvo excepciones.</p>""",
[("¿El sábado es día hábil?", "En plazos administrativos, no. En el ámbito laboral depende del convenio: en comercio, por ejemplo, el sábado suele ser laborable."),
 ("¿Agosto es hábil?", "Para plazos administrativos sí. Para plazos procesales en los juzgados, agosto se considera inhábil salvo para actuaciones urgentes.")],
None, DATEJS + """function calc(){let a=pd('a'),b=pd('b');if(!a||!b)return;if(a>b)[a,b]=[b,a];const h=hol(),m=v('m');let n=0,w=0,f=0,t=0;
for(let d=new Date(a);d<=b;d.setDate(d.getDate()+1)){t++;const g=d.getDay();if(g==0||(m==2&&g==6)){w++;continue;}if(h.has(iso(d))){f++;continue;}n++;}
show('r','Días hábiles:<b class="big">'+n+'</b>Total días: '+t+' · Fines de semana: '+w+' · Festivos excluidos: '+f);}"""))

P.append(("sumar-dias", "Sumar o restar días a una fecha (naturales o hábiles) | CalculadoraDías",
"Calcula qué fecha será dentro de X días naturales o hábiles, o qué fecha fue hace X días. Ideal para calcular plazos.",
"""<p class="lead">Calcula la fecha de vencimiento de un plazo sumando o restando días naturales o hábiles.</p>
<div class="card"><div class="row"><div><label for="a">Fecha de inicio</label><input id="a" type="date" data-today></div>
<div><label for="n">Número de días</label><input id="n" inputmode="numeric" value="30"></div>
<div><label for="o">Operación</label><select id="o"><option value="1">Sumar</option><option value="-1">Restar</option></select></div>
<div><label for="t">Tipo de días</label><select id="t"><option value="n">Naturales</option><option value="h">Hábiles (lunes a viernes)</option></select></div></div>""" + FEST + """
<button onclick="calc()">Calcular fecha</button><div class="res" id="r"></div></div>
<h2>Cómo calcular un plazo</h2><p>Los plazos se empiezan a contar el día siguiente a la notificación o publicación. Por ejemplo, si te notifican el lunes y tienes 10 días hábiles, el primer día del plazo es el martes. Si el último día cae en festivo o fin de semana, el plazo se alarga al siguiente día hábil.</p>""",
[("¿Qué fecha será dentro de 30 días?", "Pon la fecha de hoy, 30 días y «sumar»: la calculadora te da el día exacto y el día de la semana."),
 ("¿Un plazo de un mes es lo mismo que 30 días?", "No. Los plazos en meses se cuentan de fecha a fecha (del 15 de enero al 15 de febrero), no como 30 días.")],
None, DATEJS + """function calc(){const a=pd('a');if(!a)return;let n=Math.round(v('n')),s=v('o'),d=new Date(a);
if(document.getElementById('t').value=='n'){d.setDate(d.getDate()+s*n);}else{const h=hol();let c=0;while(c<n){d.setDate(d.getDate()+s);const g=d.getDay();if(g==0||g==6||h.has(iso(d)))continue;c++;}}
show('r','Fecha resultante:<b class="big">'+fmt(d)+'</b>');}"""))

P.append(("calcular-edad", "Calculadora de edad exacta: años, meses y días | CalculadoraDías",
"Calcula tu edad exacta en años, meses y días a partir de tu fecha de nacimiento, y cuántos días faltan para tu próximo cumpleaños.",
"""<p class="lead">Introduce tu fecha de nacimiento y descubre tu edad exacta y cuánto queda para tu cumpleaños.</p>
<div class="card"><div class="row"><div><label for="a">Fecha de nacimiento</label><input id="a" type="date" value="2000-01-01"></div>
<div><label for="b">Calcular a fecha de</label><input id="b" type="date" data-today></div></div>
<button onclick="calc()">Calcular edad</button><div class="res" id="r"></div></div>
<h2>Curiosidades</h2><p>Si naciste un 29 de febrero, en los años no bisiestos legalmente cumples años el 1 de marzo en España. Y a los 10.000 días de vida tienes unos 27 años y 4 meses: buena excusa para una segunda fiesta.</p>""",
[("¿Cómo se calcula la edad exacta?", "Se restan los años completos cumplidos y luego los meses y días transcurridos desde el último cumpleaños."),
 ("¿Cuántos días he vivido?", "La calculadora te muestra también el total de días vividos hasta la fecha indicada.")],
None, DATEJS + """function calc(){const a=pd('a'),b=pd('b');if(!a||!b||a>b)return;let y=b.getFullYear()-a.getFullYear(),m=b.getMonth()-a.getMonth(),d=b.getDate()-a.getDate();
if(d<0){m--;d+=new Date(b.getFullYear(),b.getMonth(),0).getDate();}if(m<0){y--;m+=12;}
let nx=new Date(b.getFullYear(),a.getMonth(),a.getDate());if(nx<b)nx.setFullYear(b.getFullYear()+1);
show('r','Tienes:<b class="big">'+y+' años</b>'+y+' años, '+m+' meses y '+d+' días · '+nf(diff(a,b),0)+' días vividos<br>Faltan <b>'+diff(b,nx)+' días</b> para tu cumpleaños ('+fmt(nx)+')');}"""))

P.append(("cuantos-dias-faltan", "¿Cuántos días faltan para Navidad, verano o cualquier fecha? | CalculadoraDías",
"Cuenta atrás: cuántos días faltan para Navidad, Nochevieja, el verano o la fecha que quieras.",
"""<p class="lead">Elige un evento o una fecha y te decimos cuántos días, semanas y fines de semana faltan.</p>
<div class="card"><label for="e">Evento</label><select id="e" onchange="pre()"><option value="12-25">Navidad (25 de diciembre)</option><option value="12-31">Nochevieja (31 de diciembre)</option>
<option value="01-06">Reyes (6 de enero)</option><option value="06-21">Verano (21 de junio)</option><option value="08-01">1 de agosto</option><option value="x">Otra fecha…</option></select>
<label for="b">Fecha</label><input id="b" type="date"><button onclick="calc()">Ver cuenta atrás</button><div class="res" id="r"></div></div>
<h2>Planifica con tiempo</h2><p>Saber cuántos días faltan ayuda a organizar compras, ahorro y vacaciones. Por ejemplo, si quieres ahorrar 300 € para Navidad, divide esa cantidad entre las semanas que faltan y sabrás cuánto apartar cada semana.</p>""",
[("¿Cuántos días faltan para Navidad?", "Elige «Navidad» en el desplegable y verás la cuenta atrás actualizada a hoy."),
 ("¿Cuenta el día de hoy?", "No: se cuentan los días que faltan desde hoy hasta la fecha elegida.")],
None, DATEJS + """function pre(){const e=document.getElementById('e').value;if(e=='x')return;const [m,d]=e.split('-').map(Number);let t=new Date(today.getFullYear(),m-1,d);if(diff(today,t)<0)t.setFullYear(t.getFullYear()+1);document.getElementById('b').value=iso(t);}
function calc(){const b=pd('b');if(!b)return;const n=diff(today,b);let we=0;for(let d=new Date(today);d<b;d.setDate(d.getDate()+1))if(d.getDay()==6)we++;
show('r',(n>=0?'Faltan:':'Pasaron:')+'<b class="big">'+Math.abs(n)+' días</b>'+nf(Math.abs(n)/7,1)+' semanas · '+we+' fines de semana · '+fmt(b));}pre();calc();"""))

P.append(("semana-del-ano", "¿En qué semana del año estamos? Número de semana | CalculadoraDías",
"Consulta el número de semana del año (ISO 8601) de hoy o de cualquier fecha, con el lunes y domingo de esa semana.",
"""<p class="lead">Número de semana según la norma ISO 8601, la que se usa en España y en la mayoría de Europa.</p>
<div class="card"><label for="a">Fecha</label><input id="a" type="date" data-today><button onclick="calc()">Ver semana</button><div class="res" id="r"></div></div>
<h2>Cómo funciona la semana ISO</h2><p>Las semanas empiezan en lunes y la semana 1 es la que contiene el primer jueves del año. Por eso los primeros días de enero pueden pertenecer a la última semana del año anterior, y algunos años tienen 53 semanas.</p>""",
[("¿Cuántas semanas tiene un año?", "52 o 53 semanas ISO, según en qué día de la semana empiece el año."),
 ("¿Por qué Excel me da otro número?", "La función NUM.DE.SEMANA de Excel por defecto empieza en domingo. Usa ISO.NUM.DE.SEMANA para obtener el mismo resultado que aquí.")],
None, DATEJS + """function wk(d){const t=new Date(Date.UTC(d.getFullYear(),d.getMonth(),d.getDate()));const n=t.getUTCDay()||7;t.setUTCDate(t.getUTCDate()+4-n);const y=new Date(Date.UTC(t.getUTCFullYear(),0,1));return [Math.ceil(((t-y)/864e5+1)/7),t.getUTCFullYear()];}
function calc(){const a=pd('a');if(!a)return;const [w,y]=wk(a),g=a.getDay()||7,l=new Date(a);l.setDate(a.getDate()-g+1);const s=new Date(l);s.setDate(l.getDate()+6);
show('r','Semana:<b class="big">'+w+' de '+y+'</b>Del '+fmt(l)+' al '+fmt(s));}calc();"""))

exec(open("extra_fechas.py").read())
build(S, P)
