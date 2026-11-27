import json
from gen import amz, ext
S['aff'] = {
    "index": amz("agenda 2027", "Agendas 2027") + amz("calendario pared 2027", "Calendarios 2027"),
    "dias-habiles": amz("agenda 2027 semana vista", "Agendas semana vista") + amz("planificador mensual", "Planificadores"),
    "cuantos-dias-faltan": amz("calendario adviento", "Calendarios de adviento") + amz("ideas regalo", "Ideas de regalo"),
    "calcular-edad": amz("ideas regalo cumpleaños", "Ideas de regalo de cumpleaños"),
    "calculadora-vacaciones": amz("maleta cabina", "Maletas de cabina") + amz("organizador maleta", "Organizadores de viaje"),
    "calculadora-horas": amz("reloj fichar", "Relojes de fichaje") + amz("temporizador cocina digital", "Temporizadores"),
}
S['tools'] += [("calculadora-vacaciones", "Calculadora de días de vacaciones", "Cuántos días de vacaciones te corresponden según lo trabajado.", ""),
               ("calculadora-horas", "Calculadora de horas trabajadas", "Horas entre entrada y salida, descansos y total semanal.", ""),
               ("que-dia-de-la-semana", "¿Qué día de la semana fue o será?", "El día de la semana de cualquier fecha.", "")]

P.append(("calculadora-vacaciones", "Calculadora de vacaciones 2026 y 2027: días que me corresponden | CalculadoraDías",
"Calcula los días de vacaciones que te corresponden según lo trabajado (30 naturales o 22 laborables), cuántos te quedan antes del 31 de diciembre y cuánto valen en el finiquito.",
"""<p class="lead">Pon desde cuándo trabajas este año y los días que ya has disfrutado. Te decimos las vacaciones generadas, las que te quedan y lo que valen si dejas la empresa.</p>
<div class="card"><div class="row"><div><label for="a">Fecha de inicio (alta o 1 de enero)</label><input id="a" type="date" value="2026-01-01"></div>
<div><label for="b">Fecha de fin (31 de diciembre, baja o hoy)</label><input id="b" type="date" value="2026-12-31"></div>
<div><label for="d">Días de vacaciones al año</label><select id="d"><option value="30">30 días naturales</option><option value="22">22 días laborables</option><option value="x">Otro (convenio)</option></select></div>
<div><label for="dx">Días según convenio</label><input id="dx" inputmode="numeric" value="23"></div>
<div><label for="u">Días ya disfrutados</label><input id="u" inputmode="numeric" value="0"></div>
<div><label for="sm">Salario bruto mensual (opcional, para valorar los días)</label><input id="sm" inputmode="decimal" value=""></div></div>
<button onclick="calc()">Calcular vacaciones</button><div class="res" id="r" aria-live="polite"></div></div>
<p class="note">El Estatuto de los Trabajadores fija un mínimo de 30 días naturales al año; tu convenio puede mejorarlo. Si dejas la empresa, los días generados y no disfrutados se pagan en el finiquito.</p>
<h2>Cómo se calculan</h2><p>Las vacaciones se generan de forma proporcional al tiempo trabajado: <b>días trabajados ÷ 365 × días anuales</b>. Si entraste el 1 de julio con 30 días naturales al año, a 31 de diciembre habrás generado unos 15 días (184 ÷ 365 × 30 = 15,1).</p>
<table><tr><th>Alta en 2026</th><th>30 naturales</th><th>22 laborables</th></tr>
<tr><td>1 de enero</td><td>30</td><td>22</td></tr><tr><td>1 de abril</td><td>22,6</td><td>16,6</td></tr><tr><td>1 de julio</td><td>15,1</td><td>11,1</td></tr><tr><td>1 de septiembre</td><td>10</td><td>7,4</td></tr><tr><td>1 de noviembre</td><td>5</td><td>3,7</td></tr></table>
<h2>¿Se pierden las vacaciones que no gastes antes del 31 de diciembre?</h2><p>Por regla general, las vacaciones son del año natural y no se acumulan al siguiente: si tu convenio no dice otra cosa, lo normal es disfrutarlas antes de que acabe el año. Hay excepciones importantes. Si no pudiste cogerlas por una <b>incapacidad temporal</b>, embarazo, parto o lactancia, tienes derecho a disfrutarlas después, aunque haya terminado el año (en caso de baja por enfermedad, hasta 18 meses después del final del año en que se generaron). Y la empresa no puede alegar que se han perdido si no te dio la oportunidad real de disfrutarlas. El calendario de vacaciones debes conocerlo al menos dos meses antes del comienzo del disfrute (artículo 38 del Estatuto).</p>
<p>Para planificar los días que te quedan, mira los <a href="calendario-laboral-2027.html">puentes del calendario laboral 2027</a> y cuenta los <a href="dias-habiles.html">días laborables entre dos fechas</a>. Si te vas de la empresa, calcula tu <a href="calcular-finiquito.html">finiquito</a> completo con las vacaciones y las pagas extra.</p>
<p>¿Vas a tener un bebé? Las vacaciones se pueden disfrutar justo después del <a href="permiso-nacimiento.html">permiso por nacimiento</a> aunque haya terminado el año natural.</p>""",
[("¿Cuántos días de vacaciones me corresponden al año?", "Como mínimo 30 días naturales (equivalen aproximadamente a 22 laborables), salvo que tu convenio establezca más."),
 ("¿Las vacaciones no disfrutadas se pagan?", "Solo cuando termina la relación laboral: se incluyen en el finiquito. Mientras sigues en la empresa no pueden sustituirse por dinero."),
 ("¿Puedo pasar las vacaciones que me quedan al año que viene?", "Solo si lo permite tu convenio o lo acuerdas con la empresa, o si no pudiste disfrutarlas por una baja médica, por embarazo, parto o lactancia. En esos casos se pueden coger después del 31 de diciembre."),
 ("¿Cuántos días de vacaciones me corresponden si entré a mitad de año?", "La parte proporcional: días trabajados ÷ 365 × 30. Entrando el 1 de julio te corresponden unos 15 días naturales hasta el 31 de diciembre.")],
None, DATEJS + """function calc(){const a=pd('a'),b=pd('b');if(!a||!b||b<a){show('r','Revisa las fechas.');return;}const s=document.getElementById('d').value,an=s=='x'?v('dx'):parseFloat(s);const t=diff(a,b)+1,g=t/365*an,p=g-v('u'),sm=v('sm');
const ud=s=='30'?'naturales':s=='22'?'laborables':'de convenio';
let h='Vacaciones generadas:<b class="big">'+nf(g,1)+' días</b>Días trabajados: '+t+' · '+(p>=0?'Pendientes de disfrutar: <b>'+nf(p,1)+'</b>':'Has disfrutado <b>'+nf(-p,1)+' días de más</b>')+' ('+ud+')';
if(sm>0&&p>0){const nat=s=='30'?p:p*30/an;h+='<br>Si dejas la empresa, en el finiquito valen unos <b>'+eur(nat*sm/30)+'</b> brutos ('+nf(nat,1)+' días naturales × '+eur(sm/30)+').';}
const fin=new Date(b.getFullYear(),11,31),rest=diff(today,fin);if(p>0&&rest>=0&&rest<62&&b.getFullYear()==today.getFullYear())h+='<br>Quedan <b>'+rest+' días</b> para el 31 de diciembre: revisa si tu convenio permite pasarlas al año que viene.';
show('r',h);}"""))

P.append(("calculadora-horas", "Calculadora de horas trabajadas: jornada, descansos y horas extra | CalculadoraDías",
"Calcula las horas trabajadas entre la entrada y la salida, restando descansos, con turno partido o de noche: total del día, la semana y el mes, horas extra sobre 40 h y paso a horas decimales.",
"""<p class="lead">Pon tu hora de entrada, de salida y el descanso, y te sumamos las horas del día, la semana y el mes. Si haces jornada partida, añade el segundo tramo.</p>
<div class="card"><div class="row"><div><label for="e">Entrada</label><input id="e" type="time" value="09:00"></div><div><label for="s">Salida</label><input id="s" type="time" value="18:00"></div>
<div><label for="e2">Entrada de tarde (jornada partida, opcional)</label><input id="e2" type="time" value=""></div><div><label for="s2">Salida de tarde (opcional)</label><input id="s2" type="time" value=""></div>
<div><label for="p">Descanso no retribuido (minutos)</label><input id="p" inputmode="numeric" value="60"></div><div><label for="dd">Días trabajados a la semana</label><input id="dd" inputmode="decimal" value="5"></div>
<div><label for="jc">Jornada de tu contrato (horas a la semana)</label><input id="jc" inputmode="decimal" value="40"></div>
<div><label for="ph">Precio por hora (€, opcional)</label><input id="ph" inputmode="decimal" value="0"></div></div>
<button onclick="calc()">Calcular horas</button><div class="res" id="r" aria-live="polite"></div></div>
<p class="note">Si sales después de medianoche (turno de noche) también funciona: se suma el día siguiente. El mes se calcula con 52 semanas ÷ 12 = 4,33 semanas.</p>
<h2>Cómo se calculan las horas trabajadas</h2><p><b>Horas del día = salida − entrada − descanso</b>. Si la salida es anterior a la entrada, el turno termina al día siguiente y se suman 24 horas. Para la semana se multiplica por los días trabajados, y para el mes por 4,33 semanas. Ejemplo: de 9:00 a 18:00 con una hora para comer son 8 horas al día, 40 a la semana y unas 173 al mes.</p>
<h2>Pasar minutos a horas decimales</h2><p>Las nóminas y muchas apps de fichaje usan horas decimales. Divide los minutos entre 60:</p>
<table><tr><th>Minutos</th><th>Horas decimales</th></tr><tr><td>15 min</td><td>0,25 h</td></tr><tr><td>20 min</td><td>0,33 h</td></tr><tr><td>30 min</td><td>0,5 h</td></tr><tr><td>45 min</td><td>0,75 h</td></tr><tr><td>7 h 50 min</td><td>7,83 h</td></tr></table>
<h2>Jornada máxima y horas extra en España</h2><p>Según el Estatuto de los Trabajadores, la jornada ordinaria máxima es de <b>40 horas semanales</b> de trabajo efectivo de promedio en cómputo anual, con un máximo de 9 horas ordinarias al día salvo que el convenio las distribuya de otra forma, y al menos <b>12 horas de descanso</b> entre el final de una jornada y el inicio de la siguiente. Las horas que superan tu jornada son <b>horas extraordinarias</b>: se pagan (en la cuantía que fije el convenio, nunca por debajo de la hora ordinaria) o se compensan con descanso en los cuatro meses siguientes, y no pueden pasar de 80 al año. Si trabajas a tiempo parcial, las horas por encima de tu contrato son horas complementarias, que deben estar pactadas por escrito.</p>
<p>Desde 2019 todas las empresas deben llevar un <b>registro diario de jornada</b> con la hora de inicio y fin de cada trabajador y guardarlo cuatro años: si te salen más horas de las de tu contrato, ese registro es tu prueba.</p>
<p>¿Necesitas contar días en vez de horas? Usa la <a href="dias-entre-fechas.html">calculadora de días entre fechas</a> o la de <a href="dias-habiles.html">días hábiles</a>. Si vas a dejar el trabajo, calcula tu <a href="calcular-finiquito.html">finiquito</a>.</p>""",
[("¿Cómo paso minutos a horas decimales?", "Divide los minutos entre 60: 7 horas y 45 minutos son 7,75 horas; 30 minutos son 0,5 horas."),
 ("¿El descanso del bocadillo cuenta como tiempo trabajado?", "Solo si así lo establece tu convenio o contrato. Por ley, en jornadas continuadas de más de 6 horas hay derecho a una pausa mínima de 15 minutos (30 minutos para menores de 18 años con más de 4 horas y media)."),
 ("¿Cuántas horas al mes son 40 horas semanales?", "Unas 173 horas: 40 × 52 semanas ÷ 12 meses = 173,3 horas al mes. Con 37,5 horas semanales salen unas 162,5 al mes."),
 ("¿Cuántas horas extra puedo hacer al año?", "Como máximo 80 horas extraordinarias al año. No cuentan en ese límite las que se compensan con descanso en los cuatro meses siguientes ni las hechas para prevenir o reparar daños urgentes.")],
None, """function mn(id){const x=document.getElementById(id).value;if(!x)return null;const [h,m]=x.split(':').map(Number);return h*60+m;}
function hm(x){x=Math.round(x);return Math.floor(x/60)+' h '+String(x%60).padStart(2,'0')+' min';}
function tr(a,b){const e=mn(a),s=mn(b);if(e===null||s===null)return 0;let d=s-e;if(d<0)d+=1440;return d;}
function calc(){let d=tr('e','s')+tr('e2','s2')-v('p');d=Math.max(0,d);const w=d*v('dd'),m=w*52/12,ph=v('ph'),jc=v('jc');
let h='Horas al día:<b class="big">'+hm(d)+'</b>('+nf(d/60,2)+' h decimales) · Semana: <b>'+hm(w)+'</b> · Mes: <b>'+nf(m/60,1)+' h</b>';
if(jc>0){const x=w/60-jc;if(x>0.01)h+='<br>Superas tu jornada en <b>'+nf(x,2)+' h a la semana</b> (unas '+nf(x*52/12,1)+' h al mes): son horas extra o complementarias.';else if(x<-0.01)h+='<br>Te quedan '+nf(-x,2)+' h a la semana por debajo de tu jornada de '+nf(jc,1)+' h.';else h+='<br>Coincide con tu jornada de '+nf(jc,1)+' h semanales.';}
if(d>540)h+='<br>Más de 9 horas al día: solo es posible si tu convenio distribuye así la jornada.';
if(ph>0)h+='<br>Ingresos: '+eur(d/60*ph)+'/día · '+eur(w/60*ph)+'/semana · '+eur(m/60*ph)+'/mes';
show('r',h);}
document.querySelectorAll('.card input').forEach(x=>x.addEventListener('input',()=>calc()));"""))

P.append(("que-dia-de-la-semana", "¿Qué día de la semana cae? Cualquier fecha, Navidad y Reyes 2027 | CalculadoraDías",
"Descubre qué día de la semana cae cualquier fecha: Nochebuena 2026 es jueves, Reyes 2027 miércoles. Tu cumpleaños, una boda o el día en que naciste, y cómo cae los próximos años.",
"""<p class="lead">Elige una fecha y te decimos qué día de la semana fue o será, y cómo cae en los próximos años.</p>
<div class="card"><label for="a">Fecha</label><input id="a" type="date" value="2027-12-25"><button onclick="calc()">Ver día</button><div class="res" id="r"></div></div>
<h2>¿Por qué cada año cambia el día?</h2><p>Un año normal tiene 365 días, es decir, 52 semanas y 1 día. Por eso una misma fecha avanza un día de la semana cada año, y dos cuando hay un 29 de febrero de por medio. Así, si tu cumpleaños es martes este año, el que viene será miércoles.</p>
<h2>Qué día cae cada fiesta de estas Navidades y de 2027</h2>
<table><tr><th>Fecha</th><th>Día de la semana</th></tr>
<tr><td>Nochebuena, 24 de diciembre de 2026</td><td>jueves</td></tr><tr><td>Navidad, 25 de diciembre de 2026</td><td>viernes</td></tr>
<tr><td>Nochevieja, 31 de diciembre de 2026</td><td>jueves</td></tr><tr><td>Año Nuevo, 1 de enero de 2027</td><td>viernes</td></tr>
<tr><td>Reyes, 6 de enero de 2027</td><td>miércoles</td></tr><tr><td>San Valentín, 14 de febrero de 2027</td><td>domingo</td></tr>
<tr><td>Jueves y Viernes Santo de 2027</td><td>25 y 26 de marzo</td></tr><tr><td>Navidad, 25 de diciembre de 2027</td><td>sábado</td></tr></table>
<p>Con Navidad y Año Nuevo en viernes, estas fiestas dejan dos fines de semana largos seguidos. Mira los puentes de todo el año en el <a href="calendario-laboral-2027.html">calendario laboral 2027</a>, cuenta los días con la <a href="cuantos-dias-faltan.html">cuenta atrás para Navidad</a> o calcula <a href="dias-entre-fechas.html">los días entre dos fechas</a>.</p>""",
[("¿Qué día de la semana cae Nochebuena en 2026?", "En jueves. Navidad, el 25 de diciembre de 2026, cae en viernes, y Año Nuevo de 2027 también es viernes."),
 ("¿Qué día de la semana nací?", "Pon tu fecha de nacimiento en la calculadora y te dirá el día exacto."),
 ("¿Qué día cae Navidad el año que viene?", "Elige el 25 de diciembre del año que quieras y lo verás al instante, junto con los años siguientes.")],
None, DATEJS + """function calc(){const a=pd('a');if(!a)return;let h='<table><tr><th>Año</th><th>Día</th></tr>';for(let i=1;i<=5;i++){const d=new Date(a);d.setFullYear(a.getFullYear()+i);h+='<tr><td>'+d.getFullYear()+'</td><td>'+d.toLocaleDateString('es-ES',{weekday:'long'})+'</td></tr>';}
show('r','Es:<b class="big">'+a.toLocaleDateString('es-ES',{weekday:'long'})+'</b>'+fmt(a)+h+'</table>');}calc();"""))

# --- Calendario laboral 2027 (BOE-A-2026-21254, Resolución de 8 de octubre de 2026) ---
CCAA = [("AN","Andalucía"),("AR","Aragón"),("AS","Asturias"),("IB","Illes Balears"),("CN","Canarias"),("CB","Cantabria"),("CL","Castilla-La Mancha"),("CM","Castilla y León"),("CT","Cataluña"),("VC","Comunitat Valenciana"),("EX","Extremadura"),("GA","Galicia"),("MD","Comunidad de Madrid"),("MC","Región de Murcia"),("NC","Navarra"),("PV","País Vasco"),("RI","La Rioja"),("CE","Ceuta"),("ML","Melilla")]
_ALL = "AN AR AS IB CN CB CL CM CT EX GA MD MC NC PV RI VC CE ML"
FEST27 = [("2027-01-01","Año Nuevo",_ALL),("2027-01-06","Epifanía del Señor",_ALL),("2027-03-01","Día de Andalucía","AN"),("2027-03-01","Día de les Illes Balears","IB"),
 ("2027-03-10","Fiesta del Eid Fitr","ML"),("2027-03-19","San José","GA MD MC NC VC"),("2027-03-25","Jueves Santo","AN AR AS IB CN CB CL CM EX GA MD MC NC PV RI CE ML"),
 ("2027-03-26","Viernes Santo",_ALL),("2027-03-29","Lunes de Pascua","IB CT NC PV RI VC"),("2027-04-23","San Jorge / Día de Aragón","AR"),("2027-04-23","Fiesta de Castilla y León","CM"),
 ("2027-05-01","Fiesta del Trabajo",_ALL),("2027-05-17","Día de las Letras Gallegas","GA"),("2027-05-17","Eidul Adha, Fiesta del Sacrificio","CE"),("2027-05-17","Fiesta del Sacrificio, Aid Al Adha","ML"),
 ("2027-05-27","Corpus Christi","CL"),("2027-05-31","Día de Castilla-La Mancha","CL"),("2027-06-09","Día de la Región de Murcia","MC"),("2027-06-09","Día de La Rioja","RI"),("2027-06-24","Día de San Juan","CT"),
 ("2027-07-28","Día de las Instituciones de Cantabria","CB"),("2027-08-05","Nuestra Señora de África","CE"),("2027-08-16","Lunes siguiente a la Asunción de la Virgen","AN AR AS CN CM MD"),
 ("2027-09-08","Día de Asturias","AS"),("2027-09-08","Día de Extremadura","EX"),("2027-09-11","Fiesta Nacional de Cataluña","CT"),("2027-09-15","La Bien Aparecida","CB"),
 ("2027-10-07","Aniversario del primer Gobierno vasco","PV"),("2027-10-09","Día de la Comunitat Valenciana","VC"),("2027-10-11","Sustitución del 15 de agosto","EX"),
 ("2027-10-12","Fiesta Nacional de España",_ALL),("2027-11-01","Todos los Santos",_ALL),("2027-12-06","Día de la Constitución Española",_ALL),("2027-12-08","Inmaculada Concepción",_ALL),("2027-12-25","Natividad del Señor",_ALL)]
