/* Curated layer: navigation, candidate profiles, research-priority groups, comparison, export. Reads D.cur (embedded data) and D.ui (Italian orientation strings). No network.
   Data/presentation boundary: every orientation string comes from D.ui (T); the code below only composes them with the data. Scientific text (titles, quotes, identifiers, compound names) is shown as stored. */
(function () {
'use strict';
var D = JSON.parse(document.getElementById('data').textContent);
var T = D.ui;
var TITLE = document.title;
var C = D.cur, NEEDS = C.needs, CANDS = C.cands, META = C.meta;
var NM = {}, CM = {}, SC = {}, GR = {}, WO = {};
NEEDS.forEach(function (n) { NM[n.id] = n; });
CANDS.forEach(function (c) { CM[c.id] = c; });
C.scopes.forEach(function (s) { SC[s.code] = s; });
C.groups.forEach(function (g) { GR[g.id] = g; });
(C.work_order.entries || []).forEach(function (e) { WO[e.need] = e; });
function $(id) { return document.getElementById(id); }
function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
function uniq(a) { var o = {}, r = []; a.forEach(function (x) { if (x != null && x !== '' && !o[x]) { o[x] = 1; r.push(x); } }); return r; }
function fill(s, o) { return String(s).replace(/\{(\w+)\}/g, function (m, k) { return o[k] == null ? m : o[k]; }); }
var PUBMED = 'https://pubmed.ncbi.nlm.nih.gov/', CHEMBL = 'https://www.ebi.ac.uk/chembl/compound_report_card/', DOI = 'https://doi.org/';
function ext(url, text) { return '<a href="' + esc(url) + '" rel="noopener noreferrer">' + esc(text) + '</a>'; }
function pmidLink(id) { return ext(PUBMED + id + '/', 'PMID ' + id); }
function pmidFull(p) { return pmidLink(p.id) + ' <span class="url">' + esc(PUBMED + p.id + '/') + '</span>' + (p.title ? ' ' + esc(p.title) : '') + (p.journal || p.year ? ' <span class="mut">[' + esc([p.journal, p.year].filter(Boolean).join(', ')) + ']</span>' : '') + ' <span class="mut">(' + esc(p.role) + ')</span>'; }
function first(t, n) { t = String(t || '').replace(/\s+/g, ' ').trim(); if (t.length <= n) return t; var cut = t.slice(0, n), i = Math.max(cut.lastIndexOf('. '), cut.lastIndexOf('; ')); if (i > n * 0.5) return cut.slice(0, i + 1); return cut.slice(0, cut.lastIndexOf(' ')) + ' …'; }
function sc(code, n) { var s = SC[code] || { glyph: '?', label: String(code) }; return '<span class="sc s-' + esc(code) + '"><span class="gl" aria-hidden="true">' + esc(s.glyph) + '</span>' + esc(T.scopeL[code] || s.label) + (n != null ? ' ×' + n : '') + '</span>'; }
function grp(g) { var p = T.pos[g]; return '<span class="grp ' + g.toLowerCase() + '" title="' + esc(p.label + '. ' + p.plain) + '">' + esc(g + ' ' + p.short) + '</span>'; }
function grpS(g) { return '<span class="grp ' + g.toLowerCase() + '" title="' + esc(T.pos[g].label) + '">' + esc(g) + '</span>'; }
function chip(t, cls) { return '<span class="chip' + (cls ? ' ' + cls : '') + '">' + esc(t) + '</span>'; }
function goalTxt(g) { return g ? T.chip_goal + ': ' + (g === 'deep_recovery' ? T.goal_deep : T.goal_partial) : T.chip_goal + ': ' + T.track_none; }
function goalShort(g) { return g ? (g === 'deep_recovery' ? T.goal_deep : T.goal_partial) : T.track_none; }
function dirOn(n) { return n.dir ? '<b>' + esc(dirTxt(n.dir)) + '</b>' + (n.dir_on ? ' (' + esc(T.nv_on) + ': «' + esc(n.dir_on) + '»)' : '') : ''; }
function trackTxt(t) { return t ? (t === 'A' ? T.track_A_s : T.track_B_s) : T.track_none_s; }
function needName(n) { return T.need[n.id] || n.short; }
function threadName(t) { return (T.thread[t.id] || { name: t.name }).name; }
function statusTxt(s) { return T.statusL[s] || s; }
function dirTxt(d) { return T['dir_' + d] || d; }
function more(shortT, fullT) { shortT = shortT || ''; fullT = fullT || ''; if (!fullT || fullT.replace(/\s+/g, ' ') === shortT.replace(/\s+/g, ' ') || fullT.length <= shortT.length + 3) return esc(shortT); return esc(shortT) + ' <details class="inl"><summary>' + esc(T.full_text) + '</summary>' + esc(fullT) + '</details>'; }
function critTxt(t) { var base = String(t).replace(/ \(found:.*\)$/, ''), tail = String(t).slice(base.length); return esc((T.crit[base] || base) + tail); }
function moreN(n) { return '<p class="mini">' + esc(fill(n === 1 ? T.more_in_tech1 : T.more_in_tech, { n: n })) + '</p>'; }

// ---------------------------------------------------------------- filters
var CF = { thread: '', need: '', access: '', country: '', scope: '', track: '', goal: '', status: '', q: '' };
var RK = { mode: 'need', sort: 'group' };
var SEL = [];
var IDS = { thread: 'c-thread', need: 'c-need', access: 'c-access', country: 'c-country', scope: 'c-scope', track: 'c-track', goal: 'c-goal', status: 'c-status', q: 'c-q' };
function opt(sel, pairs, all) { sel.innerHTML = '<option value="">' + esc(all) + '</option>' + pairs.map(function (p) { return '<option value="' + esc(p[0]) + '">' + esc(p[1]) + '</option>'; }).join(''); }
opt($('c-thread'), C.threads.map(function (t) { return [t.id, threadName(t)]; }), T.f_any_thread);
opt($('c-need'), NEEDS.map(function (n) { return [n.id, needName(n)]; }), T.f_any_need);
opt($('c-access'), uniq([].concat.apply([], CANDS.map(function (c) { return c.access; }))).sort().map(function (a) { return [a, T['acc_' + a] || a]; }), T.f_any_access);
opt($('c-country'), uniq(CANDS.map(function (c) { return c.country; })).sort().map(function (a) { return [a, T.countryL[a] || a]; }), T.f_any_country);
opt($('c-scope'), C.scopes.filter(function (s) { return CANDS.some(function (c) { return (c.scope_counts.int[s.code] || c.scope_counts.need[s.code]); }) || NEEDS.some(function (n) { return n.scopes.indexOf(s.code) >= 0; }); }).map(function (s) { return [s.code, s.glyph + ' ' + (T.scopeL[s.code] || s.label)]; }), T.f_any_scope);
opt($('c-track'), [['A', T.track_A_s], ['B', T.track_B_s]], T.f_any_track);
opt($('c-goal'), Object.keys(C.goals).map(function (g) { return [g, T.goalL[g]]; }), T.f_any_goal);
opt($('c-status'), uniq(CANDS.map(function (c) { return c.status; })).sort().map(function (a) { return [a, statusTxt(a)]; }), T.f_any_status);
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
  if (CF.q) { var t = (c.name + ' ' + c.id + ' ' + c.chembl.join(' ') + ' ' + c.needs.join(' ') + ' ' + c.needs.map(function (n) { return needName(NM[n]); }).join(' ') + ' ' + c.why).toLowerCase(); var w = CF.q.toLowerCase().split(/\s+/); for (var i = 0; i < w.length; i++) if (w[i] && t.indexOf(w[i]) < 0) return false; }
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
function bestCands(n) { return n.cards.map(function (id) { return CM[id]; }).filter(candOk).sort(function (a, b) { return a.short.localeCompare(b.short); }); }   // alphabetical: the letter carries no order
function navRow(n) {
  var cs = bestCands(n), ob = {};
  n.obs.forEach(function (o) { ob[o.scope] = (ob[o.scope] || 0) + 1; });
  var nx = '';
  for (var i = 0; i < cs.length; i++) { if (cs[i].next && !cs[i].abstention) { nx = '<b>' + esc(cs[i].short) + ':</b> ' + esc(first(cs[i].next, 230)); break; } }
  if (!nx) nx = cs.length && cs[0].missing ? '<b>' + esc(cs[0].short) + ' (' + esc(T.nv_missing) + '):</b> ' + esc(first(cs[0].missing, 200)) : '<span class="mut">' + esc(T.nv_next_none) + '</span>';
  return '<article class="navrow" data-need="' + esc(n.id) + '" aria-label="' + esc(needName(n)) + '">' +
    '<div><span class="lab">' + esc(T.nv_c_need) + '</span><b>' + esc(needName(n)) + '</b>' + chip(goalTxt(n.goal)) + chip(trackTxt(n.track)) + '</div>' +
    '<div><span class="lab">' + esc(T.nv_mech_lab) + '</span>' + (n.dir ? esc(T.nv_dir) + ': ' + dirOn(n) : '') + (n.uncertain ? ' <span class="chip">' + esc(T.nv_uncertain) + '</span>' : '') +
    '<div class="mini">' + esc(T.nv_targets) + ': ' + esc(n.targets.join(', ') || T.nv_none) + '</div></div>' +
    '<div><span class="lab">' + esc(T.nv_c_comp) + '</span>' + (cs.length ? cs.map(function (c) { return '<button type="button" class="chip ' + c.links[n.id].group.toLowerCase() + '" data-open="' + esc(c.id) + '">' + esc(c.short) + ' · ' + esc(c.links[n.id].group) + '</button>'; }).join(' ') : '<span class="mut">' + esc(fill(T.nv_comp_none, { n: n.fam_link })) + '</span>') + '</div>' +
    '<div><span class="lab">' + esc(T.nv_c_evid) + '</span>' + (Object.keys(ob).length ? Object.keys(ob).map(function (k) { return sc(k, ob[k]); }).join('') : '<span class="mut">' + esc(T.nv_evid_none) + '</span>') +
    '<div class="mini">' + esc(fill(T.nv_evid_line, { w: n.n_wwox_obs, c: n.n_case_obs, k: n.counter.length })) + '</div></div>' +
    '<div><span class="lab">' + esc(T.nv_c_next) + '</span><span class="mini">' + nx + '</span></div></article>';
}
function renderNav() {
  var ns = NEEDS.filter(needOk), out = '';
  C.threads.forEach(function (t) {
    var inT = ns.filter(function (n) { return n.thread === t.id; });
    if (inT.length) out += '<h3>' + esc(threadName(t)) + ' <span class="mut">(' + esc(fill(T.nv_shown, { a: inT.length, b: t.needs.length })) + ')</span></h3>' + inT.map(navRow).join('');
  });
  $('nav-list').innerHTML = out || '<p class="state-none">' + esc(T.nv_nomatch) + '</p>';
  var cs = CANDS.filter(candOk);
  $('c-count').textContent = fill(T.count_line, { n1: ns.length, n2: NEEDS.length, c1: cs.length, c2: CANDS.length });
  Array.prototype.forEach.call($('nav-list').querySelectorAll('[data-open]'), function (b) { b.onclick = function () { openCand(b.dataset.open); }; });
}

// ---------------------------------------------------------------- candidate profile (six short answers; the rest one click further)
function obsLine(o) { return '<li>' + sc(o.scope) + ' ' + esc(o.short) + (o.pmid ? ' ' + pmidLink(o.pmid) : '') + (o.cite ? ' <span class="mut">' + esc(o.cite) + '</span>' : '') + (o.limits ? ' <span class="mut">' + esc(o.limits) + '</span>' : '') + '</li>'; }
function asLine(a) { return '<li>' + sc(a.scope) + ' ' + esc(a.text) + (a.note ? ' <span class="mini">– ' + esc(a.note) + '</span>' : '') + (a.species ? ' <span class="mut">[' + esc(a.species) + (a.genotype ? ', ' + esc(first(a.genotype, 70)) : '') + ']</span>' : '') + (a.pmids.length ? ' ' + a.pmids.map(pmidLink).join(' ') : '') + '</li>'; }
var WWOX_SC = { WWOX_EXPERIMENT_IN_DEE_SYSTEM: 1, WWOX_CLINICAL_CASE: 1 };
function bySpec(c) { return c.needs.slice().sort(function (a, b) { return NM[a].cards.length - NM[b].cards.length || a.localeCompare(b); }); }
function profileParts(c) {
  var needsObs = []; bySpec(c).forEach(function (nid) { NM[nid].obs.forEach(function (o) { needsObs.push(o); }); });
  var wObs = needsObs.filter(function (o) { return o.scope === 'WWOX_EXPERIMENT_IN_DEE_SYSTEM' || o.scope === 'WWOX_CLINICAL_CASE'; });
  var oObs = needsObs.filter(function (o) { return !(o.scope === 'WWOX_EXPERIMENT_IN_DEE_SYSTEM' || o.scope === 'WWOX_CLINICAL_CASE'); });
  var own = c.asserts.filter(function (a) { return WWOX_SC[a.scope]; });
  function wwoxAssert(a) { return a.scope === 'UNCLASSIFIED' && /WWOX|WOREE/i.test(a.system || '') && !/NOT WWOX/i.test((a.system || '') + ' ' + (a.genotype || '')); }
  function wwoxObs(o) { return o.scope === 'WWOX_BIOLOGY_OTHER_CONTEXT' || (o.scope === 'COMPUTATIONAL_RESULT' && /knock|wwox/i.test(String(o.model || ''))); }
  var wOther = c.asserts.filter(wwoxAssert).map(asLine).concat(oObs.filter(wwoxObs).map(obsLine));
  oObs = oObs.filter(function (o) { return !wwoxObs(o); });
  var other = c.asserts.filter(function (a) { return !WWOX_SC[a.scope] && a.scope !== 'SAFETY_SIGNAL' && !wwoxAssert(a); });
  var safety = c.asserts.filter(function (a) { return a.scope === 'SAFETY_SIGNAL'; });
  var counter = []; c.needs.forEach(function (nid) { NM[nid].counter.forEach(function (t) { counter.push(t); }); });
  var q = {};
  var gu = uniq(c.needs.map(function (n) { return c.links[n].group; }).sort());
  q.why = (gu.length ? '<p class="mini whyl">' + gu.map(function (g) { return '<b>' + esc(g) + '</b> ' + esc(T.pos[g].plain); }).join('<br>') + '</p>' : '') + '<p>' + more(first(c.why, 240), c.why_full) + '</p>' + (c.needs.length ? '<p class="mini">' + esc(T.q1_needs) + ': ' + c.needs.map(function (n) { return esc(needName(NM[n])); }).join('; ') + '.</p>' : '<p class="mini">' + esc(T.q1_noneed) + '</p>');
  q.wwox = (own.length ? '<p class="mini"><b>' + esc(T.q2_own) + ':</b></p><ul>' + own.slice(0, 2).map(asLine).join('') + '</ul>' + (own.length > 2 ? moreN(own.length - 2) : '') : '<p class="mini"><b>' + esc(T.q2_none) + '</b></p>') +
    (wObs.length ? '<details class="inl"><summary>' + esc(T.q2_ctx) + '</summary><ul>' + wObs.slice(0, 2).map(obsLine).join('') + '</ul>' + (wObs.length > 2 ? moreN(wObs.length - 2) : '') + '</details>' : '<p class="mini">' + esc(T.q2_noctx) + '</p>') +
    (wOther.length ? '<details class="inl"><summary>' + esc(T.q2_other) + '</summary><ul>' + wOther.slice(0, 4).join('') + '</ul>' + (wOther.length > 4 ? moreN(wOther.length - 4) : '') + '</details>' : '');
  var oth = other.slice(0, 2).map(asLine).concat(oObs.slice(0, 2).map(obsLine));
  q.other = oth.length ? '<ul>' + oth.join('') + '</ul>' + ((other.length + oObs.length) > oth.length ? moreN(other.length + oObs.length - oth.length) : '') : '<p class="mini">' + esc(T.q3_none) + '</p>';
  var ag = c.against.slice(0, 2).map(function (t) { return '<li>' + esc(first(t, 240)) + '</li>'; }).concat(counter.slice(0, 1).map(function (t) { return '<li><span class="mut">' + esc(T.q4_need) + ':</span> ' + esc(first(t, 220)) + '</li>'; })).concat(safety.slice(0, 1).map(asLine));
  q.counter = (ag.length ? '<ul>' + ag.join('') + '</ul>' : '') + (c.against_note ? '<p class="mini">' + esc(T.q4_note) + ': ' + esc(first(c.against_note, 300)) + '</p>' : '') + ((!ag.length && !c.against_note) ? '<p class="mini">' + esc(T.q4_none) + '</p>' : '') +
    ((c.against.length + counter.length) > 3 ? moreN(c.against.length + counter.length - 3) : '');
  q.miss = '<p>' + (c.missing ? '<b>' + esc(T.q5_miss) + ':</b> ' + esc(first(c.missing, 260)) : esc(T.q5_nomiss)) + '</p>' + (c.reopen ? '<p class="mini">' + esc(T.q5_reopen) + ': ' + esc(c.reopen) + '</p>' : '');
  q.next = c.next ? '<p>' + more(c.next, c.next_full) + '</p>' : '<p class="mini">' + esc(T.q6_none) + '</p>';
  return q;
}
function whyPos(c) {
  return '<details class="inl whypos"><summary>' + esc(T.pos_why_h) + '</summary><ul>' + c.needs.map(function (nid) {
    var l = c.links[nid]; return '<li>' + grp(l.group) + ' <span class="mut">' + esc(T.pos_for) + '</span> ' + esc(needName(NM[nid])) + '<div class="mini">' + esc(T.pos[l.group].plain) + '</div></li>';
  }).join('') + '</ul></details>';
}
function techDetails(c) {
  var h = '<details class="tech"><summary>' + esc(T.tech_sum) + '</summary><p class="mini mut">' + esc(T.tc_text_en) + '</p>';
  h += '<h4>' + esc(T.tc_identity) + '</h4><p class="mini">' + esc(c.identity) + '</p><p class="mini"><b>' + esc(T.tc_mech) + ':</b> ' + esc(c.mechanism) + '</p><p class="mini"><b>' + esc(T.tc_novelty) + ':</b> ' + esc(c.novelty) + '</p><p class="mini"><b>' + esc(T.tc_pharm) + ':</b> ' + esc(c.pharm) + '</p><p class="mini"><b>' + esc(T.tc_access) + ':</b> ' + esc(c.access_text) + '</p>';
  h += '<h4>' + esc(T.tc_links_h) + '</h4><table class="tbl"><thead><tr><th>' + esc(T.tc_need) + '</th><th>' + esc(T.tc_pos) + '</th><th>' + esc(T.tc_crit) + '</th></tr></thead><tbody>' + c.needs.map(function (nid) {
    var l = c.links[nid];
    return '<tr><td>' + esc(needName(NM[nid])) + '<div class="mut">' + esc(nid) + '</div></td><td>' + grp(l.group) + (l.tags || []).map(function (t) { return '<div>' + chip(t, '') + '</div>'; }).join('') + '</td><td><ul class="crit-list">' + l.criteria.map(function (x) { return '<li class="' + (x.met ? 'met' : 'unmet') + '"><span aria-hidden="true">' + (x.met ? '✓' : '✗') + '</span> <b>' + esc(x.met ? T.crit_met : T.crit_not) + ':</b> ' + critTxt(x.text) + '</li>'; }).join('') + '</ul><details class="inl"><summary>' + esc(T.tc_text_en) + '</summary><ul>' + l.reasons.map(function (r) { return '<li><b>' + esc(r[0]) + ':</b> ' + esc(r[1]) + '</li>'; }).join('') + '</ul></details></td></tr>';
  }).join('') + '</tbody></table>';
  if (c.asserts.length) h += '<h4>' + esc(T.tc_asserts) + ' (' + c.asserts.length + ')</h4><table class="tbl"><thead><tr><th>' + esc(T.tc_scope) + '</th><th>' + esc(T.tc_stmt) + '</th><th>' + esc(T.tc_sys) + '</th><th>' + esc(T.tc_depth) + '</th><th>' + esc(T.tc_src) + '</th></tr></thead><tbody>' + c.asserts.map(function (a) { return '<tr><td>' + sc(a.scope) + '</td><td>' + esc(a.text) + '<div class="mini">' + more(a.note, a.note_full) + '</div></td><td>' + esc([a.species, a.system, a.genotype].filter(Boolean).join('; ')) + '</td><td>' + esc(a.depth || '') + '</td><td>' + (a.pmids.map(pmidLink).join(' ') || '') + '</td></tr>'; }).join('') + '</tbody></table>';
  var allW = []; c.needs.forEach(function (nid) { NM[nid].obs.forEach(function (o) { allW.push([nid, o]); }); });
  if (allW.length) h += '<h4>' + esc(T.tc_obs) + ' (' + allW.length + ')</h4><ul>' + allW.map(function (x) { return obsLine(x[1]).replace('<li>', '<li><span class="mut">' + esc(needName(NM[x[0]])) + ':</span> '); }).join('') + '</ul>';
  if (c.against.length) h += '<h4>' + esc(T.tc_against) + ' (' + c.against.length + ')</h4><ul>' + c.against.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>';
  if (c.for.length) h += '<h4>' + esc(T.tc_for) + '</h4><ul>' + c.for.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>';
  if (c.not_known.length) h += '<h4>' + esc(T.tc_notknown) + '</h4><ul>' + c.not_known.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>';
  if (c.actions.length) h += '<h4>' + esc(T.tc_actions) + '</h4><table class="tbl"><thead><tr><th>' + esc(T.tc_need) + '</th><th>' + esc(T.tc_target) + '</th><th>' + esc(T.tc_action) + '</th><th>' + esc(T.tc_rel) + '</th></tr></thead><tbody>' + c.actions.map(function (a) { return '<tr><td>' + esc(NM[a.need] ? needName(NM[a.need]) : a.need) + '</td><td>' + esc(a.target) + '</td><td>' + esc(T['act_' + a.action] || a.action) + '</td><td>' + (/oppos/.test(a.cons) ? '<span class="opp">' + esc(T.opposed) + '</span>' : esc(T['cons_' + a.cons] || String(a.cons).replace(/_/g, ' '))) + '</td></tr>'; }).join('') + '</tbody></table>';
  h += '<h4>' + esc(T.tc_sources) + '</h4>' + sourcesHtml(c) + '<p class="mini">' + esc(T.tc_cardfile) + ': <code>' + esc(c.card_path) + '</code>. ' + esc(T.tc_assess) + ': ' + esc(c.assessment) + '; ' + esc(T.tc_bridge) + ': ' + esc(c.summary) + '.</p>';
  return h + '</details>';
}
function sourcesHtml(c) {
  var h = '<ul class="srcs">';
  c.pmids.forEach(function (p) { h += '<li>' + pmidFull(p) + '</li>'; });
  c.chembl.forEach(function (id) { h += '<li>' + ext(CHEMBL + id + '/', 'ChEMBL ' + id) + ' <span class="url">' + esc(CHEMBL + id + '/') + '</span> <span class="mut">(' + esc(T.tc_compound_id) + ')</span></li>'; });
  c.dois.forEach(function (d) { h += '<li>' + ext(DOI + d, 'DOI ' + d) + ' <span class="url">' + esc(DOI + d) + '</span></li>'; });
  if (!c.pmids.length && !c.chembl.length && !c.dois.length) h += '<li class="mut">' + esc(T.tc_nosrc) + '</li>';
  return h + '</ul>';
}
function candHtml(c) {
  var q = profileParts(c), sel = SEL.indexOf(c.id) >= 0, gl = uniq(c.needs.map(function (n) { return c.links[n].group; }).sort());
  var scopes = {}; Object.keys(c.scope_counts.int).forEach(function (k) { scopes[k] = (scopes[k] || 0) + c.scope_counts.int[k]; });
  return '<article class="cand" id="cand-' + esc(c.id) + '" data-cand="' + esc(c.id) + '"><h3>' + esc(c.short) + ' <span class="mut">' + esc(c.id) + '</span></h3>' +
    '<div class="chips2">' + (gl.length ? gl.map(grp).join('') : chip(T.cd_no_need)) + chip(goalTxt(c.goal)) + chip(trackTxt(c.track)) + chip(T.cd_status + ': ' + statusTxt(c.status)) + (c.access.length ? chip(T.cd_access + ': ' + c.access.map(function (a) { return T['acc_' + a] || a; }).join(', ')) : chip(T.cd_access_none)) + '</div>' +
    '<div>' + (Object.keys(scopes).length ? Object.keys(scopes).map(function (k) { return sc(k, scopes[k]); }).join('') : '<span class="mini mut">' + esc(T.cd_noscope) + '</span>') + '</div>' +
    '<div class="btns noprint"><label><input type="checkbox" data-sel="' + esc(c.id) + '"' + (sel ? ' checked' : '') + '> ' + esc(T.cd_pick) + '</label><button type="button" data-export="' + esc(c.id) + '">' + esc(T.cd_export) + '</button><button type="button" data-brief="' + esc(c.id) + '">' + esc(T.cd_brief) + '</button></div>' +
    '<div class="qa"><div><h4>' + esc(T.q1) + '</h4>' + q.why + '</div><div><h4>' + esc(T.q2) + '</h4>' + q.wwox + '</div><div><h4>' + esc(T.q3) + '</h4>' + q.other + '</div><div><h4>' + esc(T.q4) + '</h4>' + q.counter + '</div><div><h4>' + esc(T.q5) + '</h4>' + q.miss + '</div><div><h4>' + esc(T.q6) + '</h4>' + q.next + '</div></div>' + (c.needs.length ? whyPos(c) : '') + techDetails(c) + '</article>';
}
var CSORT = 'group';
function renderCands() {
  var cs = CANDS.filter(candOk);
  if (CSORT === 'name') cs.sort(function (a, b) { return a.short.localeCompare(b.short); });
  else cs.sort(function (a, b) { return a.positions.join('+').localeCompare(b.positions.join('+')) || a.short.localeCompare(b.short); });   // groups cards that share the same SET of need-level positions; not a ranking
  $('cand-list').innerHTML = cs.length ? cs.map(candHtml).join('') : '<p class="state-none">' + esc(T.cd_none) + '</p>';
  $('cand-n').textContent = cs.length;
  wireCands($('cand-list'));
  renderSel();
}
function wireCands(root) {
  Array.prototype.forEach.call(root.querySelectorAll('[data-sel]'), function (b) { b.onchange = function () { toggleSel(b.dataset.sel, b.checked); }; });
  Array.prototype.forEach.call(root.querySelectorAll('[data-export]'), function (b) { b.onclick = function () { location.hash = '#export=' + b.dataset.export; }; });
  Array.prototype.forEach.call(root.querySelectorAll('[data-brief]'), function (b) { b.onclick = function () { location.hash = '#brief=' + b.dataset.brief; }; });
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
    if (s === 'wwox') return (y.l.n_w + y.l.n_c) - (x.l.n_w + x.l.n_c) || x.c.short.localeCompare(y.c.short);
    if (s === 'counter') return (y.c.against.length + NM[y.n].counter.length) - (x.c.against.length + NM[x.n].counter.length) || x.c.short.localeCompare(y.c.short);
    return x.c.short.localeCompare(y.c.short);
  });
}
function rkItem(it, showNeed) {
  var c = it.c, l = it.l, n = NM[it.n];
  var sum = T.pr_sum_wwox + ': ' + T['res_' + l.result] + (l.result !== 'none' ? ' (' + fill(T.pr_w_counts, { w: l.n_w, nul: l.n_null, unf: l.n_harm }) + ')' : '') + '. ' + T.pr_sum_counter + ': ' + (c.against.length + n.counter.length) + ' ' + ((c.against.length + n.counter.length) === 1 ? T.pr_sum_item1 : T.pr_sum_item) + (c.against_note && !c.against.length ? ' (' + T.pr_sum_prose + ')' : '') + '. ' + T.pr_sum_next + ': ' + (c.next ? T.pr_next_yes : T.pr_next_no) + '.';
  return '<div class="rk-item" data-cand="' + esc(c.id) + '" data-need="' + esc(n.id) + '"><b>' + esc(c.short) + '</b>' + (showNeed ? ' <span class="mut">' + esc(T.pos_for) + ' ' + esc(needName(n)) + '</span>' : '') + ' ' + grp(l.group) + (l.tags || []).map(function (t) { return ' ' + chip(t, ''); }).join('') + (c.goal !== n.goal && c.goal ? ' ' + chip(T.pr_goal_aim_diff, '') : '') +
    '<div class="sum">' + esc(sum) + '</div><details><summary>' + esc(T.pr_reasons) + '</summary><ul class="crit-list">' + l.criteria.map(function (x) { return '<li class="' + (x.met ? 'met' : 'unmet') + '"><span aria-hidden="true">' + (x.met ? '✓' : '✗') + '</span> <b>' + esc(x.met ? T.crit_met : T.crit_not) + ':</b> ' + critTxt(x.text) + '</li>'; }).join('') + '</ul><details class="inl"><summary>' + esc(T.tc_text_en) + '</summary><ul>' + l.reasons.map(function (r) { return '<li><b>' + esc(r[0]) + ':</b> ' + esc(r[1]) + '</li>'; }).join('') + '</ul></details><button type="button" class="chip" data-open="' + esc(c.id) + '">' + esc(T.pr_open_card) + '</button></details></div>';
}
function groupBlock(items, showNeed) {
  var h = '';
  C.groups.forEach(function (g) {
    var it = sortItems(items.filter(function (x) { return x.l.group === g.id; }));
    if (it.length) h += '<div class="rk-group" data-group="' + g.id + '"><h3>' + grp(g.id) + ' <span class="mut">(' + it.length + ' ' + esc(it.length > 1 ? T.pr_links : T.pr_link) + ')</span></h3><p class="mini mut">' + esc(T.pos[g.id].plain) + '</p>' + it.map(function (x) { return rkItem(x, showNeed); }).join('') + '</div>';
  });
  return h || '<p class="mini mut">' + esc(T.pr_nolink) + '</p>';
}
function renderRank() {
  var links = [];
  CANDS.forEach(function (c) { if (candOk(c)) c.needs.forEach(function (n) { if (needOk(NM[n])) links.push({ c: c, n: n, l: c.links[n] }); }); });
  var h = '';
  if (RK.mode === 'need') {
    NEEDS.filter(needOk).forEach(function (n) {
      var it = links.filter(function (x) { return x.n === n.id; });
      h += '<section class="rk-need" data-need="' + esc(n.id) + '"><h3>' + esc(needName(n)) + ' <span class="mut">' + esc(goalTxt(n.goal)) + '</span></h3>' + (WO[n.id] ? '<p class="mini"><a href="#wo-' + esc(n.id) + '" data-wo="' + esc(n.id) + '">' + esc(T.wo_see) + '</a> <span class="chip wo-k">' + esc(WO[n.id].kind) + '</span></p>' : '') + (it.length ? groupBlock(it, false) : '<p class="mini mut">' + esc(fill(T.pr_need_nocard, { n: n.fam_link })) + '</p>') + '</section>';
    });
    var orphan = CANDS.filter(function (c) { return candOk(c) && !c.needs.length && !CF.need && !CF.thread; });
    if (orphan.length) h += '<section class="rk-need"><h3>' + esc(T.pr_axis_h) + '</h3><p class="mini mut">' + esc(T.pr_axis_note) + '</p>' + orphan.sort(function (a, b) { return a.short.localeCompare(b.short); }).map(function (c) { return '<div class="rk-item"><b>' + esc(c.short) + '</b> ' + chip(T.cd_no_need) + ' ' + esc(first(c.missing || '', 200)) + ' <button type="button" class="chip" data-open="' + esc(c.id) + '">' + esc(T.pr_open) + '</button></div>'; }).join('') + '</section>';
  } else {
    Object.keys(C.goals).forEach(function (g) {
      var it = links.filter(function (x) { return NM[x.n].goal === g; });
      h += '<section class="rk-need" data-goal="' + g + '"><h3>' + esc(T.goalL[g]) + ' <span class="mut">(' + it.length + ' ' + esc(T.pr_goal_links) + ')</span></h3>' + groupBlock(it, true) + '</section>';
    });
  }
  $('rk-list').innerHTML = h || '<p class="state-none">' + esc(T.nv_nomatch) + '</p>';
  Array.prototype.forEach.call($('rk-list').querySelectorAll('[data-open]'), function (b) { b.onclick = function () { openCand(b.dataset.open); }; });
}

