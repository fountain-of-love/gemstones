# Gemstones

This repository is a structured gemstone knowledge base built from the Semoea gemstone catalog, then enriched with scientific validation sources and Obsidian-friendly graph links.

The work started as a simple menu extraction from [Semoea - Edelstenen](https://www.semoea.nl/edelstenen): a complete A-L and M-Z list of stones with clickable source links. It has since grown into a repeatable content system for creating one Markdown file per gemstone, preserving the source structure while making each page easier to read, navigate, validate, and extend.

## Intention

The purpose is to have a limited playing ground to experiment with best practices of knowledge engineering. To create a full ontology for dual-usage, where both humans and technology can amplify each other. The project balances therefore three reading modes:

- Human orientation: every gemstone starts with a readable overview and table of contents.
- Structured comparison: recurring tables make identity, composition, appearance, geology, sources, and validation comparable across stones.
- Graph knowledge: Obsidian links connect minerals, elements, related stones, places, traditions, and dictionary concepts.

Note that the content of gemstones is gradually and slowly growing due to the economic cost of token burn and this a considered an experiment. We recognise the value of this knowledge, at the moment we just don't prioritise spending more tokens and energy to it.

## Most Important Lessons Learned

The main lesson is that the dictionary/ontology should act as an interface, not as an attempt to absorb every surrounding domain. Gemstones naturally touch chemistry, geology, history, symbolism, spirituality, health traditions, language, and commerce; without a boundary, the knowledge graph would immediately try to become all of those things at once.

The dictionary solves this by defining shared concepts in one sentence, just enough for this repository to use them consistently. A concept such as chemical class, mineral group, chakra, zodiac sign, source notation, or validation does not need to become a full chemistry textbook or spiritual encyclopedia inside this repo.

Later, the dictionary can become a portal layer. Each concept can point outward or onward to deeper knowledge sources that handle that topic in its proper context, such as scientific chemistry, mineralogy, cultural history, or therapeutic traditions. That keeps the gemstone domain clear while still allowing the graph to connect across knowledge repositories.

This boundary makes the Obsidian graph more useful: the gemstone notes can link through stable concepts without pulling in the full depth of every connected world.

Supporting lessons:

- Define interfaces before depth: a clear one-sentence concept is often more valuable early on than a sprawling expert article.
- Keep domain boundaries visible: this repository is about gemstones, while chemistry, spirituality, history, and medicine remain connected but separate knowledge domains.
- Let links carry expansion: a graph link can preserve future depth without forcing that depth into the current note.
- Prefer portals over duplication: when another knowledge source owns a topic better, the dictionary should point to it instead of recreating it poorly.
- Make structure serve navigation: shared vocabulary lets humans and AI move through the same graph without flattening nuance.

## Playground

The tensions in this repository that are intentionally played with:

- **Human-readable vs AI-readable**: pages should feel natural to read while still exposing predictable fields, links, and validation signals for tooling.
- **Structured vs non-structured data**: tables carry stable facts, while prose preserves nuance, context, and the living texture of each stone.
- **Easy entrance vs expert deep dive**: each note starts gently, then opens toward scientific composition, source comparison, and specialist detail.
- **Source fidelity vs original voice**: Semoea's structure and facts are preserved without copying long prose or making the source the subject of every sentence.
- **Primary tradition vs external validation**: therapeutic and cultural material keeps its source context, while scientific claims are cross-checked against mineralogical references.
- **Local note vs knowledge graph**: every gemstone must stand alone, but Obsidian links should let the collection become more than a folder of isolated pages.
- **Consistency vs stone-specific character**: the shared template makes comparison possible, while each overview can breathe according to the stone's own story.
- **Empty fields vs false completeness**: missing data stays visible so absence is honest instead of quietly hidden.
- **Scientific precision vs accessible language**: formulas and mineral names stay exact, but the surrounding explanation should remain approachable.

These tensions could come together as a scientific field of knowledge composition. Each gemstone page reflects the same composition as in it separates general identity formulas, source notation, mineral species, trace elements, inclusions, and external validation so they do not get buried in a generic properties table.

## Source And Validation Model

Semoea is treated as the primary source for the original gemstone page structure, Dutch naming, therapeutic tradition, imagery, and source-page content. The repository does not aim to copy long Semoea prose verbatim. Instead, it preserves factual coverage, section coverage, images, links, and scientific notation while rewriting in original wording.

“Factual coverage” includes source-specific historical, symbolic, naming, trade, cultural, and `Did You Know` details, as well as therapeutic claims, practical instructions, warnings, and the source's own responsibility/disclaimer language. These are checked against a raw source-coverage inventory before a page is considered complete.

Each gemstone file should add at least two high-quality external sources, preferably from mineralogical, gemological, museum, university, or scientific references such as Mindat, Webmineral, GIA, RRUFF, Handbook of Mineralogy, museums, or peer-reviewed sources.

Therapeutic and energetic claims remain source-attributed and are not presented as medical advice.

## What This Repository Contains

| File or folder | Purpose |
|---|---|
| `gemstone-index-nl.md` | Dutch gemstone catalog from the Semoea menu, grouped by A-L and M-Z. This remains untranslated as the source worklist. |
| `gemstone-spec.md` | The reusable gemstone page contract and Markdown template. |
| `gemstone-process.md` | The step-by-step workflow for creating each gemstone file. |
| `gemstone-dictionary.md` | Shared vocabulary for recurring table fields, concepts, validation terms, and Obsidian links. |
| `gemstone-proof-run-5.md` | Audit trail for the first five gemstone files created with the process. |
| `gemstone-expansion-plan.md` | Batch protocol, quality floor, diversity plan, metrics, and audit template for expansion. |
| `gemstone-expansion-batch-1-audit.md` | Audit of the first diversity batch, including source-access limitations and process decisions. |
| `therapeutic-concept-model.md` | Controlled mental, emotional, and physical concept model for graph navigation and filtering. |
| `therapeutic-concept-coverage-audit.md` | Candidate register and reconciliation status for concept extraction across existing gemstone pages. |
| `concept-coverage/` | Sentence-level evidence registers and the reusable register template for therapeutic concept extraction. |
| `gemstones/` | The gemstone note collection. Currently contains the five proof-run gemstones. |
| `concepts/` | Canonical graph nodes for source-attributed therapeutic concepts. |
| `scripts/validate_therapeutic_concepts.py` | Structural validator for frontmatter edges, canonical notes, reciprocal links, and register completion. |
| `skills/` | Local reusable skills for defining specs, making processes, and writing structured content. |

## Current Gemstone Files

The first proof run created five complete gemstone notes, and Batch 1 adds five diversity-test notes:

| Gemstone | File | Scientific focus |
|---|---|---|
| Amethyst | `gemstones/amethyst.md` | Quartz variety, SiO<sub>2</sub>, trace elements and color centers. |
| Amazonite | `gemstones/amazonite.md` | Microcline / alkali feldspar, KAlSi<sub>3</sub>O<sub>8</sub>, lead-related color discussion. |
| Rock crystal | `gemstones/rock-crystal.md` | Colorless quartz, SiO<sub>2</sub>. |
| Moonstone | `gemstones/moonstone.md` | Feldspar gemstone, orthoclase/adularia and albite layering caveats. |
| Malachite | `gemstones/malachite.md` | Copper carbonate hydroxide, Cu<sub>2</sub>(CO<sub>3</sub>)(OH)<sub>2</sub>. |

Batch 1:

| Gemstone | File | Scientific focus |
|---|---|---|
| Amber | `gemstones/amber.md` | Organic fossil resin rather than a mineral species. |
| Diamond | `gemstones/diamond.md` | Native carbon and trace-element color. |
| Lapis lazuli | `gemstones/lapis-lazuli.md` | Mixed lazurite-bearing rock. |
| Obsidian | `gemstones/obsidian.md` | Amorphous volcanic glass. |
| Turquoise | `gemstones/turquoise.md` | Hydrated copper-aluminium phosphate and treatment caveats. |

Each note keeps the hard structure from the spec, but the writing style is observational about the stone rather than repeatedly phrased around the source.

## How To Add The Next Gemstone

Use this order, following the controlled batch protocol in [gemstone-expansion-plan.md](/Users/yveslangeraert/Documents/Edelstenen/gemstone-expansion-plan.md):

1. Pick the next stone from `gemstone-index-nl.md`.
2. Read `gemstone-spec.md`.
3. Read `gemstone-process.md`.
4. Use one or two completed files in `gemstones/` as examples.
5. Visit the source page and capture the full article body in source order.
6. Extract composition with special care, preserving Semoea's notation exactly.
7. Create `gemstones/<english-slug>.md` from the spec.
8. Preserve empty required fields as explicit empty fields or `Not listed on source page.`
9. Add at least two external scientific validation sources.
10. Compare the finished page against the raw source-coverage inventory, including historical, symbolic, trade, `Did You Know`, instruction, warning, and disclaimer content.
11. Extract explicit mental, emotional, and physical concepts into the controlled graph vocabulary.
12. Create the sentence-level therapeutic coverage register before declaring concept extraction complete.
13. Run the therapeutic graph validator and the process checklist, with a final composition validation pass.

Create new pages in batches of three to five. Complete the per-page checklist, then perform a cross-page batch audit before changing the specification or starting the next batch. Do not trade away source access, composition validation, or omission checks for throughput.

## Obsidian Notes

This repository is intended to work well as an Obsidian vault. The gemstone pages use `[[...]]` links for reusable scientific and contextual concepts, while structured table labels link back to `gemstone-dictionary.md`.

That gives the collection a stable interface: gemstone files can keep using the same field labels while dictionary entries later grow into deeper notes, maps, or dedicated concept pages.

## Project Principles

The repository is intentionally modular and incremental:

- One source catalog.
- One reusable page specification.
- One repeatable creation process.
- One dictionary interface.
- One Markdown file per gemstone.
- One sentence-level coverage register per gemstone with therapeutic concept extraction.
- One repeatable structural validator for the graph contract.

This keeps the system simple enough to grow stone by stone, while still supporting scientific precision, source traceability, validation, and graph-based exploration.