ISLAS = [("","Selecciona tu isla"),("2027-09-24|El Hierro","El Hierro"),("2027-09-17|Fuerteventura","Fuerteventura"),("2027-09-08|Gran Canaria","Gran Canaria"),("2027-10-04|La Gomera","La Gomera"),("2027-08-05|La Palma","La Palma"),("2027-09-15|Lanzarote y La Graciosa","Lanzarote y La Graciosa"),("2027-02-02|Tenerife","Tenerife")]
_fj = json.dumps([[d, n, c.split()] for d, n, c in FEST27], ensure_ascii=False)
S['tools'].insert(0, ("calendario-laboral-2027", "Calendario laboral 2027", "Festivos de tu comunidad, puentes y días laborables de 2027, según el BOE.", "Calendario 2027"))
S['aff']["calendario-laboral-2027"] = amz("calendario pared 2027", "Calendarios 2027") + amz("agenda 2027", "Agendas 2027")
_opts = "".join(f'<option value="{c}"{" selected" if c=="MD" else ""}>{n}</option>' for c, n in CCAA)
_isl = "".join(f'<option value="{v}">{n}</option>' for v, n in ISLAS)
P.append(("calendario-laboral-2027", "Calendario laboral 2027: festivos por comunidad y puentes | CalculadoraDías",
"Calendario laboral 2027 oficial: festivos nacionales y de tu comunidad autónoma, puentes, días laborables por mes y opción de añadir tus festivos locales. Según el BOE.",
"""<p class="lead">Elige tu comunidad y te mostramos todos los festivos de 2027, los puentes y los días laborables de cada mes, según la relación oficial publicada en el BOE.</p>
<div class="card"><label for="cc">Comunidad autónoma</label><select id="cc" onchange="pinta()">""" + _opts + """</select>
<div id="isw" style="display:none"><label for="is">Isla (Canarias tiene una fiesta insular)</label><select id="is" onchange="pinta()">""" + _isl + """</select></div>
<label for="lo">Tus 2 festivos locales (opcional, dd/mm)</label><input id="lo" placeholder="15/05, 09/11" oninput="pinta()">
<div id="r2" style="margin-top:16px"></div></div>
<h2>Festivos comunes a toda España en 2027</h2><p>Nueve fiestas son iguales en todo el país: 1 de enero (Año Nuevo), 6 de enero (Epifanía), 26 de marzo (Viernes Santo), 1 de mayo (Fiesta del Trabajo), 12 de octubre (Fiesta Nacional), 1 de noviembre (Todos los Santos), 6 de diciembre (Constitución), 8 de diciembre (Inmaculada) y 25 de diciembre (Navidad). En 2027 el 15 de agosto cae en domingo, así que varias comunidades lo pasan al lunes 16 y otras lo sustituyen por otra fiesta.</p>
<h2>Festivos locales</h2><p>Además de estos, cada municipio tiene dos fiestas locales, que publica el boletín oficial de cada comunidad o provincia. Añádelas arriba para ver tu calendario completo y tus días laborables exactos.</p>
<p>¿Quieres saber qué días pedir de vacaciones para encadenar más descanso? Usa el <a href="puentes-2027.html">planificador de puentes 2027</a>.</p>
<p class="note">Fuente: Resolución de 8 de octubre de 2026, de la Dirección General de Trabajo, por la que se publica relación de fiestas laborales para el año 2027 (BOE núm. 254, de 13 de octubre de 2026, BOE-A-2026-21254). En el Valle de Arán, el 29 de marzo se sustituye por el 17 de junio (Fiesta de Arán).</p>""",
[("¿Cuántos festivos hay en 2027?", "Doce festivos de ámbito nacional y autonómico en cada comunidad (once en Canarias más la fiesta de cada isla), a los que se suman dos fiestas locales de cada municipio: catorce en total."),
 ("¿Qué festivos son iguales en toda España en 2027?", "Año Nuevo, Epifanía, Viernes Santo, Fiesta del Trabajo, Fiesta Nacional de España, Todos los Santos, Día de la Constitución, Inmaculada Concepción y Navidad."),
 ("¿Qué pasa con el 15 de agosto de 2027?", "Cae en domingo. Andalucía, Aragón, Asturias, Canarias, Castilla y León y Madrid lo trasladan al lunes 16 de agosto; Extremadura lo sustituye por el 11 de octubre."),
 ("¿Dónde consulto mis festivos locales?", "En el boletín oficial de tu comunidad o provincia, o en la web de tu ayuntamiento. Cuando los tengas, añádelos en el campo de festivos locales.")],
"Calendario laboral 2027",
"""const F=""" + _fj + """;
const MES=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'],DS=['L','M','X','J','V','S','D'];
const iso=(m,d)=>'2027-'+String(m+1).padStart(2,'0')+'-'+String(d).padStart(2,'0');
function pinta(){const cc=document.getElementById('cc').value;document.getElementById('isw').style.display=cc=='CN'?'block':'none';
const fs={};F.forEach(f=>{if(f[2].includes(cc))fs[f[0]]=f[1];});
if(cc=='CN'){const v=document.getElementById('is').value;if(v){const p=v.split('|');fs[p[0]]='Fiesta insular de '+p[1];}}
const loc=[];document.getElementById('lo').value.split(/[,;\\s]+/).forEach(x=>{const m=x.match(/^(\\d{1,2})[\\/.-](\\d{1,2})$/);if(m){const k=iso(+m[2]-1,+m[1]);if(!fs[k]){fs[k]='Festivo local';loc.push(k);}}});
const ks=Object.keys(fs).sort();const dow=k=>(new Date(k+'T12:00').getDay()+6)%7;
const lab=[];let tot=0;for(let m=0;m<12;m++){let n=0;const dim=new Date(2027,m+1,0).getDate();for(let d=1;d<=dim;d++){const w=(new Date(2027,m,d).getDay()+6)%7;if(w<5&&!fs[iso(m,d)])n++;}lab.push(n);tot+=n;}
const adj=k=>{const dt=new Date(k+'T12:00');dt.setDate(dt.getDate()+(dow(k)==1?-1:1));return dt;};const k2=d=>d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');
const pu=ks.filter(k=>(dow(k)==1||dow(k)==3)&&!fs[k2(adj(k))]).map(k=>{const dt=new Date(k+'T12:00');const o=adj(k);return fmt(dt)+': coge libre el '+o.toLocaleDateString('es-ES',{weekday:'long',day:'numeric',month:'long'})+' y tienes 4 días';});
const lg=ks.filter(k=>dow(k)==0||dow(k)==4).map(k=>fmt(new Date(k+'T12:00'))+': fin de semana largo de 3 días');
let h='<b class="big" style="font-size:1.4rem">'+ks.filter(k=>dow(k)<5).length+' festivos entre semana · '+tot+' días laborables</b>';
h+='<table><tr><th>Fecha</th><th>Fiesta</th></tr>'+ks.map(k=>'<tr><td>'+new Date(k+'T12:00').toLocaleDateString('es-ES',{weekday:'short',day:'numeric',month:'short'})+'</td><td>'+fs[k]+(dow(k)>4?' <span class="note">(cae en fin de semana)</span>':'')+'</td></tr>').join('')+'</table>';
if(pu.length||lg.length)h+='<h3>Puentes y fines de semana largos</h3><ul>'+pu.concat(lg).map(x=>'<li>'+x+'</li>').join('')+'</ul>';
const cel=i=>'<td style="text-align:center"><b>'+MES[i].slice(0,3)+'</b><br>'+lab[i]+'</td>';h+='<h3>Días laborables por mes</h3><table><tr>'+[0,1,2,3,4,5].map(cel).join('')+'</tr><tr>'+[6,7,8,9,10,11].map(cel).join('')+'</tr></table>';
h+='<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px;margin-top:16px">';
for(let m=0;m<12;m++){const off=(new Date(2027,m,1).getDay()+6)%7,dim=new Date(2027,m+1,0).getDate();h+='<div><b>'+MES[m]+'</b><div style="display:grid;grid-template-columns:repeat(7,1fr);gap:2px;font-size:.75rem;text-align:center">'+DS.map(x=>'<span class="note">'+x+'</span>').join('')+'<span></span>'.repeat(off);
for(let d=1;d<=dim;d++){const k=iso(m,d),w=(off+d-1)%7,f=fs[k];h+='<span title="'+(f||'')+'" style="padding:3px 0;border-radius:4px;'+(f?'background:#5f3dc4;color:#fff;font-weight:700':w>4?'color:#9aa0b0':'')+'">'+d+'</span>';}h+='</div></div>';}
h+='</div><p style="margin-top:14px"><a class="afl" href="dias-habiles.html?f='+encodeURIComponent(ks.map(k=>k.slice(8)+'/'+k.slice(5,7)+'/2027').join(','))+'">Calcular días hábiles con estos festivos →</a></p>';
document.getElementById('r2').innerHTML=h;}
function fmt(d){return d.toLocaleDateString('es-ES',{weekday:'long',day:'numeric',month:'long'});}
pinta();"""))

# --- Calculadora de jubilación ---
S['tools'].insert(3, ("calculadora-jubilacion", "¿Cuándo me jubilo?", "Fecha exacta de tu jubilación ordinaria y anticipada según tu edad y lo cotizado.", ""))
S['aff']["calculadora-jubilacion"] = amz("libro planificar jubilacion", "Libros para planificar la jubilación") + amz("agenda 2027", "Agendas 2027")
P.append(("calculadora-jubilacion", "Calculadora de jubilación: ¿cuándo me jubilo? Fecha exacta 2027 | CalculadoraDías",
"Calcula el día exacto en que podrás jubilarte según tu fecha de nacimiento y los años cotizados: 65 o 67 años con las reglas de 2027, jubilación anticipada y cuenta atrás.",
"""<p class="lead">Pon tu fecha de nacimiento y lo que llevas cotizado y te decimos el día en que podrás jubilarte, a qué edad y cuánto te falta.</p>
<div class="card"><label for="a">Fecha de nacimiento</label><input id="a" type="date" value="1962-05-15">
<div class="row"><div><label for="cy">Años cotizados hasta hoy</label><input id="cy" inputmode="numeric" value="36"></div>
<div><label for="cm">Meses adicionales</label><input id="cm" inputmode="numeric" value="0"></div></div>
<label for="s">¿Seguirás cotizando hasta jubilarte?</label><select id="s"><option value="1">Sí, sigo trabajando o cobrando paro contributivo</option><option value="0">No, ya no cotizo</option></select>
<button onclick="calc()">Calcular mi jubilación</button><div class="res" id="r"></div></div>
<p class="note">Los años cotizados los ves en tu <a href="https://portal.seg-social.gob.es/wps/portal/importass/importass/tramites/informeVidaLaboral" rel="noopener" target="_blank">informe de vida laboral</a> (sección «Total de días cotizados»: divide entre 365). Cálculo orientativo con las reglas generales de la Ley General de la Seguridad Social; no incluye jubilaciones especiales (profesiones con coeficientes reductores, discapacidad) ni la jubilación activa o demorada.</p>
<h2>Cómo se calcula la edad de jubilación</h2><p>Desde 2013 la edad ordinaria sube poco a poco hasta los 67 años, salvo para quien ha cotizado mucho. En <b>2027 termina la transición</b>: podrás jubilarte a los <b>65 años si acumulas 38 años y 6 meses cotizados</b>; si no, a los <b>67</b>. Lo que cuenta es la regla del año en que te jubilas y lo cotizado en ese momento, así que alguien que cumple los 65 sin llegar a 38,5 años puede jubilarse antes de los 67 justo el día en que complete ese periodo.</p>
<table><tr><th>Año</th><th>Edad con menos cotizado</th><th>A los 65 si tienes</th></tr>
<tr><td>2024</td><td>66 años y 6 meses</td><td>38 años</td></tr><tr><td>2025</td><td>66 años y 8 meses</td><td>38 años y 3 meses</td></tr>
<tr><td>2026</td><td>66 años y 10 meses</td><td>38 años y 3 meses</td></tr><tr><td>2027 y siguientes</td><td>67 años</td><td>38 años y 6 meses</td></tr></table>
<h2>Jubilación anticipada</h2><p>La <b>voluntaria</b> permite adelantar hasta 2 años la edad que te corresponda si tienes al menos 35 años cotizados; la <b>involuntaria</b> (por despido o cierre), hasta 4 años con 33 cotizados. En ambos casos la pensión se reduce con un coeficiente por cada mes de adelanto, por lo que conviene pedir antes una simulación en <a href="https://portal.seg-social.gob.es/" rel="noopener" target="_blank">Tu Seguridad Social</a>.</p>
<p><b>Ejemplo:</b> una persona nacida el 15 de mayo de 1962 con 36 años cotizados en noviembre de 2026 cumple 65 en mayo de 2027, pero entonces solo tendrá unos 36 años y medio. Aunque siga cotizando, no llegará a 38 años y 6 meses hasta después de cumplir los 67, así que su jubilación ordinaria es el 15 de mayo de 2029. Como tendrá más de 35 años cotizados, podría adelantarla de forma voluntaria hasta el 15 de mayo de 2027, con la pensión reducida.</p>""",
[("¿Con cuántos años me puedo jubilar en 2027?", "A los 65 años si tienes 38 años y 6 meses cotizados o más; con menos, a los 67. Es la regla definitiva que se aplica desde 2027."),
 ("¿Cuántos años hay que cotizar para jubilarse a los 65?", "En 2026, 38 años y 3 meses; a partir de 2027, 38 años y 6 meses. Para cobrar pensión hacen falta al menos 15 años cotizados, 2 de ellos dentro de los últimos 15."),
 ("¿Cuándo puedo pedir la jubilación anticipada?", "La voluntaria, hasta 2 años antes de tu edad ordinaria si tienes 35 años cotizados; la involuntaria, hasta 4 años antes con 33 años cotizados. La pensión se reduce por cada mes de adelanto."),
 ("¿Dónde veo cuántos años he cotizado?", "En el informe de vida laboral de la Seguridad Social, que puedes descargar gratis en su web o app con certificado, Cl@ve o SMS.")],
"Calculadora de jubilación: ¿cuándo me jubilo?",
DATEJS + """const RQ={2013:[781,423],2014:[782,426],2015:[783,429],2016:[784,432],2017:[785,435],2018:[786,438],2019:[788,441],2020:[790,444],2021:[792,447],2022:[794,450],2023:[796,453],2024:[798,456],2025:[800,459],2026:[802,459]};
const rq=y=>y<2013?[780,0]:(RQ[y]||[804,462]);
const am=(d,n)=>{const y=d.getFullYear(),m=d.getMonth()+n,t=new Date(y,m,1),dim=new Date(t.getFullYear(),t.getMonth()+1,0).getDate();return new Date(t.getFullYear(),t.getMonth(),Math.min(d.getDate(),dim));};
const mb=(a,b)=>{let m=(b.getFullYear()-a.getFullYear())*12+b.getMonth()-a.getMonth();if(b.getDate()<a.getDate())m--;return m;};
const ym=m=>{const y=Math.floor(m/12),r=m%12;return (y?y+(y>1?' años':' año'):'')+(y&&r?' y ':'')+(r?r+(r>1?' meses':' mes'):'')||'0 meses';};
function calc(){const b=pd('a');if(!b)return;const hoy=new Date();hoy.setHours(0,0,0,0);const c0=Math.round(v('cy'))*12+Math.round(v('cm')),sg=document.getElementById('s').value=='1';
const cot=D=>D>hoy&&sg?c0+mb(hoy,D):c0;let n=780,D;for(;n<=804;n++){D=am(b,n);const r=rq(D.getFullYear());if(n>=r[0]||cot(D)>=r[1])break;}
const r0=rq(D.getFullYear());if(sg&&n>780&&n<r0[0]){const E=am(hoy,r0[1]-c0);if(E<D&&E>am(b,n-1))D=E;}
const ord=mb(b,D),cD=cot(D);let h='Podrás jubilarte el:<b class="big">'+fmt(D)+'</b>Con <b>'+ym(ord)+'</b> de edad y unos <b>'+ym(cD)+'</b> cotizados.';
const f=diff(hoy,D);if(f>0){const mm=mb(hoy,D),r2=am(hoy,mm),dd=diff(r2,D);h+='<br>Te faltan <b>'+ym(mm)+(dd?' y '+dd+' días':'')+'</b> ('+f.toLocaleString('es-ES')+' días).';}else h+='<br>Ya has alcanzado tu edad de jubilación ordinaria.';
if(cD<180)h+='<br><b>Ojo:</b> para cobrar pensión contributiva necesitas al menos 15 años cotizados.';
const F=am(b,780),ex=cot(F)>=rq(F.getFullYear())[1]?780:r0[0],A=am(b,ex-24),cA=cot(A);
if(A<D&&A>hoy)h+='<br><br>Jubilación anticipada voluntaria: '+(cA>=420?'desde el <b>'+fmt(A)+'</b> (a los '+ym(ex-24)+'), con la pensión reducida.':'necesitas 35 años cotizados en ese momento y tendrías unos '+ym(cA)+'.');
show('r',h);}"""))

