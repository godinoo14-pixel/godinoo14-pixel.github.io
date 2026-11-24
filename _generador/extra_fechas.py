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

P.append(("calculadora-vacaciones", "Calculadora de días de vacaciones: ¿cuántos me corresponden? | CalculadoraDías",
"Calcula los días de vacaciones que te corresponden según el tiempo trabajado: proporcional a 30 días naturales o 22 laborables al año.",
"""<p class="lead">Calcula las vacaciones generadas según las fechas trabajadas en el año.</p>
<div class="card"><div class="row"><div><label for="a">Fecha de inicio</label><input id="a" type="date" value="2026-01-01"></div>
<div><label for="b">Fecha de fin (o hoy)</label><input id="b" type="date" data-today></div>
<div><label for="d">Días de vacaciones al año</label><select id="d"><option value="30">30 días naturales</option><option value="22">22 días laborables</option><option value="x">Otro (convenio)</option></select></div>
<div><label for="dx">Días según convenio</label><input id="dx" inputmode="numeric" value="23"></div>
<div><label for="u">Días ya disfrutados</label><input id="u" inputmode="numeric" value="0"></div></div>
<button onclick="calc()">Calcular vacaciones</button><div class="res" id="r"></div></div>
<p class="note">El Estatuto de los Trabajadores fija un mínimo de 30 días naturales al año; tu convenio puede mejorarlo. Si dejas la empresa, los días generados y no disfrutados se pagan en el finiquito.</p>
<h2>Cómo se calculan</h2><p>Las vacaciones se generan de forma proporcional al tiempo trabajado: días trabajados ÷ 365 × días anuales. Si entraste el 1 de julio con 30 días naturales al año, a 31 de diciembre habrás generado unos 15 días.</p>""",
[("¿Cuántos días de vacaciones me corresponden al año?", "Como mínimo 30 días naturales (equivalen aproximadamente a 22 laborables), salvo que tu convenio establezca más."),
 ("¿Las vacaciones no disfrutadas se pagan?", "Solo cuando termina la relación laboral: se incluyen en el finiquito. Mientras sigues en la empresa no pueden sustituirse por dinero.")],
None, DATEJS + """function calc(){const a=pd('a'),b=pd('b');if(!a||!b||b<a)return;const s=document.getElementById('d').value,an=s=='x'?v('dx'):parseFloat(s);const t=diff(a,b)+1,g=t/365*an;
show('r','Vacaciones generadas:<b class="big">'+nf(g,1)+' días</b>Días trabajados: '+t+' · Pendientes de disfrutar: <b>'+nf(Math.max(0,g-v('u')),1)+'</b> ('+(s=='30'?'naturales':'laborables')+')');}"""))

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

P.append(("que-dia-de-la-semana", "¿Qué día de la semana fue o será? Calculadora | CalculadoraDías",
"Descubre en qué día de la semana cae cualquier fecha: tu cumpleaños, una boda, un festivo o el día en que naciste.",
"""<p class="lead">Elige una fecha y te decimos qué día de la semana fue o será, y cómo cae en los próximos años.</p>
<div class="card"><label for="a">Fecha</label><input id="a" type="date" value="2027-12-25"><button onclick="calc()">Ver día</button><div class="res" id="r"></div></div>
<h2>¿Por qué cada año cambia el día?</h2><p>Un año normal tiene 365 días, es decir, 52 semanas y 1 día. Por eso una misma fecha avanza un día de la semana cada año, y dos cuando hay un 29 de febrero de por medio. Así, si tu cumpleaños es martes este año, el que viene será miércoles.</p>""",
[("¿Qué día de la semana nací?", "Pon tu fecha de nacimiento en la calculadora y te dirá el día exacto."),
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
