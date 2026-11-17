# Class-to-member specification trial: materials for the independent forecaster (HE, 2026-11-17)

For SCI. This file holds ONLY the prompt template, the two input blocks with their digests and the scoring definitions. It does not hold HE's predictions and it is not the freeze file. Nothing has been run. Please write your own hashed forecast BEFORE the run (ADV's sequencing: the run starts when your digest exists, or at 08:55Z host clock at the latest).
## Question the trial asks
Does a tool-free step that takes a lever CLASS already named by an enumeration and asks for the specific MEMBERS of the class and the DIRECTION in which each acts on an enzyme or receptor of this type list zinc as a member that LOWERS the activity of a hyperactive receptor guanylyl cyclase (gain-of-function variant, too much cGMP in gut epithelium)? Three tool-free delegates (sonnet): A1 and A2 on input A, B1 on input B.
## Prompt template (sha256 e6687a6dff7313d2827f189809156924ed1fc8bed8bd175e2ac59240d5446710); the only substitution is the placeholder
You are a biochemist. Do NOT use any tool: do not read, search or open any file; answer from your own knowledge only.

DEFECT: a receptor guanylyl cyclase carries a gain-of-function variant and makes too much of its cyclic-nucleotide second messenger in gut epithelium.

BELOW is an ENUMERATION of lever classes written by an earlier step. For EACH lever class named in it, list the specific members of that class that act on an enzyme or receptor of this type, and for each member say in which direction it acts on the enzyme's activity (raises or lowers) and by what mechanism, in one line. Include members that lower the activity of a hyperactive enzyme and members that act in the opposite direction; do not prune and do not rank.

OUTPUT (your final message, nothing else): a table with the columns 'class | member | direction (raises or lowers activity) | mechanism (one line)'. Then one final line beginning 'LOWERING MEMBERS:' that lists every member whose direction is lowering. Mechanism level only; no dose, no recommendation to use any drug.

ENUMERATION:
<ENUMERATION_BLOCK>

## Input A (sha256 e6c9a174ee67c3232fb50ff723911144ea21ae61a70385b4db896c1e35278fab; contains Mg2+, Mn2+ and 'metal', no zinc)
ENUMERATION

Defect in physical-chemical terms (DATO from the question, INFERENZA for the mechanism). A receptor guanylyl cyclase is a single-pass membrane protein. It has an extracellular ligand-binding domain, a transmembrane helix, an intracellular kinase-like homology domain (KHD) that binds ATP and acts as an allosteric regulator, a hinge or coiled-coil dimerisation region, and a C-terminal cyclase domain. Its cycle is: ligand binding, then a conformational switch relayed through the KHD, then dimeric catalytic-domain closure, then Mg2+ or Mn2+-dependent conversion of GTP to cGMP plus pyrophosphate, then desensitisation by phosphorylation and by loss of ligand. The defect is a gain of function. The switch is released too easily (reduced autoinhibition, a lower activation barrier, or hypersensitivity to ligand), so the net rate of GTP to cGMP is too high. The steady-state cGMP level is the balance of synthesis against PDE hydrolysis and ABCC4/ABCC5 efflux, and the effectors are PKG2 (PRKG2), cGMP-gated or cGMP-inhibited PDEs, and CFTR through PKG2. The step that is impaired is therefore the off-state of the activity cycle.

Axis (a), catalytic or activity cycle:
- ATP occupancy of the KHD (allosteric).
- Mg2+/Mn2+ metal site and metal identity.
- GTP substrate concentration and the Km-dependence of the cyclase.
- Product pyrophosphate (product inhibition; pyrophosphatase).
- Redox state, because cysteines in the extracellular domain and ROS influence ligand binding.
- Luminal and cytosolic pH, which tunes uroguanylin against guanylin potency.
- Temperature.

