/* Numeria — motor genérico de calculadoras. Cada herramienta: id → función(v) que devuelve {label,big,rows,note} */
(function(){
  const CUR=(document.documentElement.dataset.cur||'EUR');
  const m=(v,d=2)=>v.toLocaleString('es-ES',{style:'currency',currency:CUR,minimumFractionDigits:d,maximumFractionDigits:d});
  const n=(v,d=2)=>v.toLocaleString('es-ES',{minimumFractionDigits:0,maximumFractionDigits:d});
  const p=(v,d=2)=>n(v*100,d)+' %';
  const cuota=(P,r,k)=> r===0? P/k : P*r/(1-Math.pow(1+r,-k));
  const T={
    pct:v=>({label:`${n(v.p)} % de ${n(v.n)}`,big:n(v.p/100*v.n,4),rows:[
      ['Variación de A a B', v.a? p((v.b-v.a)/v.a):'—'],['A es este % de B', v.b? p(v.a/v.b):'—'],['B + '+n(v.p)+' %',n(v.n*(1+v.p/100),4)],['B − '+n(v.p)+' %',n(v.n*(1-v.p/100),4)]]}),
    iva:v=>{const t=v.tipo/100; if(v.modo==='anadir'){const c=v.imp*t; return {label:'Precio con IVA',big:m(v.imp+c),rows:[['Base imponible',m(v.imp)],['IVA ('+n(v.tipo)+' %)',m(c)]]};}
      const b=v.imp/(1+t); return {label:'Precio sin IVA (base)',big:m(b),rows:[['IVA incluido ('+n(v.tipo)+' %)',m(v.imp-b)],['Precio con IVA',m(v.imp)]]};},
    desc:v=>{const f=v.precio*(1-v.d1/100)*(1-v.d2/100); return {label:'Precio final',big:m(f),rows:[['Ahorro',m(v.precio-f)],['Descuento total equivalente',v.precio?p(1-f/v.precio):'—']],
      note: v.d2? 'Los descuentos sucesivos no se suman: '+n(v.d1)+' % + '+n(v.d2)+' % equivale a '+(v.precio?p(1-f/v.precio):'—')+'.':''};},
    r503020:v=>({label:'Ahorro e inversión (20 %)',big:m(v.ing*.2),rows:[['Necesidades (50 %)',m(v.ing*.5)],['Deseos (30 %)',m(v.ing*.3)],['Ahorro (20 %)',m(v.ing*.2)],['Ahorro en un año',m(v.ing*.2*12)]]}),
    cagr:v=>{if(!v.ini||!v.fin||!v.anos) return null; const tot=v.fin/v.ini-1, c=Math.pow(v.fin/v.ini,1/v.anos)-1;
      return {label:'Rentabilidad anual compuesta (CAGR)',big:p(c),rows:[['Rentabilidad total',p(tot)],['Ganancia',m(v.fin-v.ini)]]};},
    r72:v=>{if(v.tasa<=0) return null; return {label:'Años para duplicar tu dinero (regla del 72)',big:n(72/v.tasa,1)+' años',rows:[['Cálculo exacto',n(Math.log(2)/Math.log(1+v.tasa/100),1)+' años'],['Para triplicarlo (exacto)',n(Math.log(3)/Math.log(1+v.tasa/100),1)+' años']]};},
    inf:v=>{const f=Math.pow(1+v.inf/100,v.anos); return {label:`Necesitarás dentro de ${n(v.anos,0)} años`,big:m(v.cant*f),rows:[['Poder de compra futuro de '+m(v.cant,0),m(v.cant/f)],['Pérdida de poder adquisitivo',p(1-1/f)]]};},
    dep:v=>{const b=v.cap*(Math.pow(1+v.tae/100,v.meses/12)-1), r=b*v.ret/100; return {label:'Intereses netos',big:m(b-r),rows:[['Intereses brutos',m(b)],['Retención ('+n(v.ret)+' %)',m(r)],['Capital al vencimiento',m(v.cap+b-r)]]};},
    amort:v=>{const r=v.tin/1200, k=Math.round(v.anos*12); if(!v.pend||!k) return null; const c0=cuota(v.pend,r,k), P1=v.pend-v.amo; if(P1<=0) return {label:'Préstamo liquidado',big:m(0),rows:[]};
      const c1=cuota(P1,r,k); const k2= r===0? Math.ceil(P1/c0) : Math.ceil(-Math.log(1-P1*r/c0)/Math.log(1+r));
      const intBase=c0*k-v.pend;
      return {label:'Ahorro en intereses reduciendo plazo',big:m(intBase-(c0*k2-P1)),rows:[['Cuota actual',m(c0)],['Opción reducir cuota → nueva cuota',m(c1)],['Ahorro en intereses reduciendo cuota',m(intBase-(c1*k-P1))],['Opción reducir plazo → meses menos',n(k-k2,0)+' meses']]};},
    tarjeta:v=>{const r=Math.pow(1+v.tae/100,1/12)-1; if(v.pago<=v.deuda*r) return {label:'Con ese pago la deuda nunca se termina',big:'∞',rows:[['Interés del primer mes',m(v.deuda*r)]],note:'El pago mensual no cubre ni los intereses. Sube la cuota o busca refinanciar.'};
      let s=v.deuda,k=0,i=0; while(s>0.005&&k<1200){const x=s*r; i+=x; s=s+x-v.pago; k++;} return {label:'Tiempo para liquidar la deuda',big:(k>=12? n(k/12,1)+' años':k+' meses'),rows:[['Meses',n(k,0)],['Intereses totales',m(i)],['Total pagado',m(v.deuda+i)]]};},
    emerg:v=>{const obj=v.gasto*v.meses, falta=Math.max(0,obj-v.ahorro); return {label:'Tu fondo de emergencia',big:m(obj,0),rows:[['Te falta',m(falta,0)],['Tiempo para completarlo',falta? (v.aporte? n(Math.ceil(falta/v.aporte),0)+' meses':'—'):'¡Completado!']]};},
    hora:v=>{const h=v.horas*v.semanas; if(!h) return null; const bruto=(v.neto+v.gastos)/(1-v.imp/100); return {label:'Precio mínimo por hora',big:m(bruto/h),rows:[['Facturación anual necesaria',m(bruto,0)],['Horas facturables al año',n(h,0)],['Precio por día (8 h)',m(bruto/h*8)]]};},
    sueldo:v=>{const h=v.horas*52; return {label:'Sueldo bruto mensual ('+n(v.pagas,0)+' pagas)',big:m(v.anual/v.pagas),rows:[['Mensual prorrateado (12)',m(v.anual/12)],['Semanal',m(v.anual/52)],['Por hora',h?m(v.anual/h):'—']],note:'Importes brutos: el neto depende de las retenciones y cotizaciones de tu país.'};}
  };
  document.querySelectorAll('[data-tool]').forEach(sec=>{
    const fn=T[sec.dataset.tool], out=sec.querySelector('.res'), els=sec.querySelectorAll('input,select');
    const run=()=>{const v={}; els.forEach(e=>{const k=e.id.split('-').slice(1).join('-'); const x=parseFloat(String(e.value).replace(',','.')); v[k]= e.tagName==='SELECT'&&isNaN(x)? e.value : (isFinite(x)?x:0);});
      const r=fn(v); if(!r){out.innerHTML='<p class="note">Completa los datos.</p>';return;}
      out.innerHTML=`<div>${r.label}</div><div class="big">${r.big}</div><table>${r.rows.map(x=>`<tr><td>${x[0]}</td><td>${x[1]}</td></tr>`).join('')}</table>`+(r.note?`<p class="note">${r.note}</p>`:'');
      try{ if(window.gtag) gtag('event','calculo',{tool:sec.dataset.tool}); }catch(e){} };
    els.forEach(e=>{e.addEventListener('input',run);e.addEventListener('change',run);}); run();
  });
  window.NT=T;
})();
