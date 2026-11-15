"""IT55: five-language passages for the two V14 cells extended with the dated [IT 2026-11-15] clauses (assistant translations, not native-reviewed; old keys replaced by the new hashes)."""
import json
from pathlib import Path
I18N = Path(__file__).resolve().parent.parent / "view/i18n"
OP_OLD, OP_NEW, CT_OLD, CT_NEW = "a98dc83eb0c1", "5cf87de70e15", "ffe61ba5c2e6", "b6219c404c6e"
OP = {
"it": " [IT 2026-11-15] Passo con Ba2+: non è stata trovata alcuna curva concentrazione-risposta primaria del Ba2+ nella finestra 50-200 micromolare per TASK-1, TASK-3 o THIK-1 (TASK-1 è stato testato solo da 0,3 a 10 millimolare); l'affermazione a livello di famiglia qui sopra resta invariata.",
"fr": " [IT 2026-11-15] Étape au Ba2+ : aucune courbe concentration-réponse primaire du Ba2+ dans la fenêtre 50-200 micromolaire n'a été trouvée pour TASK-1, TASK-3 ou THIK-1 (TASK-1 n'a été testé que de 0,3 à 10 millimolaire) ; l'énoncé au niveau de la famille ci-dessus reste inchangé.",
"es": " [IT 2026-11-15] Paso con Ba2+: no se encontró ninguna curva concentración-respuesta primaria del Ba2+ en la ventana de 50-200 micromolar para TASK-1, TASK-3 o THIK-1 (TASK-1 solo se probó de 0,3 a 10 milimolar); el enunciado a nivel de familia anterior no cambia.",
"de": " [IT 2026-11-15] Ba2+-Schritt: Für TASK-1, TASK-3 oder THIK-1 wurde keine primäre Ba2+-Konzentrations-Wirkungs-Kurve im Fenster 50-200 mikromolar gefunden (TASK-1 wurde nur von 0,3 bis 10 millimolar getestet); die obige Aussage auf Familienebene bleibt unverändert."}
CT = {
"it": " [IT 2026-11-15] L'unico EC50 primario raggiunto per quel modulatore (139,4 micromolare) è una corrente nativa in neuroni simpatici di topo, attribuita soprattutto a TREK-2, non un valore su TREK-1 o TRAAK clonati, e il legame tra la riga della revisione e quell'articolo è un'inferenza; gli strumenti K2P sono misure a un solo pH, nessuno testato a un secondo pH.",
"fr": " [IT 2026-11-15] Le seul EC50 primaire atteint pour ce modulateur (139,4 micromolaire) est un courant natif de neurones sympathiques de souris, attribué surtout à TREK-2, et non une valeur sur TREK-1 ou TRAAK clonés ; le lien entre la ligne de la revue et cet article est une inférence ; les outils K2P sont des mesures à un seul pH, aucun testé à un second pH.",
"es": " [IT 2026-11-15] El único EC50 primario alcanzado para ese modulador (139,4 micromolar) es una corriente nativa en neuronas simpáticas de ratón, atribuida sobre todo a TREK-2, no un valor en TREK-1 o TRAAK clonados, y el vínculo entre la fila de la revisión y ese artículo es una inferencia; las herramientas K2P son medidas a un solo pH, ninguna probada a un segundo pH.",
"de": " [IT 2026-11-15] Der einzige erreichte primäre EC50 für diesen Modulator (139,4 mikromolar) ist ein nativer Strom in Sympathikusneuronen der Maus, überwiegend TREK-2 zugeschrieben, kein Wert an klonierten TREK-1- oder TRAAK-Kanälen, und die Verbindung von der Übersichtszeile zu dieser Arbeit ist eine Schlussfolgerung; die K2P-Werkzeuge sind Messungen bei einem pH, keines wurde bei einem zweiten pH getestet."}
for L in ("it", "fr", "es", "de"):
    p = I18N / f"content_{L}.json"; raw = p.read_text(encoding="utf-8"); d = json.loads(raw)
    if OP_NEW in d: continue
    d[OP_NEW] = d.pop(OP_OLD) + OP[L]; d[CT_NEW] = d.pop(CT_OLD) + CT[L]
    d = dict(sorted(d.items()))
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ("\n" if raw.endswith("\n") else ""), encoding="utf-8")
print("ok")