# --- Calculadora de embarazo: semanas y fecha probable de parto ---
S['tools'].insert(4, ("calculadora-embarazo", "Semanas de embarazo y fecha de parto", "En qué semana estás, fecha probable de parto y calendario de pruebas.", ""))
S['aff']["calculadora-embarazo"] = amz("diario embarazo", "Diarios y agendas de embarazo") + amz("almohada embarazo", "Almohadas de embarazo")
P.append(("calculadora-embarazo", "Calculadora de embarazo: semanas y fecha probable de parto | CalculadoraDías",
"¿De cuántas semanas estás? Calcula la fecha probable de parto, el trimestre, los meses y el calendario de ecografías y pruebas a partir de tu última regla o de la ecografía.",
"""<p class="lead">Pon el primer día de tu última regla (o la fecha de la ecografía) y te decimos de cuántas semanas estás, la fecha probable de parto y cuándo tocan las pruebas.</p>
<div class="card"><label for="m">Calcular a partir de</label><select id="m" onchange="modo();calc()"><option value="f">Primer día de la última regla</option><option value="c">Fecha de concepción</option><option value="e">Una ecografía (semanas y días que te dieron)</option></select>
<div class="row"><div><label for="a" id="al">Primer día de la última regla</label><input id="a" type="date"></div>
<div id="bc"><label for="cl">Duración de tu ciclo (días)</label><input id="cl" inputmode="numeric" value="28"></div>
<div id="be1" style="display:none"><label for="es">Semanas en esa ecografía</label><input id="es" inputmode="numeric" value="12"></div>
<div id="be2" style="display:none"><label for="ed">Días adicionales</label><input id="ed" inputmode="numeric" value="3"></div></div>
<button onclick="calc()">Calcular</button><div class="res" id="r"></div></div>
<p class="note">Cálculo de fechas orientativo: la fecha que manda es la que te dé tu matrona o tu ginecólogo, normalmente corregida con la ecografía del primer trimestre. Solo un 4-5 % de los bebés nace justo el día de la fecha probable de parto.</p>
<h2>Cómo se calcula la fecha probable de parto</h2><p>Se usa la <b>regla de Naegele</b>: fecha de la última regla + <b>280 días</b> (40 semanas). Supone un ciclo de 28 días con ovulación el día 14, así que si tus ciclos son más largos o más cortos se suma o resta la diferencia. Si conoces la fecha de concepción (o de transferencia en una FIV), se cuentan <b>266 días</b> desde ese día; en FIV con embrión de 5 días, 261 días desde la transferencia. Las semanas de embarazo se cuentan siempre desde la última regla, por eso en la semana 2 aún no hay embarazo.</p>
<table><tr><th>Etapa</th><th>Semanas</th></tr><tr><td>Primer trimestre</td><td>1 a 13+6</td></tr><tr><td>Segundo trimestre</td><td>14 a 27+6</td></tr><tr><td>Tercer trimestre</td><td>28 al parto</td></tr><tr><td>Parto a término</td><td>37+0 a 41+6</td></tr></table>
<p><b>Ejemplo:</b> si tu última regla empezó el 1 de marzo de 2027 y tus ciclos son de 28 días, la fecha probable de parto es el 6 de diciembre de 2027. Con ciclos de 32 días, se retrasa 4 días, al 10 de diciembre. El 1 de junio estarías de 13 semanas y 1 día, acabando el primer trimestre.</p>
<h2>Calendario orientativo de pruebas</h2><p>Las fechas exactas dependen de tu comunidad y tu centro de salud, pero en la sanidad pública española el seguimiento suele incluir: analítica y cribado combinado del primer trimestre con ecografía entre las <b>semanas 11 y 14</b>, la ecografía morfológica hacia la <b>semana 20</b>, el test de O'Sullivan (glucosa) entre las <b>semanas 24 y 28</b>, la ecografía del tercer trimestre hacia la <b>semana 32-34</b> y el cultivo del estreptococo entre las <b>semanas 35 y 37</b>. La calculadora te da las fechas que corresponden a tu caso.</p>
<p>Con la fecha probable de parto, calcula también las fechas de tu <a href="permiso-nacimiento.html">permiso por nacimiento</a> (20 semanas por progenitor para los nacidos desde el 26 de noviembre de 2026).</p>
<p>¿Quieres saber cuántos días faltan exactamente o qué día de la semana caerá? Usa la <a href="cuantos-dias-faltan.html">cuenta atrás</a> o el <a href="que-dia-de-la-semana.html">día de la semana de cualquier fecha</a>.</p>""",
[("¿Cómo sé de cuántas semanas estoy?", "Cuenta los días desde el primer día de tu última regla y divide entre 7: el cociente son las semanas y el resto, los días. Por ejemplo, 93 días son 13 semanas y 2 días (se escribe 13+2)."),
 ("¿Cuántas semanas dura un embarazo?", "Unas 40 semanas (280 días) contando desde la última regla, que equivalen a unas 38 semanas desde la concepción. Se considera a término entre la semana 37 y la 41+6."),
 ("¿Cuántos meses de embarazo son 20 semanas?", "Unos 4 meses y medio. Como los meses no tienen 4 semanas exactas, 40 semanas son algo más de 9 meses naturales contados desde la última regla."),
 ("¿Es fiable la fecha probable de parto?", "Es una estimación: la mayoría de partos ocurre en las dos semanas anteriores o posteriores a esa fecha. La ecografía del primer trimestre es la forma más precisa de fecharla.")],
"Calculadora de semanas de embarazo y fecha probable de parto",
DATEJS + """const ad=(d,n)=>{const x=new Date(d);x.setDate(x.getDate()+n);return x;};
const sd=n=>Math.floor(n/7)+' semanas'+(n%7?' y '+(n%7)+(n%7>1?' días':' día'):'');
function modo(){const m=document.getElementById('m').value;document.getElementById('al').textContent=m=='f'?'Primer día de la última regla':m=='c'?'Fecha de concepción':'Fecha de la ecografía';
document.getElementById('bc').style.display=m=='f'?'':'none';document.getElementById('be1').style.display=m=='e'?'':'none';document.getElementById('be2').style.display=m=='e'?'':'none';}
(function(){const e=document.getElementById('a');if(!e.value)e.value=iso(ad(new Date(),-93));})();
function calc(){const m=document.getElementById('m').value,a=pd('a');if(!a)return;let f;
if(m=='f'){const c=Math.min(45,Math.max(20,v('cl')||28));f=ad(a,c-28);}else if(m=='c')f=ad(a,-14);else f=ad(a,-(Math.round(v('es'))*7+Math.round(v('ed'))));
const fpp=ad(f,280),h=new Date();h.setHours(0,0,0,0);const g=diff(f,h),q=diff(h,fpp);
let r='Fecha probable de parto:<b class="big">'+fmt(fpp)+'</b>';
if(g<0)r+='La fecha de la regla es posterior a hoy: revisa el dato.';
else if(g<=300){const w=Math.floor(g/7),t=w<14?'primer':w<28?'segundo':'tercer';r+='Hoy estás de <b>'+sd(g)+'</b> ('+w+'+'+(g%7)+'), en el <b>'+t+' trimestre</b>, unos '+nf(g/30.44,1)+' meses.';
r+=q>0?' Faltan <b>'+q+' días</b> para la fecha probable.':' Ya has superado la fecha probable de parto en '+(-q)+' días.';
r+='<br>A término desde el <b>'+ad(f,259).toLocaleDateString('es-ES')+'</b> (semana 37).';}
const T=[['Ecografía y cribado del 1.er trimestre',77,97],['Ecografía morfológica',133,146],["Test de O'Sullivan",168,195],['Ecografía del 3.er trimestre',224,237],['Cultivo de estreptococo',245,258]];
r+='<table><tr><th>Prueba orientativa</th><th>Entre</th></tr>'+T.map(x=>'<tr><td>'+x[0]+'</td><td>'+ad(f,x[1]).toLocaleDateString('es-ES',{day:'numeric',month:'short'})+' y '+ad(f,x[2]).toLocaleDateString('es-ES',{day:'numeric',month:'short',year:'numeric'})+'</td></tr>').join('')+'</table>';
show('r',r);}"""))

# --- Lotería de Navidad y del Niño: premio neto tras Hacienda (gravamen especial: 20 % sobre lo que pasa de 40.000 € por décimo) ---
S['tools'].insert(1, ("premio-loteria-navidad", "Premio de la Lotería de Navidad y del Niño", "Cuánto te queda tras Hacienda, hasta cuándo puedes cobrar y dónde.", "Lotería"))
S['aff']["premio-loteria-navidad"] = amz("cartera porta decimos loteria", "Fundas para guardar décimos") + amz("agenda 2027", "Agendas 2027")
P.append(("premio-loteria-navidad", "Calculadora Lotería de Navidad 2026: premio neto tras Hacienda | CalculadoraDías",
"Calcula el premio neto de tu décimo o participación de la Lotería de Navidad (22 de diciembre) o del Niño: retención del 20 % a partir de 40.000 €, fecha límite para cobrar y dónde hacerlo.",
"""<p class="lead">Elige el sorteo, el premio y lo que juegas de ese número (un décimo son 20 €). Te decimos cuánto se queda Hacienda, lo que cobras limpio y hasta qué día puedes cobrarlo.</p>
<div class="card"><label for="so">Sorteo</label><select id="so" onchange="lista()"><option value="n">Lotería de Navidad · martes 22 de diciembre de 2026</option><option value="k">Lotería del Niño · miércoles 6 de enero de 2027</option></select>
<label for="pz">Premio</label><select id="pz" onchange="calc()"></select>
<div class="row"><div><label for="ju">Lo que juegas de ese número (€)</label><input id="ju" inputmode="decimal" value="20"></div>
<div><label for="ot">Premio por décimo si eliges «Otro importe» (€)</label><input id="ot" inputmode="decimal" value="1000"></div></div>
<p class="note">Un décimo entero = 20 €. Una participación de 5 € es la cuarta parte de un décimo; dos décimos del mismo número = 40 €.</p>
<button onclick="calc()">Calcular premio neto</button><div class="res" id="r" aria-live="polite"></div></div>
<h2>Cómo tributa el premio</h2><p>Los premios de Loterías y Apuestas del Estado pagan un <b>gravamen especial del 20 %</b>, pero solo sobre la parte del premio que supera los <b>40.000 € por décimo</b>. Si juegas una fracción, la parte exenta se reduce en la misma proporción: con una participación de 5 € (un cuarto de décimo) tienes exentos 10.000 €. La retención se aplica al cobrar y es definitiva: no tienes que volver a pagar por el premio en la declaración de la renta.</p>
<p><b>Fórmula:</b> premio bruto = premio por décimo × (lo jugado ÷ 20). Impuesto = 20 % × (premio bruto − 40.000 × lo jugado ÷ 20), si sale positivo.</p>
<table><tr><th>Premio (por décimo)</th><th>Bruto</th><th>Hacienda</th><th>Te queda</th></tr>
<tr><td>Primer premio («el Gordo»)</td><td>400.000 €</td><td>72.000 €</td><td><b>328.000 €</b></td></tr>
<tr><td>Segundo premio</td><td>125.000 €</td><td>17.000 €</td><td><b>108.000 €</b></td></tr>
<tr><td>Tercer premio</td><td>50.000 €</td><td>2.000 €</td><td><b>48.000 €</b></td></tr>
<tr><td>Cuarto premio (hay 2)</td><td>20.000 €</td><td>0 €</td><td><b>20.000 €</b></td></tr>
<tr><td>Quinto premio (hay 8)</td><td>6.000 €</td><td>0 €</td><td><b>6.000 €</b></td></tr>
<tr><td>Aproximaciones al 1.º / 2.º / 3.º</td><td>2.000 / 1.250 / 960 €</td><td>0 €</td><td>íntegro</td></tr>
<tr><td>Pedrea, centenas y dos últimas cifras</td><td>100 €</td><td>0 €</td><td>100 €</td></tr>
<tr><td>Reintegro (última cifra del Gordo)</td><td>20 €</td><td>0 €</td><td>20 €</td></tr></table>
<p><b>Ejemplo:</b> compartes un décimo del Gordo a medias con tu pareja (10 € cada uno). A cada uno le corresponden 200.000 €, con 20.000 € exentos: Hacienda retiene el 20 % de 180.000 €, es decir 36.000 €, y cada uno cobra <b>164.000 €</b>.</p>
<h2>Plazos y dónde cobrar</h2><p>Hay <b>tres meses</b> para cobrar desde el día siguiente al sorteo: los premios de Navidad 2026 se pueden cobrar hasta el <b>22 de marzo de 2027</b> y los del Niño, hasta el <b>6 de abril de 2027</b>. Después, el dinero pasa al Estado. Los premios de menos de 2.000 € por décimo se cobran en cualquier administración de lotería; los mayores, en las entidades bancarias colaboradoras de Loterías y Apuestas del Estado. Firma el décimo por detrás y hazle una foto en cuanto sepas que tiene premio. Comprueba siempre los números con la lista oficial en la web de <a href="https://www.loteriasyapuestas.es/" rel="noopener" target="_blank">Loterías y Apuestas del Estado</a>.</p>
<p>¿Cuánto queda para el sorteo? Míralo en la <a href="cuantos-dias-faltan.html">cuenta atrás para la Lotería y Navidad</a>, y organiza los días libres de 2027 con el <a href="calendario-laboral-2027.html">calendario laboral y los puentes</a>.</p>""",
[("¿Cuánto se queda Hacienda del Gordo de Navidad?", "De un décimo de 20 € premiado con el Gordo (400.000 €) los primeros 40.000 € están exentos y el resto paga el 20 %: Hacienda retiene 72.000 € y cobras 328.000 €."),
 ("¿Los premios de menos de 40.000 € pagan impuestos?", "No. Un premio de hasta 40.000 € por décimo está exento y se cobra íntegro. Ojo: si juegas una participación, el mínimo exento se reduce en proporción a lo que juegas."),
 ("¿Hasta cuándo se puede cobrar la Lotería de Navidad 2026?", "Tienes tres meses desde el día siguiente al sorteo del 22 de diciembre de 2026, es decir, hasta el 22 de marzo de 2027. Los premios del Niño (6 de enero de 2027) caducan el 6 de abril de 2027."),
 ("¿Tengo que declarar el premio en la renta?", "No. La retención del 20 % que se practica al cobrar es el gravamen especial definitivo y el premio no se suma al resto de ingresos del IRPF.")],
"Calculadora del premio de la Lotería de Navidad y del Niño",
"""const PZ={n:[['Primer premio (el Gordo)',400000],['Segundo premio',125000],['Tercer premio',50000],['Cuarto premio',20000],['Quinto premio',6000],['Aproximación al primer premio',2000],['Aproximación al segundo premio',1250],['Aproximación al tercer premio',960],['Pedrea, centena o dos últimas cifras',100],['Reintegro',20],['Otro importe',0]],
k:[['Primer premio',200000],['Segundo premio',75000],['Tercer premio',25000],['Aproximación al primer premio',1200],['Aproximación al segundo premio',610],['Terminación de 4 cifras',350],['Terminación de 3 cifras',100],['Terminación de 2 cifras',40],['Reintegro',20],['Otro importe',0]]};
const SD={n:[new Date(2026,11,22),new Date(2027,2,22),'22 de marzo de 2027'],k:[new Date(2027,0,6),new Date(2027,3,6),'6 de abril de 2027']};
function lista(){const s=document.getElementById('so').value;document.getElementById('pz').innerHTML=PZ[s].map((x,i)=>'<option value="'+i+'">'+x[0]+(x[1]?' · '+x[1].toLocaleString('es-ES')+' € el décimo':'')+'</option>').join('');calc();}
function calc(){const s=document.getElementById('so').value,p=PZ[s][+document.getElementById('pz').value||0],pd=p[1]||v('ot'),j=v('ju'),f=j/20;
if(j<=0||pd<=0){show('r','Escribe lo que juegas y el importe del premio.');return;}
const br=pd*f,ex=40000*f,tx=Math.max(0,br-ex)*0.2,ne=br-tx,hoy=new Date();hoy.setHours(0,0,0,0);
const ds=Math.round((SD[s][0]-hoy)/864e5),ok=Math.round((SD[s][1]-hoy)/864e5);
let h='Cobras limpio:<b class="big">'+eur(ne)+'</b>Premio bruto: <b>'+eur(br)+'</b> ('+nf(f,2)+(f==1?' décimo':' décimos')+' × '+eur(pd)+')<br>';
h+=tx>0?'Exento: '+eur(ex)+' · Retención del 20 % sobre '+eur(br-ex)+': <b>'+eur(tx)+'</b>':'<b>Sin impuestos</b>: no supera los '+eur(ex)+' exentos que corresponden a lo que juegas.';
h+='<br>'+(br/f<2000?'Se cobra en cualquier administración de lotería.':'Más de 2.000 € por décimo: se cobra en las entidades bancarias colaboradoras.');
h+='<br>'+(ds>0?'Faltan <b>'+ds+' días</b> para el sorteo. ':'')+'Fecha límite para cobrar: <b>'+SD[s][2]+'</b>'+(ds<=0&&ok>=0?' (quedan '+ok+' días)':'')+'.';
show('r',h);}
lista();"""))

