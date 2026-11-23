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
