# Data Sources For Domains And Proteins Of Unknown Function

**Date:** 2026-09-30

## Verdict

Use InterPro/Pfam as the first DUF family catalog, keyed by Pfam accession.
Pfam is queried through the InterPro API and already exposes the pieces needed
for DUF discovery: Pfam entry metadata, integrated InterPro entries, member
signatures, protein members, matched structures, domain architectures,
taxonomic counters, and AlphaFold model counters.

There is no equivalent canonical catalog for proteins of unknown function.
Build that set as a release-specific predicate over complete or metagenomic
protein universes: sequences from UniProtKB Reference Proteomes, representative
MGYP clusters from MGnify Proteins, and, where permanence matters, UniParc
sequence identities.

The first-pass ingestion should:

1. Search Pfam entries in InterPro for DUF-like families.
2. Normalize to `PFxxxxx`, attach any integrated `IPRxxxxxx` parent, and keep
   InterPro/Pfam descriptions as metadata rather than evidence-backed facts.
3. Pull UniProtKB members and collapse redundancy with UniRef clusters.
4. Pull MGnify cluster representatives for the same Pfam accessions to recover
   environmental proteins and biome context.
5. Join PDB, PDBe-KB, 3D-Beacons, AlphaFold DB, CATH-Gene3D, CDD, STRING,
   eggNOG, EFI-GNT, JGI IMG, Rhea, and QuickGO as evidence layers.
6. Score the family or protein as still unknown, partially characterized, or
   known but historically named DUF instead of assuming that a DUF short name
   still means no function is known.

## Source Classes

| Source | DUF/PUF contribution | Join keys | Caveat |
|---|---|---|---|
| InterPro / Pfam | Primary DUF family registry, entry descriptions, InterPro integration, protein and structure counters | `PFxxxxx`, `IPRxxxxxx`, UniProt accession, PDB ID | DUF names are historical and string search is over-inclusive |
| UniProtKB, Proteomes, UniRef | Protein universe for organisms with sequenced genomes | UniProt accession, proteome ID, taxon, UniRef cluster | TrEMBL entries are not all unknown, and low annotation score is not evidence of unknown function |
| UniParc | Permanent sequence identity for removed or non-reference proteins | `UPI`, checksum, cross-references | Sequence archive only; functional context must be rejoined |
| MGnify Proteins | Environmental cluster representatives, biome occurrence, Pfam hits, assembly and contig provenance | `MGYP`, Pfam accession, biome ID, study/assembly/contig accession | Detailed records exist only for cluster representatives |
| AlphaFold DB | Predicted monomer models and confidence metadata | UniProt accession, AlphaFold model URL | Low-confidence or disordered regions can create false fold analogies |
| PDB, RCSB, PDBe-KB, 3D-Beacons | Experimental structures, ligands, assemblies, and residue annotations | PDB ID, polymer entity, UniProt accession, residue number | A solved structure often covers one domain boundary |
| CATH-Gene3D | Domain superfamily and FunFam placement | Gene3D/CATH IDs, UniProt accession, PDB domain | Homologous superfamily membership can be broader than one biochemical function |
| NCBI CDD and NCBIFAM | Independent PSSM/HMM assignments and curated families | CDD accession, NCBIFAM accession, query protein | Specific hits are high-confidence; superfamily hits are remote context |
| STRING and eggNOG | Functional association networks and orthology clusters | STRING protein ID, taxon, eggNOG/COG | STRING edges include indirect associations |
| EFI-GNT and JGI IMG | Genome-neighborhood evidence and context profiles | UniProt/UniRef/NCBI IDs, Pfam, InterPro, contig/genome | Powerful for hypothesis generation, less convenient for bulk API ingest |
| Rhea, GO, QuickGO | Reaction, molecular-function, and GOA evidence | `RHEA:nnnnn`, `GO:nnnnnnn`, EC, UniProt accession, ECO evidence | Mostly validation and known-function filters |

## Unknown-Function Predicate

The unknown-function predicate should stay explicit and auditable.

| Signal | Suggested interpretation |
|---|---|
| Product names like "uncharacterized protein" or "protein of unknown function" | Weak positive seed |
| DUF Pfam or InterPro hit | Strong family seed, weak proof of ignorance |
| No experimentally supported GO molecular function | Weak positive, because absence of evidence is common |
| No Rhea, EC, catalytic-activity comment, or curated Swiss-Prot function | Stronger positive |
| Specific CDD/NCBIFAM, Rhea/EC, or experimental GOA hit | Demote to partially characterized or known |
| Reference Proteome membership and full-length ORF | Promote over fragments and singletons |
| UniRef cluster size and taxonomic span | Prioritize families with breadth |

## First Worklist

The `duf-puf-worklist` command fetches `entry/pfam` rows from the InterPro API
with `search=DUF` and these extra fields:

```text
entry_id,short_name,description,counters
```

It normalizes rows to one `PFxxxxx` record, classifies broad-text false
positives, and preserves historically named DUFs whose current descriptions no
longer say the function is unknown.