# --- Paga extra de Navidad: parte proporcional según días trabajados en el periodo de devengo (art. 31 ET; cuantía y devengo según convenio) ---
S['tools'].insert(2, ("paga-extra-navidad", "Paga extra de Navidad", "Cuánto cobras de paga extra según los días trabajados, tu jornada y el IRPF.", "Paga extra"))
S['aff']["paga-extra-navidad"] = amz("agenda 2027", "Agendas 2027") + amz("hucha ahorro", "Huchas y libretas de ahorro")
P.append(("paga-extra-navidad", "Calcular paga extra de Navidad 2026 por días trabajados | CalculadoraDías",
"Calcula tu paga extra de Navidad: parte proporcional por días trabajados si entraste este año, devengo anual o semestral, jornada parcial e IRPF. Bruto y neto al instante.",
"""<p class="lead">Pon lo que cobras en una paga extra completa y desde cuándo trabajas en la empresa. Calculamos los días que generan paga dentro del periodo de tu convenio y lo que te llegará en bruto y en neto.</p>
<div class="card"><div class="row"><div><label for="pe">Paga extra completa según convenio (€ brutos)</label><input id="pe" inputmode="decimal" value="1600"></div>
<div><label for="dv">Periodo de devengo de la paga de Navidad</label><select id="dv"><option value="a">Anual: 1 de enero a 31 de diciembre de 2026</option><option value="s">Semestral: 1 de julio a 31 de diciembre de 2026</option><option value="d">Anual: 1 de diciembre de 2025 a 30 de noviembre de 2026</option></select></div>
<div><label for="al">Fecha de alta en la empresa</label><input id="al" type="date" value="2026-03-02"></div>
<div><label for="fb">Fecha de baja (si dejas la empresa; si no, vacío)</label><input id="fb" type="date"></div>
<div><label for="nc">Días que no generan paga (excedencia, permiso sin sueldo, huelga)</label><input id="nc" inputmode="numeric" value="0"></div>
<div><label for="jo">Jornada (% de la completa)</label><input id="jo" inputmode="decimal" value="100"></div>
<div><label for="ir">Retención de IRPF de tu nómina (%)</label><input id="ir" inputmode="decimal" value="15"></div></div>
<button onclick="calc()">Calcular paga extra</button><div class="res" id="r" aria-live="polite"></div></div>
<h2>Cómo se calcula la paga extra</h2><p>El <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430#a31" rel="noopener" target="_blank">artículo 31 del Estatuto de los Trabajadores</a> reconoce al menos dos pagas extraordinarias al año, una de ellas en Navidad. Su importe y el periodo en el que se «genera» (devengo) los fija tu convenio colectivo: lo más habitual es que la de Navidad se genere a lo largo de todo el año natural, pero hay convenios con devengo semestral (de julio a diciembre) o de diciembre a noviembre. Si no has trabajado el periodo completo, cobras la parte proporcional:</p>
<p><b>Fórmula:</b> paga = paga completa × (días trabajados en el periodo ÷ días del periodo) × % de jornada.</p>
<p><b>Ejemplo:</b> entraste el 2 de marzo de 2026, tu paga completa es de 1.600 € y el devengo es anual. Del 2 de marzo al 31 de diciembre van 305 de los 365 días del año: 1.600 × 305 ÷ 365 = <b>1.336,99 € brutos</b>. Con un 15 % de IRPF te llegan unos 1.136 €. Si el devengo fuera semestral, cobrarías la paga entera porque has trabajado todo el semestre.</p>
<table><tr><th>Alta en 2026 (devengo anual)</th><th>Días computados</th><th>% de la paga</th></tr>
<tr><td>2 de enero</td><td>364</td><td>99,7 %</td></tr><tr><td>1 de abril</td><td>275</td><td>75,3 %</td></tr><tr><td>1 de julio</td><td>184</td><td>50,4 %</td></tr><tr><td>1 de octubre</td><td>92</td><td>25,2 %</td></tr></table>
<h2>Impuestos y cuándo se cobra</h2><p>La paga extra no paga cotizaciones a la Seguridad Social el mes en que la cobras: ya se cotiza repartida en las nóminas de todo el año. Sí lleva la <b>retención de IRPF</b> de tu nómina. La fecha la marca el convenio, normalmente antes del 20-22 de diciembre. Si tus pagas están <b>prorrateadas</b>, ya cobras cada mes la doceava parte y en diciembre no recibirás nada extra. Si dejas la empresa antes, la parte generada se paga en el finiquito.</p>
<p>Organiza los días libres de Navidad con la <a href="calculadora-vacaciones.html">calculadora de vacaciones</a> y el <a href="calendario-laboral-2027.html">calendario laboral 2027 con puentes</a>, o cuenta los <a href="dias-entre-fechas.html">días entre dos fechas</a>.</p>""",
[("¿Cuánto me corresponde de paga extra si empecé a trabajar este año?", "La parte proporcional a los días trabajados dentro del periodo de devengo. Con devengo anual y alta el 1 de julio, te corresponde algo más de la mitad: 184 de 365 días, el 50,4 % de la paga completa."),
 ("¿La paga extra de Navidad lleva descuento de Seguridad Social?", "No en el mes en que se cobra, porque se cotiza prorrateada en todas las nóminas del año. Sí se le aplica la retención de IRPF, así que el neto es la paga bruta menos ese porcentaje."),
 ("¿Las bajas por enfermedad o por nacimiento reducen la paga extra?", "Depende del convenio. Durante esas bajas la prestación ya incluye la parte proporcional de las pagas extra, por lo que muchas empresas descuentan ese periodo. Si tu convenio lo dice, indica esos días como días que no generan paga."),
 ("¿Cuándo cobran los pensionistas la paga extra de Navidad?", "Las pensiones contributivas se pagan en 14 pagas: la extra de Navidad se abona junto con la pensión de noviembre, a finales de ese mes.")],
"Calculadora de la paga extra de Navidad",
DATEJS + """const PER={a:[new Date(2026,0,1),new Date(2026,11,31)],s:[new Date(2026,6,1),new Date(2026,11,31)],d:[new Date(2025,11,1),new Date(2026,10,30)]};
function calc(){const p=PER[document.getElementById('dv').value],pe=v('pe'),jo=(v('jo')||100)/100,al=pd('al'),fb=pd('fb'),irp=v('ir');
if(pe<=0){show('r','Escribe el importe de una paga extra completa.');return;}
const ini=al&&al>p[0]?al:p[0],fin=fb&&fb<p[1]?fb:p[1],tot=diff(p[0],p[1])+1;
let d=Math.max(0,diff(ini,fin)+1-Math.max(0,Math.round(v('nc'))));if(d>tot)d=tot;
const br=pe*d/tot*jo,ne=br*(1-irp/100),f=x=>x.toLocaleDateString('es-ES',{day:'numeric',month:'long',year:'numeric'});
let h='Paga extra de Navidad (bruto):<b class="big">'+eur(br)+'</b>Neto aproximado con '+nf(irp,1)+' % de IRPF: <b>'+eur(ne)+'</b>';
h+='<br>Días que generan paga: <b>'+d+' de '+tot+'</b> ('+nf(d/tot*100,1)+' %), del '+f(ini)+' al '+f(fin)+(jo<1?' · Jornada al '+nf(jo*100,1)+' %':'')+'.';
if(d==0)h+='<br>No has trabajado ningún día de este periodo, así que no te corresponde esta paga.';
if(fb&&fb<p[1])h+='<br>Como dejas la empresa, esta cantidad debe aparecer en tu <b>finiquito</b>.';
h+='<br><span class="note">Si tienes las pagas prorrateadas, ya cobras cada mes '+eur(pe*jo/12)+' brutos por esta paga y en diciembre no recibirás nada aparte.</span>';
show('r',h);}
calc();"""))

# --- Indemnización por despido según antigüedad (arts. 49.1.c, 53.1.b y 56.1 ET y DT 11.ª del Estatuto de los Trabajadores) ---
S['tools'].insert(3, ("indemnizacion-despido", "Indemnización por despido", "Cuánto te corresponde según tu antigüedad, tu salario y el tipo de despido.", "Despido"))
S['aff']["indemnizacion-despido"] = amz("estatuto de los trabajadores 2026", "Estatuto de los Trabajadores") + amz("agenda 2027", "Agendas 2027")
P.append(("indemnizacion-despido", "Calcular indemnización por despido 2026: improcedente y objetivo | CalculadoraDías",
"Calcula tu indemnización por despido improcedente (33 o 45 días por año), objetivo (20 días) o fin de contrato (12 días) con tus fechas exactas y los topes legales.",
"""<p class="lead">Pon tu fecha de alta, la del despido y tu salario bruto anual. Calculamos la antigüedad exacta, el salario diario y la indemnización que marca el Estatuto de los Trabajadores, con sus topes.</p>
<div class="card"><div class="row"><div><label for="al">Fecha de alta en la empresa</label><input id="al" type="date" value="2018-03-01"></div>
<div><label for="de">Fecha del despido o fin de contrato</label><input id="de" type="date" value="2026-11-30"></div>
<div><label for="sa">Salario bruto anual, con pagas extra (€)</label><input id="sa" inputmode="decimal" value="24000"></div>
<div><label for="ti">Tipo de extinción</label><select id="ti"><option value="i">Despido improcedente (33 días por año)</option><option value="o">Despido objetivo o ERE (20 días por año)</option><option value="t">Fin de contrato temporal (12 días por año)</option><option value="d">Despido disciplinario declarado procedente (sin indemnización)</option></select></div></div>
<button onclick="calc()">Calcular indemnización</button><div class="res" id="r" aria-live="polite"></div></div>
<h2>Cuánto se cobra por cada tipo de despido</h2>
<div style="overflow-x:auto"><table><tr><th>Tipo</th><th>Días por año</th><th>Tope</th></tr>
<tr><td>Improcedente</td><td>33 (45 por el tiempo antes del 12/02/2012)</td><td>24 meses de salario (720 días si hay tiempo anterior a 2012, hasta 42 meses)</td></tr>
<tr><td>Objetivo o colectivo (ERE)</td><td>20</td><td>12 mensualidades</td></tr><tr><td>Fin de contrato temporal</td><td>12</td><td>Sin tope</td></tr>
<tr><td>Disciplinario procedente</td><td>0</td><td>—</td></tr></table></div>
<p><b>Fórmula:</b> indemnización = salario diario × días por año × años de servicio. El salario diario es el salario bruto anual (con pagas extra y complementos salariales) ÷ 365. Los periodos de menos de un año se prorratean por meses y, como hacen los tribunales y la mayoría de calculadoras oficiales, la fracción de mes se cuenta como mes completo.</p>
<p><b>Ejemplo:</b> entraste el 1 de marzo de 2018 y te despiden el 30 de noviembre de 2026 con 24.000 € brutos al año. Llevas 8 años y 9 meses (105 meses) y tu salario diario es de 65,75 €. Si el despido es improcedente te corresponden 33 × 105 ÷ 12 = 288,75 días: <b>18.986 €</b>. Si es objetivo, 175 días: <b>11.507 €</b>.</p>
<h2>Impuestos, plazos y finiquito</h2><p>La indemnización por despido está <b>exenta de IRPF</b> hasta la cuantía obligatoria que marca el Estatuto, con un máximo de 180.000 € (artículo 7.e de la Ley del IRPF); en un despido improcedente la exención exige que se reconozca en conciliación o por sentencia. Si no estás de acuerdo con el despido, tienes <b>20 días hábiles</b> para presentar la papeleta de conciliación: calcula la fecha límite con <a href="sumar-dias.html">sumar días hábiles</a>. Aparte de la indemnización, el finiquito incluye el salario del mes, las <a href="calculadora-vacaciones.html">vacaciones no disfrutadas</a> y la parte proporcional de la <a href="paga-extra-navidad.html">paga extra</a>. Puedes revisar la norma en el <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430" rel="noopener" target="_blank">Estatuto de los Trabajadores (BOE)</a>.</p>""",
[("¿Cuánto me corresponde por despido improcedente?", "33 días de salario por año trabajado, prorrateando por meses, con un máximo de 24 mensualidades. Si empezaste antes del 12 de febrero de 2012, el tiempo anterior se paga a 45 días por año. Con 5 años y 30.000 € brutos al año son unos 13.562 €."),
 ("¿Cómo se calcula el salario diario para la indemnización?", "Se divide el salario bruto anual entre 365. Debe incluir las pagas extra y los complementos salariales fijos; no entran las dietas ni los gastos de locomoción."),
 ("¿Tengo que pagar IRPF por la indemnización por despido?", "No hasta la cuantía obligatoria que marca la ley, con un límite de 180.000 €. Lo que la empresa pague de más sí tributa."),
 ("¿Cuánto se cobra al terminar un contrato temporal?", "12 días de salario por año trabajado, prorrateando por meses. Con un contrato de 6 meses y 20.000 € al año, unos 329 €.")],
"Calculadora de indemnización por despido",
DATEJS + """function meses(a,b){if(b<a)return 0;const e=new Date(b);e.setDate(e.getDate()+1);let m=(e.getFullYear()-a.getFullYear())*12+e.getMonth()-a.getMonth();const add=k=>{const x=new Date(a.getFullYear(),a.getMonth()+k,1);x.setDate(Math.min(a.getDate(),new Date(x.getFullYear(),x.getMonth()+1,0).getDate()));return x;};while(m>0&&add(m)>e)m--;return m+(add(m)<e?1:0);}
function calc(){const a=pd('al'),b=pd('de'),sa=v('sa'),ti=document.getElementById('ti').value;
if(!a||!b||b<a||sa<=0){show('r','Revisa las fechas y el salario.');return;}
const sd=sa/365,mens=sa/12,m=meses(a,b),y=Math.floor(m/12),mm=m%12,ant='Antigüedad: <b>'+y+' años y '+mm+' meses</b> ('+m+' meses computados, '+(diff(a,b)+1)+' días)<br>Salario diario: <b>'+eur(sd)+'</b>';
let d=0,tope='',det='';
if(ti=='d'){show('r','Indemnización:<b class="big">'+eur(0)+'</b>'+ant+'<br>El despido disciplinario declarado procedente no da derecho a indemnización. Sí te corresponde el finiquito y puedes cobrar el paro si cumples los requisitos.');return;}
if(ti=='o'){d=Math.min(20*m/12,365);tope=20*m/12>365?' (aplicado el tope de 12 mensualidades)':'';det='20 días × '+nf(m/12,2)+' años';}
else if(ti=='t'){d=12*m/12;det='12 días × '+nf(m/12,2)+' años';}
else{const R=new Date(2012,1,12);if(a<R){const pre=new Date(2012,1,11),m1=meses(a,b<pre?b:pre),m2=b>=R?meses(R,b):0,d1=45*m1/12,d2=33*m2/12;
det='45 días × '+nf(m1/12,2)+' años (hasta el 11/02/2012) + 33 días × '+nf(m2/12,2)+' años';
if(d1>720){d=Math.min(d1,42*365/12);tope=' (el tiempo anterior a 2012 ya supera los 720 días: se mantiene, con un máximo de 42 mensualidades)';}else{d=Math.min(d1+d2,720);tope=d1+d2>720?' (aplicado el tope de 720 días)':'';}}
else{d=Math.min(33*m/12,730);tope=33*m/12>730?' (aplicado el tope de 24 mensualidades)':'';det='33 días × '+nf(m/12,2)+' años';}}
const imp=d*sd;
show('r','Indemnización:<b class="big">'+eur(imp)+'</b>'+ant+'<br>Días de indemnización: <b>'+nf(d,2)+'</b> = '+det+tope+'<br>Equivale a '+nf(imp/mens,1)+' mensualidades. Exenta de IRPF hasta lo que marca la ley'+(imp>180000?', con un máximo de 180.000 €':'')+'.');}
calc();"""))

# --- Finiquito: salario pendiente, vacaciones no disfrutadas (art. 38 ET), parte proporcional de pagas extra (art. 31 ET) y descuento de preaviso ---
S['tools'].insert(4, ("calcular-finiquito", "Calculadora de finiquito", "Salario pendiente, vacaciones no disfrutadas y parte de las pagas extra al dejar la empresa.", ""))
S['aff']["calcular-finiquito"] = amz("estatuto de los trabajadores 2026", "Estatuto de los Trabajadores") + amz("archivador documentos", "Archivadores para nóminas y papeles")
P.append(("calcular-finiquito", "Calcular finiquito 2026: vacaciones y pagas extra | CalculadoraDías",
"Calcula tu finiquito con tus fechas exactas: días del último mes, vacaciones no disfrutadas, parte proporcional de las pagas extra y descuento por no avisar con 15 días. Baja voluntaria, despido o fin de contrato.",
"""<p class="lead">Pon tu fecha de alta, el último día que trabajas y tu sueldo. Te desglosamos lo que tiene que pagarte la empresa al irte: el finiquito, que te corresponde siempre, te despidan o te vayas tú.</p>
<div class="card"><div class="row"><div><label for="al">Fecha de alta en la empresa</label><input id="al" type="date" value="2024-03-01"></div>
<div><label for="fb">Último día trabajado (fecha de baja)</label><input id="fb" type="date" value="2026-12-15" onchange="dia()"></div>
<div><label for="sm">Salario bruto mensual sin pagas extra (€)</label><input id="sm" inputmode="decimal" value="1800"></div>
<div><label for="pg">Pagas extra</label><select id="pg"><option value="a">2 pagas · devengo anual</option><option value="s">2 pagas · devengo semestral</option><option value="p">Prorrateadas en la nómina</option></select></div>
<div><label for="pe">Importe de cada paga extra completa (€)</label><input id="pe" inputmode="decimal" value="1800"></div>
<div><label for="dm">Días del último mes sin cobrar</label><input id="dm" inputmode="numeric" value="15"></div>
<div><label for="vu">Tus vacaciones se cuentan en</label><select id="vu"><option value="n">Días naturales</option><option value="l">Días laborables</option></select></div>
<div><label for="va">Vacaciones al año</label><input id="va" inputmode="numeric" value="30"></div>
<div><label for="vd">Vacaciones ya disfrutadas este año</label><input id="vd" inputmode="numeric" value="22"></div>
<div><label for="pa">Días de preaviso que no has dado (solo baja voluntaria)</label><input id="pa" inputmode="numeric" value="0"></div>
<div><label for="ir">Retención de IRPF de tu nómina (%)</label><input id="ir" inputmode="decimal" value="15"></div></div>
<label style="font-weight:400"><input type="checkbox" id="yc" onchange="calc()" style="width:auto;margin-right:8px">Ya he cobrado la paga de Navidad de este año</label>
<button onclick="calc()">Calcular finiquito</button><div class="res" id="r" aria-live="polite"></div></div>
<p class="note">Si tu convenio cuenta las vacaciones en días laborables (normalmente 22 al año), elige «días laborables»: cada día laborable vale más que uno natural porque los fines de semana no cuentan. Si tienes una tercera paga (de beneficios), súmala aparte con la misma regla que las otras.</p>
<h2>Qué incluye el finiquito</h2><ul><li><b>Salario de los días trabajados</b> en el último mes que aún no has cobrado: salario mensual ÷ 30 × días.</li>
<li><b>Vacaciones generadas y no disfrutadas</b>: se generan en proporción a lo trabajado en el año (días trabajados ÷ 365 × días de vacaciones). Las que no hayas disfrutado se pagan, ya que el <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430#a38" rel="noopener" target="_blank">artículo 38 del Estatuto</a> solo prohíbe cambiarlas por dinero mientras sigues en la empresa. Si disfrutaste más de las generadas, la empresa puede descontarlas.</li>
<li><b>Parte proporcional de las pagas extra</b> generadas desde la última que cobraste (art. 31 ET). Con devengo anual, la de Navidad se genera de enero a diciembre y la de verano de julio a junio; con devengo semestral, la de verano de enero a junio y la de Navidad de julio a diciembre. Si están prorrateadas, ya las has cobrado cada mes.</li>
<li><b>Descuento por falta de preaviso</b>: si te vas por tu cuenta sin avisar con la antelación de tu convenio (lo más habitual son 15 días), la empresa puede descontar un día de salario por cada día que falte.</li></ul>
<p><b>Ejemplo:</b> alta el 1 de marzo de 2024, baja el 15 de diciembre de 2026, 1.800 € al mes y dos pagas de 1.800 € con devengo anual, 22 días de vacaciones disfrutados. Te corresponden 900 € de los 15 días de diciembre, 6,7 días de vacaciones (401 €), 1.721 € de la paga de Navidad (349 de 365 días) y 828 € de la de verano (168 días desde el 1 de julio): <b>3.851 € brutos</b>.</p>
<h2>Finiquito e indemnización no son lo mismo</h2><p>El finiquito es lo que la empresa te debe por el trabajo ya hecho y se cobra en <b>todos los casos</b>, también en una baja voluntaria. La indemnización solo existe en algunos despidos y al terminar un contrato temporal: calcúlala con la <a href="indemnizacion-despido.html">calculadora de indemnización por despido</a>. El finiquito tributa en el IRPF y cotiza a la Seguridad Social como una nómina más. Antes de firmarlo, comprueba las cuentas: puedes firmar añadiendo «no conforme» y, si es por despido, pedir que esté presente un representante de los trabajadores (art. 49.2 ET). Para reclamar un despido tienes 20 días hábiles: calcula la fecha con <a href="sumar-dias.html">sumar días hábiles</a>.</p>
<p>Revisa también la <a href="paga-extra-navidad.html">paga extra de Navidad</a> con su periodo de devengo o los <a href="calculadora-vacaciones.html">días de vacaciones que te corresponden</a>.</p>""",
[("¿Cuánto me corresponde de finiquito si me voy de la empresa?", "El salario de los días trabajados del último mes, las vacaciones generadas y no disfrutadas y la parte proporcional de las pagas extra que no hayas cobrado. Si no avisas con el preaviso del convenio, te pueden descontar los días que falten."),
 ("¿Se cobra finiquito en una baja voluntaria?", "Sí. El finiquito se paga siempre que termina el contrato, sea por despido, por fin de contrato o porque te vas tú. Lo que no hay en una baja voluntaria es indemnización ni, por lo general, derecho a paro."),
 ("¿Cómo se calculan las vacaciones no disfrutadas en el finiquito?", "Se multiplican los días trabajados en el año por los días de vacaciones anuales y se divide entre 365. A esa cifra se le restan los días ya disfrutados y cada día pendiente se paga a tu salario diario (salario mensual ÷ 30)."),
 ("¿Cuánto tarda la empresa en pagar el finiquito?", "El Estatuto no fija un plazo concreto: lo habitual es pagarlo el último día de trabajo o con la nómina de ese mes, y muchos convenios lo concretan. Si se retrasa, puedes reclamarlo con un 10 % de interés por mora (artículo 29.3 del Estatuto). Tienes un año para reclamar las cantidades que te deban."),
 ("¿Cuántos días de preaviso hay que dar al dejar un trabajo?", "Los que diga tu convenio o tu contrato; lo más habitual son 15 días naturales. Si no das el preaviso, la empresa puede descontarte del finiquito un día de salario por cada día que falte.")],
"Calculadora de finiquito",
DATEJS + """function per(t,b){const y=b.getFullYear(),m=b.getMonth();
if(t=='a')return [['Paga de Navidad',new Date(y,0,1),new Date(y,11,31)],['Paga de verano',m<6?new Date(y-1,6,1):new Date(y,6,1),m<6?new Date(y,5,30):new Date(y+1,5,30)]];
return m<6?[['Paga de verano',new Date(y,0,1),new Date(y,5,30)]]:[['Paga de Navidad',new Date(y,6,1),new Date(y,11,31)]];}
function dia(){const b=pd('fb');if(b){const ul=new Date(b.getFullYear(),b.getMonth()+1,0).getDate();document.getElementById('dm').value=b.getDate()==ul?30:Math.min(30,b.getDate());document.getElementById('yc').checked=b.getMonth()==11&&b.getDate()>=22;}calc();}
function calc(){const al=pd('al'),b=pd('fb'),sm=v('sm'),t=document.getElementById('pg').value,pe=v('pe'),irp=v('ir');
if(!al||!b||b<al||sm<=0){show('r','Revisa las fechas y el salario.');return;}
const sd=sm/30,dm=Math.min(30,Math.max(0,v('dm'))),sdm=t=='p'?(sm+pe*2/12)/30:sd,sal=sdm*dm;
const y0=new Date(b.getFullYear(),0,1),ini=al>y0?al:y0,dy=diff(ini,b)+1,dya=diff(y0,new Date(b.getFullYear(),11,31))+1;
const lab=document.getElementById('vu').value=='l',va=v('va'),gen=dy/dya*va,pend=gen-v('vd'),vac=va>0?pend*(lab?30/va:1)*sd:0,ud=lab?' laborables':'',fe=x=>x.toLocaleDateString('es-ES',{day:'numeric',month:'short',year:'numeric'});
const fila=(c,d,x)=>'<tr><td>'+c+'<br><span class="note">'+d+'</span></td><td style="text-align:right;white-space:nowrap"><b>'+eur(x)+'</b></td></tr>';
let rows=fila('Salario del último mes',nf(dm,0)+' días × '+eur(sdm)+(t=='p'?' (con la parte de pagas)':''),sal);
rows+=fila(pend>=0?'Vacaciones no disfrutadas':'Vacaciones disfrutadas de más',nf(Math.abs(pend),1)+' días'+ud+' (generadas '+nf(gen,1)+' de '+nf(va,0)+')'+(lab?' · cada uno vale '+eur(sd*30/va):''),vac);
let pag=0;if(t!='p'){per(t,b).filter(p=>!(document.getElementById('yc').checked&&p[0]=='Paga de Navidad')).forEach(p=>{const i=al>p[1]?al:p[1],d=Math.max(0,diff(i,b)+1),tot=diff(p[1],p[2])+1,x=pe*d/tot;pag+=x;rows+=fila(p[0],d+' de '+tot+' días, desde el '+fe(i),x);});}
const pre=sd*Math.max(0,v('pa'));if(pre>0)rows+=fila('Descuento por falta de preaviso',nf(v('pa'),0)+' días × '+eur(sd),-pre);
const br=sal+vac+pag-pre,ss=Math.max(0,sal+vac-pre)*0.065,ne=Math.max(0,br*(1-irp/100)-ss);
let h='Finiquito (bruto):<b class="big">'+eur(br)+'</b>Neto aproximado: <b>'+eur(ne)+'</b> (IRPF del '+nf(irp,1)+' % y 6,5 % de Seguridad Social sobre salario y vacaciones)';
h+='<table style="margin-top:10px">'+rows+'<tr><th>Total bruto</th><th style="text-align:right">'+eur(br)+'</th></tr></table>';
if(document.getElementById('yc').checked&&t!='p')h+='<span class="note">No contamos la paga de Navidad porque ya la has cobrado.</span><br>';
if(t=='p')h+='<span class="note">Pagas prorrateadas: ya las has cobrado cada mes, solo queda la parte del último mes incluida en el salario.</span><br>';
h+='<button type="button" onclick="window.print()" style="width:auto;padding:9px 14px;margin:8px 0;font-size:.95rem">Imprimir o guardar en PDF</button><br>';
h+='<span class="note">La parte de las pagas extra no vuelve a cotizar: ya se cotizó repartida en cada nómina. Si te despiden, la indemnización va aparte.</span>';
show('r',h);}
document.querySelectorAll('.card input,.card select').forEach(e=>e.addEventListener(e.tagName=='SELECT'||e.type=='checkbox'||e.type=='date'?'change':'input',()=>calc()));
calc();"""))