// ---------------------------------------------------------------- selection and comparison
function toggleSel(id, on) {
  var i = SEL.indexOf(id);
  if (on && i < 0) { if (SEL.length >= 4) { alert(T.cp_max); renderCands(); return; } SEL.push(id); }
  if (!on && i >= 0) SEL.splice(i, 1);
  renderSel();
  Array.prototype.forEach.call(document.querySelectorAll('[data-sel]'), function (b) { b.checked = SEL.indexOf(b.dataset.sel) >= 0; });
}
function sgn(d) { return d === 'up' || d === 'restore' ? 1 : (d === 'down' ? -1 : 0); }
function renderSel() {
  $('sel-bar').innerHTML = SEL.length ? SEL.map(function (id) { return chip(CM[id].short); }).join(' ') + ' <button type="button" id="sel-clear">' + esc(T.cd_sel_clear) + '</button> <button type="button" id="sel-export">' + esc(T.cd_sel_export) + '</button> <button type="button" id="sel-brief">' + esc(T.cd_sel_brief) + '</button>' : '<span class="mut">' + esc(T.cd_sel_none) + '</span>';
  if ($('sel-clear')) $('sel-clear').onclick = function () { SEL = []; renderCands(); };
  if ($('sel-export')) $('sel-export').onclick = function () { location.hash = '#export=' + SEL.join(','); };
  if ($('sel-brief')) $('sel-brief').onclick = function () { location.hash = '#brief=' + SEL.join(','); };
  renderCompare();
}
function actTxt(a) { return T['act_' + a] || a; }
function renderCompare() {
  var box = $('cmp-out');
  if (SEL.length < 2) { box.innerHTML = '<p class="mut">' + esc(T.cp_pick) + '</p>'; return; }
  var cs = SEL.map(function (id) { return CM[id]; });
  function row(label, fn) { return '<tr><th scope="row">' + label + '</th>' + cs.map(function (c) { return '<td>' + fn(c) + '</td>'; }).join('') + '</tr>'; }
  var h = '<div class="cmpwrap"><table class="cmp"><caption class="sr">' + esc(fill(T.cp_caption, { n: cs.length })) + '</caption><thead><tr><th scope="col">' + esc(T.cp_dim) + '</th>' + cs.map(function (c) { return '<th scope="col">' + esc(c.short) + '<div class="mut">' + esc(c.id) + '</div></th>'; }).join('') + '</tr></thead><tbody>';
  h += row(esc(T.cp_aim), function (c) { return esc(goalShort(c.goal)); });
  h += row(esc(T.cp_track), function (c) { return esc(trackTxt(c.track)); });
  h += row(esc(T.cp_status), function (c) { return esc(statusTxt(c.status)) + '<br>' + uniq(c.needs.map(function (n) { return c.links[n].group; })).sort().map(grp).join('') + (c.needs.length ? '' : '<span class="mut">' + esc(T.cd_no_need) + '</span>'); });
  h += row(esc(T.cp_needs), function (c) { return c.needs.length ? '<ul>' + c.needs.map(function (n) { return '<li>' + esc(needName(NM[n])) + ': ' + dirOn({ dir: NM[n].dir || '?', dir_on: first(NM[n].dir_on || '', 70) }) + '</li>'; }).join('') + '</ul>' : '<span class="mut">' + esc(T.cp_none) + '</span>'; });
  h += row(esc(T.cp_actions), function (c) { return c.actions.length ? '<ul>' + c.actions.slice(0, 8).map(function (a) { return '<li>' + esc(a.target) + ': ' + esc(actTxt(a.action)) + ' ' + (/oppos/.test(a.cons) ? '<span class="opp">' + esc(T.opposed) + '</span>' : '<span class="mini">(' + esc(T['cons_' + a.cons] || String(a.cons).replace(/_/g, ' ')) + ')</span>') + '</li>'; }).join('') + '</ul>' + (c.actions.length > 8 ? '<span class="mini">+' + (c.actions.length - 8) + '</span>' : '') : '<span class="mut">' + esc(T.cp_noact) + '</span>'; });
  h += row(esc(T.cp_scopes), function (c) { var k = Object.keys(c.scope_counts.int); return k.length ? k.map(function (s) { return sc(s, c.scope_counts.int[s]); }).join('') : '<span class="mut">' + esc(T.cp_noscope) + '</span>'; });
  h += row(esc(T.cp_against), function (c) { return String(c.against.length) + (c.against_note && !c.against.length ? ' (' + esc(T.cp_prose) + ')' : ''); });
  h += row(esc(T.cp_missing), function (c) { return esc(first(c.missing || T.cp_nostated, 200)); });
  h += '</tbody></table></div>';
  var shared = cs[0].needs.filter(function (n) { return cs.every(function (c) { return c.needs.indexOf(n) >= 0; }); });
  var anyShared = uniq([].concat.apply([], cs.map(function (c) { return c.needs; }))).filter(function (n) { return cs.filter(function (c) { return c.needs.indexOf(n) >= 0; }).length >= 2; });
  var tg = {}; cs.forEach(function (c) { c.needs.forEach(function (n) { NM[n].targets.forEach(function (t) { (tg[t] = tg[t] || {})[c.id] = 1; }); }); });
  var sharedT = Object.keys(tg).filter(function (t) { return Object.keys(tg[t]).length >= 2; });
  var only = cs.map(function (c) { return [c, c.needs.filter(function (n) { return !cs.some(function (d) { return d !== c && d.needs.indexOf(n) >= 0; }); })]; });
  var opp = [];
  cs.forEach(function (c) { c.actions.forEach(function (a) { if (/oppos/.test(a.cons)) opp.push('<b>' + esc(c.short) + '</b> ' + esc(T.cp_opp_acts) + ' ' + esc(a.target) + ' (' + esc(actTxt(a.action)) + ') ' + esc(T.cp_opp_dir) + ' ' + esc(NM[a.need] ? needName(NM[a.need]) : a.need)); }); });
  var byT = {};
  cs.forEach(function (c) { c.actions.forEach(function (a) { var s = a.action === 'up' ? 1 : (a.action === 'down' ? -1 : 0); if (s) (byT[a.target] = byT[a.target] || []).push([c, s]); }); });
  Object.keys(byT).forEach(function (t) { var u = byT[t].filter(function (x) { return x[1] > 0; }), d = byT[t].filter(function (x) { return x[1] < 0; }); if (u.length && d.length) opp.push(esc(T.cp_on) + ' <b>' + esc(t) + '</b>, <b>' + esc(u[0][0].short) + '</b> ' + esc(T.cp_raises) + ' <b>' + esc(d[0][0].short) + '</b> ' + esc(T.cp_lowers)); });
  var wd = {};
  cs.forEach(function (c) { c.needs.forEach(function (n) { NM[n].targets.forEach(function (t) { var s = sgn(NM[n].dir); if (s) (wd[t] = wd[t] || []).push([c, n, s]); }); }); });
  Object.keys(wd).forEach(function (t) { var u = wd[t].filter(function (x) { return x[2] > 0; }), d = wd[t].filter(function (x) { return x[2] < 0; }); if (u.length && d.length && u[0][0] !== d[0][0]) opp.push(esc(fill(T.cp_wanted_diff, { t: t })) + ': ' + esc(needName(NM[u[0][1]])) + ' (' + esc(dirTxt(NM[u[0][1]].dir)) + ', ' + esc(u[0][0].short) + ') / ' + esc(needName(NM[d[0][1]])) + ' (' + esc(dirTxt(NM[d[0][1]].dir)) + ', ' + esc(d[0][0].short) + ')'); });
  h += '<h3>' + esc(T.cp_overlap) + '</h3><p>' + esc(T.cp_all) + ': ' + (shared.length ? shared.map(function (n) { return esc(needName(NM[n])); }).join('; ') : '<b>' + esc(T.cp_none) + '</b>') + '. ' + esc(T.cp_two) + ': ' + (anyShared.length ? anyShared.map(function (n) { return esc(needName(NM[n])); }).join('; ') : esc(T.cp_none)) + '. ' + esc(T.cp_tg) + ': ' + (sharedT.length ? esc(sharedT.join(', ')) : esc(T.cp_none)) + '.</p>';
  h += '<h3>' + esc(T.cp_comp) + '</h3><ul>' + only.map(function (x) { return '<li><b>' + esc(x[0].short) + '</b> ' + esc(T.cp_alone) + ': ' + (x[1].length ? x[1].map(function (n) { return esc(needName(NM[n])); }).join('; ') : esc(T.cp_nothing)) + '</li>'; }).join('') + '</ul>';
  h += '<h3>' + esc(T.cp_opp_h) + '</h3>' + (opp.length ? '<ul data-opposed="' + opp.length + '">' + opp.map(function (t) { return '<li><span class="opp">' + esc(T.cp_opp_word) + '</span> ' + t + '</li>'; }).join('') + '</ul>' : '<p data-opposed="0">' + esc(T.cp_opp_none) + '</p>');
  h += '<p class="note"><b>' + esc(T.cp_nosyn) + '</b> ' + esc(T.cp_nosyn_txt) + '</p>';
  box.innerHTML = h;
}

