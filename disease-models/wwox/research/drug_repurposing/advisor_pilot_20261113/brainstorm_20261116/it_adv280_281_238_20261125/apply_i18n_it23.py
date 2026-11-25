"""IT 2026-11-25 (IT23): the three investigation clauses (INV-06, INV-15, INV-16, ADV-239) in it, fr, es and de. Each changed passage keeps its earlier
translation and gets the new clause appended. Idempotent. Run from the repository root after apply_it23.py and `repurposing_view.py i18n --what collect`."""
import json
from pathlib import Path
I = Path("disease-models/wwox/research/drug_repurposing/view/i18n")
# (earlier hash, new hash) in the order INV-06, INV-15, INV-16 (the hash is that of the English passage)
PAIRS = [("a48cb7ee5f80", "14240276ff47"), ("bb44b7e4c4d0", "9a6ae28c1ba7"), ("d3ced5a366c7", "7f8411ae3df0")]
T = {
 "it": ["[IT 2026-11-25, ADV-239: nel deposito corticale di topo della delezione mirata ai neuroni la variazione di CTGF non è stabile: log2 +0.19 con tutte le librerie, da -0.37 a +0.46 se si toglie una libreria.]",
        "[IT 2026-11-25, ADV-239: nella delezione mirata ai neuroni (Syn-Cre) il calo di Pvalb nell'ippocampo viene da 2 librerie di controllo contro 3 knockout (tutte e tre sotto entrambi i controlli); nella corteccia della stessa delezione, 4 contro 3, il calo è più piccolo (log2 -0.59 contro -1.70) e le librerie si sovrappongono. Anche gli altri due contrasti dell'ippocampo calano, con ogni libreria knockout sotto ogni controllo (Nestin-Cre log2 -0.86, 2 contro 2; germline null -1.16, 3 contro 2).]",
        "[IT 2026-11-25, ADV-239: nel topo P47T il trascritto SLC2A1 più alto è una lettura del proencefalo (log2 +0.19 a +0.27, 5 contro 5); il cervelletto va nel senso opposto (-0.17, 3 P47T contro 4 wild type); i genotipi si sovrappongono in tutte e quattro le regioni e, nella corteccia, togliere un animale wild type (F5) lascia meno della metà dell'aumento.]"],
 "fr": ["[IT 2026-11-25, ADV-239 : dans le dépôt cortical de souris de la délétion ciblée sur les neurones, la variation de CTGF n'est pas stable : log2 +0.19 avec toutes les banques, de -0.37 à +0.46 lorsqu'on retire une banque.]",
        "[IT 2026-11-25, ADV-239 : dans la délétion ciblée sur les neurones (Syn-Cre), la baisse de Pvalb dans l'hippocampe vient de 2 banques témoins contre 3 knockout (toutes trois sous les deux témoins) ; dans le cortex de la même délétion, 4 contre 3, la baisse est plus faible (log2 -0.59 contre -1.70) et les banques se chevauchent. Les deux autres contrastes de l'hippocampe baissent aussi, chaque banque knockout étant sous chaque témoin (Nestin-Cre log2 -0.86, 2 contre 2 ; germline null -1.16, 3 contre 2).]",
        "[IT 2026-11-25, ADV-239 : chez la souris P47T, le transcrit SLC2A1 plus élevé est une lecture du prosencéphale (log2 +0.19 à +0.27, 5 contre 5) ; le cervelet va en sens inverse (-0.17, 3 P47T contre 4 sauvages) ; les génotypes se chevauchent dans les quatre régions et, dans le cortex, retirer un animal sauvage (F5) laisse moins de la moitié de la hausse.]"],
 "es": ["[IT 2026-11-25, ADV-239: en el depósito cortical de ratón de la deleción dirigida a las neuronas, el cambio de CTGF no es estable: log2 +0.19 con todas las bibliotecas, de -0.37 a +0.46 al retirar una biblioteca.]",
        "[IT 2026-11-25, ADV-239: en la deleción dirigida a las neuronas (Syn-Cre), la caída de Pvalb en el hipocampo procede de 2 bibliotecas control frente a 3 knockout (las tres por debajo de ambos controles); en la corteza de la misma deleción, 4 frente a 3, la caída es menor (log2 -0.59 frente a -1.70) y las bibliotecas se solapan. Los otros dos contrastes del hipocampo también caen, con cada biblioteca knockout por debajo de cada control (Nestin-Cre log2 -0.86, 2 frente a 2; germline null -1.16, 3 frente a 2).]",
        "[IT 2026-11-25, ADV-239: en el ratón P47T, el transcrito SLC2A1 más alto es una lectura del prosencéfalo (log2 +0.19 a +0.27, 5 frente a 5); el cerebelo va en sentido contrario (-0.17, 3 P47T frente a 4 silvestres); los genotipos se solapan en las cuatro regiones y, en la corteza, retirar un animal silvestre (F5) deja menos de la mitad del aumento.]"],
 "de": ["[IT 2026-11-25, ADV-239: im Kortex-Datensatz der Maus mit neuronengerichteter Deletion ist die CTGF-Änderung nicht stabil: log2 +0.19 mit allen Bibliotheken, von -0.37 bis +0.46, wenn eine Bibliothek entfernt wird.]",
        "[IT 2026-11-25, ADV-239: bei der neuronengerichteten Deletion (Syn-Cre) stammt der Pvalb-Abfall im Hippocampus aus 2 Kontroll- gegen 3 Knockout-Bibliotheken (alle drei unter beiden Kontrollen); im Kortex derselben Deletion, 4 gegen 3, ist der Abfall kleiner (log2 -0.59 gegen -1.70) und die Bibliotheken überlappen. Auch die beiden anderen Hippocampus-Kontraste fallen, wobei jede Knockout-Bibliothek unter jeder Kontrolle liegt (Nestin-Cre log2 -0.86, 2 gegen 2; germline null -1.16, 3 gegen 2).]",
        "[IT 2026-11-25, ADV-239: bei der P47T-Maus ist das höhere SLC2A1-Transkript ein Vorderhirnbefund (log2 +0.19 bis +0.27, 5 gegen 5); das Kleinhirn geht in die Gegenrichtung (-0.17, 3 P47T gegen 4 Wildtyp); die Genotypen überlappen in allen vier Regionen, und im Kortex lässt das Entfernen eines Wildtyp-Tieres (F5) weniger als die Hälfte des Anstiegs übrig.]"],
}
if __name__ == "__main__":
    for lang, clauses in T.items():
        p = I / f"content_{lang}.json"; raw = p.read_text(encoding="utf-8"); d = json.loads(raw)
        for (old, new), cl in zip(PAIRS, clauses):
            if new in d: continue
            if old not in d and lang == "it": continue  # the Italian page has no translation of this passage before this change either
            assert old in d, (lang, old)
            d[new] = d[old].rstrip() + " " + cl
        for old, _ in PAIRS: d.pop(old, None)  # the earlier passages no longer exist in the source
        p.write_text(json.dumps(dict(sorted(d.items())), ensure_ascii=False, indent=1), encoding="utf-8"); print(lang, "ok")