# --- Puentes 2027: planificador de vacaciones con los festivos oficiales del BOE (usa FEST27, CCAA e ISLAS) ---
S['tools'].insert(1, ("puentes-2027", "Puentes 2027: aprovecha tus vacaciones", "Qué días pedir para encadenar el máximo de descanso con los festivos de tu comunidad.", "Puentes 2027"))
S['aff']["puentes-2027"] = amz("calendario pared 2027", "Calendarios 2027") + amz("maleta cabina", "Maletas de cabina") + ext("https://www.booking.com/", "Buscar alojamiento para tu escapada")
_opts2 = "".join(f'<option value="{c}"{" selected" if c=="MD" else ""}>{n}</option>' for c, n in CCAA)
P.append(("puentes-2027", "Puentes 2027: qué días pedir para tener más vacaciones | CalculadoraDías",
"Puentes 2027 en tu comunidad y planificador de vacaciones: dinos cuántos días tienes y te decimos qué fechas pedir para encadenar el máximo de días libres. Festivos oficiales del BOE.",
"""<p class="lead">Elige tu comunidad y cuántos días de vacaciones quieres usar. Te decimos qué días pedir en 2027 para juntarlos con fines de semana y festivos y conseguir el máximo de días libres seguidos.</p>
<div class="card"><div class="row"><div><label for="cc">Comunidad autónoma</label><select id="cc">""" + _opts2 + """</select></div>
<div><label for="n">Días de vacaciones (laborables) a usar</label><input id="n" inputmode="numeric" value="10"></div>
<div><label for="mx">Días como máximo por escapada</label><select id="mx"><option value="99">Sin límite</option><option value="5" selected>Hasta 5 días (una semana)</option><option value="3">Hasta 3 días (puentes cortos)</option><option value="1">Solo 1 día (puentes)</option></select></div>
<div id="isw" style="display:none"><label for="is">Isla</label><select id="is">""" + _isl + """</select></div></div>
<label for="lo">Tus festivos locales (opcional, dd/mm)</label><input id="lo" placeholder="15/05, 09/11">
<div class="res" id="r" aria-live="polite"></div></div>
<h2>Cómo elegimos los días</h2><p>Para cada combinación posible de fines de semana y festivos de tu comunidad, contamos cuántos días laborables tendrías que pedir para unirlos y cuántos días libres seguidos conseguirías. Después elegimos el reparto que, con los días que indiques, te da <b>más días de descanso en total</b>. Los días que pides son siempre de lunes a viernes no festivos: sábados, domingos y festivos no gastan vacaciones.</p>
<p><b>Ejemplo en la Comunidad de Madrid:</b> el 12 de octubre de 2027 cae en martes. Pidiendo solo el lunes 11 tienes 4 días libres (del sábado 9 al martes 12). Y en diciembre, con el 6 en lunes y el 8 en miércoles, pidiendo el martes 7 enlazas cinco días, del sábado 4 al miércoles 8; si añades el jueves 9 y el viernes 10, son 9 días seguidos gastando solo 3.</p>
<h2>Los puentes de 2027 en toda España</h2><ul><li><b>Año Nuevo y Reyes:</b> el 1 de enero es viernes (fin de semana de tres días) y el 6 de enero, miércoles.</li>
<li><b>Semana Santa:</b> Jueves Santo 25 de marzo (en casi todas las comunidades) y Viernes Santo 26. En las comunidades con Lunes de Pascua (29 de marzo) son cinco días seguidos sin pedir ninguno.</li>
<li><b>1 de mayo:</b> cae en sábado, así que no hay puente nacional.</li>
<li><b>15 de agosto:</b> es domingo. Seis comunidades lo pasan al lunes 16.</li>
<li><b>12 de octubre:</b> martes; puente pidiendo el lunes 11.</li>
<li><b>1 de noviembre:</b> lunes; fin de semana largo de tres días.</li>
<li><b>Constitución e Inmaculada:</b> lunes 6 y miércoles 8 de diciembre: el gran puente del año.</li>
<li><b>Navidad:</b> el 25 de diciembre es sábado. Algunas comunidades podrían trasladarlo; consulta el <a href="calendario-laboral-2027.html">calendario laboral 2027</a> de la tuya.</li></ul>
<p class="note">Fuente de los festivos: Resolución de 8 de octubre de 2026 de la Dirección General de Trabajo (BOE-A-2026-21254). Los festivos locales los fija cada ayuntamiento: añádelos arriba. Si trabajas a turnos o en fin de semana, tu cuadrante manda. Las vacaciones se fijan de común acuerdo con la empresa: pídelas con antelación. ¿Cuántos días te corresponden? Calcúlalo con la <a href="calculadora-vacaciones.html">calculadora de vacaciones</a>.</p>""",
[("¿Cuáles son los mejores puentes de 2027?", "En casi toda España: el 12 de octubre (martes), pidiendo el lunes 11, y el puente de diciembre, con el 6 en lunes y el 8 en miércoles: pidiendo el martes 7 tienes cinco días libres, y con tres días de vacaciones, nueve. Además, Semana Santa (25 y 26 de marzo) y el 1 de noviembre, que cae en lunes."),
 ("¿Cuántos días de vacaciones tengo al año?", "El Estatuto de los Trabajadores fija un mínimo de 30 días naturales al año, que suelen equivaler a 22 días laborables. Tu convenio puede mejorarlo."),
 ("¿Los festivos que caen en sábado se recuperan?", "No automáticamente. Si un festivo nacional cae en domingo, las comunidades pueden trasladarlo al lunes; los que caen en sábado, como el 1 de mayo y el 25 de diciembre de 2027, normalmente se pierden salvo que tu comunidad decida otra cosa."),
 ("¿Puedo pedir solo días sueltos para hacer puente?", "Sí, si tu empresa lo acepta. Las vacaciones se acuerdan con la empresa; muchos convenios permiten fraccionarlas, aunque a veces exigen un periodo mínimo seguido. Revisa tu convenio.")],
"Puentes 2027: qué días pedir de vacaciones",
"""const F=""" + _fj + """;
const D0=new Date(2027,0,1),ND=365,k2=d=>d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');
const DAY=i=>new Date(2027,0,1+i),fc=d=>d.toLocaleDateString('es-ES',{weekday:'short',day:'numeric',month:'short'});
function plan(cc,isla,locs,N,MX){const fs={};F.forEach(f=>{if(f[2].includes(cc))fs[f[0]]=f[1];});if(cc=='CN'&&isla){const p=isla.split('|');fs[p[0]]='Fiesta insular de '+p[1];}locs.forEach(k=>{if(!fs[k])fs[k]='Festivo local';});
const off=[];for(let i=0;i<ND;i++){const d=DAY(i),w=d.getDay();off.push(w==0||w==6||!!fs[k2(d)]);}
const B=[];for(let i=0;i<ND;i++){if(off[i]&&(i==0||!off[i-1])){let j=i;while(j+1<ND&&off[j+1])j++;B.push([i,j]);}}
const m=B.length;
const C=[];for(let a=0;a<m;a++){C[a]=[];let c=0;C[a][a]=0;for(let b=a+1;b<m;b++){c+=B[b][0]-B[b-1][1]-1;C[a][b]=c;}}
const W=[];for(let a=0;a<m;a++)for(let b=a+1;b<m;b++){const c=C[a][b];if(c>MX)break;if(c>=1&&c<=N)W.push([a,b,c,B[b][1]-B[a][0]+1]);}
const f=[],ch=[];for(let i=0;i<=m;i++){f.push(new Array(N+1).fill(0));ch.push(new Array(N+1).fill(null));}
for(let i=1;i<=m;i++)for(let n=0;n<=N;n++){f[i][n]=f[i-1][n];ch[i][n]=null;W.forEach((w,x)=>{if(w[1]==i-1&&w[2]<=n){const val=f[w[0]][n-w[2]]+w[3]+w[3]*w[3]/1e4;if(val>f[i][n]){f[i][n]=val;ch[i][n]=x;}}});}
const sel=[];let i=m,n=N;while(i>0){const x=ch[i][n];if(x===null){i--;}else{const w=W[x];sel.unshift(w);n-=w[2];i=w[0];}}
const pide=w=>{const r=[];for(let t=B[w[0]][0];t<=B[w[1]][1];t++)if(!off[t])r.push(DAY(t));return r;};
const top=W.filter(w=>w[2]<=2).map(w=>[w,w[3]/w[2]]).sort((p,q)=>q[1]-p[1]||q[0][3]-p[0][3]).slice(0,8).map(p=>p[0]);
return {fs,sel,top,pide,B,tot:sel.reduce((s,w)=>s+w[3],0),used:sel.reduce((s,w)=>s+w[2],0)};}
function calc(){const cc=document.getElementById('cc').value;document.getElementById('isw').style.display=cc=='CN'?'block':'none';
const locs=[];document.getElementById('lo').value.split(/[,;\\s]+/).forEach(x=>{const mm=x.match(/^(\\d{1,2})[\\/.-](\\d{1,2})$/);if(mm)locs.push('2027-'+mm[2].padStart(2,'0')+'-'+mm[1].padStart(2,'0'));});
const N=Math.max(0,Math.min(40,Math.round(v('n')))),MX=+document.getElementById('mx').value;if(N<1){show('r','Escribe cuántos días de vacaciones quieres usar.');return;}
const p=plan(cc,document.getElementById('is').value,locs,N,MX);
if(!p.sel.length){show('r','Con estos datos no encontramos ninguna combinación. Prueba con más días o sin límite por escapada.');return;}
let h='Con <b>'+p.used+' días</b> de vacaciones consigues:<b class="big">'+p.tot+' días libres</b>en '+p.sel.length+' '+(p.sel.length==1?'escapada':'escapadas')+(p.used<N?' (te sobran '+(N-p.used)+' días: úsalos cuando quieras)':'')+'.';
h+='<table style="margin-top:10px;font-size:.92rem"><tr><th>Descansas</th><th>Días libres</th><th>Pide</th></tr>'+p.sel.map(w=>{const a=DAY(p.B[w[0]][0]),b=DAY(p.B[w[1]][1]);return '<tr><td>'+fc(a)+' – '+fc(b)+'</td><td><b>'+w[3]+'</b></td><td>'+p.pide(w).map(fc).join(', ')+'</td></tr>';}).join('')+'</table>';
if(p.top.length)h+='<h3 style="margin-bottom:4px">Mejores puentes pidiendo 1 o 2 días</h3><ul style="margin-top:4px">'+p.top.map(w=>'<li>'+fc(DAY(p.B[w[0]][0]))+' – '+fc(DAY(p.B[w[1]][1]))+': <b>'+w[3]+' días</b> pidiendo '+p.pide(w).map(fc).join(' y ')+'</li>').join('')+'</ul>';
show('r',h);}
document.querySelectorAll('.card input,.card select').forEach(e=>e.addEventListener(e.tagName=='SELECT'?'change':'input',()=>calc()));
calc();"""))