// ---------------------------------------------------------------- export (print / PDF / standalone HTML)
var EXCSS = 'body{font:12px/1.45 system-ui,Segoe UI,Roboto,sans-serif;color:#111;background:#fff;margin:0;padding:14px}.xc{border:1px solid #888;border-radius:6px;padding:10px 14px;margin:0 0 14px;max-width:780px;page-break-inside:avoid}.xc h2{font-size:15px;margin:0}.xc h3{font-size:12px;margin:9px 0 3px;border-bottom:1px solid #bbb}.xc .meta{color:#444;font-size:11px}.xc p,.xc li{font-size:12px}table{border-collapse:collapse;width:100%;font-size:11px}td,th{border-bottom:1px solid #ccc;padding:2px 5px;text-align:left;vertical-align:top}.url{font-family:monospace;font-size:10px;word-break:break-all}.sc{border:1px solid #888;border-radius:4px;padding:0 5px;font-size:11px;margin-right:3px}a{color:#000;overflow-wrap:anywhere}@media print{@page{size:A4;margin:13mm}.noprint{display:none}}@media (max-width:480px){body{padding:8px}.xc{padding:8px 10px}}';
function exportCard(c) {
  var wObs = [], oObs = [], counter = [];
  bySpec(c).forEach(function (nid) { NM[nid].obs.forEach(function (o) { ((o.scope === 'WWOX_EXPERIMENT_IN_DEE_SYSTEM' || o.scope === 'WWOX_CLINICAL_CASE') ? wObs : oObs).push(o); }); NM[nid].counter.forEach(function (t) { counter.push(t); }); });
  var safety = c.asserts.filter(function (a) { return a.scope === 'SAFETY_SIGNAL'; });
  var gl = uniq(c.needs.map(function (n) { return c.links[n].group; }).sort());
  var h = '<article class="xc" data-export-card="' + esc(c.id) + '"><h2>' + esc(c.short) + '</h2><div class="meta">' + esc(T.ex_card) + ' ' + esc(c.id) + ' &middot; ' + esc(goalTxt(c.goal)) + ' &middot; ' + esc(trackTxt(c.track)) + ' &middot; ' + esc(T.cd_status) + ': ' + esc(statusTxt(c.status)) + ' &middot; ' + (gl.length ? gl.map(function (g) { return esc(g + ' ' + T.pos[g].short); }).join(', ') : esc(T.cd_no_need)) + '</div>';
  h += '<p class="meta"><b>' + esc(T.ex_data_date) + ':</b> ' + esc(META.data_date) + ' (' + esc(T.ex_needs_rec) + ' ' + esc(META.needs_built_on) + '; ' + esc(T.ex_cat_build) + ' ' + esc(META.catalogue_generated) + '). <b>' + esc(T.ex_perim) + ':</b> ' + esc(T.ex_perim_txt) + '</p>';
  h += '<h3>' + esc(T.ex_rationale) + '</h3><p>' + esc(first(c.why_full || c.why, 700)) + '</p>' + (c.needs.length ? '<p class="meta">' + esc(T.ex_needs) + ': ' + c.needs.map(function (n) { return esc(needName(NM[n])); }).join('; ') + '.</p>' : '');
  h += '<h3>' + esc(T.ex_evid) + '</h3>';
  var ev = [];
  c.asserts.filter(function (a) { return a.scope !== 'SAFETY_SIGNAL'; }).forEach(function (a) { ev.push('<li>' + sc(a.scope) + ' ' + esc(a.text) + ' – ' + esc(first(a.note_full || a.note, 260)) + (a.pmids.length ? ' (' + a.pmids.map(function (p) { return 'PMID ' + p; }).join(', ') + ')' : '') + '</li>'); });
  if (wObs.length || oObs.length) ev.push('<li class="meta"><i>' + esc(T.ex_ctx) + '</i></li>');
  wObs.slice(0, 4).forEach(function (o) { ev.push('<li>' + sc(o.scope) + ' <i>' + esc(T.ex_need_obs) + ':</i> ' + esc(o.short) + (o.pmid ? ' (PMID ' + esc(o.pmid) + ')' : '') + '</li>'); });
  oObs.slice(0, 3).forEach(function (o) { ev.push('<li>' + sc(o.scope) + ' <i>' + esc(T.ex_need_obs) + ':</i> ' + esc(o.short) + (o.pmid ? ' (PMID ' + esc(o.pmid) + ')' : '') + '</li>'); });
  h += ev.length ? '<ul>' + ev.join('') + '</ul>' : '<p>' + esc(T.ex_no_assert) + '</p>';
  if (!c.asserts.some(function (a) { return WWOX_SC[a.scope]; })) h += '<p><b>' + esc(T.q2_none) + '</b></p>';
  h += '<h3>' + esc(T.ex_counter) + '</h3>' + ((c.against.length || counter.length || safety.length || c.against_note) ? '<ul>' + c.against.slice(0, 6).map(function (t) { return '<li>' + esc(first(t, 300)) + '</li>'; }).join('') + counter.slice(0, 3).map(function (t) { return '<li><i>' + esc(T.q4_need) + ':</i> ' + esc(first(t, 280)) + '</li>'; }).join('') + safety.map(function (a) { return '<li>' + sc(a.scope) + ' ' + esc(a.text) + ' ' + esc(first(a.note_full || a.note, 220)) + '</li>'; }).join('') + (c.against_note ? '<li>' + esc(T.ex_asw) + ': ' + esc(first(c.against_note, 400)) + '</li>' : '') + '</ul>' : '<p>' + esc(T.ex_counter_none) + '</p>');
  h += '<h3>' + esc(T.ex_limits) + '</h3><ul><li>' + esc(T.ex_lim_1) + '</li><li>' + esc(T.ex_lim_2) + '</li><li>' + esc(T.ex_lim_3) + ': ' + esc(c.access.map(function (a) { return T['acc_' + a] || a; }).join(', ') || T.cp_none) + '.</li><li>' + esc(T.ex_lim_4) + '</li></ul>' + ((c.transfer_limits || c.limits.length) ? '<p class="meta">' + esc(T.ex_lim_card) + '</p><ul>' + (c.transfer_limits ? '<li>' + esc(first(c.transfer_limits, 300)) + '</li>' : '') + c.limits.slice(0, 3).map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>' : '');
  h += '<h3>' + esc(T.ex_miss) + '</h3><p>' + (c.missing ? '<b>' + esc(T.q5_miss) + ':</b> ' + esc(first(c.missing, 300)) + '. ' : '') + '</p><p>' + (c.next_full ? '<b>' + esc(T.ex_next) + ':</b> ' + esc(first(c.next_full, 900)) : esc(T.q6_none)) + '</p>';
  h += '<h3>' + esc(T.ex_srcs) + '</h3>' + sourcesHtml(c);
  h += '<p class="meta">' + esc(T.ex_gen) + ' (schema ' + esc(D.schema) + ', ' + esc(D.source) + '). ' + esc(D.source === 'shareable' ? T.ex_share : T.ex_full) + '</p></article>';
  return h;
}
function enterExport(ids) {
  var cs = ids.map(function (i) { return CM[i]; }).filter(Boolean);
  var area = $('export-area');
  area.innerHTML = '<div class="btns noprint"><button type="button" id="x-back">' + esc(T.ex_back) + '</button><button type="button" id="x-print">' + esc(T.ex_print) + '</button><button type="button" id="x-dl">' + esc(T.ex_dl) + '</button><span class="mut">' + esc((cs.length === 1 ? T.ex_n1 : fill(T.ex_n, { n: cs.length }))) + '</span></div>' + (cs.map(exportCard).join('') || '<p class="state-none">' + esc(T.ex_unknown) + '</p>');
  document.body.classList.add('exporting');
  document.title = T.ex_title + ': ' + cs.map(function (c) { return c.short; }).join(', ');
  $('x-back').onclick = function () { history.pushState('', '', location.pathname + location.search); leaveExport(); };
  $('x-print').onclick = function () { window.print(); };
  $('x-dl').onclick = function () {
    var body = cs.map(exportCard).join('');
    var doc = '<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + esc(T.ex_std_title) + '</title><style>' + EXCSS + '</style></head><body>' + body + '</body></html>';
    var a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([doc], { type: 'text/html' })); a.download = 'wwox_card_' + cs.map(function (c) { return c.id; }).join('_') + '.html'; document.body.appendChild(a); a.click(); a.remove();
  };
  window.scrollTo(0, 0);
}
// ---------------------------------------------------------------- one section on its own, for A4 print (#section=selection|hypotheses|predictive)
function enterSection(id) {
  var src = { selection: 'selection', hypotheses: 'hypotheses', predictive: 'predictive', ranking: 'ranking', rankingprint: 'rankingprint' }[id] && $(id);
  var area = $('export-area');
  if (!src) { area.innerHTML = '<p class="state-none">' + esc(T.sec_unknown) + '</p>'; document.body.classList.add('exporting'); return; }
  var clone = src.cloneNode(true);
  Array.prototype.forEach.call(clone.querySelectorAll('.noprint'), function (e) { e.parentNode.removeChild(e); });
  Array.prototype.forEach.call(clone.querySelectorAll('[id]'), function (e) { e.removeAttribute('id'); });
  Array.prototype.forEach.call(clone.querySelectorAll('details'), function (d) { d.open = true; });
  Array.prototype.forEach.call(clone.querySelectorAll('.rk-view'), function (e) { e.hidden = false; });
  Array.prototype.forEach.call(clone.querySelectorAll('.rk-hide'), function (e) { e.classList.remove('rk-hide'); });
  clone.removeAttribute('id');
  area.innerHTML = '<div class="btns noprint"><button type="button" id="x-back">' + esc(T.ex_back) + '</button><button type="button" id="x-print">' + esc(T.ex_print) + '</button></div><div class="secprint" data-section="' + esc(id) + '"></div>';
  area.querySelector('.secprint').appendChild(clone);
  document.body.classList.add('exporting');
  document.title = T.sec_title + ': ' + (src.querySelector('h2') ? src.querySelector('h2').textContent : id);
  $('x-back').onclick = function () { history.pushState('', '', location.pathname + location.search + '#' + id); leaveExport(); if ($(id)) $(id).scrollIntoView(); };
  $('x-print').onclick = function () { window.print(); };
  window.scrollTo(0, 0);
}
function leaveExport() { document.body.classList.remove('exporting'); document.title = TITLE; }

