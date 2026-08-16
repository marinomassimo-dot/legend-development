---
artifact: LEGEND governance — ANNEX I · BOOTSTRAP & DEPLOYMENT
governance_version: 3.1.1
status: FROZEN
normative: yes
materialized_by: plan
materialized_on: 2026-08-16
materialized_from: operator-supplied annex text, transmitted verbatim
body: GOVERNANCE_v3.1.1.md
---

> **Materialization note (Plan).** The text below is the annex exactly as supplied. Nothing was
> added, summarized or reordered. I.5 forbids absolute paths in the governance; the concrete
> local values therefore live in the deployment profile, not here.

---

## ANNEX I — BOOTSTRAP & DEPLOYMENT

### I.1 · Nucleo bootstrap canonico

```
/BOOTSTRAP.md · /governance/ (corpo + annessi + design_records/) · /roles/*.md ·
/deployment/deployment_profile.md · CLAUDE.md root = router minimo (§0.3)
```

### I.2 · Protocollo BOOTSTRAP_CONTROLLER

```
1. prima chat in <REPO_ROOT> → CLAUDE.md → nessun lease ACTIVE → BOOTSTRAP_MODE
2. legge /BOOTSTRAP.md, governance, deployment profile
3. verifica: identità repo · stato root · GOVERNANCE_VERSION · nessun root writer concorrente · worktree
4. crea/verifica worktree: lettore, lettore-b, lettore-c, evidence-index, mirror
5. prepara Agent Card registry (I.4) e inventory scheletro
6. presenta all'operatore la LISTA ESATTA delle 5 chat da aprire (path per ACTOR_ID)
7. ogni attore legge /roles/<suo>.md, si reidrata, si REGISTRA (ACTOR_ID + SESSION_REF + capabilities dichiarate)
8. L1 messaging smoke → L2 capability smoke (capabilities → VERIFIED/UNVERIFIED)
9. condizioni PASS → acquisizione ORCHESTRATOR_LEASE (I.3)
10. ORCHESTRATOR_REGISTRATION durevole → ACTIVE_ORCHESTRATOR → governance ordinaria
```

Perimetro pre-promozione: SOLO artefatti di bootstrap. Lease ACTIVE già esistente → la chat è OBSERVER.

### I.3 · ORCHESTRATOR_LEASE — singleton con scadenza

```
LEASE: ACTOR_ID=orchestrator / SESSION_REF / GOVERNANCE_VERSION / ROOT_HEAD /
       ACTIVATED_AT / LAST_RENEWED (heartbeat) / EXPIRES_AT / STATUS: ACTIVE | STALE | RELEASED
```

Un solo ACTIVE; rinnovo via heartbeat; scadenza → STALE; reacquisition SOLO su STALE/RELEASED con successione registrata; in dubbio → operatore. Lease STALE con Orchestrator vivo ma degradato = segnale di rotazione, non usurpazione.

```
GUARANTEE:  nessuna autoproclamazione; successione tracciata
FAILURE:    due sessioni leggono STALE quasi simultaneamente e tentano entrambe la reacquisition (nessun CAS)
DETECTION:  doppio record sulla stessa successione → alla scrittura o alla riconciliazione; GATE 0 blocca i batch
RECOVERY:   entrambe si fermano (stop condition); l'operatore designa; successione registrata
```

### I.4 · LEGEND AGENT CARD — identità e capacità **[v3.1.1, E5a]**

```
ACTOR_ID (permanente) / ROLE / WORKTREE / ROLE_CONTRACT (path) / ROLE_CONTRACT_HASH
CAPABILITIES: [{capability, declared_in_role_contract, status: VERIFIED (L2) | UNVERIFIED, last_verified}]
CURRENT_SESSION_REF (effimero) / CURRENT_SESSION_ID / STATUS / LAST_SEEN
```

Dopo crash: ACTOR_ID identico, SESSION_REF nuovo. Il `from` è routing; l'ACTOR_ID è identità, provenance, learning. Orchestrator assegna sulle capabilities VERIFIED; una capability con fallimenti ripetuti torna UNVERIFIED (nuovo smoke). Continuità storica col lineage `actor_id → sessionId` del runtime background.

```
GUARANTEE:  assegnazioni su capacità verificate, non presunte (CONFIGURED != PROVEN)
FAILURE:    capability degradata dopo L2 (deriva del runtime)
DETECTION:  fallimenti ripetuti sullo stesso tipo di task → Mirror coordination review
RECOVERY:   retrocessione a UNVERIFIED → nuovo smoke → riabilitazione
```

### I.5 · DEPLOYMENT_PROFILE — portabilità

```
PORTABLE LAB DEFINITION (repo): governance, annessi, design_records, roles, BOOTSTRAP.md, skills, learning, actor definitions
LOCAL RUNTIME INSTANCE (per macchina): REPO_ROOT, WORKTREE_ROOT, INTERACTION_PROFILE (VISIBLE_VSCODE),
                                       RUNTIME_INSTANCE_ID, SESSION_REFS correnti
```

Nessun path assoluto nella governance. Stesso lab, altra macchina → cambia solo la runtime instance.

### I.6 · Fresh-install vs migration

Migration: Plan materializza → review → commit → bootstrap §47. Fresh-install: la governance è già nella repo — si legge, non si rimaterializza. Criterio di accettazione: il test §0.1 del corpo.