# --- Plazo de devolución y garantía: desistimiento de 14 días, garantía de 3 años (RDL 7/2021) ---
S['tools'].insert(2, ("plazo-devolucion-garantia", "Plazo de devolución y garantía", "Hasta qué día puedes devolver una compra online y cuándo termina la garantía de 3 años.", "Devoluciones"))
S['aff']["plazo-devolucion-garantia"] = amz("archivador tickets facturas", "Archivadores para tickets y garantías") + amz("cinta embalar dispensador", "Cinta y cajas para devoluciones") + ext("https://www.consumo.gob.es/", "Ministerio de Consumo: tus derechos")
P.append(("plazo-devolucion-garantia", "Plazo de devolución de compras online y garantía: calculadora | CalculadoraDías",
"Plazo de devolución y garantía de tu compra: pon la fecha en que la recibiste y te decimos hasta qué día puedes devolverla (14 días online) y cuándo vence la garantía de 3 años.",
"""<p class="lead">Pon cuándo recibiste el pedido o compraste en la tienda y te decimos hasta qué día puedes devolverlo, cuánto tiempo tiene la tienda para reembolsarte y hasta cuándo te cubre la garantía legal. Ideal para los regalos de Black Friday, Navidad y Reyes.</p>
<div class="card"><div class="row"><div><label for="t">Dónde compraste</label><select id="t"><option value="o">Online, por teléfono o a distancia</option><option value="f">En tienda física</option><option value="x">Fuera del establecimiento (a domicilio, excursión…)</option></select></div>
<div><label for="g">Qué compraste</label><select id="g"><option value="n">Producto nuevo</option><option value="s">Producto de segunda mano</option><option value="d">Contenido o servicio digital</option></select></div>
<div><label for="a">Fecha de entrega o de compra</label><input id="a" type="date" data-today></div>
<div><label for="b">La tienda acepta devoluciones hasta (opcional)</label><input id="b" type="date"></div></div>
<p class="note">Si la tienda anuncia un plazo ampliado (muchas lo alargan en Navidad hasta finales de enero), ponlo en el último campo: ese compromiso también obliga al vendedor.</p>
<div class="res" id="r" aria-live="polite"></div></div>
<h2>Cuánto tiempo tienes para devolver una compra</h2><p>En las compras <b>online, por teléfono o fuera de la tienda</b>, la ley te da <b>14 días naturales</b> para desistir sin dar explicaciones (artículo 102 y siguientes de la Ley General para la Defensa de los Consumidores). Se cuentan desde el día en que recibes el producto, sin incluir ese día. Si la tienda no te informó de este derecho, el plazo se alarga <b>12 meses</b> más. Tras avisar de que desistes, tienes otros 14 días para enviar el producto, y la tienda debe devolverte el dinero, incluidos los gastos de envío estándar, en un máximo de 14 días desde tu aviso (puede esperar a recibir el producto o la prueba de que lo has enviado).</p>
<p>En una <b>tienda física</b> no hay obligación legal de aceptar devoluciones si el producto está bien: depende de la política de la tienda. Pero si la anuncia (en el ticket, en carteles o en su web), está obligada a cumplirla, también en rebajas, salvo que avise claramente de lo contrario.</p>
<p><b>Ejemplo:</b> si recibes un pedido el viernes 27 de noviembre de 2026, puedes desistir hasta el viernes 11 de diciembre. Si avisas ese día, tienes hasta el 25 de diciembre para enviarlo y la tienda debe reembolsarte como tarde también el 25 de diciembre. La garantía de ese producto nuevo dura hasta el 27 de noviembre de 2029.</p>
<h2>La garantía legal: 3 años</h2><table><tr><th>Producto</th><th>Garantía legal</th></tr><tr><td>Nuevo, comprado desde 2022</td><td>3 años desde la entrega</td></tr><tr><td>Segunda mano</td><td>Se puede pactar menos, pero nunca menos de 1 año</td></tr><tr><td>Contenido o servicio digital</td><td>2 años (o lo que dure el suministro)</td></tr></table>
<p>Si el producto falla en los <b>2 primeros años</b>, se presume que el defecto ya existía y no tienes que demostrarlo: la tienda debe repararlo o cambiarlo gratis y, si no es posible, rebajar el precio o devolverte el dinero. A partir del tercer año sigues cubierto, pero puede pedirte que acredites que el fallo es de origen. Además, el fabricante debe tener repuestos durante 10 años desde que deja de fabricar el producto. Fuente: Real Decreto-ley 7/2021 y portal del <a href="https://portal-cec.consumo.gob.es/es/informacion-general/temas-de-consumo/garantias" rel="noopener" target="_blank">Centro Europeo del Consumidor (Ministerio de Consumo)</a>.</p>
<p>¿Te ha tocado devolver un regalo de Reyes? Mira <a href="que-dia-de-la-semana.html">qué día de la semana cae</a> el último día del plazo, o calcula cualquier otro plazo con <a href="sumar-dias.html">sumar días a una fecha</a>.</p>""",
[("¿Cuántos días tengo para devolver una compra online?", "14 días naturales desde que recibes el producto, sin dar explicaciones. Si la tienda no te informó de ese derecho, el plazo se amplía 12 meses. Algunas tiendas dan más días por su cuenta, sobre todo en Navidad."),
 ("¿Una tienda física está obligada a devolverme el dinero?", "No, si el producto no tiene ningún defecto. Solo si la tienda lo ofrece en su política de devoluciones; si lo anuncia, debe cumplirlo. Si el producto está defectuoso, sí te cubre la garantía legal."),
 ("¿Cuánto dura la garantía de un producto en España?", "3 años para productos nuevos comprados desde el 1 de enero de 2022, 2 años para contenidos y servicios digitales y un mínimo de 1 año pactado para productos de segunda mano."),
 ("¿Desde cuándo se cuenta el plazo de devolución?", "Desde el día siguiente a la entrega del producto. Si el pedido llega en varios envíos, desde que recibes el último.")],
"Calculadora del plazo de devolución y la garantía",
DATEJS + """const add=(d,n)=>{const x=new Date(d);x.setDate(x.getDate()+n);return x;},addY=(d,n)=>{const x=new Date(d.getFullYear()+n,d.getMonth(),d.getDate());if(x.getDate()!=d.getDate())x.setDate(0);return x;};
const lab=d=>{const x=new Date(d);while(x.getDay()==0||x.getDay()==6)x.setDate(x.getDate()+1);return x;};
function fila(n,d,x){const f=diff(today,d);return '<tr><td>'+n+'</td><td><b>'+d.toLocaleDateString('es-ES',{weekday:'short',day:'numeric',month:'short',year:'numeric'})+'</b>'+(x?'<br><span class="note">'+x+'</span>':'')+'</td><td>'+(f<0?'vencido':f==0?'hoy':'faltan '+nf(f,0)+' días')+'</td></tr>';}
function calc(){const a=pd('a'),b=pd('b'),t=document.getElementById('t').value,g=document.getElementById('g').value;if(!a){show('r','Escribe la fecha de entrega o de compra.');return;}
let h='',R=[];if(t!='f'){const e=add(a,14),e2=lab(e),ok=diff(today,e)>=0;
h='Puedes devolverlo (desistir) hasta el:<b class="big">'+fmt(e)+'</b>'+(ok?'Te quedan <b>'+nf(diff(today,e),0)+' días</b> para avisar a la tienda.':'El plazo legal de 14 días ya ha pasado'+(b&&diff(today,b)>=0?', pero la tienda te deja devolverlo hasta el '+fmt(b)+'.':'.'));
if(e2-e)h+='<br>El día 14 cae en fin de semana: según las normas europeas de cómputo de plazos pasa al '+fmt(e2)+', pero para ir sobre seguro avisa antes.';
R.push(fila('Último día para desistir (14 días)',e,'Avisa por escrito: correo, formulario de la web o el modelo de desistimiento.'));
const base=ok?today:e;R.push(fila('Enviar el producto si desistes '+(ok?'hoy':'el último día'),add(base,14),'14 días desde que avisas.'));R.push(fila('Plazo máximo de reembolso',add(base,14),'14 días desde tu aviso, incluido el envío estándar.'));
R.push(fila('Si no te informaron del derecho a desistir',addY(e,1),'El plazo se amplía 12 meses.'));}
else h='En tienda física, la devolución depende de la política de la tienda.<b class="big">'+(b?'Hasta el '+fmt(b):'Mira el ticket')+'</b>'+(b?(diff(today,b)>=0?'Te quedan <b>'+nf(diff(today,b),0)+' días</b>.':'Ese plazo ya ha pasado.'):'Si no anuncia política de devoluciones, solo está obligada a responder por defectos (garantía).');
if(b&&t!='f')R.push(fila('Plazo que ofrece la tienda',b,'Compromiso comercial: también te obliga a cumplirlo a la tienda.'));if(b&&t=='f')R.push(fila('Plazo que ofrece la tienda',b,''));
if(g=='n'){R.push(fila('Fin de la presunción de defecto de origen',addY(a,2),'Hasta aquí no tienes que demostrar que el fallo es de fábrica.'));R.push(fila('Fin de la garantía legal (3 años)',addY(a,3),''));}
else if(g=='s')R.push(fila('Garantía mínima pactable (1 año)',addY(a,1),'Si no pactasteis nada por escrito, se aplican los 3 años.'));
else R.push(fila('Fin de la garantía (2 años)',addY(a,2),'O lo que dure el suministro, si es más.'));
show('r',h+'<table style="margin-top:12px;font-size:.92rem"><tr><th>Qué vence</th><th>Fecha</th><th>Cuándo</th></tr>'+R.join('')+'</table>');}
document.querySelectorAll('.card input,.card select').forEach(e=>e.addEventListener(e.tagName=='SELECT'?'change':'input',()=>calc()));
calc();"""))

# --- Cuánto paro me corresponde: duración según los días cotizados (art. 269 LGSS) y fecha de fin ---
S['tools'].insert(5, ("calcular-paro", "¿Cuánto paro me corresponde?", "Días de prestación por desempleo según lo cotizado en los últimos 6 años y fecha en que se acaba.", "Paro"))
S['aff']["calcular-paro"] = amz("libro entrevista de trabajo", "Libros para preparar entrevistas") + amz("agenda 2027", "Agendas 2027")
P.append(("calcular-paro", "¿Cuánto paro me corresponde? Calculadora de días y fecha de fin | CalculadoraDías",
"Calcula cuánto paro te corresponde según los días cotizados en los últimos 6 años (de 120 a 720 días), hasta qué fecha lo cobrarás y cuánto te falta para el siguiente tramo.",
"""<p class="lead">Pon lo que has trabajado en los últimos 6 años y el día en que empiezas a cobrar. Te decimos cuántos días de paro te corresponden, hasta qué fecha y cuánto te falta para el siguiente tramo.</p>
<div class="card"><div class="row"><div><label for="an">Años trabajados en los últimos 6 años</label><input id="an" inputmode="numeric" value="3"></div>
<div><label for="me">Meses (además de los años)</label><input id="me" inputmode="numeric" value="4"></div>
<div><label for="dc">O días cotizados exactos (opcional)</label><input id="dc" inputmode="numeric" value="" placeholder="Del informe de vida laboral"></div>
<div><label for="fi">Primer día de paro</label><input id="fi" type="date" data-today></div>
<div><label for="br">Base reguladora mensual (€, opcional)</label><input id="br" inputmode="decimal" value="" placeholder="Media de tus bases de cotización"></div></div>
<button onclick="calc()">Calcular mi paro</button><div class="res" id="r" aria-live="polite"></div></div>
<p class="note">Cuenta solo lo cotizado por desempleo en los 6 años anteriores (contratos por cuenta ajena) que no hayas usado ya para cobrar otro paro. Los días exactos los tienes en tu informe de vida laboral de la Seguridad Social. Resultado orientativo: el SEPE es quien reconoce la prestación.</p>
<h2>Tabla de duración del paro</h2><p>La duración de la prestación contributiva la fija el artículo 269 de la Ley General de la Seguridad Social según los días cotizados en los últimos seis años:</p>
<table><tr><th>Días cotizados</th><th>Días de paro</th><th>Meses</th></tr>
<tr><td>De 360 a 539</td><td>120</td><td>4</td></tr><tr><td>De 540 a 719</td><td>180</td><td>6</td></tr><tr><td>De 720 a 899</td><td>240</td><td>8</td></tr>
<tr><td>De 900 a 1.079</td><td>300</td><td>10</td></tr><tr><td>De 1.080 a 1.259</td><td>360</td><td>12</td></tr><tr><td>De 1.260 a 1.439</td><td>420</td><td>14</td></tr>
<tr><td>De 1.440 a 1.619</td><td>480</td><td>16</td></tr><tr><td>De 1.620 a 1.799</td><td>540</td><td>18</td></tr><tr><td>De 1.800 a 1.979</td><td>600</td><td>20</td></tr>
<tr><td>De 1.980 a 2.159</td><td>660</td><td>22</td></tr><tr><td>Desde 2.160</td><td>720</td><td>24 (máximo)</td></tr></table>
<p>En la práctica: por cada año cotizado tienes unos 4 meses de paro, hasta un máximo de 2 años de prestación con 6 años cotizados. Los días que superan el mínimo de tu tramo no dan más paro: con 539 días cotizados cobras lo mismo que con 360.</p>
<p><b>Ejemplo:</b> has trabajado 3 años y 4 meses en los últimos 6 años, unos 1.215 días. Estás en el tramo de 1.080 a 1.259 días: te corresponden <b>360 días de paro</b> (12 meses). Si empiezas a cobrar el 1 de diciembre de 2026, el último día de prestación es el 25 de noviembre de 2027. Con 45 días más cotizados habrías llegado al tramo de 420 días.</p>
<h2>Cuánto se cobra</h2><p>La cuantía se calcula sobre la <b>base reguladora</b>: la media de tus bases de cotización por desempleo de los últimos 180 días trabajados. Los primeros 180 días de paro cobras el <b>70 %</b> de esa base, y a partir del día 181 el porcentaje baja. Además, el SEPE aplica unos importes mínimos y máximos que dependen del IPREM y de si tienes hijos a cargo, y descuenta la cotización a la Seguridad Social y, si toca, el IRPF. Para el importe exacto usa el simulador del <a href="https://www.sepe.es/" rel="noopener" target="_blank">SEPE</a>.</p>
<h2>Plazos que no debes pasar</h2><ul><li>Tienes <b>15 días hábiles</b> desde el despido o el fin del contrato para pedir el paro sin perder días de prestación.</li><li>Si en el finiquito te pagan vacaciones no disfrutadas, el paro empieza a contar cuando terminan esos días.</li><li>Antes, inscríbete como demandante de empleo en el servicio de empleo de tu comunidad.</li></ul>
<p>Calcula también tu <a href="calcular-finiquito.html">finiquito</a> y la <a href="indemnizacion-despido.html">indemnización por despido</a>, o cuenta los <a href="dias-habiles.html">días hábiles</a> que te quedan para pedir el paro.</p>""",
[("¿Cuánto paro me corresponde por año trabajado?", "Unos 4 meses por cada año cotizado: con 1 año (360 días) cobras 120 días, con 2 años 240 días, con 3 años 360 días, y así hasta el máximo de 720 días (2 años) con 6 años o más cotizados."),
 ("¿Cuántos días tengo que haber trabajado para cobrar el paro?", "Al menos 360 días cotizados por desempleo en los 6 años anteriores, que no se hayan usado para otra prestación. Con menos, puede que tengas derecho al subsidio por desempleo: consúltalo en el SEPE."),
 ("¿Se pierden los días cotizados que sobran del tramo?", "No te dan más paro: la duración es la del tramo en el que caes. Por eso, si estás cerca del siguiente tramo, unos días más de trabajo pueden darte 2 meses más de prestación."),
 ("¿Cuándo tengo que pedir el paro?", "En los 15 días hábiles siguientes al despido o al fin del contrato. Si lo pides tarde, no lo pierdes, pero se descuentan de la prestación los días de retraso.")],
"¿Cuánto paro me corresponde?",
DATEJS + """const TR=[[360,120],[540,180],[720,240],[900,300],[1080,360],[1260,420],[1440,480],[1620,540],[1800,600],[1980,660],[2160,720]];
const fd=d=>d.toLocaleDateString('es-ES',{day:'numeric',month:'long',year:'numeric'});
function calc(){const dc=v('dc');let d=dc>0?Math.round(dc):Math.round(v('an')*365+v('me')*30);const fi=pd('fi')||today,br=v('br');
if(d>2190)d=2190;let k=-1;TR.forEach((t,i)=>{if(d>=t[0])k=i;});
if(k<0){show('r','Con <b>'+d+' días</b> cotizados aún no llegas a la prestación contributiva:<b class="big">Te faltan '+(360-d)+' días</b>Necesitas 360 días cotizados en los últimos 6 años. Mientras, pregunta en el SEPE si tienes derecho al subsidio por desempleo.');return;}
const p=TR[k][1],f=new Date(fi.getFullYear(),fi.getMonth(),fi.getDate()+p-1);
let h='Te corresponden:<b class="big">'+p+' días de paro ('+(p/30)+' meses)</b>Con '+d.toLocaleString('es-ES')+' días cotizados (tramo de '+TR[k][0].toLocaleString('es-ES')+(k<10?' a '+(TR[k+1][0]-1).toLocaleString('es-ES'):' o más')+')';
h+='<br>Cobrando desde el '+fd(fi)+', el último día de paro es el <b>'+fmt(f)+'</b>.';
if(k<10)h+='<br>Con <b>'+(TR[k+1][0]-d)+' días</b> más cotizados pasarías a '+TR[k+1][1]+' días de paro (2 meses más).';
if(br>0){const m=br*0.7,c=Math.min(180,p);h+='<br>Primeros '+c+' días: unos <b>'+eur(m)+' al mes</b> brutos (70 % de tu base reguladora), antes de aplicar los topes del SEPE.';}
show('r',h);}"""))

# --- Portada: accesos a lo más buscado en temporada (Navidad e invierno) ---
S['home_intro'] += '<nav class="share" aria-label="Lo más buscado estos días"><span>Lo más buscado estos días:</span><a href="premio-loteria-navidad.html">Lotería de Navidad</a><a href="puentes-2027.html">Puentes 2027</a><a href="calendario-laboral-2027.html">Calendario laboral 2027</a><a href="paga-extra-navidad.html">Paga extra</a><a href="cuantos-dias-faltan.html">Días para Navidad</a><a href="permiso-nacimiento.html">Permiso por nacimiento</a></nav>'

