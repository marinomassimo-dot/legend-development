/* Curated layer: navigation, candidate profiles, research-priority groups, comparison, export. Reads D.cur (embedded JSON). No network. */
(function () {
'use strict';
var D = JSON.parse(document.getElementById('data').textContent);
var TITLE = document.title;
var C = D.cur, NEEDS = C.needs, CANDS = C.cands, META = C.meta;
var NM = {}, CM = {}, SC = {}, GR = {};
NEEDS.forEach(function (n) { NM[n.id] = n; });
CANDS.forEach(function (c) { CM[c.id] = c; });
C.scopes.forEach(function (s) { SC[s.code] = s; });
C.groups.forEach(function (g) { GR[g.id] = g; });
function $(id) { return document.getElementById(id); }
function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
function uniq(a) { var o = {}, r = []; a.forEach(function (x) { if (x != null && x !== '' && !o[x]) { o[x] = 1; r.push(x); } }); return r; }
var PUBMED = 'https://pubmed.ncbi.nlm.nih.gov/', CHEMBL = 'https://www.ebi.ac.uk/chembl/compound_report_card/', DOI = 'https://doi.org/';
function ext(url, text) { return '<a href="' + esc(url) + '" rel="noopener noreferrer">' + esc(text) + '</a>'; }
function pmidLink(id) { return ext(PUBMED + id + '/', 'PMID ' + id); }
function pmidFull(p) { return pmidLink(p.id) + ' <span class="url">' + esc(PUBMED + p.id + '/') + '</span>' + (p.title ? ' ' + esc(p.title) : '') + ' <span class="mut">(' + esc(p.role) + ')</span>'; }
function first(t, n) { t = String(t || '').replace(/\s+/g, ' ').trim(); if (t.length <= n) return t; var cut = t.slice(0, n), i = Math.max(cut.lastIndexOf('. '), cut.lastIndexOf('; ')); if (i > n * 0.5) return cut.slice(0, i + 1); return cut.slice(0, cut.lastIndexOf(' ')) + ' …'; }
function sc(code, n) { var s = SC[code] || { glyph: '?', label: String(code) }; return '<span class="sc s-' + esc(code) + '"><span class="gl" aria-hidden="true">' + esc(s.glyph) + '</span>' + esc(s.label) + (n != null ? ' ×' + n : '') + '</span>'; }
function grp(g) { return '<span class="grp ' + g.toLowerCase() + '" title="' + esc(GR[g].why) + '">' + esc(GR[g].label.split(':')[0]) + '</span>'; }
function chip(t, cls) { return '<span class="chip' + (cls ? ' ' + cls : '') + '">' + esc(t) + '</span>'; }
function goalTxt(g) { return g ? (g === 'deep_recovery' ? 'Aim: broad, durable recovery' : 'Aim: useful partial benefit') : 'Aim: not stated'; }
function trackTxt(t) { return t ? 'Track ' + t + (t === 'A' ? ' (variant-independent)' : ' (variant- or lesion-specific)') : 'Track: not stated in the card'; }
function more(shortT, fullT) { shortT = shortT || ''; fullT = fullT || ''; if (!fullT || fullT.replace(/\s+/g, ' ') === shortT.replace(/\s+/g, ' ') || fullT.length <= shortT.length + 3) return esc(shortT); return esc(shortT) + ' <details class="inl"><summary>full text</summary>' + esc(fullT) + '</details>'; }

// ---------------------------------------------------------------- filters
var CF = { thread: '', need: '', access: '', country: '', scope: '', track: '', goal: '', status: '', q: '' };
var RK = { mode: 'need', sort: 'group' };
var SEL = [];
var IDS = { thread: 'c-thread', need: 'c-need', access: 'c-access', country: 'c-country', scope: 'c-scope', track: 'c-track', goal: 'c-goal', status: 'c-status', q: 'c-q' };
function opt(sel, pairs, all) { sel.innerHTML = '<option value="">' + esc(all) + '</option>' + pairs.map(function (p) { return '<option value="' + esc(p[0]) + '">' + esc(p[1]) + '</option>'; }).join(''); }
opt($('c-thread'), C.threads.map(function (t) { return [t.id, t.name]; }), 'any biological area');
opt($('c-need'), NEEDS.map(function (n) { return [n.id, n.id.replace('NEED-', '') + ' – ' + n.short]; }), 'any need');
opt($('c-access'), uniq([].concat.apply([], CANDS.map(function (c) { return c.access; }))).sort().map(function (a) { return [a, a]; }), 'any access category');
opt($('c-country'), uniq(CANDS.map(function (c) { return c.country; })).sort().map(function (a) { return [a, a]; }), 'any country evidence');
opt($('c-scope'), C.scopes.filter(function (s) { return CANDS.some(function (c) { return (c.scope_counts.int[s.code] || c.scope_counts.need[s.code]); }) || NEEDS.some(function (n) { return n.scopes.indexOf(s.code) >= 0; }); }).map(function (s) { return [s.code, s.glyph + ' ' + s.label]; }), 'any evidence scope');
opt($('c-track'), [['A', 'Track A (variant-independent)'], ['B', 'Track B (variant- or lesion-specific)']], 'any Track');
opt($('c-goal'), Object.keys(C.goals).map(function (g) { return [g, C.goals[g]]; }), 'any recovery goal');
opt($('c-status'), uniq(CANDS.map(function (c) { return c.status; })).sort().map(function (a) { return [a, a]; }), 'any research status');
function candActive() { return !!(CF.access || CF.country || CF.status); }
function candOk(c) {
  if (CF.thread && !c.needs.some(function (n) { return NM[n].thread === CF.thread; })) return false;
  if (CF.need && c.needs.indexOf(CF.need) < 0) return false;
  if (CF.access && c.access.indexOf(CF.access) < 0) return false;
  if (CF.country && c.country !== CF.country) return false;
  if (CF.scope && !(c.scope_counts.int[CF.scope] || c.scope_counts.need[CF.scope])) return false;
  if (CF.track && !(c.track === CF.track || c.tracks.indexOf(CF.track) >= 0)) return false;
  if (CF.goal && c.goal !== CF.goal) return false;
  if (CF.status && c.status !== CF.status) return false;
  if (CF.q) { var t = (c.name + ' ' + c.id + ' ' + c.chembl.join(' ') + ' ' + c.needs.join(' ') + ' ' + c.why).toLowerCase(); var w = CF.q.toLowerCase().split(/\s+/); for (var i = 0; i < w.length; i++) if (w[i] && t.indexOf(w[i]) < 0) return false; }
  return true;
}
function needOk(n) {
  if (CF.thread && n.thread !== CF.thread) return false;
  if (CF.need && n.id !== CF.need) return false;
  if (CF.track && n.track !== CF.track) return false;
  if (CF.goal && n.goal !== CF.goal) return false;
  if (CF.scope && n.scopes.indexOf(CF.scope) < 0 && !n.cards.some(function (id) { return CM[id].scope_counts.int[CF.scope]; })) return false;
  if (candActive() || CF.q) { if (!n.cards.some(function (id) { return candOk(CM[id]); })) return false; }
  return true;
}

// ---------------------------------------------------------------- navigation: need -> mechanism -> compounds -> evidence -> next question
function bestCands(n) { return n.cards.map(function (id) { return CM[id]; }).filter(candOk).sort(function (a, b) { return a.links[n.id].group.localeCompare(b.links[n.id].group) || a.short.localeCompare(b.short); }); }
function navRow(n) {
  var cs = bestCands(n), ob = {};
  n.obs.forEach(function (o) { ob[o.scope] = (ob[o.scope] || 0) + 1; });
  var nx = '';
  for (var i = 0; i < cs.length; i++) { if (cs[i].next && !cs[i].abstention) { nx = '<b>' + esc(cs[i].short) + ':</b> ' + esc(first(cs[i].next, 230)); break; } }
  if (!nx) nx = cs.length && cs[0].missing ? '<b>' + esc(cs[0].short) + ' (missing datum):</b> ' + esc(first(cs[0].missing, 200)) : '<span class="mut">No candidate card names a next step for this need.</span>';
  return '<article class="navrow" data-need="' + esc(n.id) + '" aria-label="' + esc(n.short) + '">' +
    '<div><span class="lab">Need</span><b>' + esc(n.short) + '</b><div class="mut">' + esc(n.id) + '</div>' + chip(goalTxt(n.goal)) + chip(trackTxt(n.track)) + '</div>' +
    '<div><span class="lab">Mechanism (what would be moved)</span>' + (n.dir ? 'Wanted direction: <b>' + esc(n.dir) + '</b> on ' + esc(n.dir_on) : '') + (n.uncertain ? ' <span class="chip">uncertain sign: exploration only</span>' : '') +
    '<div class="mini">Targets: ' + esc(n.targets.join(', ') || 'none listed') + '</div></div>' +
    '<div><span class="lab">Compounds and interventions (candidate cards)</span>' + (cs.length ? cs.map(function (c) { return '<button type="button" class="chip ' + c.links[n.id].group.toLowerCase() + '" data-open="' + esc(c.id) + '">' + esc(c.short) + ' – ' + esc(GR[c.links[n.id].group].label.split(':')[0]) + '</button>'; }).join(' ') : '<span class="mut">none with a card (' + n.fam_link + ' catalogue families have a documented link; links are not candidates)</span>') + '</div>' +
    '<div><span class="lab">Evidence (observations in the need record)</span>' + (Object.keys(ob).length ? Object.keys(ob).map(function (k) { return sc(k, ob[k]); }).join('') : '<span class="mut">no observation recorded</span>') +
    '<div class="mini">' + n.n_wwox_obs + ' in a WWOX system (' + n.n_case_obs + ' of them uncontrolled case reports); counter-evidence items on the need: ' + n.counter.length + '</div></div>' +
    '<div><span class="lab">Next question</span><span class="mini">' + nx + '</span></div></article>';
}
function renderNav() {
  var ns = NEEDS.filter(needOk), out = '';
  C.threads.forEach(function (t) {
    var inT = ns.filter(function (n) { return n.thread === t.id; });
    if (inT.length) out += '<h3>' + esc(t.name) + ' <span class="mut">(' + inT.length + ' of ' + t.needs.length + ' needs shown)</span></h3>' + inT.map(navRow).join('');
  });
  $('nav-list').innerHTML = out || '<p class="state-none">No need matches these filters (a filter result, not a finding).</p>';
  var cs = CANDS.filter(candOk);
  $('c-count').textContent = ns.length + ' of ' + NEEDS.length + ' needs and ' + cs.length + ' of ' + CANDS.length + ' candidate cards match';
  Array.prototype.forEach.call($('nav-list').querySelectorAll('[data-open]'), function (b) { b.onclick = function () { openCand(b.dataset.open); }; });
}

// ---------------------------------------------------------------- candidate profile
function obsLine(o) { return '<li>' + sc(o.scope) + ' ' + esc(o.short) + (o.pmid ? ' ' + pmidLink(o.pmid) : '') + (o.limits ? ' <span class="mut">Limits: ' + esc(o.limits) + '</span>' : '') + '</li>'; }
function asLine(a) { return '<li>' + sc(a.scope) + ' ' + esc(a.text) + (a.note ? ' <span class="mini">\u2013 ' + esc(a.note) + '</span>' : '') + (a.species ? ' <span class="mut">[' + esc(a.species) + (a.genotype ? ', ' + esc(first(a.genotype, 70)) : '') + ']</span>' : '') + (a.pmids.length ? ' ' + a.pmids.map(pmidLink).join(' ') : '') + '</li>'; }
var WWOX_SC = { WWOX_EXPERIMENT_IN_DEE_SYSTEM: 1, WWOX_CLINICAL_CASE: 1 };
function bySpec(c) { return c.needs.slice().sort(function (a, b) { return NM[a].cards.length - NM[b].cards.length || a.localeCompare(b); }); }
function profileParts(c) {
  var needsObs = []; bySpec(c).forEach(function (nid) { NM[nid].obs.forEach(function (o) { needsObs.push(o); }); });
  var wObs = needsObs.filter(function (o) { return o.scope === 'WWOX_EXPERIMENT_IN_DEE_SYSTEM' || o.scope === 'WWOX_CLINICAL_CASE'; });
  var oObs = needsObs.filter(function (o) { return !(o.scope === 'WWOX_EXPERIMENT_IN_DEE_SYSTEM' || o.scope === 'WWOX_CLINICAL_CASE'); });
  var own = c.asserts.filter(function (a) { return WWOX_SC[a.scope]; });
  var other = c.asserts.filter(function (a) { return !WWOX_SC[a.scope] && a.scope !== 'SAFETY_SIGNAL'; });
  var safety = c.asserts.filter(function (a) { return a.scope === 'SAFETY_SIGNAL'; });
  var counter = []; c.needs.forEach(function (nid) { NM[nid].counter.forEach(function (t) { counter.push(t); }); });
  var q = {};
  q.why = '<p>' + more(c.why, c.why_full) + '</p>' + (c.needs.length ? '<p class="mini">Needs it would address: ' + c.needs.map(function (n) { return esc(NM[n].short); }).join('; ') + '.</p>' : '<p class="mini">No need is linked to this card.</p>');
  q.wwox = (own.length ? '<p class="mini"><b>This intervention, tested in a WWOX system:</b></p><ul>' + own.slice(0, 3).map(asLine).join('') + '</ul>' + (own.length > 3 ? '<p class="mini">' + (own.length - 3) + ' more in the technical details.</p>' : '') : '<p class="mini"><b>No readout of this intervention in a WWOX system is recorded in its card.</b></p>') +
    (wObs.length ? '<p class="mini"><b>Observations on the linked need(s) in WWOX systems (context: they may concern other interventions):</b></p><ul>' + wObs.slice(0, 2).map(obsLine).join('') + '</ul>' + (wObs.length > 2 ? '<p class="mini">' + (wObs.length - 2) + ' more in the technical details.</p>' : '') : '<p class="mini">The linked needs hold no WWOX-system observation.</p>');
  var oth = other.slice(0, 2).map(asLine).concat(oObs.slice(0, 2).map(obsLine));
  q.other = oth.length ? '<ul>' + oth.join('') + '</ul>' + ((other.length + oObs.length) > oth.length ? '<p class="mini">' + (other.length + oObs.length - oth.length) + ' more in the technical details.</p>' : '') : '<p class="mini">None recorded.</p>';
  var ag = c.against.slice(0, 3).map(function (t) { return '<li>' + esc(first(t, 260)) + '</li>'; }).concat(counter.slice(0, 2).map(function (t) { return '<li><span class="mut">need:</span> ' + esc(first(t, 240)) + '</li>'; })).concat(safety.slice(0, 1).map(asLine));
  q.counter = (ag.length ? '<ul>' + ag.join('') + '</ul>' : '') + (c.against_note ? '<p class="mini">As written in the card (pro and contra together, not itemised): ' + esc(first(c.against_note, 330)) + '</p>' : '') + ((!ag.length && !c.against_note) ? '<p class="mini">No counter-evidence is itemised in this card (absence in the card is not a negative finding).</p>' : '') +
    ((c.against.length + counter.length) > 5 ? '<p class="mini">' + (c.against.length + counter.length - 5) + ' more in the technical details.</p>' : '');
  q.miss = '<p>' + (c.missing ? '<b>Missing datum:</b> ' + esc(first(c.missing, 260)) : 'No missing datum is stated.') + '</p>' + (c.next ? '<p><b>Informative next step:</b> ' + more(c.next, c.next_full) + '</p>' : '<p class="mini">No next step is named (abstention or axis card).</p>') + (c.reopen ? '<p class="mini">Reopening condition: ' + esc(c.reopen) + '</p>' : '');
  return q;
}
function techDetails(c) {
  var h = '<details class="tech"><summary>Technical details and full tables</summary>';
  h += '<h4>Identity and mechanism (as written in the card)</h4><p class="mini">' + esc(c.identity) + '</p><p class="mini"><b>Mechanism:</b> ' + esc(c.mechanism) + '</p><p class="mini"><b>Novelty and known roads:</b> ' + esc(c.novelty) + '</p><p class="mini"><b>Pharmacology:</b> ' + esc(c.pharm) + '</p><p class="mini"><b>Access:</b> ' + esc(c.access_text) + '</p>';
  h += '<h4>All needs it is linked to, and why it sits in its group</h4><table class="tbl"><thead><tr><th>Need</th><th>Group</th><th>Criteria</th></tr></thead><tbody>' + c.needs.map(function (nid) { var l = c.links[nid]; return '<tr><td>' + esc(NM[nid].short) + '<div class="mut">' + esc(nid) + '</div></td><td>' + grp(l.group) + '</td><td><ul>' + l.reasons.map(function (r) { return '<li><b>' + esc(r[0]) + ':</b> ' + esc(r[1]) + '</li>'; }).join('') + '</ul></td></tr>'; }).join('') + '</tbody></table>';
  if (c.asserts.length) h += '<h4>Intervention-side assertions in the card (' + c.asserts.length + ')</h4><table class="tbl"><thead><tr><th>Scope</th><th>Statement</th><th>System</th><th>Reading depth</th><th>Sources</th></tr></thead><tbody>' + c.asserts.map(function (a) { return '<tr><td>' + sc(a.scope) + '</td><td>' + esc(a.text) + '<div class="mini">' + more(a.note, a.note_full) + '</div></td><td>' + esc([a.species, a.system, a.genotype].filter(Boolean).join('; ')) + '</td><td>' + esc(a.depth || '') + '</td><td>' + (a.pmids.map(pmidLink).join(' ') || '') + '</td></tr>'; }).join('') + '</tbody></table>';
  var allW = []; c.needs.forEach(function (nid) { NM[nid].obs.forEach(function (o) { allW.push([nid, o]); }); });
  if (allW.length) h += '<h4>Observations in the linked need records (' + allW.length + ')</h4><ul>' + allW.map(function (x) { return obsLine(x[1]).replace('<li>', '<li><span class="mut">' + esc(NM[x[0]].short) + ':</span> '); }).join('') + '</ul>';
  if (c.against.length) h += '<h4>All counter-evidence items of the card (' + c.against.length + ')</h4><ul>' + c.against.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>';
  if (c.for.length) h += '<h4>Evidence in favour, as written in the card</h4><ul>' + c.for.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>';
  if (c.not_known.length) h += '<h4>Not known</h4><ul>' + c.not_known.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>';
  if (c.actions.length) h += '<h4>Catalogue actions on need targets (source statements, not modulation in a WWOX system)</h4><table class="tbl"><thead><tr><th>Need</th><th>Target</th><th>Action</th><th>Relation to the wanted direction</th></tr></thead><tbody>' + c.actions.map(function (a) { return '<tr><td>' + esc((NM[a.need] || { short: a.need }).short) + '</td><td>' + esc(a.target) + '</td><td>' + esc(a.action) + '</td><td>' + (/oppos/.test(a.cons) ? '<span class="opp">OPPOSED to the wanted direction</span>' : esc(String(a.cons).replace(/_/g, ' '))) + '</td></tr>'; }).join('') + '</tbody></table>';
  h += '<h4>Sources by public identifier</h4>' + sourcesHtml(c) + '<p class="mini">Card file (repository-relative, local use only): <code>' + esc(c.card_path) + '</code>. Assessment: ' + esc(c.assessment) + '; bridge direction summary: ' + esc(c.summary) + '.</p>';
  return h + '</details>';
}
function sourcesHtml(c) {
  var h = '<ul class="srcs">';
  c.pmids.forEach(function (p) { h += '<li>' + pmidFull(p) + '</li>'; });
  c.chembl.forEach(function (id) { h += '<li>' + ext(CHEMBL + id + '/', 'ChEMBL ' + id) + ' <span class="url">' + esc(CHEMBL + id + '/') + '</span> <span class="mut">(compound identity)</span></li>'; });
  c.dois.forEach(function (d) { h += '<li>' + ext(DOI + d, 'DOI ' + d) + ' <span class="url">' + esc(DOI + d) + '</span></li>'; });
  if (!c.pmids.length && !c.chembl.length && !c.dois.length) h += '<li class="mut">No public identifier is attached to this card.</li>';
  return h + '</ul>';
}
function candHtml(c) {
  var q = profileParts(c), sel = SEL.indexOf(c.id) >= 0, gl = uniq(c.needs.map(function (n) { return c.links[n].group; }).sort());
  var scopes = {}; Object.keys(c.scope_counts.int).forEach(function (k) { scopes[k] = (scopes[k] || 0) + c.scope_counts.int[k]; });
  return '<article class="cand" id="cand-' + esc(c.id) + '" data-cand="' + esc(c.id) + '"><h3>' + esc(c.short) + ' <span class="mut">' + esc(c.id) + '</span></h3>' +
    '<div>' + (gl.length ? gl.map(grp).join('') : grp('G4')) + chip(goalTxt(c.goal)) + chip(trackTxt(c.track)) + chip('Status: ' + c.status) + (c.access.length ? chip('Access (US evidence): ' + c.access.join(', ')) : chip('Access: no catalogue identity or no evidence obtained')) + '</div>' +
    '<div>' + (Object.keys(scopes).length ? Object.keys(scopes).map(function (k) { return sc(k, scopes[k]); }).join('') : '<span class="mini mut">No intervention-side assertion carries a scope in this card.</span>') + '</div>' +
    '<div class="btns noprint"><label><input type="checkbox" data-sel="' + esc(c.id) + '"' + (sel ? ' checked' : '') + '> select for comparison or export</label><button type="button" data-export="' + esc(c.id) + '">Export this card (print / PDF)</button></div>' +
    '<div class="qa"><div><h4>1. Why are we studying it?</h4>' + q.why + '</div><div><h4>2. What was observed in WWOX?</h4>' + q.wwox + '</div><div><h4>3. What comes from other diseases or predictions?</h4>' + q.other + '</div><div><h4>4. Counter-evidence</h4>' + q.counter + '</div><div><h4>5. What proof is missing, and which step would be informative?</h4>' + q.miss + '</div></div>' + techDetails(c) + '</article>';
}
var CSORT = 'group';
function renderCands() {
  var cs = CANDS.filter(candOk);
  if (CSORT === 'name') cs.sort(function (a, b) { return a.short.localeCompare(b.short); });
  else cs.sort(function (a, b) { return a.group.localeCompare(b.group) || a.short.localeCompare(b.short); });
  $('cand-list').innerHTML = cs.length ? cs.map(candHtml).join('') : '<p class="state-none">No candidate card matches these filters.</p>';
  $('cand-n').textContent = cs.length;
  wireCands($('cand-list'));
  renderSel();
}
function wireCands(root) {
  Array.prototype.forEach.call(root.querySelectorAll('[data-sel]'), function (b) { b.onchange = function () { toggleSel(b.dataset.sel, b.checked); }; });
  Array.prototype.forEach.call(root.querySelectorAll('[data-export]'), function (b) { b.onclick = function () { location.hash = '#export=' + b.dataset.export; }; });
}
function openCand(id) {
  if (!candOk(CM[id])) { Object.keys(CF).forEach(function (k) { CF[k] = ''; }); syncCtl(); renderAll(); }
  var el = $('cand-' + id); if (!el) return;
  el.scrollIntoView(); var h = el.querySelector('h3'); h.setAttribute('tabindex', '-1'); h.focus();
}

// ---------------------------------------------------------------- research-priority groups
function sortItems(a) {
  var s = RK.sort;
  return a.sort(function (x, y) {
    if (s === 'name') return x.c.short.localeCompare(y.c.short);
    if (s === 'wwox') return (y.l.n_w + y.l.n_c) - (x.l.n_w + x.l.n_c) || x.c.short.localeCompare(y.c.short);
    if (s === 'counter') return (y.c.against.length + NM[y.n].counter.length) - (x.c.against.length + NM[x.n].counter.length) || x.c.short.localeCompare(y.c.short);
    return x.c.short.localeCompare(y.c.short);
  });
}
function rkItem(it, showNeed) {
  var c = it.c, l = it.l, n = NM[it.n];
  var sum = l.reasons[0][1] + '. Counter-evidence: ' + (c.against.length + n.counter.length) + ' item(s)' + (c.against_note && !c.against.length ? ' (prose)' : '') + '. Next step: ' + (l.reasons[5][1]) + '.';
  return '<div class="rk-item" data-cand="' + esc(c.id) + '" data-need="' + esc(n.id) + '"><b>' + esc(c.short) + '</b>' + (showNeed ? ' <span class="mut">for ' + esc(n.short) + '</span>' : '') + ' ' + grp(l.group) + (c.goal !== n.goal && c.goal ? ' ' + chip('card aim differs from the need aim', '') : '') +
    '<div class="sum">' + esc(sum) + '</div><details><summary>reasons for this position (six criteria)</summary><ul>' + l.reasons.map(function (r) { return '<li><b>' + esc(r[0]) + ':</b> ' + esc(r[1]) + '</li>'; }).join('') + '</ul><button type="button" class="chip" data-open="' + esc(c.id) + '">open the candidate profile</button></details></div>';
}
function groupBlock(items, showNeed) {
  var h = '';
  C.groups.forEach(function (g) {
    var it = sortItems(items.filter(function (x) { return x.l.group === g.id; }));
    if (it.length) h += '<div class="rk-group" data-group="' + g.id + '"><h3>' + grp(g.id) + ' ' + esc(g.label.split(': ')[1]) + ' <span class="mut">(' + it.length + ' link' + (it.length > 1 ? 's' : '') + ')</span></h3><p class="mini mut">' + esc(g.why) + '</p>' + it.map(function (x) { return rkItem(x, showNeed); }).join('') + '</div>';
  });
  return h || '<p class="mini mut">No candidate link.</p>';
}
function renderRank() {
  var links = [];
  CANDS.forEach(function (c) { if (candOk(c)) c.needs.forEach(function (n) { if (needOk(NM[n])) links.push({ c: c, n: n, l: c.links[n] }); }); });
  var h = '';
  if (RK.mode === 'need') {
    NEEDS.filter(needOk).forEach(function (n) {
      var it = links.filter(function (x) { return x.n === n.id; });
      h += '<section class="rk-need" data-need="' + esc(n.id) + '"><h3>' + esc(n.short) + ' <span class="mut">' + esc(n.id) + ' – ' + esc(goalTxt(n.goal)) + '</span></h3>' + (it.length ? groupBlock(it, false) : '<p class="mini mut">No candidate card is linked to this need. Catalogue links exist for ' + n.fam_link + ' families, but a link is a source statement and not a candidate.</p>') + '</section>';
    });
    var orphan = CANDS.filter(function (c) { return candOk(c) && !c.needs.length && !CF.need && !CF.thread; });
    if (orphan.length) h += '<section class="rk-need"><h3>Axis cards with no linked need</h3><p class="mini mut">Endpoint or anchor axes: no group applies, listed so that the full list stays reachable.</p>' + orphan.sort(function (a, b) { return a.short.localeCompare(b.short); }).map(function (c) { return '<div class="rk-item"><b>' + esc(c.short) + '</b> ' + chip('no linked need') + ' ' + esc(first(c.missing || '', 200)) + ' <button type="button" class="chip" data-open="' + esc(c.id) + '">open</button></div>'; }).join('') + '</section>';
  } else {
    Object.keys(C.goals).forEach(function (g) {
      var it = links.filter(function (x) { return NM[x.n].goal === g; });
      h += '<section class="rk-need" data-goal="' + g + '"><h3>' + esc(C.goals[g]) + ' <span class="mut">(needs whose aim is this; ' + it.length + ' candidate-need links)</span></h3>' + groupBlock(it, true) + '</section>';
    });
  }
  $('rk-list').innerHTML = h || '<p class="state-none">Nothing matches these filters.</p>';
  Array.prototype.forEach.call($('rk-list').querySelectorAll('[data-open]'), function (b) { b.onclick = function () { openCand(b.dataset.open); }; });
}

// ---------------------------------------------------------------- selection and comparison
function toggleSel(id, on) {
  var i = SEL.indexOf(id);
  if (on && i < 0) { if (SEL.length >= 4) { alert('At most four cards can be compared. Remove one first.'); renderCands(); return; } SEL.push(id); }
  if (!on && i >= 0) SEL.splice(i, 1);
  renderSel();
  Array.prototype.forEach.call(document.querySelectorAll('[data-sel]'), function (b) { b.checked = SEL.indexOf(b.dataset.sel) >= 0; });
}
function sgn(d) { return d === 'up' || d === 'restore' ? 1 : (d === 'down' ? -1 : 0); }
function renderSel() {
  $('sel-bar').innerHTML = SEL.length ? SEL.map(function (id) { return chip(CM[id].short); }).join(' ') + ' <button type="button" id="sel-clear">clear selection</button> <button type="button" id="sel-export">Export selected (print / PDF)</button>' : '<span class="mut">No card selected. Tick "select for comparison or export" on two to four candidate cards.</span>';
  if ($('sel-clear')) $('sel-clear').onclick = function () { SEL = []; renderCands(); };
  if ($('sel-export')) $('sel-export').onclick = function () { location.hash = '#export=' + SEL.join(','); };
  renderCompare();
}
function renderCompare() {
  var box = $('cmp-out');
  if (SEL.length < 2) { box.innerHTML = '<p class="mut">Select two to four cards to compare.</p>'; return; }
  var cs = SEL.map(function (id) { return CM[id]; });
  function row(label, fn) { return '<tr><th scope="row">' + label + '</th>' + cs.map(function (c) { return '<td>' + fn(c) + '</td>'; }).join('') + '</tr>'; }
  var h = '<div class="cmpwrap"><table class="cmp"><caption class="sr">Comparison of ' + cs.length + ' candidate cards</caption><thead><tr><th scope="col">Dimension</th>' + cs.map(function (c) { return '<th scope="col">' + esc(c.short) + '<div class="mut">' + esc(c.id) + '</div></th>'; }).join('') + '</tr></thead><tbody>';
  h += row('Recovery aim', function (c) { return esc(goalTxt(c.goal)); });
  h += row('Track', function (c) { return esc(trackTxt(c.track)); });
  h += row('Status and group', function (c) { return esc(c.status) + '<br>' + uniq(c.needs.map(function (n) { return c.links[n].group; })).sort().map(grp).join('') + (c.needs.length ? '' : '<span class="mut">no linked need</span>'); });
  h += row('Needs aimed at (wanted direction)', function (c) { return c.needs.length ? '<ul>' + c.needs.map(function (n) { return '<li>' + esc(NM[n].short) + ': <b>' + esc(NM[n].dir || '?') + '</b> on ' + esc(first(NM[n].dir_on || '', 70)) + '</li>'; }).join('') + '</ul>' : '<span class="mut">none</span>'; });
  h += row('Catalogue actions on need targets', function (c) { return c.actions.length ? '<ul>' + c.actions.slice(0, 8).map(function (a) { return '<li>' + esc(a.target) + ': ' + esc(a.action) + ' ' + (/oppos/.test(a.cons) ? '<span class="opp">OPPOSED to the wanted direction</span>' : '<span class="mini">(' + esc(String(a.cons).replace(/_/g, ' ')) + ')</span>') + '</li>'; }).join('') + '</ul>' + (c.actions.length > 8 ? '<span class="mini">+' + (c.actions.length - 8) + ' more</span>' : '') : '<span class="mut">no catalogue action rows (class, gene-based or axis card: direction comes from the need record)</span>'; });
  h += row('Evidence scopes (assertions in the card)', function (c) { var k = Object.keys(c.scope_counts.int); return k.length ? k.map(function (s) { return sc(s, c.scope_counts.int[s]); }).join('') : '<span class="mut">none scoped</span>'; });
  h += row('Counter-evidence items in the card', function (c) { return String(c.against.length) + (c.against_note && !c.against.length ? ' (prose only)' : ''); });
  h += row('Missing datum', function (c) { return esc(first(c.missing || 'none stated', 200)); });
  h += '</tbody></table></div>';
  // overlaps, complementarity, opposition
  var shared = cs[0].needs.filter(function (n) { return cs.every(function (c) { return c.needs.indexOf(n) >= 0; }); });
  var anyShared = uniq([].concat.apply([], cs.map(function (c) { return c.needs; }))).filter(function (n) { return cs.filter(function (c) { return c.needs.indexOf(n) >= 0; }).length >= 2; });
  var tg = {}; cs.forEach(function (c) { c.needs.forEach(function (n) { NM[n].targets.forEach(function (t) { (tg[t] = tg[t] || {})[c.id] = 1; }); }); });
  var sharedT = Object.keys(tg).filter(function (t) { return Object.keys(tg[t]).length >= 2; });
  var only = cs.map(function (c) { return [c, c.needs.filter(function (n) { return !cs.some(function (d) { return d !== c && d.needs.indexOf(n) >= 0; }); })]; });
  var opp = [];
  cs.forEach(function (c) { c.actions.forEach(function (a) { if (/oppos/.test(a.cons)) opp.push('<b>' + esc(c.short) + '</b> acts on ' + esc(a.target) + ' (' + esc(a.action) + ') opposite to the direction wanted for ' + esc((NM[a.need] || { short: a.need }).short)); }); });
  var byT = {};
  cs.forEach(function (c) { c.actions.forEach(function (a) { var s = a.action === 'up' ? 1 : (a.action === 'down' ? -1 : 0); if (s) (byT[a.target] = byT[a.target] || []).push([c, s]); }); });
  Object.keys(byT).forEach(function (t) { var u = byT[t].filter(function (x) { return x[1] > 0 && true; }), d = byT[t].filter(function (x) { return x[1] < 0; }); if (u.length && d.length) opp.push('On <b>' + esc(t) + '</b>, <b>' + esc(u[0][0].short) + '</b> raises while <b>' + esc(d[0][0].short) + '</b> lowers (catalogue action rows)'); });
  var wd = {};
  cs.forEach(function (c) { c.needs.forEach(function (n) { NM[n].targets.forEach(function (t) { var s = sgn(NM[n].dir); if (s) (wd[t] = wd[t] || []).push([c, n, s]); }); }); });
  Object.keys(wd).forEach(function (t) { var u = wd[t].filter(function (x) { return x[2] > 0; }), d = wd[t].filter(function (x) { return x[2] < 0; }); if (u.length && d.length && u[0][0] !== d[0][0]) opp.push('Wanted direction on <b>' + esc(t) + '</b> differs between needs: ' + esc(NM[u[0][1]].short) + ' (' + esc(NM[u[0][1]].dir) + ', card ' + esc(u[0][0].short) + ') versus ' + esc(NM[d[0][1]].short) + ' (' + esc(NM[d[0][1]].dir) + ', card ' + esc(d[0][0].short) + ')'); });
  h += '<h3>Overlap</h3><p>Needs shared by all selected cards: ' + (shared.length ? shared.map(function (n) { return esc(NM[n].short); }).join('; ') : '<b>none</b>') + '. Needs shared by at least two: ' + (anyShared.length ? anyShared.map(function (n) { return esc(NM[n].short); }).join('; ') : 'none') + '. Targets in common between the needs of two or more cards: ' + (sharedT.length ? esc(sharedT.join(', ')) : 'none') + '.</p>';
  h += '<h3>Complementarity (different needs, not a joint effect)</h3><ul>' + only.map(function (x) { return '<li><b>' + esc(x[0].short) + '</b> alone covers: ' + (x[1].length ? x[1].map(function (n) { return esc(NM[n].short); }).join('; ') : 'nothing that the others do not also cover') + '</li>'; }).join('') + '</ul>';
  h += '<h3>Opposed actions</h3>' + (opp.length ? '<ul data-opposed="' + opp.length + '">' + opp.map(function (t) { return '<li><span class="opp">OPPOSED</span> ' + t + '</li>'; }).join('') + '</ul>' : '<p data-opposed="0">No opposed action is recorded among these cards in the catalogue rows or in the wanted directions of their needs. This is a statement about the data held, not a finding that none exists.</p>');
  h += '<p class="note"><b>No synergy is inferred.</b> Sharing a need or covering different needs says nothing about whether the interventions work together; interactions, doses and combined safety are not assessed here.</p>';
  box.innerHTML = h;
}

// ---------------------------------------------------------------- export (print / PDF / standalone HTML)
var EXCSS = 'body{font:12px/1.45 system-ui,Segoe UI,Roboto,sans-serif;color:#111;background:#fff;margin:0;padding:14px}.xc{border:1px solid #888;border-radius:6px;padding:10px 14px;margin:0 0 14px;max-width:780px;page-break-inside:avoid}.xc h2{font-size:15px;margin:0}.xc h3{font-size:12px;margin:9px 0 3px;border-bottom:1px solid #bbb}.xc .meta{color:#444;font-size:11px}.xc p,.xc li{font-size:12px}table{border-collapse:collapse;width:100%;font-size:11px}td,th{border-bottom:1px solid #ccc;padding:2px 5px;text-align:left;vertical-align:top}.url{font-family:monospace;font-size:10px;word-break:break-all}.sc{border:1px solid #888;border-radius:4px;padding:0 5px;font-size:11px;margin-right:3px}a{color:#000}@media print{@page{size:A4;margin:13mm}.noprint{display:none}}';
function exportCard(c) {
  var wObs = [], oObs = [], counter = [];
  bySpec(c).forEach(function (nid) { NM[nid].obs.forEach(function (o) { ((o.scope === 'WWOX_EXPERIMENT_IN_DEE_SYSTEM' || o.scope === 'WWOX_CLINICAL_CASE') ? wObs : oObs).push(o); }); NM[nid].counter.forEach(function (t) { counter.push(t); }); });
  var own = c.asserts.filter(function (a) { return a.scope !== 'SAFETY_SIGNAL'; }), safety = c.asserts.filter(function (a) { return a.scope === 'SAFETY_SIGNAL'; });
  var gl = uniq(c.needs.map(function (n) { return c.links[n].group; }).sort());
  var h = '<article class="xc" data-export-card="' + esc(c.id) + '"><h2>' + esc(c.short) + '</h2><div class="meta">Card ' + esc(c.id) + ' &middot; ' + esc(goalTxt(c.goal)) + ' &middot; ' + esc(trackTxt(c.track)) + ' &middot; status: ' + esc(c.status) + ' &middot; ' + (gl.length ? gl.map(function (g) { return esc(GR[g].label.split(':')[0]); }).join(', ') : 'no linked need') + '</div>';
  h += '<p class="meta"><b>Data date:</b> ' + esc(META.data_date) + ' (needs record ' + esc(META.needs_built_on) + '; catalogue build ' + esc(META.catalogue_generated) + '). <b>Perimeter:</b> WWOX-related developmental and epileptic encephalopathy (WWOX-DEE), reference genotype class; public literature and public databases only; no individual-level data. Research material for discussion with a treating clinical team: not medical advice, not a treatment recommendation, not a probability of benefit.</p>';
  h += '<h3>Rationale</h3><p>' + esc(first(c.why_full || c.why, 700)) + '</p>' + (c.needs.length ? '<p class="meta">Needs addressed: ' + c.needs.map(function (n) { return esc(NM[n].short); }).join('; ') + '.</p>' : '');
  h += '<h3>Evidence, by scope</h3>';
  var ev = [];
  c.asserts.filter(function (a) { return a.scope !== 'SAFETY_SIGNAL'; }).forEach(function (a) { ev.push('<li>' + sc(a.scope) + ' ' + esc(a.text) + ' \u2013 ' + esc(first(a.note_full || a.note, 260)) + (a.pmids.length ? ' (' + a.pmids.map(function (p) { return 'PMID ' + p; }).join(', ') + ')' : '') + '</li>'); });
  if (wObs.length || oObs.length) ev.push('<li class="meta"><i>Observations recorded on the linked need(s): context only, they may concern other interventions.</i></li>');
  wObs.slice(0, 4).forEach(function (o) { ev.push('<li>' + sc(o.scope) + ' <i>need-level observation:</i> ' + esc(o.short) + (o.pmid ? ' (PMID ' + esc(o.pmid) + ')' : '') + '</li>'); });
  oObs.slice(0, 3).forEach(function (o) { ev.push('<li>' + sc(o.scope) + ' <i>need-level observation:</i> ' + esc(o.short) + (o.pmid ? ' (PMID ' + esc(o.pmid) + ')' : '') + '</li>'); });
  h += ev.length ? '<ul>' + ev.join('') + '</ul>' : '<p>No scoped assertion is recorded in this card.</p>';
  if (!c.asserts.some(function (a) { return WWOX_SC[a.scope]; })) h += '<p><b>No readout of this intervention in a WWOX system is recorded in the card.</b></p>';
  h += '<h3>Counter-evidence</h3>' + ((c.against.length || counter.length || safety.length || c.against_note) ? '<ul>' + c.against.slice(0, 6).map(function (t) { return '<li>' + esc(first(t, 300)) + '</li>'; }).join('') + counter.slice(0, 3).map(function (t) { return '<li><i>need:</i> ' + esc(first(t, 280)) + '</li>'; }).join('') + safety.map(function (a) { return '<li>' + sc(a.scope) + ' ' + esc(a.text) + ' ' + esc(first(a.note_full || a.note, 220)) + '</li>'; }).join('') + (c.against_note ? '<li>As written in the card: ' + esc(first(c.against_note, 400)) + '</li>' : '') + '</ul>' : '<p>None itemised in the card (absence is not a negative finding).</p>');
  h += '<h3>Limits</h3><ul><li>Association is not modulation, and modulation is not rescue; a precedent from another disease is not a WWOX result.</li><li>Evidence scopes are kept apart and never pooled; shared sources are not independent confirmations.</li>' + (c.transfer_limits ? '<li>' + esc(first(c.transfer_limits, 300)) + '</li>' : '') + '<li>Access categories are US evidence found in the sources on the retrieval dates (not approval, not suitability for any person, not safety): ' + esc(c.access.join(', ') || 'none') + '.</li>' + c.limits.slice(0, 3).map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '<li>Text may cite repository-internal record ids (for example DL-, CLAIM, map records); only the identifiers in the Sources table are public.</li></ul>';
  h += '<h3>Missing proof and next experiment</h3><p>' + (c.missing ? '<b>Missing datum:</b> ' + esc(first(c.missing, 300)) + '. ' : '') + '</p><p>' + (c.next_full ? '<b>Next step:</b> ' + esc(first(c.next_full, 900)) : 'No next step is named in the card.') + '</p>';
  h += '<h3>Sources (public identifiers)</h3>' + sourcesHtml(c);
  h += '<p class="meta">Generated by repurposing_view.py (schema ' + esc(D.schema) + ', ' + esc(D.source) + ' build). ' + (D.source === 'shareable' ? 'Shareable build: see the attribution footer of the page for the sources embedded.' : 'Full local build: not for redistribution.') + '</p></article>';
  return h;
}
function enterExport(ids) {
  var cs = ids.map(function (i) { return CM[i]; }).filter(Boolean);
  var area = $('export-area');
  area.innerHTML = '<div class="btns noprint"><button type="button" id="x-back">Back to the view</button><button type="button" id="x-print">Print or save as PDF</button><button type="button" id="x-dl">Download as standalone HTML</button><span class="mut">' + cs.length + ' card(s). Links are public identifiers; they stay valid outside this folder.</span></div>' + (cs.map(exportCard).join('') || '<p class="state-none">Unknown card id.</p>');
  document.body.classList.add('exporting');
  document.title = 'Export: ' + cs.map(function (c) { return c.short; }).join(', ');
  $('x-back').onclick = function () { history.pushState('', '', location.pathname + location.search); leaveExport(); };
  $('x-print').onclick = function () { window.print(); };
  $('x-dl').onclick = function () {
    var body = cs.map(exportCard).join('');
    var doc = '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>WWOX candidate card</title><style>' + EXCSS + '</style></head><body>' + body + '</body></html>';
    var a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([doc], { type: 'text/html' })); a.download = 'wwox_card_' + cs.map(function (c) { return c.id; }).join('_') + '.html'; document.body.appendChild(a); a.click(); a.remove();
  };
  window.scrollTo(0, 0);
}
function leaveExport() { document.body.classList.remove('exporting'); document.title = TITLE; }

// ---------------------------------------------------------------- state <-> controls <-> hash
function syncCtl() { Object.keys(IDS).forEach(function (k) { $(IDS[k]).value = CF[k]; }); }
function renderAll() { renderNav(); renderCands(); renderRank(); }
function fromHash() {
  var h = decodeURIComponent(location.hash || ''), m;
  if ((m = h.match(/^#export=(.+)$/))) { enterExport(m[1].split(',')); return; }
  leaveExport();
  if ((m = h.match(/^#c=(.*)$/))) { Object.keys(CF).forEach(function (k) { CF[k] = ''; }); m[1].split('&').forEach(function (kv) { var i = kv.indexOf(':'); if (i > 0) { var k = kv.slice(0, i); if (k in CF) CF[k] = kv.slice(i + 1); else if (k === 'rank') RK.mode = kv.slice(i + 1); } }); syncCtl(); $('rk-mode').value = RK.mode; renderAll(); $('navigate').scrollIntoView(); }
  if ((m = h.match(/^#compare=(.+)$/))) { SEL = m[1].split(',').filter(function (i) { return CM[i]; }).slice(0, 4); renderCands(); }
}
Object.keys(IDS).forEach(function (k) { $(IDS[k]).addEventListener(k === 'q' ? 'input' : 'change', function () { CF[k] = this.value; renderAll(); }); });
$('c-reset').onclick = function () { Object.keys(CF).forEach(function (k) { CF[k] = ''; }); syncCtl(); renderAll(); };
$('rk-mode').onchange = function () { RK.mode = this.value; renderRank(); };
$('rk-sort').onchange = function () { RK.sort = this.value; renderRank(); };
$('cand-sort').onchange = function () { CSORT = this.value; renderCands(); };
document.addEventListener('click', function (e) { var a = e.target.closest ? e.target.closest('a[data-open]') : null; if (a) { e.preventDefault(); openCand(a.dataset.open); } });
window.addEventListener('hashchange', fromHash);
renderAll();
fromHash();
document.body.setAttribute('data-cur-ready', '1');
})();