// ---------------------------------------------------------------- one-page synthesis (#brief=): eight labelled fields per card, one A4 page per card
var BFCSS = 'body{font:12px/1.45 system-ui,Segoe UI,Roboto,sans-serif;color:#111;background:#fff;margin:0;padding:14px}.bf{border:1px solid #888;border-radius:6px;padding:10px 14px;margin:0 0 14px;max-width:780px}.bf h2{font-size:15px;margin:0}.bf .meta{color:#444;font-size:11px;margin:3px 0}dl.bf8{display:grid;grid-template-columns:132px minmax(0,1fr);gap:4px 12px;margin:8px 0;counter-reset:bf}dl.bf8 dt::before{counter-increment:bf;content:counter(bf) ". "}dl.bf8 dt{font-weight:700;font-size:11px;border-top:1px solid #bbb;padding-top:4px}dl.bf8 dd{margin:0;font-size:12px;border-top:1px solid #bbb;padding-top:4px;overflow-wrap:anywhere}.bf ul{margin:0;padding-left:16px}.bf li{font-size:11px}.url{display:none;font-family:monospace;font-size:10px;word-break:break-all}.bf ol{margin:0;padding-left:16px}a{color:#000;overflow-wrap:anywhere}.mini{font-size:11px}.mut{color:#444}.chip{border:1px solid #888;border-radius:8px;padding:0 5px}@media print{@page{size:A4;margin:12mm}.url{display:inline}.noprint{display:none}.bf{border:0;padding:0;margin:0;max-width:none;page-break-after:always;break-after:page}.bf:last-child{page-break-after:auto;break-after:auto}dl.bf8{grid-template-columns:34mm 1fr}dl.bf8 dd,dl.bf8 dt{font-size:9pt}.bf li{font-size:8pt}}@media (max-width:560px){body{padding:8px}.bf{padding:8px 10px}dl.bf8{grid-template-columns:minmax(0,1fr);gap:0}dl.bf8 dt{padding-top:6px}dl.bf8 dd{border-top:0;padding-top:1px}}';
function briefSrc(s) {
  if (s.kind === 'PMID') return '<li>' + pmidLink(s.id) + ' <span class="url">' + esc(PUBMED + s.id + '/') + '</span>' + (s.title ? ' ' + esc(s.title) : '') + (s.journal || s.year ? ' <span class="mut">[' + esc([s.journal, s.year].filter(Boolean).join(', ')) + ']</span>' : '') + '</li>';
  return '<li>' + ext(CHEMBL + s.id + '/', 'ChEMBL ' + s.id) + ' <span class="url">' + esc(CHEMBL + s.id + '/') + '</span> <span class="mut">(' + esc(T.tc_compound_id) + ')</span></li>';
}
function briefCard(c, std) {
  var b = c.brief, gl = uniq(c.needs.map(function (n) { return c.links[n].group; }).sort());
  var f = [
    [T.bf_f1, c.needs.length ? c.needs.map(function (n) { return esc(needName(NM[n])); }).join('; ') : esc(T.bf_no_need)],
    [T.bf_f2, '<b>' + esc(c.name) + '</b> <span class="mut">(' + esc(goalTxt(c.goal)) + '; ' + esc(trackTxt(c.track)) + '; ' + esc(statusTxt(c.status)) + ')</span>'],
    [T.bf_f3, esc(b.wwox)],
    [T.bf_f4, esc(b.external)],
    [T.bf_f5, '<ol class="bf-counter">' + b.counter.map(function (x) { return '<li>' + (x.category ? '<span class="mini mut">[' + esc(x.category) + ']</span> ' : '') + esc(x.text) + '</li>'; }).join('') + '</ol>' + (b.counter_more ? '<span class="mini mut">+ ' + esc(fill(T.bf_counter_more, { n: b.counter_more })) + '. </span>' : '') + '<span class="mini mut">(' + esc(T.bf_f5_note) + ')</span>'],
    [T.bf_f6, esc(b.missing)],
    [T.bf_f7, esc(b.next)],
    [T.bf_f8, b.sources.length ? '<ul class="srcs">' + b.sources.map(briefSrc).join('') + '</ul>' : esc(T.bf_src_none)]
  ];
  var dl = f.map(function (x, i) { return '<dt data-field="' + (i + 1) + '">' + esc(x[0]) + '</dt><dd data-field="' + (i + 1) + '">' + x[1] + '</dd>'; }).join('');
  return '<article class="bf" data-brief-card="' + esc(c.id) + '"><h2>' + esc(c.short) + '</h2><div class="meta">' + esc(T.bf_card) + ' ' + esc(c.id) + ' &middot; ' + (gl.length ? gl.map(function (g) { return esc(g + ' ' + T.pos[g].short); }).join(', ') : esc(T.cd_no_need)) + '</div>' +
    (b.window ? '<p class="meta" data-window="1"><b>' + esc(T.bf_window) + ':</b> ' + b.window.states.map(function (x) { return '<span class="chip" title="' + esc(b.window.note) + '">' + esc(T['ws_' + x]) + '</span>'; }).join(' ') + ' ' + esc(b.window.note) + '</p>' : '') +
    '<p class="meta"><b>' + esc(T.bf_data_date) + ':</b> <span data-date="data">' + esc(META.research_update) + '</span> &middot; <b>' + esc(T.bf_needs_rec) + '</b> <span data-date="registro">' + esc(META.needs_built_on) + '</span> &middot; <b>' + esc(T.bf_cat_build) + '</b> <span data-date="catalogo">' + esc(META.catalogue_generated) + '</span> (' + esc(T.bf_dates_note) + ').</p>' +
    '<dl class="bf8">' + dl + '</dl>' +
    '<p class="meta"><b>' + esc(T.bf_dossier) + ':</b> ' + (std ? esc(T.bf_dossier_std) + ' <code>#export=' + esc(c.id) + '</code>' : '<a href="#export=' + esc(c.id) + '" data-dossier="' + esc(c.id) + '">#export=' + esc(c.id) + '</a>') + '. ' + esc(T.bf_warn) + ' ' + esc(T.ex_gen) + ' (schema ' + esc(D.schema) + ', ' + esc(D.source) + '). ' + esc(D.source === 'shareable' ? T.ex_share : T.ex_full) + '</p></article>';
}
function enterBrief(ids) {
  var cs = ids.map(function (i) { return CM[i]; }).filter(Boolean);
  var area = $('export-area');
  area.innerHTML = '<div class="btns noprint"><button type="button" id="x-back">' + esc(T.ex_back) + '</button><button type="button" id="x-print">' + esc(T.ex_print) + '</button><button type="button" id="x-dl">' + esc(T.ex_dl) + '</button><button type="button" id="x-dossier">' + esc(T.bf_dossier_open) + '</button><span class="mut">' + esc((cs.length === 1 ? T.bf_n1 : fill(T.bf_n, { n: cs.length }))) + '</span></div>' + (cs.map(function (c) { return briefCard(c, false); }).join('') || '<p class="state-none">' + esc(T.bf_unknown) + '</p>');
  document.body.classList.add('exporting');
  document.title = T.bf_title + ': ' + cs.map(function (c) { return c.short; }).join(', ');
  $('x-back').onclick = function () { history.pushState('', '', location.pathname + location.search); leaveExport(); };
  $('x-print').onclick = function () { window.print(); };
  $('x-dossier').onclick = function () { location.hash = '#export=' + cs.map(function (c) { return c.id; }).join(','); };
  $('x-dl').onclick = function () {
    var body = cs.map(function (c) { return briefCard(c, true); }).join('');
    var doc = '<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + esc(T.bf_std_title) + '</title><style>' + BFCSS + '</style></head><body>' + body + '</body></html>';
    var a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([doc], { type: 'text/html' })); a.download = 'wwox_sintesi_' + cs.map(function (c) { return c.id; }).join('_') + '.html'; document.body.appendChild(a); a.click(); a.remove();
  };
  window.scrollTo(0, 0);
}