# --- Permiso por nacimiento 2026 (20 semanas desde el 26/11/2026, RDL 42/2026) ---
S['tools'].insert(3, ("permiso-nacimiento", "Permiso por nacimiento: fechas de tus 20 semanas", "Fin de las 6 semanas obligatorias, plazo de las semanas flexibles y de las semanas hasta los 8 años, con la ampliación de noviembre de 2026.", "Permiso nacimiento"))
S['aff']["permiso-nacimiento"] = amz("agenda bebe primer año", "Agendas del primer año del bebé") + amz("vigilabebes", "Vigilabebés") + amz("mochila portabebes ergonomica", "Mochilas portabebés")
P.append(("permiso-nacimiento", "Permiso por nacimiento 2026: calculadora de las 20 semanas | CalculadoraDías",
"Nuevo permiso por nacimiento de 20 semanas (34 monoparental) para nacidos desde el 26/11/2026: calcula el fin de las 6 obligatorias, los plazos y tu vuelta al trabajo.",
"""<p class="lead">Pon la fecha de nacimiento (o la prevista) y te decimos cuántas semanas te corresponden, hasta qué día van las 6 obligatorias, cuándo vuelves al trabajo si las coges seguidas y hasta cuándo puedes usar las semanas flexibles.</p>
<div class="card"><div class="row"><div><label for="a">Fecha de nacimiento (o prevista)</label><input id="a" type="date" data-today></div>
<div><label for="q">¿Quién lo disfruta?</label><select id="q"><option value="o">Progenitor distinto de la madre biológica</option><option value="m">Madre biológica</option></select></div>
<div><label for="an">Semanas antes del parto (solo madre biológica)</label><select id="an"><option value="0">Ninguna</option><option value="1">1 semana</option><option value="2">2 semanas</option><option value="3">3 semanas</option><option value="4">4 semanas</option></select></div>
<div><label for="ex">Semanas extra (parto múltiple o discapacidad)</label><select id="ex"><option value="0">Ninguna</option><option value="1">1 semana (discapacidad o gemelos)</option><option value="2">2 semanas (trillizos, o gemelos con discapacidad)</option><option value="3">3 semanas</option></select></div></div>
<label class="chk"><input type="checkbox" id="mo"><span>Familia monoparental</span></label>
<button onclick="calc()">Calcular mi permiso</button><div class="res" id="r" aria-live="polite"></div></div>
<p class="note">Cálculo orientativo de los plazos que marca la ley. El día concreto en que empieza y termina lo fija la resolución del INSS a partir de lo que solicites.</p>
<h2>Cuántas semanas son desde noviembre de 2026</h2><p>El Consejo de Ministros aprobó el 24 de noviembre de 2026 ampliar el permiso por nacimiento y cuidado de menor de <b>19 a 20 semanas por progenitor</b>, y de 32 a 34 en las familias monoparentales (Real Decreto-ley 42/2026). La semana nueva se suma a las semanas flexibles que se pueden usar hasta que el niño cumpla 8 años. Se aplica a los hijos <b>nacidos a partir del 26 de noviembre de 2026</b>, y esa semana adicional se podrá solicitar desde el 1 de marzo de 2027.</p>
<table><tr><th>Tramo</th><th>Cada progenitor</th><th>Monoparental</th><th>Plazo</th></tr>
<tr><td>Obligatorias, a jornada completa</td><td>6 semanas</td><td>6 semanas</td><td>Justo después del parto</td></tr>
<tr><td>Resto hasta el año</td><td>11 semanas</td><td>22 semanas</td><td>Antes de que cumpla 12 meses</td></tr>
<tr><td>Flexibles hasta los 8 años</td><td>3 semanas</td><td>6 semanas</td><td>Antes de que cumpla 8 años</td></tr>
<tr><td><b>Total</b></td><td><b>20 semanas</b></td><td><b>34 semanas</b></td><td></td></tr></table>
<p class="note">Para nacidos entre el 31 de julio de 2025 y el 25 de noviembre de 2026 son 19 semanas (6 + 11 + 2; 32 en monoparentales: 6 + 22 + 4). Las 2 semanas hasta los 8 años (4 en monoparentales) también corresponden a los nacidos desde el 2 de agosto de 2024. La calculadora aplica el régimen que toca según la fecha que pongas. Fuente: <a href="https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/inclusion/Paginas/2025/solicitud-permiso-nacimiento-y-cuidado-menor.aspx" rel="noopener" target="_blank">La Moncloa, 25/11/2026</a> y <a href="https://www.seg-social.es/" rel="noopener" target="_blank">Seguridad Social</a>. Al ser un real decreto-ley, el Congreso debe convalidarlo en los 30 días siguientes.</p>
<h2>Cómo se calculan las fechas</h2><p>Las <b>6 primeras semanas</b> se disfrutan seguidas y a jornada completa desde el día del parto: terminan el día anterior a cumplirse 42 días. Las <b>11 siguientes</b> se pueden coger justo después o repartir en periodos de semanas completas, a jornada completa o parcial si lo acuerdas con la empresa, pero siempre antes de que el bebé cumpla 12 meses. La madre biológica puede adelantar hasta <b>4 semanas antes de la fecha prevista del parto</b>; esas semanas salen de las 11 flexibles, no se suman.</p>
<p><b>Ejemplo:</b> un bebé nace el 10 de diciembre de 2026. Cada progenitor tiene 20 semanas. Las 6 obligatorias van del 10 de diciembre al 20 de enero de 2027. Si se encadenan las 11 siguientes, el permiso dura hasta el 7 de abril de 2027 y se vuelve al trabajo el 8 de abril. Las 3 semanas restantes se pueden pedir en cualquier momento hasta el 10 de diciembre de 2034.</p>
<h2>Cuánto se cobra y cómo se pide</h2><p>La Seguridad Social paga el <b>100 % de la base reguladora</b> durante las semanas del permiso, y la prestación está exenta de IRPF. Se solicita en <a href="https://sede.seg-social.gob.es/" rel="noopener" target="_blank">Tu Seguridad Social</a> con certificado digital o Cl@ve, por correo o con cita previa en el INSS. ¿Quieres saber en qué semana de embarazo estás o la fecha probable de parto? Usa la <a href="calculadora-embarazo.html">calculadora de embarazo</a>. Para planificar el resto del año, mira tus <a href="calculadora-vacaciones.html">días de vacaciones</a> (se pueden encadenar con el permiso) y el <a href="calendario-laboral-2027.html">calendario laboral 2027</a>.</p>""",
[("¿Cuántas semanas de baja por nacimiento hay en 2026?", "Para los hijos nacidos desde el 26 de noviembre de 2026, 20 semanas por progenitor (34 en familias monoparentales): 6 obligatorias tras el parto, 11 hasta que cumpla un año y 3 flexibles hasta los 8 años. Para nacidos entre el 31 de julio de 2025 y el 25 de noviembre de 2026, 19 semanas."),
 ("¿Las 20 semanas se aplican a bebés nacidos antes del 26 de noviembre?", "No. Según el Gobierno, la nueva semana es para hijos nacidos a partir del 26 de noviembre de 2026. Los nacidos antes mantienen 19 semanas (17 hasta el año y 2 hasta los 8 años) si nacieron desde el 31 de julio de 2025."),
 ("¿Cuándo vuelvo al trabajo si cojo el permiso seguido?", "Con 17 semanas seguidas desde el parto (6 obligatorias y 11 voluntarias), al día siguiente de cumplirse 119 días. Pon la fecha de nacimiento en la calculadora y te dice el día exacto."),
 ("¿Puede la madre empezar el permiso antes del parto?", "Sí, la madre biológica puede adelantar hasta 4 semanas antes de la fecha prevista del parto. Esas semanas se descuentan de las 11 que no son obligatorias, así que el permiso total no aumenta.")],
"Calculadora del permiso por nacimiento",
DATEJS + """const addD=(d,n)=>{const x=new Date(d);x.setDate(x.getDate()+n);return x;},addY=(d,n)=>{const x=new Date(d.getFullYear()+n,d.getMonth(),d.getDate());if(x.getDate()!=d.getDate())x.setDate(0);return x;};
const fc=d=>d.toLocaleDateString('es-ES',{day:'numeric',month:'long',year:'numeric'});
function calc(){const p=pd('a');if(!p){show('r','Escribe la fecha de nacimiento.');return;}
const mo=document.getElementById('mo').checked,mb=document.getElementById('q').value=='m',an=mb?+document.getElementById('an').value:0,ex=+document.getElementById('ex').value;
document.getElementById('an').disabled=!mb;
const k=iso(p);let y1,y8,reg;
if(k>='2026-11-26'){y1=mo?28:17;y8=mo?6:3;reg='nacimientos desde el 26/11/2026 (RDL 42/2026)';}
else if(k>='2025-07-31'){y1=mo?28:17;y8=mo?4:2;reg='nacimientos del 31/07/2025 al 25/11/2026';}
else if(k>='2024-08-02'){show('r','Para nacimientos entre el 2 de agosto de 2024 y el 30 de julio de 2025, el permiso hasta el año era de 16 semanas y ya habrá terminado. Te quedan <b>'+(mo?4:2)+' semanas</b> flexibles que puedes pedir desde el 1 de enero de 2026 y usar hasta el <b>'+fmt(addY(p,8))+'</b>, día en que cumple 8 años.');return;}
else{show('r','Para nacimientos anteriores al 2 de agosto de 2024 no hay semanas pendientes de este permiso. Revisa la fecha.');return;}
y1+=ex;const tot=y1+y8,ini=addD(p,-7*an),ob=addD(p,41),fin=addD(ini,7*y1-1),ret=addD(fin,1),hoy=new Date();hoy.setHours(0,0,0,0);
let h='Te corresponden:<b class="big">'+tot+' semanas</b>'+(mo?'Familia monoparental · ':'')+'Régimen de '+reg+'.';
h+='<table style="margin-top:12px;font-size:.92rem"><tr><th>Tramo</th><th>Semanas</th><th>Fechas</th></tr>';
if(an)h+='<tr><td>Antes del parto</td><td>'+an+'</td><td>Desde el '+fc(ini)+'</td></tr>';
h+='<tr><td>Obligatorias tras el parto</td><td>6</td><td>Del '+fc(p)+' al <b>'+fc(ob)+'</b></td></tr>';
h+='<tr><td>Resto hasta el año</td><td>'+(y1-6-an)+'</td><td>Antes del <b>'+fc(addY(p,1))+'</b></td></tr>';
h+='<tr><td>Flexibles hasta los 8 años</td><td>'+y8+'</td><td>Antes del <b>'+fc(addY(p,8))+'</b>'+(k>='2026-11-26'?' (la nueva se pide desde el 1/3/2027)':'')+'</td></tr></table>';
h+='Si encadenas las '+y1+' semanas del primer año desde el '+fc(ini)+', el permiso termina el <b>'+fmt(fin)+'</b> y vuelves al trabajo el <b>'+fmt(ret)+'</b>.';
if(fin<hoy)h+='<br>Según esas fechas, el tramo del primer año ya habría terminado si lo cogiste seguido.';
else if(p>hoy)h+='<br>Faltan '+diff(hoy,p)+' días para la fecha prevista.';
show('r',h);}
document.querySelectorAll('.card input,.card select').forEach(e=>e.addEventListener(e.tagName=='SELECT'||e.type=='checkbox'?'change':'input',()=>calc()));
(function(){const d=new Date();d.setDate(d.getDate()+14);document.getElementById('a').value=iso(d);})();calc();"""))

# --- Hora de amanecer y anochecer por ciudad (algoritmo solar de la NOAA, hora oficial de España con cambio de hora) ---
CIUD = [("A Coruña",43.362,-8.411),("Albacete",38.994,-1.858),("Alicante",38.345,-0.481),("Almería",36.834,-2.464),("Ávila",40.656,-4.681),("Badajoz",38.879,-6.970),
("Barcelona",41.385,2.173),("Bilbao",43.263,-2.935),("Burgos",42.344,-3.697),("Cáceres",39.475,-6.372),("Cádiz",36.527,-6.288),("Castellón de la Plana",39.986,-0.051),
("Ceuta",35.889,-5.320),("Ciudad Real",38.985,-3.927),("Córdoba",37.888,-4.779),("Cuenca",40.070,-2.137),("Gijón",43.532,-5.661),("Girona",41.979,2.821),("Granada",37.177,-3.599),
("Guadalajara",40.633,-3.167),("Huelva",37.261,-6.945),("Huesca",42.136,-0.409),("Ibiza",38.909,1.433),("Jaén",37.779,-3.785),("Las Palmas de Gran Canaria",28.124,-15.430,1),
("León",42.599,-5.567),("Lleida",41.617,0.620),("Logroño",42.465,-2.445),("Lugo",43.012,-7.556),("Madrid",40.417,-3.704),("Málaga",36.721,-4.421),("Melilla",35.292,-2.938),
("Murcia",37.992,-1.131),("Ourense",42.336,-7.864),("Oviedo",43.362,-5.849),("Palencia",42.010,-4.533),("Palma",39.570,2.650),("Pamplona",42.812,-1.646),("Pontevedra",42.431,-8.645),
("Salamanca",40.970,-5.663),("San Sebastián",43.318,-1.981),("Santa Cruz de Tenerife",28.464,-16.251,1),("Santander",43.462,-3.810),("Santiago de Compostela",42.878,-8.544),
("Segovia",40.942,-4.108),("Sevilla",37.389,-5.984),("Soria",41.764,-2.465),("Tarragona",41.119,1.245),("Teruel",40.345,-1.106),("Toledo",39.863,-4.027),("Valencia",39.470,-0.376),
("Valladolid",41.652,-4.725),("Vigo",42.240,-8.720),("Vitoria",42.847,-2.672),("Zamora",41.504,-5.745),("Zaragoza",41.649,-0.889)]
_copt = "".join(f'<option value="{c[1]},{c[2]},{c[3] if len(c)>3 else 0}"{" selected" if c[0]=="Madrid" else ""}>{c[0]}</option>' for c in CIUD)
S['tools'].insert(4, ("hora-amanecer-anochecer", "¿A qué hora amanece y anochece?", "Salida y puesta del sol en tu ciudad cualquier día, horas de luz y cuándo empiezan a alargarse los días.", "Amanecer"))
S['aff']["hora-amanecer-anochecer"] = amz("lampara despertador luz amanecer", "Despertadores con luz de amanecer") + amz("lampara luz dia invierno 10000 lux", "Lámparas de luz de día") + amz("linterna frontal led recargable", "Linternas frontales")
P.append(("hora-amanecer-anochecer", "¿A qué hora anochece hoy? Hora de amanecer y anochecer en tu ciudad | CalculadoraDías",
"Hora de salida y puesta del sol hoy o cualquier día en 56 ciudades de España (con Canarias y el cambio de hora), horas de luz, el día más corto y cuándo empieza a anochecer más tarde.",
"""<p class="lead">Elige tu ciudad y una fecha: te decimos a qué hora sale y se pone el sol (hora oficial, con el cambio de hora ya aplicado), cuántas horas de luz hay y cuánto cambian respecto a la víspera.</p>
<div class="card"><div class="row"><div><label for="c">Ciudad</label><select id="c">""" + _copt + """</select></div>
<div><label for="a">Fecha</label><input id="a" type="date" data-today></div></div>
<button onclick="calc()">Ver amanecer y anochecer</button><div class="res" id="r" aria-live="polite"></div></div>
<div id="tb"></div>
<p class="note">Cálculo astronómico con el algoritmo de la NOAA (Administración Nacional Oceánica y Atmosférica de EE. UU.) para el centro de cada ciudad, a nivel del mar y con la refracción atmosférica estándar. La diferencia con los datos oficiales del <a href="https://astronomia.ign.es/" rel="noopener" target="_blank">Observatorio Astronómico Nacional (IGN)</a> suele ser de uno o dos minutos; las montañas del horizonte pueden adelantar el ocaso real.</p>
<h2>Por qué anochece tan pronto en diciembre</h2><p>El día más corto del año es el del <b>solsticio de invierno, el 21 de diciembre</b>: en Madrid hay unas 9 horas y 17 minutos de luz, frente a más de 15 horas en junio. Pero el sol <b>no se pone más pronto el día 21</b>: por la ecuación del tiempo (la órbita de la Tierra es una elipse y su eje está inclinado), las puestas de sol más tempranas llegan hacia el 10 de diciembre y los amaneceres más tardíos, hacia el 4 de enero. Por eso, a mediados de diciembre ya empieza a anochecer unos segundos más tarde cada día, aunque las mañanas sigan oscureciéndose hasta Reyes. La tabla de arriba lo calcula para tu ciudad.</p>
<h2>Cómo influye el huso horario</h2><p>Toda la península, Baleares, Ceuta y Melilla usan la hora de Europa central (UTC+1 en invierno y UTC+2 en verano), aunque casi todo el territorio está al oeste del meridiano de Greenwich. Por eso en España amanece y anochece más tarde que en países a la misma latitud: en Galicia el sol se pone en diciembre unos 35 minutos después que en Cataluña. Canarias tiene una hora menos (UTC+0 en invierno), y su cercanía al ecuador hace que la duración del día cambie mucho menos a lo largo del año.</p>
<table><tr><th>21 de diciembre de 2026</th><th>Amanecer</th><th>Anochecer</th><th>Horas de luz</th></tr>
<tr><td>A Coruña</td><td>9:03</td><td>18:00</td><td>8 h 58 min</td></tr><tr><td>Madrid</td><td>8:34</td><td>17:51</td><td>9 h 17 min</td></tr><tr><td>Barcelona</td><td>8:14</td><td>17:25</td><td>9 h 11 min</td></tr><tr><td>Sevilla</td><td>8:34</td><td>18:09</td><td>9 h 35 min</td></tr><tr><td>Las Palmas (hora canaria)</td><td>7:49</td><td>18:10</td><td>10 h 21 min</td></tr></table>
<p>¿Planeas un viaje en coche para las fiestas? Con estas horas sabrás cuánta luz te queda; calcula también los <a href="cuantos-dias-faltan.html">días que faltan para Navidad</a>, los <a href="puentes-2027.html">puentes de 2027</a> o la <a href="semana-del-ano.html">semana del año</a> en la que estamos.</p>""",
[("¿Cuál es el día más corto del año en España?", "El del solsticio de invierno, el 21 de diciembre en 2026. En Madrid tiene unas 9 horas y 17 minutos de luz, casi 6 horas menos que el 21 de junio."),
 ("¿Cuándo empieza a anochecer más tarde?", "Antes que el solsticio: la puesta de sol más temprana del año llega hacia el 10 de diciembre en la península (entre el 9 y el 11 según la ciudad). Desde entonces anochece un poco más tarde cada día, aunque los amaneceres siguen retrasándose hasta el 3-5 de enero."),
 ("¿A qué hora anochece en Navidad?", "En Madrid, hacia las 17:53 el 25 de diciembre; en Barcelona, hacia las 17:27; en Sevilla, hacia las 18:11; y en A Coruña, hacia las 18:02. Elige tu ciudad y la fecha en la calculadora para verlo exacto."),
 ("¿Cuándo es el próximo cambio de hora?", "El último domingo de marzo, el 28 de marzo de 2027: a las 2:00 serán las 3:00 y anochecerá una hora más tarde. La calculadora aplica el cambio de hora automáticamente.")],
"¿A qué hora amanece y anochece?",
DATEJS + """function lsun(y,m){const d=new Date(Date.UTC(y,m,0));return d.getUTCDate()-d.getUTCDay();}
function off(y,m,d,can){const t=Date.UTC(y,m-1,d,12),a=Date.UTC(y,2,lsun(y,3),1),b=Date.UTC(y,9,lsun(y,10),1);return (can?0:60)+((t>=a&&t<b)?60:0);}
function sun(lat,lon,y,m,d){const n=Math.round((Date.UTC(y,m-1,d)-Date.UTC(y,0,1))/864e5)+1,g=2*Math.PI/365*(n-1),
eq=229.18*(0.000075+0.001868*Math.cos(g)-0.032077*Math.sin(g)-0.014615*Math.cos(2*g)-0.040849*Math.sin(2*g)),
de=0.006918-0.399912*Math.cos(g)+0.070257*Math.sin(g)-0.006758*Math.cos(2*g)+0.000907*Math.sin(2*g)-0.002697*Math.cos(3*g)+0.00148*Math.sin(3*g),
r=Math.PI/180,c=Math.cos(90.833*r)/(Math.cos(lat*r)*Math.cos(de))-Math.tan(lat*r)*Math.tan(de),ha=Math.acos(Math.max(-1,Math.min(1,c)))/r;
return [720-4*(lon+ha)-eq,720-4*lon-eq,720-4*(lon-ha)-eq];}
function hm(x){x=Math.round(x);return Math.floor(x/60)+':'+String(x%60).padStart(2,'0');}
function du(x){x=Math.round(x);return Math.floor(x/60)+' h '+String(x%60).padStart(2,'0')+' min';}
function loc(c,y,m,d){const o=off(y,m,d,c[2]),s=sun(c[0],c[1],y,m,d);return [s[0]+o,s[1]+o,s[2]+o,s[2]-s[0]];}
function fe(t){const d=new Date(t);return d.getUTCDate()+' de '+['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'][d.getUTCMonth()];}
function calc(){const a=pd('a');if(!a)return;const c=document.getElementById('c').value.split(',').map(Number),nm=document.getElementById('c').selectedOptions[0].text;
const y=a.getFullYear(),m=a.getMonth()+1,d=a.getDate(),L=loc(c,y,m,d),p=new Date(y,m-1,d-1),P=loc(c,p.getFullYear(),p.getMonth()+1,p.getDate()),dl=Math.round(L[3]-P[3]);
let h='En '+nm+' el '+fmt(a)+':<b class="big">Amanece '+hm(L[0])+' · Anochece '+hm(L[2])+'</b>Horas de luz: <b>'+du(L[3])+'</b> ('+(dl>0?dl+' min más':dl<0?(-dl)+' min menos':'casi igual')+' que el día anterior) · Mediodía solar: '+hm(L[1])+(c[2]?' (hora canaria)':'');
show('r',h);
const SO={2025:[5,20,11,21],2026:[5,21,11,21],2027:[5,21,11,22],2028:[5,20,11,21]};let mn=[1e9,0],mx=[0,0],ss=[1e9,0],sr=[0,0];for(let i=0;i<366;i++){const t=Date.UTC(y,0,1)+i*864e5,q=new Date(t);if(q.getUTCFullYear()!==y)break;const Q=loc(c,y,q.getUTCMonth()+1,q.getUTCDate());
if(Q[3]<mn[0])mn=[Q[3],t];if(Q[3]>mx[0])mx=[Q[3],t];const mo=q.getUTCMonth();if(mo>9&&Q[2]-off(y,mo+1,q.getUTCDate(),c[2])<ss[0])ss=[Q[2]-off(y,mo+1,q.getUTCDate(),c[2]),t];if(mo<2&&Q[0]>sr[0])sr=[Q[0],t];}
if(SO[y]){mx=[0,Date.UTC(y,SO[y][0],SO[y][1])];mn=[0,Date.UTC(y,SO[y][2],SO[y][3])];mx[0]=loc(c,y,SO[y][0]+1,SO[y][1])[3];mn[0]=loc(c,y,SO[y][2]+1,SO[y][3])[3];}
const S1=loc(c,y,(new Date(ss[1])).getUTCMonth()+1,(new Date(ss[1])).getUTCDate()),R1=loc(c,y,(new Date(sr[1])).getUTCMonth()+1,(new Date(sr[1])).getUTCDate());
document.getElementById('tb').innerHTML='<h2>'+nm+' en '+y+'</h2><table><tr><th>Dato</th><th>Fecha</th><th>Valor</th></tr>'+
'<tr><td>Día más corto (solsticio de invierno)</td><td>'+fe(mn[1])+'</td><td>'+du(mn[0])+' de luz</td></tr><tr><td>Día más largo (solsticio de verano)</td><td>'+fe(mx[1])+'</td><td>'+du(mx[0])+' de luz</td></tr>'+
'<tr><td>Puesta de sol más temprana (final de año)</td><td>'+fe(ss[1])+'</td><td>'+hm(S1[2])+'</td></tr><tr><td>Amanecer más tardío (principio de año)</td><td>'+fe(sr[1])+'</td><td>'+hm(R1[0])+'</td></tr></table>';}
document.querySelectorAll('.card input,.card select').forEach(x=>x.addEventListener('change',()=>calc()));"""))

