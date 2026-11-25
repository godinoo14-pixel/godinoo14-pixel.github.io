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

P.append(("calculadora-vacaciones", "Calculadora de vacaciones: ¿cuántos días me corresponden en 2026? | CalculadoraDías",
"Calcula los días de vacaciones que te corresponden según lo trabajado este año (30 naturales, 22 laborables o tu convenio), cuántos te quedan por disfrutar antes del 31 de diciembre y cuánto te pagarían en el finiquito.",
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
<p>Para planificar los días que te quedan, mira los <a href="calendario-laboral-2027.html">puentes del calendario laboral 2027</a> y cuenta los <a href="dias-habiles.html">días laborables entre dos fechas</a>. Si te vas de la empresa, calcula tu <a href="calcular-finiquito.html">finiquito</a> completo con las vacaciones y las pagas extra.</p>""",
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

P.append(("calculadora-horas", "Calculadora de horas trabajadas: entrada, salida y descansos | CalculadoraDías",
"Calcula las horas trabajadas entre la hora de entrada y la de salida, restando descansos, y el total semanal y mensual.",
"""<p class="lead">Pon tu hora de entrada, de salida y el descanso, y te sumamos las horas del día, la semana y el mes.</p>
<div class="card"><div class="row"><div><label for="e">Entrada</label><input id="e" type="time" value="09:00"></div><div><label for="s">Salida</label><input id="s" type="time" value="18:00"></div>
<div><label for="p">Descanso (minutos)</label><input id="p" inputmode="numeric" value="60"></div><div><label for="dd">Días trabajados a la semana</label><input id="dd" inputmode="numeric" value="5"></div>
<div><label for="ph">Precio por hora (€, opcional)</label><input id="ph" inputmode="decimal" value="0"></div></div>
<button onclick="calc()">Calcular horas</button><div class="res" id="r"></div></div>
<p class="note">Si sales después de medianoche (turno de noche) también funciona: se suma el día siguiente.</p>
<h2>Jornada máxima en España</h2><p>La jornada ordinaria máxima es de 40 horas semanales de trabajo efectivo en cómputo anual, con al menos 12 horas de descanso entre jornadas. Desde 2019 las empresas están obligadas a registrar la jornada de cada trabajador.</p>""",
[("¿Cómo paso minutos a horas decimales?", "Divide los minutos entre 60: 7 horas y 45 minutos son 7,75 horas."),
 ("¿El descanso del bocadillo cuenta como tiempo trabajado?", "Solo si así lo establece tu convenio o contrato. Por ley, en jornadas de más de 6 horas hay derecho a una pausa mínima de 15 minutos.")],
None, """function mn(id){const [h,m]=document.getElementById(id).value.split(':').map(Number);return h*60+m;}
function hm(x){x=Math.round(x);return Math.floor(x/60)+' h '+String(x%60).padStart(2,'0')+' min';}
function calc(){let d=mn('s')-mn('e');if(d<0)d+=1440;d-=v('p');d=Math.max(0,d);const w=d*v('dd'),m=w*52/12,ph=v('ph');
show('r','Horas al día:<b class="big">'+hm(d)+'</b>('+nf(d/60,2)+' h) · Semana: <b>'+hm(w)+'</b> · Mes: <b>'+nf(m/60,1)+' h</b>'+(ph>0?'<br>Ingresos: '+eur(d/60*ph)+'/día · '+eur(m/60*ph)+'/mes':''));}"""))

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
<table><tr><th>Lotería de Navidad (por décimo)</th><th>Bruto</th><th>Hacienda</th><th>Te queda</th></tr>
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
P.append(("indemnizacion-despido", "Calcular indemnización por despido 2026: improcedente, objetivo y fin de contrato | CalculadoraDías",
"Calcula tu indemnización por despido improcedente (33 o 45 días por año), objetivo (20 días) o fin de contrato temporal (12 días) con tus fechas exactas, salario diario y topes legales.",
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
P.append(("calcular-finiquito", "Calcular finiquito 2026: vacaciones, pagas extra y días del mes | CalculadoraDías",
"Calcula tu finiquito con tus fechas exactas: días del último mes, vacaciones no disfrutadas, parte proporcional de las pagas extra y descuento por no avisar con 15 días. Baja voluntaria, despido o fin de contrato.",
"""<p class="lead">Pon tu fecha de alta, el último día que trabajas y tu sueldo. Te desglosamos lo que tiene que pagarte la empresa al irte: el finiquito, que te corresponde siempre, te despidan o te vayas tú.</p>
<div class="card"><div class="row"><div><label for="al">Fecha de alta en la empresa</label><input id="al" type="date" value="2024-03-01"></div>
<div><label for="fb">Último día trabajado (fecha de baja)</label><input id="fb" type="date" value="2026-12-15"></div>
<div><label for="sm">Salario bruto mensual sin pagas extra (€)</label><input id="sm" inputmode="decimal" value="1800"></div>
<div><label for="pg">Pagas extra</label><select id="pg"><option value="a">2 pagas, cada una se genera en 12 meses</option><option value="s">2 pagas, cada una se genera en 6 meses</option><option value="p">Prorrateadas en la nómina mensual</option></select></div>
<div><label for="pe">Importe de cada paga extra completa (€)</label><input id="pe" inputmode="decimal" value="1800"></div>
<div><label for="dm">Días de este mes sin cobrar</label><input id="dm" inputmode="numeric" value="15"></div>
<div><label for="va">Vacaciones al año (días naturales)</label><input id="va" inputmode="numeric" value="30"></div>
<div><label for="vd">Vacaciones ya disfrutadas este año (días naturales)</label><input id="vd" inputmode="numeric" value="22"></div>
<div><label for="pa">Días de preaviso que no has dado (solo baja voluntaria)</label><input id="pa" inputmode="numeric" value="0"></div>
<div><label for="ir">Retención de IRPF de tu nómina (%)</label><input id="ir" inputmode="decimal" value="15"></div></div>
<button onclick="calc()">Calcular finiquito</button><div class="res" id="r" aria-live="polite"></div></div>
<p class="note">Si tu convenio cuenta las vacaciones en días laborables (por ejemplo 22), pásalas a naturales multiplicando por 30 y dividiendo entre 22. Si tienes una tercera paga (de beneficios), súmala aparte con la misma regla.</p>
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
 ("¿Cuántos días de preaviso hay que dar al dejar un trabajo?", "Los que diga tu convenio o tu contrato; lo más habitual son 15 días naturales. Si no das el preaviso, la empresa puede descontarte del finiquito un día de salario por cada día que falte.")],
"Calculadora de finiquito",
DATEJS + """function per(t,b){const y=b.getFullYear(),m=b.getMonth();
if(t=='a')return [['paga de Navidad',new Date(y,0,1),new Date(y,11,31)],['paga de verano',m<6?new Date(y-1,6,1):new Date(y,6,1),m<6?new Date(y,5,30):new Date(y+1,5,30)]];
return m<6?[['paga de verano',new Date(y,0,1),new Date(y,5,30)]]:[['paga de Navidad',new Date(y,6,1),new Date(y,11,31)]];}
function calc(){const al=pd('al'),b=pd('fb'),sm=v('sm'),t=document.getElementById('pg').value,pe=v('pe'),irp=v('ir');
if(!al||!b||b<al||sm<=0){show('r','Revisa las fechas y el salario.');return;}
const sd=sm/30,dm=Math.min(30,Math.max(0,v('dm'))),sal=sd*dm;
const y0=new Date(b.getFullYear(),0,1),ini=al>y0?al:y0,dy=diff(ini,b)+1,dya=diff(y0,new Date(b.getFullYear(),11,31))+1;
const gen=dy/dya*v('va'),pend=gen-v('vd'),vac=pend*sd;
let pag=0,lp='';if(t!='p'){per(t,b).forEach(p=>{const i=al>p[1]?al:p[1],d=Math.max(0,diff(i,b)+1),tot=diff(p[1],p[2])+1,x=pe*d/tot;pag+=x;lp+='<br>Parte de la '+p[0]+': <b>'+eur(x)+'</b> ('+d+' de '+tot+' días)';});}
const pre=sd*Math.max(0,v('pa')),br=sal+vac+pag-pre,ne=br*(1-irp/100)-(sal+vac-pre+pag)*0.065;
let h='Finiquito (bruto):<b class="big">'+eur(br)+'</b>Salario de '+nf(dm,0)+' días de este mes: <b>'+eur(sal)+'</b>';
h+='<br>Vacaciones '+(pend>=0?'pendientes: <b>'+nf(pend,1)+' días = '+eur(vac)+'</b>':'disfrutadas de más: <b>'+nf(-pend,1)+' días = −'+eur(-vac)+'</b>')+' (generadas '+nf(gen,1)+' de '+nf(v('va'),0)+' en '+dy+' días de este año)';
h+=t=='p'?'<br>Pagas extra: ya cobradas cada mes (prorrateadas).':lp;
if(pre>0)h+='<br>Descuento por falta de preaviso: <b>−'+eur(pre)+'</b>';
h+='<br>Neto aproximado: <b>'+eur(Math.max(0,ne))+'</b> (con '+nf(irp,1)+' % de IRPF y un 6,5 % de cotización a la Seguridad Social).';
h+='<br><span class="note">Salario diario usado: '+eur(sd)+' (salario mensual ÷ 30). Si te despiden, la indemnización va aparte.</span>';
show('r',h);}
calc();"""))
