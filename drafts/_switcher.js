/* 시안 전환 플로팅 바 — 모든 drafts/<skill>/vN.html 에 공통 주입 */
(function () {
  var DRAFTS = [
    ['frontend-design', 'v1', 'Swiss Industrial'],
    ['frontend-design', 'v2', 'Warm Editorial Paper'],
    ['frontend-design', 'v3', 'Neo-Brutalist'],
    ['apple-design', 'v1', 'Apple Store Light'],
    ['apple-design', 'v2', 'Soft Gradient Glass'],
    ['apple-design', 'v3', 'Technical Blueprint'],
    ['design-taste-frontend', 'v1', 'Nordic Minimal'],
    ['design-taste-frontend', 'v2', 'Terminal / Data'],
    ['design-taste-frontend', 'v3', 'Bold Color Block'],
    ['impeccable', 'v1', 'Corporate Clean SaaS'],
    ['impeccable', 'v2', 'Steel & Copper'],
    ['impeccable', 'v3', 'Monochrome Magazine']
  ];
  var SKILL_LABEL = {
    'frontend-design': 'Frontend Design',
    'apple-design': 'Apple Design',
    'design-taste-frontend': 'Design Taste',
    'impeccable': 'Impeccable'
  };

  var path = decodeURIComponent(location.pathname).split('\\').join('/');
  var m = path.match(/drafts\/([^\/]+)\/(v\d+)\.html$/);
  var cur = -1;
  if (m) DRAFTS.forEach(function (d, i) { if (d[0] === m[1] && d[1] === m[2]) cur = i; });
  function hrefOf(i) { var d = DRAFTS[i]; return '../' + d[0] + '/' + d[1] + '.html'; }

  var css = [
    '#hone-switcher{position:fixed;left:50%;bottom:18px;transform:translateX(-50%);z-index:2147483000;font:12px/1 system-ui,"Noto Sans KR",sans-serif;display:flex;align-items:center;gap:6px;padding:6px 8px;border-radius:999px;background:rgba(14,15,24,.82);backdrop-filter:blur(14px) saturate(160%);-webkit-backdrop-filter:blur(14px) saturate(160%);border:1px solid rgba(255,255,255,.14);box-shadow:0 10px 40px rgba(0,0,0,.45);color:#e8e8ee;user-select:none;transition:transform .35s cubic-bezier(.2,.8,.2,1),opacity .3s}',
    '#hone-switcher.min{transform:translateX(-50%) translateY(calc(100% + 26px))}',
    '#hone-switcher .hs-btn{all:unset;box-sizing:border-box;display:inline-flex;align-items:center;justify-content:center;min-width:30px;height:30px;padding:0 9px;border-radius:999px;color:#cfd1dc;cursor:pointer;font-weight:600;font-variant-numeric:tabular-nums;position:relative;transition:background .15s,color .15s,transform .1s}',
    '#hone-switcher .hs-btn:hover{background:rgba(255,255,255,.1);color:#fff}',
    '#hone-switcher .hs-btn:active{transform:scale(.94)}',
    '#hone-switcher .hs-btn.on{background:#5b3df5;color:#fff}',
    '#hone-switcher .hs-btn[data-tip]:hover::after{content:attr(data-tip);position:absolute;bottom:calc(100% + 10px);left:50%;transform:translateX(-50%);white-space:nowrap;background:#0e0f18;color:#fff;padding:7px 10px;border-radius:8px;font-size:11px;font-weight:500;border:1px solid rgba(255,255,255,.14);pointer-events:none}',
    '#hone-switcher .hs-sep{width:1px;height:18px;background:rgba(255,255,255,.14);margin:0 2px}',
    '#hone-switcher .hs-arrow{font-size:14px;min-width:28px;padding:0}',
    '#hone-switcher .hs-home{font-size:11px;letter-spacing:.06em;color:#9aa0b8}',
    '#hone-switcher .hs-name{font-size:11px;color:#9aa0b8;padding:0 6px 0 2px;max-width:220px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}',
    '#hone-switcher-tab{position:fixed;left:50%;bottom:0;transform:translateX(-50%);z-index:2147483000;background:rgba(14,15,24,.85);color:#cfd1dc;border:1px solid rgba(255,255,255,.14);border-bottom:0;border-radius:10px 10px 0 0;padding:6px 14px;font:11px system-ui,sans-serif;cursor:pointer;display:none;backdrop-filter:blur(10px)}',
    '#hone-switcher-tab.show{display:block}',
    '@media (max-width:760px){#hone-switcher .hs-name,#hone-switcher .hs-home{display:none}#hone-switcher .hs-btn{min-width:26px;height:26px;padding:0 6px;font-size:11px}}'
  ].join('\n');
  var st = document.createElement('style');
  st.textContent = css;
  document.head.appendChild(st);

  var bar = document.createElement('nav');
  bar.id = 'hone-switcher';
  bar.setAttribute('aria-label', '시안 전환');
  var h = '';
  h += '<a class="hs-btn hs-home" href="../index.html" data-tip="시안 인덱스">INDEX</a><span class="hs-sep"></span>';
  h += '<button class="hs-btn hs-arrow" data-go="-1" data-tip="이전 시안 ( [ )">&#8249;</button>';
  var lastSkill = null;
  DRAFTS.forEach(function (d, i) {
    if (lastSkill && lastSkill !== d[0]) h += '<span class="hs-sep"></span>';
    lastSkill = d[0];
    h += '<a class="hs-btn' + (i === cur ? ' on' : '') + '" href="' + hrefOf(i) + '" data-tip="시안 ' + (i + 1) + ' · ' + SKILL_LABEL[d[0]] + ' · ' + d[2] + '">' + (i + 1) + '</a>';
  });
  h += '<button class="hs-btn hs-arrow" data-go="1" data-tip="다음 시안 ( ] )">&#8250;</button>';
  if (cur >= 0) h += '<span class="hs-sep"></span><span class="hs-name">' + SKILL_LABEL[DRAFTS[cur][0]] + ' · ' + DRAFTS[cur][2] + '</span>';
  h += '<button class="hs-btn hs-arrow" data-min="1" data-tip="숨기기">&#215;</button>';
  bar.innerHTML = h;

  var tab = document.createElement('button');
  tab.id = 'hone-switcher-tab';
  tab.textContent = '시안 ' + (cur + 1) + ' / ' + DRAFTS.length + ' ▴';
  document.body.appendChild(bar);
  document.body.appendChild(tab);

  function go(delta) {
    if (cur < 0) return;
    var n = (cur + delta + DRAFTS.length) % DRAFTS.length;
    location.href = hrefOf(n);
  }
  function minimize(on) {
    bar.classList.toggle('min', on);
    tab.classList.toggle('show', on);
    try { if (on) localStorage.setItem('hone-switcher-min', '1'); else localStorage.removeItem('hone-switcher-min'); } catch (_) {}
  }
  bar.addEventListener('click', function (e) {
    var b = e.target.closest('[data-go]');
    if (b) { go(parseInt(b.getAttribute('data-go'), 10)); return; }
    if (e.target.closest('[data-min]')) minimize(true);
  });
  tab.addEventListener('click', function () { minimize(false); });
  document.addEventListener('keydown', function (e) {
    if (e.target && /input|textarea|select/i.test(e.target.tagName)) return;
    if (e.ctrlKey || e.metaKey || e.altKey) return;
    if (e.key === ']') go(1);
    else if (e.key === '[') go(-1);
    else if (/^[1-9]$/.test(e.key)) { var n = parseInt(e.key, 10) - 1; if (n < DRAFTS.length) location.href = hrefOf(n); }
    else if (e.key === '0') { location.href = hrefOf(9); }
  });
  try { if (localStorage.getItem('hone-switcher-min')) minimize(true); } catch (_) {}
})();
