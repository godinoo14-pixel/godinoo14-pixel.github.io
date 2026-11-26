from gen import build
S = dict(dir="calculadoradias", name="CalculadoraDías", logo="Calculadora<span>Días</span>", acc="#5f3dc4",
         base="https://calculadoradias.es/", domain="calculadoradias.es",
         tools=[("dias-entre-fechas", "Días entre dos fechas", "Días naturales, semanas y meses entre dos fechas.", "Entre fechas"),
                ("dias-habiles", "Calculadora de días hábiles", "Días laborables entre fechas, sin fines de semana ni festivos.", "Días hábiles"),
                ("sumar-dias", "Sumar o restar días a una fecha", "Fecha final de un plazo en días naturales o hábiles.", "Sumar días"),
                ("calcular-edad", "Calculadora de edad exacta", "Edad en años, meses y días, y días hasta tu cumpleaños.", ""),
                ("cuantos-dias-faltan", "¿Cuántos días faltan para…?", "Cuenta atrás para Navidad, verano o cualquier fecha.", ""),
                ("semana-del-ano", "¿En qué semana del año estamos?", "Número de semana ISO de cualquier fecha.", "")],
         home_title="Calculadora de días hábiles, días entre fechas y plazos | CalculadoraDías",
         home_desc="Calcula días hábiles y naturales entre fechas, plazos, tu edad exacta y cuándo te jubilas. Con el calendario laboral 2027 oficial del BOE. Gratis y al momento.",
         home_h1="Calculadoras de fechas y plazos",
         home_intro='<p class="lead">Cuenta días naturales y hábiles, calcula plazos, tu edad exacta o cuántos días faltan para cualquier fecha. Todo funciona en tu navegador, sin registros.</p>',
         home_extra='<h2>Días naturales vs días hábiles</h2><p>Los <b>días naturales</b> son todos los del calendario. Los <b>días hábiles</b> excluyen sábados, domingos y festivos (en los procedimientos administrativos en España, los sábados no son hábiles desde la Ley 39/2015). Confundirlos es el error más común al calcular plazos de recursos, entregas o vacaciones.</p>')

DATEJS = """const pd=id=>{const s=document.getElementById(id).value;if(!s)return null;const [y,m,d]=s.split('-').map(Number);return new Date(y,m-1,d);};
const fmt=d=>d.toLocaleDateString('es-ES',{weekday:'long',day:'numeric',month:'long',year:'numeric'});
const iso=d=>d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');
const diff=(a,b)=>Math.round((Date.UTC(b.getFullYear(),b.getMonth(),b.getDate())-Date.UTC(a.getFullYear(),a.getMonth(),a.getDate()))/864e5);
const NAT=['2026-01-01','2026-01-06','2026-04-03','2026-05-01','2026-08-15','2026-10-12','2026-12-08','2026-12-25','2027-01-01','2027-01-06','2027-03-26','2027-05-01','2027-10-12','2027-11-01','2027-12-06','2027-12-08','2027-12-25'];
function hol(){const t=(document.getElementById('f')||{value:''}).value;const s=new Set();const nc=document.getElementById('nac');if(nc&&nc.checked)NAT.forEach(x=>s.add(x));t.split(/[\\s,;]+/).forEach(x=>{const m=x.match(/^(\\d{1,2})[\\/\\-](\\d{1,2})[\\/\\-](\\d{4})$/);if(m)s.add(m[3]+'-'+m[2].padStart(2,'0')+'-'+m[1].padStart(2,'0'));});return s;}
const today=new Date();document.querySelectorAll('input[type=date][data-today]').forEach(e=>e.value=iso(today));
setTimeout(()=>document.querySelectorAll('.card input,.card select,.card textarea').forEach(e=>e.addEventListener(e.tagName=='SELECT'||e.type=='checkbox'?'change':'input',()=>{if(typeof calc==='function')try{calc();}catch(x){}})),0);
"""
FEST = """<label class="chk"><input type="checkbox" id="nac" checked><span>Excluir los festivos nacionales de 2026 y 2027 (BOE)</span></label><label for="f">Otros festivos a excluir: autonómicos o locales (opcional, uno por línea, dd/mm/aaaa)</label><textarea id="f" rows="3" placeholder="07/12/2026&#10;15/05/2027"></textarea>"""