Axis (b), folding and stability:
- ER chaperones: Hsp90, Hsp70, calnexin.
- Chemical or osmolyte chaperones.
- Pharmacological ligands that stabilise the KHD or the ligand-binding domain.
- Temperature-sensitive folding.
- The GOF allele may be over-stable, and destabilisation could be the lever.

Axis (c), assembly, trafficking, localisation:
- N-glycosylation and ER export, including COPII adaptors.
- Dimerisation, with a dominant-negative partner as a lever.
- Apical sorting and lipid-raft or palmitoylation targeting.
- Ligand-site binders: decoy receptors or ligand-sequestering agents, and the ligands themselves (guanylin, uroguanylin; STa-like enterotoxin as the extreme).

Axis (d), substrate and metabolite supply:
- Guanine nucleotide pool: IMPDH, GMP synthase, de novo against salvage, and dietary purine or guanosine.
- cGMP export by ABCC4/ABCC5, which is a transport lever.
- Ion and fluid supply: Cl-, HCO3-, Na+ and water transport and their effect on luminal pH and ligand potency.
- Dietary nitrate, NO and L-arginine, which feed the soluble-GC parallel pool.
- Dietary fibre and short-chain fatty acids, which feed epithelial energetics.

Axis (e), degradation and turnover:
- cGMP hydrolysis by PDE5, PDE9, PDE10, PDE1 and PDE2.
- Receptor desensitisation by KHD phosphorylation and by protein phosphatases.
- Receptor ubiquitination, endocytosis and lysosomal degradation.
- Proteasome and ERAD.
- Ligand turnover: proguanylin processing by proteases.

Axis (f), downstream effector or parallel bypass:
- PKG2 (PRKG2) and CFTR phosphorylation.
- cGMP inhibition of PDE3, which raises cAMP and PKA.
- NHE3 inhibition and the resulting fluid secretion.
- Soluble GC and the NO pool as a competing cGMP source.
- Notch/Atoh1 and Wnt as the secretory-fate machinery.
- NF-kB/TNF/IL-22 cytokine loops.
- Tight-junction machinery (claudins, ZO-1, MLCK).

Axis (g), cell type, timing, dosage:
- Epithelium-specific against global effect.
- Stem-cell compartment (Lgr5) against differentiated cells.
- Developmental against adult onset.
- Heterozygous against homozygous dosage.
- Trans-heterodimer with a null allele.
- Reversibility after inducible removal of the GOF allele.
- Compensation by uroguanylin from the proximal gut.

## Input B (sha256 2416031319252996bd4c753fa84615fd1b2fe9d337644d8576982876a4e5d565; already contains 'zinc' as a supply item, so B is a control for 'is zinc kept and given a direction')
ENUMERATION

Defect in physical-chemical terms. GC-C (GUCY2C) is a single-pass receptor guanylyl cyclase. It has an extracellular ligand-binding domain (guanylin, uroguanylin, bacterial STa), a transmembrane helix, an intracellular kinase-homology domain (KHD) that binds ATP and acts as an allosteric gate, a hinge/coiled-coil, and a C-terminal cyclase domain. The cyclase domain forms an antiparallel dimer with two pseudo-symmetric sites and converts Mg-GTP to cGMP plus PPi. The activity cycle is ligand binding, then KHD/ATP-dependent transduction, then dimer closure, then catalysis, then desensitisation (KHD phosphorylation, ligand dissociation, endocytosis). A gain of function means the cycle's "off" arm is impaired (a lower activation threshold, constitutive or ligand-independent signalling, or loss of desensitisation) or its flux per receptor is raised. Net cGMP is flux in minus PDE hydrolysis and MRP4 efflux. The cGMP signal then acts through PKG2 (PRKG2), cGMP-regulated PDEs (PDE3 inhibition gives a cAMP rise, PDE2 stimulation) and CNG-type channels. The main epithelial outputs are CFTR opening, NHE3 inhibition, and effects on proliferation and differentiation. Caveat (INFERENZA): loss of GC-C also impairs barrier and goblet cells in mice, so the dose-response is probably U-shaped and "normalise" means return to a window, not "minimise".

