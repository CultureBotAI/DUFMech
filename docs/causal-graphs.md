# DUF Causal Graphs

The corpus-wide goal is to review and update every family's causal knowledge, not
to populate graph slots or treat absent data as evidence that no mechanism exists.
All 8,296 families in the October 10 snapshot remain in scope. Initial inventory
found no overlays, assertions or graphs; every projection was SEEDED.

## Native Representation

Human-owned `curation/families/PFxxxxx.yaml` may supply `causal_graphs`, which the
guarded builder projects into `data/families/`. Graphs use the shared `graph_list`
field shape (`graph_id`, `nodes[].node_id`, `edges[].subject/object/predicate`).
This is native support, not adoption of the fleet causal-coverage capability;
that capability stays disabled pending its separate compatibility/adoption gates.

Each graph has an exact tested scope, context, family mapping, limitations,
typed nodes, and nonempty evidence-backed edges. Each edge states directness,
support, mechanism, evidence kind, and hash-checked primary-source extracts under
the existing ClaimEvidence contract. Keep identity annotations separate from the
experiment supporting causality. A domain annotation does not turn a whole-gene
phenotype into a domain-specific biochemical mechanism.

`MECHANISTIC` requires a directly observed experimental step. `PHENOTYPIC`
requires an observed experimental effect but does not assert a resolved molecular
mechanism. `HYPOTHETICAL` cannot contain an OBSERVED edge. Mixed graphs keep each
edge's separate support label. These checks prevent categorical overstatement;
they cannot decide whether a paper actually supports an interpretation.

Native validation rejects duplicate IDs/relations, dangling endpoints, unused
nodes, missing evidence, invalid quotations/hashes and blank scope/mechanism.
Cycles require an explicit feedback explanation plus the normal edge evidence.
Changes enter the semantic review digest and require canonical history even if
the author accidentally leaves curation_status as SEEDED.

The family page renders a directed edge table with scope, limitations and source
quotations; the JSON preserves full node/edge data. Rendering does not imply
publication, scientific review or status promotion.

## Per-Family Workflow

Use `dufmech-causal-graphs` and the native curation/review skills. Investigate each
family's primary evidence and tested members; preserve uncertain or contradictory
results. Do not infer causal edges from similarity, genomic adjacency or shared
annotations. A family with no supported edge stays graphless and receives a scoped
review explaining the searches, evidence gaps and any access limits, not a dummy
graph or a family-wide claim of ignorance.

Append actual canonical history before `just records --apply`. Save a completed
review through the native structured saver, preserving its exact digest and
scientific-review scope. IN_PROGRESS remains appropriate for incomplete coverage.
Passing tests do not promote a family to REVIEWED.

The identity exports also carry `curation_status`: KGX nodes have a dedicated
column and SSSOM records include it in their comments. After a status change,
regenerate them with `just exports --apply`, inspect the scoped changes, and run
`just exports --check`. These association exports do not serialize causal edges.

`just causal-graphs` emits a deterministic, full-membership structural inventory
of validated, current projections. It includes each semantic digest and counts
both graphless and graph-bearing families. It does not label records reviewed or
infer scientific completion from the presence of an edge. Retained reports and
the family's actual reviewed scope remain authoritative for that determination.

After regenerating records, refresh the retained structural report with
`just causal-graphs --apply`. `just causal-graphs --check` compares every byte,
including all family semantic digests, and fails on a missing or stale report
without writing. This check is part of `just qc`. The default command still emits
JSON to stdout without modifying the repository. Inventory refresh never changes
family content, history, or scientific review status.

## Progress

Worktree: `/private/tmp/dufmech-causal-graphs`, branch `feat/duf-pf01976-causal-evidence`.
Starting source revision: `9d7a87f74786813fcdf65801bdf940d79cc7a56e`.
Initial inventory and implementation began at 2026-10-11T04:00:01Z.
The initial batch was merged in PR #199. Continuation begins from
`2da6c366b06615fbb6c34379318771fe09f4cfda`. PF01972 was published through merged
[PR #200](https://github.com/CultureBotAI/DUFMech/pull/200). PF01973 was published
through PRs #202, #208 and #210. The current PF01976 continuation starts from
`d53afef37b7e7f0667511c3e919a44c1270631a4`, the merged PR #210 revision.
Earlier local-only checkpoints below describe their state at the time, not the
current release status.

One hundred and twenty-six families now have 1,680 evidence-linked edge entries in 791
scoped graphs. Of these, 1,653 are OBSERVED, twenty-three are HYPOTHESIZED,
three are INFERRED and one is CONTESTED;
counts are structural, not numbers of independent experiments:

- PF04149 (DUF397): Scr2 dependency and two medium-specific joint-gene
  perturbations; three PHENOTYPIC, INDIRECT edges.
- PF01937 (former DUF89): separate YMR027W phosphatase and deletion contexts;
  one MECHANISTIC, DIRECT edge and one PHENOTYPIC, INDIRECT edge.
- PF05114 (former DUF692): purified OB3b MbnBC activity, with explicit partner
  and construct limitations; one MECHANISTIC, DIRECT edge.
- PF01883 (former DUF59): SufT deletion and normalized AcnA activity in defined
  USA300 LAC derivatives; one PHENOTYPIC, INDIRECT edge.
- PF03883 (former DUF328): separate YaaA deletion effects on unincorporated iron
  and radical signal in peroxide-scavenging-deficient cells; two PHENOTYPIC,
  INDIRECT edges.
- PF06568 (former DUF1127): CcaF1 overexpression and measured CcsR1/UpsM RNA
  half-lives; two PHENOTYPIC, INDIRECT edges in one graph.
- PF01887 (former DUF62): intact SaDUF62 and commercial-SAM hydrolysis;
  one MECHANISTIC, DIRECT edge without a sulfur-isomer or cellular-role claim.
- PF07005 and PF17042 (former DUF1537): the same intact ReDtnK phosphorylation
  experiment, mapped separately to its N- and C-terminal domains. Each record
  retains one MECHANISTIC, DIRECT edge; this is not independent replication or
  evidence that either isolated domain is sufficient.
- PF08759 (former DUF1792): the dGT1 1-272 construct transfers glucose to
  premodified Fap1; one MECHANISTIC, DIRECT edge, not complete Fap1 maturation.
- PF01885 (Tpt1/KptA): intact CthTpt1 removes terminal 2'- and 3'-phosphates
  from separate synthetic RNA substrates; two MECHANISTIC, DIRECT edges in one
  graph. Approximately stoichiometric terminal reactions and negative homolog
  results limit turnover and family-wide claims.
- PF01996 (CofE): intact Af-CofE produces predominant F420-2 from F420-1;
  one MECHANISTIC, DIRECT edge. Shared-method salt notation and assay timing
  remain unresolved, and structural catalytic microsteps are not observed edges.
- PF01796 (former DUF35 OB fold): separate M. tuberculosis Ltp2-DUF35 complex
  and T. curvata DUF35-addition assays; two MECHANISTIC, DIRECT edges. Exact
  M. tuberculosis truncation boundaries remain unresolved.
- PF12172 (DUF35 zinc ribbon): the same T. curvata addition experiment as in
  PF01796, mapped to the second domain in the tested construct; one MECHANISTIC,
  DIRECT edge. This is not independent replication or isolated-domain sufficiency.
  The M. tuberculosis experiment is excluded because its verified protein's
  current Pfam annotations do not include PF12172.
- PF02410 (former DUF143/RsfS): purified E. coli RsfS reduces the associated
  70S fraction and oligo(Phe) output; two MECHANISTIC, DIRECT edges in one graph.
  A separate PHENOTYPIC, INDIRECT edge records a whole-gene deletion's prolonged
  growth adaptation after LB-to-M9 transfer, with distinct complementation
  outcomes retained. These are not joined into an experimentally observed chain.
- PF01784 (DUF34/YbgI): one PHENOTYPIC, INDIRECT edge records lower early liquid
  OD600 of the ybgI folE double mutant compared with folE alone, in dT-supplemented
  LB. Conflicting broader growth prose, inaccessible strain details and missing
  established rescue of this endpoint remain explicit; no general metal-insertase
  or GTP-cyclohydrolase function is assigned.
- PF02130 (YbeY/UPF0054): two MECHANISTIC graphs retain three DIRECT edges for
  short synthetic-RNA cleavage and joint YbeY/RNase R degradation of rRNA in
  deletion-derived and kasugamycin-derived 70S preparations. The joint treatment
  is not split into independently sufficient enzymes or an observed sequence of
  catalytic microsteps. Historical P77385 is resolved to the E. coli successor
  P0A898 by organism context; exact purified tag and extended methods remain open.
- PF02583 (former DUF156/CsoR): separate B. subtilis purified-protein and cellular
  reporter graphs retain one MECHANISTIC, DIRECT decrease in operator binding
  after Cu(I) loading and one PHENOTYPIC, INDIRECT increase in reporter output
  after csoR replacement. Ectopic complementation, binding-fit limitations and
  the source's correction of an earlier YhdQ attribution remain explicit.
  These are not joined into an observed copper-to-efflux or growth pathway.
- PF01837 (former DUF39/HcyBio): two bacterial PHENOTYPIC graphs retain three
  INDIRECT edges for Miyazaki F pooled-fitness loss, its methionine rescue,
  and G20 individual-mutant plate-growth loss with genetic complementation.
  A deleted UniProt entry is resolved through an exact NCBI/UniParc sequence
  match. The corrected G20 complementation start and conflicting medium labels
  remain explicit; proposed sulfur-transfer chemistry is not adopted.
- PF07796 (DUF1638): one PHENOTYPIC graph retains two INDIRECT edges for
  P. inhibens PGA1_c13340 insertion-mutant fitness in ammonium/sucrose and
  methionine/sucrose conditions. The nutrient comparison is not silently
  rewritten as an extra supplement in unchanged medium. B12 reactivation,
  cofitness-based partners and a later study's other-protein rescue remain
  separate hypotheses or leads, not observed DUF1638 chemistry.
- PF00563 (EAL): one MECHANISTIC graph retains two DIRECT edges for purified
  PAO1 RocR c-di-GMP hydrolysis and its E352Q turnover decrease. Full-length
  reference Q9HX69 maps to PF00563 at 147-379; the graph does not claim
  isolated-domain sufficiency, a proven proton-transfer microstep or a cellular
  signaling chain. The later study's one-/two-metal uncertainty stays explicit.
- PF00990 (GGDEF): one MECHANISTIC graph retains three DIRECT, OBSERVED edges
  for full-length PleD synthesis, product inhibition and joint DivJ-plus-ATP
  stimulation. The negative product-feedback cycle is explicitly justified;
  it is not a measured cellular trajectory or a structural-motion proof.
  CB15/NA1000 identical sequences do not establish two independent experiments.
- PF01139 (RtcB): three MECHANISTIC graphs retain protein guanylylation,
  5'-blocked RNA processing and separate 5'-OH RNA ligation. Three edges are
  DIRECT, OBSERVED; the specific RNA 3'-ppG chemical-conversion assignment is
  DIRECT, INFERRED from the experimental evidence. Blocked and ligatable
  substrates are not joined into one directly tracked molecular pathway.
- PF01206 (TusA): two graphs retain DIRECT, MECHANISTIC stimulation of purified
  IscS sulfide-production activity and a separate PHENOTYPIC decrease in the
  Fe-S assembly-associated A456 readout at equimolar TusA/IscU. Both edges are
  OBSERVED, but the latter has UNRESOLVED directness; neither establishes an
  intracellular sulfur-diversion chain or the entire TusA relay chemistry.
- PF01519 (DUF16): separate M129 MPN104-29 and MPN524-74 insertion contexts
  retain four PHENOTYPIC, INDIRECT, OBSERVED edges. MPN104 gliding frequency
  and MPN524 frequency, normalized velocity and glass binding are reduced.
  Missing target-specific genetic rescue and predicted-only polarity controls
  prevent a resolved domain mechanism or transfer to the MPN010 structure.
- PF01579 (DUF19): four PHENOTYPIC graphs retain four INDIRECT, OBSERVED edges
  for EXC-13 RNAi canal defects, C36C5.5 RNAi reporter aggregation, and separate
  C36C5.5 overexpression effects with and without coelomocytes. Gene-resolved
  reference mapping distinguishes O01454 from O16405 and excludes O16406 as the
  wrong C36C5 gene. No shared domain mechanism or direct holdase reaction is
  inferred from these phenotypes or from co-purification.
- PF01882 (DUF58): one PHENOTYPIC graph retains two INDIRECT, OBSERVED edges
  for Slr2013 Y294Stop suppressor-associated photoautotrophic growth and oxygen
  recovery in the psbDI-T192H/psbDII-deleted background. Region-level genetic
  transfer, partial-domain truncation and conditional negative controls remain
  explicit; neither isolated-domain sufficiency nor direct chaperone/protease
  chemistry is established. The parallel outcomes are not joined into a serial
  experimentally resolved pathway.
- PF00668 (Condensation): one MECHANISTIC graph retains four DIRECT, OBSERVED
  edges for joint holo-TycB1/GrsA DKP output and separate R62A/H147R/H147V
  substitutions. The first TycB PF00668 interval is mapped explicitly; its
  other matches, including the epimerization region, do not inherit this assay.
  The coupled endpoint does not establish an elementary histidine mechanism,
  isolated-domain sufficiency or enzymatic catalysis of final cyclization.
- PF00672 (HAMP): three PHENOTYPIC graphs retain three INDIRECT, OBSERVED
  edges for G235E increased CW rotation in UU1250, G235C decreased CW rotation
  in UU1535, and G235P loss of the WT soft-agar chemotactic response. Distinct
  host adaptation backgrounds and assays remain separate. Weighted rotation
  estimates are not direct kinase measurements or proof of HAMP packing states;
  G235P's roughly WT rotation does not rescue its chemotaxis defect.
- PF00892 (EamA/former DUF6): one PHENOTYPIC graph retains three INDIRECT,
  OBSERVED edges for YdeD deletion, plasmid rescue and WT plasmid expression
  affecting peroxide-stressed colony growth. Both reference repeats are mapped;
  neither isolated-repeat activity nor the complete cysteine/cystine shuttle is
  established by this endpoint. Multi-gene pDES interventions remain separate.
- PF00893 (SMR): three MECHANISTIC graphs retain five DIRECT, OBSERVED edges
  for EmrE proton efflux under a pH gradient, efflux with positive-inside
  potential, influx with negative-inside potential and the two E14Q losses.
  Proton direction is measured; exact drug microsteps, a unique symport route
  and universal strict 2:1 coupling are not promoted to observed mechanisms.
- PF00902 (TatC): three MECHANISTIC graphs retain five DIRECT, OBSERVED edges
  for Tat-positive protected mature product, CCCP sensitivity, TatAC processing,
  RR-to-KK loss and TatC-only processing. Cleavage is not mature-protein transport,
  and TatC-only means the sole Tat component in native vesicles, not purified
  TatC sufficiency. Reference mapping and the cited C-terminal tag are explicit;
  hairpin insertion remains an interpretation rather than an observed microstep.
- PF00924 (MscS beta-domain): three MECHANISTIC graphs retain six DIRECT,
  OBSERVED edges for G168D adaptation loss, N117K/G168D restoration, reversible
  DTT-dependent N117C/G168C activity and separate WT/G168D crowding responses.
  The 2011 adaptation and 2014 inactivation protocols retain distinct conditions.
  Pfam residues 114-180 are not identical to the structural beta domain 128-181;
  neither salt-bridge chemistry nor S-S locking or cage motion is directly shown.
- PF01026 (TatD): four graphs retain seven OBSERVED edges: six DIRECT biochemical
  effects for tagged ssDNA digestion, H62A/E91A/E201A/D203A decreases and separate
  untagged internal-THF duplex incision, plus one INDIRECT chronic-peroxide
  growth effect of whole-gene deletion. Tagged/untagged preparations and
  terminal-abasic/internal-THF substrates remain distinct. No catalytic metal
  count, calcium-only activity switch or intracellular repair chain is asserted.
- PF01027 (Bax1-I/YetJ): one MECHANISTIC graph retains two DIRECT, OBSERVED
  decreases in calcium influx for lower pH and D171N in the 2020 proteoliposome
  assay. Exact supplementary conditions remain unresolved. The earlier pH-7
  optimum differs from this pH-8 maximum; no universal pH rule, observed
  protonation/pore motion or transfer to human apoptosis is claimed.
- PF01042 (Ribonuc_L-PSP/RidA): five MECHANISTIC graphs retain nine DIRECT,
  OBSERVED effects in coupled threonine-rate, ferricyanide-endpoint, substitution,
  serine-rate and retained-IlvE assays. Required partners remain explicit; no
  elementary hydrolysis trajectory or stand-alone RidA dehydratase is asserted.
  The IlvE caption/Methods addition-order discrepancy prevents a proven repair
  or reversal claim. Frozen RNase labels are not transferred to Salmonella.
- PF01060 (TTR-52): four graphs retain six OBSERVED effects, three INDIRECT
  cellular effects and three DIRECT lipid-strip substitution effects. sm211/V43M
  corpse persistence and CED-1 rings, tm2078 WT rescue and D51A/D80A/N85A binding
  remain distinct. The deposited cDNA translation matches G5ED35 exactly.
  Nested microscopy sampling, heat-shock intervention, mutant-label conflicts
  and modeled WT geometry limit stronger domain or atomic-mechanism claims.
- PF01062 (Bestrophin): five MECHANISTIC graphs retain eight DIRECT, OBSERVED
  effects for chicken BEST1 chelation, calcium reactivation, DIDS, normalized
  neck-mutant current and clasp-mutant flux/rescue. Retired E1C3A0 matches the
  modern reference exactly over tested 1-405, not full-length. Bilayer orientation,
  voltage, joint substitutions, processed Thr2 start and coupled ACMA readout
  remain explicit; no atomic trajectory or KpBest selectivity is transferred.
- PF01121 (CoaE): three MECHANISTIC graphs retain five DIRECT, OBSERVED effects
  and one DIRECT, CONTESTED R140A loss claim. E. coli preparative CoA formation
  is distinct from mycobacterial mutant kinetics. Opposite L114A turnover changes
  belong to different substrate series. R140A no-reaction text/Table 2 conflicts
  with a Figure 5 Km fit; other parameter and clone-primer inconsistencies remain
  open rather than being silently corrected or promoted to chemical mechanisms.
- PF01128 (IspD): four graphs retain eleven OBSERVED effects, six DIRECT in
  purified product, isotope-trapping and fitted-turnover assays, and five with
  UNRESOLVED directness in crude extracts. Inactive unpurified variants are not
  represented as directly measured catalytic defects. The 2004 full text is a
  primary proof with numerical-label conflicts; final-publication comparison,
  complete clones and mutant normalization remain open. No atomic trajectory
  or family-wide substrate specificity is inferred.
- PF01168 (alanine racemase N domain): four MECHANISTIC graphs retain seven
  DIRECT, OBSERVED effects for separate racemization directions, K39A loss,
  D-alanine preincubation, joint PMP/pyruvate reactivation and tritium release.
  Intact P10724 maps at 12-229, including K39 but excluding Y265. Separate
  reaction vessels are not a tracked cycle; methylamine-dependent tritium
  release is not quantified recovery of normal racemase turnover. Clone and
  assay metadata, a concentration conflict and a missing displayed control
  remain explicit.
- PF01169 (GDT1/former UPF0016): six graphs retain eight OBSERVED effects.
  Two DIRECT gradient interventions increase calcium/manganese uptake readouts
  in DML1; four expression-associated pH effects have UNRESOLVED protein-level
  attribution; two INDIRECT effects concern native yeast compartment pH after
  glucose re-addition. Both reference repeats are mapped. Historical tagged
  delta23 constructs, calibration wording and different starvation protocols
  are not silently transferred; no isolated-transporter stoichiometry or
  directly observed native reverse cycle is claimed.
- PF01171 (PP-loop/TilS): three MECHANISTIC graphs retain eight DIRECT,
  OBSERVED effects for lysine/ethanolamine product formation and separate
  E. coli S100 and purified B. subtilis IleRS preparation comparisons. The
  cited Z50870 translation and primer ends match current P52097. Intact-RNA
  mass does not independently localize the modification, and unrepurified
  reaction preparations can carry over components. Distinct normalization,
  contaminated analogs and later ortholog-specific behavior remain explicit;
  no whole-family atomic pathway or in-vivo decoding outcome is inferred.
- PF01172 (SBDS_N/former UPF0023): four MECHANISTIC graphs retain seven
  DIRECT, OBSERVED effects for whole-SBDS eIF6 release and EFL1 hydrolysis.
  Human factors with mouse pre-60S and rabbit mature 60S are separate systems.
  Q9Y3A5/NP_057122.2 map PF01172 to 14-100; R126T/K151N are outside it.
  K151N retains stimulation over the no-SBDS baseline but reduces release in
  another assay; separate vessels are not an observed conformational trajectory.
- PF01174 (SNO/former UPF0030): five MECHANISTIC graphs retain five DIRECT,
  OBSERVED effects in untagged strain-168 PdxT/PdxS preparations: coupled
  glutaminase activation, joint PLP formation, ribulose/ammonium dependence
  and two separate acivicin readouts. P37528 maps PF01174 to 6-188. Product
  HPLC/MS/NMR support PLP, but conflicting concentrations, rate units and
  mass descriptions remain explicit. Earlier SMY/His6 contexts are not transferred.
- PF01205 (Impact_N/former UPF0029): three PHENOTYPIC graphs retain three
  INDIRECT, OBSERVED effects for GST-Yih1-associated eIF2alpha phosphorylation
  loss and separate H1511/ESY11001b starvation-growth losses. The cited GI matches
  P25637, with PF01205 at C-terminal 144-251 and separate RWD at 6-108. The
  frozen name is not a coordinate definition; RWD-only activity is not assigned
  to the ancient domain. The unrelated PCI8 YIH1 synonym is excluded.
- PF01207 (Dus/former UPF0034): five MECHANISTIC graphs retain five DIRECT,
  OBSERVED redox/product effects for yeast Dus2 with NADPH, synthetic RNA,
  knockout-derived RNA and separate aerobic/anaerobic bacterial RNA assays.
  P53720 maps at 32-352. C117A primers disagree at H120/Q120, so no mutant-specific
  edge is adopted. Concentration, template and temperature differences remain
  explicit; colorimetric product detection is not site-resolved D20 chemistry.
- PF01255 (Prenyltransf/former UPF0015): three graphs retain one DIRECT,
  MECHANISTIC product-formation edge and two PHENOTYPIC edges with UNRESOLVED
  directness for detergent/magnesium effects in a coupled phosphate assay.
  All three are OBSERVED. Archived Q47675 exactly matches P60472, PF01255
  24-244. Reported C50/C55-compatible TLC is unshown; residual omission output
  prevents absolute-dependence claims. The yeast coupling enzyme remains explicit.
- PF01256 (Carb_kinase/former UPF0031): five MECHANISTIC graphs retain five
  DIRECT, OBSERVED conversions in yeast ATP-dependent and bacterial ADP-dependent
  NADHX/NADPHX assays. P36059 maps at 35-305; P31806 maps at 258-496 with a
  separate PF03853 interval at 40-199. Intact YjeF's R-enriched-mixture repair
  is not isolated-domain epimerization. Unequal doses, mixed substrates and
  distinct pH/assay contexts prevent a comparative rate or atomic-cycle claim.
- PF01345 (CLIPPER/former DUF11): three MECHANISTIC graphs retain three
  DIRECT, OBSERVED K715A effects on thermal-transition temperature, CD recovery
  and intact-domain survival during proteolysis. A0A1Y3CHT7 708-828 contains
  PF01345 712-812; Table S6 translations and 9IFR verify the intended fragment.
  N748/D749 contradicts the proposed Asp748 label, and Methods alternate K517A
  with sequence-confirmed K715A. No exclusive crosslink or native-adhesion
  mechanism follows from these effects; biochemical tag processing remains open.
- PF01458 (SUFBD_core/former UPF0051): four graphs retain seven OBSERVED
  effects, five DIRECT in purified SufB-complex assays and two INDIRECT for
  SufD H360A cellular phenotypes. P77522 maps at 225-466 and P77689 at 166-393.
  Basal SufSE output, residual C405A sulfur and lower mutant SufD abundance
  remain explicit. DTT-containing activity and no-DTT loading, and unsupplemented
  plates and supplemented cultures, are separate contexts; the sulfur tunnel
  and atomic ligand sequence are not adopted as observed chemistry.
- PF01493 (GXGXG): three graphs retain two DIRECT, MECHANISTIC salt-dependent
  GltSHis particle-radius effects and one INDIRECT, PHENOTYPIC delta40 production
  effect. Q05755 PF01493 1249-1496 corresponds to mature 1213-1460; the deposited
  1EA0 sequence resolves the 36-residue offset. Delta40 partly overlaps the
  domain and removes an outside tail; delta7 is outside it. Low-salt dilution
  retains 0.1 M NaCl. Neither size changes nor reported production failure
  establish isolated-domain assembly sufficiency or directly measured misfolding.
- PF01513 (NAD_kinase): five DIRECT, OBSERVED MECHANISTIC effects retain N75T's
  lower ATP-associated activity, increased activity with three separately
  specified phosphate donors, and a distinct qualitative TLC product endpoint.
  P0A7B3 PF01513 8-121 contains N75, but full historical constructs remain
  uncertain because of printed terminal-primer differences. WT polyphosphate
  activity is nonzero, tripolyphosphate is an exception, and donor mixtures
  are not equimolar. No atomic recognition rule or physiological switch is inferred.
- PF01535 (PPR): two MECHANISTIC graphs retain four DIRECT, OBSERVED HCF152
  mini-protein binding effects: two single-mutant losses and two matched
  double-mutant partial rescues. K426 maps within current PF01535 416-442;
  N464 is outside both current hits. Thioredoxin/six-His fusions, old motif
  conventions and inaccessible supplementary primers/gels limit interpretation.
  Operational half-binding concentrations do not establish atomic RNA contacts,
  native chloroplast processing or a universal PPR recognition code.
- PF01549 (ShK, former DUF18): two DIRECT, OBSERVED MECHANISTIC graphs retain
  recombinant mature-peptide inhibition of mouse Kv1.3 and Kv1.1 currents in
  separate L929 lines. Printed primers encode exact P29187 after DDDDK.
  Family association is supported by the curated PF01549 description and
  integrated IPR003582 3-35, not a current direct Pfam hit or seed membership.
  Current-block midpoints are not independent physical binding constants;
  atomic pore contacts, cellular mediation and family-wide transfer are excluded.
- PF01554 (MatE): three graphs retain six OBSERVED effects, one INDIRECT
  cellular sodium/ethidium-fluorescence response and five DIRECT purified-binding
  effects. Historical AAF94694.1 D36/E255/D371 map to Q9KRU4 D32/E251/D367
  within PF01554 17-176/243-404; the initiating sequence differs. The 12.5/20 mM
  glucose discrepancy, low-concentration sodium effect and residual mutant
  binding remain explicit. Binding fits and simulations are not observed ion
  trajectories, site counts or a complete transport cycle.
- PF01594 (AI-2E_transport): seven PHENOTYPIC graphs retain eight INDIRECT,
  OBSERVED effects for whole-gene TqsA deletion and extracellular complementation.
  P0AFS5 maps at 17-328, but BW25113 constructs are not independently resequenced.
  BB170 activity and lsr::lacZ output remain reporter proxies, not chemical
  concentrations. Distinct OD600/antibiotic contexts and the opposite LB
  attached-mass response are preserved. The 2022 study's inability to demonstrate
  transport prevents treating structural/binding proposals as observed export.
- PF01595 (CNNM/former DUF21): three MECHANISTIC graphs retain eleven DIRECT,
  OBSERVED effects for intact MtCorB/TtCorB reconstitution, separate TtCorB
  loading/substrate series and seven substitutions. Tt means Tepidiphilus,
  not Thermus; current domains are 19-189 and 13-187. Mutant incorporation
  controls coexist with altered SEC profiles and residual activity. Native
  direction, counterion/stoichiometry, the Mt detergent discrepancy and
  elementary structural motions remain unresolved.
- PF01638 (HxlR/former DUF24): four graphs retain seven OBSERVED effects,
  four DIRECT biochemical and three INDIRECT reporter responses. Purified
  plus-12-Da product, WT/C11A EMSA, lower-range K13A EMSA and BW25113 GFP
  phenotypes are separate contexts. C11/K13 lie outside PF01638 19-107;
  GSH processing, possible pBAD S2G and the 1/0.6-mM formaldehyde discrepancy
  remain explicit. K13A retains binding and high basal reporter activity;
  static structures do not establish an observed helix-flipping trajectory.
- PF01657 (former DUF26/Gnk2): six graphs retain fourteen OBSERVED effects,
  four DIRECT SPR responses and ten INDIRECT yeast/Fusarium phenotypes.
  Current PF01657 36-131 maps to mature 10-105 and includes all three tested
  binding residues; 4XRE exactly matches the mature reference plus extra Met.
  The twofold SPR dose discrepancy, residual R93A/delta-mnn2 responses and
  unavailable supplementary visual controls remain explicit. Yeast lag, two
  species-specific disc assays and liquid OD600 are separate contexts, not
  an observed binding-to-cell-death trajectory or family-wide lectin function.
- PF01641 (SelR): five graphs retain six OBSERVED effects, two DIRECT
  dabsyl-methionine product assays and four INDIRECT yeast-growth effects.
  Deposited 155-aa fly SelR exactly matches Q8INK9-2; canonical PF01641
  61-186 transfers to isoform19-133 through annotated deletions, not a new
  HMM analysis. Mouse U95C is not the native Sec enzyme. Zero, 2 and 0.5 mM
  peroxide contexts, MsrA-deletion backgrounds, residual double-mutant growth
  and later single-mutant convergence remain distinct. Uninspected later
  intermediate-trapping and zinc-mutant results are follow-up leads, not edges.
- PF01661 (Macro): five graphs retain eight OBSERVED effects, seven DIRECT and
  one UNRESOLVED. Intact Af1521 binding, D20A/N34A/Y176L affinity changes,
  coupled Appr1-phosphate processing, PARP1-conjugate retention and two distinct
  demodification assays remain separate. O28751/PDB2BFQ maps at PF01661 30-155;
  D20 and Y176 are outside that current interval. Jankevicius's GST assay leaves
  NAD unwashed; Rosenthal's common protocol removes it by G50. Missing construct
  termini, Af-specific dose/tag details, text/table stoichiometry disagreement,
  Figure6 panel-label swap and absent Af-specific product MS remain explicit.
  Human MacroD2 chemistry and cellular effects are not transferred to Af1521.
- PF01679 (Pmp3): twelve PHENOTYPIC graphs retain fifteen INDIRECT, OBSERVED
  effects for salt growth in three yeast backgrounds, sodium accumulation,
  methylammonium retention, toxic-cation growth, trk-background growth,
  divalent supplements and chromosomal plant RCI2A replacement. W303-1B
  X91499.1 exactly matches P87284, PF01679 5-52; the cited plant EST's computed
  reverse-strand ORF matches Q9ZNQ7, PF01679 6-52. Sodium protocol conflict,
  joint EGTA/calcium substitution, distinct normalization controls and partial
  hygromycin rescue remain explicit. No proton pore, direct voltage change,
  NSC1 blockade or plant-organism mechanism is adopted.
- PF01680 (SOR/SNZ, former UPF0019): eight MECHANISTIC graphs retain eleven
  DIRECT, OBSERVED effects for PdxS/PdxT reconstitution, external-ammonium
  substrate contexts, the K81-linked early adduct, partner H170N, spectral
  conversion and phosphate release. P37527 maps at PF01680 7-212; archived
  sequence version 2 differs only by the initial M, and the paper's K81
  peptide matches current residues 61-83. Untagged 2005 and tagged 2007
  preparations stay distinct. The 0.4-mM/0.4-uM dose and pH ambiguities,
  partial conversion and incomplete tag matching remain explicit. Later
  NMR qualifies the early-imine and nitrogen-free proposals; acid/urea Z2
  is not adopted as a native intermediate. Shared PF01174 experiments are
  not independent replications.
- PF01697 (GT92, former DUF23): eight graphs retain fifteen OBSERVED effects,
  ten DIRECT biochemical-preparation effects and five INDIRECT genotype
  effects. Whole GALT-1/O16374 maps at PF01697 189-394; the long historical
  NP_504545.2 reference matches, without proving every experimental clone.
  Raw Sf9 extracts support product formation and donor, acceptor and metal
  comparisons. Separate unc-119 and pmk-1 backgrounds retain developmental
  resistance, joint-construct rescue and a selected glycan-peak deficit.
  Unresolved assay units, minor UDP-Glc signal, qualitative MS conversion,
  marker co-rescue and incomplete opIs444 restoration remain explicit.
  The fut-8 lectin-staining experiment is not transferred to galt-1, and
  these contexts are not joined into an entirely observed molecular chain.
- PF01709 (TACO1/YebC, former DUF28): five graphs retain fourteen OBSERVED
  effects, four DIRECT biochemical-preparation effects and ten INDIRECT
  genotype/profiling effects. Mouse Q8K0Z7/NP_081622.1 maps at134-293;
  human Q9BSH4/NP_057444.2 at136-296. Mature mouse probeB binding and three
  grouped substitutions remain distinct from adult liver/heart COXI pulses,
  human KO/rescue COX1/COX3 products and proline-window footprint occupancies.
  Two binding-mutation groups are outside current PF01709. Tag handling,
  clone/lesion gaps, isotope/emetine/offset discrepancies, contextual PP
  negatives and incomplete three-Pro rescue are retained. Frozen mammalian
  transcription wording is qualified as translation evidence in the discussion,
  without editing the source snapshot or inventing an atomic elongation chain.
- PF01732 (MIP, former DUF31): four graphs retain twenty OBSERVED effects,
  eleven DIRECT purified-preparation effects and nine INDIRECT cellular effects.
  Exact GM12 ACU78687.1/UniParc UPI0001793D5F maps PF01732 at 290-776.
  Joint MIB-MIP cleavage of IgG/Fab/F(ab')2, MIB omission and published r-0582A
  effects remain separate from antigen-complex dissociation, whole-locus
  deletion and ATPase-partner perturbations. MIB alone and inactive-MIP joint
  mixtures dissociate complexes; cleavage is not a necessary release step.
  The 2016 S727A label conflicts with full-reference Y727/S759, and exact
  historical clones remain unresolved. Single-pair retention is not a rescue;
  ATPase K152A is compared in its shared G3S/K4R background. Protocol conflicts,
  inaccessible supplements and other-member coverage remain explicit, without
  claiming observed ATP hydrolysis, energy transfer or antibody-release/reset.
- PF01757 (Acyl_transf_3): five graphs retain twenty-two OBSERVED effects,
  sixteen DIRECT preparation effects and six INDIRECT cellular effects, plus
  two HYPOTHESIZED/UNRESOLVED acetyl-relay steps. Matched Q2FV54, USA300
  A0A0H2XFE4 and ABD21303.1 references map PF01757 at 19-344; S453, E357 and
  the isolated C-domain are outside this interval. Full-length glycan product,
  CoASH-release/substitution effects, cellular PG acetylation and conditional
  lysozyme/tunicamycin growth remain separate. Y136A increases CoASH release
  but lacks detected G5 acetylation. The deposited S453A search reference has
  extra K495A/K496A changes, and both treated and untreated samples contain
  acetylated Tyr206. These observations limit treatment-specific attribution;
  no normalized enrichment or exact biochemical-clone genotype is claimed.
  Acetyl-CoA-to-Tyr206 and Tyr206-to-Ser453 remain explicitly hypothetical.
  Assay/caption discrepancies, inaccessible SI and other members stay open.
- PF01795 (Methyltransf_5/RsmH): four graphs retain seventeen OBSERVED
  effects, five DIRECT reconstitution effects and twelve INDIRECT cellular
  modification, reporter and growth effects. P60390 matches NP_414624.1 and
  parental BW25113 WIA74303.1, with PF01795 at 5-310. RsmH's N4 mark remains
  distinct from RsmI's 2'-O mark. Joint enzyme/donor/substrate states, low
  RsmH-alone product and the half-dose naked-RNA comparator are explicit.
  UGA reduction follows Figure 4B and Results despite the opposite Discussion
  statement. Reporter ratios are not rate constants, and longer doubling time
  is not faster growth. Later Bacillus and O157:H7 studies remain follow-ups.
- PF01809 (YidD/former DUF37): nine PHENOTYPIC graphs retain twenty-one
  INDIRECT, OBSERVED effects. P0A8C8 equals YP_588472.1, PF01809 10-76;
  the GFP-H1 construct tests only residues 1-27, not the full domain.
  MC4100 processing/abundance, fusion localization and tagged induction
  are separate from BW25113 vesicle gradient proxies, enzyme readouts,
  protein abundance and protease protection. YidC compensation restores
  F0c protection but not NuoK protection. The submitted 2015 thesis is
  version-qualified; Lemo21/BL21 and Figure 6 E/F-versus-D/E discrepancies
  remain explicit. No purified YidD insertase, direct lipid binding or
  linear insertion-to-respiration-to-assembly mechanism is asserted.
- PF01827 (FTH/former DUF38): five PHENOTYPIC graphs retain eight
  INDIRECT, OBSERVED effects in FOG-2/FTR-1 reporter and C. elegans
  germline contexts. Historical AL110477.1 splice reconstruction exactly
  matches Q2YS43/CAJ43447.1, 327 aa, with current FTH at 144-271.
  Terminal truncations and the 254-327 chimera segment are not isolated
  domain experiments. Ordinal yeast output, RNAi gonad-arm counts,
  phenotype-selected q71 genotyping and partial TRA-2-tag suppression
  remain separate. Fog includes self-fertile animals in the sensitized cross;
  no FOG-2-loss increase in germline TRA-2 was detected by the inspected
  assay. No direct ubiquitination or translational-repression chain is claimed.
- PF01861 (BpsA_C/former DUF43): eight graphs retain sixteen OBSERVED
  effects, ten DIRECT and six INDIRECT, plus one UNRESOLVED HYPOTHESIZED
  carrier-transfer step. Q5JIZ3/BAD85880.1 and Q72L89/AAS80519.1 map at
  106-350 and 115-351 respectively. Exact deposits and mutant-primer
  translations retain tag, extra N-terminal residue and two-position acidic-
  site numbering discrepancies. Separate acceptor products, substitution
  effects, terminal peptide mass, historical-comparator kinetics and C9
  specificity do not prove the complete chemical relay. DBP1 pdaD relocation,
  partial chemical rescue, independent KPS replacement, different growth
  media and temporary cold-cycle compensation remain explicit. Incorrect
  image accessibility text does not override the inspected survival plot.
- PF01862 (PvlArgDC): one MECHANISTIC graph retains three DIRECT, OBSERVED
  preparation-level effects for Mj-PdaD CO2 output and E109Q/N47A activity
  decreases. A separate HYPOTHETICAL graph retains one UNRESOLVED processing
  contribution to N47A activity loss. Q57764 equals AAB98302.1, PF01862 19-162;
  published primer frames and 2QQC/2QQD establish native mutant numbering
  despite residual His0 and inconsistent PYR53 deposit representation.
  Specific activity is not intrinsic kcat, neither mutant is inactive, and
  mixed crystal states do not establish assay-solution fractions or relative
  maturation rates. Original processing protocols and Tk-PdaD growth contexts
  remain explicit primary-source follow-ups.

- PF01863 (YgjP-like/former DUF45): four graphs retain three DIRECT, OBSERVED
  preparation-level effects and two UNRESOLVED, HYPOTHESIZED latency edges.
  E. coli His6-YgjP UMP output is separate from archaeal proabylysin thermal
  deletion effects and distinct cis/trans tail models. P42597 reference maps
  at 94-149; Q9V1Y2 and Q57587 map at 2-88 and 7-95, excluding the implicated
  terminal segments. PDB4JIU establishes L2V despite the paper's K2V label;
  PDB4JIX confirms K2A plus residual GP. Missing YgjP clone/protocol details,
  different thermal-purification conditions, unsuccessful protease activation,
  B80 peptide-identification inconsistencies and computational-only candidates
  remain explicit. No whole-family protease activity is asserted.

- PF01864 (CarS-like/former DUF46): eight graphs retain nineteen DIRECT,
  OBSERVED preparation-level effects and two UNRESOLVED, HYPOTHESIZED steps.
  Q9YF05 equals BAA79391.1; PF01864 12-174 excludes D8/W9. Product, ion,
  temperature, ITC and lipid-strip assays remain separate. Each grouped mutation
  node denotes separately tested single variants. Q123A/H157A increase strip
  signal but lower product output; P31A retains product despite undetected ITC
  binding. Co-purified CTP, residual activity, endpoint-versus-rate limits and
  missing protocol details prevent stronger chemical claims. Proposed phosphate
  attack and TM5-mediated release remain hypotheses. AfCarS's accessible 2014
  author reproduction is a partially inspected follow-up, not a completed review.

- PF01865 (PhoU_div/former DUF47): eight PHENOTYPIC graphs retain seventeen
  INDIRECT, OBSERVED effects. Pap O30498 equals NP_384293.1 with PF01865 4-212;
  Newman PitR BAF66904.1 exactly matches UPI00000549A3 with PF01865 2-202.
  Native operon rescue, separately tested substitutions and heterologous
  expression remain distinct from PitR reporter and combined-genotype effects.
  Pap-only failure, downstream polarity, positive mutant residuals and altered
  protein bands prevent direct activation claims. PitR reporter changes are
  not uptake rates; exopolyphosphatase-treated lysate phosphate includes
  polyP-derived Pi. Supplementary tables establish the phoU::erm background.
  Other members, experimental contexts and direct molecular mechanisms remain
  follow-up; the 2017 Pap source is explicitly an MSc thesis.

- PF01867 (Cas_Cas1): eight graphs retain fourteen OBSERVED effects, nine
  DIRECT purified-assay effects and five INDIRECT cellular/lysate effects.
  Q46896 equals NP_417235.1 and PDB4P6I entity2; PF01867 131-226 includes
  tested active-site positions but excludes R245/R252/R256. Joint integration,
  Mn-specific partner enhancement, DNA-substrate perturbations and synthetic
  Y-DNA disintegration remain separate from cellular acquisition and co-IP.
  K224A loses cellular acquisition yet retains purified integration. Later IHF
  evidence bounds the older linear-target negative and event-order model.
  Predominantly half-site products are not completed chromosomal repair;
  the mismatched ED5 image prevents a target-rejoining visual-review claim.
  Remaining member and host-factor contexts are explicit follow-ups.

PF02621 (MqnD family) has a retained scientific review and native discussion,
but no graph. The inspected 2021 paper and supplement support reaction chemistry;
they do not resolve the tested B. halodurans clone to an exact accession or
sequence. Q9K9F8/BH2689 is explicitly a candidate, not an adopted experimental
identity. This is an identity prerequisite, not evidence of absent function.

PF20352 (DUF6647) also has a retained scientific review and native discussion,
but no graph. The inspected 2024 computational paper supports a relationship
to metallopeptidase families, not a directed biological effect or a substrate
reaction. Its Figure 11A caption says DUF4157, whereas the image and verified
A0A2Z2P7G5 mapping support DUF6647; this discrepancy is retained. Neither that
comparison nor a YbeY-like fold justifies importing RNA or protein cleavage.
The bounded source/member search is not an exhaustive claim of absent function.

PF01629 (DUF22) has a graphless scientific assessment and native discussion.
Q58031/MJ0614 reference identity is verified, but ATPase proximity and dUTPase
clan membership are not causal assays. The inspected 2009 primary abstract
assigns mutations to ATP synthase A/B, not an isolated DUF22 intervention.
Full-text access limits and the uninspected 2003 purification lead remain open;
plant DUF221/OSCA alias collisions are not transferred to archaeal PF01629.

PF01724 (DUF29) has a graphless scientific assessment and native discussion.
Q2RPE2 identity and the 3FCN structural sample mapping are verified. Selected
metagenomic thesis sections retain low-confidence ORF1 function predictions;
Figure 5.12 is a prediction workflow, not a biological causal graph. The separate
TC11pol polymerase experiments are not transferred to ORF1. Its exact modern
accession/taxon and additional member-specific experiments remain unresolved.

PF01868 (RNase_P-MRP_p29) adds seven MECHANISTIC graphs with twelve DIRECT,
OBSERVED preparation-level or composite-protocol effects: Mth fitted KM and
pH-normalized rate, Pfu NMR/ITC responses and separate two/four-RPP truncation
activities, and Pfu/Mja correct-cleavage fractions. Salt, RNA dose, time and
pH changes are retained in the intervention scope. Pfu Q8U007/NP_579545.1
matches2KI7 entity1, with PF01868 41-123; delta17/24/31 remove outside-match
residues. Mth O26119 maps6-88 and Mja Q57903/NP_247439.1 maps6-87. The
published Mth primer predicts terminal W rather than reference P93, so exact
canonical-WT clone identity remains unresolved. Residual activity, unchanged
pair kobs and incomplete yield prevent an invented binding-to-catalysis chain.
Eukaryotic RNaseP/MRP and further archaeal contexts remain open.

PF01870 (Hjc) adds nine graphs with sixteen OBSERVED effects: thirteen DIRECT
purified-preparation effects and three INDIRECT extract/cellular endpoints.
Pfu synthetic and RecA-generated junction processing, anti-Hjc depletion,
ligation-compatible ends, Mg dependence and binding competition remain separate.
SiRe mutation-dependent phosphorylation readouts, cleavage substitutions and
high-dose UV/cisplatin spot outgrowth do not form an observed repair pathway.
Pfu E7FHX4 matches BAA82839.1/WP_011012650.1, PF01870 1-97; SiRe F0NID3
matches WP_012711550.1, PF01870 4-134. T138 is outside the mapped domain.
Glu substitutions are not verified phosphoserine, and outgrowth is not direct
repair kinetics. Supplementary constructs/controls and Hje contexts remain open.

PF01871 (AMMECR1) adds six PHENOTYPIC graphs with nine INDIRECT, OBSERVED
effects: human G177D nuclear pattern, three dose-specific zebrafish heart-rate
perturbations, tail shortening and partial human-mRNA rescue, and three mouse
ESC transcript-marker responses. Human Q9Y4X0/NP_056180.1 maps132-301,
zebrafish Q6PH60/NP_956875.1 maps109-277, mouse Q9JHT5/NP_062369.1 maps143-312.
Nuclear retention, dose differences, E1I1 manuscript disagreement and unverified
rescue-insert sequence remain explicit. Marker changes do not establish lineage
conversion; SRRT antitermination is not assigned to AMMECR1 protein. Biochemical
function and additional member contexts remain open.

PF01875 (Memo) adds eleven graphs with sixteen OBSERVED effects: six DIRECT
purified-preparation readouts and ten INDIRECT cellular endpoints. Human
Q9Y316 sequence version1 equals NP_057039.1, PF01875 8-291; deposited7KQ8
is canonical4-297. Copper competition/protection, historical H192A luminol
response and iron-site substitutions remain distinct from wound closure,
MTT/probe signals, iron fractions, basal MDA, RSL3 response and chelator-induced
mitochondrial clustering. Conflicting redox interpretations, conditional metal
affinities, residual mutant signal and assay discrepancies remain explicit.
No isolated-domain reaction, intracellular metal flux or iron-to-ferroptosis
chain is asserted. Construct specificity and other family contexts remain open.

PF01876 (RNase P p30) adds fifteen graphs with twenty-four OBSERVED effects:
fifteen DIRECT preparation or mutation readouts and nine INDIRECT yeast effects.
Five exact reference sequences map the tested yeast and archaeal proteins;
whole proteins, protein pairs and catalytic RNA remain explicit. Reconstitution,
kinetics, fidelity, SPR, R107A and pair-dose effects are kept separate from
yeast growth and RNA-processing patterns. Mixed immunoprecipitates do not
establish isolated p30 catalysis or exclusively RNase P rather than RNase MRP.
Optimized buffer comparisons, residual mutant activity, partial product yield,
uninspected supplements and source discrepancies remain visible.

PF01877 (PAB1135/former DUF54) adds two MECHANISTIC graphs with three
DIRECT, OBSERVED effects. Q9UXX8 matches CAB50635.1 and WP_010868849.1,
with PF01877 at 9-132; the trypsin-treated preparation's exact termini remain
unknown. Protein-dose and matched-dose RNA-probe comparisons retain the
bound/free denominator, weak nonzero comparison-probe binding and coupled
sequence/structure changes. These are three views of one experiment, not
independent replications. No KD, dimer necessity, individual residue effect,
RNase P/exosome reaction or family-wide RNA-binding function is asserted.

PF01878 (EVE/former DUF55) adds nine PHENOTYPIC graphs with seventeen
INDIRECT, OBSERVED effects: eight WEHI-231 Thy28-V5 cellular readouts and
nine DT40 knockdown, rescue, ChIP and partner-perturbation effects. Mouse
Q91YJ3/BAC21100.1/NP_653126.1 maps56-219; chicken Q90679/AAA75591.1
maps73-235, but NP_989618.2 differs at51 outside EVE. Exact experimental
insert sequences remain unresolved. Mammalian Pax5 negatives restrict transfer;
parallel cellular readouts are not an observed JNK/ROS/caspase or transcriptional
relay. No domain/residue-specific biochemical mechanism is claimed. VcaM4I's
structural EVE label remains an exact-member/Pfam mapping question.

PF01881 (Cas6 C-terminal/former DUF57) adds eight graphs: sixteen direct,
observed purified-assay effects and one unresolved, explicitly hypothetical
wraparound-alignment step. Q8U1S4 equals AAL81255.1/WP_011012271.1;
PF01881 maps121-237, while the N-terminal PF21350 maps17-117. The joint
G223A/G225A/G231A/G233A mutant is one C-domain intervention, not four
individual residue tests; Y31/H46/K52 are outside PF01881. RNA sequence,
linker length, probe protection and conditional cleavage-site shifts remain
separate contexts. Residual binding/activity, tolerated linker edits and the
75 versus0.75 mM DTT discrepancy are retained. No isolated-domain sufficiency,
observed full RNA path, final maturation or universal antiviral mechanism is
claimed.

PF01886 (DUF61/UPF0216) retains a graphless scientific assessment and two
open discussions. SSO0941/Q97ZH2 equals AAK41217.1/WP_009992374.1 over138
residues; PF01886 maps4-123, while 5VFK contains the complete reference plus
LEHHHHHH. The inspected Zhou2018 abstract/deposition and Wang2024
computational benchmark do not establish a directed biological edge. Operon
proximity, fold similarity and energy/force performance are not promoted to
RNA-processing causality. Full2018 text/supplements and broader member-specific
functional evidence remain incomplete; an access failure is not a negative assay.

PF01889 (archaeal AliA/AliB, former DUF63) retains nine PHENOTYPIC graphs
with 34 INDIRECT, OBSERVED edges. AliA D4GXF7/ADE04977.2 maps87-379;
AliB D4GUE1/ADE03618.1/WP_004042703.1 maps17-263. DS2 reference sequences
are distinguished from experimental H53 derivatives and pneumococcal PF00496
namesakes. Tagged processing, phase partitioning, processed lipid recovery,
two growth media, cell shape, soft-agar halos, endogenous proteomics and
cell fractions remain separate contexts. AliB residual processing/growth,
nonsignificant lipid/global-proteome comparisons and tagged/endogenous HVO_1176
disagreement are retained. The2026 lipid deposit reuses2025 WT/double-mutant
controls; these are not independent replications. Whole-gene effects do not
establish purified catalysis, an AliB peptidase reaction, conserved-residue
chemistry or a serial lipidation-to-motility pathway.

PF01894 (YjbQ, historical UPF0047) retains three PHENOTYPIC graphs with five
INDIRECT, OBSERVED growth-rescue effects. P0AF48/NP_418480.1 reference138 aa
maps PF01894 at6-138; experimental clone sequences remain unverified. MC1061
delta-thiE rescue is separate from JU283 delta-pdxB growth on unsupplemented,
mixed-supplement and serine-only plates and qualitative liquid rescue. The
recovered original2010 supplement confirms lineage, tags and plate conditions,
but printed start-region primers and FigureS1 antibiotics conflict. YjbQ was
insoluble and unassayed for4PE dehydrogenase, not a measured enzyme-negative.
Ordinal colony timing is not catalytic activity; FigureS4 is not a YjbQ curve.
No identified OHPB-producing step or native physiological substrate is claimed.

PF01895 (PhoU/former DUF65) adds twelve graphs with24 OBSERVED effects:
four DIRECT purified-system readouts and20 INDIRECT cellular outcomes.
P0A9K7/NP_418180.1 reference241 aa maps26-112 and129-212; mycobacterial
PhoU1 A0R4B7 maps18-103/122-204 and PhoU2 A0QSU6 maps17-103/123-204.
All are whole proteins with two repeats. E. coli uptake, engineered-probe
fluorescence, integrant AP, membrane fractions, joint reconstitution, yield
and BACTH remain separate assays. Unequal probe masses, plasmid-versus-
integrant effects and the2015 medium discrepancy are retained. Figure5B
does not test R148E with PstB. Mycobacterial high-Pi reporter effects remain
separate from purified PhoU1/Pi-dependent net RegX3 phosphorylation. The latter
does not reduce SenX3 autophosphorylation or establish isolated PhoU catalysis,
Pi occupancy, a binding-site residue or an individual phosphatase rate.
PF01865/PitR and other species' PhoU proteins are not silently merged.

PF01899 (MNHE/MrpE, former DUF68) adds nine PHENOTYPIC graphs with twelve
INDIRECT, OBSERVED effects. OF4 Q9RGZ1 equals the experimental parent deposition
ABS70477.1 over158 aa, with PF01899 at8-156. B. subtilis deletion and His6
complementation retain distinct salt conditions; the current Q7WY60 sequence
revision is not silently assigned to the historical UOT1285-derived inserts.
OF4 deletion, T113A transport loss, E/F/G membrane signals, full-complex bands,
P114G response/apparent Km, and T113Y transport/growth are separate endpoints.
P114A tolerance, residual deletion activity, pH-dependent T113Y loss, conflicting
P114G growth claims and discrepant reused2008/2010 values remain visible.
Apparent Km is not Kd, and no observation proves isolated MrpE ion binding or
E-G-to-A-D conformational activation. The newer two-TM/cytoplasmic fold supersedes
the old predicted cartoon; L41W's retained dimer/growth and7QRU's distinct sequence
are retained as limits rather than invented causal steps.

PF01900 (Rpp14/Pop5, former DUF69) adds nineteen graphs with35 OBSERVED
edges:3 DIRECT,14 UNRESOLVED and18 INDIRECT. Six reference proteins map to
versioned NCBI sequences and current domain intervals. Archaeal joint-protein
and ionic protocols, apparent SPR affinity and pair-dose cleavage are distinct
from human fraction/preparation assays, RNAi, Cas9 populations and two separate
upstream-knockout rescue backgrounds. Figure4C does not support increased
40-minute mononucleotides after human Pop5 addition. Residual knockdown,
unverified transgene sequences, incomplete purity, gradient/replicate discrepancies
and missing historical mutation methods remain explicit. RNA abundance is not
a direct catalytic rate or measured stability mechanism. These are seventeen
PHENOTYPIC and two MECHANISTIC graphs, not a universal family mechanism.

PF01901 (O_anti_polymase, former DUF70) has seven PHENOTYPIC graphs with
eight OBSERVED, INDIRECT effects. Four ATCC43895 insertion contrasts retain
lower tube staining, long-O-antigen LPS signal, microtiter staining and motility
halo, with residual and negative findings explicit. Three SK2526 readouts retain
lower surface-coat, LPS and capsular-fraction signals. A separate ATCC43888
complementation contrast retains increased phage spot clearing, not direct
binding or measured infection efficiency. These are not interchangeable alleles
or one universally rescued pathway. ATCC establishes700927 as derived from43895;
the catalog relationship is resolved, not the actual historical assay sequence.
ATCC43888 QDZ55367.1 exactly matches Q8X4T7. The partial PF01901 hit8-205 of394
residues, score0.041, remains insufficient for domain-specific chemistry.
Temperature/species wording, figure-panel labels and earlier glucose/duration
conflicts remain explicit. O86purified Wzy(PF14296) and serotyping associations
are excluded; inaccessible sources are not negative results.

PF01902 (Diphthami_syn_2_N, former DUF71) has nine graphs retaining twelve
OBSERVED effects and two HYPOTHESIZED chemical steps. Purified whole-protein
reporter controls and an AMP-assigned spot are four DIRECT outputs, not direct
intermediate detection. Yeast and human-in-yeast complementation, deletion
reporters, distal-construct drug responses and conditional growth are eight
INDIRECT effects in separate contexts. The proposed adenylation/ammonia-attack
sequence remains UNRESOLVED and CONTEXTUAL. Current Q12429/NP_013244.1 maps
PF01902 to 1-135 and PF28410 to 171-231; G216N/E220A is a combined perturbation
in PF28410, not two individual PF01902 residue tests. Q7L8W6/NP_542381.1 maps
PF01902 to 1-136. Reference identity does not verify historical clone sequences
or isolated-domain sufficiency. Reporter-name, length and growth-wording
conflicts, unavailable supplements and unassessed members remain explicit.

PF01904 (DUF72) has two graphs with 21 OBSERVED, INDIRECT experimental growth
effects and two HYPOTHESIZED, UNRESOLVED computational cleavage steps. Each
YecE/partner joint deletion is compared with multiplicative single-mutant
expected fitness, not WT or addition of one deletion. Sixteen scores aggravate
and five alleviate; positive scores are not WT rescue or absolute growth gains.
Reference P37348/NP_416382.1 maps PF01904 at 3-258. Tm1631 Q9X1W6/AAD36698.1
maps at 3-259, and the supplement explicitly maps model Lys73 to native K72.
The proposed pentacovalent state and P-O3' cleavage remain model-only chemistry,
not experimental nuclease activity, trapped intermediates or measured kinetics.
The Hfr/Keio-derived screen and preorganized Tm1631-DNA/two-Mg model remain
separate biological contexts with explicit clone, assay and model limitations.

PF01905 (former DUF73, DevR/Csa2) has eleven graphs with fourteen OBSERVED,
EXPERIMENTAL edges: six DIRECT binding effects and eight INDIRECT cellular
effects. Csa2 Q97Y91/AAK41675.1 maps PF01905 at 5-273; DevR
Q07765/AAA16134.1 maps only 19-176 within 302 aa, provider score 0.00022.
Neither whole-protein assay nor whole-gene deletion isolates domain function.
Csa2-alone and complex gel shifts, guide/target-strand comparisons and H160A
residual binding remain separate from the room-temperature P1 spacer-26
anisotropy assay. DevR deletion affects mature-spore CFU, cell shape,
fruiting-body darkening and dev RNA abundance at different timepoints.
Promoter/devI deletions suppress developmental effects without restoring DevR;
they are not DevR complementation. RNA abundance does not demonstrate direct
repression, and the 2017 DevTRS/antisense model remains unproven context.

PF01906 (former DUF74, YbjQ_1) retains one PHENOTYPIC graph with ten
OBSERVED, INDIRECT, EXPERIMENTAL joint-deletion growth effects: six above and
four below the multiplicative single-mutant expectation. These are not WT
comparisons, isolated deletion effects or gene-to-gene molecular interactions.
P0A8C1/NP_415387.1/AAC73953.1 map PF01906 at 1-105 of 107 aa; reference
equality does not sequence the historical Keio-derived clone. Three OPEN
discussions retain assay/member gaps, fusion constructs, metal-binding and
retron leads, and Rv1762c revision/nonsignificance. The latter's removed
uncomplemented phenotype and published pooled adjusted p=1 do not establish
oxidative protection. Static pentamers and ongoing metal assays are not
observed biochemical steps. YbjQ is not YjbQ/b4056/PF01894.

PF01909 (former DUF76, NTP_transf_2) retains three MECHANISTIC graphs with
eleven DIRECT, OBSERVED biochemical effects in E. coli GlnD. Transfer assays
distinguish full-length, 1-371, deltaNT and individual G93L/G93V/G94D variants;
G94L is a retained-activity exception. P27249 sequence version 2 maps PF01909
at 85-144, not the complete active 1-371 fragment. Separate H514/D515 removal
controls map to the HD domain outside PF01909. Glutamine effects are scoped
to Mg-only assays; Mg/Mn net endpoints can instead reflect competing removal.
Current P05057 annotations do not return a PF01909 match, so related-fold
ANT(4') chemistry is not imported despite the frozen description's example.
Two OPEN discussions retain mapping, construct and other NTase-branch gaps.

PF01910 (former DUF77, Thiamine_BP) retains twelve graphs and twenty-four
OBSERVED effects. Two DIRECT binding edges concern purified TM0486; the
remaining twenty-two are INDIRECT production, RNA or phenotype effects.
Q9WYV6/AAD35571.1 maps PF01910 at 6-93. Fungal H99 ECM15
J9VTN7/AFR95954.1/XP_012050770.1 maps at 9-102, with the displayed
supplement sequence checked; Sc P35195 maps at 8-98 but the BY4741 assay
clone remains qualified. Bacterial binding is not transferred to fungal
ligand chemistry. Fluorescence is not direct Cac2 transport, pigmentation
is not direct laccase activity, and steady-state RNA is not transcription
rate. Mouse experiments retain separate comparators and inocula. The
supplement's conflicting cross-rescue genotype/YP617 and suspicious printed
assay units remain open rather than silently corrected. Four evidence
ledgers and two OPEN discussions preserve these limits and remaining members.

PF01914 (former UPF0056, MarC) retains thirteen PHENOTYPIC graphs and
thirty-nine OBSERVED, INDIRECT cellular effects from six primary studies.
Exact KS-1 SnatA BAC53669.1/UPI0000062A6D maps at 9-214; retirement of
Q8J305 is not biological absence. SnatA construct uptake, upstream-region
effects, energetic perturbations, competition and WAT9 growth are separate
contexts. K-12 MarC P0AEY1 maps at 5-217 and YchE P25743 at 9-210.
MarC threonine edges name whole selected clones, including B2059 passengers;
YchE growth rescue is not a significant uptake result in the different host.
The 2011 reconstruction retains its EcHW24/EcNR1 MutS-background ambiguity.
The 2020 M35stop comparison is not wild-type rescue. ATCC25922 MarC
AIL17056.1/UPI00000DEBB0 differs by N36S from K-12; primer mapping supports
the full validation insert but leaves the enrichment interval unresolved.
Its five small TOP10 MIC shifts are not clinical resistance or direct efflux,
and the 2008 negative susceptibility context remains visible. Antibiotic
exposure increases steady-state RNA, not proven direct transcription.
Eight current ledgers and two OPEN discussions retain these limits and other
members. A ninth, superseded extract is preserved with the earlier review;
the successor corrects the YchE Figure 1C label to p=0.38 without changing
the nonsignificant result or any graph direction.

PF01918 (Alba, former DUF78) retains sixteen graphs with fifty-three
OBSERVED effects: forty-six DIRECT biochemical/physical readouts in fourteen
MECHANISTIC graphs, and seven INDIRECT transcription/growth effects in two
PHENOTYPIC graphs. Sso Alba DNA binding, Pat acetylation, architecture and
stiffness remain separate from transcription. Sis10b RNA binding, unwinding,
strand exchange and growth complementation are not joined into an observed
intracellular pathway. Human Rpp25-Rpp20 assembly/P3 binding does not establish
RNase catalysis; Rpp20 is PF12328, not another PF01918 member. PfAlba3 binding,
plasmid/abasic-probe cleavage, mixed K23/K32 acetylation, acetyl-specific
immunoblot changes and synthetic-peptide deacetylation retain their own
constructs and protocols. Current mappings are P60849/F0NHH1 at10-72,
Q97ZF4 at6-69, Q9BUL9 at37-100 and Q8IJX8 at14-83; none establishes a
minimal isolated-Pfam-domain assay. Cao2018 abstract-level counterevidence
challenges native archaeal K16 acetylation without erasing Marsh2005's
in-vitro reaction. Residual mutant activity, cross-panel plasmid comparison,
the printed500mM NAD unit, historical initiation/tags and uncurated member
branches remain explicit in eleven evidence ledgers and two OPEN discussions.

PF01923 (Cob_adeno_trans, former DUF80) adds twenty-seven graphs with
seventy-seven OBSERVED effects: fifty-six DIRECT biochemical/physical
readouts and twenty-one INDIRECT complementation/growth effects. Eighteen
MECHANISTIC and nine PHENOTYPIC contexts separate Salmonella PduO,
L. reuteri PduO, Salmonella and Listeria EutT, and human MMAB. Cofactors,
reduction systems, truncations, metalation, inhibitors and strain backgrounds
remain explicit. SeEutT H67/C79/C80/C83 and LrPduO F187/tail183-188 are
outside the mapped Pfam intervals. LmEutT accepts cob(I)inamide but not
cob(II)inamide in the tested biological reducing systems; transition-metal
independence does not exclude MgATP. Human FDX1-supported synthesis,
ATP-EPR complexes and ADP-R190H redox titrations are separate experiments.
Ten ledgers and two OPEN discussions retain source discrepancies, negative
results, unresolved constructs and uncurated transfer/repair contexts.

PF01925 (TauE, former DUF81) adds nine graphs and thirty-seven edges:
thirty-six OBSERVED/INDIRECT cellular effects in eight PHENOTYPIC contexts
and one HYPOTHESIZED/UNRESOLVED CysZ uptake proposal. C. glutamicum CysZ
growth, Serratia PmpC normalized pigment output and AMB-1 MamO processing
and magnetic-response assays remain separate. Exact reference mappings place
PF01925 at Q8NLX4 residues 7-246, E7BBJ3 residues 5-260 and Q2W8Q2
residues 357-633. MamO substitutions tested here are outside that interval;
LimO-positive rescue is not transferred to the delta-R9 background. No
direct transport, substrate identity or isolated-domain sufficiency is
established. Seven ledgers and two OPEN discussions retain conditional
negative results, source/construct discrepancies and uncurated contexts.

PF01927 (Mut7-C, former DUF82) adds fourteen graphs and twenty-four
OBSERVED edges: nineteen DIRECT biochemical/physical effects, three INDIRECT
cellular effects and two coexpression-recovery effects with UNRESOLVED
directness. Eleven MECHANISTIC and three PHENOTYPIC contexts separate worm
MUT-7/human EXD3 binding and cleavage, joint complex capture, crowded-mixture
droplets, RNAi hatching and tagged germline localization. Current matches
P34607 666-779 and Q8N9H8 631-734 are narrower than the experimental CTDs.
The tested catalytic/interface substitutions lie outside these intervals.
Affinity labels, allele numbering, full-length clone assignments, tags and
imaging reagent identity retain explicit conflicts or limits. Four ledgers
and two OPEN discussions preserve conditional negatives and member gaps;
no isolated-domain nuclease, MUT-8 activation, direct MUT-7/MUT-16 contact,
all-foci dissolution or observed native RNA-processing pathway is asserted.

PF01930 (Cas_Cas4, former DUF83) adds thirteen graphs and seventeen OBSERVED
effects: eleven DIRECT, four UNRESOLVED and two INDIRECT. Ten MECHANISTIC and
three PHENOTYPIC contexts keep Pcal_0546 DNA processing and residue/cluster
effects separate from Gsu fusion/Cas2 assembly, ExoI-assisted processing,
integration and surrogate-cell acquisition. A3MTK6 maps57-210 of213aa;
Q74H36 maps15-197 of559aa and also contains Cas1. Historical SSO0001 DUF83
wording is not current PF01930 mapping. Pcal metal assignment, Gsu vector
names and the ED4g cellular-PAM-switch contradiction remain unresolved.
Four ledgers and two OPEN discussions retain member and native-function gaps.

PF01931 (NTPase_I-T, former DUF84) adds eight graphs and twenty OBSERVED
effects: eight DIRECT, nine INDIRECT and three UNRESOLVED. Two MECHANISTIC
contexts retain YjjX phosphate release and reaction inhibition; six PHENOTYPIC
contexts retain human PRRC1 coat signals, RUSH transport, distinct ATRAP/ATG9A
localization, mixed-assay cargo packaging and LC3 morphology. P39411 maps4-168
of170aa; Q96M27 maps260-376 of445aa. Whole-protein effects do not establish
isolated-domain function or a shared bacterial/mammalian mechanism. Five
ledgers and two OPEN discussions retain source conflicts, missing supplementary
methods and additional developmental, domain-specific and member contexts.

PF01933 (CofD) adds seven graphs with ten OBSERVED effects: four DIRECT,
three INDIRECT and three UNRESOLVED. Paired cofactor reactions, cellular
fbiA deletion, relative product fractions, GlmS regulation, transformation
frequency and mixed-particle scattering remain distinct. P9WP81 maps3-294,
A0QTG2 maps3-291, O06974 maps7-292 and Q58653 maps5-275. The source-labeled
GlmR R301 lies outside the current match; conflicting Methods numbering,
synthetic clone identities and missing supplements remain explicit. Six
ledgers and two OPEN discussions retain further CofD, uridyltransferase,
modification and member-specific contexts.

PF01934 (HepT-like, former DUF86) adds sixteen graphs with twenty-eight
OBSERVED effects: four DIRECT, fifteen INDIRECT and nine UNRESOLVED.
SO_3166 host-specific CFU, substitutions, purified RNA cleavage and MntA
AMP-transfer assays remain separate from heterologous Thermococcus effects
and the SO_1440 fusion. The fusion's WP_164925653.1 reference has276 residues;
its positions26-276 exactly match Q8EGZ7 positions2-252. Current PF01934
Q8EGZ7 144-234 projects to WP168-258. Source C163/C270 flank that core,
so their redox-conditioned effects are not isolated Pfam-core functions.
Six ledgers and two OPEN discussions retain source discrepancies, qualified
preparation effects, missing cyanobacterial full text and remaining member
contexts. Legionella Q5ZRG2 evidence belongs to PF08780 and is excluded.

PF01935 (DUF87/HerA) adds six graphs with twenty-one OBSERVED effects:
one DIRECT, two INDIRECT and eighteen UNRESOLVED. SSO2251 phosphate release,
short-duplex unwinding, triplex displacement and joint HerA/NurA degradation
remain separate from E233S deletion rescue and overhang-product comparisons.
Q97WG8v1 and F0NFK8v1 both map PF01935 at121-331; several tested residues
lie outside that interval. D471A's increased ATP turnover and nondecreased
short-duplex unwinding are not collapsed into its reduced DNA-processing
readouts. Four ledgers and two OPEN discussions retain source discrepancies,
unresolved atomic coupling and bacterial, antiviral and further archaeal work.

PF01936 (NYN/former DUF88) adds eight graphs with twenty-two OBSERVED effects:
two DIRECT, two INDIRECT and eighteen UNRESOLVED. Human purified238-510,
full-protein and N-terminal tethering, and protected-poly(A) reporters remain
separate from mouse multidomain cleavage, truncation, oocyte resupply and
knockin phenotypes. Human Q9Y4F3v6 maps353-490; mouse Q8BJ34v3 maps352-489.
PDB5YAA reconciles source D272 with canonical D451 locally, not by assuming
a global isoform offset. N4BP1/KHNYN PF11977 and Rae1/YacP PF05991 are
excluded transfers. Four ledgers and two OPEN discussions retain native-target,
whole-construct, later-study and nonmammalian coverage limits.

PF01938 (TRAM/former DUF90) adds ten graphs with thirty-two OBSERVED effects:
six DIRECT, five INDIRECT and twenty-one UNRESOLVED. MMP0076/Q6M142v1
maps PF01938 at13-67. RNA complex formation, DNA-beacon fluorescence,
native growth, RL211 reporter growth, UTR-mCherry fluorescence and BX04
cold rescue retain their distinct conditions. I33A abundance/host effects,
K62A partial rescue and induction-dependent R15 results remain explicit.
Four ledgers and two OPEN discussions preserve construct/source discrepancies,
native RNA-mechanism gaps and other archaeal/multidomain member coverage.

PF01939 (NucS_C/former DUF91) adds nine graphs with thirty-three OBSERVED
effects: fifteen DIRECT, seven INDIRECT and eleven UNRESOLVED. The three
reference proteins retain current PF01939/PF21003 boundaries. Pab N-terminal
substitutions, the Tko tail outside PF01939, and the distinct Cgl five-/two-residue
truncations are not treated as interchangeable domain experiments. Low- and
high-concentration cleavage, native mutation frequency and mutation rate remain
separate contexts. Six ledgers and two OPEN discussions preserve the same-strain
three-/five-nucleotide product discrepancy and unfinished native repair coverage.

PF01940 (DUF92) adds thirteen graphs with thirty-two OBSERVED effects and one
HYPOTHESIZED toxicity step: three DIRECT, eighteen INDIRECT and twelve
UNRESOLVED edges. VTE6 crude-extract reactions, plant lipid/growth phenotypes,
AtPGR glucose responses, bHLH34 regulation, mouse TMEM19 probe labeling,
human MPC transcript effects and mouse retinal outcomes remain separate.
Current PF01940 mappings are VTE6 97-316, PGR 15-276 and human/mouse TMEM19
60-321. Six ledgers and two OPEN discussions retain incomplete suppression,
NS control contrasts, fixed-eye assignment and remaining member/source gaps.

PF01941 (AdoMet_Synthase/former DUF93) adds eight graphs with twelve OBSERVED
effects: seven DIRECT preparation-level relations and five UNRESOLVED
perturbation effects. TkMAT SAM production, MjMAT urea and double-mutant
assays, engineered L147A/I351A surrogate-product assays and Ecm1/MTAN cap
cascades remain separate. Current PF01941 intervals are Q5JF22 6-401 and
Q58605 2-402. Five ledgers and two OPEN discussions preserve the TkMAT
gene-length discrepancy, later sequence-accession errors, the surrogate
endpoint-versus-kinetics distinction and incomplete member coverage.

PF01944 (SpoIIM/former DUF95) adds eight PHENOTYPIC graphs with ten OBSERVED,
UNRESOLVED effects. PspoIID and native-promoter reporters, protein abundance,
septal targeting and I92T suppression in the GFP-SpoIIP S108G background
remain separate. Reference P37873 maps PF01944 25-203; experiments use PY79
derivatives rather than silently relabeled strain 168. Five ledgers and two
OPEN discussions retain source-label conflicts, uninspected figures, candidate
Q18B81 mapping and bacteriocin/archaeal follow-ups. SpoIIM hydrolase activity
and a direct binding interface are not established by these observations.

PF01947 (Rv2949c-like/former DUF98) adds nine graphs with fourteen OBSERVED
effects: five DIRECT product-conversion edges and nine with UNRESOLVED molecular
directness. Three MECHANISTIC graphs cover two Rv2949c preparations and Sll1797
chemistry; six PHENOTYPIC graphs separate product inhibition, host complementation,
native growth/rescue, PQ, oxygen and independent markerless-deletion contexts.
P9WIC5 maps24-173 and P73322 maps2-130; E. coli UbiC/P26602 maps PF04345,
not this family. Source-panel, unit, clone and assay-control limits remain open.

PF01949 (Endo_dU/former DUF99) adds twelve graphs with nineteen OBSERVED
effects: seven DIRECT cleavage-product edges and twelve UNRESOLVED assay or
cellular effects. Five tested homologs remain separate; Afu/Halo dsDNA assays
are distinct from ssDNA assays and H. volcanii physiology. The supplement
was retrieved and inspected, preserving Figure7E H166R versus Results/S11
H166A, partial deletion, relative TPM and late optical-density qualifications.
Current Halo/Gm Pfam boundaries and historical constructs remain unresolved.
Five ledgers and three OPEN discussions retain evidence and coverage limits.

PF01950 (FBPase_3/former DUF100) adds five graphs with eight OBSERVED effects:
one DIRECT purified-protein F6P product edge and seven UNRESOLVED cellular
effects in KOD1-derived strains. Synthetic-medium growth is separate from
rich-medium extracts, and carbon-regimen effects on RNA and activity do not
form an observed mediation chain. Later bifunctionality prevents assigning
the deletion phenotype solely to phosphatase activity. Six ledgers and three
OPEN discussions retain primary-method, rescue and member-coverage follow-ups.

PF01951 (Archease/former DUF101) now has forty-two graphs with ninety
OBSERVED effects: thirty-eight DIRECT biochemical effects and fifty-two
UNRESOLVED mutant, preparation or cellular effects. Human RTCB activation and XBP1 ligation are separate from
P. horikoshii RNA-ppG formation and purine-cofactor assays. Paper human
D51/K156 map to Q8IWT0 D39/K144, not the current sequence positions51/156.
U2OS day3 RNA ratios and stress outputs remain distinct from the qualitative
day8 mature-tRNA reduction. The follow-up adds eleven cofactor-specific
Archease-mutant effects and six selective RtcB-rescue outputs, without confusing
partner mutations with Archease residues. Nine PAB1946 effects retain separate
tRNA selectivity, poly(C), RNA affinity and aggregation contexts. Species-level
P. abyssi grounding avoids assigning an unconfirmed assay strain. Bacterial
turnover and small Thermobifida short-assay changes are now retained separately.
Human complex activation/restart/dose/cofactor assays remain distinct from
HeLa depletion/rescue and tagged yeast-tRNA accumulation in a human host.
DDX1 partner effects remain separate from Archease mutations, including
RNA-binding and codepletion controls and conflicting kinetic/residue labels.
Jurkin extract XBP1, single-Archease protein response, joint-depletion outputs
and endogenous tRNA abundance retain distinct assays. The nonsignificant
single-Archease RNA trend is ledger-only; no RTCB-only mouse phenotype is
transferred to Archease. S1D preparation ambiguity remains explicit.
Seventeen ledgers and five OPEN discussions preserve source discrepancies,
unresolved bacterial clones and human construct N termini, uninspected Auxilien
figures, mutant-folding limits and remaining biochemical/cellular/member work.

PF01954 (AF2212-like/former DUF104/UPF0165) retains a graphless scientific
assessment, five evidence ledgers and three OPEN discussions. Comparative
prediction, an AbrB-related alignment and the tagged 2NWT NMR structure do not
establish toxin neutralization. Current InterPro maps O28071 to 1-34 while the
older RCSB Pfam annotation maps 1-57; construct, source-strain and salt metadata
limits remain explicit. The inspected 2025 Thermococcus cassette antitoxins
map to other Pfam families, so their growth effects are not transferred here.

PF01955 (CbiZ/former DUF105) retains twenty graphs and sixty-six edges:
sixty-five OBSERVED and one cross-figure INFERRED, eleven DIRECT purified-enzyme
substrate conversions and fifty-five UNRESOLVED assay or phenotype effects.
The prior sixteen graphs and forty-three edges remain unchanged.
Thirteen earlier Rhodobacter additions cover four substrates, five
condition comparisons, two acetate-growth effects and two separate cellular
corrinoid-fraction effects. Q8Q0G3 maps15-198; Q9HPK9 maps14-208; Q8TUT1 has
PF01955 8-205 and PF04608 257-353; Q3J3R7/RSP_2406 maps PF01955 6-208.
Cyano-HPLC and ligand-free MALDI are not intact AdoCby measurements; joint
rescue is not independent sufficiency. C-terminal phosphatase results remain
domain-attribution controls, not PF01955 causal edges. Five newer native-salvage
edges separate conditional partner requirements, cross-figure CbiZ dependence
and joint Cby/CobY bypass. The newest twenty-three edges cover seven alternative
2008 donor rescue arms, seven AP comparisons, six12h induction effects and three
mixed-extract products. Seventeen evidence ledgers
and six OPEN discussions retain primer, clone, unit, genotype, native-role,
bacterial remodeling and other-member limits. Rhodobacter's retained MBP/His6
tags, buffer/pH confounding, source-caption discrepancy and inaccessible
remodeling supplements remain explicit; no complete native remodeling chain is
claimed. Native-salvage TableS1 text supports a predicted 41-residue deletion
product but not the actual historical clone. Printed endpoint, retained-length,
vector-strain and tetracycline-unit discrepancies remain visible.
The2008 donor constructs are distinguished from current candidate accessions;
historical insert/strain tables remain uninspected. The whole BtuD-CbiZ fusion
does not isolate domain catalysis, and the later-deposited Ferroplasma accession
does not by itself identify the2008 clone. LowCNCbl activity in mixed extract
and the2009 purified negative remain distinct observations. Reporter wording,
antibiotic units and product-trace access limits remain explicit.

PF01956 (EMC3_TMCO1/former DUF106) now has fourteen graphs with 43 OBSERVED,
EXPERIMENTAL effects. Two DIRECT edges concern insertion by purified assembled
human EMC, not EMC3 alone. The original twenty-seven UNRESOLVED effects retain protease
pretreatment, human tagged exogenous EMC3 variants and distinct yeast deletion/
K26L growth and reporter contexts. R31K improves the SQS comparison but not
OPRK1; the four-methionine mutant is not four independent perturbations.
Human Q9P0I2 v3 maps 5-191, yeast P36039 v3 maps 2-197, and the outside-domain
second methionine loop's negative assay remains separate. Hxt3 RNA decline,
BY4741/W303-1a differences, assembly controls and protocol/construct limits are
explicit. Seven additional PHENOTYPIC graphs add fourteen UNRESOLVED effects:
endogenous EAAT1 abundance in TMCO1-containing knockout genotypes, separate
TMCO1/OPTI partner dependencies, microsomal YIPF1 glycosylation and protection,
cellular YIPF1 glycosylation and three fluorescent client ratios. Different tags,
single versus joint genotypes and siRNA timing remain distinct. Current human
TMCO1 Q9UM00 maps PF01956 59-216 of 239 residues; the shorter Q9UM00-1 lacks
canonical 1-51 but historical clones remain unverified. Seven ledgers and three
OPEN discussions retain inaccessible channel experiments, archaeal Ylp1, further
EMC/TMCO1 contexts, source-data/gating issues and exact historical mapping.

PF01957 (NfeD) adds three PHENOTYPIC graphs with four OBSERVED, EXPERIMENTAL,
UNRESOLVED effects. E. coli YbbJ coexpression enhances QmcA-assisted plate and
liquid growth in a sensitized ftsH/htpX/sfhC21 background. Bacillus YqeZ-containing
operon deletion and complementation are separate contexts, not isolated-domain
activity or a matched deletion/rescue pair. Current P0AAS3 maps 94-148 and
P54465 maps 382-435; historical clones remain unverified. Bacillus NfeD2/YuaF
maps instead to PF31148/PF25842, and PH1510's C-terminal PF01957 does not
identify its N-terminal protease activity. Five ledgers and two OPEN discussions
retain those exclusions, source-panel inconsistencies and missing original figures.

PF01958 (Asp_DH_C) adds five graphs with six OBSERVED, EXPERIMENTAL, DIRECT
TM1643 redox/inhibition effects, one contextual INFERRED immediate product and
one contextual HYPOTHESIZED cellular NAD-biosynthetic contribution. Full-protein
Q9X1X6 maps PF01958 121-234 alongside PF03447 41-106; structural domain
boundaries differ. The oxidative and reverse assays keep their distinct buffers,
cofactors and ammonium conditions. Iminoaspartate was not directly identified,
and no isolated-domain, catalytic-His193 or channeling mechanism is asserted.
Four ledgers and two OPEN discussions retain 2017 construct/label conflicts,
additional bacterial/archaeal contexts and the divergent human ASPDH preprint.

PF01959 (DHQS) adds two graphs and three qualitative OBSERVED, EXPERIMENTAL,
DIRECT product-readout effects for the full MJ0400 plus MJ1249 pair. Q58646
maps PF01959 1-173 and PF26558 187-361; isolated-domain catalysis is not
claimed. Phosphate and alternative NAD/NADP assays retain distinct buffers
and readouts. The reported330nmol yield exceeds the stated substrate amounts,
and air/argon descriptions conflict. MMP0006 negative growth evidence and
GriH's divergent chemistry remain separate from the observed graphs.

PF01969 (Ni_insertion/LarC) adds nine graphs with38 OBSERVED effects and
four HYPOTHESIZED transfer/chemistry steps. Q2RFJ5/Moth_2512 maps PF01969
4-383 across both LarC structural regions. The2022 whole-reaction MS and
coupled LarATt assays are separate from2026 coexpression/purified-LarALp
reporters. Original figures establish increased H72A output, no plotted
H70A and small cleft-variant changes obscured by simplified prose. Linker
sequences conflict between Figure4B and TableS1; exact clones, Mg/Mn assay
recipes, normalization and metal occupancy remain open. No direct nickel
coordination, natural-intermediate routing or Glu104 adduct is asserted.

PF01970 (TctA, former DUF112) adds six PHENOTYPIC graphs with sixteen
OBSERVED effects. E6 TctA/BAN66712.1 and TpiA/BAN66716.1 retain distinct
citrate and aromatic-acid contexts; tracer rescue, residual citrate uptake
and delayed versus abolished growth are not collapsed. Joint PpY1100
conversion requires transport and catabolic genes. C. glutamicum whole-operon
deletion reduces magnesium growth but improves strontium growth; heterologous
growth and CitAB-dependent tctA transcript effects remain separate. Archived
Pfam mapping, inactive UniProt IDs, uninspected supplement, E. coli host
discrepancy and unresolved ion/transport chemistry are explicit.

PF01972 (former DUF114, SDH_protease) adds one PHENOTYPIC assay-response
graph and one HYPOTHETICAL catalytic-arrangement graph. Ammelburg2011
identifies the Mm2878 comparator, mapped to Q8PT40/PF01972, but missing
controls and preparation details prevent direct catalytic attribution.
Pandit2004 supplies a computational proposal, not experimental proof of the
SDH triad. PH1510 and MjMPM cross-family transfers are excluded. The 2026
44FH/44FI structures remain unmapped functional research leads, not defense
or cleavage edges.

PF01973 (MptE-like, former DUF115/MAF_flag10) adds eight graphs with fourteen
OBSERVED effects and two HYPOTHESIZED residue roles. Two archaeal whole-protein
reactions, MJ1634 heterologous complementation, AMB-1 Maf deletion/rescue and
separate E324A/D415A variants retain distinct contexts. The Maf profile 259-419
is not its structural 273-530 region. Original figures, mutation primers and
reference residues support N491A despite a conflicting N494A caption. Glu324
catalytic-base and Asp415 donor-pocket proposals are not observed chemistry.
Maf variant controls, exact glycan stereochemistry and later-member mechanisms
remain open; no kinase/glycosyltransferase function is generalized across PF01973.

PF01976 (DUF116) retains a graphless assessment: the comparative redox
prediction, automated prenyl-synthase annotations and a DVU3364 frameshift in
a multi-mutant salt-adapted strain do not establish a directed DUF116 effect.
Three OPEN discussions distinguish reaction evidence, fusion-domain attribution
and allele-specific causality. Exact reference mappings and access limits are
retained in `evidence/PF01976/causal-evidence-assessment.txt`.

All 133 curated families remain IN_PROGRESS with partial scientific
self-review, not exhaustive family reviews. Git access returned during the
2008 follow-up, and PF01955's `20261012T130729Z` successor now covers all twenty
graphs, including the previously unretained native2009 additions. It supersedes
stale access-limit prose in the `20261012T130529Z` report without changing
scientific content. PF01956's `20261012T140035Z` successor covers selected
TMCO1/GEL contexts and the unchanged earlier EMC/EMC3 graphs; neither report
claims complete family coverage. PF01957's `20261012T141835Z` report assesses
its four scoped effects and explicit domain/coverage boundaries. PF01958's
`20261012T143541Z` report distinguishes six biochemical observations from its
inferred product and proposed cellular role. PF01959's `20261012T145330Z`
report retains qualitative joint-assay evidence with quantitative and coverage
limits. PF01969's `20261012T181928Z` report retains the LarC evidence and
construct/source discrepancies without promoting proposed chemistry.
PF01970's `20261012T210007Z` report retains the six cellular graphs,
archived member mapping, cation-specific signs and unresolved construct/host
questions without asserting direct molecular transport.
PF01972's `20261014T205229Z` report preserves the observation/hypothesis
distinction, scoped mapping and open assay/coverage findings.
PF01973's `20261014T223640Z` report preserves the archaeal/bacterial boundaries,
observed-versus-proposed residue effects and two open coverage findings.
The other 8,163 families still need
individual evidence research and retained dispositions. The structural inventory
has 8,170 graphless families, including PF01629, PF01724, PF01886, PF01954,
PF01976, PF02621 and PF20352.
No edge is invented for a graphless family. Do not mark the corpus-wide goal complete based on schema
support or these examples.

The complete structural membership is retained in
`reports/causal_graphs/inventory.json`; refresh with `just causal-graphs --apply`
after record changes and verify with `just causal-graphs --check`. The default
CLI prints JSON without saving. It is not a list of completed scientific reviews. The first
scoped review is `reviews/structured/20261011T040849Z-pf04149-causal-pilot/`;
its context-coverage finding requires successor evidence, not silent closure.
The successor assessment is
`reviews/structured/20261011T041734Z-pf04149-causal-contexts/`; it records the new
contexts and explicitly keeps the same coverage finding open. Neither report
promotes the family to REVIEWED. Further scoped reviews are retained at:

- `reviews/structured/20261011T043437Z-pf01937-causal-graphs/`, with the open
  `pf01937-causal-member-coverage` finding.
- `reviews/structured/20261011T043811Z-pf05114-causal-graph/`, with the open
  `pf05114-causal-member-coverage` finding.
- `reviews/structured/20261011T045001Z-pf01883-suft-causal-graph/`, with the open
  `pf01883-causal-context-coverage` finding.
- `reviews/structured/20261011T045004Z-pf03883-yaaa-causal-graphs/`, with the open
  `pf03883-causal-context-coverage` finding.
- `reviews/structured/20261011T045006Z-pf06568-ccaf1-causal-graph/`, with the open
  `pf06568-causal-context-coverage` finding.
- `reviews/structured/20261011T050311Z-pf01887-saduf62-causal-graph/`, with the open
  `pf01887-causal-context-coverage` finding.
- `reviews/structured/20261011T050313Z-pf07005-redtnk-causal-graph/`, with the open
  `pf07005-causal-context-coverage` finding.
- `reviews/structured/20261011T050315Z-pf08759-duf1792-causal-graph/`, with the open
  `pf08759-causal-context-coverage` finding.
- `reviews/structured/20261011T050318Z-pf17042-redtnk-causal-graph/`, with the open
  `pf17042-causal-context-coverage` finding.
- `reviews/structured/20261011T051606Z-pf01885-cthtpt1-causal-graph/`, with the open
  `pf01885-causal-context-coverage` finding.
- `reviews/structured/20261011T051610Z-pf01996-afcofe-causal-graph/`, with the open
  `pf01996-causal-context-coverage` finding.
- `reviews/structured/20261011T053101Z-pf01796-duf35-causal-graphs/`, with the open
  `pf01796-causal-context-coverage` finding.
- `reviews/structured/20261011T053103Z-pf12172-duf35-causal-graph/`, with the open
  `pf12172-causal-context-coverage` finding.
- `reviews/structured/20261011T053106Z-pf02621-mqnd-identity-gap/`, with the open
  `pf02621-causal-context-coverage` identity finding.
- `reviews/structured/20261011T054323Z-pf02410-rsfs-causal-graphs/`, with the open
  `pf02410-causal-context-coverage` finding.
- `reviews/structured/20261011T054325Z-pf01784-ybgi-causal-context/`, with the open
  `pf01784-causal-context-coverage` finding.
- `reviews/structured/20261011T055552Z-pf02130-ybey-causal-graphs/`, with the open
  `pf02130-causal-context-coverage` finding.
- `reviews/structured/20261011T055555Z-pf20352-duf6647-causal-evidence-gap/`, with
  the open `pf20352-causal-context-coverage` evidence finding.
- `reviews/structured/20261011T060730Z-pf02583-csor-causal-graphs/`, with the open
  `pf02583-causal-context-coverage` finding.
- `reviews/structured/20261011T061700Z-pf01837-duf39-causal-graphs/`, with the open
  `pf01837-causal-context-coverage` finding.
- `reviews/structured/20261011T062155Z-pf07796-duf1638-causal-graph/`, with the open
  `pf07796-causal-context-coverage` finding.
- `reviews/structured/20261011T063139Z-pf00563-rocr-causal-graph/`, with the open
  `pf00563-causal-context-coverage` finding.
- `reviews/structured/20261011T064424Z-pf00990-pled-causal-feedback/`, with the open
  `pf00990-causal-context-coverage` finding.
- `reviews/structured/20261011T064426Z-pf01139-rtcb-causal-graphs/`, with the open
  `pf01139-causal-context-coverage` finding.
- `reviews/structured/20261011T065730Z-pf01206-tusa-causal-assays/`, with the open
  `pf01206-causal-context-coverage` finding.
- `reviews/structured/20261011T065732Z-pf01519-duf16-causal-phenotypes/`, with the open
  `pf01519-causal-context-coverage` finding.
- `reviews/structured/20261011T071405Z-pf01579-duf19-causal-phenotypes/`, with the open
  `pf01579-causal-context-coverage` finding.
- `reviews/structured/20261011T071407Z-pf01629-duf22-causal-evidence-gap/`, with the open
  `pf01629-causal-context-coverage` evidence finding.
- `reviews/structured/20261011T073048Z-pf01724-duf29-causal-evidence-gap/`, with the open
  `pf01724-causal-context-coverage` evidence finding.
- `reviews/structured/20261011T073050Z-pf01882-duf58-causal-phenotypes/`, with the open
  `pf01882-causal-context-coverage` finding.
- `reviews/structured/20261011T074515Z-pf00668-tycb1-condensation-causal-assays/`, with
  the open `pf00668-causal-context-coverage` finding.
- `reviews/structured/20261011T074517Z-pf00672-tsr-hamp-causal-phenotypes/`, with the
  open `pf00672-causal-context-coverage` finding.
- `reviews/structured/20261011T075907Z-pf00892-eama-peroxide-growth-causal-effects/`,
  with the open `pf00892-causal-context-coverage` finding.
- `reviews/structured/20261011T075909Z-pf00893-emre-condition-specific-proton-flux/`,
  with the open `pf00893-causal-context-coverage` finding.
- `reviews/structured/20261011T081604Z-pf00902-tatc-vesicle-processing-and-transport/`,
  with the open `pf00902-causal-context-coverage` finding.
- `reviews/structured/20261011T081606Z-pf00924-mscs-interface-redox-and-crowding/`,
  with the open `pf00924-causal-context-coverage` finding.
- `reviews/structured/20261011T083335Z-pf01026-tatd-nuclease-and-peroxide-contexts/`,
  with the open `pf01026-causal-context-coverage` finding.
- `reviews/structured/20261011T083337Z-pf01027-yetj-ph-and-d171n-calcium-flux/`,
  with the open `pf01027-causal-context-coverage` finding.
- `reviews/structured/20261011T085102Z-pf01042-rida-coupled-biochemical-assays/`,
  with the open `pf01042-causal-context-coverage` finding.
- `reviews/structured/20261011T085104Z-pf01060-ttr52-clearance-and-lipid-binding/`,
  with the open `pf01060-causal-context-coverage` finding.
- `reviews/structured/20261011T090737Z-pf01062-best1-calcium-and-substitution-assays/`,
  with the open `pf01062-causal-context-coverage` finding.
- `reviews/structured/20261011T090741Z-pf01121-coae-product-and-contested-kinetics/`,
  with the open `pf01121-causal-context-coverage` finding.
- `reviews/structured/20261011T092759Z-pf01128-ispd-product-and-scoped-mutant-effects/`,
  with the open `pf01128-causal-context-coverage` finding.
- `reviews/structured/20261011T092801Z-pf01168-alr-racemization-and-cofactor-assays/`,
  with the open `pf01168-causal-context-coverage` finding.
- `reviews/structured/20261011T094431Z-pf01169-gdt1-gradient-and-compartment-ph/`,
  with the open `pf01169-causal-context-coverage` finding.
- `reviews/structured/20261011T094436Z-pf01171-tils-modification-and-aminoacylation/`,
  with the open `pf01171-causal-context-coverage` finding.
- `reviews/structured/20261011T100217Z-pf01172-sbds-release-and-hydrolysis-contexts/`,
  with the open `pf01172-causal-context-coverage` finding.
- `reviews/structured/20261011T100219Z-pf01174-pdxt-partner-and-substrate-contexts/`,
  with the open `pf01174-causal-context-coverage` finding.
- `reviews/structured/20261011T101618Z-pf01205-yih1-phenotypes-and-ancient-domain-boundary/`,
  with the open `pf01205-causal-context-coverage` finding.
- `reviews/structured/20261011T101620Z-pf01207-dus2-separated-redox-and-product-assays/`,
  with the open `pf01207-causal-context-coverage` finding.
- `reviews/structured/20261011T103417Z-pf01255-upps-products-and-coupled-assay-limits/`,
  with the open `pf01255-causal-context-coverage` finding.
- `reviews/structured/20261011T103421Z-pf01256-nadhx-repair-nucleotide-and-domain-contexts/`,
  with the open `pf01256-causal-context-coverage` finding.
- `reviews/structured/20261011T105305Z-pf01345-clipper-stability-and-residue-numbering/`,
  with the open `pf01345-causal-context-coverage` finding.
- `reviews/structured/20261011T105307Z-pf01458-sufbd-biochemical-and-cellular-contexts/`,
  with the open `pf01458-causal-context-coverage` finding.
- `reviews/structured/20261011T111009Z-pf01493-glts-assembly-and-expression-contexts/`,
  with the open `pf01493-causal-context-coverage` finding.
- `reviews/structured/20261011T111011Z-pf01513-nadk-donor-specific-activity-and-product/`,
  with the open `pf01513-causal-context-coverage` finding.
- `reviews/structured/20261011T112951Z-pf01535-hcf152-mini-ppr-binding-and-rescue/`,
  with the open `pf01535-causal-context-coverage` finding.
- `reviews/structured/20261011T112953Z-pf01549-shk-current-inhibition-and-family-association/`,
  with the open `pf01549-causal-context-coverage` finding.
- `reviews/structured/20261011T114941Z-pf01554-norm-binding-and-cellular-contexts/`,
  with the open `pf01554-causal-context-coverage` finding.
- `reviews/structured/20261011T114944Z-pf01594-tqsa-reporters-and-medium-specific-biofilms/`,
  with the open `pf01594-causal-context-coverage` finding.
- `reviews/structured/20261011T120912Z-pf01595-corb-reconstitution-and-substitution-effects/`,
  with the open `pf01595-causal-context-coverage` finding.
- `reviews/structured/20261011T120914Z-pf01638-hxlr-chemical-binding-and-reporter-contexts/`,
  with the open `pf01638-causal-context-coverage` finding.
- `reviews/structured/20261011T122505Z-pf01657-gnk2-binding-and-growth-contexts/`,
  with the open `pf01657-causal-context-coverage` finding.
- `reviews/structured/20261011T123903Z-pf01641-selr-products-and-conditional-growth/`,
  with the open `pf01641-causal-context-coverage` finding.
- `reviews/structured/20261011T130027Z-pf01661-af1521-binding-and-demodification-contexts/`,
  with the open `pf01661-causal-context-coverage` finding.
- `reviews/structured/20261011T131924Z-pf01679-pmp3-strain-and-medium-specific-phenotypes/`,
  with the open `pf01679-causal-context-coverage` finding.
- `reviews/structured/20261011T134104Z-pf01680-pdxs-adduct-and-reconstitution-contexts/`,
  with the open `pf01680-causal-context-coverage` finding.
- `reviews/structured/20261011T140125Z-pf01697-galt1-extract-and-genotype-contexts/`,
  with the open `pf01697-causal-context-coverage` finding.
- `reviews/structured/20261011T141903Z-pf01709-taco1-binding-and-translation-contexts/`,
  with the open `pf01709-causal-context-coverage` finding.
- `reviews/structured/20261011T143610Z-pf01732-mib-mip-cleavage-and-cellular-contexts/`,
  with the open `pf01732-causal-context-coverage` finding.
- `reviews/structured/20261011T145601Z-pf01757-oata-assay-effects-and-hypothetical-relay/`,
  with the open `pf01757-causal-context-coverage` finding.
- `reviews/structured/20261011T151345Z-pf01795-rsmh-methylation-and-genotype-contexts/`,
  with the open `pf01795-causal-context-coverage` finding.
- `reviews/structured/20261011T153306Z-pf01809-yidd-localization-and-vesicle-contexts/`,
  with the open `pf01809-causal-context-coverage` finding.
- `reviews/structured/20261011T154842Z-pf01827-fog2-construct-and-germline-contexts/`,
  with the open `pf01827-causal-context-coverage` finding.
- `reviews/structured/20261011T160704Z-pf01861-bpsa-products-carrier-and-stress-contexts/`,
  with the open `pf01861-causal-context-coverage` finding.
- `reviews/structured/20261011T162025Z-pf01862-pvlargdc-activity-and-processing-limits/`,
  with the open `pf01862-causal-context-coverage` finding.
- `reviews/structured/20261011T163659Z-pf01863-ygjp-products-thermal-effects-and-latency-hypotheses/`,
  with the open `pf01863-causal-context-coverage` finding.
- `reviews/structured/20261011T165542Z-pf01864-apcars-product-binding-and-qualified-catalytic-models/`,
  with the open `pf01864-causal-context-coverage` finding.
- `reviews/structured/20261011T171710Z-pf01865-pap-operon-and-pitr-condition-specific-effects/`,
  with the open `pf01865-causal-context-coverage` finding.
- `reviews/structured/20261011T173730Z-pf01867-cas1-integration-and-cellular-contexts/`,
  with the open `pf01867-causal-context-coverage` finding.
- `reviews/structured/20261011T175537Z-pf01868-rpp29-binding-processing-and-fidelity-contexts/`,
  with the open `pf01868-causal-context-coverage` construct/coverage finding.
- `reviews/structured/20261011T181351Z-pf01870-hjc-processing-substitution-and-tolerance-contexts/`,
  with the open `pf01870-causal-context-coverage` supplementary/member finding.
- `reviews/structured/20261011T183245Z-pf01871-ammecr1-localization-development-and-marker-contexts/`,
  with the open `pf01871-causal-context-coverage` construct/biochemical finding.
- `reviews/structured/20261011T185212Z-pf01875-memo-metal-binding-redox-and-cellular-contexts/`,
  with the open `pf01875-causal-context-coverage` preparation/member finding.
- `reviews/structured/20261011T191036Z-pf01876-rpp30-reconstitution-mutation-and-yeast-contexts/`,
  with the open `pf01876-causal-context-coverage` protocol/member finding.
- `reviews/structured/20261011T192026Z-pf01877-pab1135-dose-and-probe-binding-contexts/`,
  with the open `pf01877-causal-context-coverage` preparation/function finding.
- `reviews/structured/20261011T193644Z-pf01878-thy28-cellular-effects-and-species-limits/`,
  with the open `pf01878-causal-context-coverage` construct/mechanism finding.
- `reviews/structured/20261011T195259Z-pf01881-cas6-domain-boundaries-and-rna-contexts/`,
  with the open `pf01881-causal-context-coverage` residue/protocol/member finding.
- `reviews/structured/20261011T200930Z-pf01886-duf61-structure-and-causal-evidence-gap/`,
  with the open `pf01886-causal-context-coverage` functional-evidence finding.
- `reviews/structured/20261011T203315Z-pf01889-alia-alib-paralog-and-assay-contexts/`,
  with the open `pf01889-causal-context-coverage` catalysis/substrate-context finding.
- `reviews/structured/20261011T205809Z-pf01894-yjbq-growth-rescue-and-construct-limits/`,
  with the open `pf01894-causal-context-coverage` construct/biochemistry finding.
- `reviews/structured/20261011T212426Z-pf01895-phou-metal-signaling-and-phosphorylation-contexts/`,
  with the open `pf01895-causal-context-coverage` construct/chemical-mechanism finding.
- `reviews/structured/20261011T214656Z-pf01899-mrpe-context-specific-transport-and-growth/`,
  with the open `pf01899-causal-context-coverage` source/construct/member finding.
- `reviews/structured/20261011T220937Z-pf01900-pop5-rpp14-context-specific-rna-effects/`,
  with the open `pf01900-causal-context-coverage` construct/catalysis/member finding.
- `reviews/structured/20261011T222500Z-pf01901-o157-wzy-insertion-phenotypes-and-mapping-limits/`,
  with the open `pf01901-causal-context-coverage` assay-identity/attribution finding.
- `reviews/structured/20261011T224118Z-pf01901-strain-lineage-capsule-and-phage-context-followup/`,
  refining strain lineage and selected primary coverage; the same finding stays
  open and the preceding review remains immutable.
- `reviews/structured/20261011T225946Z-pf01902-dph6-domain-split-assays-and-hypothetical-chemistry/`,
  with the open `pf01902-causal-context-coverage` domain/member finding.
- `reviews/structured/20261011T231925Z-pf01904-yece-relative-growth-and-tm1631-computational-cleavage/`,
  with the open `pf01904-causal-context-coverage` assay/model/member finding.
- `reviews/structured/20261011T233726Z-pf01905-csa2-binding-and-devr-developmental-contexts/`,
  with the open `pf01905-causal-context-coverage` regulatory/construct/member finding.
- `reviews/structured/20261012T000124Z-pf01906-ybjq-relative-growth-and-qualified-mechanism-leads/`,
  with the open `pf01906-causal-context-coverage` assay/biochemistry/member finding.
- `reviews/structured/20261012T001545Z-pf01909-glnd-domain-and-cofactor-specific-biochemistry/`,
  with the open `pf01909-causal-context-coverage` mapping/assay/NTase-branch finding.
- `reviews/structured/20261012T003323Z-pf01910-thiamine-binding-and-separated-ecm15-phenotypes/`,
  with the open `pf01910-causal-context-coverage` source/assay/member finding.
- `reviews/structured/20261012T005223Z-pf01914-snata-marc-yche-cellular-effects-and-conflicting-contexts/`,
  retaining the first partial PF01914 assessment and superseded YchE p-value.
- `reviews/structured/20261012T005526Z-pf01914-yche-figure-label-correction-and-cellular-contexts/`,
  correcting the figure label to p=0.38 with unchanged graph directions and
  the open `pf01914-causal-context-coverage` source/clone/member finding.
- `reviews/structured/20261012T011947Z-pf01918-alba-dna-rna-and-nuclease-assay-contexts/`,
  retaining the initial partial PF01918 assessment and original evidence.
- `reviews/structured/20261012T012924Z-pf01918-assay-specific-dna-evidence-and-alba-contexts/`,
  replacing five same-paper transcription quotations on DNA-binding edges with
  the actual Figure 3 binding excerpt, without changing effects or directions;
  the `pf01918-causal-context-coverage` native-PTM/construct/member finding stays open.
- `reviews/structured/20261012T015942Z-pf01923-pduo-eutt-mmab-assay-and-domain-contexts/`,
  retaining the partial PduO/EutT/MMAB assessment with the open
  `pf01923-causal-context-coverage` construct/source/member finding.
- `reviews/structured/20261012T021931Z-pf01925-cysz-pmpc-mamo-effects-and-transport-boundaries/`,
  retaining the partial CysZ/PmpC/MamO assessment with the open
  `pf01925-causal-context-coverage` transport/construct/member finding.
- `reviews/structured/20261012T024436Z-pf01927-mut7-exd3-biochemical-assembly-and-cellular-contexts/`,
  retaining the partial MUT-7/EXD3 assessment with the open
  `pf01927-causal-context-coverage` native-function/construct/member finding.
- `reviews/structured/20261012T030857Z-pf01930-pcal-gsu-cas4-processing-and-acquisition-contexts/`,
  retaining the partial Pcal/Gsu assessment with the open
  `pf01930-causal-context-coverage` source/native-function/member finding.
- `reviews/structured/20261012T033054Z-pf01931-yjjx-biochemistry-and-prrc1-trafficking-contexts/`,
  retaining the partial YjjX/PRRC1 assessment with the open
  `pf01931-causal-context-coverage` source/construct/domain/member finding.
- `reviews/structured/20261012T035103Z-pf01933-cofd-fbia-and-glmr-separated-causal-contexts/`,
  retaining the partial CofD/FbiA/GlmR assessment with the open
  `pf01933-causal-context-coverage` source/construct/member finding.
- `reviews/structured/20261012T042052Z-pf01934-hept-ampylation-and-fusion-causal-contexts/`,
  retaining the partial HepT/fusion assessment with the open
  `pf01934-causal-context-coverage` source/member/physiology finding.
- `reviews/structured/20261012T044202Z-pf01935-hera-domain-boundaries-and-separated-assay-effects/`,
  retaining the partial HerA assessment with the open
  `pf01935-causal-context-coverage` source/domain/member finding.
- `reviews/structured/20261012T050509Z-pf01936-marf1-domain-mapping-and-separated-rna-phenotypes/`,
  retaining the partial MARF1 assessment with the open
  `pf01936-causal-context-coverage` native-target/member/construct finding.
- `reviews/structured/20261012T052935Z-pf01938-tram0076-dna-beacons-and-separated-rna-growth-contexts/`,
  retaining the partial TRAM0076 assessment with the open
  `pf01938-causal-context-coverage` native-RNA/member/construct finding.
- `reviews/structured/20261012T055417Z-pf01939-nucs-domain-boundaries-and-conflicting-cleavage-contexts/`,
  retaining the partial NucS assessment with the open
  `pf01939-causal-context-coverage` product/native-repair/member finding.
- `reviews/structured/20261012T061754Z-pf01940-duf92-separated-plant-and-mammalian-causal-contexts/`,
  retaining the partial DUF92 assessment with the open
  `pf01940-causal-context-coverage` mechanism/source/member finding.
- `reviews/structured/20261012T064400Z-pf01941-mat-separated-enzyme-denaturation-and-cascade-contexts/`,
  retaining the partial MAT assessment with the open
  `pf01941-causal-context-coverage` mechanism/source/member finding.
- `reviews/structured/20261012T071012Z-pf01944-spoiim-scoped-localization-and-suppressor-effects/`,
  retaining the partial SpoIIM assessment with the open
  `pf01944-causal-context-coverage` construct/mapping/source/member finding.
- `reviews/structured/20261012T073748Z-pf01947-scoped-lyase-and-sll1797-phenotype-effects/`,
  retaining the partial lyase/phenotype assessment with the open
  `pf01947-causal-context-coverage` assay/source/member finding.
- `reviews/structured/20261012T080813Z-pf01949-scoped-endodu-cleavage-and-cellular-effects/`,
  retaining the partial Endo_dU assessment with the open
  `pf01949-causal-context-coverage` mutation/mapping/assay/member finding.
- `reviews/structured/20261012T083350Z-pf01950-thermococcus-hydrolysis-and-conditional-effects/`,
  retaining the partial Thermococcus assessment with the open
  `pf01950-causal-context-coverage` bifunctional-mechanism/cellular/member finding.
- `reviews/structured/20261012T090304Z-pf01951-archease-scoped-activation-and-rna-processing/`,
  retaining the partial Archease assessment with the open
  `pf01951-causal-context-coverage` biochemical/cellular/construct-mapping finding.
- `reviews/structured/20261012T093010Z-pf01951-archease-mutants-and-methyltransferase-support/`,
  retaining the successor partial Archease assessment. The same coverage finding
  stays open; mutant/rescue figures and PAB1946 assay text are now inspected,
  while source preparation discrepancies and further contexts remain unresolved.
- `reviews/structured/20261012T095819Z-pf01951-bacterial-turnover-and-human-archease-rescue/`,
  retaining the next partial Archease assessment. Nineteen new bacterial and
  human effects preserve all forty-three prior edges; the same coverage finding
  remains open for clone/protocol, partner-control and further member work.
- `reviews/structured/20261012T102918Z-pf01951-partner-controls-and-xbp1-contexts/`,
  retaining the partial partner/XBP1 assessment. Twenty-eight new effects
  preserve all sixty-two prior edges; nonsignificant trends and conflicting
  protocols are not promoted to resolved mechanisms. The coverage finding stays open.
- `reviews/structured/20261012T105749Z-pf01954-af2212-prediction-structure-and-cross-family-boundaries/`,
  retaining the graphless AF2212 prediction/structure assessment and exclusion
  of other Pfam families' experimental TA effects; mapped functional evidence
  and construct/source reconciliation remain open.
- `reviews/structured/20261012T112351Z-pf01955-cbiz-chemistry-and-conditional-salvage/`,
  retaining scoped CbiZ chemistry and conditional rescue with the open
  `pf01955-causal-context-coverage` source/construct/fusion/remodeling finding.
- `reviews/structured/20261012T113218Z-pf01955-cbiz-amide-bond-precision/`,
  this successor clarifies bond hydrolysis without implying loss of the
  corrin side-chain carbonyl. The eight edge scopes and open coverage finding
  remain; the earlier report is preserved unchanged.
- `reviews/structured/20261012T115538Z-pf01955-cbis-domain-scoped-conversion-and-rescue/`,
  this successor retains seventeen additional CbiS effects with separate
  domain attribution, assay conditions and joint rescue. The same coverage
  finding remains open for constructs, source conflicts and bacterial remodeling.
- `reviews/structured/20261012T121906Z-pf01955-rhodobacter-conversion-and-cellular-contexts/`,
  retains thirteen remodeling effects with native-parent mapping and tagged
  preparation limits; the later reports cover the subsequent additions.
- `reviews/structured/20261012T130529Z-pf01955-2008-donor-rescue-and-extract-contexts/`,
  retains the native-salvage and 2008 extension but contains stale access-limit prose.
- `reviews/structured/20261012T130729Z-pf01955-2008-contexts-and-restored-provenance/`,
  supersedes that prose and binds all seventeen ledgers for twenty graphs and
  sixty-six effects. Historical constructs, source conflicts and coverage remain open.
- `reviews/structured/20261012T133200Z-pf01956-emc-reconstitution-and-emc3-variant-contexts/`,
  retains seven graphs and twenty-nine effects without equating complex insertion,
  cellular reporters and yeast phenotypes. TMCO1 and archaeal branches remain open.
- `reviews/structured/20261012T140035Z-pf01956-tmco1-gel-and-separated-client-biogenesis-effects/`,
  binds fourteen graphs and forty-three effects, adding separate TMCO1/GEL
  contexts while keeping channel, historical construct and member coverage open.
- `reviews/structured/20261012T141835Z-pf01957-ybbj-growth-and-yqez-operon-contexts/`,
  retains separate conditional growth and whole-operon resistance effects, with
  cross-family exclusions, unavailable original figures and further mechanisms open.
- `reviews/structured/20261012T143541Z-pf01958-tm1643-redox-and-separated-interpretations/`,
  retains the separate observed redox/inhibitor effects and qualified product/
  physiological interpretations, with construct mapping and human chemistry open.
- `reviews/structured/20261012T145330Z-pf01959-joint-enzyme-assays-and-quantitation-limits/`,
  retains three qualitative joint-assay effects with unresolved absolute yields,
  oxygen wording, cellular negatives and distinct bacterial GriH follow-up.
- `reviews/structured/20261012T181928Z-pf01969-larc-readouts-linker-conflicts-and-hypotheses/`,
  retains scoped LarC reaction and reporter effects, figure-based polarity,
  linker identity and protocol discrepancies, and separate transfer/chemistry
  hypotheses. The source/construct/member coverage finding stays open.
- `reviews/structured/20261012T210007Z-pf01970-tcta-tpia-cellular-effects-and-cation-contexts/`,
  retains six cellular graphs with distinct E6 paralogs, conditional growth,
  whole-operon and joint-system limits. Supplement, host discrepancy and
  further member/mechanism coverage remain open.

Each directory contains the authoritative YAML and native-derived Markdown.
Primary-source inspection varies by family; full-text, method and access limits
are recorded below and in each scoped report. SufT Figure 3
and YaaA Figure 10 were visually inspected; YaaA Figure 9 and CcaF1 Figure 8 were
assessed from text and captions only. Plotted figures in the earlier DUF89 and
DUF692 reviews were not independently visually checked. Raw and supplemental data
were not independently reanalyzed. Minimal attributed quotations and identity
facts are hash-anchored under `evidence/`.
For the biochemical additions, SaDUF62 Scheme 1, the DtnK paper's E4163/E4168
pages and DUF1792 Figure 2 were visually inspected. DtnK supplementary data and
the later DUF62 stereoselectivity study's full text remain outside the completed
review scope; access failures and inspected abstract-only leads are retained.
PF05114 retains the MbnC cellular qualification and a contradictory source
sentence; neither is silently discarded or converted into a family-wide claim.
Tpt1 Figure 1 and the 2024 CofE Figure 2 were visually inspected. Other Tpt1
kinetic/homolog plots were assessed from text and captions only. The 2007 CofE
full-text XML failed with HTTP 500; its abstract remains a lead, not an adopted
kinetic experiment. Raw spectra, structural models and supplementary assays
were not independently reanalyzed.
The M. tuberculosis DUF35 Figure 5 was visually inspected. The T. curvata
DUF35 tables and methods were inspected as text; structural figures were not
visually reviewed. The M. tuberculosis supplement endpoint returned HTML, not
the requested PDF, so truncation boundaries remain unresolved. MqnD main-paper
page 3 and supplemental Figure S41 were visually inspected, alongside expression
and assay methods. Direct ACS supplement access failed with HTTP 403; the
publisher's Figshare supplement was retrieved and inspected. Its accession gap
is scoped to the inspected material, not a claim about every possible source.
RsfS Figures 3 and 4 and YbgI Figure 8 were visually inspected. RsfS molecular
model contacts are not adopted as observed edges; the later pre-50S study was
inspected only as an abstract/database lead. YbgI Table S2 remains inaccessible:
PMC returned HTML instead of the archive and the publisher supplement returned
403. The paper's plate methods and image caption differ on incubation time;
neither is used to define the adopted liquid-growth edge. The HcgD/HP0959
primary experiments remain unreviewed leads, and the 2018 YbgI cell-wall paper
was inspected only as an abstract. No raw growth or translation data were
independently reanalyzed.

YbeY Figures 1 and 3 and the DUF6647 paper's Figure 11A were visually inspected.
The YbeY supplement route returned HTML and Europe PMC reported the manuscript
outside its open-access subset; its extended methods were not inspected. The
later S. meliloti substrate-specificity/contamination discussion (PMID:31777930)
is a follow-up lead, not an adopted experiment. DUF6647 similarity models and
benchmark inputs were not reanalyzed, and no experimental function is inferred
from the computational figure's drawn zinc or aligned side chains.

CsoR Figure 7 (2009) and Figure 2 (2007) were visually inspected with main
methods and relevant tables. The current reference protein maps to O32222,
but the exact purified tag/construct sequence is not independently established.
Raw fluorescence and reporter data were not reanalyzed. Weak Ni/Zn coupling
does not establish a universal negative; fit assumptions and nanomolar assembly
uncertainty prevent a precise structural or quantitative allosteric claim.

DUF39 Figure 3 (2018) and Figure 4 (2014) were visually inspected. The G20
plate image says MOLS4 but its caption says LS4D; the Miyazaki-specific methods
give 10 mL but generic fitness methods give 5 mL. These discrepancies remain
open rather than being silently normalized. G20 supplements returned HTML or
HTTP 403, leaving the exact insertion and clone junctions unverified. The
corrected G20 start is distinguished from the 421-aa reference, with coordinate
offsets explicitly labeled as calculations. Archaeal biochemical papers remain
abstract-only leads, and the SepCysS single-turnover result is not transferred
to MA1821. DUF1638 Figure 4 (2018) was visually inspected. A 2025 primary paper's
SPO2162 proteomics and separate MtgC/MtgD mutant-results sections were read;
their underlying data, figure and member mapping were not independently curated.
No bacterial fitness or co-occurrence result establishes an isolated-domain
catalytic function, and no raw data were reanalyzed.

RocR Figures 3 and 4 (2008) were visually inspected alongside Table 1 and its
23 C assay-condition footnote. The E352Q rate measurements are distinct from
the E352A high-magnesium endpoint experiment. The 2012 structural discussion
was read, but its figures and supplements were not independently reviewed.
Raw chromatograms, kinetic fits and exact tag junctions remain unverified;
Europe PMC XML returned HTTP 500, while PMC HTML was accessible. The source's
atomic-mechanism proposals are not promoted to observed edges.

PleD Figures 5-7 from the original 2004 Genes & Development paper were visually
inspected. The later PNAS main text changes the competitive-binding suggestion
to noncompetitive inhibition; its supplementary figure/fit was not retrieved.
The PMC supplement and institutional thesis URLs returned HTML, and Europe PMC
XML returned HTTP 500. Exact pCC2 template, DivJ boundaries and TLC temperature
remain unresolved. The separate HPLC temperature is not transferred to TLC.

RtcB PNAS Figures 2 and 4 and NAR Figures 2 and 7 were visually inspected with
their methods. The PNAS caption's 732.92-732.94 value differs from the roughly
723.93 image/Results value. The NAR Figure 7 no-GTP substrate label differs
between caption and main text; the processing edges use its plus-GTP time course.
Initial substrate impurities and unequal panel time units remain explicit.
The earlier purification methods establish tag removal, not the exact cloning
template. NAR Figures 5-6 and MS/MS interpretation were assessed from text only;
raw spectra, gels and fits were not independently reprocessed. An inferred
RNA-intermediate assignment is not promoted by successful schema validation.

TusA Figures 1 and 5 (2024) were visually inspected; the two reductant systems
and concentration dependence are retained. The B/E spectral-panel caption's
yellow-line reference conflicts with the no-TusA red-line key, so the adopted
assembly comparison uses only the A/D time courses. Exact clone sequence,
Figure 1 protein doses and Figure 5 temperature remain unresolved; supplemental
figures and raw data were not inspected. The 2013 pJD34 protocol is a mapping
lead, not independent verification of the later experimental clone.

DUF16 Figure 5 (2006) was visually inspected for insertion polarity predictions;
Tables 2/3 and their footnotes were inspected as text. Table 3's unit headings
conflict with the Results: frequency is a percentage and velocity is normalized
to WT, not an absolute 52.8 um/s for MPN524. No complementation from other genes
is borrowed for MPN104/MPN524. Raw movies and detailed prior binding protocols
were not reviewed; structure-based motility hypotheses remain separate.

DUF19 EXC-13 Figure 4 and C36C5.5 Figure 2 were visually inspected. EXC-13
main Table 2 reports 79 canals/19% affected, while Supplement S2 reports
75 canals/15 short/fraction 0.204; the unresolved discrepancy is retained.
The C44Y strain contains other mutations and does not isolate residue causality.
The Nature main text and Methods were paywalled; public figure captions,
source-data tables and Supplement Table 5 support the bounded C36C5.5 graphs.
Figure 1k was assessed from caption/data only; its experiment is not silently
merged with the distinct day-4 RNAi setup. Exact panel-specific strains, some
exposure conditions and fusion junctions remain unverified. Raw microscopy,
blots and statistical fits were not reanalyzed. DUF22's adopted primary
assessment is abstract-only, and its inaccessible 2003 lead is not counted
as a completed full-text review.

DUF58 Figures 1 and 7 were visually inspected alongside Table 2 and methods.
The oxygen-assay temperature is not specified; growth temperature and parental
maintenance atrazine are not transferred to that assay. The mutant stop product
is predicted, not directly measured, and failed deletion segregation is not a
viable null-mutant phenotype. Raw fluorescence/EPR traces and fits were not
reanalyzed. DUF29 thesis Figure 5.12 was visually inspected; the assessment covers
selected sections, not the full thesis. PDB metadata and exact sequence mapping
were inspected, but coordinates, diffraction data and a 3D view were not reviewed.

TycB1's 2002 publisher text and Figures 1-5 captions were inspected; direct
HTML/figure downloads and the 1998 precursor PDF returned 403. No plotted image
or raw chromatogram inspection is claimed. The phenylalanine unit, exact fusion
sequences, GrsA partner accession and D151N/D151A, Y166F/Y151F and Figure 1
tycA/tycB inconsistencies remain open. The three consecutive DKP experiments
share one protein batch. The 1997 identity and 2007 mechanistic qualification
papers were assessed at abstract level, not as fully curated additional assays.

Tsr-HAMP Figures 2 and 4 (2008) were visually inspected. Rotation-category
thresholds are not exact mutant percentages; the 100-cell displays are not
independent experimental replicates. The cited 2002 weighting method was read,
but unrelated crosslinking conditions were not borrowed. Exact tethering
conditions and direct molecular output remain unresolved. Selected later
Discussion and Methods were inspected; its deletion figures and supplements
were not reviewed or transferred to the G235 mutations.

YdeD Figure 1 was visually inspected, with panel A supplying the adopted graph.
The malformed control-concentration text is not interpreted as 10 mM peroxide;
the image labels the control LB. Panel-B pretreatment and pDES multi-gene
conditions are not transferred. Clone junctions, induction and replicate details
remain open, and transcription time/dose discrepancies are not silently resolved.
The 2009 construction source was subscription-only and the attempted 2000
full-text route was unavailable. Raw colonies and supplements were not assessed.

EmrE Figure 7 was visually inspected with transport Results and Methods. Its
cartoons and Figure 6 simulations are not experimentally tracked microsteps.
The supplemental PDF route returned HTML, leaving exact F/G ethidium dose,
temperature, protein-to-lipid ratio and additional quantitation unresolved.
The cited earlier protocol establishes an N-terminal GS remnant after His6
cleavage, not independently sequenced 2017 clones. Raw traces and later proton-
hopping datasets were not reanalyzed; the 2026 study remains an unadopted lead
after full-text access failed in the attempted routes.

TatC Figures 1-4 (2012) were visually inspected, including the Tat-component
immunoblot and processing/protection controls. Figure 4B is a model, not a
tracked insertion trajectory. Figure 5 text supplies substrate/linker limits;
its additional assays and Figure 6 remain outside the adopted graph scope.
The cited 2007 method establishes pFAT588's MC4100 origin and C-terminal His6
tag, not complete later clone sequencing. Raw gels, supplements and referenced
buffer/protease details remain incompletely assessed. K-12 reference identity
is distinct from the BL21 vesicle-production host; graph taxon is E. coli.

MscS Figures 4/6 (2011) and Figure 4 (2014) were visually inspected. The former
cannot distinguish desensitization from inactivation and displays three traces
from the same patch, not three independent replicates. The later adopted D/E
panels use 5% Ficoll, n=3 patches per genotype, distinct from the 10% A/B examples.
Tension is required along with crowding, and pressure-to-tension conversion has
explicit calibration assumptions. Complete clone sequences, assay temperatures,
per-panel 2014 strain assignment and direct structural chemistry remain open.
Raw traces, simulations and supplements were not reanalyzed; the 2018
N117C/N167C lead is not transferred to the different N117C/G168C double mutant.

TatD Figures 2, 3 and 5 (2014) were visually inspected. Figure 5C's concentration
series lacks units, its exact duration/cofactor conditions remain unresolved,
and the main method's protease-K quench unit is questionable. The 2023 published
Methods, bacterial Results and Discussion were checked against the author's
manuscript Figure 6 and Table S1, both visually inspected. The manuscript's
Figure 5 caption and Table S1 disagree on THF position numbering. Human BH110
controls are not transferred to the EcTatD preparation; no matched mock-control
lane is labeled for its Figure 6 assay. Raw data and complete clones remain open.

YetJ Figure 5 (2020) was visually inspected, adopting only panel C transport
comparisons. Main Results and relevant Discussion were read; supplementary PDF
routes returned HTML/403 and Europe PMC reported the article outside its OA
subset. Exact lipid composition, doses, buffers, timing, temperature and tag
remain unverified; nanodisc conditions are not borrowed for proteoliposomes.
Raw traces, simulation trajectories and other family/lipid contexts remain open.

RidA Figures 2/4/6/7 (2012) and Figure 1 (2013) were visually inspected with
relevant Methods and Results. High-pH kinetics use 30-60 s, and Figure 6 has a
single CHES buffer rather than the other kinetic assays' mixture. None of the
four substitutions abolishes all activity. The ferricyanide endpoint temperature
and IlvE addition order remain unresolved; source caption and Methods differ on
the latter. Complete clones, raw MS, the modified peptide and additional homolog
and cellular contexts were not independently resolved. Structural water and
proton-transfer proposals are not adopted as observed steps.

TTR-52 Figures 1/2/4 (2010) and Figures 3/4 (2012) were visually inspected.
The author-hosted 2010 PDF supplies Methods pages 11-12, with page 11 visually
checked. Its deposited HM130527.1 translation exactly matches G5ED35. sm211 is
V43M, not the tm2078 deletion. The 2012 M5 labeling discussion conflicts with
earlier Results, and its C-terminal double-mutant text says I113R/L132K while
Figure 3 says I113R/L132R; those ambiguous constructs are excluded. The strip
protocols differ tenfold in cation concentration. Full supplements, movies,
structural coordinates, exact protein doses, raw images and folding controls
remain outside this partial assessment; modeled WT geometry is not an observed
binding trajectory.

BEST1 Figures 1/3/4 (2016) were visually inspected with main assay Methods and
relevant Results/Discussion. The cited 2014 construct and flux Methods establish
Thr2 processing and dye/ionophore details; they do not supply missing 2016
replicate counts or recording temperature. Historical and modern sequences
differ only outside the tested 1-405 region, and 4RDQ exactly matches 2-405 plus
EGEEF. Retained-current fractions do not establish absolute conductance or open
probability. Aperture experiments, later inactivation, cryo-EM and GABA activation
remain separate follow-ups; structural models are not observed trajectories.

CoaE's 2001 reaction scheme and 2011 Figure 5 were visually inspected, with
relevant Methods, Results and Table 2 read. The original NMR spectrum is reported
but not supplied for independent reanalysis. R140A is marked no reaction in the
table yet has a plotted Km; D32A ATP Km, G8A values, the R140K fold claim and
printed efficiency ratios also conflict. The 2009 forward-primer junction
encodes MVTDRD while the archived and current mycobacterial sequences begin
MLRIGL. Exact clones, raw kinetics, cofactor naming and magnesium/reporter controls
remain unresolved. Kinetic directions are scoped to their substrate series;
no atomic catalytic role is inferred from the docking model or fitted parameters.

IspD's 1999 Methods/Results/Discussion and Tables 1-3 were read, with sequence
and purification Figures 3/4 visually inspected. The 2004 primary proof was read
through pages A-H, with Figures 3/4 on page E and Table 1/Figure 5 on page F
visually checked. Lettered pages and placeholder publication fields prevent
claiming final-publisher comparison. The isotope percent-axis, time range,
protein concentration/mass and T104V/T140V labels conflict. These do not become
precise trapped fractions or corrected source data. Purified turnover fits and
unpurified inactive-mutant screens remain separate; folding, normalization,
final kinetic-assay pH and complete clones remain unresolved.

Alr's 1998 main text and Methods were read, with Figures 2-5 and Table I visually
checked. The K39A primer matches current P10724 residues 34-44 locally, not every
historical clone. Table I's loss/reactivation experiments use distinct enzyme
preparations. Figure 4 implies 0.1 M methylamine in its caption but says 0.5 M
in prose; Figure 5 independently specifies the adopted 0.5 M. A displayed
enzyme-free methylamine control is absent from Figure 5, and formaldehyde in the
proposed recycling scheme was not identified. The separate 1999 chemical-rescue
paper was inspected only at abstract level and contributes no edges. Its indexed
erratum concerns an author's name. No isolated-domain or in-vivo regulatory
mechanism follows from these assays.

Gdt1's 2023 main Methods/Results/Discussion and Tables 1/2 were read, with
Figures 1-6 visually checked. All four supplement pages were inspected, with
S1 and Table S1 visually checked after the direct PDF route returned HTML and
Europe PMC supplied a valid archive. The Figure 1 caption says digitonin while
Methods and S1 specify nigericin; neither is silently substituted. Only pH 8.0
versus 6.8 is adopted for both ions, not every adjacent contrast. Whole-cell
pH effects do not exclude leakage or endogenous transport. The 2016 tagged
delta23 protein and three-hour induction differ from 2023's incompletely
reconstructed constructs and two-hour induction. The 2020 sensor method's ice
starvation is not transferred to the 2023 60-min/28-C protocol. Native pH effects
remain indirect and bounded by steady-state and late-cytosolic negatives.

TilS's 2009 Methods/Results/Discussion and Tables 1-5 were read; Figure 2 was
visually checked. Product mass and gel shifts support lysine and ethanolamine
modification preparations, not independently localized bond chemistry. The
published reverse primer omits the native stop and is compatible with the
reported His6 fusion; an exact vector scar is not reconstructed. E. coli S100
and FLAG-tagged B. subtilis IleRS are different preparations, with distinct
normalization references. Reactions were frozen without repurifying tRNA;
carryover controls, replicate counts and uncertainties remain incomplete.
Ornithine and N-alpha-methyllysine products reflect reported lysine contamination.
The 2025 abstract and selected near-cognate-recognition Results/caption were
read as a follow-up lead; full Methods, figure and member mapping are not claimed.

SBDS's selected 2011 biochemical/structural Results, Discussion and main Methods
were read, with Figures 3/6 visually checked. Human SBDS and EFL1 act on mouse
or rabbit particles, and R126T/K151N are outside the N-terminal Pfam match.
The supplement API returned a non-open-access XML error and the publisher route
returned HTTP 403; full tag/scar and S7 binding details remain unverified.
Neither S235-independent truncation release nor retained K151N hydrolysis
stimulation establishes every cellular mechanism. The 2022 recycling abstract
is a follow-up lead, not a full-study review or source of adopted edges.

PdxT's 2005 article and appended supplement were read, with Figures 1-4, 6/7,
S2/S3 and cloning Methods visually checked. Untagged strain-168 preparations
are distinct from His6 pull-out protein and the earlier SMY assays. Product
identity has HPLC/MS/NMR support; S3's unknown 3.75-ppm contaminant remains
visible. The kinetic caption's 1-mM glutamine differs from Methods/Results'
10 mM, and inhibition captions use seconds where text/axes use minutes.
Acivicin dose lists and peptide/intact-adduct masses also require reconciliation.
No precise rate repair, ammonia-channel trajectory or cellular drug efficacy
is inferred. SMY's pBB1181 penultimate-residue description is not silently
mapped onto the strain-168 reference or independent expression constructs.

Yih1's main Methods/Table 1, fragment/mutant Results, ancient-domain analysis and
Discussion were read, with Figures 2/5 visually checked. The plate protocol's
dose, time and temperature remain unresolved; liquid 10-mM/1-h treatment is not
transferred. Truncated-construct labels and confusing H3 growth wording are not
silently corrected or adopted as mutant edges. Exact historical clones, raw
blots and later cell-cycle mechanisms remain open; the 2015 abstract is a lead.

Dus2's 2009 main Methods/Results/Discussion were read, with Figures 2-5/8 visually
checked. The forward and reverse C117A primers disagree at a second residue;
the synthetic RNA strings do not independently establish the stated intron
difference. Figure 3 differs at 35/60-uM enzyme and 450/457 nm, and Figure 4's
axis says mM while its caption says uM. Native/mutant substrate comparisons
also differ in temperature. No exact rate repair, mutant-specific proton transfer
or physiological reverse cycle is inferred. Raw spectra and unshown NMR were not
reanalyzed; the 2002 yeast and 2026 bacterial DusA abstracts remain leads.

UppS's 1999 expression/purification and assay Methods, relevant Results and
Discussion were read; Figure 6 was visually checked. Product TLC is reported
but not shown, and its complete recipe is unspecified. The magnesium and
detergent panels retain residual output and nonmonotonic dose responses;
pyrophosphatase coupling prevents assigning a specific UppS molecular step.
The archived Q47675 sequence exactly matches P60472, but historical donor
strain and full clones remain unverified. The M. luteus 1998 paper is an
abstract-only lead; the Bos-12 2001 paper was inspected only through its
abstract and selected Methods, not mutant figures or full Results.

NADHX repair's 2011 main Methods/Results/Discussion and supplemental Methods,
Tables S1-S3 and captions were read; Figure 2, Table S1 and Figure S4 were
visually checked. Cited RefSeq proteins match current UniProt references, and
primer coding termini agree locally, without reconstructing full historical
His fusions or source strains. Figure 2C does not specify stock enrichment or
which optical wavelength was used. HPLC identities rely on retention/UV
comparison; raw chromatograms and unshown stoichiometry were not reanalyzed.
The 2018 study's abstract, Introduction and selected early Results/Figure 3
caption are follow-up evidence leads, not adopted cellular edges; the 2026
Cell study remains an unreviewed search lead.

CLIPPER Figures 5/6/S8 (2025) were visually inspected with experimental Methods
and Table S6. Its synthetic WT sequence exactly matches reference 708-828, and
the mutant differs only at K715A. Both encode N748/D749, not the proposed Asp748;
the K517A Methods label is inconsistent with the encoded mutation. Deposited
9IFR is GP plus the same WT segment, but biochemical tag removal is not proven
by crystallographic processing. Four CD scans are not independent preparation
replicates, and proteolysis remains a qualitative endpoint. Raw diffraction and
biophysical data were not reanalyzed. Several direct routes failed; complete
Europe PMC XML and a subsequently completed supplemental archive supplied the
inspected material. Selected CaT2 domain-analysis Results/Discussion remain a
separate scope-qualification lead, not a complete new cellular assessment.

SufBD Figure 4 and supplemental S2/S3 (2017) were visually inspected with main
Methods/Results/Discussion and supplemental tables/captions. Table S1 fixes the
MG1655-derived strains; C254A/C405A primer translations agree locally, not over
whole clones. Retained sulfur is not a site-resolved chemical trajectory and
C405A retains stimulation in the other assay. H360A abundance is lower, and
the particular plate's glucose supplementation remains unresolved. Other plotted
figures, raw measurements and prior/later family experiments remain uncurated.
Publisher HTML and the original supplement were accessible after PMC's challenge.

GXGXG/GltS main enzyme/SAXS Methods, assembly/kinetic Results and relevant
Discussion (2008), plus supplemental construction/DLS Methods, Tables 1-3 and
Figure S3/S8 captions, were read. Figure S3, main Table 2 and supplemental
Methods pages 1-2 were visually inspected. Printed primers locally support
the named deletions, but nucleotide stop-position prose and complete clones
remain unresolved. The delta40 production endpoint lacks a displayed gel or
quantitative detection limit. DLS size, SAXS mixture models and kinetic
correlations are not equivalent evidence for a unique domain-specific pathway.
Raw scattering/reconstruction and the unshown expression data were not reanalyzed.

NADK's 2013 Methods/Results/Discussion and supplement were read; Figures 2/3
and S1-S4 were visually inspected. S4 is an expression-extract gel, not a
purified-protein purity control. HTML/XML Table 2 has internally inconsistent
displayed ratios; no repaired kcat/Km values are adopted. Exact coupled-assay
enzyme doses, volumes and rate windows remain incompletely specified, and TLC
is an uncalibrated ten-hour endpoint. Selected 2001 parent-plasmid Methods and
identity/donor Results qualify the MG1655 lineage, N2/D2 and terminal-primer
differences, assay units and KND/KNDE descriptions; its figures were not visually
reviewed. Other mutants, homologs, cellular yields and evolution remain uncurated.

HCF152's production, RNA-probe and gel-shift Methods, relevant Results and
Discussion were read, with Figures 2 and 3 visually inspected. Supplement
Table S1 and Figures S1/S3/S4 were unavailable after failed/timed-out requests;
incomplete archives were not used. Local motif mapping resolves K426/N464 but
not complete historical fusion boundaries. Figure 3B supports partial rescues
at 384.6/454.5 nM, not WT recovery; the reversed K_D wording in prose is not
adopted. Pet309 2014 remains a separate lead because its S288c reference's
current Pfam assignment is PF23276, not PF01535, and its tested strain differs.

ShK's 2012 Methods, Results, Discussion and Figure 6 captions were read from
NCBI XML. Primer reverse-complement assembly gives a unique 21-base overlap
and the exact mature reference sequence after the cleavage site; this is a
printed-design check, not independent clone resequencing. Figure 6B is synthetic
peptide, whereas 6C reports recombinant dose responses. Images, supplementary
NMR data and raw currents were not inspected because media routes failed or
returned challenge HTML. The curated-family versus current-HMM discrepancy,
unverified channel clones and separate human/rat T-cell contexts stay explicit.

NorM's 2021 functional and biochemical Results, relevant Methods and Discussion
were read; Figures 2 and 4 were visually inspected. The current Q9KRU4 sequence
matches InterPro, and archived AAF94694.1 establishes the initiation difference
and internal numbering offset. Supplement download failed DNS resolution;
expression blots, primer details and the complete historical plasmid remain
unverified. The 2014 XML was front matter/abstract only and its PDF inaccessible.
Other mutants, chimeras, ionophore/reconstitution contexts and other family
members still require separate evidence review.

TqsA's 2006 Methods/Table 1, relevant Results and Discussion were read from
the author-hosted PDF; Methods and Figure 3 were visually checked. The selected
2022 full-text binding/antiport Results, Methods and concluding Discussion were
read, but its figures and spectra were not visually inspected. Its explicit
inability to demonstrate transport is an assay limitation, not proof of absent
function. Historical constructs, initial well-assay duration/temperature,
additional rescue/motility/flow endpoints and the detailed reporter protocol
remain open. Neither a suspect mass-shift unit nor ambiguous MIC ordering is
silently repaired into a causal edge.

CorB's 2021 transport Results and relevant cloning/purification/reconstitution
Methods were read; Figure 6 and Supplementary Figure 8 were visually inspected,
including SEC and reconstituted-protein gels. Supplementary Table 1 provides
mutagenic primers. Exact UniProt/InterPro sequence checks verify both accessions
and the TtCorB residues. Protein-free controls and calibration support the
vesicle response, but orientation, counterion and active fraction are unresolved.
The earlier cellular chimera paper has not been independently full-text reviewed;
human CNNM and isolated CBS-domain results are not transferred to these graphs.

HxlR's 2021 biochemical/structural Results and relevant Methods were read;
Figure 1 and Supplementary Figures 1/2 were visually inspected. Supplementary
Notes 2-4 and Table 2 distinguish the 50-bp EMSA probe from crystallization DNA,
and the K13A range from the WT/C11A range. Exact P42406/InterPro and 7BZD
GSH-plus-reference sequence checks preserve extra-domain C11/K13 mapping.
The pBAD primer suggests a possible S2G difference but does not establish the
assembled plasmid sequence. No raw data reanalysis, independent cloning,
2005 native-regulation review or exhaustive FAsor/member survey is claimed.

A concrete filesystem-read failure recurred while rendering these supplements:
offline `uv` could not read `/Users/marcin/.cache/uv/sdists-v9/.git` under the
sandbox. A narrowly approved retry succeeded. Repository and installed-skill
reads succeeded without escalation; no filesystem permission or configuration
changes were made. This identifies the failing cache read, not the cause of
every earlier reported denial.

The later PF01901 follow-up retried repository and installed-skill reads,
the specific cache-path metadata read, and offline `uv`/Pillow import. All
succeeded without escalation. Chromium still failed separately at Mach-port
startup with error1100 and required a narrowly approved command retry. No
permission configuration was changed; successful reads do not establish a
global permission repair. The distinction is consistent with the documented
[command sandbox boundary](https://learn.chatgpt.com/docs/sandboxing), which
also applies to spawned package managers and test runners.

Gnk2's 2014 Results, Discussion and Methods were read, and Figures 5, 7 and 8
were visually inspected. Figure 5 labels 0.625-10 mM mannobiose while Methods
list 1.25-20 mM. Figure 7B retains a small delta-mnn2 response despite stronger
no-effect wording in the text. Both qualifications are preserved. Supplementary
S5-S7 returned HTML rather than the linked DOC and remain author-reported
controls, not visually verified ones. UniProt/InterPro sequences match; 4XRE
is exactly extra Met plus precursor27-134 and cites the paper. A formal
3W9Q-to-4XRE supersession was not established. Later actin work and other
DUF26 members remain follow-ups. The initial dry run rejected a misnamed
discussion key before projection writes; the corrected overlay passed.

SelR's PNAS Methods, Results and Discussion were read and Figures 1-4 visually
inspected; Figures 2-3 were rechecked during the saved review. Fly R-substrate
product formation has displayed enzyme-free controls; the mouse panel does not.
The deposited fly clone and UniProt isoform match exactly, while the domain
interval is coordinate-transferred rather than independently HMM-tested. Archived
mouse C95 with an explicit SE_CYS annotation is not a natural cysteine allele.
P25566 grounds the yeast locus to S288c, not a resequenced BY4741 isolate.
Exact PNAS biochemical doses/timing, mouse vector termini, detailed yeast medium
and the original MAT-alpha notation remain unresolved. Later JBC abstract,
Methods and initial Results were accessible, but subsequent full-text routes
did not yield the remaining Results or figures; C124/C69 intermediates, zinc-site
mutants and complementation are not adopted. Its 10-versus-20-mM DTT discrepancy
is retained without assigning either value to the earlier PNAS assays.

Af1521's Karras Results, Methods and TablesI-III were read, with Figures1,2,3,6,7
visually inspected. TLC identity is co-migration, not MS/NMR verification; all
binding mutants retain measurable binding and their error definitions are unresolved.
Jankevicius Figure4 and supplementary pages19-20 were inspected, preserving the
GST-specific unwashed-NAD exception and separating human MacroD2 product assays.
Rosenthal Figure1, Online Methods and Supplementary Figure1/caption were visually
checked. The supplement identifies the PARP10 818-1025 substrate and shows
retained protein bands; the roughly45% remaining modification is not complete
hydrolysis. The common G50/30C protocol does not enumerate the Af1521 dose or
prove its tag state. Exact native reference/PDB sequence matching does not
resolve every expression construct. Allen2003 and Dani2009 construct-source
access gaps and uninspected later nucleotide/engineered-variant studies remain
follow-up work. No simulated water step or human cellular endpoint is adopted.

Pmp3's Navarre 2000 Results, Discussion, Methods, Table I and all eight figures
were inspected. Sodium-content and methylammonium assays do not directly measure
voltage; Figure 6 does not establish single-deletion Pma1 activation. The exact
yeast deposited peptide and plant EST translation support identity, not final
yeast construct sequencing or isolated-domain activity. YR93/CY162 alleles,
integrated flanks, expression abundance and the sodium protocol remain open.
No-added-KCl YD is not potassium-free, and the EGTA-to-calcium substitution
jointly changes two medium conditions. De Block 2015 public text was read only
through initial proteomics/PDR5 Results and the Figure 1 caption; remaining
Results, full Methods, figures and supplement need assessment. Its successful
public-text access is not negated by a separate curl 403. Later strain, membrane
fraction and Ena1/Ena2 peptide distinctions are retained as follow-up boundaries.

PdxS's Raschle 2007 main text and Figures 2, 3, 4, 6/Table 1 were inspected;
the 2005 Figure 1C/2 was rechecked against retained main/supplement evidence.
Mass shift and K81 peptide localization do not settle the initial bond chemistry.
The Hanes 2008 author-hosted main text and publisher supplement were read, and
S5 was visually inspected: isotope coupling supports ammonia-nitrogen
incorporation, while Z2 requires acid/urea quenching and is explicitly off-pathway.
The remaining NMR panels were not independently visually assessed in this session.
The 2006 supplement request returned HTML, not a readable PDF; its deposited
2NV1 construct sequence and selected main-paper Methods were inspected instead,
without claiming they sequence every 2007 assay vial. Historical clones, WT
partner tag matching, G3P-dose/pH conflicts, assay-specific missing conditions,
JACS substrate work and later second-site/species studies remain follow-ups.

GALT-1's Titz 2009 primary HTML Methods, Results and Discussion and Figures
2-6 were inspected. The companion Butschi 2010 genotype/glycome Results,
relevant Methods, Figures 4/7 and one-page supplement S2 were also inspected.
Figure 2B's reversed caption order is resolved by the displayed precursor
masses. The 2009 beta1,4 supplement and primer table remain uninspected;
its PDF request returned HTML, publisher access returned 403 and ETH 429.
Printed 40-uM MES and 10-uM metal concentrations are not silently changed to
mM. Directness is at the joint extract-reaction level, not purified-domain
chemistry. Developmental fractions are not death rates; the glycome comparison
uses OP50-grown animals and a selected fraction, not the CGL2 feeding condition.
Other members, purified enzyme, historical clones and matched glycome rescue
remain follow-ups rather than assumed extensions of nematode specificity.

TACO1's Richman2016 selected Results, Methods, Discussion and Figures2/3/6
were inspected. Figure6 identifies the mutant EMSA probeB, mapped in Figure3
to mouse mtDNA5446-5632. Versioned RefSeq and current InterPro/UniProt
sequences agree; the larger mature protein, N-terminal substitutions and
current PF01709 interval are not conflated. The2016 supplement was text-surveyed,
not completely visually assessed. Brischigliaro2024 selected Methods/Results,
Figures1/2, supplementS3 and TableS4 were inspected. Footprints are normalized
occupancy, not directly measured kinetic rates; P-site offsets remain discrepant.
PMC supplement requests returned challenge HTML; publisher downloads succeeded.
Human rescue clone/promoter/tag and exact exon1 lesions remain incompletely
specified. The2026 human structural Results/nucleotide Methods and supplement
text were partly inspected, but its figures and commercial construct were not
fully assessed. The2025 bacterial early text and2026 plant downloaded XML are
follow-ups, not curated edges. No GTPase, universal PP-stall, mtEF-Tu displacement
or collision-to-cleavage mechanism is promoted from these incomplete assessments.

MIP's Arfi 2016 relevant Methods/Results and inline SI were inspected, including
visual checks of Figures 2/3/4/S5. S4/S7 images were not checked, so inhibitor
and kinetic extensions are not adopted. Nottelet 2021 selected Methods/Results,
Figure 4/5 captions and the 440-pixel PMC panels support qualitative effects,
not calibrated peak areas or immunoblot effect sizes. Publisher supplements
and the Europe PMC PDF returned 403; enlarged PMC figure pages were challenge
HTML. Supplemental strain table and validation panels remain unassessed.
The exact GenBank/UniParc sequence avoids transferring a retired reference
with X810 to GM12 L810. The 2016 mutant label and antibody CH numbering are
not silently corrected. Berlureau 2026 Figure 3 and serum-free control S13
were visually inspected at large size, with genotype, assay and Discussion
text. One-clone designs, incidental variants and missing complementation limit
cellular interpretation. Its May 2026 correction concerns acknowledgements
and author approval, not experimental results. The ATPase opening/reset model
remains a hypothesis; missing predicted pellet products and localization or
detection alternatives are retained. Other species are explicitly research
leads, not curated mechanisms. MIB, Protein M and MIP are kept distinct.

SaOatA's Jones2021 main Results, selected Methods, Discussion and Figures1/3/4/5
were inspected. Supplementary recipes, clone/strain tables and remaining
spectra were inaccessible, not treated as negative results. WT and mutant
deposited PEAKS search/coverage outputs and two annotated MS2 tables were
inspected, not raw spectra re-searched. The mutant search-reference extra
lysine substitutions are not silently applied to every biochemical preparation.
Tyr206 acetylation in the untreated control prevents a directly observed
treatment-to-intermediate claim without matched provenance/quantitation.
GenBank/UniProt sequences match, but clone resequencing is not established.
The ATCC6538 topology library, USA300 cellular host and WT search reference
are distinguished. Figure3C donor/pH/solvent conditions differ from Figure1;
Figure3D R25A/R25K, Figure1A gray-control genotype and Figure4E time remain
unresolved. OafB computational passages supply context, not validation of
SaOatA chemistry. Other primary member leads remain partial follow-ups.

RsmH's Kimura and Suzuki 2010 Methods, Results and Discussion, Figures 2/3/4
and Table 1 were inspected. Figures 1/5, exact historical clone termini and
external SI remain unassessed. Reference sequence equality is not clone
resequencing. Whole-gene effects remain indirect even where separate purified
assays support the biochemical assignment. The Figure 4B/Discussion UGA
direction conflict and the 2.5-pmol RNA versus 5-pmol particle comparison are
retained, as are reporter normalization and unverified error-bar definitions.
Selected O157:H7 2019 Methods report an anti-5-methylcytosine kit assay and
acknowledged preparation impurity; no DNA-product edge is adopted. Selected
Bacillus 2026 preprint Results/Methods are explicitly not the final article,
whose full text was inaccessible. Condition-specific negatives, active-ribosome
dose, member mapping and final-version verification remain follow-ups. No
atomic RsmH mechanism or unmeasured modification-to-growth chain is asserted.

YidD's Yu 2011 main Methods, Table 1, Results and Discussion were read;
Figures 2/4/5 were visually inspected. Figure 3/6 text and captions were
assessed, not their images. Its XML endpoint returned 500 and the supplement
URL returned download-preparation HTML; the main HTML was successfully read.
The historical DUF37 identity is not changed by Figure 1's DUF31 caption.
Geng 2015 Chapter 4 Methods/Results/Discussion and Figures 2/3/4/6/7/S1/S2
were inspected, with the chapter explicitly marked Submitted rather than
a verified journal version. Figure 5 co-purification was assessed from text,
not its image. Different F0c abundance results in MC4100 and BW25113 are
preserved. Polar YidC effects, the Lemo21/BL21 host discrepancy, Figure 6
panel labels, inherited insertion recipes and NuoK topology wording remain
open. Population toxin-gene PCR, cross-links and co-purification are not
promoted to hemolysis, recruitment or ribosome-tethering mechanisms.

For FOG-2, Nayak 2005 Results/Methods and Figure 4 were inspected, with
the 327-aa reference reconstructed from the exact genomic version and
published splice coordinates. FTR-1's 314-aa reference also matches its
versioned protein record. The 2005 Methods 318-aa value, Bait image
heading and 74/76-aa terminal-boundary differences remain open. Clifford
2000 was read through the primary-paper transcription, not original figure
images or lab supplements; missing RNAi protocol/controls remain explicit.
Hu 2019 Methods, Results, Discussion and Tables 1-3 were read, and Figures
3/6 visually checked. Its nm75/nmIs4 image discrepancy, selected genotyping,
incomplete HA-tag suppression, negative expression readouts and assumed
model parameters are retained. Neither study provides a complete observed
FTH-to-proteolysis-to-translation mechanism. Other family members and cited
gene-conversion/mating contexts need independent primary review.

For BpsA, 2017/2019 primary publisher Methods, Results and kinetic tables
were inspected through readable indexed full text; direct Wiley HTML/PDF
downloads returned HTTP403. Original biochemical figure images, raw spectra
and supplementary primers were not independently inspected. NCBI versioned
proteins exactly match UniProt references. Deposited constructs and 2019
Table 4 primer translations establish the retained sequence mappings, not
historical clone resequencing. A terminal mass shift is separate from exact
ester-site assignment and productive transfer. C9 spermidine arithmetic and
2017 T350Y table/prose discrepancies are retained, not silently resolved.
Okada 2014 Figure 6 and Fujiwara 2025 Figures 5/6 were visually inspected;
strain construction, different medium formulations, normalized CFUs and
partial rescue constrain interpretation. The 2025 Figure 6 accessibility
text reverses strain ordering; plotted curves, legend and Results agree.
Supplementary CFU counts, matched BpsA restoration and uncurated member,
transcription, RNA-polymerase, DNA and surfactant studies remain follow-ups.

For PvlArgDC, Soriano 2008 full primary XML/HTML, Tables 1/2, Methods,
Results and Conclusions were inspected, along with original Figures 3/4.
Q57764 equals versioned AAB98302.1; published primer translations and parsed
2QQC/2QQD deposits confirm N47A/E109Q and the native-versus-tag numbering.
The N47A structural comparator is S53A, not WT. Relative processing rates
were inconclusive because the WT control did not dissociate, so no observed
rate decrease or quantified mediation is asserted. JBC/Cell original
2002/2003 fulltext returned 403, and Fukuda 2008 TK0149 content was available
only at abstract scope. These access limits are not evidence of absence.
Assay-solution maturation, processed-site turnover, alternative catalytic
effects, exact original protocols and Tk cellular conditions remain open.

For PF01863, original Sevin Supplementary Figure 16 was visually inspected,
and publisher Tables 3/9 were parsed. Heat-inactivated controls support a
net preparation-level UMP outcome, not molar stoichiometry, separate PPi
quantitation or cellular flux. Main Methods and exact historical clone
sequence remain unverified; ETH thesis access returned 403/429. Lopez-Pelegrin
2013 fulltext and Figure 3 were inspected with parsed 4JIU/4JIX deposits.
Native terminal residues fall outside the current Pfam spans, and proabylysin
K2V/L2V discrepancy is retained. Reported 85/65 C thermal transitions versus
95 C full length do not establish successful activation. B80 Table 2 peptide,
coordinate and mass entries need reconciliation before assigning its activity
to PF01863. Lobb Table 4 remote-homology candidates are not biochemical assays.
The uninspected cellular datasets and remaining member contexts stay open.

For PF01864, primary Ren2017 Methods, Figures1/4 and complete publisher Figure6
were inspected, alongside published S3/S4/S5/S7 and TableS2. The initial PMC
Figure6 JPEG was incomplete; the recovered publisher image confirms that
Q123A/H157A stronger strip binding does not mean increased product formation.
Figure7 captions and Discussion, not its original image, support explicitly
labeled hypotheses. Current reference/Pfam mapping and PDB5GUF establish the
intact ApCarS construct and outside-domain D8/W9 sites. Primary expression-host
Methods take precedence over vector-as-host deposit metadata. The published
article PDF request returned HTML; public thesis Chapter2 is an accessible
Jain2014 reproduction, Chapter3 a different2015 study and Chapter5 a draft with
different figure numbering. Their incomplete inspection is retained honestly,
without importing AfCarS or multi-enzyme effects into ApCarS graphs.

For PF01865, Hsieh2017 thesis Methods, strain/construct tables and selected
Results were read; original Figures3-15/16/21/29 and Table3-28 were visually
inspected. Positive R78A and D90A/H96Y uptake contradict zero-uptake prose;
Pap-only failure and operon restoration expose a polarity/translation limit.
Vermilya2026 final Methods and Results were read with original Figures2/3.
The published supplement's FigureS1 names NWMN_0632 as PitR, while TablesS2-S4
establish strains and plasmid designs; pages22/25 were visually inspected.
The initially incomplete EuropePMC ZIP was not used; a later completed,
integrity-checked archive supplied the actual PDF. Exact Pap and Newman
reference-to-domain mappings were independently verified. Other member
studies, environmental contexts and direct biochemical mechanisms remain open.
This is not a complete thesis/literature review or experimental replication.

For PF01867, the2014/2015 primary Results and Methods were inspected with
original2014 Figures1/3/4 and2015 Figures1/2/3/ED2/ED3. K224A's cellular and
purified outcomes remain distinct. Main Figure2H supports donor release;
the image linked under ED5 instead shows ED6, and the following linked image
shows ED7. No original ED5 visual verification or separate target-rejoining
edge is claimed. The2016 IHF primary abstract and selected2017 Results/captions
qualify topology and site-selection claims without pretending those papers
received complete method/image review. Exact reference/PDB sequence equality,
current Pfam boundaries and all retained residue positions are verified.
Remaining constructs, supplementary controls and other members remain open.

For PF01868, Chen2010/2011/2012 Methods and Results were inspected with
original2010 Figure7 and supplement TableS1/FiguresS4-S6,2011 Figures4/6/7
and2012 Figures1/2. The author's linked2010 ZIP resolved the failed direct
PMC/EuropePMC supplement retrievals; its integrity and24-page PDF were checked.
Published primer translation, reference sequence equality and current domain
coordinates were checked independently. The Mth terminal-residue discrepancy
remains unresolved, and1OQK is not the untagged biochemical clone. Pfu2011
Figure4 caption pairings conflict with image labels; delta24 ITC is reported
without a displayed trace. The2010 pH correction uses a control at20 rather
than30 mM Mg. No matched-buffer protein-only effect is substituted for the
optimized-protocol comparisons. Human H3.3 papers remain primary leads, not
completed scientific reviews. No full-text publication was committed.

For PF01870, the1999/2000 main Methods/Results and original Figures3-5 were
inspected, together with2019 Methods/Results/Discussion and original Figures1/2/3/5.
Current protein/domain JSON, original GenBank CDS and current RefSeq FASTA
support reference identity. The2019 supplementary DOCX/TIF requests returned
HTML challenge pages; their primers and additional controls are not claimed
inspected. Figure2 kinase dose is not independently resolved from its caption.
The2000 mutagenesis PDF returned403 and remains a primary follow-up lead.
Zinc counterion disagreement, residual activity, Hje-intact strain context and
condition-specific negatives are retained. Mg-coordination interference and
repair-pathway switching remain hypotheses, not observed graph trajectories.

For PF01871, original human Figure2, final zebrafish Figure4 and mouse
Supplementary Figure7 were visually inspected with their relevant Methods.
The older zebrafish manuscript has different supplement numbering and an
8.2/8.4-ng E1I1 disagreement; supplementary captions were read but the final
supplement images remain unreviewed. Mouse reagent and primer tables were
retrieved from the correct publisher host after initial DNS/HTML failures.
Reference sequences equal versioned GenBank translations, and the human
mutagenesis primer supports G177D; rescue-insert/batch identity remains limited.
The A549 abstract is not converted to canonical edges without full Methods and
figures. Proteasomal degradation, radical transfer and family-wide enzymatic
function remain unproven by the inspected experiments. During self-review the
human evidence quotation was corrected to the source's exact wording before
the retained review; no previous retained report was changed.

For PF01875, original2022 Figures1/2 and S1,2023 Figures1-3,2024 Figures4/5
and Figure5 supplement1, and2014 reprinted Figure4 were visually inspected
with relevant Methods/Results. EuropePMC supplied the PNAS supplement after
a publisher403; the public author-thesis repository supplied the older paper
after an obsolete URL returned HTML. Full papers remain temporary, not committed.
Reference/domain and deposited-construct sequences were verified separately.
The2022 BCA10/20-uM discrepancy, Amplex wavelength disagreement and wound-time
labels remain unresolved. The2014 unpreloaded protein dose and folding controls
are not inferred from other panels or later preparations. H192A retains signal,
and the historical efficiency table does not support greater WT kcat/Km.
Whole-cell assays lack independently verified clonal alleles/complementation;
probe readouts, crude fractions, basal MDA and drug-conditioned metabolic
viability remain separate endpoints. No raw-data refit or exhaustive survey is
claimed. The installed causal skill validates and repository/skill reads pass
without escalation; no permission configuration was changed on this retry.

For PF01876, original Stolc1997 Figures1/2/4/5/6/7, Chen2010 Figures3/4/7,
Chen2012 Figures1/2 and Hamasaki2015/2016 Figures2/5 were inspected with
relevant Methods and tables. The public Chen2010 supplement supplied cloning,
primer, identity and kinetic-control details. Pho supplementary retrieval returned
XML or download-preparation HTML, and the publisher returned403; SupplementS3
was not inspected. Earlier2008/2011 Methods were read for protocol context,
not treated as additional independently reviewed experiments. Exact reference
sequences and member-specific domain intervals were checked separately.
The IP150/IP600 wash discrepancy, printed BSA unit, Pho affinity arithmetic,
K196A specificity cell and earlier-method mixing/reference details remain open.
FC0 excludes unreacted RNA; improved fidelity is not complete product yield.
R107A retains activity and does not establish a chemical catalytic residue.
The fitted SPR comparison uses different models; no observed chaperone trajectory
is claimed. RNA abundance is not a measured half-life, and growth effects do not
identify a lethal molecular intermediate. Additional members and exact constructs
remain follow-ups. Skill validation and repository/skill reads passed on retry
without changing permission configuration.

For PF01877, Luz2010 Methods/Results and original Figures1-4 were inspected.
The protein-dose titration and probe comparisons use high nominal protein excess
and a bound/free RNA ratio; the largest plotted ratio is not fractional occupancy.
Sequence and predicted RNA folding change together, and all probes show some
shifted signal. Trypsin removes unspecified native N-terminal residues; printed
trypsin concentrations, exact active preparation and replicate statistics remain
unresolved. Reference sequences and the 9-132 domain interval were verified,
but no exact assay-batch sequence was established. K133 in the proposed basic
patch is outside the match and none of the suggested contacts was mutated here.
Rao2008 relevant Methods, surface analysis, quaternary structure and conclusions
were read with captions, not independent figure inspection. Its prediction is
not a matched negative binding assay. Miyazono2009 full text returned403 and
remains a coverage limit; metadata and the primary 3D7A deposition are not proof
of a functional dimer requirement. The relevant Lai2010 paragraph supports
genomic context, not a DUF54-specific response to proteinase treatment.
No raw-data refit, exhaustive member survey or experimental replication is claimed.

For PF01878, Toyota2012 original Figures1-5, Fujita2015 Figures6-8/S1/S2,
and Kitaura2019 Figures3/5/7/S2 were visually inspected with their Methods.
Fujita TableS2 was read; its Figure9 and Kitaura S1 original images were not
visually inspected. The retained edges preserve clone6's higher secondary-
necrotic24h fraction, unspecified Figure3A timing, baseline p27/fluorescence
differences, pooled-clone blots, residual Pax5 transcripts, reused rescue lanes,
nonexpressing rescue clones and incomplete location-specific ChIP recovery.
Mouse knockout/human-cell negatives are not evidence that challenged WEHI
overexpression has no effect. Raji uses CRISPR despite main-text wording.
The VcaM4I RCSB-linked homolog differs at13 positions and only reports HNH_2;
this does not resolve the studied enzyme's exact PF01878 membership. Remaining
modified-base and restriction-enzyme leads are explicitly uncurated. Publisher
PDF and PLOS supplementary downloads succeeded; alternate PDF endpoints returned
HTML/403. An offline uv cache restriction was resolved by approved rendering
retry, without changing filesystem permissions or repository configuration.

For PF01881, Carte2008 original Figures1/3/7, Carte2010 Figures2-5 and
Tables1/2, and Wang2011 Figures2/5 were visually inspected with primary
Methods/Results/Discussion. Versioned reference FASTAs and member-specific
PF01881/PF21350 mappings establish the domain boundary; 3I4H's tag plus
reference2-264 is exact, without claiming every assay batch was resequenced.
Other original images and supplements remain incomplete; the2011 DOC endpoint
returned challenge HTML rather than a document. The earlier linker claim is
explicitly revised, unshown M/N binding is not promoted to inspected data, and
the PF0393 noncatalytic label remains a lead pending primary functional review.
Repository and installed causal-skill reads and skill validation passed on retry;
the unavailable base-venv Biopython dependency worked in the existing offline
uv environment. No permissions were changed. All1831 family proteins remain
in scope beyond the three inspected PF1131 studies.

For PF01886, the Zhou2018 abstract and5VFK entry/entity/assembly metadata
were inspected, not the full paper or supplements. ScienceDirect returned403;
Elsevier and CAS supplied bibliographic information, not full text. The BMRB30279
summary and attempted STAR endpoint did not provide data; this is not a finding
of withdrawal or universal raw-data unavailability. Wang2024 selected energy/force
Results, simulation Methods, data availability and original Figure2 were inspected.
Its computational samples and multi-protein error averages are not DUF61
biological replicate measurements. The current196-entry UniProt query has no
FUNCTION comments, a bounded annotation observation rather than proof of absent
functional literature. Exact reference/construct sequences and the member-specific
Pfam interval are verified; all196 proteins counted in the frozen snapshot remain
within the family-coverage question. Repository and installed-skill reads and skill
validation succeeded, with no permission changes. A local endpoint-parser shape
error was corrected; it was not a filesystem-read denial.

For PF01889, Hong2025 relevant Results/Methods/Discussion and original
Figures2-5, plus Hong2026 Results/Discussion/relevant Experimental procedures
and original Figures2-5 were inspected. Exact reference sequences, member-specific
Pfam intervals, species/strain taxonomy and frozen DUF63 naming were checked.
The predicted AliA R138/R370 and AliB H56/H260 positions match the references,
but are not experimental residue tests. Both Stanford lipid-deposit metadata
records establish shared WT/double-mutant controls. Supplement attachments
returned challenge HTML or403; alternate endpoints encountered DNS,404 or429
failures. Complementation remains primary-text-only, not independently inspected
Supplementary Figure6. Raw lipid/proteomic/genome data, exact substrate inserts
and extended substrate tables were not independently reconstructed. These access
limits are not filesystem-read failures. Checkout and personal-skill reads and
skill validation succeeded without permission changes. All866 frozen family
proteins remain in scope beyond the inspected H53 experiments.

For PF01894, Kim2010 relevant main-text Results/Methods/Discussion, HTML
TablesI/II and original Figure1 were inspected. The original publisher DOC
supplement was recovered after initial access failures; relevant Methods and
TablesI-III/V were read, and FiguresS1/S4 and TablesIII/V were visually inspected
on rendered pages12,15,18,20. YjbQ colonies and vector controls have different
labeled times, not measured matched-time rates. Morett2008 remains limited to
the primary abstract and accessible Introduction/partial Methods; full kinetic,
mutagenesis and homolog evidence remains open. Selected RhiN and2024 tRNA-study
passages and ST2072 deposition metadata do not establish new YjbQ chemistry.
LibreOffice initially aborted and offline uv explicitly denied a package-cache
read; approved render-only/offline retries succeeded. These do not establish a
checkout-read failure, and no permissions were changed. All14125 frozen family
proteins remain in scope beyond the inspected E. coli experiments.

For PF01895, eleven original figures were inspected singly: Rice2009 Figure7,
Gardner2014 Figures5-7, Gardner2015 Figures2-5 and Seung2025 Figures6-8.
Methods, captions, selected Results/Discussion and construct tables bound the
adopted edges. Seven NCBI FASTAs exactly match the three UniProt references;
member-specific InterPro locations bound both repeats. Actual experimental
inserts were not independently resequenced. Europe PMC's2014 supplement request
returned an XML access response, not a ZIP; supplementary Mg/SEC plots remain
uninspected. New web-tool article opens hit a browser challenge, while retained
primary HTML/original images supplied the reviewed evidence. Ordinary repository
and skill reads passed, but sandboxed UV denied its package-cache marker; the
approved offline invocation succeeded without changing permissions. That error
is distinct from DNS and browser-access failures. Other structural homologs,
persistence and virulence studies remain evidence-research leads.

For PF01899, eight original images were inspected: Kajiyama2007 Figure1;
Morino2008 Figures1,2,4,5; Morino2010 Table1 at readable resolution using54
official zoom tiles; Steiner2020 Figure4 and Figure1-supplement1. The deposited
OF4 parent CDS and eight NCBI FASTA references were parsed and compared.
The2010 table exposes the pH9 T113Y exception and numerical differences from
the attributed2008 rows.2008/2010 supplemental endpoints returned HTML or XML
errors, not PDFs/ZIPs; deletion boundaries, supplementary growth curves and
blots remain uninspected.2022 structure text and polymer identity were reviewed,
not raw maps or figures.7QRU differs from the2008 MrpE parent at54,62,158.
The2025 histidine-switch paper and earlier S. aureus/R. meliloti/B. subtilis
studies remain leads. This is partial member-scoped evidence, not an exhaustive
family review or proof that every MrpE homolog has the same function.

For PF01900, sixteen original images were inspected: Chen2010 Figures3/4/7
and supplementTableS2; Chen2012 Figures1/2; Hamasaki2015 Figures2/5;
human2023 Figures3-7 and supplementS2; Panah2026 Figure2 and supplement2.
Relevant primary Methods/Results/tables and recovered supplementary methods
were read. The complete2023 SI ZIP succeeded after a prior transfer timed out;
the nominal direct PDF had returned HTML. Current UniProt and versioned NCBI
references match over all six proteins, but do not prove exact human transgene
sequences. Abstract-only2006/2013 mutation leads and unavailable2015 mutant
SPR sensorgrams remain open. Reused PF01876 evidence is not new replication.
An offline uv/Pillow rendering command reproduced an open error at its cache
marker; the approved single-command retry succeeded. Repository/skill reads
still worked, and no permissions or configuration were changed.

For PF01902, Su2012 Figures 3/4, Uthman2013 Figures 3/4/6/7, Lin2014 Figure 2
and Hawer2018 Figure 5 were visually inspected. Selected Results/Methods and
publisher DOCX tables Uthman S2/S3 and Hawer S1 were read or structurally parsed.
The tables establish independent double-mutant clones and distinct strain
backgrounds; they do not provide protein abundance or folding controls. The
Su2012 and Lin2014 supplement routes returned challenge HTML, a publisher 403
or an explicit non-open-access-subset response; those supplements were not
inspected. The later Dph7 substrate-processing experiment qualifies an older
pathway model but is not silently reassigned as a PF01902 intervention. B12
salvage, structural docking and cofitness remain leads, not observed catalytic
steps. No raw growth, mass-spectrometry or clone-sequence reanalysis is claimed.

For PF01904, Konc2013 Figure 5, Ogrizek2016 Figures 1-5 and both one-page
Babu2014 Protocols S2/S16 were visually inspected. Three primary XLS tables
were converted with existing LibreOffice and parsed as ZIP/XML; all 21 exact
YecE recipient rows, score strings, directions and locators match the overlay.
Tables S1/S16 identify the selected non-essential donors as new Hfr Cavalli
deletion::Cm strains, not independent historical replications. Both computational
papers' DOC supplements were text/table-parsed; conversion dropped their images,
so supplementary plots were not visually checked. Five of 48 model coordinate
subsets were parsed, not rerun as quantum calculations or full trajectories.
DNA restraints, initial neutral lysine, ion assumptions and relative potential
energy versus free-energy distinctions remain explicit. YunF expression,
beta-clamp motifs, cofitness and prophage insertion at the yecE locus are not
adopted as protein mechanisms. No exhaustive all-member or raw-colony review.

For PF01905, eight original main figures were visually inspected: Lintner2011
Figures 3/4, Reeks2013 Figure 2, Rajagopalan2015 Figures 2/3/4 and
Rajagopalan2017 Figures 2/8. All thirteen Lintner supplement pages were
text-extracted; pages 2/9/11 were rendered and visually inspected, including
S1, Table S3 and construct methods. PDB 3PS0 sequence and current domain
mapping retain native H160 without inferring a direct RNA contact. The
anisotropy Kd's 0.14 uM uncertainty is fit error, not the plotted SEM.
DevR CFU combines heat/sonication resistance, germination and colony formation;
the 24 h RNA probe differs from the Figure 4A junction probe. Reconstructed
devT mutants qualify the older separate-role inference, while the antisense
observation remains unpublished. The 2015 supplement was unavailable through
attempted endpoints; Reeks2013 supplementary sequences, Hu2022 full text and
later structural manuscript/construct contexts remain incomplete. These are
coverage limits, not biological negatives or proof that no later paper exists.

For PF01906, all ten YbjQ rows in the primary Babu2014 Table S2 were parsed
and compared with the graph's exact scores, donors, joint-genotype nodes and
polarity. Tables S1/S16 establish donor provenance; Protocols S2/S16 were
visually inspected. Marino-Ramirez2004 Figure 1, Lien2021 Figure 1 and
the 2025 Barto/Reddick showcase page 3 were also visually inspected. The
original YbjQ fusion clone and its controls remain unavailable. Lien's
published supplement Key and RVBD_1762c row 1802 were parsed, and the author
response confirms removal of the separate individual-mutant result. Nichols
Figure 3.5F and Bomponis retron Figure 19 remain uninspected access-limited
leads, not observed edges. The related Bobonis2022 main HTML was searched
without a YbjQ occurrence; supplementary coverage was not exhaustive. No raw
colony/WIG reanalysis, complete construct mapping or all-member review is claimed.

Publication, source checkpoint capture and a full site regeneration have not been
performed. They must follow the existing source-pin workflow when authorized.
The earlier full test run encountered this gate in the renderer: the published
pin for a newly curated family does not match its current bytes. Do not bypass
the guard or describe the local preview as a published, fully QC-passed site.

Verification at the PF01955 checkpoint (latest PF01956 checks are recorded below):

- Final native `dufmech.records.load_records` reconstructs, validates and checks
  all 8,296 projections with zero generated differences after the latest canonical
  history events are projected; the inventory is generated from this checked set.
- All 8,296 inventory semantic digests match the current projections after the
  history updates; this does not imply scientific coverage of all records.
- All 124 latest scoped scientific reviews match current record digests and
  retained overlay/evidence hashes. PF01955's `20261012T130729Z` successor binds
  all 17 evidence ledgers and covers the native-salvage and 2008 extensions.
  Access returned during native review retention without permission changes.
  These remain partial self-reviews, not complete scientific approval.
- The expanded graph/record/review/history/structured-review/projection-binding
  suite passed 256 tests, including the shared review contract.
- The current export suite passed 38 tests, including real-artifact
  reproducibility and shared KGX/SSSOM contracts. One upstream LinkML
  deprecation warning remains; identity exports do not include causal edges.
  An earlier run overlapped record regeneration and correctly detected changing
  corpus bytes; the successful rerun occurred after all projection writes ended.
  The CbiS checkpoint passed all 294 tests in 186.47 seconds. The newer
  Rhodobacter checkpoint ran after all projection writers ended: 292 passed
  and two Git-provenance contract tests failed in 138.70 seconds because the
  original checkout became unreadable. Both failures are in
  `tests/test_record_review_contract.py` (`test_review_skill_routes_and_rubrics_exist`
  and `test_every_saved_structured_bundle_is_valid`). This is not a green suite;
  these were failed historical checkpoints, not a green suite.
  The newer native-salvage checkpoint reran the same 294 tests after all record
  writers completed: 292 passed, the same two Git-provenance checks failed,
  and one warning remained in 156.67 seconds. No checks were excluded.
  After access returned and both new REVIEW events were projected, the same
  294-test suite passed completely in 158.00 seconds, with one upstream LinkML
  deprecation warning. This includes the two formerly blocked contract tests.
- The initial full suite had 1,316 passes, three skips and four failures: the
  source-pin gate plus three local-environment failures. After an offline locked
  environment sync and explicit `CLAW_SRC`, all 74 recipe/source-governance tests
  passed, including the three failed recipes. A second full-suite pass is not
  claimed; the initial run's three skips are not counted as passes.
- Current native checks validate 148 retained reports and 284 canonical history
  files; shared validation checks 140 structured bundles with declared scopes.
  The restored Git-dependent preservation check passes all 8,296 inventory
  digests, all 124 latest review/evidence bindings and exact overlay/rendered
  JSON matches. Imported fields equal `HEAD`; generated family changes belong
  exactly to the 124 overlays and manifest. Frozen worklists and configuration
  are unchanged. The supplemental check confirms PF01955's previous sixteen
  graphs and fourteen evidence ledgers are unchanged. Earlier access-blocked
  checkpoints remain documented below, not the current verification state.
- The previous all-curated-pages Chromium sweep checked all 1,454 edge entries at1440px
  and390px across
  one hundred and eighteen graph-bearing families and the graphless
  PF01629/PF01724/PF01886/PF01954/PF02621/PF20352 discussions,
  unique anchors, opening/closing evidence and no page-wide horizontal overflow
  or JavaScript errors. PleD's feedback explanation and RtcB's one inferred/three
  observed support labels are checked explicitly; all 124 rendered JSON
  records exactly match current YAML. TusA's unresolved edge, DUF16/DUF19's four
  indirect labels and DUF58's two indirect labels are checked separately.
  The native-salvage checkpoint separately reran PF01955 at both widths with
  forty-three edges, forty-two OBSERVED/one INFERRED labels, eleven DIRECT/thirty-two
  UNRESOLVED effects, exact domain mappings, joint-gene and AP contexts,
  primer/genotype/protocol discrepancies, phosphatase-attribution limits,
  retained tags, buffer confounding and distinct cellular contexts are checked
  explicitly in the current browser script. The cross-figure inference,
  conditional Cby/CobY bypass and native source discrepancies are also checked.
  Eight new heading/evidence screenshots were visually inspected. This targeted
  rerun is not claimed as a repeat of all 124 pages at the newer 1,459-edge total.
  The latest targeted PF01955 rerun passes at both widths with 66 edges,
  65 OBSERVED/one INFERRED and eleven DIRECT/55 UNRESOLVED effects. Candidate
  versus historical clone identity, the actual cobD lesion, midpoint versus
  endpoint effects, mixed-extract scope and source contradictions are checked.
  Four new desktop heading and four mobile evidence screenshots were visually
  inspected. No page-wide overflow or JavaScript errors were detected. This is
  not an all-124-page browser sweep at the current 1,482-edge corpus total.
  TycB1's four direct labels and unresolved phenylalanine unit, and HAMP's three
  indirect labels and distinct UU1250/UU1535 contexts, are checked explicitly.
  EamA's three indirect labels and two-repeat mapping, and EmrE's five direct
  labels, opposite-potential contexts and coupling qualification, are checked.
  TatC's five direct labels, tagged construct and native-vesicle qualification,
  and MscS's six direct labels, distinct domain boundaries, double mutant and
  Ficoll conditions, are checked explicitly.
  TatD's six direct/one indirect labels and tagged/untagged substrate contexts,
  and YetJ's two direct labels, pH qualification and missing supplementary
  conditions, are checked explicitly.
  RidA's nine direct labels, high-pH timing and addition-order qualification,
  and TTR-52's three direct/three indirect labels, distinct alleles, deposited
  sequence, nested sampling and mutant-label discrepancy, are checked explicitly.
  BEST1's eight direct/observed labels, historical reference, processed start,
  normalization and mixed orientations, and CoaE's five observed/one contested
  labels, separate turnover directions and clone-primer qualification, are checked.
  CoaE's contested row is visually checked at both viewport widths.
  IspD's eleven observed labels, six direct/five unresolved distinctions and
  proof/unpurified-screen limits, and Alr's seven direct observed labels,
  domain interval, Y265 exclusion, concentration discrepancy, missing displayed
  control and separate-vessel scope, are checked explicitly.
  Gdt1's eight observed labels, two direct/four unresolved/two indirect
  distinctions, repeat mapping, calibration discrepancy and time-specific
  phenotypes, and TilS's eight direct observed labels, primer match, separate
  enzyme preparations and carryover limits, are checked explicitly.
  Gdt1's unresolved row is visually checked at both viewport widths.
  SBDS's seven direct observed labels, mixed-species contexts, truncated eIF6,
  domain interval, outside-domain substitutions and separate-vessel scope,
  and PdxT's five direct observed labels, untagged strain-168 scope, SMY
  distinction, ammonium condition and unresolved kinetic/spectral details,
  are checked explicitly.
  Yih1's three indirect observed labels, C-terminal PF01205 interval, separate
  RWD domain, H1511/ESY11001b contexts and non-rescue qualification, and Dus2's
  five direct observed labels, domain interval, primer discrepancy, differing
  assay conditions and mixed-species preparations, are checked explicitly.
  UppS's one direct/two unresolved observed labels, archived-reference mapping,
  residual coupled-assay output and unshown product TLC, and NADHX repair's five
  direct observed labels, separate domain intervals, ATP/ADP contexts, unequal
  enzyme doses and intact-protein R-enriched mixture scope, are checked explicitly.
  UppS's unresolved row is visually checked at both viewport widths.
  CLIPPER's three direct observed labels, 708-828 construct and 712-812 domain,
  K715A/K517A and N748/D749 discrepancies, scan-repetition and tag-processing
  limits are checked explicitly. SufBD's five direct/two indirect observed
  labels, separate 225-466/166-393 domain mappings, basal output and retained
  sulfur, lower H360A abundance, unresolved plate glucose and distinct liquid
  supplementation are checked explicitly.
  GXGXG's two direct/one indirect observed labels, mature/reference domain
  coordinates, partial-domain deletion, beta tag and nonzero dilution salt,
  and NADK's five direct observed labels, N75 mapping, terminal-primer
  uncertainty, tripolyphosphate exception, residual WT activity, qualitative
  product conditions and expression-gel/kinetic-table limits, are checked.
  PPR's four direct observed labels, K426/N464 mapping, fusion context and
  expanded-evidence partial-rescue values, and ShK's two direct observed labels,
  qualified integrated-domain association, separate recombinant/synthetic
  contexts and functional current midpoints, are checked explicitly.
  NorM's five direct/one indirect observed labels, two-repeat mapping, residue
  offset, glucose discrepancy and detergent conditions, and TqsA's eight
  indirect observed labels, gene/domain scope, reporter identities, distinct
  complementation sampling and opposite LB response, are checked explicitly.
  CorB's eleven direct observed labels, two species/domain mappings, loading
  and magnesium series, SEC controls and DDM/UDM discrepancy, and HxlR's four
  direct/three indirect labels, extra-domain C11/K13, GSH/S2G qualifications,
  different titration/probe contexts and basal K13A signal, are checked explicitly.
  Gnk2's fourteen observed labels, four direct/ten indirect distinctions,
  precursor/mature boundaries, extra Met, factor-two SPR doses, residual
  delta-mnn2 delay, named fungal strains and unavailable visual supplement
  controls are checked explicitly. Its normal and expanded-edge screenshots
  were visually inspected at both widths; mobile edge tables scroll internally.
  SelR's six observed labels, two direct/four indirect distinctions, fly
  clone/isoform mapping and transferred interval, mouse U95C/Sec distinction,
  yeast reference grounding, peroxide contexts and residual/convergent growth
  are checked explicitly. Its normal and expanded-edge screenshots were visually
  inspected at both widths, with internal mobile table scrolling.
  Af1521's eight observed labels, seven direct/one unresolved distinctions,
  Pfam30-155 boundary, extra-domain substitutions, coupled TLC context,
  stoichiometry discrepancy, unwashed-NAD versus G50 protocols, partial
  demodification and unresolved dose/tag details are checked explicitly.
  Its normal, expanded-edge and unresolved-support screenshots were visually
  inspected at both widths; mobile edge tables scroll internally.
  Pmp3's fifteen indirect observed labels, yeast/plant coordinate mappings,
  three strain backgrounds, sodium-protocol conflict, no-added-KCl and joint
  EGTA/calcium qualifications, different normalization controls and partial
  chromosomal plant rescue are checked explicitly. Normal and expanded-edge
  screenshots were visually inspected at both widths; mobile tables scroll
  internally without page-wide overflow.
  PdxS's eleven direct observed labels, PF01680 interval and historical
  methionine numbering, shared-experiment qualification, K81/K149 distinctions,
  partner H170N/tag boundary, G3P dose and pH conflicts, partial conversion,
  nitrogen-free interpretation limit and off-pathway Z2 qualification are
  checked explicitly. Normal and expanded-edge screenshots were visually
  inspected at both widths; mobile tables scroll internally.
  GALT-1's fifteen observed labels, ten direct versus five indirect effects,
  whole-protein interval, crude-extract and unit limits, small donor signal,
  residual cofactors, joint rescue, distinct genotypes and selected glycome
  scope are checked explicitly. Normal and expanded-edge screenshots were
  visually inspected at both widths. An initial browser assertion looked for
  evidence text before opening its details panel; the corrected check verifies
  that content after opening, and the full desktop/mobile run passed.
  TACO1's fourteen observed labels, four direct versus ten indirect effects,
  mouse/human reference intervals, extra-domain groups, binding-tag boundary,
  Ile/Leu caption conflict, pulse isotope and emetine discrepancies, normalized
  occupancy/offset qualifications and incomplete three-Pro rescue are checked
  explicitly. Normal and expanded-edge screenshots were visually inspected
  at both widths; mobile tables scroll internally. Its first regeneration
  preview stopped before a CREATE history sidecar existed, after the initial
  history invocation omitted its required timestamp. The corrected history
  entry and subsequent guarded preview/apply/check completed successfully.
  MIP's twenty observed labels, eleven direct versus nine indirect effects,
  exact ACU/UniParc mapping, Y727/S759 numbering discrepancy, MIB-only
  dissociation controls, preincubation/serum-dose conflicts, non-rescue
  single-pair comparison, recode-matched ATPase mutant and unobserved reset
  mechanism are checked explicitly. Normal and expanded-edge screenshots
  were visually inspected at both widths; mobile edge tables scroll internally.
  OatA's twenty-two observed and two hypothetical labels, sixteen direct/six
  indirect/two unresolved distinctions, exact reference/Pfam mapping,
  extra-domain residues, MS lysine-mutant caveat, untreated Tyr206 acetylation,
  divergent Y136A assays and tunicamycin-dependent growth are checked explicitly.
  Normal, expanded-edge and hypothesis-label screenshots were visually inspected
  at both widths. An initial browser assertion queried assay values before
  opening their evidence panels; the corrected post-expansion assertion and
  full desktop/mobile run passed. No application code change was needed.
  RsmH's seventeen observed labels, five direct/twelve indirect distinctions,
  versioned reference/domain mapping, joint substrate/donor conditions,
  half-dose RNA comparator, retained cellular 2'-O mark, UGA textual conflict,
  reporter normalization and growth-rate polarity are checked explicitly.
  Normal and expanded-edge screenshots were visually inspected at both widths;
  mobile tables scroll internally without page-wide overflow. No application
  code changes were needed for this addition.
  YidD's twenty-one indirect observed labels, exact reference/domain mapping,
  partial-domain H1 boundary, tagged-induction dose, thesis-version and host
  discrepancies, fluorescence polarity, separate F0c endpoints and YidC
  compensation limits are checked explicitly. Normal and expanded-edge
  screenshots were visually inspected at both widths; mobile edge tables scroll
  internally. Its native projection and retained review digest agree after the
  REVIEW history update. No application code changes were needed.
  FOG-2's eight indirect observed labels, historical sequence reconstruction,
  current FTH/tail boundaries, ordinal reporter scores, retained SKR-1
  controls, FTR-1 length discrepancy, RNAi gonad-arm denominator, selected
  Table 2 genotyping and partial HA-tag suppression are checked explicitly.
  Normal and expanded-edge screenshots were visually inspected at both widths;
  mobile tables scroll internally without page-wide overflow. Its review
  digest remains current after history projection. An initial ad hoc validation
  command named a nonexistent helper; the corrected native FamilyCuration
  validation and guarded regeneration passed. No application code change
  was needed for this addition.
  BpsA's sixteen observed and one hypothetical labels, ten direct/six indirect/
  one unresolved distinctions, versioned references, primer-supported residue
  offset, historical WT kinetics, separate mass-shift/carrier claims, pdaD
  relocation, partial KPS compensation and conflicting image alt text are
  checked explicitly. Normal, expanded-edge and hypothesis-label screenshots
  were visually inspected at both widths; mobile tables scroll internally.
  Its saved review digest matches after REVIEW history projection, and all
  imported fields, remaining projection bytes and frozen inputs are preserved.
  No application code changes were needed for this addition.
  PvlArgDC's three direct observed labels and one unresolved hypothetical
  label, versioned reference, domain boundaries, residual His0, distinct assay
  and crystallization conditions, specific-activity units and failed processing
  comparison are checked explicitly. Both mutant residual activities and the
  N47A uncertainty gap remain visible. Normal, expanded-edge and hypothesis
  screenshots were inspected at both widths; mobile tables scroll internally.
  Exact reviewed content survives the REVIEW history projection. The review
  draft's missing bounded-search metadata and an incorrect history CLI flag
  were corrected before the successful native saves; no previous report was
  overwritten. No application code changes were needed for this addition.
  PF01863's three direct observed and two unresolved hypothetical labels,
  verified reference/domain mappings, K2V/L2V discrepancy, GP tag residues,
  missing YgjP assay context, distinct thermal endpoints and failed protease
  activation remain visible. Normal, expanded-edge and hypothesis-label
  screenshots were inspected at both widths; mobile tables scroll internally.
  Its exact review digest survives REVIEW history projection. An initial
  unsupported predicate spelling was corrected to native `decreases` before
  projection. No schema or application code changes were needed.
  PF01864's nineteen direct observed and two unresolved hypothetical labels,
  versioned reference, Pfam12-174, His-tag tail and primary expression host are
  checked explicitly. CTP carryover, outside-domain D8/W9, separate 25/4/90 C
  assay contexts and individually tested mutation groups remain visible.
  Expanded evidence retains TableS2 units, P31A product despite undetected ITC,
  W9A residual output and Q123A/H157A opposite strip/product effects without
  inventing a measured release step. Normal, expanded-edge and hypothesis
  screenshots were inspected at both widths; mobile tables scroll internally.
  Its exact review digest survives REVIEW history projection. No schema or
  application code changes were needed for this addition. The installed
  causal-graph skill's filesystem reads and skill validator also passed on retry.
  PF01865's seventeen indirect observed labels and eight phenotypic graph
  scopes are checked explicitly, together with both exact reference/domain
  mappings, operon-only rescue, separate single/double mutants, phoU::erm and
  Pi concentration contexts. Expanded evidence preserves 3.48 versus0.78
  operon uptake, nonzero R78A and D90A/H96Y values and the polyP-inclusive
  readout. Normal and expanded-edge screenshots were visually inspected at
  both widths; mobile edge tables scroll internally. All current review
  digests and retained inputs match after REVIEW history projection.
  No schema or application code changes were needed for this addition.
  Offline PDF rendering needed approved access to uv's cached dependency;
  this specific cache denial did not prevent repository or skill reads.
  PF01867's fourteen observed labels, nine direct/five indirect distinctions,
  exact reference and narrow Pfam mapping, outside-match interface variants,
  K224A assay discordance and IHF-absent topology scope are checked explicitly.
  Cas2 enhancement is not necessity, and synthetic Y-DNA donor release is not
  joined to plasmid BandX as an observed trajectory. The ED5 image mismatch
  remains visible. Normal and expanded-edge screenshots were inspected at
  both widths; mobile tables scroll internally. Its reviewed semantic digest
  survives the canonical REVIEW history projection. No application or schema
  changes were needed. A malformed ad hoc inspection command was corrected
  before the successful native review save; no earlier report was overwritten.
  PF01868's twelve direct observed labels, three reference/domain mappings,
  outside-domain truncations and unresolved terminal-primer discrepancy are
  checked explicitly. Composite-protocol scope, normalized versus raw rates,
  residual57/56/8/4% activity, unchanged pair kobs and incomplete61% yield
  remain visible. Normal and expanded-edge screenshots were inspected at
  both widths; mobile tables scroll internally. Its exact reviewed semantic
  digest survives REVIEW history projection. No application or schema changes
  were needed. All87 current review digests and retained evidence/overlay
  hashes match, and all8296 inventory entries match current projections.
  PF01870's sixteen observed labels, thirteen direct and three indirect effects,
  two reference/domain mappings, outside-domain T138, Hje-intact E233S context,
  unresolved kinase dose and phosphomimetic/repair-endpoint limits are checked
  explicitly. Normal and expanded-edge screenshots were inspected at both widths;
  mobile tables scroll internally. Its reviewed digest survives the two-event
  history projection. A scalar node-grounding field was corrected to the native
  list shape before successful generation and review; no schema change was made.
  PF01871's nine indirect observed labels, six phenotypic scopes, three exact
  reference/domain mappings, nuclear retention, dose/manuscript distinctions,
  partial tail rescue and negative marker comparisons are checked explicitly.
  Normal and expanded-edge screenshots were visually inspected at both widths;
  mobile edge tables scroll internally. Its reviewed digest remains current
  after the two-event history projection. The DOI prefix and human quotation
  were corrected before the retained review. No schema or application code
  changes were needed for this addition. Frozen inputs and the remaining
  8,209 projection bytes are unchanged.
  PF01875's sixteen observed labels, six direct/ten indirect distinctions,
  eleven scopes, exact reference/domain mapping and deposited4-297 construct
  are checked explicitly. BCA and wavelength discrepancies, residual H192A
  signal, basal knockdown effects, crude iron fractions and the higher-MDA/
  lower-iron distinction remain visible. Expanded evidence retains all four
  primary references, coupled-assay limits, conditional drug-dose effects and
  the distinction between historical Km and binding Kd. Normal and expanded
  screenshots were visually inspected at both widths; mobile tables scroll
  internally. The semantic review digest survives the two-event history
  projection. No schema or application code changes were needed.
  PF01876's twenty-four observed labels, fifteen direct/nine indirect distinctions,
  fifteen scopes and five exact reference mappings are checked explicitly.
  Composite protocols, IP150/IP600 and BSA discrepancies, missing SupplementS3,
  residual R107A activity and incomplete61% product amplitude remain visible.
  Expanded evidence preserves all four primary references and excludes isolated
  p30 catalysis, a measured KM-as-Kd interpretation and exclusive RNaseP activity
  in mixed preparations. Normal and expanded screenshots were visually inspected
  at both widths; mobile tables scroll internally. Its exact review digest survives
  the two-event history projection. No schema or application changes were needed.
  The latest focused suite passed256 tests and the export suite passed38 tests
  after projection and export writes completed, with the known LinkML warning.
  PF01877's three direct observed labels and two scopes are checked explicitly,
  together with exact reference mapping, uncertain tryptic termini, the outside-
  match K133 and combined sequence/structure intervention. Expanded evidence
  preserves the 2.5-20-uM protein range, bound/free rather than total occupancy,
  weak nonzero UUA/C binding and shared-experiment scope. Normal and expanded
  screenshots were visually inspected at both widths; mobile tables scroll
  internally. Its reviewed digest survives the two-event history projection.
  All87 current review hashes and all8296 inventory entries match. No schema or
  application changes were needed. The focused suite passed256 tests, and the
  export suite passed38 tests after all generated writes, with the known warning.
  PF01878's seventeen indirect observed labels and nine phenotypic scopes are
  checked explicitly, together with reference/domain mapping, unresolved insert
  identity, the outside-domain chicken reference difference and VcaM4I mapping
  limit. Expanded evidence preserves the clone-specific negative comparison,
  baseline differences, residual Pax5 output, incomplete ChIP rescue and the
  distinction between MYH9 and the EVE-bearing protein. Normal and expanded
  screenshots were visually inspected at both widths; mobile tables scroll
  internally. Its reviewed digest survives the two-event history projection.
  All88 current review digests and all8296 inventory entries match; frozen
  inputs and the other8208 projections are unchanged. The focused suite passed
  256 tests, and the export suite passed38 tests after all generated writes,
  with the known upstream LinkML warning. The initial history command's actor enum was corrected before
  successful history creation and guarded regeneration; no schema was changed.
  No application-code changes were needed for this addition.
  PF01881's sixteen direct observed and one unresolved hypothetical labels,
  eight scopes, exact reference/domain mapping and outside-domain N-terminal
  substitutions are checked explicitly. Joint four-glycine mutation scope,
  residual K52A output, reported-but-unshown binding, tolerated linker edits,
  conditional deoxy-site rerouting and the DTT discrepancy remain visible.
  Normal, expanded-edge and hypothesis screenshots were visually inspected at
  both widths; mobile tables scroll internally. Its semantic review digest
  survives REVIEW history projection. All89 current review digests and retained
  input hashes match, as do all8296 inventory entries; the other8207 projections
  and frozen sources are unchanged. The focused suite passed256 tests, and the
  export suite passed38 tests after all generated writes completed, with the
  known upstream LinkML warning. No application or schema changes were needed
  for this addition.
  PF01886's graphless state and explicit functional-evidence prerequisite are
  checked at both widths. Reference/domain/construct scope, incomplete full-paper
  access and computational-benchmark limits remain visible. Its desktop/mobile
  evidence-gap screenshots were visually inspected; neither has page-wide
  horizontal overflow. The semantic review digest survives REVIEW history
  projection. All90 current review digests and retained input hashes match,
  as do all8296 inventory entries; frozen sources and the other8206 projections
  are unchanged. The focused suite passed256 tests, and the export suite passed
  38 tests after all generated writes, with the known upstream LinkML warning.
  No application or schema changes were needed for this graphless addition.
  PF01889's nine graph scopes and34 indirect observed labels are checked at
  both widths. Exact paralog/domain mapping, substrate-specific residual effects,
  shared lipid controls, nonsignificant comparisons and tagged/endogenous
  disagreement remain visible. Normal and expanded-edge screenshots were
  visually inspected at both widths; mobile tables scroll internally. The first
  browser attempt rejected an over-specific test phrase; the assertion was
  corrected to the retained limitation without changing the scientific record.
  Its semantic review digest survives REVIEW history projection. All91 current
  review digests and retained input hashes match, as do all8296 inventory
  entries; frozen sources and the other8205 projections are unchanged. The
  focused suite passed256 tests, and the export suite passed38 tests after
  all generated writes, with the known upstream LinkML warning. All three
  documented export byte counts and hashes match the regenerated artifacts.
  No application or schema changes were needed for this addition. Current
  checkout and installed-skill reads and skill validation pass; the earlier
  filesystem-read denial was not reproduced and no permissions were changed.
  PF01894's three phenotypic scopes and five indirect observed labels are
  checked at both widths, including exact reference mapping, serine-only context,
  printed-primer and antibiotic limits, unmatched plate times and unassayed
  dehydrogenase status. Expanded evidence preserves both primary studies and
  the distinction between supplementary chemical growth curves and the text-only
  YjbQ liquid result. Normal and expanded-edge screenshots were visually inspected
  at both widths; mobile tables scroll internally. Its semantic review digest
  survives the three-event CREATE/EDIT/REVIEW projection. All92 latest review
  digests and evidence hashes and all8296 inventory entries match; frozen
  worklists, configuration and the other8204 projections are unchanged.
  An intermediate dry run caught a cache hash awaiting refresh after evidence
  edits; updated hashes passed guarded generation. The inventory CLI initially
  printed the new inventory without saving it, so the native inventory function
  regenerated the saved JSON before the exact comparison passed. The focused
  suite passed256 tests and the export suite passed38 after all generated writes,
  with the known LinkML warning. Documented export sizes and hashes match.
  No schema or application changes were needed for this family, and no
  publication, source-pin capture or full-QC pass is claimed.
  PF01895's twelve graph scopes and24 observed labels (four direct and20
  indirect) are checked at both widths. Exact three-member/two-repeat mapping,
  unequal fluorescence doses, plasmid/integrant behavior, missing R148E-PstB
  data, conjunctions and unchanged autokinase output remain visible. Normal
  and expanded-edge screenshots were visually inspected at both widths;
  mobile tables scroll internally. Its current semantic digest survives the
  CREATE/EDIT/REVIEW projection. Self-review corrected a sentence that could
  confuse retained assay components with separately tested necessity. An
  initial assessment-input YAML colon error was repaired before the native
  review saver succeeded; no retained report was overwritten. All93 current
  scientific review digests and evidence hashes match, as do all8296 inventory
  digests and93 rendered JSON records. The other8203 projections and frozen
  worklists/configuration are unchanged. The focused suite was rerun after
  the final prose change and passed256 tests; the export suite passed38 with
  the known LinkML warning after all generated writes ended. Documented export
  hashes and byte counts match. No schema/application changes, permission
  changes, publication, source-pin capture or full-QC pass are claimed.
  PF01899's nine phenotypic scopes and twelve indirect observed labels are
  checked at both widths, including exact OF4 deposited-parent mapping,
  historical B. subtilis sequence uncertainty, distinct salt conditions,
  coupled vesicle readouts, apparent-Km versus Kd and source discrepancies.
  Expanded evidence preserves the pH9 T113Y11.8%-of-parent exception. An initial
  browser assertion looked for that detail before opening its evidence panel;
  moving it to the expanded-panel check fixed the test without changing the
  scientific record. Normal and expanded-edge screenshots were visually
  inspected at1440px and390px; mobile tables scroll internally.
  CREATE/REVIEW history projection preserves semantic digest
  `b3abd4ca3fcd6539dc777991398362bf70f848550675f5d068dd920da198e5d0`.
  All94 latest review digests and evidence hashes match, as do all8296 inventory
  digests and94 rendered JSON records. The other8202 projections and frozen
  worklists/configuration are unchanged. The focused suite passed256 tests;
  the export suite passed38 after all generated writes, with the known LinkML
  warning. All documented export byte counts and hashes match. New authoring,
  evidence, history and report files are not ignored. No schema/application
  change, publication, source-pin capture or full-QC pass is claimed.
  PF01900's nineteen scopes and35 observed labels are checked at both widths,
  including3 direct,14 unresolved and18 indirect edges, all six reference
  mappings, joint ionic protocols, retained loop-mutant binding, the lack of a
  Figure4C40-minute increase, residual RPP14 mRNA and upstream-background rescue.
  Normal and expanded-edge screenshots were visually inspected at1440px and390px;
  mobile tables scroll internally. CREATE/REVIEW projection preserves digest
  `ebb83480db23e6496c1105dccf1b2bb13efac5401a187cde487575d11225bc77`.
  All95 current review digests and retained source hashes match, as do all8296
  inventory entries and95 rendered JSON records. The other8201 projections and
  frozen worklists/configuration remain unchanged. Focused tests passed256;
  exports passed38 after every generated write completed, with the known
  upstream LinkML warning. Documented export bytes/hashes and the README corpus
  check pass. Native validation covers108 reviews,100 structured bundles and202
  history files. Initial review-input evidence typing was corrected to the
  supported search kind with an explicit bounded scope before retention; no
  prior report was overwritten. New files are not ignored and diff checking
  passes. No schema/application changes, publication, source-pin capture or
  full publication-QC pass are claimed.
  The initial PF01901 pass checked four PHENOTYPIC scopes and four OBSERVED/INDIRECT labels
  at both widths,including Q8X4T7/AIG69277.1,8-205,score0.041,the ATCC700927 versus
  ATCC43895 distinction,missing Wzy rescue,glucose/time discrepancies and the
  lack of an invasion-defect claim. Five original source images were inspected
  (2020Figure1;2024Figures1/2/4/5),as were normal and expanded-edge screenshots
  at1440px and390px. Mobile tables scroll internally. CREATE/REVIEW projection
  preserves digest
  `5e426dd11dd4188aad4bf639eae76e14d76358ee04b5d7984c7c3dbedc950516`.
  All96 latest review digests and retained evidence hashes match;all8296
  inventory entries and96rendered JSON records are exact. The other8200
  projections and frozen worklists/configuration are unchanged. Focused tests
  passed256;exports passed38 after all generated writes,with the known upstream
  LinkML warning. Native checks cover109reports,101structured bundles and204
  history files. Documented export bytes/hashes and the README corpus check
  pass. New files are not ignored and diff checking passes. Repository/skill
  reads and offline UV/Biopython worked normally; Chromium again required its
  scoped approved retry after Mach-port startup was denied. No global permission
  fix,permission-config edit,schema/application change,publication,source-pin
  capture or full publication-QC pass is claimed for this family pass.
  The successor PF01901 follow-up checks seven scopes and eight OBSERVED/INDIRECT
  labels at both widths, including known ATCC lineage, distinct SK2526 and43888
  backgrounds, QDZ55367.1 mapping, actual Figure4C and no cross-strain rescue.
  Capsule/LPS and phage graph-heading and expanded-edge screenshots were visually
  inspected at1440px and390px; mobile tables retain internal horizontal scrolling.
  EDIT/REVIEW projection preserves semantic digest
  `18b72f171e4f8e5944b53ffa944d5adcf36a77d2763d96b13a4ee0e9372ec331`.
  All8296 projections validate without drift; schema generation also has no drift.
  All96 current review digests and retained source hashes,8296 inventory entries
  and96 rendered JSON records match. The earlier PF01901 review's five evidence
  hashes remain unchanged. The other8200 projections, frozen worklists and
  configuration are untouched. Focused tests passed256; exports passed38 after
  all generated writes, with one known LinkML deprecation warning. Native checks
  validate110 reports and206 history files; shared validation covers102 bundles.
  Export bytes/hashes and README corpus checks pass. New files are not ignored,
  diff checking passes, and the original checkout is unchanged. Repository/skill
  reads and offline UV/Pillow now pass without escalation; Chromium needed its
  separately approved Mach-port retry. No permission changes, publication,
  source-pin capture, exhaustive family review or full publication-QC pass.
- PF01902 adds nine scoped graphs with twelve OBSERVED and two HYPOTHESIZED
  edges. Desktop/mobile checks verify four DIRECT, eight INDIRECT and two
  UNRESOLVED labels, the two current protein mappings, combined distal mutant,
  reporter-name discrepancy, conditional growth and unobserved chemical steps.
  Graph-heading, expanded-edge and hypothesis screenshots were visually
  inspected at 1440px and 390px; mobile tables scroll internally. CREATE/REVIEW
  projection preserves semantic digest
  `21ec7903520a0e45252648df59890ad8829fe61aa1c3bfd26aa4fb059678128f`.
  All 8,296 projections validate without drift; schema generation also has no
  drift. All 97 latest review digests and retained source hashes, 8,296 inventory
  entries and 97 rendered JSON records match. Frozen worklists, configuration
  and the other 8,199 projections are unchanged. Focused tests passed 256;
  exports passed 38 after all generated writes, with one known LinkML warning.
  Native checks validate 111 reports and 208 history files; shared validation
  covers 103 bundles. Export byte/hash documentation and README corpus checks
  pass. New artifacts are not ignored and diff checking passes. Repository and
  skill reads, cache-marker metadata and offline UV/Pillow work without
  escalation. Chromium again failed at sandboxed Mach-port registration with
  error 1100 and required a narrowly approved command retry. No permission or
  source-pin change, publication, exhaustive family review or full QC is claimed.
  Relation labels remain on one line. New-family screenshots
  were visually inspected. Chromium needed an approved retry after its
  sandboxed Mach-port startup was denied; the retry completed successfully.
  This was a browser-startup restriction, not a filesystem-read failure. Scoped
  previews are under `/private/tmp/dufmech-causal-preview/families/`.
- PF01904 adds two scoped graphs with 21 OBSERVED/INDIRECT/EXPERIMENTAL and
  two HYPOTHESIZED/UNRESOLVED/COMPUTATIONAL edges. All 21 primary Table S2
  YecE rows match the overlay's partner, score, direction and locator. Desktop
  and mobile checks preserve the multiplicative comparator, separate Hfr/Keio
  and Tm1631 systems, model Lys73/native K72 mapping and absence of experimental
  nuclease claims. Graph-heading, expanded-edge and hypothesis screenshots were
  visually inspected at 1440px and 390px; mobile tables scroll internally.
  CREATE/REVIEW projection preserves semantic digest
  `2d29ac3a5a2b7c6a0bb314f77cf7c20e15fe922c710584ad9454ce13a6ccc1cd`.
  All 8,296 projections validate without drift and schema generation has no
  drift. All 98 latest review digests and retained source hashes, 8,296 inventory
  entries and 98 rendered JSON records match. The other 8,198 projections,
  frozen worklists and configuration are unchanged. The focused suite passed
  256 tests before this family curation; the export suite passed 38 after all
  generated writes, with one known LinkML warning. Native checks validate 112
  reports and 210 history files; shared validation covers 104 bundles. Export
  byte/hash documentation and the README corpus check pass. New artifacts are
  not ignored, diff checking passes and the original checkout is preserved.
  The browser retry completed all 98 pages and 758 evidence toggles at each
  width. No publication, source-pin capture, exhaustive family review or full
  publication-QC pass is claimed.

  Access diagnostics distinguish readable files from commands that need writes.
  Repository/skill reads and direct `stat`/`head` on the empty UV cache marker
  succeed. A normal offline PDF dependency command still fails opening
  `/Users/marcin/.cache/uv/sdists-v9/.git`; the earlier narrowly approved PDF
  rendering command succeeded. The installed `uv 0.6.13` initializes that marker
  with create/write access even when it exists, as verified in its
  [versioned cache implementation](https://github.com/astral-sh/uv/blob/0.6.13/crates/uv-cache/src/lib.rs#L325-L335).
  This explains the command's failure as a cache-write restriction, not evidence
  that ordinary repository reads are denied. Prefer the existing project Python
  when its dependencies suffice, or a narrowly approved required UV command;
  no global permissions or cache configuration were changed. Separately,
  Chromium's normal launch failed at Mach-port registration (1100), and its
  approved retry passed. Public CDN and LibreOffice retries are recorded in the
  research ledger. No global filesystem-access fix is claimed.
- PF01905 adds eleven graphs with fourteen OBSERVED/EXPERIMENTAL edges,
  six DIRECT binding effects and eight INDIRECT phenotypes. CREATE/REVIEW
  history projection preserves semantic digest
  `da5bd67ca8bdd47baa6a425e27619c9fa9fa475581fea6a915b12b7afdb5244e`.
  The native record check validates all 8,296 projections with zero drift;
  schema generation has zero drift. All 99 latest review digests and retained
  source hashes, all 8,296 inventory digests and all 99 rendered JSON records
  match. Imported identities, frozen worklists, configuration and the other
  8,197 projections are unchanged. The focused suite passed 256 tests before
  curation; the post-write export suite passed 38 with one known LinkML warning.
  Native checks validate 113 reviews and 212 history files; shared validation
  covers 105 bundles. Export byte/hash documentation and the README corpus
  check pass. New artifacts are not ignored and the original checkout is
  preserved. No source-pin capture, publication, exhaustive family review or
  full publication-QC pass is claimed.

  Retried repository/skill reads, direct reading of the UV marker and standalone
  offline UV/Biopython all succeed. This does not claim that every cache-writing
  command is now unrestricted. Chromium still fails sandboxed Mach-port
  registration (1100) and needs a narrowly approved local preview check; no
  global permission or cache configuration was changed.
  The approved browser run completed all 99 pages and all 772 evidence toggles
  at each of 1440px and 390px, with unique anchors, no page-wide horizontal
  overflow and no JavaScript errors. PF01905 checks distinguish six DIRECT
  from eight INDIRECT labels, the two domain intervals, H160A residual signal,
  probe/temperature differences, fit error versus SEM, composite spore CFU,
  suppression rather than DevR complementation and RNA abundance rather than
  direct repression. Csa2 and DevR graph-heading and expanded-edge screenshots
  were visually inspected at both widths; mobile tables scroll internally.
- PF01906 adds one PHENOTYPIC graph with ten OBSERVED, INDIRECT, EXPERIMENTAL
  edges. All ten exact primary rows, scores, donor identities, joint-genotype
  labels and six-increase/four-decrease directions match the authored graph.
  Three OPEN discussions retain assay/construct/member gaps, the uninspected
  retron source and qualified Rv1762c evidence. CREATE/REVIEW projection retains
  semantic digest
  `9b8b1ff8c2f82f09a230d56cba81231cbfafa75b0705d1eb8dd35c45eb6c3514`.
  All 8,296 records validate with zero generated drift; schema generation has
  zero drift. All 100 latest review digests and retained source hashes, all
  inventory digests and all 100 rendered JSON records match current projections.
  Frozen worklists/conf and the other 8,196 projections are unchanged. Native
  validation covers 114 reviews and 214 history files; shared validation covers
  106 bundles. The 256-test focused suite passed before this addition; the
  38-test export suite passed after all projection/export writes, with one
  upstream LinkML deprecation warning. Export bytes/hashes, README corpus
  documentation, new-path ignore checks and diff checking pass.

  The browser run checks all 100 pages and 782 evidence toggles at both 1440px
  and 390px, with unique anchors, no page-wide overflow and no JavaScript errors.
  PF01906 checks preserve the multiplicative comparator, exact reference/domain
  mapping, YbjQ/YjbQ distinction, ongoing metal-assay qualification and the
  nonsignificant Rv1762c row. Graph-heading, expanded-edge and right-side
  evidence screenshots were visually inspected at both sizes; mobile tables
  scroll internally. Chromium required a scoped approved retry after Mach-port
  startup error 1100; ordinary repository/skill reads succeed. No permission
  configuration, application/schema change, source pin, publication, full QC
  or exhaustive family-review claim is made by this pass.
- PF01909's three graphs retain eleven DIRECT, OBSERVED biochemical effects
  and two OPEN discussions. Original Zhang2010 Figures 3/4/5/8, the main
  Methods/Results/Discussion and Table 1 were inspected; raw gels and other
  figures' images were not. The reference residues and PF01909 85-144 mapping
  were checked against current source JSON, and every retained quotation
  occurs in the inspected primary HTML. Whole-protein HD controls remain
  outside PF01909; G94L and Mg/Mn response exceptions remain explicit.
  Its partial self-review digest is
  `5d41ffb4b03a984dac3a3fd2250d5601e2e1cb724b4f634bba8f2c0c7aba6aa4`.
  After CREATE/REVIEW projection, all 8,296 records pass with zero drift;
  generated schema checks also show zero differences. All 101 latest review
  digests, retained source hashes and rendered JSON records match, and all
  8,296 inventory digests match. Native validation covers 115 reviews and
  216 history files; shared validation covers 107 bundles. The 256-test
  focused suite and 38 export tests pass; one upstream LinkML deprecation
  warning remains. Identity-only exports were regenerated and their exact
  hashes updated in `exports.md`. Source metadata, source pins and conf are
  unchanged; no publication or full-QC claim is made.
  The complete browser run checks all 101 pages and 793 evidence toggles at
  1440px and 390px without duplicate IDs, page overflow or JavaScript errors.
  PF01909's three graphs, eleven support/directness labels and mapping/assay
  limits are asserted explicitly. Its desktop/mobile normal, edge and
  expanded-evidence screenshots were visually inspected. Normal Chromium
  launch again failed at Mach-port registration (1100); the narrowly approved
  local-preview retry passed. Repository and installed skill reads work;
  this is not a blanket filesystem-read failure or a permission-policy change.
- PF01910 adds twelve scoped graphs with twenty-four OBSERVED effects:
  two DIRECT binding edges and twenty-two INDIRECT production, RNA and
  phenotype edges. Dermoun2010 Figures 2-6 and Park2018 Figures 4/5,
  Figure S5A and Table S5A were visually inspected; inaccessible Dermoun
  supplements and other uninspected Park supplements remain coverage limits.
  Q9WYV6/AAD35571.1 and J9VTN7/AFR95954.1/XP_012050770.1 exact reference
  equality, sequence versions, lengths, taxa and MD5 values were checked.
  The fungal supplement sequence agrees; the BY4741 assay clone remains
  qualified. Printed units and the cross-rescue genotype/YP617 conflict
  are preserved, with no invented residue, transport or clinical mechanism.
- After PF01910's REVIEW history projection, all 8,296 records validate
  with zero generated drift; schema-only generation also shows zero
  differences. All 102 latest review digests, source hashes, imported
  identities and rendered JSON records match, as do all inventory digests.
  Native checks cover 116 reviews and 218 history files; shared validation
  covers 108 structured bundles. The focused suite passed 256 tests and
  the export suite passed 38 after projection/export writes finished, with
  one upstream LinkML deprecation warning. Export byte counts and hashes
  in `docs/exports.md`, documentation checks and `git diff --check` pass.
  The first inventory helper used a relative root and failed before writing;
  its absolute-root retry succeeded without changes to native code.
- The complete browser run checks all 102 curated pages and 817 evidence
  toggles at both 1440px and 390px, with unique anchors and no page overflow
  or JavaScript errors. PF01910's twelve graphs, two direct/twenty-two
  indirect labels, reference mappings and source/context limits are asserted.
  Its normal, edge and expanded-evidence screenshots at both widths were
  visually inspected. Normal Chromium launch failed at macOS Mach-port
  registration (1100); the narrowly approved local-preview retry passed.
  Repository and installed skill reads succeed. No permission settings,
  source pins or publication state were changed; no full-QC pass is claimed.
- PF01914 adds thirteen PHENOTYPIC graphs with thirty-nine OBSERVED,
  INDIRECT effects from six primary studies. Eight current ledgers plus
  one preserved superseded extract and two OPEN discussions retain exact
  SnatA/MarC/YchE mappings, clone/background qualifications, negative
  comparisons and unresolved biochemical mechanisms. No family-wide
  transport or antibiotic-resistance mechanism is asserted.
- A final enlarged Figure 1C check caught a transcription error: YchE is
  p=0.38, not p=0.387; p=0.87 belongs to YjeM. The first retained review
  and its evidence bytes remain unchanged. The corrected overlay and
  separate extract have a successor partial scientific self-review,
  `20261012T005526Z-pf01914-yche-figure-label-correction-and-cellular-contexts`,
  semantic digest
  `b5bccdc33105dd206354b011caed1fd0475d54f692e0b04c45cf9b305b15808b`.
  CREATE/REVIEW/EDIT/REVIEW events preserve the actual sequence. All
  graph directions and the nonsignificant uptake conclusion are unchanged;
  IN_PROGRESS and NEEDS_FOLLOWUP remain.
- After PF01914's successor REVIEW history projection, full records-check
  validates all 8,296 records with zero generated drift. Schema-only
  reports zero model differences, not 8,296 additional record checks.
  All 103 latest scientific-review digests, retained source hashes,
  imported identities and rendered JSON records match. All 8,296 inventory
  digests match, with 98 graph-bearing and 8,198 graphless families,
  448 graphs and 856 edges (841 OBSERVED, 13 HYPOTHESIZED, one INFERRED
  and one CONTESTED). Native validation covers 118 reviews and 222 history
  files; shared validation covers 110 structured bundles.
- The focused graph/record/review/history suite passed 256 tests; export
  reproducibility and shared contracts passed 38 tests with one upstream
  LinkML deprecation warning. Export generation and tests ran after the
  final projection writes. README, export byte/hash documentation and
  diff checks pass; identity exports do not contain the causal edges.
- The complete Chromium run verifies all 103 curated pages and 856 edge
  evidence toggles at 1440px and 390px, with unique anchors and no page-wide
  overflow or JavaScript errors. PF01914's thirteen graphs, thirty-nine
  observed/indirect labels, mappings, corrected p-value and limitations
  are explicitly asserted. Normal, edge and expanded-evidence screenshots
  were visually inspected at both widths; desktop edge/evidence captures
  are identical because the evidence column already fits in view.
  Normal launch fails at macOS Mach-port registration (1100); the narrowly
  approved local-preview retry passes. Repository and installed skill reads
  succeed. No permission settings, source pins, commits or publication state
  were changed, and no full publication-QC pass is claimed.
- PF01918 adds sixteen scoped graphs with fifty-three OBSERVED effects:
  forty-six DIRECT and seven INDIRECT, in fourteen MECHANISTIC and two
  PHENOTYPIC graphs. Eleven retained ledgers and two OPEN discussions separate
  DNA binding, architecture and stiffness, transcription, RNA chaperone assays,
  cellular growth, human Rpp25/Rpp20 assembly, parasite nuclease readouts and
  peptide deacetylation. Native K16 PTM counterevidence, historical constructs,
  printed NAD units, mixed acetylation sites and additional family contexts
  remain explicit; no family-wide mechanism or complete coverage is claimed.
- The first PF01918 partial scientific self-review,
  `20261012T011947Z-pf01918-alba-dna-rna-and-nuclease-assay-contexts`, retains
  semantic digest
  `4f351def61ebe6a038c11381f47d61d8b24efeb25578bb8e428d02d163df092d`.
  A rendered-evidence check found that five DNA-binding edges displayed a
  same-paper transcription quotation. The successor review,
  `20261012T012924Z-pf01918-assay-specific-dna-evidence-and-alba-contexts`,
  binds digest
  `6c5454b5015340729df289e3c672fb359600cc38f7eda4a85d1823317caccfcc`.
  Its separate Figure 3 extract supplies the actual binding quotation.
  Structured comparison proves that only those five quotation/cache/hash
  triples changed: graph claims, directions, counts and discussions are
  identical. The first reviewed projection's digest and all ten original
  evidence ledgers remain intact. CREATE/REVIEW/EDIT/REVIEW history records
  the real sequence; status remains IN_PROGRESS with NEEDS_FOLLOWUP.
- After the successor REVIEW history projection, all 8,296 records validate
  with zero generated drift. Schema-only reports zero model differences,
  not another full-corpus validation. All 104 latest review digests, retained
  evidence hashes, imported identities and rendered JSON records match;
  all 8,296 inventory digests match. The inventory contains 99 graph-bearing
  and 8,197 graphless families, 464 graphs and 909 edges: 894 OBSERVED,
  13 HYPOTHESIZED, one INFERRED and one CONTESTED. Native validation covers
  120 reviews and 226 history files; shared validation covers 112 bundles.
  The inventory helper initially received a relative root and failed before
  writing; the corrected absolute-root invocation completed successfully.
- The focused graph/record/review/history/projection-binding suite passed
  256 tests before the narrow quotation correction. Following that correction
  and the final history projection, export reproducibility and shared contracts
  passed all 38 tests with one upstream LinkML deprecation warning. Native
  export checks report current artifacts, and documented row counts, byte
  sizes and SHA-256 hashes match. The README corpus check and diff check pass.
  Identity exports do not include causal edges. No schema or application code
  changed during this PF01918 curation and quotation-correction pass.
- After the PF01918 correction, the complete Chromium run passed all 104
  curated pages and 909 edge evidence toggles at both 1440px and 390px,
  including unique anchors, support labels, no page-wide overflow and no
  JavaScript errors. PF01918's sixteen graphs, 46 direct/seven indirect
  labels, member mappings, source limitations and five corrected binding
  quotations are explicitly asserted. Normal, edge and expanded-evidence
  screenshots were visually inspected at both widths; the two desktop table
  captures are byte-identical because the evidence column already fits.
  All 103 other JSON previews are byte-identical to their pre-correction
  copies. HTML bytes changed on regeneration, so the complete browser run
  was repeated rather than treating the earlier run as final-state proof.
  Normal Chromium startup failed at macOS Mach-port registration (1100);
  the narrowly approved local-only retry passed. Ordinary repository and
  installed-skill reads succeed. No permissions, source pins, commits or
  publication state were changed; no full publication-QC pass is claimed.
- PF01923 adds twenty-seven scoped graphs and seventy-seven OBSERVED edges:
  fifty-six DIRECT and twenty-one INDIRECT, in eighteen MECHANISTIC and nine
  PHENOTYPIC graphs. Ten retained ledgers cover eight primary studies and two
  inspected supplementary PDFs. SePduO, LrPduO, SeEutT, LmEutT and human MMAB
  remain distinct, with exact reference/domain mappings, extra-domain
  substitutions, redox/ATP/ADP conditions, source conflicts and unresolved
  historical constructs recorded. Two OPEN discussions retain coverage and
  domain-attribution limits; no family-wide mechanism is asserted.
- The partial scientific self-review,
  `20261012T015942Z-pf01923-pduo-eutt-mmab-assay-and-domain-contexts`, binds
  semantic digest
  `372e2ff334863e6ab220755ad6cb31f3ff13807e29193bd0c40fd34689bfdc63`.
  Native CREATE and REVIEW events preserve the actual curation sequence.
  Status remains IN_PROGRESS with NEEDS_FOLLOWUP. All seventy-seven edge
  quotations match the inspected primary text; retained minimal quotations
  remain within the per-source quotation limit.
- After the PF01923 REVIEW history projection, all 8,296 records validate
  with zero generated drift. Schema-only reports zero model differences,
  not another full-corpus validation. All 105 latest review digests, retained
  overlay/evidence hashes, imported identities and rendered JSON records match,
  as do all 8,296 inventory digests. The inventory contains 100 graph-bearing
  and 8,196 graphless families, 491 graphs and 986 edges: 971 OBSERVED,
  thirteen HYPOTHESIZED, one INFERRED and one CONTESTED. Native validation
  covers 121 reviews and 228 history files; shared validation covers 113 bundles.
- The focused graph/record/review/history/projection-binding suite passed
  256 tests. After the final generated writes, export reproducibility and
  shared contracts passed 38 tests with one upstream LinkML deprecation
  warning. Native export checks report current artifacts, and documented
  row counts, byte sizes and SHA-256 hashes match. Identity exports do not
  include causal edges. No schema or application code changed in this pass.
- The complete Chromium run passes all 105 curated pages and 986 edge evidence
  toggles at both 1440px and 390px, with unique anchors and no page-wide overflow
  or JavaScript errors. PF01923's twenty-seven graph scopes, 56 DIRECT/21 INDIRECT
  labels, five member mappings, ADP-versus-ATP caption discrepancy and evidence
  limitations are explicitly asserted. Normal, edge and expanded-evidence
  screenshots were visually inspected at both widths; mobile tables scroll
  internally and desktop edge/evidence captures coincide because that column
  already fits. An initial assertion looked for the apparent-Km qualification
  before opening its evidence panel; moving it after expansion fixed the
  harness without changing the scientific record or application.
  Normal Chromium launch fails at macOS Mach-port registration (1100); the
  narrowly approved local-only retry passes. Repository and installed-skill
  reads succeed. No permissions, source pins, commits or publication state
  were changed; no full publication-QC pass is claimed.
- PF01925 adds nine scoped graphs and thirty-seven edges: thirty-six
  OBSERVED/INDIRECT cellular effects and one HYPOTHESIZED/UNRESOLVED CysZ
  uptake proposal, with no DIRECT or MECHANISTIC claim. Seven ledgers retain
  the CysZ, PmpC and MamO primary contexts, exact protein/domain mappings,
  conditional negatives and qualified TauE/SafE/TsaS transport assignments.
  CysZ Figure 3, PmpC Figure 6, MamO Figure 3 and the original S3 figure
  were visually inspected; publisher S4/S5 DOCX tables were parsed. The
  CysZ primer supplement returned challenge HTML and was not inspected.
  Original CysZ/PmpC CDS translations match current references; PmpC also
  matches its archived UniSave sequence and the primary cloning prefix.
- The partial scientific self-review,
  `20261012T021931Z-pf01925-cysz-pmpc-mamo-effects-and-transport-boundaries`,
  binds semantic digest
  `6f3b654ccf5faeddba666071806e79e48d6343e4b0e0cc7d482972eb937e837f`.
  CREATE `2026-10-12T021339Z-codex-4744a4` and REVIEW
  `2026-10-12T021922Z-codex-993d36` preserve the actual curation sequence.
  All thirty-seven edge quotations match inspected primary text; distinct
  quoted-word totals are 21 for CysZ, 10 for PmpC and 13 for MamO. Status
  remains IN_PROGRESS with NEEDS_FOLLOWUP and two OPEN discussions.
  Initial source-identifier and quotation corrections preceded retention;
  no earlier retained review was rewritten. A rejected uppercase actor enum
  was corrected to native `ai_agent` before CREATE succeeded.
- After the PF01925 REVIEW history projection, all 8,296 records validate
  with zero generated drift. All 106 latest review digests, retained
  overlay/evidence hashes, imported identities and rendered JSON records
  match, as do all 8,296 inventory digests. The inventory contains 101
  graph-bearing and 8,195 graphless families, 500 graphs and 1,023 edges:
  1,007 OBSERVED, fourteen HYPOTHESIZED, one INFERRED and one CONTESTED.
  Native validation covers 122 reviews and 230 history files; shared
  validation covers 114 bundles. Export row counts and documented hashes
  match the generated artifacts. The initial README-check invocation lacked
  its required mode; the corrected `scripts/check_docs.py --check` passes.
- The filesystem retry during PF01925 verification succeeds without
  escalation for repository/installed-skill reads, metadata for the formerly
  denied `/Users/marcin/.cache/uv/sdists-v9/.git`, and offline UV/Pillow
  import. The installed causal-graph skill passes its validator. Chromium
  still fails separately at macOS Mach-port registration (1100) under the
  command sandbox. No permission configuration was changed; these successes
  do not prove a global permission repair or establish every prior cause.
- After the final PF01925 history projection, the focused
  graph/record/review/history/projection-binding suite passed 256 tests.
  After export regeneration, the export suite passed 38 tests with one upstream LinkML deprecation
  warning. Native export checks report current artifacts. Identity exports
  do not include causal edges. No schema or application code changed in
  this family pass; frozen worklists, configuration and source pins are
  unchanged. The original checkout's unrelated files remain untouched.
- The complete Chromium run passes all 106 curated pages and 1,023 edge
  evidence toggles at both 1440px and 390px, with unique anchors and no
  page-wide overflow or JavaScript errors. PF01925's nine graphs, thirty-six
  indirect observed effects, one unresolved hypothesis, three member/domain
  mappings, vector discrepancy and measured-readout qualifications are
  explicitly checked. Normal, edge, expanded-evidence and hypothesis
  screenshots were visually inspected at both widths; mobile tables scroll
  internally. Desktop edge/evidence captures are byte-identical because the
  evidence column already fits. The narrowly approved local-only retry
  succeeded after sandboxed Mach-port startup was denied. No source-pin
  capture, commit, push or publication occurred; no full publication-QC
  pass or corpus-wide scientific completion is claimed.
- PF01927 adds fourteen graphs and twenty-four OBSERVED effects: nineteen
  DIRECT, three INDIRECT and two UNRESOLVED. Four retained ledgers separate
  purified worm/human RNA assays, complex assembly and cellular contexts.
  All main figures 1-7 and supplement S2/S3/S5/S8 and Tables S1/S2/S4 were
  visually inspected during curation. Current Pfam matches are narrower
  than the experimental CTDs; no isolated-Pfam nuclease is established.
  The Figure 7A/S8C affinity discrepancy, D435A/D453A conflict, construct/tag
  assignments and coexpression solubility remain qualified. Manufacturer
  A11029 documentation confirms a catalog mismatch with the paper's stated
  fluorophore, not the actual experimental reagent. No source result was
  silently corrected to choose one conflicting value.
- The partial scientific self-review,
  `20261012T024436Z-pf01927-mut7-exd3-biochemical-assembly-and-cellular-contexts`,
  binds digest
  `d80fa2a64f79c51ab5ddc709411da9e59260107bbd6fd09c976dc489bd7ef839`.
  CREATE `2026-10-12T022834Z-codex-012b27`, EDIT
  `2026-10-12T024132Z-codex-9f0324` and REVIEW
  `2026-10-12T024223Z-codex-0ae9df` preserve the real curation sequence.
  All twenty-four edge quotations match the primary HTML; the paper's
  thirteen distinct snippets total twenty-five quoted words. Status remains
  IN_PROGRESS, with NEEDS_FOLLOWUP and two OPEN discussions. Native checks
  validate 123 retained reviews and 233 history files; shared validation
  covers 115 bundles. The earlier validation-session handle was gone on
  resume; the CREATE file existed and was not duplicated. Fresh overlay,
  quote and evidence checks passed before regeneration and review retention.
- Ordinary repository and installed-skill reads succeed. During PF01927
  PDF rendering, offline UV/Pillow encountered another denial reading
  `/Users/marcin/.cache/uv/sdists-v9/.git`; a narrowly approved retry
  completed rendering. Earlier successful reads do not prove a permanent
  global permission repair. No permission configuration was changed.
- The PF01927 corpus verifier confirms all 8,296 inventory digests, all 107
  latest scoped review digests and evidence/overlay hashes, unchanged imported
  identities, and exact rendered JSON. There are 102 graph-bearing and 8,194
  graphless families, 514 graphs and 1,047 edges: 1,031 OBSERVED, fourteen
  HYPOTHESIZED, one INFERRED and one CONTESTED. The graph/record/review/history/
  projection-binding suite reports 256 passing tests. These structural and
  regression checks do not establish complete scientific coverage.
- After the final PF01927 REVIEW history projection, `records --check`
  validates all 8,296 records with zero generated differences. Exports are
  current and their 38-test suite passes, with one upstream LinkML
  deprecation warning. Row counts, bytes and SHA-256 values match
  `docs/exports.md`; the identity exports do not contain causal edges.
  README corpus verification and `git diff --check` pass. No application
  or schema change was made in this family pass; source snapshots,
  configuration and the original checkout's unrelated files remain unchanged.
- The full Chromium run passes all 107 curated pages and 1,047 edge
  evidence toggles at both 1440px and 390px, with unique anchors and no
  page-wide overflow or JavaScript errors. PF01927's fourteen graph scopes,
  twenty-four observed labels, nineteen direct/three indirect/two unresolved
  assessments, exact domain mappings and source discrepancies are explicitly
  checked. Normal, edge, expanded-evidence and unresolved-effect screenshots
  were visually inspected at both widths. Mobile tables scroll internally;
  desktop edge/evidence captures are byte-identical because the evidence
  column fits. Sandboxed Chromium startup failed at macOS Mach-port
  registration (1100); the narrowly approved local-only retry passed.
  No source-pin capture, commit, push or publication occurred. This is not
  full publication QC, independent scientific endorsement or corpus completion.
- Latest generated ownership, updated at the PF01955 checkpoint: only the 124
  family projections with maintained overlays and the ownership manifest change
  under `data/families/`. Complete membership is in the checked inventory at
  `reports/causal_graphs/inventory.json`; immutable worklists and the other
  8,172 projections remain unchanged. Earlier checkpoint counts remain historical.
  The original checkout's unrelated untracked files are preserved.

PF01930 retained provenance:

- Review bundle:
  `reviews/structured/20261012T030857Z-pf01930-pcal-gsu-cas4-processing-and-acquisition-contexts/`.
  YAML is authoritative; Markdown is derived. The semantic digest is
  `b5c88dcdd61ef7c68b904e4bc3c3751f792dfc0cee5ba438dd3280fa1302aaad`.
  It is a same-agent partial scientific assessment, NEEDS_FOLLOWUP, not
  independent endorsement or full-family completion.
- Actual CREATE and REVIEW events are
  `history/records/PF01930/2026-10-12T025903Z-codex-ba7113.yaml` and
  `history/records/PF01930/2026-10-12T030712Z-codex-393c80.yaml`.
  Four evidence ledgers preserve source identity, Pcal biochemistry, Gsu
  fusion/complex and surrogate-cell assays, and remaining source coverage.
- All seventeen edge snippets match the inspected primary HTML and their
  retained cache hashes. Nine Pcal residue identities and two Gsu identities
  match the current sequence references. This does not establish exact clone
  scars or isolated-domain sufficiency. The two open discussions retain
  the Pcal metal assignment, Gsu vector naming, ED4g contradiction, missing
  supplement and broader member/native-function questions.
- Pcal Figures2/3/5 and Gsu Figures1/3/4 andED4/8 were visually inspected.
  Gsu Tables1/2 pages1-3 were parsed; the Pcal supplement link returned
  challenge HTML, an alternative path404 and the attempted publisher page403.
  These are access limits, not evidence that the supplement does not exist.
  No raw-data replication or exhaustive family survey is claimed.
- After the REVIEW history projection, all 8,296 records validate with zero
  generated drift. The full inventory and verifier confirm all semantic digests,
  all108 latest review/overlay/evidence bindings, unchanged imported identities
  and exact rendered JSON. The corpus has108 IN_PROGRESS and8,188 SEEDED
  records,103 graph-bearing and8,193 graphless families,527 graphs and1,064
  edges:1,048 OBSERVED,14 HYPOTHESIZED,one INFERRED andone CONTESTED.
- The focused graph/record/review/history/projection-binding suite passes256
  tests. Export regeneration/check and all38 export tests pass, with the same
  upstream LinkML deprecation warning. Artifact row counts, bytes and hashes
  match `docs/exports.md`. Schema regeneration checks and README checks pass.
  Native history/review checks cover235 history files,124 native reviews and
  116 structured bundles. None of these checks establishes full scientific
  coverage, publication or independent endorsement.
- Full Chromium verification passes all108 curated pages and1,064 edge
  evidence toggles at1440px and390px, with unique anchors and no page-wide
  overflow or JavaScript errors. The parsed browser case list matches every
  overlay and its edge count. PF01930's13 scopes,17 observed labels,
  11 direct/4 unresolved/2 indirect assessments, mappings and source conflicts
  are checked explicitly. Normal, edge, expanded-evidence and unresolved-effect
  screenshots were visually inspected at both widths. Mobile tables scroll
  internally; desktop edge/evidence captures show the same fitted columns.
  Sandboxed Chromium startup failed at macOS Mach-port registration1100;
  the narrowly approved local-only retry passed. Ordinary filesystem reads
  work, but this does not imply unrestricted network or browser execution.
  No source-pin capture, commit, push or publication occurred. Full
  publication QC and full scientific coverage remain unclaimed.

PF01931 retained provenance:

- Review started2026-10-12T03:30:28Z and finished2026-10-12T03:30:54Z.
  `reviews/structured/20261012T033054Z-pf01931-yjjx-biochemistry-and-prrc1-trafficking-contexts/review.yaml`
  and its derived Markdown retain same-agent partial scientific assessment,
  native NEEDS_FOLLOWUP and the open context-coverage finding. Semantic digest:
  `e5a01b035c3c2b918f684a6f4958819131d401acd03d34427c0cb49ea70e90b4`.
- Actual canonical history is retained at
  `history/records/PF01931/2026-10-12T031656Z-codex-007f82.yaml` and
  `history/records/PF01931/2026-10-12T033028Z-codex-1ed0ad.yaml`.
  Native writers regenerated the projection and its history index; no prior
  history or review was rewritten and no status promotion was made.
- Five retained ledgers cover identity, Zheng2005, Huang2021, Peng2025 and
  coverage. The2005 study was read through the author's explicit2009 thesis
  republication, not an independent replication. Tables4.2/4.3 and Figure4.5,
  Huang Figure5 and Peng Figure7 were visually checked against Results/Methods.
  PNAS supplements returned challenge HTML or403; Liu2025 thesis download
  ended after50redirects. Those uninspected methods remain coverage limits.
- YjjX phosphate release is not independent identification of the nucleotide
  product. Dose curves do not establish competitive binding; no RNA-protection,
  translation-inhibition or residue-level catalytic step is adopted. The MLI
  deposited prefix versus primer-suggested MLLI, substrate-negative prose
  versus high-concentration signals, and Mn/GDP-Km discrepancies stay explicit.
- Human whole-protein knockdown/knockout and re-expression do not establish
  isolated PF01931 function. ATRAP and ATG9A readouts remain distinct; panel7I
  has an ATRAP axis label despite ATG9A images, caption and Results. The
  low-cytosol GST-PRRC1 experiment is multicomponent and lacks a shown GST-only
  lane. LC3 puncta are morphology, not flux. Steady-state EGFR and synchronized
  RUSH EGFR are different conditions, not automatically contradictory results.
- Remaining contexts include zebrafish Mys/PKA development, domain-specific
  PRRC1/COPII experiments, Lawhorn antimetabolite resistance, VC0702/1U14,
  Thermoplasma fusions and other members. No family-wide negative is claimed.
- Whole-corpus verification checks all8,296 inventory digests,109 current
  review/overlay/evidence bindings, unchanged imported identities and exact
  rendered JSON. Totals are109 IN_PROGRESS,8,187 SEEDED,104 graph-bearing,
  8,192 graphless,535 graphs and1,084 edges:1,068 OBSERVED,14 HYPOTHESIZED,
  one INFERRED and one CONTESTED. All partial follow-ups remain open.
- Final record and schema-only checks have zero generated drift. Native
  validation covers125 reviews and237 history files; shared validation covers
  117 structured bundles. The focused suite passes256 tests in143.19s.
  These checks do not establish full scientific or publication-QC completion.
- Exports were regenerated after all record writes ended, and the native
  export check is current. All38 export tests pass in115.98s with one upstream
  LinkML deprecation warning. Row counts, byte lengths and SHA-256 values match
  `docs/exports.md`; identity exports do not contain the causal edges.
- PF01931 desktop/mobile screenshots at1440px and390px were inspected for
  normal scope, edge, expanded-evidence and unresolved-effect views. Tables
  scroll internally on mobile. Desktop edge/evidence captures are byte-identical
  because the evidence column fits. Eight scopes,20 observed edges,8 DIRECT,
  9 INDIRECT and3 UNRESOLVED labels, member mappings and source limits pass
  explicit browser assertions. Original checkout files remain unchanged.
- Full Chromium verification passes all109 curated pages and1,084 edge
  evidence toggles at both widths, including the five graphless discussions,
  unique anchors, absence of page-wide overflow and absence of JavaScript
  errors. The parsed case list exactly matches all109 overlays and their
  edge counts. README corpus verification and `git diff --check` also pass.
- Repository and installed-skill reads work. The uv dependency cache still
  required scoped approval, and sandboxed Chromium failed at macOS Mach-port
  registration1100; the local-only approved retry ran the display checks.
  This is not a general permission-policy repair. No source-pin capture,
  commit, push, merge or publication was performed.

PF01933 retained provenance:

- Review started2026-10-12T03:48:47Z and finished2026-10-12T03:51:03Z.
  `reviews/structured/20261012T035103Z-pf01933-cofd-fbia-and-glmr-separated-causal-contexts/review.yaml`
  and its derived Markdown retain same-agent partial scientific assessment,
  native NEEDS_FOLLOWUP and an open coverage finding. Semantic digest:
  `286191fbde6eec7333c8ad9a6a603b6690c5492cb2ac27d8cf30c56aabbc6cc1`.
- Actual CREATE and REVIEW history:
  `history/records/PF01933/2026-10-12T033819Z-codex-a1c77d.yaml` and
  `history/records/PF01933/2026-10-12T034847Z-codex-eee6a1.yaml`.
  Native regeneration preserves the immutable imported identity; no old
  review or history was rewritten and status remains IN_PROGRESS.
- Six ledgers retain identity, four primary studies and coverage. Bashiri
  Figure2, Grinter Figure2, Hasan Figure6 and Foulquier Figures1/4 were visually
  inspected with Results and Methods; Foulquier Table1 was parsed as text.
  All ten edge quotations were independently matched to downloaded primary
  HTML as well as their hash-checked retained extracts.
- The Mtb and mixed-species cofactor pairs have explicit joint inputs.
  Hasan product fractions are compositional effects, not absolute turnover
  rates. CofC/FbiD and FbiB chemistry is not assigned to PF01933. Whole-gene
  cofactor loss, GlmR transformation phenotypes and mixed-solution scattering
  are not promoted to resolved molecular mechanisms.
- Foulquier Results Y265/R301 agree with O06974v1 but conflict with Methods
  Y264/R300/His264. R301 is outside the current7-292 match. Exact clones,
  Hasan's reported0.14nM Fo and supplementary accession/product controls remain
  unresolved. The attempted supplementary URLs returned challenge HTML.
- Older CofD reactions, other cognate pairs, GlmR accessory uridyltransferase,
  earlier morphogenesis,2026 modification studies and further member branches
  remain open. Reference maps and a71-entry reviewed-member query do not
  establish all-member functional coverage.
- All8,296 records validate with zero generated drift after the REVIEW event;
  schema-only checks are also current. Native validation covers126 reviews and
  239 history files; shared validation covers118 structured bundles. The256
  focused tests pass in126.73s. All8,296 inventory digests and110 current
  review/overlay/evidence bindings, imported identities and rendered JSON match.
  Totals are110 IN_PROGRESS,8,186 SEEDED,105 graph-bearing,8,191 graphless,
  542 graphs and1,094 edges:1,078 OBSERVED,14 HYPOTHESIZED, one INFERRED and
  one CONTESTED. These are partial reviews, not completed family coverage.
- Exports were regenerated only after record writers finished. Native export
  check is current, and all38 export tests pass in92.84s with one upstream
  LinkML deprecation warning. `docs/exports.md` records current bytes and hashes;
  these identity exports do not contain causal edges. README corpus check passes.
- The access retry confirms ordinary reads of the repository, installed causal
  skill and uv cache marker `/Users/marcin/.cache/uv/sdists-v9/.git`. Cache
  mutation was not tested in this pass. Sandboxed Chromium still fails macOS
  Mach-port registration1100; that is an execution restriction, not a failed
  repository read. No permission configuration was changed. Local browser
  verification uses a narrowly approved retry, not a general sandbox bypass.
- PF01933 normal scope, edge, expanded-evidence and unresolved-effect captures
  were visually checked at1440px and390px. Desktop edge/evidence files are
  byte-identical because the evidence column fits. Mobile tables scroll inside
  their own region. Browser assertions verify all seven scopes, ten OBSERVED
  labels, four DIRECT/three INDIRECT/three UNRESOLVED labels, mappings and
  source limitations. No page-wide overflow or JavaScript errors are present.
- Full Chromium verification passes all110 curated pages and1,094 edge
  evidence toggles at both widths, including all five graphless discussions,
  unique anchors, no page-wide overflow and no JavaScript errors. The parsed
  browser case list exactly matches all110 overlays and their edge counts.
  The original checkout remains unchanged; `git diff --check` passes.
  No source checkpoint capture, commit, push, merge or publication occurred.
  Full publication QC, independent scientific endorsement and corpus completion
  remain unclaimed.

PF01934 retained provenance:

- Review started2026-10-12T04:18:51Z and finished2026-10-12T04:20:52Z.
  `reviews/structured/20261012T042052Z-pf01934-hept-ampylation-and-fusion-causal-contexts/review.yaml`
  and its derived Markdown retain same-agent partial scientific assessment,
  native NEEDS_FOLLOWUP and an open coverage finding. Semantic digest:
  `c716584a71ec4994e2931f9ea42dd797769573bb899f3e852d265a0793ba7207`.
- Actual CREATE, EDIT and REVIEW history:
  `history/records/PF01934/2026-10-12T040422Z-codex-7b3362.yaml`,
  `history/records/PF01934/2026-10-12T041851Z-codex-61b5eb.yaml` and
  `history/records/PF01934/2026-10-12T042108Z-codex-00bb97.yaml`.
  The EDIT corrects the draft mass interpretation before review: the2026
  three-AMP assignment accounts for the approximately28Da sequence-mass
  change from two D-to-E substitutions, not just the raw peak difference.
  No prior retained review or history was rewritten.
- Six ledgers retain identity, four primary studies and coverage. Visually
  inspected2015 Figures1/5,2018 Figure1,2020 Figures4/5/7,2026
  Figures1/2/4/5/6 andSupplementS1-S6, with relevant Results and Methods.
  The2026 publisher DOCX supplied TablesS1-S4; raw MS/AUC spreadsheets
  were present but not reanalyzed. All28 edge quotations match downloaded
  primary HTML as well as their hash-checked retained extracts.
- The276-aa fusion reference is WP_164925653.1, not the shorter Q8EGZ7
  sequence. Structured RefSeq comparison proves the251-residue shared
  segment and24-position shift, with an additional start-residue difference.
  Current Q8EGZ7 PF01934 144-234 projects to WP168-258; this is not a
  fresh HMM assignment. C163/C270 lie outside that core. The NTase domain
  maps PF18765 and its chemistry is not assigned to the HEPN core.
- SO_3166 purified cleavage, joint AMP transfer, modified-preparation activity,
  species-specific induced colony recovery and substitutions remain separate
  from heterologous Thermococcus assays and fusion effects. The archaeal
  AMP count is unresolved. Fusion modification loss alone is not sufficient
  activation; redox-sensitive bands and peroxide-conditioned phenotypes are
  not a demonstrated intracellular causal relay.
- Preserved source conflicts include the frozen2:6 versus primary6:2
  HepT:MntA stoichiometry, typeII versus later typeVII interpretation,
  antibiotic units,2020 G27 substitution wording and2026 fragment/caption
  numbering. W3-18-1 RefSeq Y106 conflicts with source Y136; its current
  Pfam mapping remains open. Legionella Q5ZRG2 maps PF08780 and is excluded.
- Aphanizomenon full text returned publisher403/repository challenge and
  remains a follow-up, not negative evidence. The2026 PMC supplement was
  inaccessible but the normal publisher link succeeded. Other operon,
  MntA-helix, homolog-screen, stability/protease, native-activation and member
  contexts remain open; status is IN_PROGRESS, not family-wide completion.
- All8,296 records validate with zero generated drift after projecting the
  REVIEW event; schema-only checks are also current. Native checks validate
  127 reports and242 history files; shared validation covers119 bundles.
  All256 focused tests pass in135.45s. All8,296 inventory semantic digests
  and111 latest review/overlay/evidence bindings, imported identities and
  rendered JSON records match. Totals:111 IN_PROGRESS,8,185 SEEDED,
  106 graph-bearing,8,190 graphless,558 graphs and1,122 edges, comprising
  1,106 OBSERVED,14 HYPOTHESIZED,one INFERRED andone CONTESTED.
- Exports were regenerated after the final record writer finished. Native
  export reproducibility is current and all38 export tests pass in125.48s,
  with one upstream LinkML deprecation warning. Current bytes and hashes
  are retained in `docs/exports.md`; these identity exports do not include
  causal edges. README corpus verification and `git diff --check` pass.
- PF01934 scope, edge, expanded-evidence and unresolved-effect captures
  were visually checked at1440px and390px. Desktop edge/evidence captures
  have identical hashes because the evidence column fits. Mobile text wraps
  and edge tables scroll within their own regions. Explicit browser checks
  verify16 scopes,28 OBSERVED labels,4 DIRECT/15 INDIRECT/9 UNRESOLVED
  labels, construct mappings, flank coordinates and retained source limits.
  Sandboxed Chromium still fails macOS Mach-port registration1100; the
  narrowly approved local-file-only retry supplies browser verification.
  This is an execution restriction, not a repository-read failure, and no
  permission configuration or publication source pin was changed.
- Full Chromium verification passes all111 curated pages and1,122 edge
  evidence toggles at both widths, including the five graphless discussions,
  unique anchors, absence of page-wide overflow and absence of JavaScript
  errors. The browser case list exactly matches all111 overlays and their
  edge counts. The original checkout remains unchanged; no source checkpoint,
  commit, push, merge or publication occurred. Full publication QC, independent
  scientific endorsement and corpus completion remain unclaimed.

PF01935 retained provenance:

- Review ran2026-10-12T04:41:54Z to04:42:02Z. Authoritative bundle:
  `reviews/structured/20261012T044202Z-pf01935-hera-domain-boundaries-and-separated-assay-effects/review.yaml`
  and derived Markdown. Same-agent partial scientific assessment,
  NEEDS_FOLLOWUP, IN_PROGRESS; semantic digest
  `d4c20188a921242942a1815091e25eb0f5955ae652d7fd3f4c40cb99b801fcf3`.
- Actual CREATE and REVIEW history:
  `history/records/PF01935/2026-10-12T042916Z-codex-48cd65.yaml` and
  `history/records/PF01935/2026-10-12T044221Z-codex-05713d.yaml`.
  No earlier retained review or history was rewritten.
- Four ledgers retain current protein/domain identities, two primary assay
  studies and coverage. All21 minimal edge quotations match primary XML
  and their hash-checked retained extracts. Visually inspected2014 Figure4
  and supplementS4-S5,2015 Figures2/4/5; relevant primary methods read.
  Publisher downloads supplied the2014 supplement after PMC challenge.
  The2015 supplements and located2025 author-hosted antiviral PDF remain
  unperformed followups, not evidence of absence or global inaccessibility.
- Current Q97WG8v1 and F0NFK8v1 PF01935 matches121-331 exclude several
  tested residues and do not encompass the complete structural motor.
  D471A effects differ among assay readouts; R381A delays rather than
  completely prevents long-DNA processing. NurA-mediated cleavage is not
  HerA-intrinsic nuclease chemistry. E233S deletion rescue is an indirect
  selected-cell effect, not a direct biochemical-to-viability chain.
- All8,296 records validate with zero generated drift; schema generation,
  native128 reviews/244 history files and120 shared bundles pass. The256
  focused tests pass in142.47s. All8,296 inventory digests and112 latest
  review/overlay/evidence bindings, imported identities and rendered JSON
  records match. Totals:112 IN_PROGRESS,8,184 SEEDED,107 graph-bearing,
  8,189 graphless,564 graphs,1,143 edges;1,127 OBSERVED,14 HYPOTHESIZED,
  one INFERRED andone CONTESTED. All family and cohort followups remain open.
- Eight PF01935 scope/edge/evidence/uncertainty captures were visually
  inspected at1440px and390px. Mobile tables scroll internally and text
  wraps; desktop edge/evidence captures share SHA256
  `04c5db5c8beb94e9b87d9ec71ca2df574fbdd05a1034d07ebd27c899f12d727c`.
  Explicit browser checks verify6 graphs,21 OBSERVED labels and
  1 DIRECT/2 INDIRECT/18 UNRESOLVED distinctions plus mapping/assay limits.
  Normal Chromium launch failed macOS Mach-port registration1100; the
  scoped approved local-file retry works. Repository and skill reads work;
  no permission configuration or publication source pin was changed.
- Identity exports were regenerated after final record writes. Their native
  reproducibility check passes; all38 export tests pass in136.43s, with one
  upstream LinkML deprecation warning. Updated bytes/hashes are retained
  in `docs/exports.md`. No causal edges are included in those identity exports.
- The full browser sweep passes all112 curated pages and1,143 edge evidence
  toggles at both widths, including graphless discussions, unique anchors,
  no page-wide overflow and no JavaScript errors. The case list exactly
  matches all112 overlays. README corpus verification and `git diff --check`
  pass. The original checkout remains unchanged. No commit, push, merge,
  publication, full publication-QC pass or corpus completion is claimed.

PF01936 retained provenance:

- Review ran2026-10-12T05:04:42Z to05:05:09Z. Authoritative bundle:
  `reviews/structured/20261012T050509Z-pf01936-marf1-domain-mapping-and-separated-rna-phenotypes/review.yaml`
  and derived Markdown. Same-agent partial scientific assessment,
  NEEDS_FOLLOWUP, IN_PROGRESS; semantic digest
  `9903ec448d54288469906df062d9a72240df580dc263d37e9b4dc4ddd796c953`.
- Actual CREATE and REVIEW history:
  `history/records/PF01936/2026-10-12T045030Z-codex-eba42f.yaml` and
  `history/records/PF01936/2026-10-12T050520Z-codex-4654b7.yaml`.
  No earlier retained review or history was rewritten.
- Four ledgers retain identity, primary human/mouse assays and coverage.
  All22 minimal quotations match inspected primary XML and retained cache
  hashes. Human Figures3/5/6 and mouse Figures1-5/S5/S6 were visually
  inspected; relevant primary methods and mouse supplement pp2-7 were read.
  The first mouse supplement download timed out; a longer EuropePMC
  retrieval succeeded. Bacterial supplement and LabA access limits do not
  establish absent research. Human supplemental interaction/SEC data and
  raw mouse RNA-seq remain outside this review.
- Human238-510 cleavage is not the352-500 crystal construct. Mouse source
  NYN158-320 aligns to canonical337-499 with only two deposited crystal
  mutations, mapping D178/D215/D246/D272 to D357/D394/D425/D451. This local
  proof does not establish every full-length isoform coordinate. Full mouse
  assay preparation includes RRM/LOTUS domains; shorter constructs differ
  in expression host. Knockin protein abundance increases, and two marker
  substitutions accompany D272A. RNA/foci, maturation and fertility effects
  are not joined into an experimentally demonstrated molecular chain.
- All8,296 records validate with zero generated drift; schema generation,
  native129 reviews/246 history files and121 shared bundles pass. The256
  focused tests pass in152.82s. All8,296 inventory digests and113 latest
  review/overlay/evidence bindings, imported identities and rendered JSON
  records match. Totals:113 IN_PROGRESS,8,183 SEEDED,108 graph-bearing,
  8,188 graphless,572 graphs,1,165 edges;1,149 OBSERVED,14 HYPOTHESIZED,
  one INFERRED andone CONTESTED. All family and cohort followups remain open.
- Identity exports were regenerated only after final projection writes.
  Native reproducibility passes; all38 export tests pass in148.41s, with
  one upstream LinkML deprecation warning. Current bytes and hashes are
  retained in `docs/exports.md`; these identity exports contain no causal edges.
- The full browser sweep passes all113 curated pages and1,165 edge evidence
  toggles at1440px and390px, including graphless discussions, unique anchors,
  no page-wide horizontal overflow and no JavaScript errors. The case array
  exactly matches all113 overlays and their edge counts. A focused PF01936
  rerun also passes after adjusting only the temporary screenshot helper to
  scroll the unresolved row into view. Eight scope/edge/evidence/uncertainty
  captures were inspected; uncertainty labels are visible at both widths.
  Mobile tables scroll internally and text wraps. Desktop edge/evidence
  captures share SHA256
  `249a621c6a0aa467636c643dd5950686df12dbcb0c346ccc16a5d70d47221ea6`.
- Repository and installed-skill reads work. Normal Chromium launch still
  fails at macOS Mach-port registration1100; the scoped approved local-file
  retry succeeds. No permission configuration was changed. README corpus
  verification and `git diff --check` pass; the original checkout remains
  unchanged. No commit, push, merge, publication source-pin capture, full
  publication-QC pass or corpus-wide completion is claimed.

PF01938 retained provenance:

- Review bundle:
  `reviews/structured/20261012T052935Z-pf01938-tram0076-dna-beacons-and-separated-rna-growth-contexts/`.
  YAML is authoritative; Markdown is derived. Semantic digest:
  `9ae7f13cbdcea70bce1bb1a2472b5c80da2d6e38c4c0654aeea1f50038561ad8`.
  The same-agent partial scientific assessment is NEEDS_FOLLOWUP, not
  independent endorsement or full-family completion.
- Actual CREATE and REVIEW history:
  `history/records/PF01938/2026-10-12T051759Z-codex-792f49.yaml` and
  `history/records/PF01938/2026-10-12T052959Z-codex-abed6e.yaml`.
  Earlier retained artifacts were not rewritten.
- Primary Figures1,3,4,5,S2,S4,S7 were visually inspected; relevant
  Results/Methods and S1/S2 DOCX table content were read. All eight distinct
  minimal quotations were checked against the primary XML. S3 SPR pixels,
  raw RNA-seq/RIP and experimental clones were not independently analyzed.
  2017 relevant text/captions were read without a figure-pixel review;
  the attempted2025 full text redirected to its abstract.
- Q6M142v1 has69 residues; PF01938 maps13-67. PDB1YVC aligns1-69 plus a
  terminalL and is not the tagged biochemical construct. Assays use S0001,
  not an assumed S2 wild type. S2 Table repeats D25A in several primer-purpose
  cells; Figure4/S1 and canonical numbering distinguish the actual variants.
  Vector-derived biochemical termini remain incompletely sequence-verified.
- Figure3C/5A use DNA beacons, not directly measured native RNA melting.
  Figure4 mutant outcomes are reporter/native growth phenotypes, not shown
  purified-mutant RNA-unfolding reactions. I33A has reduced reporter-host
  abundance but rescues native growth; K62A partially rescues. UTR1515MT
  removes or reverses the parental fluorescence advantage, not every
  numerical genotype difference. Cold-shock reporter responses are transient.
  The2017 uninduced TRAM3066 positive and induced negative are not a
  like-for-like contradiction of the2019 induced negative.
- Other R15 proteins, Ctr3, PyTRAM, enzyme-fused TRAM domains and direct
  native RNA mechanisms remain open. No enzyme activity is transferred to
  TRAM merely because the domain occurs in the enzyme. Native validation
  and review retention do not imply publication or whole-corpus completion.
- Final native reconstruction and ownership checks validate all8,296
  projections with zero drift. Schema generation is current; native130
  reviews/248 history files and122 shared bundles validate. The256 focused
  tests pass in165.68s. All8,296 inventory digests and114 latest scoped
  review/overlay/evidence bindings, imported identities and rendered JSON
  records match. Totals:114 IN_PROGRESS,8,182 SEEDED,109 graph-bearing,
  8,187 graphless,582 graphs,1,197 edges;1,181 OBSERVED,14 HYPOTHESIZED,
  one INFERRED andone CONTESTED. These structural counts are not completed
  family reviews; all family/cohort followups remain open.
- Identity exports were regenerated after all projection writes ended;
  native reproducibility and all38 export tests pass in124.12s, with one
  upstream LinkML deprecation warning. Bytes/hashes in `docs/exports.md`
  are current. These exports do not contain causal edges.
- PF01938 passes the1440px and390px browser checks; eight scope,edge,
  evidence and uncertainty captures were visually inspected. Tables scroll
  internally on mobile, text wraps and uncertainty remains visible. Desktop
  edge/evidence captures share SHA256
  `0bc7f340419169fd463624402de80d1129f220d0a0fa2008fa9cd4e9db3deb69`.
  Normal Chromium startup again failed at macOS Mach-port registration1100;
  the narrowly approved local-file retry succeeds. Repository/skill reads
  work; permission settings were not changed.
- The full browser sweep passes all114 curated pages at1440px and390px,
  including all1,197 edge entries, graphless discussions, unique anchors,
  evidence opening/closing, no page-wide horizontal overflow and no JavaScript
  errors. Its case array exactly matches all114 overlays and their edge counts.
  README corpus verification and `git diff --check` pass. The original
  checkout remains unchanged. No commit,push,merge,source-pin capture,
  full publication-QC pass or corpus-wide completion is claimed.

PF01939 retained provenance:

- Review bundle:
  `reviews/structured/20261012T055417Z-pf01939-nucs-domain-boundaries-and-conflicting-cleavage-contexts/review.yaml`
  and its derived `review.md`; review session05:54:12Z-05:54:17Z.
  Semantic digest:
  `e67c3c5ef9296a17643e5b08e9184f9ed84c1f23d7a554c83dcd5aa76b06cf9b`.
  Canonical CREATE and REVIEW events:
  `history/records/PF01939/2026-10-12T054300Z-codex-7ca2fe.yaml` and
  `history/records/PF01939/2026-10-12T055441Z-codex-b73c1e.yaml`.
- Nine graphs contain33 OBSERVED edges:15 DIRECT,7 INDIRECT and11
  UNRESOLVED, across7 MECHANISTIC and2 PHENOTYPIC contexts. Six evidence
  ledgers and two OPEN discussions retain the primary claims and limits.
  Status remains IN_PROGRESS; the same-agent review is partial and
  pass_with_limitations/native NEEDS_FOLLOWUP, not expert endorsement.
- Q9V2E8/PAB2263 maps PF01939 126-244, Q5JER9/TK1898 maps131-245,
  and Q8NR49/Cgl NCgl1168 maps110-230. NCBI Gene1019198 confirms the
  NCgl1168/currentCGL_RS06055/RefSeq/UniProt identity chain. The separate
  PF21003 N-terminal domain contains PabR42/W75. Tko QKTLF248-252 is
  outside today's PF01939 match. Whole-protein effects do not demonstrate
  isolated-domain sufficiency.
- Both2018 Cgl studies use ATCC13032, not different strains, but report
  five- versus three-nucleotide overhangs under different biochemical
  conditions. The cause is unresolved. Ishino removes five terminal
  residues; Takemoto removes two. Native mutation FREQUENCY and
  fluctuation-derived RATE are separately represented. No universal
  Mn-only requirement, clamp-alone cleavage or native DSB-to-HR chain
  is inferred. Later short-patch repair studies remain scoped follow-ups.
- Pab Figures4/5; Tko Figures2/3/6/8/S6; IshinoCgl Figures1/3/4; and
  TakemotoCgl Figures1/2/S3/S4 were visually inspected. Remaining figures,
  exact assay constructs, other members and raw-data questions are open.
  Pab2012 full-text attempts returned500/reCAPTCHA, not evidence of absence.
- Final native reconstruction checks all8,296 projections with zero drift.
  Schema generation is current;131 reviews,250 history files and123
  structured bundles validate. The256 focused tests pass in133.70s.
  All8,296 inventory digests and115 latest scoped review/input hashes
  match; imported identity and exact rendered JSON are preserved.
  Totals:115 IN_PROGRESS,8,181 SEEDED,110 graph-bearing,8,186 graphless,
  591 graphs and1,230 edges:1,214 OBSERVED,14 HYPOTHESIZED,1 INFERRED
  and1 CONTESTED. Counts are not independent-experiment or completion counts.
- Export apply/check succeeds after all projection writes finish. All38
  export tests pass in162.03s with one upstream LinkML deprecation warning.
  Row counts remain16,534 KGX nodes,8,238 identity edges and8,238 SSSOM
  mappings. Updated byte counts and hashes are in [exports.md](exports.md).
  These identity exports do not contain causal mechanism edges.
- PF01939 passes1440px and390px interaction checks. Eight scope,edge,
  evidence and uncertainty captures were visually inspected; mobile tables
  scroll internally. Desktop edge/evidence captures are byte-identical:
  `35862a77293154e5de3db2e78045eeaa4f44f64d1c7d4a48c8bd1fc87a60d3d9`.
  Chromium still requires the narrowly approved local-file retry after
  macOS Mach-port error1100; filesystem reads themselves work normally.
  No permission configuration was changed.
- The full Chromium sweep passes all115 curated pages and1,230 edge
  entries at1440px and390px, including evidence opening/closing, unique
  anchors, support labels, graphless discussions, no page overflow and no
  JavaScript errors. The parsed case list exactly matches the115 overlays
  and every edge count. README corpus verification and diff whitespace
  checks pass. Historical checkpoint counts above are not rewritten.
- Original checkout and frozen source inputs are unchanged. No commit,
  push, merge, source-pin capture, full publication QC or corpus-wide
  completion is claimed. PF01940 is the next ascending uncurated record.

PF01940 retained provenance:

- Review bundle:
  `reviews/structured/20261012T061754Z-pf01940-duf92-separated-plant-and-mammalian-causal-contexts/`.
  Its current semantic digest is
  `f3ca784db37846a4c0cebb27cad5a0ec3109c3588e6f775e436eabaf33ae508e`.
  Canonical CREATE and REVIEW events are
  `history/records/PF01940/2026-10-12T061457Z-codex-e87cd3.yaml` and
  `history/records/PF01940/2026-10-12T061811Z-codex-e5508e.yaml`.
- Thirteen graphs contain 33 edges: 32 OBSERVED and one HYPOTHESIZED;
  three DIRECT, eighteen INDIRECT and twelve UNRESOLVED. Three MECHANISTIC,
  nine PHENOTYPIC and one HYPOTHETICAL context retain six evidence ledgers
  and two OPEN discussions. IN_PROGRESS and the same-agent partial review
  are not a full-family PASS or independent expert endorsement.
- VTE6/Q9SYM0 PF01940 97-316 and PGR/Q0WP96 15-276 are different plant
  loci. Human Q96HH6 and mouse Q91W52 map 60-321. Mouse TMEM19 was
  expressed in human HEK293T for the probe-validation assay; human MPC
  knockdown and rd10 retinal experiments are separate contexts.
- VTE6 crude-extract activity is not purified-enzyme or isolated-domain
  sufficiency. Coupled phytol conversion requires VTE5/VTE6 and CTP.
  Double-mutant growth suppression is incomplete, with tocopherol deficiency
  remaining; phytyl-P toxicity is a hypothesis with free-phytol alternatives.
  PGR expression/greening is not glucose binding or transport. bHLH34
  regulates PGR expression without establishing PGR mediation of every
  regulator phenotype. TMEM19 modified-probe engagement is not a native
  ligand-affinity or receptor-activation assay. VEGF/TNF control induction
  is NS; fixed-eye assignment, unpaired statistics and caption discrepancies
  remain visible rather than being silently resolved.
- VTE6 Figures 2-8, PGR2011 public Figures 4/5, PGR2017 Figures 2/5 and
  TMEM19 Figures 4/5 were visually inspected. Supplementary ZIP integrity
  passed for PGR2017 and TMEM19, not exhaustive supplement/raw-data review.
  VTE6 supplement access returned HTML; VTE6 2017 full-text endpoints
  returned 403; PGR2011 PDF access returned a subscription preview. These
  are coverage limits, not evidence of biological absence.
- Final native reconstruction validates all 8,296 projections with zero
  drift. Schema generation is current; 132 native reviews, 252 history files
  and 124 structured bundles validate. All 256 focused tests pass in 114.32s.
  Inventory digests for all 8,296 records and current review/input hashes
  for all 116 curated families match; imported identity and exact rendered
  JSON are preserved. Totals: 116 IN_PROGRESS, 8,180 SEEDED, 111 graph-bearing,
  8,185 graphless, 604 graphs, 1,263 edges: 1,246 OBSERVED, 15 HYPOTHESIZED,
  one INFERRED and one CONTESTED. These are not completion counts.
- Export apply/check succeeds after projection writes finish; all 38 export
  tests pass in 120.28s with one upstream LinkML deprecation warning.
  Identity-export rows remain 16,534 KGX nodes, 8,238 identity edges and
  8,238 SSSOM mappings. Updated byte counts/hashes are in [exports.md](exports.md).
  These identity artifacts do not export causal edges.
- PF01940 passes 1440px/390px interaction checks. Eight scope, edge,
  evidence and uncertainty screenshots were visually inspected; mobile
  tables scroll internally. Desktop edge/evidence screenshots are identical:
  `d9cead0be9f60e9bd4103170b2f9663ba45e62889e559bb90cf834eef3615c10`.
  The normal Chromium launch still fails macOS Mach-port registration 1100;
  the narrowly approved local-file retry works. Filesystem reads work and
  permission configuration was not changed.
- The complete browser sweep passes all 116 curated pages and 1,263 edge
  entries at both widths, checking unique anchors, evidence opening/closing,
  support labels, graphless discussions, page overflow and JavaScript errors.
  The parsed browser case list exactly matches the 116 overlays and their
  edge counts. README corpus and diff-whitespace checks pass. Earlier
  checkpoint counts remain historical observations, not rewritten results.
- Original checkout and frozen source inputs are unchanged. No commit, push,
  merge, source-pin capture, full publication QC or corpus completion is
  claimed. PF01941 is the next ascending uncurated record; all earlier
  follow-ups remain in scope.

PF01941 retained provenance:

- Review bundle:
  `reviews/structured/20261012T064400Z-pf01941-mat-separated-enzyme-denaturation-and-cascade-contexts/`.
  Its current semantic digest is
  `ad463013c0af48de0186002019bbf27e3f82b5dd05d8038b89bf73d29152f30a`.
  Canonical CREATE and REVIEW events are
  `history/records/PF01941/2026-10-12T063057Z-codex-835899.yaml` and
  `history/records/PF01941/2026-10-12T064422Z-codex-c2a818.yaml`.
- Eight graphs contain twelve OBSERVED edges: seven DIRECT preparation-level
  relations and five UNRESOLVED perturbation effects. Four MECHANISTIC and
  four PHENOTYPIC contexts retain five evidence ledgers and two OPEN
  discussions. The scientific self-review is partial; IN_PROGRESS does not
  indicate full-family coverage or independent expert endorsement.
- Q5JF22/TK0545 maps PF01941 6-401; its 405-aa sequence exactly matches
  YP_182958.1 despite the 2013 paper's 1155-bp statement. Q58605/MJ1208
  maps PF01941 2-402. PDB 7P82 has a 20-residue His-tag prefix followed
  by the exact Q58605 core with L147A/I351A. Earlier mutant sites also
  match native-core numbering; historical assay batches are not resequenced.
- TkMAT SAM HPLC is not a phosphate-release-order experiment. MjMAT urea
  activity and sedimentation use different conditions; conflicting gel-filtration
  behavior is retained. W387F-Y226W and W387F-Y233W are double mutants,
  not isolated tyrosine substitutions. PC-MjMAT's ONB-TA signal includes heat
  breakdown of AdoONB; the 308-fold endpoint comparison is not kcat/Km.
  Cap-analog products require complete Ecm1/MTAN cascades, not MAT alone.
  The later divergence paper's Q58868/Q58605 misassignments remain visible.
- TkMAT Figure 3 and supplemental S2-S3, MjMAT Figures 3-4, PC-MjMAT
  Figures 1/3 and supplemental S8-S11 were visually inspected. Both
  supplementary ZIP integrity checks pass; relevant Methods were read,
  not every supplementary dataset. Earlier kinetics, SsoMAT/PfMAT,
  ancestral constructs, bacterial members and remaining assay contexts
  remain open. Access failures do not establish biological absence.
- Final native reconstruction validates all 8,296 projections with zero
  drift. Schema generation is current; 133 native reviews, 254 history files
  and 125 structured bundles validate. All 256 focused tests pass in 135.37s.
  All inventory digests and all 117 current review/evidence hashes match;
  imported identities and exact rendered JSON are preserved. Totals are
  117 IN_PROGRESS, 8,179 SEEDED, 112 graph-bearing, 8,184 graphless,
  612 graphs and 1,275 edges: 1,258 OBSERVED, 15 HYPOTHESIZED, one INFERRED
  and one CONTESTED. These are structural and partial-review counts.
- Export apply/check succeeds after projection writers finish. All 38 export
  tests pass in 151.87s with one upstream LinkML deprecation warning.
  Identity-export row counts remain 16,534 nodes, 8,238 edges and 8,238
  mappings; [exports.md](exports.md) retains current byte counts and hashes.
  Identity exports do not contain causal edges.
- PF01941 passes 1440px/390px interaction checks. Eight scope, edge,
  evidence and uncertainty screenshots were visually inspected. Mobile
  tables scroll internally. Desktop edge/evidence screenshots are identical:
  `6bec8ad02f8c063fa022e9622fb37fa22c0adc6ef9d4cac3e151cad79cd7d8ff`.
  Normal Chromium startup still fails macOS Mach-port registration 1100;
  the narrowly approved local-file retry works. No permission configuration
  was changed; filesystem reads work.
- The full Chromium sweep passes all 117 curated pages and 1,275 edge
  entries at both widths, checking unique anchors, evidence toggles, scope
  qualifications, support labels, graphless discussions, page overflow and
  JavaScript errors. Its parsed case set exactly matches every overlay and
  edge count. README corpus and diff-whitespace checks pass. Earlier
  checkpoint counts remain historical, not rewritten results.
- Original checkout and frozen source inputs are unchanged. No commit,
  push, merge, source-pin capture, full publication QC or corpus completion
  is claimed. PF01944 is the next ascending uncurated record; all earlier
  follow-ups remain in scope.

PF01944 retained provenance:

- Review bundle:
  `reviews/structured/20261012T071012Z-pf01944-spoiim-scoped-localization-and-suppressor-effects/`.
  Actual review interval: 2026-10-12T07:09:40Z to 07:10:12Z. Native verdict
  NEEDS_FOLLOWUP, common pass_with_limitations, partial scientific self-review.
  Semantic digest:
  `37d4fb0a0ef816380b811698df31f1d623fc175549eb7a60ccf99d073bb1b2da`.
- Canonical CREATE and REVIEW events:
  `history/records/PF01944/2026-10-12T070006Z-codex-986f23.yaml` and
  `history/records/PF01944/2026-10-12T071024Z-codex-265c5e.yaml`.
  The initial review draft's unsupported `partially_supported` term was
  rejected before saving and corrected to `concern`; no earlier retained
  report was rewritten. Two OPEN discussions and five hash-bound ledgers
  retain the incomplete member, construct and source coverage.
- Eight PHENOTYPIC graphs contain ten OBSERVED experimental effects, all
  UNRESOLVED in molecular directness. Reporter promoter/locus, partner
  mutation, abundance, initial septal targeting, leading-edge positioning
  and conditional I92T suppression are kept distinct. No M hydrolase
  activity or directly demonstrated M-P interface is asserted.
- P37873 v1 maps PF01944 25-203; it is a strain-168 reference for PY79
  experiments, not independent historical clone sequencing. Current I92
  and K82 constrain the I92T/I82T discrepancy without silently correcting
  the paper. Aung Figure 3D KP722/KP764 and Chastanet Abs292/Abs216 labels
  remain open. C. difficile CD1221 resolves to Q18B81 by locus, but current
  Pfam membership/coordinates remain unconfirmed; candidate observations
  are retained outside the canonical graph, with assay differences intact.
  LcyD full Methods/member mapping and archaeal member mechanisms remain open.
- Aung Figure 3 and Ribis Figure 2 were visually inspected. Chastanet
  primary full text, Methods and captions and selected Dembek XML sections
  were inspected, but their figure images and supplements remain outside
  the completed visual review. Wiley HTTP403, supplement HTML/XML error
  responses and a timed-out download are access limits, not negative results.
- All 8,296 projections validate with zero drift after history regeneration;
  schemas have zero drift. There are 134 valid native reviews, 256 canonical
  history files and 126 valid structured bundles. All 256 focused tests pass
  in 144.33s; all 38 export tests pass in 122.42s with one upstream LinkML
  warning. Export apply/check succeeds after projection writers finish;
  current row counts, bytes and hashes in [exports.md](exports.md) match.
- All inventory digests and all 118 latest review/evidence hashes match;
  imported identity and exact rendered JSON are preserved. Counts are
  118 IN_PROGRESS, 8,178 SEEDED, 113 graph-bearing, 8,183 graphless,
  620 graphs and 1,285 edges: 1,268 OBSERVED, 15 HYPOTHESIZED, one INFERRED
  and one CONTESTED. These are structural counts and partial reviews.
- PF01944 passes 1440px/390px interaction checks. All eight scope, edge,
  evidence and uncertainty captures were inspected. Mobile tables scroll
  internally; desktop edge/evidence captures are byte-identical with SHA256
  `22b1b784f95f8d024dc48a48d45455b2423bce21437a7e7a29b489a38f7f165d`.
  Normal Chromium launch fails macOS Mach-port registration 1100; the
  approved local-file-only retry works without changing permission settings.
  The preview test was corrected to check the 26%/78% mechanism values
  after expanding their evidence panel; no product code was changed for it.
- The full Chromium sweep passes all 118 curated pages and 1,285 edge
  entries at both widths. Its parsed case set exactly matches every overlay
  and edge count. Unique anchors, evidence toggles, support labels, scoped
  limitations, graphless discussions, overflow and JavaScript errors are
  checked. All required processes finished; diff-whitespace checks pass.
- Original checkout, frozen worklists and configuration remain unchanged.
  README corpus and documented export-digest checks pass. No commit, push,
  merge, source-pin capture, full publication QC or full family/corpus
  completion is claimed. PF01947 is the next ascending uncurated record;
  all prior open follow-ups remain in scope.

PF01947 retained provenance:

- The authoritative partial review is
  `reviews/structured/20261012T073748Z-pf01947-scoped-lyase-and-sll1797-phenotype-effects/review.yaml`,
  with native-derived `review.md`. The scientific self-review ran from
  07:37:29Z to07:37:48Z on2026-10-12 and retains NEEDS_FOLLOWUP,
  pass_with_limitations and the open `pf01947-causal-context-coverage` finding.
  Semantic digest:
  `89760744789491d34689bc0fed02126c015f1e6b5cb85ca14658c6c4f1cfc566`.
- Actual CREATE and REVIEW sidecars are
  `history/records/PF01947/2026-10-12T072814Z-codex-c15c30.yaml` and
  `history/records/PF01947/2026-10-12T073801Z-codex-047e12.yaml`.
  Five ledgers under `evidence/PF01947/` retain identity, Stadthagen2005,
  Pfaff2014, Du2025 and source coverage. No old review or source pin changed.
- Nine graphs retain fourteen OBSERVED experimental edges: five DIRECT
  product-conversion edges and nine UNRESOLVED effects. Rv2949c tag/host
  preparations are separate; coupled pyruvate detection is not direct
  chromatography. Product inhibition is a reduced assay readout, not a
  demonstrated binding mode or native feedback mechanism. Sll1797 has a
  measured4HB edge; no pyruvate edge is added without an independent measurement.
- P9WIC5 v1 maps PF01947 24-173; P73322 v1 maps2-130. E. coli UbiC/P26602
  maps PF04345 17-165. Reference strain, expression host and native assay
  strain are distinguished. R30/E120 remain proposals; archaeal2NWI and
  MJ0807 mappings do not establish catalytic function. The imported Hashimi
  citation and later PlqC paper's inconsistent locus labels remain visible.
- Pfaff Figures4/5/6/9 were visually inspected. Its M56/M59 discrepancy,
  Table1 units,4HB feeding history and OD-versus-cell normalization remain
  unresolved. Native growth rescue does not establish PQ rescue, and PQ,
  oxygen and growth are not joined into a direct chain. Du's independent
  markerless deletion uses another PCC6803 background; Figure2 caption E/F
  conflicts with Results D/E. Stadthagen and Du images remain unavailable;
  their primary text/Methods/captions were inspected. Missing access is not
  a negative finding. Only non-operational cell-free mycobacterial chemistry
  is curated; no pathogen-engineering workflow is reproduced.
- Final native loading reconstructs all8,296 schema-valid projections with
  zero drift; schema-only checks are current. Validation covers135 native
  reviews,258 canonical history files and127 structured bundles. The focused
  suite passed256 tests in199.75s. Exports are current and their38 tests
  passed in154.12s after all projection/export writes ended, with one existing
  upstream LinkML deprecation warning. Documented export rows/bytes/hashes match.
- All8,296 inventory digests and all119 latest review/evidence hashes match;
  imported fields and exact rendered JSON are preserved. Current totals:
  119 IN_PROGRESS,8,177 SEEDED,114 graph-bearing,8,182 graphless,629 graphs
  and1,299 edges:1,282 OBSERVED,15 HYPOTHESIZED,one INFERRED,one CONTESTED.
  These are structural counts and partial scientific reviews, not completion.
- Full Chromium checks pass all119 curated pages and1,299 edges at1440px
  and390px. The case set exactly matches every overlay and edge count.
  Unique IDs, evidence toggles, support labels, context limits, graphless
  discussions, page overflow and JavaScript errors are checked. All eight
  PF01947 screenshots were inspected; mobile tables scroll internally.
  Desktop edge/evidence captures are identical with SHA256
  `b11c3ee1b8eb7b0a2884e391a6f367643a1fca3dd0e1f5a1a2c5b7e475b66633`.
  Sandboxed Chromium still fails macOS Mach-port registration1100; the approved
  local-file-only retry passes without permission-setting changes.
- Original checkout, frozen worklists and configuration remain unchanged.
  No commit, push, PR, merge, source checkpoint, publication or full QC pass
  is claimed. PF01949 is next; all records and prior follow-ups remain in scope.

PF01949 retained provenance:

- The authoritative partial review is
  `reviews/structured/20261012T080813Z-pf01949-scoped-endodu-cleavage-and-cellular-effects/review.yaml`,
  with native-derived `review.md`. It ran08:05:29Z-08:08:13Z on2026-10-12,
  retaining NEEDS_FOLLOWUP, pass_with_limitations, self-review and the open
  `pf01949-causal-context-coverage` finding. Semantic digest:
  `a0b9038d11bef272649fabc5b6f97bb83f8137118391b32fafbb1fb03fb31f06`.
- Actual CREATE and REVIEW sidecars are
  `history/records/PF01949/2026-10-12T075615Z-codex-5d5411.yaml` and
  `history/records/PF01949/2026-10-12T080833Z-codex-0cffa7.yaml`.
  Five ledgers under `evidence/PF01949/` retain identity, cleavage,
  perturbation, cellular and coverage evidence. No past review was modified.
- Twelve graphs retain nineteen OBSERVED effects: seven DIRECT product
  edges and twelve UNRESOLVED effects, in seven MECHANISTIC and five
  PHENOTYPIC graphs. Each tested homolog and ssDNA/dsDNA context stays
  separate. Zinc precipitation, reaction versus preincubation temperature,
  salt labels and assay negatives do not become resolved catalytic mechanisms.
- Main Figures2-8 and supplementS3/S4/S5/S6/S9/S11/S12/S13 were inspected.
  EuropePMC supplied the valid13-page supplement after earlier HTML/403
  responses. Figure7E labels H166R while Results/S11 label H166A; D10A
  retains activity. This is a preparation-level loss, not an independently
  demonstrated H166 single-residue requirement or obligatory D10 catalysis.
- Afu reference O28839 v1 maps3-172; Loki A0A524DLA3 maps8-185 and Thor
  A0A524EN15 maps22-197. Halo/Gm have primary DUF99 assignment but unresolved
  current Pfam boundaries. HVO_0443/D4GRY4 maps26-197; S12 termini and the
  24-bp UDG gap support mapping without claiming full H26 allele reconstruction.
  Partial deletion, relative TPM and OD600 remain distinct from a full null,
  absolute transcription, viable count or complete DNA-repair chemistry.
- Final native reconstruction validates all8,296 projections with zero drift;
  schema artifacts are current. Validation covers136 native reports,
  260 history files and128 structured bundles. Focused tests pass256 in140.87s;
  export tests pass38 in105.20s, after projection/export writers terminated.
  One upstream LinkML deprecation warning remains. Exports reproduce exactly;
  documented row counts, byte sizes and hashes match.
- All8,296 inventory digests, all120 latest review/evidence hashes, imported
  identities and rendered JSON records match. Totals are120 IN_PROGRESS,
  8,176 SEEDED,115 graph-bearing,8,181 graphless,641 graphs and1,318 edges:
  1,301 OBSERVED,15 HYPOTHESIZED,one INFERRED,one CONTESTED.
  Counts are not numbers of independent experiments or completed family reviews.
- Full Chromium verification passes all120 curated pages and1,318 edge entries
  at1440px and390px, including unique IDs, evidence toggles, support labels,
  context distinctions and no page overflow or JavaScript errors. The case
  array exactly matches the overlay set and per-family edge counts. All eight
  PF01949 captures were visually inspected; mobile tables scroll internally.
  Desktop edge/evidence captures share SHA256
  `f34b0d31754d6a929e2cb0ee61311c3ad7f79660b859ae63db8700d2d0d7fc46`
  because the evidence column fits. Sandboxed launch still fails macOS
  Mach-port registration1100; the approved local-file-only retry passes.
  No permission settings were changed.
- Original checkout, frozen worklists and configuration remain unchanged.
  No commit, push, PR, merge, source checkpoint, publication or full QC pass
  is claimed. PF01950 is next; all records and prior follow-ups remain in scope.

PF01950 retained provenance:

- Began 2026-10-12T08:17:30Z. Frozen FBPase_3/former DUF100 identity,
  EX_DUF/UNSCORED status and source snapshots remain unchanged. Q8NKR9 v1
  maps PF01950 at 6-372; historical AB081839.1/BAC10571.1 links the
  biochemical protein to TK2164, not the separate class-IV Imp protein.
- Five graphs retain eight OBSERVED experimental effects: one MECHANISTIC
  graph with a DIRECT F6P product edge, and four PHENOTYPIC graphs with
  seven UNRESOLVED cellular effects. Synthetic-medium growth, rich-medium
  extracts and different-phase RNA samples are not joined into an observed
  intracellular chain. Carbon-regimen substitution is not direct inhibition.
- Sato2004 Methods/Results/Discussion and Tables1/2 were read; Figures2-4
  were visually inspected. Primary quotations and all eight edge cache
  hashes were checked against the public article and retained ledgers.
  Amino-acid-only growth is a reported result without a plotted curve.
  No fbp reintroduction or selective-activity rescue was identified.
- Later bifunctionality is retained as a necessary follow-up, not denied.
  Fushinobu2011 supplement text and selected Say2010 supplement sections
  were inspected; their main Methods and the Du2011 primary work remain
  unreviewed. ST0318 3R1M residues2-385 exactly match F9VMT6 v1 residues1-384,
  explaining paper Lys232/Tyr229 versus current Lys231/Tyr228. No residue
  mechanism is inferred merely from that numbering or static structures.
- Six ledgers under `evidence/PF01950/` and three OPEN discussions retain
  access outcomes, construct/assay limits, cellular causation and member
  coverage. All earlier follow-ups and all 8,296 records remain in scope.
- Scoped same-agent review ran 08:30:56-08:33:50Z and is retained at
  `reviews/structured/20261012T083350Z-pf01950-thermococcus-hydrolysis-and-conditional-effects/`.
  Semantic digest:
  `6029671d96f8a16ce2d1bda2ba8c9aca2ad0e3720b47c169335290c39f8ff1fa`.
  Verdict is NEEDS_FOLLOWUP/pass_with_limitations with partial scientific
  coverage; IN_PROGRESS is not promoted to REVIEWED.
- Canonical CREATE and REVIEW events are
  `history/records/PF01950/2026-10-12T081730Z-codex-0a2935.yaml` and
  `history/records/PF01950/2026-10-12T083413Z-codex-3a7b55.yaml`.
  Native generation projects both; retained review proof remains valid.
- Final native reconstruction validates all 8,296 projections with zero
  drift; generated schemas, 137 native reports, 262 history files and 129
  structured bundles pass. Focused tests pass 256 in 159.42s; export tests
  pass 38 in 120.16s with one upstream LinkML deprecation warning. Export
  tests ran after projection/export writers ended; exports check current.
- All 8,296 inventory digests, 121 latest scoped review/evidence hashes,
  imported identities and rendered JSON records match. Totals are 121
  IN_PROGRESS, 8,175 SEEDED, 116 graph-bearing, 8,180 graphless, 646 graphs
  and 1,326 edges: 1,309 OBSERVED, 15 HYPOTHESIZED, one INFERRED and one
  CONTESTED. These are structural counts, not independent experiments or
  completed family reviews. Export row counts/bytes/hashes match the docs.
- Full Chromium verification passes all 121 curated pages and 1,326 edge
  entries at 1440px and 390px, including unique anchors, evidence toggles,
  support labels, context distinctions and no page overflow or JavaScript
  errors. The parsed case list exactly matches every overlay and edge count.
  All eight PF01950 desktop/mobile captures were visually inspected.
  Evidence expands and mobile tables scroll internally without page-wide
  overflow. Desktop edge/evidence captures share SHA256
  `340aba938cf0e1940ef5ee07f3eee8f2ced1811e88514d4a998dab1c3bbfbcb5`
  because the evidence column fits. Filesystem reads work; sandboxed
  Chromium still fails macOS Mach-port registration1100, while the approved
  local-file-only retry succeeds. No permission settings were changed.
- Original checkout, worklists and configuration remain unchanged. No
  commit, push, PR, merge, source checkpoint, publication or full QC pass
  is claimed. PF01951 is next; PF01950 and earlier follow-ups remain open.

PF01951 retained provenance:

- Curation session began 2026-10-12T08:52:08Z. Frozen Archease/former DUF101
  identity, EX_DUF/UNSCORED and source snapshots remain unchanged. Q8IWT0 v2
  maps PF01951 31-167; paper D51/K156 are canonical D39/K144, verified by
  exact 8BTX entity17-183 to Q8IWT0 sequence equality. O59205 v1 maps4-142;
  the cloning-inserted leucine does not change the paper's native numbering.
- Nine graphs retain seventeen OBSERVED effects: six MECHANISTIC graphs with
  nine DIRECT biochemical edges and three PHENOTYPIC graphs with eight
  UNRESOLVED mutant/cellular edges. Activation, cleaved-XBP1 ligation,
  isolated-intron circularization, modified RNA-ppG, nucleotide substitution,
  day3 RNA ratios/stress outputs and day8 mature-tRNA signal remain distinct.
- Primary Gerber2024 Figures1/5/S1/S2, Desai2014 Figures2/3/4 and Suzuki2025
  Figure3/S6/S7 were visually checked with their relevant Methods/Results.
  After retention, the cited Desai2013 RtcB purification Methods were also
  checked in the public author PDF, page2, confirming untagged BL21 expression:
  `https://raineslab.com/sites/default/files/labs/raines/pdfs/Desai2013a.pdf`.
  No scientific correction was required by that cross-check.
- Five ledgers and three OPEN discussions retain remaining bacterial turnover,
  Thermus clone identity, PAB1946 methyltransferase support, original human,
  fly, yeast and additional-member evidence. Their acquisition is not counted
  as completed review; all earlier family follow-ups remain open.
- Partial same-agent review ran 09:01:17-09:03:04Z:
  `reviews/structured/20261012T090304Z-pf01951-archease-scoped-activation-and-rna-processing/`.
  Digest `f2f16a113ab9d83bda5df8085be34939f7fab670a6ce338122200bed708fcbe6`;
  NEEDS_FOLLOWUP/pass_with_limitations, IN_PROGRESS, no independent endorsement.
  Actual CREATE/REVIEW events are
  `history/records/PF01951/2026-10-12T085208Z-codex-b29ac6.yaml` and
  `history/records/PF01951/2026-10-12T090330Z-codex-1d461a.yaml`.
- Final native reconstruction checks all 8,296 projections with zero drift.
  Schema generation, 138 native reviews, 264 history files and 130 structured
  bundles pass. Focused tests: 256 passed in 164.20 s; exports: 38 passed
  in 91.64 s with one upstream LinkML warning, after all writers ended.
  Exports reproduce; documented row counts, bytes and SHA256 values match.
- Inventory and all 122 latest review/evidence digests, preserved identities and
  exact rendered JSON pass. Counts: 122 IN_PROGRESS, 8,174 SEEDED;
  117 graph-bearing, 8,179 graphless; 655 graphs, 1,343 edges;
  1,326 OBSERVED, 15 HYPOTHESIZED, one INFERRED, one CONTESTED.
  Counts do not establish scientific completion.
- Full Chromium checks pass all 122 curated pages at 1440px and 390px with
  unique anchors, evidence toggles, support labels and no page-wide overflow
  or JavaScript errors. All eight new desktop/mobile captures were inspected.
  Desktop edge/evidence captures are identical because the evidence fits:
  SHA256 `59b141332a9d4918a73ee3831e561b33c6ad6513860de6df77d586d72c0df8aa`.
  Sandbox Mach-port1100 failure persists; the approved local-file-only run
  passes. Filesystem reads work and no permission settings were changed.
- Original checkout, worklists and configuration remain unchanged. No commit,
  push, PR, merge, source checkpoint, publication or full QC pass is claimed.
  Remaining PF01951 branches are next; all 8,296 records stay in scope.

PF01951 archaeal-mutant and methyltransferase follow-up:

- Desai2014 Figures 5-7 and supplement S4/S5 were visually inspected. Eleven
  Archease-mutant effects are separated by GTP/ATP; E8A is not assigned a GTP
  decrease. Six WT-Archease additions restore selected mutant RtcB outputs;
  F204A rescue is GTP-specific and D95A RNA-ppG recovery is not ligation rescue.
  S5 purity is not folding verification, and partner mutations are not assigned
  to Archease. O59205 native residue identities were checked independently.
- Auxilien2007 Methods, Results, Figure 5/6/9 captions and Table 1 support nine
  scoped PAB1946 effects on methylation, affinity and aggregation. Author PDF
  and figure retrieval returned 403, so no visual or raw-gel audit is claimed.
  Q9V105 v1 maps PF01951 4-142; graph taxon is P. abyssi species 29292, not an
  unconfirmed GE5 assay strain. Table 1/Figure 2D fragment-length discrepancies
  and Methods/Figure 6 RNA concentration disagreement remain explicit.
- The original nine graphs/seventeen edges and five evidence ledgers are
  unchanged. Four additional ledgers and a fourth OPEN discussion retain the
  follow-up. Current PF01951 content has nineteen graphs/forty-three OBSERVED
  edges: twenty-four DIRECT, nineteen UNRESOLVED; fourteen MECHANISTIC and five
  PHENOTYPIC graphs. No unmeasured mediation chain connects distinct assays.
- The same-agent partial scientific review ran 09:29:13-09:30:10Z and is retained
  at `reviews/structured/20261012T093010Z-pf01951-archease-mutants-and-methyltransferase-support/review.yaml`
  and its native-derived Markdown. Current digest:
  `5f05696c89ed8cb2208773f9b4e2530c6c3853f09b5fd2b531fb8c27a857bd6c`.
  The predecessor and its OPEN `pf01951-causal-context-coverage` finding are
  explicitly referenced; NEEDS_FOLLOWUP/IN_PROGRESS is unchanged.
  Actual EDIT/REVIEW events are
  `history/records/PF01951/2026-10-12T091810Z-codex-557925.yaml` and
  `history/records/PF01951/2026-10-12T093129Z-codex-ff77c0.yaml`.
- Native reconstruction verifies all 8,296 projections with zero drift. Schema,
  139 native reports, 266 history files and 131 structured bundles validate.
  Focused tests passed 256 in 102.18 s; export tests passed 38 in 151.39 s,
  with one upstream LinkML deprecation warning. Export apply/check and documented
  row/byte/SHA values match; identity exports remain unchanged.
- Inventory digests, all 122 latest review/evidence hashes, preserved imported
  identities and rendered JSON match. Current totals are 122 IN_PROGRESS,
  8,174 SEEDED; 117 graph-bearing, 8,179 graphless; 665 graphs/1,369 edges,
  of which 1,352 are OBSERVED, fifteen HYPOTHESIZED, one INFERRED and one CONTESTED.
- Full Chromium checks pass all 122 curated pages at 1440px and 390px, including
  all 1,369 edges, unique anchors, evidence controls, support labels and absence
  of page-wide overflow or JavaScript errors. Sixteen PF01951 captures were
  inspected, including the new mutant and methyltransferase rows and fully
  scrolled evidence columns. Mobile tables intentionally scroll horizontally;
  a partial column at an intermediate scroll position is not absent content.
  The local-file-only run blocked HTTP requests and used approved execution
  outside the macOS Chromium sandbox. Filesystem reads work; no permission
  settings changed. The original checkout retains its pre-existing untracked
  files only; worklists and configuration remain unchanged.
- Remaining Archease work includes Desai2015 bacterial turnover/clone mapping,
  original human and fly perturbations, other cellular/regulatory contexts,
  Auxilien figure access and source discrepancies. All earlier follow-ups and
  all 8,296 records remain in scope. No publication or full QC pass is claimed.

PF01951 bacterial-turnover and human-rescue follow-up:

- Desai2015 Figures 1-4 and Methods now support Thermus rate acceleration,
  cross-species P. horikoshii activation and substrate-excess repeated ligation.
  Thermobifida's small reported 7% inhibition and 19% activation remain visible
  without significance claims or comparable multiple-turnover activation.
  RNA starts linear; ATP-negative and incomplete-conversion results remain
  explicit. Coevolution and metal-positioning interpretations are not edges.
- Thermus Q5SHI5/Q72HV1 v1 both map PF01951 6-139, but neither accession or
  strain is assigned to the unidentified assay clone. Human 2014 FLAG/pDONR
  and pET28a primers imply different N termini; ED4 canonical D39/K144 labels
  do not establish complete recombinant mutant sequences.
- Popow2014 main Methods/Results and all Extended Data captions were read;
  Figures 1/3/4 and ED3/4/5/6/10 images inspected. Human initial activation,
  delayed restart, dose response, guanylylation and joint GTP/Archease effects
  remain separate from mutant outputs, HeLa extract depletion/rescue and mature
  tagged yeast-tRNA abundance in human cells. Purified complex is not isolated
  RTCB; stock buffer is not final assay buffer; purity is not mutant folding.
- All nineteen prior graphs, forty-three edges and nine ledgers are unchanged.
  Thirteen new graphs add nineteen OBSERVED edges, ten DIRECT and nine
  UNRESOLVED. Current PF01951 totals are thirty-two graphs/sixty-two edges:
  thirty-four DIRECT, twenty-eight UNRESOLVED; twenty-three MECHANISTIC and
  nine PHENOTYPIC graphs. Four new ledgers and four OPEN discussions retain
  unresolved experiments and source discrepancies.
- Scientific self-review ran 09:55:08-09:58:19Z and is retained in
  `reviews/structured/20261012T095819Z-pf01951-bacterial-turnover-and-human-archease-rescue/review.yaml`
  and its native-derived Markdown. Semantic digest:
  `ef53bebd575702e02b73438cde815fa2054b3c8f82b3f90127a45588634d79a0`.
  The first save rejected missing search-scope metadata for two historical
  evidence entries; the corrected authored input passed the native saver.
  This did not rewrite any earlier review. NEEDS_FOLLOWUP and IN_PROGRESS remain.
- Actual EDIT and REVIEW history events are
  `history/records/PF01951/2026-10-12T095419Z-codex-81b235.yaml` and
  `history/records/PF01951/2026-10-12T095845Z-codex-e088b4.yaml`.
- Final native regeneration and inventory loading validate all 8,296 records
  with zero drift. Schema generation is current; 140 native reviews, 268
  canonical history files and 132 shared structured bundles validate.
  Focused graph/record/review/history tests pass: 256 in 88.88 s. After all
  projection/export writers ended, export checks pass and all 38 export tests
  pass in 93.75 s, with one upstream LinkML deprecation warning.
- All 8,296 inventory digests, 122 latest review digests and source hashes,
  imported identities and exact rendered JSON records match. Totals remain
  122 IN_PROGRESS and 8,174 SEEDED, 117 graph-bearing and 8,179 graphless;
  there are now 678 graphs/1,388 edges: 1,371 OBSERVED, 15 HYPOTHESIZED,
  one INFERRED and one CONTESTED. Identity-export row counts, byte counts
  and SHA-256 values still match `docs/exports.md`; no causal edges are added
  to those identity exports.
- Full Chromium checks pass for all 122 pages/1,388 edges at 1440 and 390 px,
  including exact PF01951 graph/support counts, unique anchors, evidence
  expansion/collapse and no page-wide overflow or JavaScript errors. The
  first attempt checked two effect-size strings before their evidence panels
  opened; moving those assertions after expansion yielded the full pass,
  without weakening content coverage or changing rendering code.
  All twenty-four PF01951 captures were visually inspected, including the
  bacterial-turnover and human-rescue panels and their right-scrolled evidence.
  Table scrolling is intentional; the complete evidence remains readable.
- README/docs and diff checks pass. Repository and installed-skill reads work;
  no filesystem-read denial was reproduced. The original checkout's three
  pre-existing untracked paths are unchanged. Browser checks use the narrow
  approved local-file launch, with every HTTP(S) request aborted. No permission
  configuration, frozen worklist, source pin, old review or history was edited;
  no commit, push, merge, publication or full publication-QC pass is claimed.
- Exact bacterial clones, the cited Popow2011 base protocol, human mutant
  construct sequences, DDX1/partner controls and ED7-9 images remain open,
  alongside Jurkin/XBP1, fly and other member contexts and Auxilien source
  discrepancies. All 8,296 records and all prior follow-ups remain in scope.

PF01951 partner-control and XBP1 follow-up:

- Continued at 2026-10-12T10:08:54Z with all 8,296 records and earlier findings
  still in scope. Baseline validation passed with zero projection drift.
  Four new ledgers retain Popow2014 partner controls, Jurkin2014 human XBP1/tRNA,
  DDX1 identity and bounded coverage. Thirteen predecessor evidence hashes,
  thirty-two graphs and all sixty-two earlier edges remain unchanged.
- Popow ED7-9 images were inspected with Figure3e/f and Figure4d/ED10c.
  Twelve new effects distinguish nucleotide interventions, DDX1 variants,
  reported apparent turnover and partner depletion with added Archease.
  DDX1 Q92499 v2 K52/E371 are not Archease residues; K52N RNA retention and
  CGI99/DDX1 codepletion limit molecular attribution. E271Q/E371Q and
  R557K/R577K conflicts remain explicit; no exact Arg-mutant edge was added.
  The kcat-caption multiplication/division conflict is not silently repaired.
- Jurkin Figure1/2 and S1-S3 images plus all supplement legends were inspected.
  Sixteen new effects retain extract XBP1, ambiguous preparation comparisons,
  single-Archease XBP1s protein, six joint-depletion outputs and four endogenous
  tRNA abundance effects. The provisional nonsignificant single-Archease RNA
  edge was excluded during self-review; its mean trend remains ledger-only.
  S1D normalization is buffer at two minutes, not a same-time sevenfold effect.
  Caption/Methods preparation disagreement, buffer units, template ordering
  and primer discrepancies remain unresolved. Residual protein, the late RNA
  fraction exception and nonsignificant controls prevent absolute or mediated
  pathway claims. RTCB-only mouse phenotypes are not Archease knockouts.
- Current PF01951 totals are forty-two graphs and ninety OBSERVED edges:
  thirty-eight DIRECT and fifty-two UNRESOLVED; twenty-five MECHANISTIC and
  seventeen PHENOTYPIC graphs. Seventeen ledgers and five OPEN discussions
  preserve the remaining source, construct and member-coverage questions.
  The new ten graphs contain twenty-eight edges, not the provisional twenty-nine.
- Same-agent partial scientific review ran 10:28:28-10:29:18Z and is retained at
  `reviews/structured/20261012T102918Z-pf01951-partner-controls-and-xbp1-contexts/review.yaml`
  with its native-derived Markdown. Digest:
  `1bf56920395146dba1bf21ffc513dda47f166d090b2ec224db404fd9d390f601`.
  Verdict remains NEEDS_FOLLOWUP/pass_with_limitations, with the same open
  `pf01951-causal-context-coverage` finding and IN_PROGRESS status.
  Actual EDIT/REVIEW sidecars:
  `history/records/PF01951/2026-10-12T102707Z-codex-e5acba.yaml` and
  `history/records/PF01951/2026-10-12T102956Z-codex-6e237f.yaml`.
- Native schema generation, 141 retained reviews, 270 canonical history files
  and 133 shared structured bundles validate. Focused graph/record/review/history
  tests passed 256/256 in 109.34 seconds; export tests passed 38/38 in 99.27
  seconds with the existing upstream LinkML deprecation warning. Export apply
  and check both report current; all three identity export row counts, bytes
  and hashes match `docs/exports.md` unchanged. Projection/export writers were
  serialized, and export tests ran after projection writes ended.
- Final native inventory validates all 8,296 records with zero generation drift.
  All 122 latest review digests and retained source hashes match, and every
  curated rendered JSON equals its projection with imported identity preserved.
  Counts remain 122 IN_PROGRESS, 8,174 SEEDED, 117 graph-bearing and 8,179 graphless;
  there are 688 graphs and 1,416 edges: 1,399 OBSERVED, 15 HYPOTHESIZED,
  one INFERRED and one CONTESTED. These are structural counts, not independent
  experiments or completed family reviews.
- Full Chromium checks pass for all 122 pages and 1,416 edges at 1440 and
  390 px, including exact PF01951 graph/support counts, the single-Archease
  graph's one retained protein edge, source-discrepancy text, unique anchors,
  evidence expansion/collapse and no page-wide overflow or JavaScript errors.
  Thirty-two PF01951 screenshots were produced. Twelve were visually inspected
  this checkpoint: all eight new partner/XBP1 views plus the four base/edge
  captures. Mobile tables scroll intentionally; right-scrolled evidence retains
  complete text and citations. The preceding checkpoint inspected the older
  panels, and preservation checks confirm their graph content is unchanged.
  Browser execution used a narrowly approved local-file-only launch with all
  HTTP(S) requests aborted. This is a local preview, not a published site.
- Repository, temporary-worktree and installed-skill reads succeeded without
  read escalation; the causal-graph skill passes its bundled validator.
  The earlier filesystem-read denial was not reproduced, so its original cause
  remains unconfirmed. Inspection of existing Claude settings/hooks shows a
  separate coordination-lock gate for Bash, not proof of the Codex read-denial
  cause. The bounded hook search included hidden/ignored files and found no
  matching denial wording. No hook or permission configuration was changed.
  [Official sandbox documentation](https://learn.chatgpt.com/docs/sandboxing)
  distinguishes command boundaries from approval policy.
- Final README/docs and diff checks pass. The original checkout retains only
  its three pre-existing untracked paths. No old review/history, frozen worklist,
  source pin or permission settings were edited; no commit, push, merge or
  full publication-QC pass is claimed.
- Exact human constructs, Popow2011 base protocol, Jurkin preparation/protocol
  discrepancies, fly allele/rescue/localization, additional XBP1 and other-member
  branches and Auxilien source/image gaps remain open. No full-corpus completion,
  independent expert endorsement, source-pin change or publication is claimed.

PF01954 prediction, structure and cross-family assessment:

- Native storage is supported, but the inspected AF2212 material does not
  support a directed causal effect. Five minimal evidence ledgers and three
  OPEN discussions retain this scoped graphless disposition, not an assertion
  that all 440 frozen members lack experimental characterization.
- O28071 sequence version 1 is 61 residues from A. fulgidus VC-16. Current
  InterPro maps PF01954 to 1-34; the RCSB Pfam34.0 feature maps 1-57. The 2NWT
  construct is exactly the native sequence plus LEHHHHHH, with chains A/B.
  Its 20 submitted NMR conformers are not experimental replicates. The XL-10
  source-strain field and BMRB/PDB salt metadata need reconciliation.
- Makarova2009 Results, Methods, Table2 and original Figure4C support a
  comparative prediction. Pandey2005 Methods and selected Results are a
  genome survey; their original supplementary inventories remain uninspected.
  The verified Makarova DOI is `10.1186/1745-6150-4-19`, differing from the
  InterPro citation metadata's `4-29`; frozen source bytes are unchanged.
- Li/Xu2025 SupplementFigureS2, its caption, TableS1 entries and original
  PDFpage3 were inspected. Exact locus resolution maps the four antitoxins to
  PF02697, PF26688 or PF10047, not PF01954. Host identity does not establish
  TK0335 as a tested antitoxin. The main article remains inaccessible at the
  attempted endpoint; no complete-paper or PF01954 phenotype claim is made.
- Review:
  `reviews/structured/20261012T105749Z-pf01954-af2212-prediction-structure-and-cross-family-boundaries/review.yaml`
  and sibling `review.md`; actual review 10:57:38-10:57:49Z on October12.
  Digest `353d02ad59639beefe3bcb4912cb972259e71204dc3961a15459cae71ed9da48`.
  Partial same-agent scientific review, NEEDS_FOLLOWUP/pass_with_limitations;
  status remains IN_PROGRESS. Stable finding `pf01954-causal-context-coverage`.
- Canonical CREATE and REVIEW:
  `history/records/PF01954/2026-10-12T105459Z-codex-493673.yaml` and
  `history/records/PF01954/2026-10-12T105829Z-codex-936139.yaml`.
  Additional members, later full papers, supplementary locus mappings and
  construct/metadata reconciliation remain open. No unsupported graph is added.
- Post-write verification passes: all 8,296 projections validate with zero
  generated drift; all inventory digests, 123 latest scientific-review digests
  and retained overlay/evidence hashes match. Imported identities are preserved
  and all 123 rendered JSON records equal their current YAML projections.
  Counts: 123 IN_PROGRESS, 8,173 SEEDED, 117 graph-bearing and 8,179 graphless;
  688 graphs and 1,416 edges, including 1,399 OBSERVED, 15 HYPOTHESIZED,
  one INFERRED and one CONTESTED. These are not completion counts.
- Schema generation, 142 native reviews, 272 canonical history files and 134
  shared structured bundles validate. The combined focused and export suites
  pass all 294 tests in 188.13 seconds, with one upstream LinkML deprecation
  warning. Tests ran after projection and export writers were terminal.
- Exports apply/check pass with unchanged row counts. KGX nodes and SSSOM
  each increase by five bytes for the SEEDED-to-IN_PROGRESS status change;
  KGX identity edges remain byte-identical. Current hashes are recorded in
  `docs/exports.md`; no causal edge is exported as an identity association.
- Full Chromium checks pass all 123 pages at 1440px and 390px, including all
  1,416 edge entries, support labels, evidence toggles, unique IDs, six
  graphless discussions and absence of page overflow or JavaScript errors.
  All six PF01954 screenshots were visually inspected: the functional-evidence,
  construct and cross-family discussions at each width. Browser traffic to
  HTTP(S) was blocked; this is a local preview, not publication.
- Documentation and diff checks pass. The original checkout still has only
  its three pre-existing untracked paths. Frozen worklists, source pins,
  permission settings and previous retained reviews/history are unchanged.
  No commit, push, merge, full publication-QC pass or corpus completion is claimed.
  PF01955 is next, with its reviewed members and accessible PNAS primary paper
  located; no PF01955 curation or causal assertions have been written yet.

PF01955 CbiZ chemistry and conditional salvage checkpoint:

- Six native graphs retain eight OBSERVED/EXPERIMENTAL edges: two DIRECT
  purified-enzyme conversions and six UNRESOLVED phenotype effects. Joint
  cbiZ/cobY complementation is one intervention, not independent sufficiency.
  Native deletion/restoration, Cby bypass, extract-reporter growth and AP rescue
  remain separate contexts. Five evidence ledgers and three OPEN discussions
  retain scoped evidence and unresolved mechanisms, protocols and coverage.
- Q8Q0G3 v1 (200 residues) maps PF01955 to 15-198 in M. mazei Go1; Q9HPK9 v1
  (231 residues) maps 14-208 in H. salinarum NRC-1. Woodson2004 Methods,
  Results and original Figures2-6 were inspected. Cyanide-processed HPLC and
  ligand-free MALDI support a Cby-assigned product, not intact AdoCby detection.
  The exact historical clones, rate/mass-balance discrepancy, JE6894/JE6984,
  AP recipes and unavailable supporting Methods/Table1/Figure8 remain open.
- Initial review:
  `reviews/structured/20261012T112351Z-pf01955-cbiz-chemistry-and-conditional-salvage/review.yaml`.
  A subsequent wording edit specifies hydrolysis of the amide bond linking
  aminopropanol to the corrin side chain, rather than removal of the amide.
  The immutable successor is
  `reviews/structured/20261012T113218Z-pf01955-cbiz-amide-bond-precision/review.yaml`
  and sibling Markdown. Its actual review interval is 11:32:15-11:32:18Z on
  October12, with semantic digest
  `da5dceaced5d317d4b84c26a528da04d3c5f07d3dca7bb8a3c5f417f0186853f`.
  Both are partial same-agent scientific assessments, not independent review.
  NEEDS_FOLLOWUP/pass_with_limitations and IN_PROGRESS remain; stable finding
  `pf01955-causal-context-coverage` stays OPEN.
- Native history retains CREATE `2026-10-12T111531Z-codex-255f1c.yaml`,
  initial REVIEW `2026-10-12T112414Z-codex-89cddd.yaml`, wording EDIT
  `2026-10-12T113108Z-codex-1d81b0.yaml` and successor REVIEW
  `2026-10-12T113303Z-codex-ad812f.yaml`, all under `history/records/PF01955/`.
  Earlier reviews, ledgers and family histories are preserved.
- Final native reconstruction checks all 8,296 projections with no generated
  drift. Inventory digests, all 124 latest scoped review digests, source hashes
  and imported identities match; all 124 rendered JSON records equal the YAML.
  Counts are 124 IN_PROGRESS, 8,172 SEEDED, 118 graph-bearing and 8,178 graphless,
  with 694 graphs and 1,424 edges: 1,407 OBSERVED, 15 HYPOTHESIZED, one INFERRED
  and one CONTESTED. These counts do not measure exhaustive scientific coverage.
- Schema generation, 144 native reviews, 276 history files and 136 shared
  review bundles validate. All 294 focused tests pass in 157.14 seconds after
  final projection writes ended, with one upstream LinkML deprecation warning.
  Exports are current; row counts are unchanged and hashes are in
  `docs/exports.md`. Identity exports do not contain causal edges.
- The next CbiS2006 primary paper's full main Methods/Results/Discussion,
  Table1 and original Figures3-6 have now been inspected as provisional
  research, not new canonical graph evidence. Deposited MK1672 CDS translation
  matches Q8TUT1 v1; PF01955 maps 8-205 and PF04608 maps 257-353. Printed
  primers, fragment endpoints, assay units and strain alleles have unresolved
  discrepancies. The C-terminal primer predicts a boundary substitution, not
  a verified historical clone mutation. These findings remain in the temporary
  research handoff pending separately scoped curation and successor review.
  Rhodobacter remodeling, additional members and all earlier follow-ups remain
  open. PF01956 is the next ascending uncurated accession, not a coverage cutoff.
- The final complete Chromium sweep passes all 124 pages and 1,424 edge entries
  at 1440px and 390px, including labels, unique IDs, evidence toggles and six
  graphless discussions, without page overflow or JavaScript errors. Comparing
  preview hashes showed that other HTML pages also changed on regeneration,
  so the whole sweep was repeated rather than relying on a PF01955-only rerun.
  Only PF01955 JSON changed; all 124 JSON records match their current projection.
  The corrected chemistry-evidence screenshots were visually inspected at both
  widths; the six graph-heading screenshots per width were also inspected before
  the wording correction. HTTP(S) traffic was blocked during browser checks.
- Documentation and diff checks pass. The original checkout still has only
  its three pre-existing untracked paths. Frozen worklists, source pins,
  permission settings and previous retained reviews/history are unchanged.
  No commit, push, merge, full publication-QC pass or corpus completion is claimed.

PF01955 CbiS fusion follow-up checkpoint:

- Four new graphs add seventeen OBSERVED/EXPERIMENTAL edges: five purified
  corrinoid conversions, eight separate assay-condition effects and four
  joint/conditional heterologous growth comparisons. All six prior graphs and
  eight edges match the preceding immutable review snapshot exactly. Totals:
  ten graphs, twenty-five edges, seven DIRECT and eighteen UNRESOLVED; two
  MECHANISTIC and eight PHENOTYPIC graphs. No independent CobY/CbiS sufficiency,
  missing N-terminal-minus-AP comparison or universal substrate preference is added.
- Q8TUT1 v1/AAM02885.1 maps PF01955 to 8-205 and PF04608 to 257-353 of the
  357-residue MK1672 fusion. The deposited CDS translates exactly with table11
  alternative initiation. Published primer comparisons retain the predicted
  addedMet/Y208S boundary and noncanonical SalI sequence as unresolved source
  discrepancies, not experimentally verified mutations. Clone junctions, assay
  mass/rate units, genotype labels and per-arm AP recipes remain open.
- Main Woodson2006 Methods/Results/Discussion, Table1 and original Figures3-6
  were inspected. C-terminal phosphatase-related rescue and whole-fusion alphaRP
  chemistry are retained as domain-attribution counterevidence, not PF01955
  phosphatase edges. O2, pH, temperature, magnesium and buffer effects do not
  establish folding, catalytic residues, binding or fusion-mediated thermostability.
  Four new ledgers supplement the unchanged five earlier ledgers; four discussions
  remain OPEN. The earlier coverage ledger is preserved as a dated checkpoint.
- Successor review:
  `reviews/structured/20261012T115538Z-pf01955-cbis-domain-scoped-conversion-and-rescue/review.yaml`
  and sibling Markdown, actual session 11:55:34-11:55:38Z on October12.
  Semantic digest:
  `629819f9f88c61f0070245b7a0184af5d8f956d5554ce5bcfb0f17e0122689d4`.
  Same-agent partial scientific review, NEEDS_FOLLOWUP/pass_with_limitations;
  IN_PROGRESS and stable finding `pf01955-causal-context-coverage` remain open.
  Canonical EDIT `2026-10-12T114721Z-codex-c87e27.yaml` and REVIEW
  `2026-10-12T115630Z-codex-5160e5.yaml` are under `history/records/PF01955/`.
- Final native reconstruction validates all 8,296 projections with zero drift.
  All inventory digests, 124 latest review digests and source hashes match;
  imported identities are preserved and all 124 rendered JSON records equal YAML.
  An initial inventory comparison overlapped inventory generation and failed;
  the successful comparison ran after that writer was terminal. Counts remain
  124 IN_PROGRESS, 8,172 SEEDED, 118 graph-bearing and 8,178 graphless, now with
  698 graphs and 1,441 edges: 1,424 OBSERVED, 15 HYPOTHESIZED, one INFERRED and
  one CONTESTED. These are structural totals, not exhaustive coverage claims.
- Schema, 145 native reviews, 278 canonical history files and 137 shared review
  bundles validate. All 294 focused tests pass in 186.47 seconds, with the known
  upstream LinkML deprecation warning, after projection writers were terminal.
  Exports remain byte-identical to the preceding checkpoint and pass `--check`.
- Full Chromium checks pass all 124 pages at 1440px and 390px: all 1,441 edges,
  support labels, unique IDs, evidence toggles and six graphless discussions,
  without page-wide overflow or JavaScript errors. Sixteen new CbiS screenshots
  were visually inspected: each of four graph scopes and its selected expanded
  evidence at both widths. Browser HTTP(S) traffic was blocked; these are local
  previews, not a published site or a full publication-QC pass.
- Rhodobacter2009 main text, Tables1-3 and captions now have a provisional
  research handoff. Q3J3R7/RSP_2406 is the mapped 2.4.1 candidate, PF01955 6-208;
  exact historical construct mapping, original figures and supplementS1/S2 still
  need assessment. Tagged purified protein, acetate growth and succinate cellular
  corrinoid profiles must remain distinct. No Rhodobacter edge is added yet.
  The next ascending uncurated accession remains PF01956; all earlier open
  follow-ups and all unassessed families remain in the corpus-wide goal.
- Documentation and diff checks pass; the original checkout's three pre-existing
  untracked paths remain unchanged. No prior retained review/history, source pin,
  frozen worklist or permission setting is edited. No commit, push, PR, merge,
  publication or corpus completion is claimed.

PF01955 Rhodobacter conversion and cellular-context checkpoint:

- Added four graphs and thirteen OBSERVED/EXPERIMENTAL edges from Gray2009
  (PMID19889098), after reading main text/Tables1-3 and visually inspecting
  original Figures1-4. Four substrate conversions are DIRECT; five assay
  condition effects, two acetate-growth contrasts and two succinate-culture
  fraction effects have UNRESOLVED intervening mechanisms. All ten previous
  graphs and all nine previous evidence ledgers are byte/content-preserved.
- Q3J3R7v1/ABA78567.1/RSP_2406 maps PF01955 6-208 of219aa. Native CDS
  translation and the100bp downstream flank resolve the reverse-primer matches,
  including the rescue insert's40bp extension. Complete historical MBP/His6
  junctions and native deletion alleles remain open. Retained tags, cyanide
  derivatization, pH-buffer confounding and assay-specific Cbl negatives are
  explicit. No complete CbiZ-alone remodeling or transport mechanism is claimed.
- The author-manuscript Figure2 caption mentions an absent fourth column;
  the original image and publisher caption haveA-C. No experiment is invented
  from that mismatch. SupplementS1/S2 retrieval returned challengeHTML rather
  than aPDF; no bypass was attempted. Five discussions remain OPEN.
- New minimal ledgers are `evidence/PF01955/gray-2009-identity-constructs.txt`,
  `gray-2009-purified-assays.txt` and `gray-2009-cellular-contexts.txt` in that
  directory. Their hashes are respectively
  `94fe51731b082b001b850082c5f2614b54fdc9b07ec38521c55449a87b390257`,
  `392fc2d3d2379bc21614a0279b7d0a2f99d8d17fc596d29afcf766b5cba661f3`,
  `fd3733e52154fe1e0c8723732b75097b2012509a2b7b08b0fff9787043fe9f63`.
- Saved successor review:
  `reviews/structured/20261012T121906Z-pf01955-rhodobacter-conversion-and-cellular-contexts/review.yaml`
  and derived `review.md`. Same-agent partial scientific assessment,
  NEEDS_FOLLOWUP/pass_with_limitations; current semantic digest
  `f9cadfe5805a8942b44daa6250d02c57c0dfa78eda805c7a7ec738739038e7f8`.
  Native EDIT `2026-10-12T121237Z-codex-3c2221.yaml` and REVIEW
  `2026-10-12T121928Z-codex-24faff.yaml` are under `history/records/PF01955/`;
  both are projected. Status remains IN_PROGRESS.
- Native whole-corpus reconstruction and inventory pass for8,296 records.
  Current totals are702graphs/1,454edges:1,437OBSERVED,15HYPOTHESIZED,
  oneINFERRED andoneCONTESTED;124IN_PROGRESS/8,172SEEDED and
  118graph-bearing/8,178graphless families are unchanged. Schema and exports
  checks pass; all three interchange hashes remain unchanged.
- The final Git-based preservation check stopped when reads of the original
  checkout under Documents began returning `Operation not permitted`. The
  original GitHEAD, worktreeHEAD and README contents fail even approved narrow
  read-only escalation, while file metadata and the temporary worktree remain
  accessible. Git's resulting `not a git repository` message is not evidence
  that the Git directory disappeared. No permission or Git configuration was
  changed. Root cause is not established; access must be restored before the
  Git-dependent checks and original-checkout status can be reverified.
- Tests:292passed,2Git-provenance failures,onewarning in138.70s. The retained
  review/history checks passed before that denial; no full current QC pass is
  claimed. Independent non-Git comparisons verify8,296inventorydigests and all
  124latest review/evidence hashes,overlay matches and renderedJSON records.
- Browser verification: full desktop/mobile sweep passed all124pages and
  1,454edges at1440px/390px with uniqueanchors, evidence toggles and no page-wide
  overflow or JavaScript errors. Sixteen new screenshots (four graph headings
  and four selected evidence panels at each width) were visually inspected.
  The first attempt
  tested a hidden mechanism before opening its disclosure; that assertion was
  moved after expansion and the entire sweep restarted. This was a test-order
  error, not a change to scientific content or a disabled check.
- README documentation check and no-index whitespace checks of the modified
  overlay/documentation pass. Final repository-wide `git diff --check` and
  original-checkout status remain blocked by the read denial; the earlier
  pre-denial check is not represented as a final check.
- Both earlier salvage studies (PMC2602876/PMC2698395) are now accessible as
  publicHTML. The native2009 deletion Methods identifyRSP_2406 but contain
  endpoint/frame/length arithmetic requiring primer reconciliation. The2008
  extract assay reports low CNCbl activity under a different protocol from
  the2009 tagged-enzyme negative. Neither result is made universal. Temporary
  next-research notes are
  `/private/tmp/dufmech-PF01955-native-salvage-next-research-20261012.yaml`;
  they are not canonical evidence or a completed review. Original figures,
  exact constructs, further members and all earlier follow-ups remain open.
- No source pin, frozen worklist, earlier retained review/history or permission
  setting was intentionally edited. No commit, push, PR, merge, publication or
  full family/corpus completion is claimed. All8,296records remain in scope.

PF01955 native conditional-salvage checkpoint (2026-10-12T12:50:00Z):

- Added `rs-cbiz-native-conditional-salvage-2009` and
  `rs-cbiz-native-cby-bypass-2009` from PMID19376876. Four OBSERVED edges retain
  partner requirements and conditional bypass; one INFERRED edge explicitly
  compares the CbiZ-positive/deficient strains across separate Figures5/4.
  All five have UNRESOLVED molecular directness. Existing fourteen graphs and
  thirty-eight edges are unchanged, checked against the prior retained projection.
- Main text/Table1 and originalFigures2-6 were inspected. Native-study
  supplementTablesS1/S2 were read as PDF text, not visually inspected images.
  TableS1 primers predict a41aa deletion product from CDS1-69 plusTCTAGA
  plus610-660. Printed70-610/48nt conflicts remain distinct from predicted
  deletion70-609/51nt retention; no actual historical clone sequence is invented.
  JE11844/JE11906 resolves as parent/plasmid derivative; JE10708/JE10780,
  tetracycline1ug/ml versus1ug/ul and calibration11/22mM glycerol remain conflicts.
  Carbon/oxygen effects and partner-only controls are not PF01955 catalytic steps.
- Added `evidence/PF01955/gray-2009-deletion-primers.txt` (SHA256
  `b0a08588958b66e8eb9046d76d1063333dc32643cd09612b9322857fbfaf5010`)
  and `evidence/PF01955/gray-2009-native-salvage.txt` (SHA256
  `1d04a43a043270f109ca910b7c30a4f8c168d0c180787f020137dda3e90c43e1`).
  Prior twelve evidence ledgers remain unchanged. Raw sources stay temporary.
- Native EDIT event:
  `history/records/PF01955/2026-10-12T123814Z-codex-7561f2.yaml`.
  An initial compact-format timestamp was rejected before writing; the corrected
  native event validates. A preview overlapping that history update detected a
  changing history index; after it completed, the repeated preview validated all
  8,296 records and the guarded apply updated two generated files. Subsequent
  native load validates all 8,296 projections with zero drift; schema artifacts
  also have zero drift. All 281 canonical history files pass validation.
- PF01955 now has16graphs/43edges:42OBSERVED,1INFERRED,11DIRECT,32UNRESOLVED,
  3MECHANISTIC and13PHENOTYPIC. Corpus totals are704graphs/1,459edges:
  1,441OBSERVED,2INFERRED,15HYPOTHESIZED,1CONTESTED. Counts remain124IN_PROGRESS,
  8,172SEEDED,118graph-bearing and8,178graphless; these are not completion counts.
  Current semantic digest is
  `568dd08be542f3607e0402abac6ceec0a6bd64d2b441a6d62b8b2c917cd76481`.
- Successor review input is
  `/private/tmp/dufmech-pf01955-native-salvage-assessments-20261012.yaml`.
  Native retention was attempted and stopped at `git rev-parse HEAD` before
  creating a report. Thus only123/124 latest scoped reviews are current. The
  previous `20261012T121906Z` review is historical, not approval of these additions.
  No REVIEW event or review promotion was fabricated. Reinspect the current
  record and source hashes, use actual new review timestamps, and retain the
  successor after access restoration; then append its real REVIEW event.
- Original checkout cwd and contents still return `Operation not permitted`,
  including an approved exact read-only `.git/HEAD` retry. Metadata/stat remains
  readable and shows normal file modes; root cause is undetermined. Git-dependent
  full preservation verification fails at `git show HEAD:data/families/PF00990.yaml`.
  Permissions and repository metadata were not changed to bypass the failure.
  Final original-checkout status and repository-wide Git diff remain unverified.
- Tests finished292passed,2failed,onewarning in156.67s; failures are the same
  two Git-provenance contract tests documented above. Separate bounded checks
  pass all8,296 inventory digests, all124 overlay/rendered JSON matches,
  unchanged prior evidence and fourteen graphs, and123current review bindings.
  Identity export hashes are unchanged. This is not a full QC pass.
- PF01955 browser checks pass all43edges at1440px/390px: uniqueanchors,
  support labels, evidence toggles and no page-wide overflow or JavaScript errors.
  Eight new screenshots were visually inspected. Wide edge tables deliberately
  scroll within their own region on mobile. The native renderer regenerated all
  124 local preview pages; no website publication or source-pin change is claimed.
- Earlier2008 member-specific salvage/extract experiments, historical clones,
  supplementary images, later members and every earlier family follow-up remain
  in scope. The causal-graph skill validates. No commit, push, PR, merge, branch
  deletion, full-family completion or corpus completion is claimed.

PF01955 2008 donor-context and restored-access checkpoint (2026-10-12T13:17:13Z):

- Added four PHENOTYPIC graphs with 23 OBSERVED, EXPERIMENTAL edges of
  UNRESOLVED molecular directness: seven alternative donor/CobY rescue effects,
  seven conditional AP rescue effects, six within-donor induction contrasts,
  and three product-forming activities in mixed extracts. The previous sixteen
  graphs remain exactly unchanged. PF01955 now has 20 graphs and 66 edges:
  65 OBSERVED, one INFERRED, eleven DIRECT and 55 UNRESOLVED effects.
- Inspected PMID18808385 main text/Methods and original Figures2-4. Current
  donor accession/domain matches are candidates, not verified historical
  inserts; S0ASV7 first appeared in 2013. The B. halodurans construct is a
  whole BtuD-CbiZ fusion, not an isolated PF01955 domain. Supplementary tables
  S1-S4 and figures S1/S2 remain uninspected. No native inactivity is inferred
  from the three negative heterologous donors.
- The AP experiment's host has a cobD lesion, not a direct cbiB deletion.
  Some Cbi-alone curves retain late growth. Induction effects are qualitative
  OD650 comparisons near 12 hours, not fitted growth rates or final biomass;
  the Rhodobacter Cbi curves later converge. Partner requirements and matched
  induction conditions remain explicit, without independent CbiZ sufficiency.
- Mixed-extract activities of 880+/-63, 120+/-16 and 15+/-2 pmol per mg total
  extract per minute remain preparation-specific, not purified enzyme rates.
  Text-reported product assignment, uninspected supplementary traces, unshown
  reporter results and contradictory reporter-method wording stay qualified.
  The low 2008 CNCbl activity does not erase the different 2009 tagged purified
  preparation's negative result. Antibiotic units and historical clones remain
  open source conflicts; no CobP or transporter mechanism was assigned to CbiZ.
- Three new ledgers under `evidence/PF01955/` bind these claims:
  `gray-2008-constructs-and-mapping.txt` SHA256
  `f043bcacd87bd4e043478226b0aa74d6d01bfc55c15df89d239d10526d151c91`;
  `gray-2008-heterologous-assays.txt` SHA256
  `1e057203c8a9bd0e57eccb6b4eacc03153c7c5834f311dece40e232c8c43f01b`;
  `gray-2008-extract-assays.txt` SHA256
  `e3b78e037bd058c0dbce093ce39f9c67ae9275d5a80472826de94277dda80c2b`.
  All prior fourteen ledgers are unchanged; raw source downloads stay temporary.
- Native EDIT event is
  `history/records/PF01955/2026-10-12T125204Z-codex-299174.yaml`.
  Native retention unexpectedly succeeded at 13:05:29Z as Git access returned.
  The first new report, `20261012T130529Z-pf01955-2008-donor-rescue-and-extract-contexts`,
  inherited stale access-blocked prose; it remains immutable. The corrected
  successor `20261012T130729Z-pf01955-2008-contexts-and-restored-provenance`
  supersedes that prose and binds all seventeen ledgers. Both use the unchanged
  current semantic digest
  `8ee5b149867883b62b293434857bcd66fb53a9be96dd66c847d3e60438b7d526`.
  Their native REVIEW events are
  `history/records/PF01955/2026-10-12T130510Z-codex-92da4b.yaml` and
  `history/records/PF01955/2026-10-12T130719Z-codex-69e11f.yaml`.
  The older native-salvage draft is now covered by the successor, not a separately
  retained report. Scientific scope remains partial, self-reviewed and
  NEEDS_FOLLOWUP, with the stable coverage finding and six discussions OPEN.
- After projection of both REVIEW events, all 8,296 records validate with zero
  generated drift; schema artifacts also have zero drift. Native validation
  passes 148 reports and 284 history files; shared validation passes 140 bundles.
  All 294 targeted tests pass in 158.00 seconds, including both previously
  access-blocked tests, with one upstream LinkML warning. Full Git preservation
  and supplemental before/after checks pass; identity export hashes are
  unchanged. This is not a new full-repository QC or source-pin check.
- Corpus totals are 708 graphs and 1,482 edges: 1,464 OBSERVED, two INFERRED,
  fifteen HYPOTHESIZED and one CONTESTED. There are still 124 IN_PROGRESS,
  8,172 SEEDED, 118 graph-bearing and 8,178 graphless records. All 124 current
  scoped review digests and retained source hashes match, without status promotion.
- The native renderer regenerated all 124 local previews. Targeted PF01955
  browser checks pass at 1440px and 390px: all 66 edges, unique anchors, evidence
  toggles, no page-wide overflow and no JavaScript errors. Four desktop heading
  and four mobile evidence screenshots were visually inspected. Wide tables
  remain internally scrollable. No full 124-page browser sweep at this count
  or published website update is claimed.
- Original-checkout reads and Git status now succeed; its same three untracked
  user paths remain untouched. No filesystem permission, configuration or Git
  metadata change was made to restore access, and the denial's cause remains
  unknown. The installed causal-graph skill validates. Git whitespace checks
  pass. No commit, push, PR, merge, branch deletion or source-pin change occurred.
  All 8,296 records and every earlier follow-up remain in scope.

PF01956 first EMC context checkpoint (2026-10-12):

- Added seven graphs with 29 OBSERVED, EXPERIMENTAL edges. The one MECHANISTIC
  graph retains two DIRECT effects of purified assembled human EMC on protected
  SQS reporter insertion. Six PHENOTYPIC graphs retain 27 UNRESOLVED effects of
  complex proteolysis, human EMC3 substitutions, and yeast deletion/K26L
  perturbations. These are not evidence that EMC3 alone is sufficient or a
  complete family mechanism. Two discussions remain OPEN; status is IN_PROGRESS.
- Inspected Guna2018 main text and original Figure4, selected supplementary
  Methods and S18/S19; Pleiner2020 main text, original Figure3, selected Methods
  and S9/S13; Bai2020 main Methods and original Figures1/3. Other supplements,
  raw gels/tables and historical clone sequences were not exhaustively examined.
  RRL and isolated CaM-SQS assays retain separate preparation/timing scope,
  active EMC orientation and empty-vesicle controls. The trypsin recipe and
  lane-specific vesicle preparation remain open; proteolysis is not EMC3-specific.
- Q9P0I2 v3 maps PF01956 5-191 and P36039 v3 maps 2-197. Reference mappings do
  not verify the historical plasmids. Human variants are tagged, exogenously
  expressed constructs, not endogenous knock-ins or EMC3-knockout rescue.
  R31K improves SQS relative to R31E but does not restore OPRK1; R180K comparisons
  are client-specific. The four-methionine mutant is one joint perturbation.
  The second methionine loop lies outside this Pfam interval. Assembly controls
  do not eliminate every folding/abundance explanation, and crosslink proximity
  is not insertion causality. The supplement's UGA/amber conflict stays explicit.
- Yeast BY4741 cellular experiments remain distinct from W303-1a structural
  purification. Conditional 37 C colony growth and membrane-associated client
  fluorescence are separate endpoints, not a demonstrated mediation chain.
  Hxt3 RNA decreases by about half, preventing an exclusively post-translational
  interpretation. K26L is not treated as equivalent to deletion.
- Four new ledgers under `evidence/PF01956/` bind these claims:
  `identity-and-boundaries.txt` SHA256
  `4dde1cd75bda311153795366df70dd0708f73c4952cb701e652ad25dde18e0ac`;
  `guna-2018-reconstitution.txt` SHA256
  `bedd3a05f58fb02d6841638c08b25ceaa3586d3ae8a3994afdb30f544b424079`;
  `pleiner-2020-emc3-variants.txt` SHA256
  `0b8c0126f629dce4ce37e6f957f7e775d56a3fb483bc293c1286aefdfabb417f`;
  `bai-2020-yeast-emc3.txt` SHA256
  `b298b570d28fb443ac0c8b2cf781dbbef7c54ab4a521f9e2c66a7be64fbb9526`.
  Raw downloads remain temporary; native quote/hash checks pass.
- Native CREATE and REVIEW events are
  `history/records/PF01956/2026-10-12T131905Z-codex-a00b7a.yaml` and
  `history/records/PF01956/2026-10-12T133132Z-codex-958a78.yaml`.
  The retained report is
  `reviews/structured/20261012T133200Z-pf01956-emc-reconstitution-and-emc3-variant-contexts/`.
  It is a partial, same-agent scientific review with NEEDS_FOLLOWUP, not independent
  expert approval. The current semantic digest is
  `8f0001e203869e12c577d44395beb6c60a0dd9b7b1500f16dd7781d8ed0a481d`.
  The stable `pf01956-causal-context-coverage` finding remains OPEN.
- All 8,296 projections validate with zero generated drift, including the two
  projected history events; schema artifacts have zero drift. Native validation
  passes 149 reports and 286 history files; shared validation passes 141 bundles.
  Full preservation checks pass all 8,296 inventory digests, all 125 imported
  identities against HEAD, all 125 exact rendered JSON records, and all 125
  current scientific review digests/source hashes. Frozen worklists and conf are
  unchanged. Export reproducibility is checked separately from graph inventory
  and imported-identity preservation.
- A repeated focused regression run finished 293 passed and one failed in
  167.11 seconds: the stored exports still carried SEEDED for PF01956 instead of
  IN_PROGRESS. The earlier run's terminal output could not be recovered; no pass
  was inferred from progress dots or a missing process handle. Native export
  regeneration and the post-fix regression result are recorded below.
- Native export regeneration changed only PF01956's curation status in the KGX
  node and SSSOM comment. Structured before/after comparison verified identical
  membership and all other values; association edges are byte-identical. New
  SHA256 values are `2f5d28003eba5d3092b1d2899b035afcd9fdd66962a629e0e77310412c8a6e93`
  for nodes and `0d09cc71ce2a56eaea9ab386edf933b977e1b9bbc253287db28d05f2dfda8fa6`
  for SSSOM. Edges remain
  `7c5ac1162eb92d57843e10f05f0ee95dcbd83d93a4ce1478628536f914e74679`.
  The per-family workflow now includes the native export refresh/check.
- Post-fix native `dufmech.exports --check` passes. All 294 focused tests pass
  in 151.81 seconds, with one upstream LinkML deprecation warning. These cover
  graphs, records, reviews, structured review contracts, canonical history,
  projection binding and offline exports. Documentation and Git whitespace
  checks pass. This is a targeted verification result, not full publication QC.
- Corpus totals are 715 graphs and 1,511 edges: 1,493 OBSERVED, two INFERRED,
  fifteen HYPOTHESIZED and one CONTESTED. There are 125 IN_PROGRESS, 8,171 SEEDED,
  119 graph-bearing and 8,177 graphless records. These are not completion counts.
- The native renderer regenerated all 125 previews. PF01956 browser checks pass
  all 29 edges at 1440px and 390px: unique anchors, evidence toggles, no page-wide
  overflow and no JavaScript errors. Four desktop heading and four expanded
  mobile evidence screenshots were visually inspected. The temporary capture
  script initially took closed-panel screenshots; corrected captures explicitly
  open the evidence panel. Wide tables scroll internally. No all-125-page browser
  sweep at this count or published website update is claimed.
- Sandboxed Chromium startup failed at macOS Mach-port creation; an approved
  local-only retry passed. This is distinct from the earlier checkout-read
  denial. Original-checkout file reads, `.git/HEAD`, Git history and Git status
  now succeed without escalation. Its same three untracked user paths remain
  untouched. The installed causal-graph skill validates. No permission,
  configuration or Git metadata change was made to restore access; the cause is
  still unknown. No full repository QC, source-pin change, commit, push, PR,
  merge or branch deletion is claimed. All 8,296 records remain in scope.

PF01956 TMCO1/GEL follow-up checkpoint (2026-10-12):

- Added seven PHENOTYPIC graphs with fourteen OBSERVED, EXPERIMENTAL edges of
  UNRESOLVED molecular directness. Prior seven graphs and four ledgers are
  unchanged. PF01956 now has fourteen graphs, 43 edges, two DIRECT and 41
  UNRESOLVED effects, seven ledgers and three OPEN discussions. It stays
  IN_PROGRESS; this is not whole-family completion.
- Newly inspected McGilvray2020 original Figure5/supplement1 and relevant
  Results/Methods; Sundaram2022 original Figures1/4, Extended Data1/5 and
  relevant Methods. Endogenous EAAT1 abundance, partner abundance, microsome
  glycosylation/protection, cellular glycosylation and fluorescence ratios are
  separate endpoints. Double-knockout graphs compare joint genotypes with WT,
  not individual-factor effects, sufficiency or epistasis. Three new ledgers are
  `evidence/PF01956/tmco1-isoforms-and-constructs.txt` SHA256
  `03efa1ce598bbd2e6a7faa2f4778ca2826eee8b423d687db8e2bbabb035e9d69`,
  `evidence/PF01956/mcgilvray-2020-eaat1.txt` SHA256
  `b75b107a52362174f4a2cc5e605621aa8242ea7bf7828b3fa48d5019a49a8393`,
  and `evidence/PF01956/sundaram-2022-gel-and-topogenesis.txt` SHA256
  `5822bb16ab7877acb2b2b265a42cd8647fc98d6e07b01be65e273c1ef875f73b`.
- Current Q9UM00 v2 is 239 residues, with PF01956 59-216. Displayed Q9UM00-3
  differs from shorter Q9UM00-1 by canonical residues1-51. The short-isoform
  interval8-165 and D140-to-D191 relation are arithmetic mappings, not a new
  profile scan or verified historical construct. No channel residue edge was
  added from database annotations or the inaccessible 2016 full paper.
- The 2020 upper EAAT1 bands are SDS-induced aggregates, not native trimers.
  RNA is modestly reduced in TMCO1-knockout cells, not exactly unchanged.
  In 2022, comparable carbonate-resistant recovery and preserved single-pass
  controls qualify glycosylation/protection defects. Loss of TMCO1 also changes
  OPTI and translocon recruitment. Different YIPF1 tag positions, reporter
  numerator/denominator colors, single versus double knockout panels and
  cellular versus cell-free timings are explicit. Gating wording and culture
  stock/final units remain unresolved; raw gels/statistical tables are uninspected.
- CSU and publisher 2016 PDFs returned403; the Anghel2017 supplement returned
  HTML; the attempted Ylp1 XML endpoint returned500. These are source-access
  limits, not filesystem failures or negative scientific findings. No challenge
  bypass was attempted. The 2020 authors' client-biogenesis explanation of
  calcium phenotypes is not proof against the 2016 channel model.
- Native EDIT and REVIEW events are
  `history/records/PF01956/2026-10-12T134751Z-codex-f6f5b4.yaml` and
  `history/records/PF01956/2026-10-12T135807Z-codex-1fb67d.yaml`.
  The latter's word "archaeological" is a prose typo for "archaeal"; the
  scientific report and discussions retain the correct target. The event is
  not silently rewritten. The successor report is
  `reviews/structured/20261012T140035Z-pf01956-tmco1-gel-and-separated-client-biogenesis-effects/`.
  Its semantic digest is
  `2ffa41da6a1c1b8c02eb1daeed6bd8bc05413b314dd23f2273b8feed723a690a`.
  It is partial same-agent scientific review, NEEDS_FOLLOWUP, with the stable
  `pf01956-causal-context-coverage` finding OPEN. Earlier reports stay immutable.
- Final guarded regeneration validates all 8,296 projections with zero remaining
  drift; schema-only validation also reports zero drift. PF01956 projects all
  four canonical history events. Native checks validate 150 retained reports
  and 288 history files; the shared check validates 142 structured reviews with
  declared scopes only. These checks do not certify whole-family scientific
  completeness or independent review.
- Inventory preservation verifies all 8,296 exact semantic digests, the imported
  identity fields of all 125 curated families, their exact rendered JSON records,
  and all 125 latest scientific-review digests and retained source hashes. Frozen
  worklists and configuration are unchanged. The current corpus has 125
  IN_PROGRESS and 8,171 SEEDED records, 119 graph-bearing and 8,177 graphless
  records, and 722 graphs with 1,525 edges: 1,507 OBSERVED, two INFERRED, one
  CONTESTED and fifteen HYPOTHESIZED. None of the 125 partial reviews is a
  claim that the all-record goal is complete.
- Native export reproduction reports `exports current`. KGX nodes, KGX edges
  and SSSOM retain the preceding checkpoint's respective SHA256 values
  `2f5d28003eba5d3092b1d2899b035afcd9fdd66962a629e0e77310412c8a6e93`,
  `7c5ac1162eb92d57843e10f05f0ee95dcbd83d93a4ce1478628536f914e74679`,
  and `0d09cc71ce2a56eaea9ab386edf933b977e1b9bbc253287db28d05f2dfda8fa6`.
  This is preservation since that checkpoint, not a claim that nodes and SSSOM
  are unchanged from HEAD.
- The targeted causal-graph, record, review, structured-review, record-review
  contract, history, review-projection binding and export regression suite passes:
  294 tests in 183.74 seconds, with one upstream LinkML dataclass-extension
  deprecation warning. All 125 local previews regenerated. PF01956 browser checks
  pass for all 43 edges, unique IDs and evidence toggles at 1440px and 390px,
  without page overflow or JavaScript errors. Eight representative desktop and
  expanded mobile evidence screenshots were visually inspected; mobile tables
  retain their internal horizontal scrolling. This is not a new all-125 browser
  sweep or full repository QC.
- Retry reads of the original checkout, `.git/HEAD`, committed README and
  installed skill succeed without escalation; the skill validator passes. Its
  three untracked user paths remain untouched. No filesystem permission,
  configuration or Git metadata change was made, and the original denial's cause
  remains unconfirmed. No source-pin change, commit, push, PR, merge or branch
  deletion occurred. All 8,296 records and prior follow-ups remain in scope.

PF01957 NfeD checkpoint (2026-10-12):

- Added three PHENOTYPIC graphs with four OBSERVED, EXPERIMENTAL edges of
  UNRESOLVED molecular directness. YbbJ coexpression affects separate plate and
  liquid growth readouts in AD1762 with ftsH/htpX defects and sfhC21. Bacillus
  yqeZyqfAB deletion and induced expression in a sigW mutant remain distinct
  contexts. Matched xylose, SPbeta immunity, producer sunA controls, failed
  partial-operon complementation and the YqfB V65E reference difference are
  retained. No isolated-domain protease, chaperone or resistance mechanism is
  claimed; the record stays IN_PROGRESS with two OPEN discussions.
- Current P0AAS3 v2 maps PF01957 94-148; its 2007 sequence update does not
  verify the 2006 MC4100 clone. P54465 v1 maps 382-435, but CU1065 historical
  YqeZ alleles remain unverified. O32077 NfeD2/YuaF maps PF25842 1-101 and
  PF31148 114-168, so its positive FloT effects were excluded from PF01957.
  PH1510 O59179 maps PF01957 377-432 separately from the N-terminal protease
  region. The five ledgers are:
  `evidence/PF01957/identity-and-domain-boundaries.txt` SHA256
  `cb9ebcb9ade539df49a77b538ec4019b96ae0f009d4cc0b82e8a42ef52764a4f`,
  `chiba-2006-ybbj-growth.txt`
  `eaac6e10c7bd3c34762336b024d0e46d1b01cca4a71695179c290c87fc5f238a`,
  `butcher-2006-operon-resistance.txt`
  `dbe96f4f6d5842c32a398ede4f6a737339309d4df79feb2f98df027724f46a97`,
  `dempwolff-2012-localization-boundaries.txt`
  `842a2f3f030e02fd99c069c925753a49a970b9cbdd3e227ddb8dea520a646e69`,
  and `structural-and-archaeal-followups.txt`
  `946d68bfd8f81b6ef9c8c27c6e98ee8bf576c06115cfea4493e483b1ab263b57`.
- Chiba2006 Figure2 and Butcher2006 Figure4 text/legends and relevant Methods
  were inspected through publisher web retrieval; their original figure images
  and supplements were not inspected after direct HTML/PDF403 responses and
  failed figure-PowerPoint retrieval. Dempwolff2012 original Figures4/6 were
  inspected and expose conflicting panel references, including a Figure6 A-I
  image with an A-G caption. The mapped YqeZ localization comparisons are
  qualitative negatives, not causal recruitment edges. Tan2024 is limited to
  abstract and 8Z5G/EMD-39773 metadata; PH0471/PH1510 full experiments and
  further members remain open. Access failures are not negative findings.
- Native CREATE and REVIEW events are
  `history/records/PF01957/2026-10-12T141337Z-codex-cfe501.yaml` and
  `history/records/PF01957/2026-10-12T141740Z-codex-cfa1ed.yaml`.
  The retained report is
  `reviews/structured/20261012T141835Z-pf01957-ybbj-growth-and-yqez-operon-contexts/`,
  binding semantic digest
  `9ff215eee0e884ed3286e127c8ecaae2ede84c9814bf26eb36296d2f6deb8fce`.
  It is a partial same-agent scientific review, native NEEDS_FOLLOWUP/common
  pass_with_limitations, with `pf01957-causal-context-coverage` OPEN. Both
  canonical events project correctly, and graph/discussion content matches
  the overlay. No earlier report or scientific record was rewritten.
- Full native regeneration and validated inventory cover 8,296 current records
  with no remaining projection drift; schema-only drift is zero. Native checks
  validate 290 history files and 151 reports; shared checks validate 143 bundles
  for declared scopes only. Preservation checks match all 8,296 inventory
  digests, all 126 curated imported identities and rendered JSON records, and
  all 126 latest scientific-review digests and evidence hashes. Frozen worklists
  and configuration are unchanged. Current totals are 126 IN_PROGRESS, 8,170
  SEEDED, 120 graph-bearing, 8,176 graphless, 725 graphs and 1,529 edges:
  1,511 OBSERVED, two INFERRED, one CONTESTED and fifteen HYPOTHESIZED.
- Exports regenerate and reproduce. Relative to HEAD, structured comparison
  confirms only curated-status changes in 126 KGX nodes and 125 SSSOM
  associations. An initial verifier incorrectly expected 126 SSSOM rows;
  current PF02410 has no InterPro mapping and is correctly absent. The corrected
  membership-based comparison passes; no export data fix was needed. KGX
  association edges remain identical to HEAD. Current SHA256 values are nodes
  `e4f1054df0ecd2899b7a5cad249ac8a9594d0198d542ac1e01f526821f532600`, edges
  `7c5ac1162eb92d57843e10f05f0ee95dcbd83d93a4ce1478628536f914e74679`, and SSSOM
  `904282f9b5c63befa0d4d85a237ad2abeacaa1bd85245ae33e4f57e2c289ea8a`.
- All 126 local previews regenerate; PF01957 passes browser checks for all
  four edges, evidence toggles, unique IDs and page overflow at 1440px and
  390px with no JavaScript errors. Six representative screenshots covering
  all three graphs and expanded mobile evidence were visually inspected;
  wide/long evidence tables remain internally scrollable. Sandboxed Chromium
  failed at macOS Mach-port startup; the approved local-only retry passed.
  This is not a filesystem-read denial or a new all-126 browser sweep.
- The targeted causal-graph, record, review, structured-review, record-review
  contract, history, review-projection binding and export suite passes all
  294 tests in 157.77 seconds, with one upstream LinkML dataclass-extension
  deprecation warning. README corpus statistics are current; tracked diffs
  and the seven new/updated authoring files have no whitespace diagnostics.
  These checks are not full repository/publication QC or scientific completion.
- Original-checkout status remains unchanged with the same three user paths
  untouched. No permissions, Git metadata, source pins or publication state
  changed. All 8,296 records and every earlier open follow-up remain in scope;
  PF01958 is the next ascending uncurated accession, not a completion boundary.

PF01958 Asp_DH_C checkpoint (2026-10-12):

- Added five graphs and eight edges for intact TM1643: six observed biochemical
  redox/inhibition effects, one inferred immediate iminoaspartate product and
  one hypothetical cellular NAD-biosynthetic contribution. The last two are
  explicitly separate HYPOTHETICAL graphs, not directly observed chemistry/flux.
  Forward and reverse assays preserve pH9.8 versus pH8.0, donor alternatives,
  ammonium sulfate and other joint conditions. Neither His193 catalysis nor
  a TM1643-NadA channeling complex is asserted as an observed mechanism.
- Current Q9X1X6 v1 maps PF01958 121-234 and PF03447 41-106. Structural
  domain boundaries and the historical tagged construct are distinguished.
  Human A6ND91 v2 maps PF01958 133-266, but the newly encountered primary
  bioRxiv preprint reports divergent chemistry and needs full-method/product
  assessment before curation. Its version1/2026-06-09 preprint status is retained.
- Four hash-bound ledgers under `evidence/PF01958/` preserve identity, the
  Yang2003 primary assay assessment, Li2017 construct/label questions, and the
  human preprint/access follow-up. Original2003 plots were not visually
  accessible. Li2017 pages2/4/5 were visually inspected, confirming pH-label
  conflicts and other context limits; Figure4 sequence mapping remains open.
- Canonical history is
  `history/records/PF01958/2026-10-12T143032Z-codex-f1e6ef.yaml` (CREATE) and
  `history/records/PF01958/2026-10-12T143442Z-codex-bc19bc.yaml` (REVIEW).
  The native-saved `20261012T143541Z-pf01958-tm1643-redox-and-separated-interpretations`
  report binds semantic digest
  `4304878e5b386368131f2e5c039492ad606ff9f56c699b3e329ad2de419de24a`.
  It is partial same-agent NEEDS_FOLLOWUP/pass_with_limitations; both discussions
  and the `pf01958-causal-context-coverage` finding remain open.
- Inventory verification covers all8,296 digests and all127 curated identities,
  projections, rendered JSON records and latest review/source hashes. Totals:
  127 IN_PROGRESS,8,169 SEEDED,121 graph-bearing,8,175 graphless,730 graphs,
  1,537 edges (1,517 OBSERVED,3 INFERRED,1 CONTESTED,16 HYPOTHESIZED).
  Native/shared checks validate292 history files,152 reports and144 structured
  bundles. Schema generation and README statistics are current.
- Export regeneration/check passes. Structured TSV comparison againstHEAD
  confirms only status changes in127 KGX nodes and126 SSSOM associations;
  PF02410 still lacks an InterPro mapping and is correctly absent fromSSSOM.
  Association-edge bytes are unchanged. SHA256: nodes
  `68d256a02af129b68b9bcebc6cbbb2e317317d8387c37750230e8f36f8aaf9ee`,
  edges `7c5ac1162eb92d57843e10f05f0ee95dcbd83d93a4ce1478628536f914e74679`,
  SSSOM `6cc8526e24c6d143abcbe03eba92cb8c58761c05642aed9ebc35633d462d8dfd`.
- All127 local previews regenerate. PF01958 browser checks pass at1440/390px
  for eight edges, five graphs, evidence toggles, unique IDs, no page overflow
  and no JavaScript errors. Six representative desktop/mobile screenshots were
  visually inspected. The normal sandbox launch failed with macOS Mach-port
  error1100; the approved local-only retry passed with HTTP(S) requests blocked.
  Filesystem reads worked without escalation. No full127-page browser sweep,
  publication, source-pin update or full repository QC is claimed.
- The original checkout's three user paths remain untouched. All8,296 families
  and every earlier open follow-up remain in scope; PF01959 is the next
  ascending uncurated accession, not a completion boundary.
- The focused causal-graph, record, review, structured-review, review-contract,
  history, projection-binding and export suite passes294 tests in163.10s,
  with one upstream LinkML dataclass-extension deprecation warning. These
  checks do not establish complete scientific coverage or publication readiness.
  Final guarded records check validates8,296 records with zero generated drift;
  tracked diffs and six new/updated authoring files have no whitespace diagnostics.

PF01959 DHQS joint-assay checkpoint (2026-10-12):

- Two MECHANISTIC graphs retain three qualitative OBSERVED, EXPERIMENTAL,
  DIRECT product-readout effects for intact MJ0400 plus MJ1249. The phosphate
  assay sums DHQ and DHB; separate NAD/NADP assays measure chemically reduced
  DHQ through quinic acid. Neither isolated PF01959 catalysis nor observed
  oxidative-deamination/cyclization microsteps are claimed.
- Three hash-bound ledgers under `evidence/PF01959/` retain current domain
  identities, primary White2004 assay details and Porat/GriH context limits.
  Original White PDF pages3/7/9 were visually inspected. The reported330nmol
  exceeds the stated200nmol ASA and275nmol DKFP; air/argon wording also
  conflicts. DHB3,4/4,5 wording instead maps onto the same substituted ring
  by reversing numbering and is not treated as a distinct-product conflict.
  MMP0006's negative growth phenotype is not replaced by aroA' rescue results;
  the GriH abstract is a follow-up lead, not an observed graph.
- Native CREATE `2026-10-12T144726Z-codex-ac3bba.yaml` and REVIEW
  `2026-10-12T145310Z-codex-ce7b5e.yaml` are under `history/records/PF01959/`.
  The first review command mistyped its start time and was rejected before
  saving; the successful retry used the actual14:53:10Z review start.
  The retained partial scientific self-review is
  `reviews/structured/20261012T145330Z-pf01959-joint-enzyme-assays-and-quantitation-limits/review.yaml`
  with native-derived `review.md`, NEEDS_FOLLOWUP/pass_with_limitations and
  open `pf01959-causal-context-coverage`. Its semantic digest is
  `b3ea3c2386d3b5558fc903f0ea2702d5df5320060e8b461c0eb04ec9abbf5c39`.
- Guarded regeneration/check validates8,296 records with zero drift. All
  inventory digests,128 imported identities, latest review/evidence hashes
  and rendered JSON records match. Totals:128 IN_PROGRESS,8,168 SEEDED,
  122 graph-bearing,8,174 graphless,732 graphs,1,540 edges (1,520 OBSERVED,
  3 INFERRED,1 CONTESTED,16 HYPOTHESIZED). Native/shared validators cover
  294 history files,153 reports and145 structured bundles; schemas and
  README corpus statistics are current.
- Exports regenerate and check cleanly. Structured TSV comparison toHEAD
  shows only128 KGX-node and127 SSSOM curation-status changes; association
  edge bytes are unchanged. SHA256: nodes
  `3685920164af6523f3d771da9badbbda3dcb30113dc30763546f7511e2255f2f`,
  edges `7c5ac1162eb92d57843e10f05f0ee95dcbd83d93a4ce1478628536f914e74679`,
  SSSOM `9752d3706dbcb3664931b188873dd97267df3452d0b9f111235bf6b803d79c0e`.
- All128 local previews regenerate. PF01959 passes1440/390px browser checks
  for three edges/two graphs, unique IDs, evidence toggles, page overflow and
  JavaScript errors; four representative screenshots were visually inspected.
  The sandboxed Chromium launch failed at macOS Mach-port registration1100;
  an approved local-only retry passed with HTTP(S) blocked. Filesystem reads
  succeeded without escalation, and the installed causal-graph skill passed
  quick_validate. The earlier filesystem-read denial was not reproduced;
  no permissions or configuration were changed.
- The main checkout's three user paths are untouched. No full128-page browser
  sweep, full publication QC, source-pin update, commit, push or publication
  is claimed. PF01969 is the next ascending uncurated accession, verified by
  gitignore-independent directory enumeration. All8,296 families and earlier
  open follow-ups remain in scope; this checkpoint is not goal completion.
- The focused graph, record, review, structured-review, review-contract,
  history, projection-binding and export suite passes294 tests in176.65s,
  with one upstream LinkML dataclass-extension deprecation warning. Tracked
  diffs, the new overlay/ledgers and the progress document have no whitespace
  diagnostics. These checks do not imply complete scientific coverage.

PF01969 LarC reaction/reporters and source-reconciliation checkpoint (2026-10-12):

- Curated9 graphs and42 edges:38 OBSERVED/EXPERIMENTAL and4 contextual
  HYPOTHESIZED. Two whole-reaction MS edges are DIRECT,26 reporter edges
  INDIRECT, and10 observed preparation/coupled-assay effects UNRESOLVED.
  Q2RFJ5 v1/Moth_2512 is396aa with PF01969 4-383; F9UST1 v2 and its
  frameshift/fusion/fragment contexts are distinct follow-up targets.
- Three hash-bound ledgers under `evidence/PF01969/` retain current identity,
  Turmo2022 Methods and original Figures2/3/4/6, and Wolfe2026 full text,
  original Figures2/3/4 and supplement TableS1 PDF pages7-9. The first
  supplementary ZIP was incomplete; the successful retry passed all CRCs.
  Failed HTML/PDF retrievals are not treated as inspected primary evidence.
- Original2026 Figure2B shows H72A above WT; H70A is absent from the plot
  and has no observed edge. Figure3D supports small E243A/R323A increases
  and E300A decrease while the prose describes retained full activity.
  Repeated H53A/H226A plots are deduplicated. R71 is not called acidic.
- TableS1 confirms LarE/LarC on pRSFDuet, resolving the main Constructs
  paragraph's LarA/LarC wording against the Expression Methods. Other
  discrepancies remain:21 plotted unique alanine variants versus count20;
  shortened EINSEESS in Figure4B versus EINEESS encoded by the primer;
  nominal GGGGSGGGGS flexible linker versus in-frame fragment GGGSGGGGSS.
  Edges use the author-named constructs, not invented corrected sequences.
- The2022 MgCl2/Mn-CTP recipe, final mixing concentrations, Figure6
  normalization and activity n1/error bars remain unresolved. E364A retains
  near-WT reporter activity despite little accumulated intermediate. PPase
  alone does not enhance the control. The no-added-nickel-growth protein
  underwent nickel-affinity purification and is not established nickel-free.
- Native CREATE `2026-10-12T181024Z-codex-1a18fc.yaml` and REVIEW
  `2026-10-12T181916Z-codex-79ddcb.yaml` are under `history/records/PF01969/`.
  The retained partial scientific self-review is
  `reviews/structured/20261012T181928Z-pf01969-larc-readouts-linker-conflicts-and-hypotheses/review.yaml`
  with native-derived `review.md`, NEEDS_FOLLOWUP/pass_with_limitations,
  and open `pf01969-causal-context-coverage`. Semantic digest:
  `f8b835627f09083bc521b0f4ea55a8b410af9f9ecc56a56d81879469e52cdd1e`.
- The native dry-run and initial apply each validate8,296 records and change
  only the expected PF01969 projection and manifest relative to the preceding
  checkpoint. Targeted graph checks pass all42 hashes/quotations, direction
  corrections, H70A/E364A exclusions, duplicate avoidance and hypothesis
  separation. Final guarded check validates8,296 records with zero drift;
  schemas and README corpus statistics are current. Native validators cover
  296 history files,154 reports and146 shared structured bundles.
- All8,296 inventory digests and all129 curated records' imported identities,
  rendered JSON, latest scientific review digests and retained source hashes
  match. Totals:129 IN_PROGRESS,8,167 SEEDED;123 graph-bearing,8,173 graphless;
  741 graphs and1,582 edges (1,558 OBSERVED,3 INFERRED,1 CONTESTED,
  20 HYPOTHESIZED). Frozen worklists and configuration remain unchanged.
- Exports regenerate and check cleanly. Structured TSV comparison withHEAD
  finds only129 KGX-node and128 SSSOM curation-status changes; association
  edge bytes are unchanged. SHA256: nodes
  `23dd33805d73d875604640051b9f73768c04a598f9335748ec18124e9881f66c`,
  edges `7c5ac1162eb92d57843e10f05f0ee95dcbd83d93a4ce1478628536f914e74679`,
  SSSOM `e27332b855745ee45d28a2d400aa123d8a26f7d7a130620583345805b0d29b74`.
- All129 local previews regenerate. PF01969 passes1440/390px checks for42
  edges/nine graphs, unique IDs, evidence toggles, expected uncertainty labels,
  no page overflow and no JavaScript errors. Four representative screenshots
  were visually inspected. A first harness assertion incorrectly expected
  hidden mechanism text before opening its evidence panel; checking it after
  opening passes without a site change. Chromium ran with approved local-only
  escalation because earlier sandbox launches failed macOS Mach-port setup;
  the script blocks HTTP(S). Filesystem reads succeeded without escalation.
- The focused graph, record, review, structured-review, review-contract,
  history, projection-binding and export suite passes294 tests in174.03s,
  with one upstream LinkML dataclass-extension deprecation warning. Tracked
  diffs and the nine new/progress files have no whitespace diagnostics.
  The main checkout's three user paths remain untouched. No full129-page
  browser sweep, full publication QC, source-pin change, commit, push or
  publication is claimed.
- PF01970 is the next ascending uncurated accession, verified by directory
  enumeration independent of gitignore. Earlier open family follow-ups
  remain in scope; this is not full-family or corpus completion.

PF01970 TctA/TpiA cellular and cation-context checkpoint (2026-10-12):

- Six PHENOTYPIC graphs retain sixteen OBSERVED, EXPERIMENTAL edges:
  fourteen UNRESOLVED and two INDIRECT. The latter concern joint-system
  extracellular TPA depletion and the CitAB-deletion tctA transcript response.
  There is no DIRECT edge or family-wide substrate/ion mechanism.
- E6 BAN66712.1/TctA is505aa with archived PF01970 20-440;
  BAN66716.1/TpiA is503aa with archived20-441. ENA AB822590.1 and
  AB822591.1 preserve Comamonas sp.E6 and its taxon364029. Historical
  S6BR91/S6BBY9 are deleted redundant UniProt entries, not current reviewed
  proteins. C. glutamicum cg3125=NCgl2724 maps CAF20846 v1,510aa,
  archived20-443; Q6M234 is inactive. Final clone sequences and new profile
  scans remain open; similarity does not relabel the experimental strain.
- Original Hosaka2013 Figures3/4/5/7 and Brocker2009 Figures2/4 were
  visually inspected, with relevant Methods/Results/Discussion and Table3.
  All sixteen edge quotations match the primary HTML and retained ledgers.
  EME019 residual citrate uptake is about54%WT; delayed growth is represented
  as increased time to growth. Magnesium/strontium opposite deletion effects
  are explicit. PpY1100 is a resting-cell conversion assay, not growth rescue;
  its complete construct combines transport and catabolic genes.
- Three evidence ledgers preserve primary contexts and identity, with SHA256:
  identity `3384944e991d58edf0a31c562608e73773218c9f7a2f89cbbf29d82aca185fdb`,
  Hosaka `50018f425a88bd7f3f9eceb347fbc57e7d3887790b8f6f13d39dc83e2e3198b5`,
  Brocker `be8f9ff0675460bbde673d7b068c5eb42abefb09014f8e831fe03d1dcb6320aa`.
  The Hosaka supplement returned XML/HTML rather than experimental PDF;
  its figures were not inspected. Brocker's Methods/Figure2 host discrepancy,
  Casamino Acids input and nickel-toxicity confound remain visible. The2014
  metagenomic modeling source does not yield an observed transport edge.
- Actual CREATE `2026-10-12T205243Z-codex-0f32a8.yaml` and REVIEW
  `2026-10-12T205949Z-codex-b63398.yaml` are under `history/records/PF01970/`.
  The native-saved review is
  `reviews/structured/20261012T210007Z-pf01970-tcta-tpia-cellular-effects-and-cation-contexts/review.yaml`
  plus derived `review.md`; same-agent, partial, NEEDS_FOLLOWUP,
  pass_with_limitations. Semantic digest
  `2269f09e2bc22522eeb7a7677561db012ce7d817d7ebdf9444b49614b6bc8934`.
  PF01970 remains IN_PROGRESS, with exact constructs, other member evidence
  and direct transport/partner/ion mechanisms open.
- Targeted native validation, all sixteen evidence hashes/quotations,
  direction/readout assertions and schema-artifact check pass. The first
  dry-run overlapped a final ledger revision and rejected its old hash;
  after the quote/hash refresh, the completed rerun validates8296 records
  with only the expected projection and manifest requiring regeneration.
- Final records-check validates8296 records with zero generated drift;
  history-check validates298 canonical files, native reviews-check155 reports,
  and shared review-check147 declared-scope reviews. Documentation checks pass.
  All8296 inventory digests and130 current scientific-review/source hashes,
  imported identities and rendered JSON records match. Current structural
  counts are130 IN_PROGRESS,8166 SEEDED,124 graph-bearing,8172 graphless,
  747 graphs and1598 edges (1574OBSERVED,3INFERRED,1CONTESTED,20HYPOTHESIZED).
- Exports apply/check cleanly. Structured TSV comparison versusHEAD finds
  only130 KGX-node and129 SSSOM curation-status changes; association edges
  remain byte-identical. SHA256: nodes
  `deb69b10cebb476f9178e25841268125065fbb382e5c37c8b5ec11b8988cac8a`,
  edges `7c5ac1162eb92d57843e10f05f0ee95dcbd83d93a4ce1478628536f914e74679`,
  SSSOM `0a28a6073d789793d72d89bf9ca1c6288b689af03c79bfc0be802ee5c97df805`.
- All130 local previews regenerate. PF01970 passes1440/390px checks for
  sixteen edges/six graphs, correct support labels and opposite effect signs,
  unique IDs, working evidence toggles, no page overflow or JavaScript errors.
  Four representative screenshots were visually inspected; mobile tables
  retain their existing internal horizontal scroll. Chromium used approved
  local-only escalation after the earlier sandbox Mach-port failure; HTTP(S)
  is blocked in the harness. Filesystem reads succeeded without escalation.
- The focused graph, record, review, structured-review, review-contract,
  history, projection-binding and export suite passes294 tests in173.47s,
  with one upstream LinkML dataclass-extension deprecation warning.
  Nine new/progress files and tracked diffs have no whitespace diagnostics.
  Main's three user paths, frozen worklists, conf and source pins are untouched.
  No full130-page browser sweep, full publication QC, commit, push or
  publication is claimed. Directory enumeration independent of gitignore
  identifies PF01972 as the next ascending uncurated accession; earlier open
  family follow-ups remain in scope.

The bounded PF01901 follow-up resolved catalog lineage and inspected selected
2008capsule and2021BECP10 primary contexts. Exact historical alleles, partial
domain attribution, controls, source discrepancies and further contexts remain
open. The2004 full paper remains inaccessible through attempted endpoints;
2008supplements and the timed-out partial2021archive were not inspected. These
are coverage limits, not negative findings. ArchaealQ57862/MJ0419 andQ57863/MJ0420
remain uncharacterized in the inspected annotations, not proven unstudied.
FPC840_340035 remains a mapping/association lead. The subsequent PF01902 pass
retains whole-protein versus domain boundaries, observed versus hypothetical
chemistry and distinct cellular contexts. Historical constructs, source
conflicts, inaccessible supplements, archaeal and native-human experiments,
and B12-related members still need follow-up. PF01904 now retains its two
scoped graphs, with independent growth validation, exact clone identities,
model-to-experiment tests and further member evidence still open. PF01905 adds
separate Csa2 binding and conditional DevR phenotypes, with molecular regulation,
exact alleles, missing supplements and later member contexts still open. PF01906
adds ten YbjQ joint-genotype effects without asserting a metal-binding mechanism;
clone/control gaps, retron primary sources and Rv1762c-specific evidence remain
open. PF01909 adds scoped GlnD biochemistry while leaving exact historical
clones, raw gels, ligand/metal mechanisms and the other NTase branches open.
PF01910 adds distinct bacterial binding and fungal phenotype branches, with
source discrepancies, historical clones, molecular mechanisms and other members
still open. PF01914 adds SnatA, MarC and YchE cellular contexts while
retaining clone/background/source discrepancies, conditional negative results
and unresolved transport mechanisms. PF01918 adds separate Alba DNA, RNA and
nuclease contexts, retaining the native-PTM dispute, source-unit issues,
historical constructs and additional eukaryotic/archaeal branches as follow-up.
PF01923 adds PduO/EutT/MMAB contexts while keeping exact construct, source
discrepancy, cofactor-transfer/repair and further member questions open.
PF01925 adds separate CysZ, PmpC and MamO contexts while keeping direct
transport, CysZ primer/vector conflicts, precise expression constructs,
MSR-1/RS-1 experiments, alternative sulfonates and other member systems open.
PF01927 adds separate MUT-7/EXD3 biochemical, assembly and cellular contexts.
Native RNA targets, remaining animal/plant/prokaryotic members, historical
constructs and source discrepancies remain open; the predicted RNA forceps
model is not an observed causal chain.
PF01930 adds Pcal_0546 and Gsu fusion/Cas2 contexts with native roles, source
conflicts and the remaining Cas4/DNA2 member branches still open.
PF01931 adds separate YjjX and human PRRC1 contexts while leaving exact
constructs, source discrepancies, Mys/PKA developmental experiments and
domain-specific/member coverage open.
PF01933 adds separated CofD/FbiA and GlmR contexts with unresolved constructs,
source conflicts, accessory uridyltransferase and other member evidence open.
PF01934 adds separate HepT modification/RNA/cellular and fusion contexts;
remaining cyanobacterial, operon, native activation and member evidence is open.
PF01935 adds separated archaeal HerA assays with current Pfam-domain boundaries;
bacterial, antiviral, other archaeal and atomic-coupling contexts remain open.
PF01936 adds separate human/mouse MARF1 contexts and resolves historical-name
cross-family transfers; native RNA targets, full constructs, nonmammalian
members and later MARF1/EDC4/P-body studies remain open.
PF01938 adds accession-mapped TRAM0076 contexts with DNA/RNA substrate,
variant/host and induction distinctions; other members, exact constructs and
direct native RNA mechanisms remain open.
PF01939 adds separated NucS cleavage, clamp and native mutation contexts;
the conflicting Cgl product assignments, other members, native intermediates
and remaining primary figures/constructs remain open.
PF01940 adds separate VTE6, PGR and TMEM19 contexts; isolated-domain mechanisms,
remaining constructs/controls, phylloquinone/PSI, upstream regulators and other
member experiments remain open. Toxicity is hypothetical, probe labeling is not
native receptor activation, and gene perturbations retain unresolved intermediates.
PF01941 adds separated TkMAT, MjMAT and engineered PC-MjMAT contexts;
earlier kinetics, SsoMAT/PfMAT, bacterial members, ancestral constructs,
remaining variants and native mechanisms remain open. Surrogate breakdown
products are not direct MAT products, and joint cap cascades are not direct
RNA methylation by MAT alone.
PF01944 adds scoped Bacillus localization, abundance and allele-specific
suppression effects. Direct binding/catalysis, exact historical constructs,
remaining source figures, Q18B81 family mapping and bacteriocin/archaeal
member mechanisms remain open. The source's I92T/I82T and strain-label
discrepancies are retained, not silently repaired.
PF01947 adds scoped cell-free lyase chemistry and Sll1797 cellular effects.
R30/E120 catalysis, historical sequences, assay controls, Table1 normalization
and supplement history, missing source figures and archaeal/plastid member
functions remain open. The independent Du deletion/rescue is a distinct context;
no direct PQ-to-oxygen-to-growth chain or E. coli UbiC family transfer is asserted.
PF01949 adds five homologs' ssDNA cleavage, separate Afu/Halo dsDNA and assay
perturbations, and H26 RNA/optical-density phenotypes. Exact mutant identity,
historical constructs, Halo/Gm profile coordinates, H26 allele/polarity/rescue,
RNA-seq replication, native repair intermediates, patent and other-member
evidence remain open. The source's H166A/H166R conflict is not silently resolved.
PF01950 adds scoped Thermococcus F6P chemistry, conditional growth and
rich-medium RNA/extract phenotypes. The later bifunctional reaction,
selective-activity rescue, exact assay methods, carbon-response mechanism
and additional members remain open; verified ST0318 construct numbering
is retained without inventing residue-level edges.
PF01951 now includes bacterial turnover, human complex/depletion/rescue,
DDX1 partner controls and Jurkin human XBP1/tRNA branches alongside its earlier
archaeal and PAB1946 contexts. Exact clones, Popow base protocol, Jurkin
preparation/buffer/primer discrepancies, fly allele/rescue/localization and
further cellular/biochemical contexts remain the immediate follow-up,
alongside Auxilien figure access and source discrepancies. PF01954 now has a
scoped graphless assessment; member-specific functional evidence, supplementary
mapping, later full papers and metadata reconciliation remain open. The former
PF01952 pointer was incorrect: an ignored-file-inclusive search and the actual
retained membership identify PF01954 through PF01959 and PF01969 among the now
partially assessed records. PF01970, PF01972 and PF01973 are now also partially
assessed. PF01976 now has a scoped graphless assessment. Continue PF01973's
later Maf/member contexts and PF01976's open evidence questions; PF01977 is the
next untouched ascending accession, not a reason to drop earlier follow-ups. PF01955's
immediate follow-ups are unresolved CbiS2006 clones, assay conflicts and native
mechanisms, the2008 historical donor strains/inserts, supplemental product traces,
reporter and unit conflicts, historical deletion alleles and fusion junctions,
and Gray2009 supplements/assay details. The2008 donor/induction/AP/extract,
native2009 and remodeling2009 main contexts are separately curated; this does not
resolve the full native pathway or other members. PF01956 retains separate
assembled-complex insertion, human/yeast EMC3 phenotypes and selected TMCO1/GEL
biogenesis effects. The inaccessible TMCO1 channel experiments still need full
primary inspection and historical isoform mapping; substrate-driven recruitment,
source-data gels/tables, archaeal Ylp1, original EMC genetics, later holo-insertase,
native clients and exact construct/protocol questions remain immediate follow-up.
PF01957 needs original 2006 figures/supplements, historical YbbJ/YqeZ alleles,
the full 2024 QmcA-YbbJ perturbation experiments, PH0471/PH1510 construct-level
research and other bacterial members. Its current graphs do not include the
distinct PF31148 NfeD2-FloT effects or assign N-terminal proteolysis to PF01957.
PF01958 needs original2003 figures and inhibitor/construct controls, exact2017
sequence mapping and source-label reconciliation, further bacterial/archaeal
experiments, and accessible humanASPDH preprint methods/product data. Its
iminoaspartate and cellular NAD-role interpretations are not observed edges.
The human preprint is not treated as peer-reviewed or assigned a bacterial
substrate on the strength of domain membership.
PF01959 needs quantitative reconciliation of White2004 Table2, original
Porat2006 growth plots and allele controls, full GriH primary experiments,
historical constructs and additional archaeal/member contexts. Shared domains
do not establish common substrate/cofactor specificity; the MMP0006 negative
phenotype is not replaced by the other gene's positive deletion/rescue result.
PF01969 needs exact sequenced constructs and resolution of shortened and
alternative-linker sequence conflicts, incomplete variant/primer coverage,
2022 Mg/Mn and normalization/replication discrepancies, fixed2026 reporter
conditions and mutant abundance/folding/occupancy controls. Full earlier
L. plantarum genetics/fusion chemistry,2024 analog assays,2025 expression
contexts and other family members remain open. Its transfer and Glu104
chemistry graphs remain hypotheses, not observed atomic mechanisms.
PF01970 needs the Hosaka supplement and exact E6 insertion/complementation
constructs, reconciliation of Brocker DH5alpha/MG1655 host labels, current
domain remapping and direct transport/ion/partner experiments. Salmonella,
Bordetella, Pseudomonas and Gillisella primary contexts remain open. The
metagenomic2014 model is not observed transport; its length and source-organism
questions are unresolved. Cellular effects are not universal family mechanisms.
Every uncurated family and these open follow-ups remain in the corpus-wide goal.
No full family or corpus completion is claimed.

PF01972 needs the historical Mm2878 clone/preparation, matched reporter controls,
direct products, replication and residue-level tests. The original2004 alignment
image and mapping, the2026 structural-study experiments and broader member
coverage remain open. Its one OBSERVED edge is a preparation-level reporter
response, not proof of purified-enzyme or isolated-domain chemistry; the separate
SDH mechanism remains HYPOTHESIZED.

PF01972 continuation checkpoint (2026-10-14):

- Native CREATE `history/records/PF01972/2026-10-14T204247Z-codex-3b40ac.yaml`
  and REVIEW `history/records/PF01972/2026-10-14T204946Z-codex-4713e3.yaml`
  accompany the human overlay and four minimal evidence ledgers. No full paper
  or thesis was added to the repository.
- The retained scientific self-review is
  `reviews/structured/20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis/`.
  Its current semantic digest, also verified against the inventory, is
  `24faf6f67f7cf3f7646966e2e6d756868e9476c6ef3d8b0203081b9edf72c1d7`.
  The report preserves a partial-scope NEEDS_FOLLOWUP verdict and open finding
  `pf01972-causal-context-coverage`; no status promotion or independent approval.
- The regenerated projection preserves every imported field. All other 8,295
  projection manifest entries are unchanged. KGX and SSSOM each change only
  PF01972's curation-status representation; association edges are unchanged.
  The inventory verifies all 8,296 rows: 131 IN_PROGRESS, 8,165 SEEDED,
  125 graph-bearing, 8,171 graphless, 749 graphs and 1,600 edge entries.
- The graph/QC regression suite passed 52 tests. Schema generation is current;
  record regeneration verifies 8,296 records with zero drift; all 303 canonical
  history files validate. Export and inventory read-only checks pass. Current
  overlay/evidence hashes match the retained review after REVIEW-index refresh.
- Final `just validate-all` passed: 8,296 current projections, 303 history files,
  four review-contract tests (126.85s), 154 structured bundles and 162 native
  reports. Review validity covers declared scopes, not scientific completion.
  The upstream LinkML `topClass` deprecation warning remains informational.
- A separate unpinned local preview passes 1440px and 390px browser checks for
  graph/edge counts, support labels, evidence disclosures, document width and
  JavaScript errors. Both screenshots were inspected. The temporary harness's
  initial title-case expectation was corrected to the native uppercase labels;
  no renderer or scientific content was changed for that test.
- Canonical Pages and source pins are unchanged. The actual source-pin check
  rejects the changed PF01972 bytes pending a new authorized source checkpoint;
  no full publication-QC pass, commit, push or publication is claimed. The main
  checkout's three pre-existing untracked paths remain untouched.
- Directory enumeration independent of gitignore identifies PF01973 as next.
  Initial leads, not curated edges, are the MptE discovery study
  [PMID22931285](https://pubmed.ncbi.nlm.nih.gov/22931285/),
  [8SD5/MJ1634/Q59028](https://www.rcsb.org/structure/8SD5), and the bacterial
  Maf study linked by [5MU5](https://www.rcsb.org/structure/5MU5),
  [PMID29076618](https://pubmed.ncbi.nlm.nih.gov/29076618/).
  Inspect full methods/figures and exact current domain mappings before combining
  or transferring the archaeal kinase and bacterial glycosylation contexts.
  PF01973 is still SEEDED; all earlier open family follow-ups remain in scope.

PF01972 publication review (PR #200, 2026-10-14):

- The initial source-pin failure was reproduced locally and in CI and tracked
  in [issue #201](https://github.com/CultureBotAI/DUFMech/issues/201).
  The published annotated candidate `source/dufmech-pr-200-candidate` retains
  `b6793ba2005e4429f0cef96a31a328825e655a00`; all 9,098 candidate source pins
  passed local byte verification and the canonical online retention gate.
- Fresh integrity checks verify all 8,296 manifest hashes, unchanged imported
  PF01972 fields, exact overlay/projection and review/inventory agreement, and
  status-only KGX/SSSOM changes. The other 8,295 projections and all association
  edges remain unchanged. The focused graph/QC suite passed 52 tests in 19.82s.
- Native candidate Pages were regenerated and PF01972 passed 1440px/390px
  browser checks for graph counts, support labels, disclosures and document
  width, without JavaScript errors. Both screenshots were inspected.
- The retained repository audit is a same-agent adversarial review, not
  independent expert approval or a replacement for the partial scientific
  review. Its own source-bearing checkpoint must be retained and rendered;
  full local QC and exact-head CI are mandatory before merge. The PR records
  those subsequent release outcomes. Preserve both annotated source tags
  when deleting the feature branch.
- No scientific finding is closed by publication. PF01972 stays IN_PROGRESS;
  its assay-attribution, triad-validation and broader-context questions remain
  open alongside the rest of the corpus.

PF01973 continuation checkpoint (2026-10-14):

- The overlay contains eight graphs and sixteen edges: fourteen OBSERVED
  effects and two HYPOTHESIZED/COMPUTATIONAL residue roles. PF0930 and MJ1634
  whole-protein biochemical assays are separate from heterologous folK rescue,
  AMB-1 deletion/rescue and the two independent Maf substitution experiments.
- Four minimal evidence ledgers retain exact mappings, inspected original
  figures/supplements, condition-specific negative results, uncertainties and
  the additional-source queue. No full publication or figure is redistributed.
  Current UniProt/Pfam data do not overwrite the frozen October10 snapshot.
- Canonical CREATE history is
  `history/records/PF01973/2026-10-14T222220Z-codex-7efd01.yaml`; REVIEW history is
  `history/records/PF01973/2026-10-14T223424Z-codex-efe5ea.yaml`.
  The saved report is
  `reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/`.
  It is a partial scientific self-review, NEEDS_FOLLOWUP, with open findings
  `pf01973-mpte-mechanistic-coverage` and
  `pf01973-maf-mechanism-and-member-coverage`. No independent approval or
  REVIEWED promotion is claimed.
- Native initial preview and guarded apply each validated all 8,296 records
  and identified only the PF01973 projection and ownership-manifest changes.
  The graph/QC regression suite passed 52 tests in 35.34s; schema generation
  found zero drift. Native record, overlay, evidence and source-preservation
  assertions passed with semantic digest
  `89129c238d759cb285e3ced3ca846405d18880302487db6e310c423ad29421bc`.
- Final `just validate-all` passed: 8,296 current projections with zero drift,
  306 valid history records, four review-contract tests (111.97s), 156 valid
  structured bundles and 164 native reports. The existing LinkML `topClass`
  deprecation warning is informational; these checks cover declared scopes.
- Read-only inventory reproduction verified all 8,296 rows; export reproduction
  reported current artifacts. A structured comparison verified every projection
  manifest hash, unchanged other 8,295 records, matching review/inventory digests
  after REVIEW-index regeneration, and unchanged reviewed overlay/evidence bytes.
  KGX and SSSOM change only PF01973's status; association edges are unchanged.
  `git diff --check` passed. No source snapshot, schema, application code or
  canonical Page was modified.
- The refreshed structural inventory has 132 IN_PROGRESS and 8,164 SEEDED
  families, 126 graph-bearing and 8,170 graphless, 757 graphs and 1,616 edge entries.
  These are structural counts, not independent experiments or completed reviews.
- A separate unpinned preview passed 1440px and 390px browser checks for all
  eight graphs, sixteen edges, support labels, evidence disclosures, document
  width and JavaScript errors. Six screenshots were inspected. The initial
  localhost bind was sandbox-denied; the approved rerun succeeded and closed
  its temporary server. Canonical Pages remain unchanged.
- The actual source-pin check rejects the changed PF01973 projection pending
  a separately authorized retained source checkpoint. No full publication-QC,
  commit, push or publication is claimed. Unrelated primary-checkout files
  remain untouched.
- Next: continue PF01973, especially the later Maf specificity/GlfM and
  Clostridium engineering contexts with exact construct/domain mapping.
  Europe PMC identity metadata confirm PMID38897200/doi:10.1016/j.cub.2024.05.058;
  its full experimental paper remains unassessed. Public full-text XML for
  PMID39169227/doi:10.1038/s42003-024-06736-y was retrieved and identity-checked;
  its Methods, figures and supplements still need scientific assessment.
  Every other family and all earlier open findings remain in the goal.
- After saving the review, a public copy of the Maf/GlfM paper was retrieved
  from [UNIGE](https://archive-ouverte.unige.ch/unige:178145). Its cover identifies
  the published version and CC BY 4.0; its SHA256 is
  `33b8af4c9c566d1fa0ec01b2e83528a2d88bf42d230136e4f51ca73b04d4e56c`.
  Full experimental/figure assessment remains next. Its primary data deposition
  is [Mendeley Data V1](https://data.mendeley.com/datasets/jrjkkb49vx/1).
- The Clostridium study has an
  [author correction](https://www.nature.com/articles/s42003-025-07774-w),
  PMID40021896, replacing pLogo panels v-x in Supplementary Figure 3. Retrieve
  the corrected supplement before assessing sequence-preference claims. Initial
  Methods inspection also distinguishes three biological preparations for intact
  mass analysis from one for tandem MS. Neither these preliminary checks nor
  successful retrieval close the saved coverage finding or add causal edges.

PF01973 publication review (PR #202, 2026-10-14):

- The initial source-pin rejection was reproduced locally and in CI run
  `38650949208`, tracked as [issue #203](https://github.com/CultureBotAI/DUFMech/issues/203).
  The initial local QC attempt was interrupted after that reproduced failure:
  288 tests passed and one failed before interruption; this is not a full-suite pass.
- Candidate checkpoint `bf3279f826a5fbb982f962dba292a3f033f1a288` is retained by
  annotated tag `source/dufmech-pr-202-candidate`. Native capture and online
  retention verification cover all 9,106 candidate source files. Canonical Pages
  were regenerated; no generated file or source ledger was hand-edited.
- The adversarial self-review checked all fifteen initial change paths and the
  candidate ledger/family page. Original MptE Figure 4 and Maf Results/Figure 5
  spot checks support the existing bounded interpretations. All 8,296 manifest
  hashes, unchanged other 8,295 projections, evidence quotes/hashes, review and
  inventory digests, and status-only export changes passed the integrity audit.
  The focused graph/QC regression suite passed 52 tests in 21.98 seconds.
- Canonical PF01973 browser checks passed at 1440px and 390px: eight graphs,
  sixteen edges, explicit observed/hypothetical support labels, evidence
  disclosures, no document overflow and no JavaScript errors. Six screenshots
  were inspected; the temporary server was closed.
- Save the publication review as an immutable structured bundle, retain its
  source-bearing checkpoint and recapture/regenerate before final full QC,
  exact-head CI and merge. These candidate checks do not claim those later
  release gates have already passed. Preserve annotated source tags after
  deleting the feature branch.
- Scientific findings remain open as
  [issue #204](https://github.com/CultureBotAI/DUFMech/issues/204) for archaeal
  constructs/native biochemical scope and
  [issue #205](https://github.com/CultureBotAI/DUFMech/issues/205) for later
  Maf/GlfM systems and discriminating residue mechanisms. Publication does not
  close these findings, promote IN_PROGRESS, or complete the corpus-wide goal.

PF01973 Maf/GlfM continuation (2026-10-15, local curation):

- Assessed Unay2024 (PMID38897200) through the primary article and its public
  UNIGE supplement, including Methods, Figures 1-5/S1-S5, Tables 1-2 and S1-S6.
  Exact MR-1 Maf1/Maf2 profiles are 174-338/822 aa and 182-352/441 aa. GlfM is a
  separate PF26154 partner; FlaA/B are acceptors, not PF01973 members.
- Added 28 graphs with 56 observed, context-specific effects. The family now has
  36 graphs and 72 edges: 70 OBSERVED and the two unchanged HYPOTHESIZED edges.
  New cellular/reporter effects are not labeled direct purified-enzyme chemistry.
  Original eight graphs, three older primary/mapping ledgers and prior reviews
  remain unchanged; the dated coverage ledger has a successor entry.
- Coverage includes native deletion/rescue, individual Maf substitutions,
  CTD truncations, BACTH readouts, GlfM variants, grouped acceptor substitutions,
  donor-pathway loss, heterologous reconstitution and CN-32 partner substitution.
  Joint inputs, host backgrounds, residual activity and unobserved peptide
  distinctions remain explicit. A +220 Da adduct is not presented as proven KDO.
- S6's deposited synthetic Maf2 sequence encodes L230S relative to both Q8EC85
  and AAN56257.1. Translation/alignment verified the full 441 aa, one mismatch,
  and its exact codon; the physical experimental plasmid is not known to match
  that deposited design. Genomic deletions and genome-amplified BACTH constructs
  remain separate. S4/Methods plasmid conflicts and S180/A181 numbering are
  retained in evidence/PF01973/unay-2024-member-mapping.txt.
- Kurthia and Irchel Maf experiments were inspected, but exact PF01973 profile
  mapping remains open; a COG2604 hit is not substituted for it. S5A also shows
  residual Kurthia modification without GlfM, preventing universal necessity.
  Archaeal findings, other bacterial contexts and the corrected Clostridium
  supplement remain open. This does not close issues 204/205 or the corpus goal.
- Baseline records-check passed 8,296 records with zero drift. Focused native
  graph/QC regression tests passed 52 tests in 27.19s. The first history command
  rejected an invalid actor enum without creating an event; the corrected
  ai_agent command succeeded. A preview overlapping that append detected stale
  history indexing and refused it; subsequent preview/apply must use the settled
  sidecars. No guard was bypassed. Final regeneration/review checks follow.
- The settled REVIEW event is
  `history/records/PF01973/2026-10-15T002541Z-codex-1400a3.yaml`; subsequent
  guarded regeneration validated 8,296 records and applied only the projection
  and ownership manifest. The saved partial scientific successor is
  `reviews/structured/20261015T002305Z-pf01973-maf-glfm-contexts/`.
  Its three findings remain open, with the new construct-identity finding tracked
  in [issue #207](https://github.com/CultureBotAI/DUFMech/issues/207).
- Publication is now separately authorized. The initial native source-pin check
  rejected the changed overlay, tracked in
  [issue #206](https://github.com/CultureBotAI/DUFMech/issues/206).
  A retained source checkpoint, canonical rendering, adversarial publication
  review, full local QC and exact-head CI are required before merge. Publication
  does not resolve the three scientific findings or complete the corpus goal.

PF01973 Maf/GlfM publication review (PR #208, 2026-10-15):

- The candidate checkpoint `0fc1b328560ad751c28eebfb5093414f59205e0c` is
  retained by annotated tag `source/dufmech-pr-208-candidate`. Native capture
  and canonical online retention verification pass for all 9,112 source files.
  Initial CI run `38660518906` reproduced the source-pin failure before full QC.
- Fresh focused regressions pass 52 tests in 27.18s. Integrity checks verify
  all 8,296 manifest hashes, four canonical PF01973 events, unchanged original
  graphs and imported fields, exact review/inventory digest agreement, and
  unchanged other family projections, frozen inputs, exports and old reviews.
  The corpus inventory now has 785 graphs and 1,672 edges across 126 families;
  this is structural coverage, not a count of independent experiments.
- Primary Tables 1/2, Figure 4 and supplemental Figure S4C were visually
  rechecked. S4 plasmid descriptions and S6 translation/alignment reproduce
  the recorded construct conflict. Native FLAG-tag abundance controls do not
  certify every SPOT-tag or BACTH lineage. No new blocking scientific defect
  was established in this scoped adversarial self-review.
- The publication review is not independent approval. Retain its own source
  checkpoint, recapture and regenerate through native writers, then require
  full local QC and exact-head CI before merge. The PR records subsequent
  release outcomes. Preserve both source tags after deleting the branch.
- Issues [#204](https://github.com/CultureBotAI/DUFMech/issues/204),
  [#205](https://github.com/CultureBotAI/DUFMech/issues/205) and
  [#207](https://github.com/CultureBotAI/DUFMech/issues/207) remain scientific
  follow-ups. None is resolved merely by publishing this bounded extension.

PF01973 Kurthia/Irchel ortholog extension (local curation, 2026-10-15):

- Six graphs add eight observed cellular effects from Unay2024 Figure 5D and
  Figure S5A/B. PF01973 now has 42 graphs and 80 edges: 78 observed and two
  hypothesized. The prior 36 graphs and their evidence are unchanged.
- Exact PF01973.24 HMM mapping places Kurthia WP_068455574.1 at alignment
  residues 159-329 and Irchel3E13 WP_095156947.1 at 196-352. Both pass the
  profile gathering threshold. The distinct envelopes, model/sequence hashes,
  software parameters and MR-1 positive controls are retained in
  `evidence/PF01973/unay-2024-ortholog-contexts.txt`.
- Kurthia's complete Maf/GlfM deposited design bodies match their references.
  Irchel's FliC/Maf construct is synthetic, but its sequence is not supplied
  among the nonempty S6 fragments. Physical plasmid identity remains unresolved.
  Neither result resolves the earlier MR-1 Maf2 L230S discrepancy.
- S5A retains partial Kurthia Hag modification-associated retardation without
  GlfM and compares delta-flmG with the double delta-flmG delta-neuB mutant.
  S5B instead uses WT and single delta-neuB, retaining host FlmG. The new
  edges do not assert isolated Maf sufficiency, direct glycosyl transfer,
  a protein-stability mechanism or universal GlfM necessity.
- The partial scientific self-review is
  `reviews/structured/20261015T021620Z-pf01973-kurthia-irchel-contexts/`.
  It preserves all three prior finding identities, targets and open issues
  204/205/207. Canonical EDIT/REVIEW history was appended and regenerated;
  PF01973 remains IN_PROGRESS, not a completed family characterization.
- All 8,296 manifest hashes, original graph/evidence preservation, unchanged
  other projections, frozen inputs and exports, 52 focused graph/QC tests,
  schema reproduction and 1440px/390px unpinned preview checks passed.
  The final inventory has 791 graphs and 1,680 edges across 126 families;
  8,170 remain graphless. These counts do not establish scientific completion.
- Final `just validate-all validate-schema` passed: 8,296 current projections
  with zero drift, 310 history records, four review-contract tests, 160
  structured bundles and 168 native reports. Inventory and export reproduction
  passed after the REVIEW-index refresh. The scientific digest remains
  `65179fa078d0fbfc89696fbeebcd5ac910c750601df893fb8475096322bf65ff`.
- Canonical Pages and source pins are unchanged by this local pass. The full
  8,296-family objective and earlier corpus findings remain active, including
  remaining Maf studies, corrected Clostridium evidence and archaeal mechanisms.

PF01973 Kurthia/Irchel publication audit (PR #210, 2026-10-15):

- The initial local source-pin check and CI run `38672125477` rejected the
  changed overlay. [Issue #209](https://github.com/CultureBotAI/DUFMech/issues/209)
  tracks the publication blocker; neither the guard nor generated hashes were
  bypassed. Candidate `5e92882f31859625c1061a17127001e59b307972` is retained by
  annotated tag `source/dufmech-pr-210-candidate`. Native capture and canonical
  remote verification pass for all 9,118 candidate source files.
- Adversarial self-review visually rechecked Figure 5D and S5A/B, their legends,
  Methods and the S4/S6 construct records. The exact HMM rerun reproduces the
  original result bytes; both complete Kurthia design bodies match references.
  No additional blocking scientific defect was established. This is not an
  independent expert review or a completed family-wide assessment.
- Fresh focused regressions pass 52 tests in 22.47s. The initial test invocation
  omitted the required shared runtime path and failed one adapter test; the
  configured rerun passed without code changes. All 148 checked runtime files
  and 22 governed artifacts match the CI-pinned CLAW revision.
- Canonical Pages were regenerated through the native writer. At 1440px and
  390px, checks pass all 42 graphs/80 edges, the six new graph headings/eight
  edge rows, mapping and support labels, evidence disclosures and pinned source
  links, with no document overflow or JavaScript errors. Selected screenshots
  were inspected. The scientific digest and prior 36 graphs remain unchanged.
- The audit-bearing checkpoint must be retained and recaptured before final
  full local QC, exact-head CI and merge. Subsequent release results belong in
  PR #210; retain both source tags after branch cleanup. Scientific issues
  [#204](https://github.com/CultureBotAI/DUFMech/issues/204),
  [#205](https://github.com/CultureBotAI/DUFMech/issues/205) and
  [#207](https://github.com/CultureBotAI/DUFMech/issues/207) remain open.
  PF01973 stays IN_PROGRESS and the corpus-wide objective remains active.

PF01976 DUF116 causal-evidence assessment (local curation, 2026-10-15):

- Added three OPEN discussions and a minimal, source-hashed evidence ledger.
  Makarova2015's redox proposal remains comparative; automated prenyl-synthase
  labels do not identify DUF116 catalysis; the Zhou2017 DVU3364 frameshift is
  associated with a multi-mutant salt-evolved strain, not an isolated allele
  effect. No directed edge is adopted from the inspected material. This is
  a scoped graphless assessment, not a claim of functional absence.
- Verified reference intervals: Q58541/MJ1141 50-213, Q6M0V6/MMP0162 47-210,
  Q725R0/DVU3364 92-260; D5SS13 has PF01976 67-231 separately from PF00348
  297-545. Reference mappings do not certify experimental/evolved constructs.
  The original salt-study Table 1 continuation was visually inspected;
  exact allele reconstruction and supplementary primer checks remain open.
- Retained partial scientific self-review:
  `reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml`
  and its derived Markdown. Verdict is `pass_with_limitations`, native
  `NEEDS_FOLLOWUP`, with three open findings. PF01976 remains IN_PROGRESS.
  Semantic digest is
  `9b7bc79ac8aed0744b99795e721badc52fc8b5ae5a6d4dfc34002190ec4ce868`.
- CREATE history is
  `history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml`; REVIEW history is
  `history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml`.
  Both events were appended before the respective guarded regeneration.
- Final records-check validates all 8,296 records with zero drift. All 8,296
  manifest hashes match; only PF01976 changes. Schema reproduction is current,
  313 history records, 162 structured bundles and 170 native reports validate.
  The 52 graph/QC tests and four review-contract tests pass. KGX/SSSOM are
  current and change only PF01976's curation status; association edges,
  imported metadata, PF01973, frozen sources and prior reports are unchanged.
- The refreshed inventory retains 791 graphs and 1,680 edges across 126
  families, with 8,170 graphless. Only PF01976's status/digest changes among
  all 8,296 compared inventory rows; the native inventory check also verifies
  all 8,296 rows. There are 133 IN_PROGRESS and 8,163
  SEEDED records; these are partial-assessment counts, not completed science.
- The unpinned one-family preview passes at 1440px and 390px: graphless
  disclaimer, all three questions, exact mappings, evidence links, no overflow
  and no JavaScript errors. Selected desktop/mobile screenshots were inspected.
  An initial case-sensitive test selector was corrected to the existing
  lowercase heading; application/rendering code was not changed.
- Canonical Pages and source pins are unchanged. The actual source-pin check
  rejects the changed PF01976 bytes pending an authorized retained checkpoint.
  Full publication QC was not run and no new GitHub publication is claimed.
  Makarova supplement download challenges, the RSC 404, uninspected allele
  primers and later member literature remain explicit coverage limits.
  PF01977 is next by actual directory membership; all earlier follow-ups and
  the full 8,296-family objective remain active.

PF01976 publication audit (PR #211, 2026-10-15):

- The user authorized commit, PR, adversarial review, issue remediation, merge
  and branch cleanup. The PR contains the completed local PF01976 assessment;
  PF01977 research remains scratch work and is not adopted by this release.
- The publication blocker was reproduced locally and in initial CI run
  `38683378652`: the preceding source ledger rejects the changed PF01976 bytes.
  [Issue #212](https://github.com/CultureBotAI/DUFMech/issues/212) tracks native
  source capture, Pages regeneration and final release verification.
- Candidate commit `13b3b6b3058c22af38a792ecf6aafd436ea91dcd` is retained by
  annotated tag `source/dufmech-pr-211-candidate`. Native capture and canonical
  remote verification pass for all 9,126 source files. Prior tags are preserved.
- The adversarial same-agent recheck confirms the comparative redox scope,
  separate fusion-domain intervals and multi-mutant salt-strain confounding.
  The original Zhou2017 table image and the retained provider mappings were
  rechecked; no new causal edge or experimental construct identity is inferred.
  This is not independent expert approval or a completed family review.
- Scientific findings remain open as
  [#213](https://github.com/CultureBotAI/DUFMech/issues/213) (redox/member evidence),
  [#214](https://github.com/CultureBotAI/DUFMech/issues/214) (prenyl-domain
  attribution), and [#215](https://github.com/CultureBotAI/DUFMech/issues/215)
  (DVU3364 allele causality). The existing native discussions guard against
  unsupported claims; publishing them does not resolve the underlying science.
- The audit-bearing checkpoint must also be retained and captured before final
  full QC, exact-head CI, merge and deployed-page verification. Those outcomes
  are subsequent release gates, not claims made by this candidate audit.
  All 8,296 families and prior follow-ups remain in the scientific objective.

PF01977 AnFdc primary-evidence pass (2026-10-15, local):

- Base is merged PR #211, `9531391dd98c6ac48e6d0f9393659c7da2241b80`, in
  isolated branch `feat/duf-pf01977-causal-graphs`. Ignored/hidden-inclusive
  searches found no earlier PF01977 overlay or graph in the maintained curation,
  evidence, history and review paths. The frozen EX_DUF identity, historical
  DUF117/UPF0096 names and all imported fields are preserved.
- Added ten whole-AnFdc graphs with 26 experimentally supported edges: 14 direct
  biochemical/state transitions and 12 perturbation effects with unresolved
  molecular directness. They cover forward/reverse reactions, three terminal
  alkenes, six internal residue substitutions, styrene isotope exchange,
  solution light sensitivity, crystal photoisomerization, E282Q Int2 trapping,
  slow alkyne-adduct decarboxylation and two C-terminal-domain substitutions.
- `evidence/PF01977/member-mapping.txt` records A2QHE5 sequence 1/entry 95 and
  exact deposited 4ZA4/6R3F/6R30/6R2Z/6R33 sequence comparisons. PF01977 is
  119-318; R173/E277/E282 lie inside it, but F437/L439 are in PF20696 at
  324-460. Complete-protein activity never establishes isolated-domain
  sufficiency. Deposited designs do not certify every physical assay plasmid.
- `evidence/PF01977/anfdc-primary-assays.txt` retains minimal quotations,
  hashes, methods, original-figure locators and exclusions for Payne2015,
  Bailey2018 and Bailey2019. Original assay/structural figures and selected
  supplement pages were visually inspected. Low R173A/E277Q activity refines
  the earlier inactivity claim; detector/color-label discrepancies, negative
  assays, cofactor occupancy and apparent-rate limitations remain visible.
  Different mutants and alkyne/alkene substrates are not combined into one
  falsely observed atomistic trajectory.
- Saved partial scientific self-review:
  `reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml`
  and its derived Markdown. Verdict `pass_with_limitations`, native
  `NEEDS_FOLLOWUP`; three OPEN findings and discussions. PF01977 remains
  IN_PROGRESS, not REVIEWED. Semantic digest:
  `5aeae5af394c7337f1aaf9db47f46484bf775f085ac1c24854c302efcba97705`.
- Canonical CREATE and REVIEW events are
  `history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml` and
  `history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml`.
  Each preceded its guarded projection refresh. The initial unsaved review
  payload needed the dedicated bounded-search field; the corrected native save
  succeeded without rewriting any retained report.
- Final record reproduction validates all 8,296 records with zero drift and
  all 316 history events validate. All 8,296 manifest hashes match; only PF01977
  changes. Schema reproduction is current; 52 graph/QC tests and four
  review-contract tests pass. Final `just validate-all` passes, including all
  164 structured bundles and 172 native retained reports.
- Native inventory and export checks pass. Only PF01977's inventory row changes;
  totals are 801 graphs/1,706 edges across 127 families, 8,169 graphless,
  134 IN_PROGRESS and 8,162 SEEDED. These are structural/partial-assessment
  counts, not scientific completion. KGX/SSSOM change only PF01977's curation
  status; association edges, all other families, frozen sources, old reports,
  schemas and application code are preserved.
- Unpinned native preview passes at 1440px and 390px: all ten graphs, 26 edges,
  support/directness labels, evidence disclosures and three OPEN questions;
  no document overflow or JavaScript errors. Desktop evidence and mobile domain
  boundary screenshots were inspected. Temporary browser/server were closed.
- Canonical Pages and pins are unchanged. The actual pin check exits 1 for
  changed PF01977 bytes; full publication QC and a retained source checkpoint
  remain a separate authorized workflow. No commit, PR or deployment is claimed.
- Continue PF01977 member and mechanism coverage, especially individually
  mapped ScFdc and VdcCD contexts, then the remaining family queue. The VdcCD
  primary Results and cloning methods distinguish Bacillus subtilis and
  Sedimentibacter hydroxybenzoicus partner-addition/reconstitution experiments;
  exact constructs, Pfam mappings, original assay figures and supplements are
  still required before adoption. Other AnFdc experiments, EcUbiD, AroY, HmfF,
  HudA and later work remain open. All earlier findings and the full 8,296-family
  objective remain active.

PF01977 publication audit (PR #220, 2026-10-15):

- The user authorized commit, PR, adversarial review, issue remediation, merge
  and branch cleanup. This release contains the ten AnFdc graphs and 26 edges;
  the unfinished VdcCD research is not adopted.
- The source-pin failure for PF01977 was reproduced and is tracked in
  [#216](https://github.com/CultureBotAI/DUFMech/issues/216). Candidate commit
  `f2b12dd9f59d877f0869f185c281f887471e63be` is retained by annotated tag
  `source/dufmech-pr-220-candidate`. Native capture and fresh canonical remote
  verification pass for all 9,134 candidate source files.
- Same-agent adversarial review rechecked all 26 edge quotations against the
  primary XML, exact record/overlay correspondence, all 8,296 manifest hashes,
  and the original Bailey2018 light-response and isotope-exchange figures.
  The 52 focused graph/QC tests pass. This is not independent expert approval.
- Scientific follow-ups remain OPEN as
  [#217](https://github.com/CultureBotAI/DUFMech/issues/217) (member/partner scope),
  [#218](https://github.com/CultureBotAI/DUFMech/issues/218) (atomic transitions
  and domain attribution), and
  [#219](https://github.com/CultureBotAI/DUFMech/issues/219) (assay discrepancies,
  normalization and construct details). Existing discussions and the partial
  scientific review remain unchanged; PF01977 stays IN_PROGRESS.
- The audit-bearing source commit must also be retained, captured and rendered
  before final full QC, exact-head CI, merge and deployment verification.
  Those are subsequent release gates, not results asserted by this note.
  All other family records, old reviews/history and frozen sources are preserved.
- Verification encountered loss of the old temporary worktree's Git pointer
  and tracked test files; its isolated OAK check failed with a missing-file
  error. The cause was not established. The published candidate was recovered
  into a fresh locked worktree, local docs/pins preserved byte-for-byte, and
  responsive checks repeated. Locked dependencies and the separate pinned
  CLAW runtime were rebuilt with a fresh cache after missing cache metadata.
  Final full QC must run in this recovered checkout; the failed attempt is
  not counted as a pass.

PF01977 VdcCD evidence extension (2026-10-15, local):

- Continued from merged PR #220, base
  `ffec8fdaebbdbae9b06702fb065eb0abd0db9f50`, in an isolated worktree.
  Baseline `just records-check` validated 8,296 records with zero drift.
  All ten AnFdc graphs and their evidence remain unchanged.
- Added thirteen VdcCD graphs with 34 edges: 30 experimentally observed
  effects, three computational hypotheses and one contextual hypothesis.
  PF01977 now has 23 graphs and 60 edges: 32 DIRECT/OBSERVED/EXPERIMENTAL,
  24 UNRESOLVED/OBSERVED/EXPERIMENTAL and four UNRESOLVED/HYPOTHESIZED.
  Eleven graphs are MECHANISTIC, ten PHENOTYPIC and two HYPOTHETICAL.
- The new `evidence/PF01977/vdcc-primary-assays.txt` retains minimal licensed
  quotations, source hashes, exact locators, assay conditions and limitations
  from Marshall2021, PMID:34417452. Primary XML, original Figures 2-5,
  supplement Figures 2-5/tables, all five source-data sheets and the archived
  docking-model inventory/provenance were inspected. Supplementary movies,
  raw structural refinement and physical plasmids were not assessed.
- Q9S4M7 sequence 1 has PF01977 at 106-312. All three deposited ShVdcC
  bodies agree; ShVdcD Q4R102 is the separate PF26358 partner. The 7AE7
  V59X partner equals Q4R102 residues 1-58. L182 lies inside PF01977;
  the T325/S326 hinge and L425 are outside it. Whole-enzyme activity is not
  isolated-domain sufficiency. P94405/C0H3U9 are explicitly reference mappings
  for the published Bs constructs, not proof of full synthetic-insert or
  strain 168 identity. C0SPB5 yclD is not substituted for small BsdD.
- Substrate-specific products, cognate partner addition, noncognate mixtures,
  D:C ratio, air exposure/cofactor rescue, viscosogens and two variant contexts
  remain separate experiments. Low C-alone vanillate activity, a nonzero
  BsCD gallic replicate, loss of low ShCD gallic activity after tail deletion,
  WT syringate negatives and text-only L182V data are retained. Rescue is
  partial, not complete; apparent turnover depends on cofactor assumptions.
- Domain closure/Int2 strain/quinoid turnover and partner-loop stabilization
  are visibly labeled hypotheses. Apo conformations, docking energies and
  viscosity effects do not establish the proposed atomic sequence. Sequence
  R168/G178 conflicts with main-figure R178 and supplement-image R138 labels;
  these source discrepancies are not silently corrected into new biology.
- The partial same-agent scientific successor review is
  `reviews/structured/20261015T083743Z-pf01977-vdcc-causal-evidence/review.yaml`
  and its derived Markdown. Verdict is `pass_with_limitations` /
  `NEEDS_FOLLOWUP`; all three earlier issue keys/targets are retained through
  exact `previous_occurrences`. Issues #217, #218 and #219 remain open.
  PF01977 stays IN_PROGRESS; no old review is reused as approval.
- Canonical EDIT and REVIEW events are
  `history/records/PF01977/2026-10-15T081608Z-codex-a85dbd.yaml` and
  `history/records/PF01977/2026-10-15T083743Z-codex-b0918e.yaml`.
  Semantic digest:
  `d89063df2e8726ac5fc1bab28a2c9aa557f2e10d263ca43831b24c0b3cb72a94`.
- The 52 focused graph/QC tests pass; schema reproduction has zero drift.
  All 8,296 manifest hashes and 60 cache/primary-XML quotations were checked.
  Only PF01977's inventory row changes: 814 graphs/1,740 edges across 127
  graph-bearing families, 8,169 graphless. KGX/SSSOM exports remain current
  and unchanged. These are structural counts, not scientific completion.
- A native unpinned PF01977 preview passes at 1440px and 390px: all graphs,
  edge support labels, evidence disclosures and three OPEN discussions remain
  accessible, without document overflow or JavaScript errors. Mobile
  hypothesis/construct and desktop partial-rescue screenshots were visually
  inspected; native horizontal table scrolling is retained. Browser/server
  were closed. This is not a corpus-wide browser sweep or canonical release.
- Source-pin verification honestly fails for the changed overlay. No source
  checkpoint, canonical Pages, full release QC or publication is performed in
  this continuation. Existing snapshots, other records, old reviews/history,
  source pins and canonical Pages are preserved. Final history-index preview
  and apply changed only PF01977 and its manifest. `just validate-all
  validate-schema` passes: 8,296 records with zero drift, 319 canonical
  history files, four review-contract tests, 166 structured bundles, 174
  native reports and zero schema differences. The final integrity check
  confirms the saved review digest still matches after history indexing;
  `just causal-graphs --check` verifies all 8,296 inventory rows.
- Continue ScFdc, EcUbiD, AroY, HmfF, HudA and later specificity/maturation
  work, together with unresolved VdcCD constructs, raw L182V data, active
  occupancy and causal domain-motion evidence. Earlier family findings and
  the full 8,296-family objective remain active.