# --- Mejoras de páginas existentes (27/11/2026) ---
def _set(slug, i, val):
    for k, t in enumerate(P):
        if t[0] == slug:
            t = list(t); t[i] = val(t[i]) if callable(val) else val; P[k] = tuple(t); return
    raise KeyError(slug)
def _add(slug, old, new):
    def f(b):
        assert old in b, (slug, old); return b.replace(old, new, 1)
    _set(slug, 3, f)

# Semana del año: calendario de semanas del año elegido, 2026 con 53 semanas, Excel y ejemplos
_set("semana-del-ano", 1, "Semana del año: ¿en qué semana estamos hoy? Calendario de semanas 2026 y 2027 | CalculadoraDías")
_set("semana-del-ano", 2, "Mira en qué número de semana estamos hoy (ISO 8601, la de los calendarios en España) y el calendario completo de semanas de 2026 y 2027 con el lunes y el domingo de cada una.")
_set("semana-del-ano", 5, "¿En qué semana del año estamos?")
_set("semana-del-ano", 3, """<p class="lead">Número de semana según la norma ISO 8601, la que usan los calendarios, las agendas y las empresas en España y en casi toda Europa. Elige cualquier fecha y verás su semana y el calendario de semanas de todo el año.</p>
<div class="card"><label for="a">Fecha</label><input id="a" type="date" data-today><button onclick="calc()">Ver semana</button><div class="res" id="r" aria-live="polite"></div></div>
<div id="tb"></div>
<h2>Cómo funciona la semana ISO</h2><p>Las semanas empiezan en <b>lunes</b> y la <b>semana 1</b> es la que contiene el primer jueves del año (o, lo que es lo mismo, la que contiene el 4 de enero). Por eso los primeros días de enero pueden pertenecer a la última semana del año anterior, y algunos años tienen <b>53 semanas</b>: los que empiezan en jueves y los bisiestos que empiezan en miércoles.</p>
<table><tr><th>Año</th><th>Semanas</th><th>Semana 1 empieza</th><th>Última semana termina</th></tr>
<tr><td>2026</td><td>53</td><td>lunes 29 de diciembre de 2025</td><td>domingo 3 de enero de 2027</td></tr>
<tr><td>2027</td><td>52</td><td>lunes 4 de enero de 2027</td><td>domingo 2 de enero de 2028</td></tr></table>
<p><b>Ejemplo:</b> el 1 de enero de 2027 es viernes. La semana que lo contiene tiene su jueves el 31 de diciembre de 2026, así que es la <b>semana 53 de 2026</b>. La semana 1 de 2027 empieza el lunes 4 de enero.</p>
<h2>Semana del año en Excel, Google Sheets y el móvil</h2><ul><li><b>Excel:</b> usa <code>=ISO.NUM.DE.SEMANA(A1)</code>. La función <code>NUM.DE.SEMANA</code> empieza por defecto en domingo y cuenta como semana 1 la del 1 de enero, así que puede dar un número distinto.</li><li><b>Google Sheets:</b> <code>=ISOWEEKNUM(A1)</code> (o <code>=ISO.NUM.DE.SEMANA(A1)</code> con la hoja en español).</li><li><b>Calendario del móvil:</b> en Google Calendar y en el de iPhone puedes activar «Mostrar número de semana» en los ajustes.</li></ul>
<p>Para planificar por semanas también te sirven los <a href="dias-habiles.html">días hábiles entre dos fechas</a>, el <a href="calendario-laboral-2027.html">calendario laboral 2027</a> con los festivos de tu comunidad o <a href="sumar-dias.html">sumar días a una fecha</a>. Y si quieres saber cuánta luz te queda por la tarde, mira <a href="hora-amanecer-anochecer.html">a qué hora anochece hoy</a>.</p>""")
_set("semana-del-ano", 4, [("¿En qué semana estamos hoy?", "La calculadora muestra arriba la semana de hoy en cuanto abres la página, con el lunes y el domingo en que empieza y termina. El 27 de noviembre de 2026, por ejemplo, es la semana 48."),
 ("¿Cuántas semanas tiene 2026?", "53 semanas ISO, porque 2026 empezó en jueves. La semana 53 va del lunes 28 de diciembre de 2026 al domingo 3 de enero de 2027."),
 ("¿Cuántas semanas tiene 2027?", "52. La semana 1 de 2027 empieza el lunes 4 de enero y la semana 52 termina el domingo 2 de enero de 2028."),
 ("¿Por qué Excel me da otro número?", "La función NUM.DE.SEMANA de Excel por defecto empieza en domingo y cuenta como semana 1 la que contiene el 1 de enero. Usa ISO.NUM.DE.SEMANA para obtener el mismo resultado que aquí.")])
_set("semana-del-ano", 6, lambda js: js.replace("show('r','Semana:<b class=\"big\">'+w+' de '+y+'</b>Del '+fmt(l)+' al '+fmt(s));}calc();",
 """show('r','Semana:<b class="big">'+w+' de '+y+'</b>Del '+fmt(l)+' al '+fmt(s));tabla(y,w);}
function tabla(y,cw){const j4=new Date(y,0,4),m=new Date(j4);m.setDate(j4.getDate()-((j4.getDay()||7)-1));const o={day:'numeric',month:'short'};let h='',n=0;
for(let d=new Date(m);;d.setDate(d.getDate()+7)){const [w,yy]=wk(d);if(yy!==y)break;n++;const e=new Date(d);e.setDate(d.getDate()+6);
h+='<tr'+(w===cw?' style="font-weight:700"':'')+'><td>'+w+'</td><td>'+d.toLocaleDateString('es-ES',o)+(d.getFullYear()!==y?' '+d.getFullYear():'')+'</td><td>'+e.toLocaleDateString('es-ES',o)+(e.getFullYear()!==y?' '+e.getFullYear():'')+'</td></tr>';}
document.getElementById('tb').innerHTML='<details><summary><b>Calendario de semanas de '+y+' ('+n+' semanas)</b></summary><table><tr><th>Semana</th><th>Lunes</th><th>Domingo</th></tr>'+h+'</table></details>';}
document.getElementById('a').addEventListener('change',()=>calc());calc();"""))

# Enlaces internos a la nueva herramienta de amanecer y anochecer
_add("cuantos-dias-faltan", "</p>", " ¿Y a qué hora se hará de noche ese día? Míralo en la calculadora de <a href=\"hora-amanecer-anochecer.html\">hora de amanecer y anochecer</a>.</p>")
_add("puentes-2027", "</p>", " Para aprovechar las tardes de tus escapadas, consulta <a href=\"hora-amanecer-anochecer.html\">a qué hora anochece</a> en tu destino.</p>")
S['home_intro'] = S['home_intro'].replace('<a href="paga-extra-navidad.html">Paga extra</a>', '<a href="hora-amanecer-anochecer.html">Hora de anochecer</a>')

# --- Nueva (27/11/2026, 13:23): cuánto cobro de baja: incapacidad temporal por enfermedad común o accidente, por tramos de días y por meses ---
S['tools'].insert(5, ("cuanto-cobro-de-baja", "¿Cuánto cobro de baja?", "Lo que cobras de baja médica por enfermedad o accidente: 60 % y 75 % por tramos de días, quién paga y cuánto en cada nómina.", "Baja médica"))
S['aff']["cuanto-cobro-de-baja"] = amz("estatuto de los trabajadores 2026", "Estatuto de los Trabajadores") + amz("agenda 2027 dia por pagina", "Agendas 2027")
P.append(("cuanto-cobro-de-baja", "¿Cuánto cobro de baja? Calculadora de la baja médica por días | CalculadoraDías",
"Calcula cuánto cobras de baja por enfermedad común o accidente: 60 % de la base reguladora del día 4 al 20 y 75 % desde el día 21, quién paga cada tramo y cuánto te llega en cada nómina.",
"""<p class="lead">Pon tu sueldo, el día en que empezó la baja y cuántos días dura (o la fecha de alta). Te decimos cuánto cobras en total, en cada tramo y en la nómina de cada mes, y quién te lo paga.</p>
<div class="card"><div class="row"><div><label for="ti">Tipo de baja</label><select id="ti"><option value="c">Enfermedad común o accidente no laboral</option><option value="l">Accidente de trabajo o enfermedad profesional</option></select></div>
<div><label for="sb">Sueldo bruto mensual (€)</label><input id="sb" inputmode="decimal" value="1800"></div>
<div><label for="np">Número de pagas</label><select id="np"><option value="14">14 (dos pagas extra)</option><option value="12">12 o pagas prorrateadas</option><option value="15">15</option></select></div>
<div><label for="bc">O base de cotización del mes anterior (€, opcional)</label><input id="bc" inputmode="decimal" value="" placeholder="Viene en tu nómina"></div>
<div><label for="fi">Primer día de baja</label><input id="fi" type="date" data-today></div>
<div><label for="nd">Días de baja</label><input id="nd" inputmode="numeric" value="30"></div>
<div><label for="fa">O fecha de alta (opcional)</label><input id="fa" type="date"></div>
<div><label for="cv">Complemento de tu convenio</label><select id="cv"><option value="0">Ninguno</option><option value="100">La empresa completa hasta el 100 % del sueldo</option></select></div></div>
<button onclick="calc()">Calcular lo que cobro</button><div class="res" id="r" aria-live="polite"></div></div>
<p class="note">Importes brutos: de la prestación se descuentan el IRPF y tus cotizaciones como en una nómina normal. Si pones la fecha de alta, contamos hasta el día anterior (el día del alta ya se trabaja).</p>
<h2>Cuánto se cobra de baja</h2><p>La prestación por incapacidad temporal no se calcula sobre el sueldo neto, sino sobre la <b>base reguladora</b>: la base de cotización del mes anterior a la baja dividida entre 30 (si cobras por meses). Esa base incluye la parte proporcional de las pagas extra, por eso con 14 pagas es mayor que tu sueldo mensual: 1.800 € × 14 ÷ 12 = 2.100 €.</p>
<table><tr><th>Días de baja</th><th>Enfermedad común o accidente no laboral</th><th>Accidente de trabajo o enfermedad profesional</th></tr>
<tr><td>Día 1 a 3</td><td>Nada (salvo mejora del convenio)</td><td>Día 1: sueldo íntegro (lo paga la empresa). Desde el día 2: 75 %</td></tr>
<tr><td>Día 4 a 15</td><td>60 % · lo paga la empresa</td><td>75 % · mutua o INSS</td></tr>
<tr><td>Día 16 a 20</td><td>60 % · INSS o mutua</td><td>75 %</td></tr>
<tr><td>Día 21 en adelante</td><td>75 % · INSS o mutua</td><td>75 %</td></tr></table>
<p>Aunque una parte la pague la Seguridad Social o la mutua, normalmente te llega todo en la <b>nómina</b>: la empresa lo adelanta (pago delegado) y luego lo descuenta de sus cotizaciones. La baja puede durar hasta <b>365 días</b>, prorrogables otros 180.</p>
<p><b>Ejemplo:</b> sueldo de 1.800 € en 14 pagas y 30 días de baja por enfermedad común. Base reguladora diaria: 2.100 ÷ 30 = 70 €. Los días 1 a 3 no se cobran; del 4 al 20 (17 días) cobras el 60 %, 42 € al día: 714 €; del 21 al 30 (10 días), el 75 %, 52,50 € al día: 525 €. En total, <b>1.239 € brutos</b> por esos 30 días, frente a los 2.100 € que habrías cotizado: unos 860 € menos. De ellos, la empresa paga los días 4 a 15 (504 €) y el INSS o la mutua el resto (735 €).</p>
<h2>Requisitos y detalles</h2><ul><li>Para la baja por <b>enfermedad común</b> necesitas haber cotizado al menos 180 días en los últimos 5 años. Para accidente (laboral o no) y enfermedad profesional no se pide cotización previa.</li><li>Muchos <b>convenios colectivos</b> mejoran la prestación: algunos pagan el 100 % desde el primer día y otros solo a partir de cierto día. Mira el tuyo.</li><li>Las <b>vacaciones</b> que coinciden con una baja no se pierden: se disfrutan después del alta. Calcula las que te corresponden con la <a href="calculadora-vacaciones.html">calculadora de vacaciones</a>.</li><li>Si la baja te pilla en el <b>paro</b>, cobras la prestación por desempleo; mira <a href="calcular-paro.html">cuánto paro te corresponde</a>. Y para contar los días exactos entre dos fechas, usa <a href="dias-entre-fechas.html">días entre fechas</a>.</li></ul>""",
[("¿Cuánto se cobra de baja por enfermedad común?", "Nada los tres primeros días (salvo que tu convenio lo mejore), el 60 % de la base reguladora del día 4 al 20 y el 75 % desde el día 21. La base reguladora diaria es la base de cotización del mes anterior dividida entre 30."),
 ("¿Quién paga la baja, la empresa o la Seguridad Social?", "En la baja por enfermedad común la empresa paga a su cargo del día 4 al 15, y desde el día 16 la Seguridad Social o la mutua. Aun así, lo normal es que la empresa te lo abone todo en la nómina y luego se lo descuente en sus cotizaciones."),
 ("¿Cuánto se cobra de baja por accidente laboral?", "El día del accidente se cobra el sueldo completo y, desde el día siguiente, el 75 % de la base reguladora, que en este caso incluye también la media de horas extra del año anterior. No hay días sin cobrar ni se exige cotización previa."),
 ("¿Se cobran las pagas extra estando de baja?", "La prestación ya incluye la parte proporcional de las pagas extra, porque la base de cotización las lleva prorrateadas. Si tu convenio no dice otra cosa, la empresa puede descontar de la paga extra el tiempo de baja; muchos convenios lo prohíben.")],
"¿Cuánto cobro de baja?",
DATEJS + """const fdm=d=>d.toLocaleDateString('es-ES',{month:'long',year:'numeric'});
function calc(){const lab=document.getElementById('ti').value==='l',np=+document.getElementById('np').value,sb=v('sb'),bc=v('bc')>0?v('bc'):sb*np/12,fi=pd('fi')||today,fa=pd('fa'),cv=+document.getElementById('cv').value;
let n=Math.round(v('nd'));if(fa){n=diff(fi,fa);if(n<1){show('r','La fecha de alta tiene que ser posterior al primer día de baja.');return;}}
if(bc<=0||n<1){show('r','Escribe tu sueldo y los días de baja.');return;}if(n>545)n=545;
const bd=bc/30;let tot=0,emp=0,tr=[0,0,0,0],dt=[0,0,0,0],mes={},orden=[];
for(let k=1;k<=n;k++){let p,t;if(lab){if(k===1){p=1;t=0;}else{p=0.75;t=3;}}else if(k<=3){p=0;t=0;}else if(k<=20){p=0.6;t=k<=15?1:2;}else{p=0.75;t=3;}
const a=bd*p;tot+=a;tr[t]+=a;dt[t]++;if(!lab&&k>=4&&k<=15)emp+=a;if(lab&&k===1)emp+=a;
const d=new Date(fi.getFullYear(),fi.getMonth(),fi.getDate()+k-1),key=d.getFullYear()*12+d.getMonth();if(!(key in mes)){mes[key]=[0,d];orden.push(key);}mes[key][0]+=a;}
const fin=new Date(fi.getFullYear(),fi.getMonth(),fi.getDate()+n-1),sueldo=bd*n;
let h='Cobras por '+n+' días de baja:<b class="big">'+eur(tot)+' brutos</b>Base reguladora: '+eur(bc)+' al mes ('+eur(bd)+' al día). Del '+fmt(fi)+' al '+fmt(fin)+'.';
if(lab)h+='<br>Día 1 (sueldo íntegro): <b>'+eur(tr[0])+'</b> · Desde el día 2 al 75 %: <b>'+eur(tr[3])+'</b> ('+dt[3]+' días a '+eur(bd*0.75)+').';
else{h+='<br>Días 1 a 3: <b>0 €</b>'+(n>3?' · Días 4 a '+Math.min(n,20)+' al 60 %: <b>'+eur(tr[1]+tr[2])+'</b> ('+(dt[1]+dt[2])+' días a '+eur(bd*0.6)+')':'')+(n>20?' · Desde el día 21 al 75 %: <b>'+eur(tr[3])+'</b> ('+dt[3]+' días a '+eur(bd*0.75)+')':'')+'.';
h+='<br>Paga la empresa: <b>'+eur(emp)+'</b> · Paga el INSS o la mutua: <b>'+eur(tot-emp)+'</b> (normalmente todo te llega en la nómina).';}
if(cv===100)h+='<br>Con el complemento de tu convenio hasta el 100 % cobrarías <b>'+eur(sueldo)+'</b>: la empresa añade '+eur(sueldo-tot)+'.';
else h+='<br>Frente a tu base de cotización de esos días ('+eur(sueldo)+'), dejas de cobrar unos <b>'+eur(sueldo-tot)+'</b>.';
if(orden.length>1)h+='<br>Por nóminas: '+orden.map(k=>fdm(mes[k][1])+' <b>'+eur(mes[k][0])+'</b>').join(' · ')+'.';
show('r',h);}
calc();"""))
for _k, _t in enumerate(P):
    if _t[0] in ("calcular-finiquito", "calcular-paro", "calculadora-vacaciones"):
        _l = list(_t)
        _l[3] = _l[3] + '<p>¿Estás de baja médica? Calcula <a href="cuanto-cobro-de-baja.html">cuánto cobras de baja</a> por enfermedad o accidente, día a día y en cada nómina.</p>'
        P[_k] = tuple(_l)

# --- Mejora (27/11/2026, 13:23): título y descripción del finiquito con lo que más se busca ---
for _k, _t in enumerate(P):
    if _t[0] == "calcular-finiquito":
        _l = list(_t)
        _l[1] = "Calcular finiquito 2026: vacaciones no disfrutadas, pagas extra y días del mes | CalculadoraDías"
        _l[2] = "Calcula tu finiquito al irte de la empresa o si te despiden: días trabajados del último mes, vacaciones no disfrutadas, parte proporcional de las pagas extra y descuento por no avisar con 15 días. Con tus fechas exactas."
        P[_k] = tuple(_l)
S['home_intro'] = S['home_intro'].replace('<a href="permiso-nacimiento.html">Permiso por nacimiento</a>', '<a href="paga-extra-navidad.html">Paga extra de Navidad</a>', 1)