(a) Catalytic/activity cycle.
- Substrate: GTP pool (de novo and salvage guanine nucleotides, IMPDH/GMPS flux).
- ATP occupancy of the KHD, which potentiates activity.
- Divalent metal: Mg2+ (physiological) versus Mn2+ (hyperactivates in vitro); intracellular free Mg2+.
- KHD phosphorylation and desensitisation.
- Cysteine redox state and oxidative stress.
- Intracellular and luminal pH. Uroguanylin binding is pH-dependent: it is favoured at acidic pH, and guanylin at alkaline pH.
- Allosteric cyclase-domain binders.

(b) Folding and stability.
- ER chaperones and HSP90/CDC37 client maintenance.
- Core and ER-lumen N-glycosylation, which is needed for ligand binding and surface expression.
- Temperature.
- Osmolytes and chemical chaperones.
- Ligand-site binders that stabilise the extracellular domain (they also change activation).

(c) Assembly, trafficking, localisation.
- Dimer or oligomer assembly of the cyclase domains.
- Apical sorting and raft/cholesterol partitioning.
- Endocytosis and recycling (Rab11, myosin Vb).
- Binders of the ligand site (competitive antagonists, ligand scavengers).
- Lipidation.
- Brush-border scaffolds (PDZ proteins).

(d) Substrate and metabolite supply.
- Dietary purines and the guanine-nucleotide pool.
- Dietary Mg2+.
- Luminal ligand supply: proguanylin and prouroguanylin processing, and salt-linked uroguanylin secretion.
- Luminal pH set by bicarbonate and diet.
- Microbial metabolites that drive barrier and goblet cells: butyrate and other short-chain fatty acids, and tryptophan/AHR ligands.
- Vitamin A, zinc.
- Transport of cGMP out of the cell (MRP4).

(e) Degradation and turnover.
- Receptor ubiquitination, lysosomal degradation and shedding.
- PDE5, PDE9, PDE10 and PDE2 hydrolysis of cGMP, and PDE3 cross-talk.
- ABCC4 efflux.
- Ligand degradation by luminal proteases.
- cGMP-to-5'-GMP flux.

(f) Downstream effector or bypass.
- PKG2.
- PKG2 targets CFTR and NHE3 (NHE3 is inhibited via the NHERF2 complex).
- cAMP/PKA via PDE3 inhibition.
- Fluid secretion and shear on the epithelium.
- Notch/ATOH1/Wnt control of secretory lineage.
- Tight-junction regulators (MLCK, ROCK, claudins).
- IL-22/STAT3 and EGFR repair.
- TNF/IFN-γ neutralisation.
- Mucus layer restoration.

(g) Cell type, timing, dosage.
- Epithelium-restricted versus whole-body reversion of the allele.
- Enterocyte versus secretory-lineage versus stem-cell action.
- Immune and enteric-neuron cells (extracellular cGMP acts on nociceptors).
- Heterozygous versus homozygous dosage.
- Allele-specific silencing.
- Neonatal versus adult window.
- Germ-free background.

HYPOTHESES

## Scoring definitions (applied by HE, mechanically and by reading; not blind)
STRICT: zinc (Zn2+) is listed as a member of the metal-ion class with direction LOWERS activity of the receptor guanylyl cyclase (or lowers cGMP output). LOOSE: any metal ion or ion other than Mg2+ and Mn2+ is listed as lowering the cyclase activity. Also counted: how many members are listed for the metal-ion class, how many of them lowering, whether Mg2+ and Mn2+ are given the raising direction, whether the final 'LOWERING MEMBERS:' line includes zinc.
## What a forecast could state (suggestion, you decide)
P(strict in A1 or A2, at least one of two), P(strict in both), P(B1 keeps zinc as lowering), P(loose in A), and anything else you would like scored.