// ---------------------------------------------------------------- state <-> controls <-> hash
function syncCtl() { Object.keys(IDS).forEach(function (k) { $(IDS[k]).value = CF[k]; }); }
function renderAll() { renderNav(); renderCands(); renderRank(); }
function openTech(el) { for (var p = el; p; p = p.parentElement) { if (p.tagName === 'DETAILS') p.open = true; } }
function fromHash() {
  var h = decodeURIComponent(location.hash || ''), m;
  if ((m = h.match(/^#export=(.+)$/))) { enterExport(m[1].split(',')); return; }
  if ((m = h.match(/^#brief=(.+)$/))) { enterBrief(m[1].split(',')); return; }
  if ((m = h.match(/^#section=(\w+)$/))) { leaveExport(); enterSection(m[1]); return; }
  leaveExport();
  if ((m = h.match(/^#c=(.*)$/))) { Object.keys(CF).forEach(function (k) { CF[k] = ''; }); m[1].split('&').forEach(function (kv) { var i = kv.indexOf(':'); if (i > 0) { var k = kv.slice(0, i); if (k in CF) CF[k] = kv.slice(i + 1); else if (k === 'rank') RK.mode = kv.slice(i + 1); } }); syncCtl(); $('rk-mode').value = RK.mode; renderAll(); $('navigate').scrollIntoView(); }
  if ((m = h.match(/^#compare=(.+)$/))) { SEL = m[1].split(',').filter(function (i) { return CM[i]; }).slice(0, 4); renderCands(); }
  if (/^#f=/.test(h)) openTech($('technical'));
  else if (/^#[\w-]+$/.test(h) && $(h.slice(1))) openTech($(h.slice(1)));
}
if (window.matchMedia && window.matchMedia('(max-width:560px)').matches) Array.prototype.forEach.call(document.querySelectorAll('.chain details'), function (d) { d.open = true; });
Object.keys(IDS).forEach(function (k) { $(IDS[k]).addEventListener(k === 'q' ? 'input' : 'change', function () { CF[k] = this.value; renderAll(); }); });
$('c-reset').onclick = function () { Object.keys(CF).forEach(function (k) { CF[k] = ''; }); syncCtl(); renderAll(); };
$('rk-mode').onchange = function () { RK.mode = this.value; renderRank(); };
$('rk-sort').onchange = function () { RK.sort = this.value; renderRank(); };
$('cand-sort').onchange = function () { CSORT = this.value; renderCands(); };
document.addEventListener('click', function (e) { var a = e.target.closest ? e.target.closest('a[data-open]') : null; if (a) { e.preventDefault(); openCand(a.dataset.open); } });

// ---------------------------------------------------------------- IT8 P9: provisional ranking: view, filters, export (all data are D.cur.ranking; no network)
(function () {
  var R = C.ranking;
  if (!R || !$('rk-table')) return;
  var UB = {}; R.units.forEach(function (u) { UB[u.id] = u; });
  var rows = Array.prototype.slice.call(document.querySelectorAll('#rk-table tr.rk-row'));
  var dets = {}; Array.prototype.forEach.call(document.querySelectorAll('#rk-table tr.rk-row-detail'), function (r) { dets[r.getAttribute('data-unit')] = r; });
  var IDS = { view: 'rk-view', cls: 'rk-class', group: 'rk-group', track: 'rk-track', need: 'rk-need', access: 'rk-access', evq: 'rk-evq', type: 'rk-type', origin: 'rk-origin', nx: 'rk-nx', q: 'rk-q' };
  var F = { view: 'general', cls: '', group: '', track: '', need: '', access: '', evq: '', type: '', origin: '', nx: '', q: '' };
  function has(attr, v) { return (' ' + attr + ' ').indexOf(' ' + v + ' ') >= 0; }
  function ok(r) {
    var a = function (n) { return r.getAttribute('data-' + n) || ''; };
    if (F.view !== 'general' && !a('g-' + F.view)) return false;
    if (F.cls && a('class') !== F.cls) return false;
    if (F.group && a('g-' + F.view) !== F.group) return false;
    if (F.track && !has(a('track'), F.track)) return false;
    if (F.need && !has(a('needs'), F.need)) return false;
    if (F.access && !has(a('access'), F.access)) return false;
    if (F.evq && !has(a('evq'), F.evq)) return false;
    if (F.type && a('type') !== F.type) return false;
    if (F.origin && a('origin') !== F.origin) return false;
    if (F.nx && !has(a('nx'), F.nx)) return false;
    if (F.q) { var w = F.q.toLowerCase().split(/\s+/); for (var i = 0; i < w.length; i++) if (w[i] && a('text').indexOf(w[i]) < 0) return false; }
    return true;
  }
  function apply() {
    var n = 0;
    rows.forEach(function (r) { var show = ok(r); r.classList.toggle('rk-hide', !show); dets[r.getAttribute('data-unit')].classList.toggle('rk-hide', !show); if (show) n++; });
    Array.prototype.forEach.call(document.querySelectorAll('.rk-view'), function (v) { v.hidden = v.getAttribute('data-view') !== F.view; });
    $('rk-count').textContent = fill(T.rk_count, { n: n, m: rows.length });
  }
  Object.keys(IDS).forEach(function (k) { var el = $(IDS[k]); el.addEventListener(k === 'q' ? 'input' : 'change', function () { F[k] = this.value; apply(); }); });
  $('rk-reset').onclick = function () { Object.keys(IDS).forEach(function (k) { F[k] = k === 'view' ? 'general' : ''; $(IDS[k]).value = F[k]; }); apply(); };
  function download(name, type, body) { var a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([body], { type: type })); a.download = name; document.body.appendChild(a); a.click(); a.remove(); }
  function cell(v) { return String(v == null ? '' : v).replace(/[\t\r\n]+/g, ' '); }
  function grp(u, v) { var x = u.views[v]; return x && x.member ? x.group : ''; }
  $('rk-tsv').onclick = function () {
    var cols = ['unit_id', 'label', 'unit_type', 'origin', 'class', 'group_broad', 'group_partial', 'lead_broad', 'lead_partial', 'tracks', 'access', 'depth', 'cards', 'wwox_evidence', 'mechanism', 'uncertainty', 'next_priority_broad', 'next_priority_partial', 'evidence_of_molecule', 'evidence_of_mechanism_or_class'];
    var out = [cols.join('\t')];
    rows.filter(function (r) { return !r.classList.contains('rk-hide'); }).forEach(function (r) {
      var u = UB[r.getAttribute('data-unit')];
      out.push([u.id, u.label, u.unit_type, u.origin, u.class, grp(u, 'broad'), grp(u, 'partial'), (u.views.broad.lead || ''), (u.views.partial.lead || ''), u.tracks.join(','), u.access, u.depth + ' ' + u.depth_text, u.cards.join(';'), u.comp.W.text, u.comp.M.text, u.comp.U.text, (u.views.broad.next_priority || {}).level || '', (u.views.partial.next_priority || {}).level || '', u.evidence_level.of_molecule, u.evidence_level.of_mechanism_or_class].map(cell).join('\t'));
    });
    download('wwox_graduatoria_' + R.meta.as_of + '.tsv', 'text/tab-separated-values', out.join('\n') + '\n');
  };
  $('rk-json').onclick = function () { download('wwox_graduatoria_' + R.meta.as_of + '.json', 'application/json', JSON.stringify(R, null, 1) + '\n'); };
  apply();
})();
window.addEventListener('hashchange', fromHash);
renderAll();
fromHash();
document.body.setAttribute('data-cur-ready', '1');
})();
