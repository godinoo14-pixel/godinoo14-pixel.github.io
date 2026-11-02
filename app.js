/* Numeria — lógica de calculadoras (sin dependencias) */
(function(){
  const $ = id => document.getElementById(id);
  const num = id => { const el=$(id); if(!el) return 0; const v=parseFloat(String(el.value).replace(',','.')); return isFinite(v)?v:0; };
  const CUR = (document.documentElement.dataset.cur||'EUR');
  const money = (v,d=0) => v.toLocaleString('es-ES',{style:'currency',currency:CUR,minimumFractionDigits:d,maximumFractionDigits:d});
  const pct = (v,d=2) => (v*100).toLocaleString('es-ES',{minimumFractionDigits:d,maximumFractionDigits:d})+' %';
  const rows = arr => '<table>'+arr.map(r=>`<tr><td>${r[0]}</td><td>${r[1]}</td></tr>`).join('')+'</table>';
  const track = name => { try{ if(window.gtag) gtag('event','calculo',{tool:name}); }catch(e){} };
  function bind(ids, fn){ ids.forEach(id=>{ const el=$(id); if(el){ el.addEventListener('input',fn); el.addEventListener('change',fn);} }); fn(); }
  function bars(el, data){ // data: [{label, a, b}] a=aportado b=intereses
    const max=Math.max(...data.map(d=>d.a+d.b))||1;
    el.innerHTML='<div class="bars">'+data.map(d=>`<div class="bar" title="${d.label}: ${money(d.a+d.b)}"><span class="b" style="height:${d.b/max*100}%"></span><span class="a" style="height:${d.a/max*100}%"></span><em>${d.label}</em></div>`).join('')+'</div><div class="legend"><span class="la"></span>Aportado <span class="lb"></span>Intereses</div>';
  }

  /* ---------- Interés compuesto ---------- */
  function compuesto(ini, mensual, tasa, anos){
    const r=tasa/12; let s=ini, ap=ini; const serie=[];
    for(let m=1;m<=anos*12;m++){ s=s*(1+r)+mensual; ap+=mensual; if(m%12===0) serie.push({y:m/12,s,ap}); }
    return {final:s, aportado:ap, serie};
  }
  if($('ic')){
    bind(['ic-ini','ic-men','ic-tasa','ic-anos','ic-inf'],()=>{
      const anos=Math.min(60,Math.max(1,Math.round(num('ic-anos'))));
      const R=compuesto(num('ic-ini'),num('ic-men'),num('ic-tasa')/100,anos);
      const real=R.final/Math.pow(1+num('ic-inf')/100,anos);
      $('ic-out').innerHTML=`<div>Capital final</div><div class="big">${money(R.final)}</div>`+rows([
        ['Total aportado', money(R.aportado)],
        ['Intereses generados', money(R.final-R.aportado)],
        ['Valor en dinero de hoy (descontando inflación)', money(real)]
      ]);
      const step=Math.max(1,Math.ceil(anos/12));
      bars($('ic-chart'), R.serie.filter(p=>p.y%step===0||p.y===anos).map(p=>({label:p.y+'a',a:p.ap,b:p.s-p.ap})));
      track('interes-compuesto');
    });
  }

  /* ---------- Préstamo / hipoteca (sistema francés) ---------- */
  function cuota(P,r,n){ return r===0? P/n : P*r/(1-Math.pow(1+r,-n)); }
  function tae(neto,c,n){ let lo=0,hi=1; const f=i=>{let s=0;for(let k=1;k<=n;k++)s+=c/Math.pow(1+i,k);return s-neto;};
    if(f(0)<=0) return 0; for(let it=0;it<200;it++){const m=(lo+hi)/2; if(f(m)>0) lo=m; else hi=m;} return Math.pow(1+(lo+hi)/2,12)-1; }
  if($('hip')){
    bind(['hip-precio','hip-entrada','hip-tin','hip-anos','hip-ingresos'],()=>{
      const P=num('hip-precio')-num('hip-entrada'), n=Math.round(num('hip-anos')*12), r=num('hip-tin')/100/12;
      if(P<=0||n<=0){ $('hip-out').innerHTML='<p class="note">Revisa los importes.</p>'; return; }
      const c=cuota(P,r,n), ing=num('hip-ingresos'), ratio=ing? c/ing:0;
      $('hip-out').innerHTML=`<div>Cuota mensual</div><div class="big">${money(c,2)}</div>`+rows([
        ['Importe del préstamo', money(P)],
        ['Intereses totales', money(c*n-P)],
        ['Total a devolver', money(c*n)],
        ['% de la entrada sobre el precio', pct(num('hip-entrada')/num('hip-precio')||0,1)],
        ['Esfuerzo sobre ingresos netos', ing? pct(ratio,1)+(ratio>0.35?' ⚠️ alto':' ✔︎'):'—']
      ]);
      // amortización anual
      let saldo=P; const data=[]; const yrs=n/12, step=Math.max(1,Math.ceil(yrs/12));
      for(let y=1;y<=yrs;y++){ let ip=0,cp=0; for(let m=0;m<12;m++){const i=saldo*r; ip+=i; cp+=c-i; saldo-=c-i;} if(y%step===0||y===yrs) data.push({label:y+'a',a:cp,b:ip}); }
      bars($('hip-chart'), data); $('hip-chart').querySelector('.legend').innerHTML='<span class="la"></span>Capital amortizado <span class="lb"></span>Intereses (por año)';
      track('hipoteca');
    });
  }
  if($('pre')){
    bind(['pre-imp','pre-tin','pre-meses','pre-com'],()=>{
      const P=num('pre-imp'), n=Math.max(1,Math.round(num('pre-meses'))), r=num('pre-tin')/100/12, com=P*num('pre-com')/100;
      if(P<=0){ $('pre-out').innerHTML='<p class="note">Introduce el importe.</p>'; return; }
      const c=cuota(P,r,n), t=tae(P-com,c,n);
      $('pre-out').innerHTML=`<div>Cuota mensual</div><div class="big">${money(c,2)}</div>`+rows([
        ['Intereses totales', money(c*n-P,2)], ['Comisión de apertura', money(com,2)],
        ['Coste total del préstamo', money(c*n-P+com,2)], ['Total a devolver', money(c*n+com,2)], ['TAE real aproximada', pct(t)]
      ]);
      track('prestamo');
    });
  }

  /* ---------- Objetivo de ahorro ---------- */
  if($('ah')){
    bind(['ah-obj','ah-ini','ah-anos','ah-tasa'],()=>{
      const F=num('ah-obj'), ini=num('ah-ini'), n=Math.round(num('ah-anos')*12), r=num('ah-tasa')/100/12;
      if(!F||!n){ $('ah-out').innerHTML='<p class="note">Introduce objetivo y plazo.</p>'; return; }
      const fvIni=ini*Math.pow(1+r,n); const fac= r===0? n : (Math.pow(1+r,n)-1)/r;
      const m=Math.max(0,(F-fvIni)/fac);
      $('ah-out').innerHTML=`<div>Debes ahorrar cada mes</div><div class="big">${money(m,2)}</div>`+rows([
        ['Ahorro al día', money(m*12/365,2)], ['Total que aportarás', money(ini+m*n)], ['Lo que pondrá la rentabilidad', money(Math.max(0,F-ini-m*n))]
      ]);
      track('ahorro');
    });
  }

  /* ---------- Independencia financiera (FIRE) ---------- */
  if($('fire')){
    bind(['fi-gasto','fi-ahorro','fi-cap','fi-tasa','fi-retiro'],()=>{
      const gasto=num('fi-gasto')*12, retiro=num('fi-retiro')/100, objetivo= retiro? gasto/retiro:0;
      const r=num('fi-tasa')/100/12, aport=num('fi-ahorro'); let s=num('fi-cap'), m=0;
      while(s<objetivo && m<1200){ s=s*(1+r)+aport; m++; }
      const txt= m>=1200? 'Más de 100 años' : (m/12).toLocaleString('es-ES',{maximumFractionDigits:1})+' años';
      $('fire-out').innerHTML=`<div>Tiempo hasta la independencia financiera</div><div class="big">${txt}</div>`+rows([
        ['Capital necesario (gasto anual ÷ tasa de retiro)', money(objetivo)], ['Gasto anual cubierto', money(gasto)], ['Tasa de retiro', pct(retiro,1)]
      ]);
      track('fire');
    });
  }
  window.NM={compuesto,cuota,tae};
})();
