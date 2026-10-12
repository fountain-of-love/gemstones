# Gemstone Page Specification

This file defines the Markdown structure to use when creating one file per gemstone from the Semoea gemstone pages.

Source pattern: [Semoea - Edelstenen](https://www.semoea.nl/edelstenen)

## File Naming

Use one Markdown file per gemstone.

Recommended filename:

```text
gemstones/<english-slug>.md
```

Where `<english-slug>` follows the English gemstone name in lowercase kebab-case. Keep `gemstone-index-nl.md` and Semoea source URLs in Dutch; only the local gemstone page filename is translated.

```text
gemstones/amethyst.md
gemstones/moonstone.md
gemstones/rock-crystal.md
```

## Page Contract

Each gemstone file should preserve the Semoea content while presenting it in a more human-friendly progression:

1. Metadata
2. Main title
3. Overview: natural description plus selective one-line essence links
4. Table of contents
5. Lead image
6. Key identity
7. Composition
8. Appearance
9. Geology and occurrence
10. Varieties, trade names, and lookalikes
11. Name origin
12. History and cultural use
13. Energetic and therapeutic traditions
14. Runes and symbolic associations
15. Zodiac signs
16. Did you know
17. Images
18. Sources
19. Validation notes

If a source page omits a section, keep the heading and write `Not listed on source page.` so the files stay comparable.

This structure intentionally separates three reading modes:

- Narrative understanding vs structured knowledge
- Navigation towards content elements vs navigation towards linked insights such as `[[Feldspar]]`
- Overall insight vs in-depth knowledge

## Dictionary Interface

Structured field labels should link to [gemstone-dictionary.md](/Users/yveslangeraert/Documents/Edelstenen/gemstone-dictionary.md) using heading links. Treat the dictionary as the stable interface layer for reusable structured concepts.

Examples:

- `[[dictionary#Mineral Group / Family|Mineral group / family]]`
- `[[dictionary#Chemical Class|Chemical class]]`
- `[[dictionary#Color|Color]]`
- `[[dictionary#Ideal Mineral Formula|Ideal mineral formula]]`

This lets the gemstone pages stay stable even if later we split concepts such as chemical class, color, crystal system, or mineral group into dedicated notes. The dictionary can then link onward to those deeper notes.

## Markdown Template

```markdown
---
name_nl: ""
name_en: ""
source_url: ""
source_site: "Semoea Helende Edelstenen"
menu_range: "A-L or M-Z"
language: "en"
last_checked: "YYYY-MM-DD"
therapeutic_concepts:
  emotional: []
  mental: []
  physical: []
---

# {English gemstone name}: Characteristics and Effects

## Overview

Write the natural opening description here. This is where the source page's introductory description belongs, translated or rewritten faithfully without losing detail. The overview should feel like a human introduction to the stone, not a generated checklist.

After the descriptive opening, add a few one-line essence links where they help orientation. Vary the wording and number of lines per gemstone. Do not force every section to appear here, and do not repeat facts that are already obvious from the description.

Example patterns:

- For scientific readers, the [[#Composition|composition]] is the key detail: ...
- Visually, the [[#Appearance|appearance]] is easiest to recognize by ...
- In the wider mineral graph, this stone connects to [[Feldspar]], [[Microcline]], and [[Moonstone]].
- Historically, the [[#History And Cultural Use|history and cultural use]] centers on ...
- The [[#Energetic And Therapeutic Traditions|therapeutic tradition]] mainly focuses on ...

Keep this section natural. Prefer 2-5 paragraphs and 2-5 essence links, adjusted to the stone.

## Table Of Contents

- [[#Overview]]
- [[#Lead Image]]
- [[#Key Identity]]
- [[#Composition]]
- [[#Appearance]]
- [[#Geology And Occurrence]]
- [[#Varieties Trade Names And Lookalikes]]
- [[#Name Origin]]
- [[#History And Cultural Use]]
- [[#Energetic And Therapeutic Traditions]]
- [[#Runes And Symbolic Associations]]
- [[#Zodiac Signs]]
- [[#Did You Know]]
- [[#Images]]
- [[#Sources]]
- [[#Validation Notes]]

## Lead Image

| [[dictionary#Field\|Field]] | [[dictionary#Value\|Value]] |
|---|---|
| [[dictionary#Image URL\|Image URL]] |  |
| [[dictionary#Alt Text\|Alt text]] |  |
| [[dictionary#Caption\|Caption]] |  |

## Key Identity

| [[dictionary#Field\|Field]] | [[dictionary#Value\|Value]] |
|---|---|
| [[dictionary#Dutch Name\|Dutch name]] | {Dutch gemstone name} |
| [[dictionary#English Name\|English name]] | {English gemstone name} |
| [[dictionary#Scientific Name / Mineral Species\|Scientific name / mineral species]] |  |
| [[dictionary#Gemstone Variety Of\|Gemstone variety of]] |  |
| [[dictionary#Mineral Group / Family\|Mineral group / family]] |  |
| [[dictionary#Chemical Class\|Chemical class]] |  |
| [[dictionary#Related Stones\|Related stones]] |  |
| [[dictionary#Primary Source\|Primary source]] | [Semoea page]({source_url}) |

Use Obsidian links for reusable concepts, for example `[[Quartz]]`, `[[Feldspar]]`, `[[Microcline]]`, `[[Moonstone]]`, or `[[Lead]]`.

## Composition

This is the priority scientific section. It captures the scientific naming and composition details. Treat it as a required table because Semoea's chemical notation is a key quality signal.

| [[dictionary#Field\|Field]] | [[dictionary#Value\|Value]] |
|---|---|
| [[dictionary#Source Notation\|Source notation]] |  |
| [[dictionary#Normalized Markdown Notation\|Normalized Markdown notation]] |  |
| [[dictionary#Ideal Mineral Formula\|Ideal mineral formula]] |  |
| [[dictionary#Scientific Name / Mineral Species\|Scientific name / mineral species]] |  |
| [[dictionary#Mineral Group / Family\|Mineral group / family]] |  |
| [[dictionary#Chemical Class\|Chemical class]] |  |
| [[dictionary#Formula Notes\|Formula notes]] |  |
| [[dictionary#Trace Elements / Substitutions\|Trace elements / substitutions]] |  |
| [[dictionary#Inclusions\|Inclusions]] |  |
| [[dictionary#Color-Causing Elements\|Color-causing elements]] |  |
| [[dictionary#External Validation\|External validation]] |  |

Use HTML subscripts in Markdown formulas where needed, for example `SiO<sub>2</sub>` or `(Na,K)AlSi<sub>3</sub>O<sub>8</sub>`. Preserve parentheses, commas, charges, hydration dots, and trace-element additions as closely as possible.

Use Obsidian links for meaningful scientific relationships:

- formula species: `[[Quartz]]`, `[[Microcline]]`, `[[Malachite]]`
- mineral groups: `[[Feldspar]]`, `[[Silica]]`, `[[Carbonate]]`
- elements: `[[Iron]]`, `[[Copper]]`, `[[Lead]]`, `[[Titanium]]`
- related stones: `[[Amethyst]]`, `[[Rock Crystal]]`, `[[Moonstone]]`

## Appearance

| [[dictionary#Property\|Property]] | [[dictionary#Value\|Value]] |
|---|---|
| [[dictionary#Color\|Color]] |  |
| [[dictionary#Luster\|Luster]] |  |
| [[dictionary#Transparency\|Transparency]] |  |
| [[dictionary#Hardness\|Hardness]] |  |
| [[dictionary#Density\|Density]] |  |
| [[dictionary#Crystal System\|Crystal system]] |  |
| [[dictionary#Cleavage\|Cleavage]] |  |
| [[dictionary#Fracture\|Fracture]] |  |
| [[dictionary#Habit / Growth Form\|Habit / growth form]] |  |
| [[dictionary#Distinctive Visual Markers\|Distinctive visual markers]] |  |

## Geology And Occurrence

Use prose first. Explain how the stone forms, where it is found, and what geological context matters.

| [[dictionary#Topic\|Topic]] | [[dictionary#Details\|Details]] |
|---|---|
| [[dictionary#Formation Environment\|Formation environment]] |  |
| [[dictionary#Common Host Rocks\|Common host rocks]] |  |
| [[dictionary#Notable Locations\|Notable locations]] |  |
| [[dictionary#Mining / Source Notes\|Mining / source notes]] |  |

## Varieties Trade Names And Lookalikes

Use prose first when the relationships need explanation.

| [[dictionary#Name\|Name]] | [[dictionary#Relationship\|Relationship]] | [[dictionary#Notes\|Notes]] |
|---|---|---|
|  | Variety / trade name / lookalike / related stone |  |

## Name Origin

Use prose first when the naming story matters.

| [[dictionary#Name Or Term\|Name or term]] | [[dictionary#Origin / Meaning\|Origin / meaning]] |
|---|---|
|  |  |

## History And Cultural Use

Use narrative prose here. This is where historical, cultural, artistic, religious, trade, pigment, jewelry, or symbolic material can breathe.

## Energetic And Therapeutic Traditions

Therapeutic claims are source-attributed and not medical advice.

### Overview

Describe the complete overall energetic / therapeutic framing from the source page. This may be several paragraphs when the source gives multiple themes. Do not reduce a detailed page to one broad sentence.

### Spiritual

Transfer every distinct source claim, chakra association, energetic action, symbolic association, and usage detail. Keep the source tradition explicit.

### Mental

Transfer every distinct source claim about thought, attention, confidence, learning, behavior, or decision-making.

### Emotional

Transfer every distinct source claim about feelings, stress, fear, grief, relationships, or emotional processing.

### Physical

Transfer every distinct source claim about body systems, symptoms, conditions, materials, preparation, placement, dosage, and use. Preserve source instructions and warnings with clear attribution.

Link explicit recurring concepts to canonical notes under `concepts/emotional/`, `concepts/mental/`, or `concepts/physical/`. Keep the full source-attributed sentence or bullet; the link is an index, not a replacement for the prose.

### Source-Therapy Details

Use this subsection when the source includes oils, elixirs, crystal water, cleansing, charging, dosage, placement, contraindications, or other operational details that do not fit cleanly into Spiritual, Mental, Emotional, or Physical. Write `Not listed on source page.` when absent.

Concept links in this section are indexes only. Each linked concept note must provide a reciprocal `## Related Gemstones` section for human navigation.

## Runes And Symbolic Associations

This section maps to `Runen`, `Runen bij {gemstone}`, or equivalent.

| [[dictionary#Field\|Field]] | [[dictionary#Value\|Value]] |
|---|---|
| [[dictionary#Rune Name\|Rune name]] |  |
| [[dictionary#Rune Symbol / Image\|Rune symbol/image]] |  |
| [[dictionary#Meaning\|Meaning]] |  |
| [[dictionary#Relation To Gemstone\|Relation to gemstone]] |  |

## Zodiac Signs

This section maps to `Sterrenbeelden`.

| [[dictionary#Zodiac Sign\|Zodiac sign]] | [[dictionary#Notes\|Notes]] |
|---|---|
|  |  |

## Did You Know

This section maps to `Wist je dat...`.

- 

## Images

Record article images so media can be audited or reused later.

| [[dictionary#Image URL\|Image URL]] | [[dictionary#Alt Text\|Alt text]] | [[dictionary#Title\|Title]] | [[dictionary#Caption\|Caption]] | [[dictionary#Section\|Section]] |
|---|---|---|---|---|
|  |  |  |  |  |

## Sources

| [[dictionary#Source\|Source]] | [[dictionary#URL\|URL]] | [[dictionary#Role\|Role]] |
|---|---|---|
| Semoea | {source_url} | Primary source |
|  |  | Scientific validation |
|  |  | Scientific validation |

## Validation Notes

| Check | Result |
|---|---|
| Semoea structure preserved |  |
| Empty fields preserved |  |
| Composition source notation preserved exactly |  |
| Composition externally validated |  |
| At least two external sources added |  |
| Therapeutic claims attributed |  |
| Therapeutic coverage complete against source |  |
| Therapeutic instructions and warnings preserved |  |
| Source-specific context coverage complete |  |
| Source disclaimers and responsibility statements preserved |  |
| Therapeutic concepts source-mapped |  |
| Therapeutic concept candidates reconciled |  |
| Body uses observational voice |  |
| Content not compressed into high-level summary |  |

## Source Notes

Record the source-access mode, source-specific omissions or uncertainty, and whether the source's responsibility/disclaimer language was preserved. Source-specific historical, symbolic, trade, and “Did You Know” material must be traceable here or in the relevant page section.

- Content is based on the linked Semoea page.
- Keep copied wording minimal; use summaries unless a short direct quote is explicitly needed.
- Preserve external links exactly as listed on the source page.
- Do not present gemstone therapy information as medical advice.
- Preserve the source page's therapeutic coverage claim by claim; do not compress detailed source lists into a general summary.
```

## Extraction Rules

Use the smallest stable structure that matches the source page.

| Semoea HTML / heading | Markdown target |
|---|---|
| `<h1>{Gemstone}: kenmerken en werking</h1>` | `# {English gemstone name}: Characteristics and Effects` |
| `Eigenschappen` / `Eigenschappen {gemstone}` | `## Composition`, `## Appearance`, and `## Key Identity` |
| `Samenstelling` inside `Eigenschappen` | `## Composition` |
| Introductory paragraphs before `Herkomst van de naam` | `## Overview`; only move non-introductory hard facts to deeper structured sections when needed |
| `Herkomst van de naam` | `## Name Origin` |
| `{Gemstone} door de eeuwen heen` | `## History And Cultural Use` |
| `{Gemstone} voor je gezondheid` / `{Gemstone} en gezondheid` | `## Energetic And Therapeutic Traditions` |
| `Spiritueel` | `### Spiritual` |
| `Mentaal` | `### Mental` |
| `Emotioneel` | `### Emotional` |
| `Fysiek` | `### Physical` |
| `Runen` / `Runen bij {gemstone}` | `## Runes And Symbolic Associations` |
| `Sterrenbeelden` | `## Zodiac Signs` |
| `Fysische eigenschappen {gemstone}` | `## Appearance`, `## Composition`, `## Geology And Occurrence`, and `## Varieties Trade Names And Lookalikes` |
| `Weblinks` / `Webtips` | `## Sources` |
| `Wist je dat...` | `## Did You Know` |

## Quality Rules

- Keep files consistent even when individual pages vary slightly.
- Keep Dutch source names and URLs in metadata.
- Use English section names in generated gemstone files.
- Preserve factual mineral properties as close to the source as possible.
- Preserve Semoea's chemical composition notation exactly in `Chemical composition, source notation`.
- Add a normalized Markdown formula using `<sub>` tags for scientific readability.
- Capture the scientific name or mineral species separately from the commercial or Dutch gemstone name.
- Write in an observational voice about the stone itself. Credit Semoea as the primary source in `## Source` and `## Source Notes`, but avoid repetitive phrases such as `Semoea notes`, `Semoea says`, or `Semoea describes` throughout the body.
- Convert long Semoea prose into faithful, detailed coverage without reproducing it verbatim.
- Put the source page's introductory description in `## Overview`, not in a separate description section.
- Avoid mechanical repetition in `## Overview`; vary sentence structure, number of essence links, and emphasis per gemstone.
- Avoid unnecessary overlap: if a detail is fully explained in `## Overview`, use the later structured section for normalized facts, validation, and deeper evidence rather than repeating the same prose.
- Use `Not listed on source page.` for missing sections or fields.
- Keep link text human-readable, never raw URLs unless the URL itself is the relevant label.
- Add source dates using the day the page was checked.
- Keep medical and therapeutic claims attributed to the source and avoid turning them into advice.

## Refactoring Check For Generated Files

After creating gemstone files, review whether the structure is still serving the content:

- If many files repeat empty fields, consider moving those fields to an optional block.
- If a section gathers too many unrelated facts, split it using the existing Semoea subheadings first.
- If source page variations become common, update this spec instead of adding one-off formats.
- If translation choices drift, create a shared glossary for gemstone names and recurring terms.