P = []
P.append(("dias-entre-fechas", "Días entre dos fechas: calculadora de días, semanas y meses | CalculadoraDías",
"Calcula al instante cuántos días hay entre dos fechas, y su equivalencia en semanas, meses y años. Con opción de incluir el último día. Gratis, sin registro y fiable en años bisiestos.",
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

P.append(("dias-habiles", "Calculadora de días hábiles y laborables entre dos fechas | CalculadoraDías",
"Cuenta los días hábiles entre dos fechas sin sábados, domingos ni festivos: para plazos administrativos (Ley 39/2015), días laborables de un mes o entregas. Añade tus festivos de 2026 o 2027.",
"""<p class="lead">Calcula los días laborables entre dos fechas, ambas incluidas, quitando fines de semana y festivos.</p>
<div class="card"><div class="row"><div><label for="a">Desde</label><input id="a" type="date" data-today></div>
<div><label for="b">Hasta</label><input id="b" type="date" value="2026-12-31"></div></div>
<label for="m">Días no laborables</label><select id="m"><option value="2">Sábados y domingos</option><option value="1">Solo domingos</option></select>""" + FEST + """
<button onclick="calc()">Calcular días hábiles</button><div class="res" id="r"></div></div>
<p class="note">Los festivos nacionales de 2026 y 2027 ya se descuentan solos. Añade los autonómicos y locales de tu zona: los publica cada año el BOE y el boletín de tu comunidad.</p>
<h2>Días hábiles en plazos administrativos</h2><p>Según la Ley 39/2015, cuando un plazo se fija en días se entienden hábiles, excluyendo sábados, domingos y festivos. Si el último día del plazo es inhábil, se pasa al siguiente hábil. Para plazos judiciales, además, agosto es inhábil salvo excepciones.</p>
<p><b>Ejemplo:</b> del 1 al 31 de diciembre de 2026 hay 23 días de lunes a viernes. Si quitas los festivos nacionales del 8 (Inmaculada) y el 25 (Navidad), quedan <b>21 días hábiles</b>; en tu comunidad pueden ser menos si hay algún festivo autonómico o local.</p>
<p>¿Necesitas saber en qué fecha vence un plazo? Usa <a href="sumar-dias.html">sumar días hábiles a una fecha</a>. Para todo 2027, abre el <a href="calendario-laboral-2027.html">calendario laboral 2027 de tu comunidad</a>: desde ahí puedes traer aquí sus festivos con un clic.</p>""",
[("¿El sábado es día hábil?", "En plazos administrativos, no. En el ámbito laboral depende del convenio: en comercio, por ejemplo, el sábado suele ser laborable."),
 ("¿Agosto es hábil?", "Para plazos administrativos sí. Para plazos procesales en los juzgados, agosto se considera inhábil salvo para actuaciones urgentes."),
 ("¿Cuántos días hábiles tiene diciembre de 2026?", "Tiene 23 días de lunes a viernes. Quitando los festivos nacionales del 8 y el 25 de diciembre, quedan 21 días hábiles, menos si en tu comunidad o municipio hay otro festivo ese mes."),
 ("¿Cómo se cuenta un plazo de 10 días hábiles?", "Se empieza a contar el día siguiente a la notificación y se saltan sábados, domingos y festivos. Si el último día cae en inhábil, el plazo termina el siguiente día hábil.")],
None, DATEJS + """try{const q=new URLSearchParams(location.search).get('f');if(q){document.getElementById('f').value=q.split(',').join('\\n');document.getElementById('a').value='2027-01-01';document.getElementById('b').value='2027-12-31';}}catch(e){}
function calc(){let a=pd('a'),b=pd('b');if(!a||!b)return;if(a>b)[a,b]=[b,a];const h=hol(),m=v('m');let n=0,w=0,f=0,t=0;
for(let d=new Date(a);d<=b;d.setDate(d.getDate()+1)){t++;const g=d.getDay();if(g==0||(m==2&&g==6)){w++;continue;}if(h.has(iso(d))){f++;continue;}n++;}
show('r','Días hábiles:<b class="big">'+n+'</b>Total días: '+t+' · '+(m==2?'Sábados y domingos':'Domingos')+': '+w+' · Festivos entre semana excluidos: '+f+(document.getElementById('nac').checked?'<br><span class="note">Incluye los festivos nacionales. Si en tu comunidad o municipio hay otros, añádelos abajo o tráelos del calendario laboral 2027.</span>':''));}"""))

P.append(("sumar-dias", "Sumar días a una fecha: naturales o hábiles, para plazos | CalculadoraDías",
"Calcula qué fecha será dentro de X días naturales o hábiles, o qué fecha fue hace X días. Ideal para plazos de contratos, devoluciones, recursos y entregas.",
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

P.append(("calcular-edad", "Calcular edad exacta: años, meses, días y días vividos | CalculadoraDías",
"Calcula tu edad exacta en años, meses y días, cuántos días, semanas y horas has vivido, qué día de la semana es tu próximo cumpleaños y cuándo cumples 10.000 días.",
"""<p class="lead">Pon una fecha de nacimiento y te decimos la edad exacta, cuántos días has vivido y cuánto falta para el próximo cumpleaños. Cambia la segunda fecha para saber qué edad tendrás (o tenías) un día concreto.</p>
<div class="card"><div class="row"><div><label for="a">Fecha de nacimiento</label><input id="a" type="date" value="1990-06-15"></div>
<div><label for="b">Calcular la edad a fecha de</label><input id="b" type="date" data-today></div></div>
<div class="res" id="r" aria-live="polite"></div></div>
<h2>Cómo se calcula la edad exacta</h2><p>Primero se cuentan los <b>años completos</b>: los que han pasado desde el nacimiento hasta el último cumpleaños. Luego, los <b>meses completos</b> desde ese cumpleaños y, por último, los <b>días</b> que sobran. Si el día del mes actual es menor que el de nacimiento, se «pide prestado» un mes y se suman los días que tenía el mes anterior.</p>
<p><b>Ejemplo:</b> alguien nacido el 15 de junio de 1990 tiene, el 25 de noviembre de 2026, 36 años, 5 meses y 10 días. Ha vivido 13.312 días (unas 1901 semanas) y celebrará su 37 cumpleaños el martes 15 de junio de 2027.</p>
<h2>Cumpleaños el 29 de febrero</h2><p>Si naciste en un año bisiesto el 29 de febrero, los demás años la calculadora toma como cumpleaños el 1 de marzo. Para los plazos legales que se cuentan por años, el artículo 5 del Código Civil dice que, si el mes de vencimiento no tiene el día equivalente, el plazo termina el último día de ese mes: el 28 de febrero.</p>
<h2>Para qué sirve saber la edad exacta</h2><ul><li><b>Trámites y requisitos:</b> becas, oposiciones, carné de conducir o descuentos que exigen tener una edad cumplida en una fecha concreta. Pon esa fecha en el segundo campo.</li><li><b>Jubilación:</b> la edad se cuenta en años y meses. Calcula la tuya con la <a href="calculadora-jubilacion.html">calculadora de jubilación</a>.</li><li><b>Bebés:</b> en los primeros meses la edad se cuenta en semanas y meses; aquí tienes ambas.</li></ul>
<p>¿Quieres saber cuántos días hay entre dos fechas cualquiera? Usa la calculadora de <a href="dias-entre-fechas.html">días entre fechas</a>, o mira <a href="que-dia-de-la-semana.html">qué día de la semana</a> naciste.</p>""",
[("¿Cómo se calcula la edad exacta?", "Se cuentan los años completos hasta el último cumpleaños, después los meses completos desde ese cumpleaños y, por último, los días restantes."),
 ("¿Cuántos días he vivido?", "Pon tu fecha de nacimiento y la calculadora te muestra el total de días vividos hasta hoy o hasta la fecha que elijas, además de las semanas y las horas aproximadas."),
 ("¿Cuándo cumplo 10.000 días?", "A los 27 años, 4 meses y unos 18 días, según los bisiestos que te toquen. La calculadora te dice la fecha exacta y el día de la semana."),
 ("¿Cuándo cumple años alguien nacido el 29 de febrero?", "En los años no bisiestos se suele celebrar el 28 de febrero o el 1 de marzo. Para plazos legales por años, el Código Civil fija el último día del mes: el 28 de febrero.")],
"Calculadora de edad exacta", DATEJS + """function calc(){const a=pd('a'),b=pd('b');if(!a||!b){show('r','Escribe las dos fechas.');return;}if(a>b){show('r','La fecha de nacimiento tiene que ser anterior a la segunda fecha.');return;}
let y=b.getFullYear()-a.getFullYear(),m=b.getMonth()-a.getMonth(),d=b.getDate()-a.getDate();
if(d<0){m--;d+=new Date(b.getFullYear(),b.getMonth(),0).getDate();}if(m<0){y--;m+=12;}
let nx=new Date(b.getFullYear(),a.getMonth(),a.getDate());if(nx<b)nx=new Date(b.getFullYear()+1,a.getMonth(),a.getDate());
const dv=diff(a,b),fn=diff(b,nx),na=nx.getFullYear()-a.getFullYear();
let h='Edad:<b class="big">'+y+' años</b>'+y+' años, '+m+' '+(m==1?'mes':'meses')+' y '+d+' '+(d==1?'día':'días')+' · '+nf(y*12+m,0)+' meses en total';
h+='<br>Días vividos: <b>'+nf(dv,0)+'</b> · '+nf(Math.floor(dv/7),0)+' semanas · unas '+nf(dv*24,0)+' horas';
h+='<br>'+(fn==0?'<b>¡Hoy cumple '+y+' años!</b>':'Faltan <b>'+fn+' días</b> para cumplir '+na+' años: '+fmt(nx));
const hi=[5000,10000,15000,20000,25000,30000].find(x=>x>dv);if(hi){const t=new Date(a.getFullYear(),a.getMonth(),a.getDate()+hi);h+='<br>Cumplirá <b>'+nf(hi,0)+' días</b> el '+fmt(t)+'.';}
h+='<br>Nació en '+fmt(a).split(',')[0]+'.';
show('r',h);}
document.querySelectorAll('.card input').forEach(e=>e.addEventListener('change',()=>calc()));
calc();"""))

P.append(("cuantos-dias-faltan", "¿Cuántos días faltan para Navidad? Cuenta atrás en directo | CalculadoraDías",
"Cuenta atrás en directo: cuántos días, horas y minutos faltan para Navidad, Nochebuena, la Lotería, Nochevieja, Reyes, Semana Santa, el verano o la fecha que quieras.",
"""<p class="lead">Elige un evento o cualquier fecha y verás la cuenta atrás en directo: días, horas, minutos, semanas y fines de semana que faltan.</p>
<div class="card"><label for="e">Evento</label><select id="e" onchange="pre()"><option value="12-25">Navidad (25 de diciembre)</option><option value="12-24">Nochebuena (24 de diciembre)</option><option value="12-22">Sorteo de la Lotería de Navidad (22 de diciembre)</option><option value="12-31">Nochevieja (31 de diciembre)</option>
<option value="01-06">Reyes (6 de enero)</option><option value="bf">Black Friday</option><option value="02-14">San Valentín (14 de febrero)</option><option value="ss">Semana Santa (Jueves Santo)</option><option value="06-21">Verano (21 de junio)</option><option value="08-01">1 de agosto</option><option value="x">Otra fecha…</option></select>
<label for="b">Fecha</label><input id="b" type="date" onchange="document.getElementById('e').value='x';calc()"><button onclick="calc()">Ver cuenta atrás</button><div class="res" id="r" aria-live="off"></div></div>
<h2>Próximas fechas señaladas</h2><table id="tb"></table>
<h2>Cómo contamos los días</h2><p>Contamos los días naturales completos desde hoy hasta la fecha elegida, sin incluir el día de hoy: si hoy es 24 de noviembre, a Navidad le faltan 31 días. Las horas y minutos se cuentan hasta las 00:00 del día del evento, en la hora de tu dispositivo. Los fines de semana son los sábados que quedan por delante. La Semana Santa y el Black Friday cambian cada año: la Semana Santa depende de la primera luna llena de primavera (el Domingo de Resurrección cae entre el 22 de marzo y el 25 de abril) y el Black Friday es el viernes siguiente al cuarto jueves de noviembre.</p>
<p><b>Ejemplo práctico:</b> si quieres ahorrar 300 € para los regalos de Navidad y faltan 4 semanas, tendrás que apartar 75 € cada semana. Si necesitas contar solo días laborables (por ejemplo, para un plazo o para saber cuántos días de trabajo quedan antes de vacaciones), usa la calculadora de <a href="dias-habiles.html">días hábiles</a>. Si juegas a la Lotería, mira <a href="premio-loteria-navidad.html">cuánto te quedaría del premio tras Hacienda</a> y hasta cuándo puedes cobrarlo; y para los festivos y puentes del año que viene, el <a href="calendario-laboral-2027.html">calendario laboral 2027</a>.</p>""",
[("¿Cuántos días faltan para Navidad?", "Depende del día en que lo consultes: la calculadora lo muestra al abrirla, en días, horas y minutos hasta el 25 de diciembre. Desde el 1 de diciembre faltan 24 días, y desde el 24 de noviembre, 31."),
 ("¿Cuándo es la Semana Santa de 2027?", "En 2027 el Jueves Santo es el 25 de marzo, el Viernes Santo el 26 y el Domingo de Resurrección el 28 de marzo. El Lunes de Pascua (29 de marzo) es festivo en algunas comunidades."),
 ("¿Cuenta el día de hoy?", "No: se cuentan los días que faltan desde hoy hasta la fecha elegida. Si la fecha es mañana, falta 1 día."),
 ("¿Cuándo es el sorteo de la Lotería de Navidad?", "Se celebra cada año el 22 de diciembre por la mañana. Elige «Sorteo de la Lotería de Navidad» en el desplegable para ver cuánto falta, y si te toca, calcula con nuestra calculadora del premio de la Lotería cuánto se queda Hacienda.")],
None, DATEJS + """function easter(y){const a=y%19,b=Math.floor(y/100),c=y%100,d=Math.floor(b/4),e=b%4,f=Math.floor((b+8)/25),g=Math.floor((b-f+1)/3),h=(19*a+b-d-g+15)%30,i=Math.floor(c/4),k=c%4,l=(32+2*e+2*i-h-k)%7,m=Math.floor((a+11*h+22*l)/451),n=Math.floor((h+l-7*m+114)/31),p=(h+l-7*m+114)%31+1;return new Date(y,n-1,p);}
function evd(e,y){if(e=='ss'){const t=easter(y);t.setDate(t.getDate()-3);return t;}if(e=='bf'){const t=new Date(y,10,1);const th=(4-t.getDay()+7)%7+1+21;return new Date(y,10,th+1);}const [m,d]=e.split('-').map(Number);return new Date(y,m-1,d);}
function next(e){let t=evd(e,today.getFullYear());if(diff(today,t)<0)t=evd(e,today.getFullYear()+1);return t;}
function pre(){const e=document.getElementById('e').value;if(e=='x')return;document.getElementById('b').value=iso(next(e));calc();}
let TM=null;function calc(){const b=pd('b');if(!b)return;const n=diff(today,b);let we=0;for(let d=new Date(today);d<b;d.setDate(d.getDate()+1))if(d.getDay()==6)we++;
const nm=document.getElementById('e'),lb=nm.value=='x'?fmt(b):nm.options[nm.selectedIndex].text.replace(/ \\(.*\\)/,'');
const tick=()=>{const ms=b-new Date();if(ms<=0||n<0)return '';const s=Math.floor(ms/1000);return '<br>Cuenta atrás: <b>'+Math.floor(s/86400)+' d '+String(Math.floor(s%86400/3600)).padStart(2,'0')+' h '+String(Math.floor(s%3600/60)).padStart(2,'0')+' min '+String(s%60).padStart(2,'0')+' s</b>';};
const base=(n>0?'Faltan para '+lb+':':n==0?'¡Es hoy!':'Pasaron:')+'<b class="big">'+Math.abs(n)+' días</b>'+nf(Math.abs(n)/7,1)+' semanas · '+we+' fines de semana · '+fmt(b);
show('r',base+tick());clearInterval(TM);TM=setInterval(()=>{const r=document.getElementById('r');r.innerHTML=base+tick();},1000);}
const EV=[['12-22','Lotería de Navidad'],['12-24','Nochebuena'],['12-25','Navidad'],['12-31','Nochevieja'],['01-06','Reyes'],['02-14','San Valentín'],['ss','Jueves Santo'],['06-21','Verano'],['bf','Black Friday']].map(x=>[x[1],next(x[0])]).sort((a,b)=>a[1]-b[1]);
document.getElementById('tb').innerHTML='<tr><th>Fecha</th><th>Día</th><th>Faltan</th></tr>'+EV.map(x=>'<tr><td>'+x[0]+'</td><td>'+x[1].toLocaleDateString('es-ES',{weekday:'short',day:'numeric',month:'long',year:'numeric'})+'</td><td><b>'+diff(today,x[1])+' días</b></td></tr>').join('');
pre();"""))

P.append(("semana-del-ano", "¿En qué semana estamos? Número de semana del año hoy (ISO) | CalculadoraDías",
"Mira en qué número de semana del año estamos hoy (norma ISO 8601, la que usan los calendarios en España) o en cualquier otra fecha, con el lunes y el domingo de esa semana.",
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
