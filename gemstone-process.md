# Gemstone File Creation Process

This process is repeated once per gemstone. Its purpose is to create a Markdown file that follows [gemstone-spec.md](/Users/yveslangeraert/Documents/Edelstenen/gemstone-spec.md), preserves the Semoea page content faithfully, and enriches it with high-quality scientific sources.

## Goal

For each gemstone, create:

```text
gemstones/<english-slug>.md
```

Use an English local filename for the gemstone page, while keeping the Dutch Semoea source URL, Dutch source name, and Dutch `gemstone-index-nl.md` worklist unchanged. The output must preserve Semoea's content structure and keep every spec section present, including empty or missing fields.

`Not summarised` means no sections, facts, links, images, list items, scientific fields, or source distinctions are omitted. It does not mean copying the full Semoea article prose verbatim. Long prose should be converted into faithful, detailed Markdown coverage in original wording, with Semoea clearly credited as the primary source.

## Process

### 1. Select The Gemstone

Use [gemstone-index-nl.md](/Users/yveslangeraert/Documents/Edelstenen/gemstone-index-nl.md) as the Dutch source worklist.

Record:

| Field | Value |
|---|---|
| Dutch name |  |
| English name |  |
| Source URL |  |
| Menu range | A-L or M-Z |
| Target file | `gemstones/<english-slug>.md` |

### 2. Visit The Semoea Page

Open the gemstone's source URL and read the article body, not only the visible menu entry.

Primary DOM area to extract:

| DOM target | Purpose |
|---|---|
| `.com-content-article.item-page` | Main Joomla article wrapper |
| `.astroid-article-text` | Main article content |
| `h1` | Page title |
| `.eigens` | Lead image and properties block, when present |
| `.vooreigens` | Opening descriptive text, when present |
| `h2` headings | Major content sections |
| `h3` headings | Health subsections and local article subsections |
| `.wistjedat` | `Wist je dat...` section |
| `.easy_img_caption img` | Article image URL, alt text, title |
| `.easy_img_caption_inner` | Image caption |
| `ul li` under `Weblinks` | External reference links |
| `script[type="application/ld+json"]` | Metadata such as page name, description, and modified date |
| `meta[property="og:*"]` | Fallback metadata and lead image |

Read the page in source order. Do not extract only search matches; use the complete article body so no content blocks are missed.

### 3. Capture Semoea Content Exactly Before Editing

Create a raw extraction note for the gemstone before writing the final Markdown.

The note may be temporary, but it must preserve:

- all article headings in order
- all paragraphs in order
- all list items in order
- all table-like property values
- all image URLs, alt text, titles, and captions
- all external links
- all scientific notation exactly as shown in the Semoea HTML

Also record a source-coverage inventory before rewriting. This inventory must flag content that is easy to lose when prose is reorganized:

- source-specific historical, religious, artistic, trade, and symbolic claims;
- naming explanations, alternative names, and word histories;
- every `Wist je dat...` item, including therapy-related items;
- operational practices such as oils, elixirs, crystal water, placements, cleansing, or charging;
- warnings, responsibility statements, treatment disclaimers, and professional-care guidance;
- source-specific dates, quantities, locations, named people, animals, objects, and institutions.

The raw checkpoint is an audit instrument, not a summary. A claim may later move to a different Markdown section, but it must remain traceable to the raw capture.

Do not summarize during this step. This is the raw capture/checkpoint step, not the publishable Markdown prose.

### 4. Give Special Attention To Composition

Composition is the highest-value property and must receive a dedicated extraction pass.

Read the `Eigenschappen` block and capture every composition-related detail:

| Composition field | Extraction rule |
|---|---|
| Source label | Usually `Samenstelling`; copy the label context if it differs |
| Source notation | Preserve the formula exactly as Semoea presents it, including commas, parentheses, hydration dots, plus signs, and trace additions |
| HTML notation | Preserve subscript markup such as `<sub>2</sub>` when present |
| Normalized Markdown notation | Convert scientific notation to readable Markdown using `<sub>` tags |
| Scientific name / mineral species | Identify the mineral species separately from the gemstone or trade name |
| Mineral group / family | Record when stated by Semoea; otherwise validate from external scientific sources later |
| Chemical class | Record when stated by Semoea; otherwise validate from external scientific sources later |
| Trace elements / inclusions | Capture trace elements, inclusions, substitutions, and impurities mentioned anywhere on the page |
| Varieties / trade names | Capture names that affect scientific interpretation or possible confusion |

Validation rule: the value in `Chemical composition, source notation` must be traceable to Semoea. The value in `Chemical composition, normalized Markdown notation` must preserve the same chemistry, only changing display format.

### 5. Create The Markdown File From The Spec

Create `gemstones/<english-slug>.md` using the full template from [gemstone-spec.md](/Users/yveslangeraert/Documents/Edelstenen/gemstone-spec.md).

Important rules:

- Keep every heading from the spec.
- Keep every table from the spec.
- Keep empty table rows and empty fields.
- Start with `## Overview` as narrative understanding: include the source page's introductory description here, then add only the essence links that genuinely help the reader navigate.
- If Semoea does not list a section, write `Not listed on source page.`
- Do not remove empty sections for neatness.
- Preserve the Semoea order even if another source uses a different structure.
- Preserve Semoea links exactly.
- Use human-readable link text.
- Keep medical or therapeutic material attributed to Semoea and avoid presenting it as advice.
- Write the body in an observational voice about the gemstone itself. Avoid repetitive source-forward phrasing such as `Semoea notes`, `Semoea says`, or `Semoea describes`.
- Use Obsidian links for graph-worthy concepts such as mineral species, groups, elements, varieties, related stones, chakras, zodiac signs, and historical concepts.
- Avoid a machine-generated impression: vary the overview shape per gemstone, avoid a fixed checklist rhythm, and do not force every section into the overview.
- Avoid overlap: use the overview for orientation and descriptive understanding; use later tables and sections for normalized facts, validation, source comparison, and detail.

### 6. Transfer Semoea Content Without Summarising

Paste or convert the Semoea article content into the Markdown equivalent according to the spec.

Use equivalent Markdown forms:

| Semoea content | Markdown equivalent |
|---|---|
| `h1` | `#` |
| `h2` | `##` |
| `h3` | `###` |
| introductory paragraphs before `Herkomst van de naam` | `## Overview` |
| other paragraph | matching deeper narrative or structured section |
| line-separated `*` claims | bullet list |
| `Eigenschappen` values | `## Composition`, `## Key Identity`, and `## Appearance` tables |
| image with caption | row in `## Lead Image` or `## Images` |
| web links list | `## Sources` table |
| `Wist je dat...` list | `## Did You Know` bullet list |

This step is not a high-level summary. Keep the meaning, order, and detail density intact. Translate labels and headings into English, but do not compress the article into a shorter overview. Use original wording rather than reproducing Semoea's long prose verbatim. The overview should retain the source description content, while deeper sections should organize the same material into structured knowledge without needless repetition.

### 6A. Transfer Energetic And Therapeutic Content Completely

The energetic and therapeutic section is a source-preservation section, not a short interpretation. Its minimum content must reflect everything present on the source page, while keeping the claims explicitly attributed to the source tradition and clearly separated from medical advice.

Before writing the final page, create a therapeutic coverage map in the raw extraction checkpoint:

| Source content | Required capture |
|---|---|
| Section overview or introductory therapy paragraph | Preserve the complete meaning in `### Overview`, not just a one-sentence theme. |
| `Spiritueel` / Spiritual | Capture every distinct claim, chakra placement, energetic action, symbolic association, and usage instruction. |
| `Mentaal` / Mental | Capture every distinct claim about thoughts, attention, confidence, learning, behavior, or decision-making. |
| `Emotioneel` / Emotional | Capture every distinct claim about feelings, stress, fear, grief, relationships, or emotional processing. |
| `Fysiek` / Physical | Capture every distinct body-system, symptom, condition, preparation, placement, and usage claim. |
| Recipes, oils, elixirs, crystal water, cleansing, charging, dosage, or placement instructions | Preserve in a clearly labeled source-tradition subsection; never silently omit operational details. |
| Warnings, contraindications, exceptions, or “use only if” language | Preserve prominently and do not soften or reinterpret. |
| Therapy-related `Wist je dat...` items | Keep in `## Did You Know` and cross-reference them in the coverage map. |

Transfer rules:

- Keep one Markdown bullet or table row for each distinct source bullet or claim. Closely related sentences may be combined only when no meaning, condition, body area, or usage detail is lost.
- Preserve the source's Spiritual, Mental, Emotional, and Physical order. If a subsection is absent, write `Not listed on source page.`
- Preserve all named body areas, symptoms, conditions, chakras, emotions, relationships, and materials. Do not replace a long list with “supports overall health.”
- Preserve source recipes and application instructions as descriptions of the tradition, but add the standard disclaimer that they are not medical advice and should not replace professional care.
- Do not add medical corrections inside the source-tradition bullets. Put safety or evidence qualifications in a separate note so the source content remains auditable.
- If the source uses repeated claims, retain them where they occur or record the repetition in the raw checkpoint; do not deduplicate until after coverage validation.
- Use observational English prose, but keep the scope and strength of the source claim. Do not turn “associated with” into “treats,” and do not turn a source instruction into a recommendation from this repository.

Therapeutic content is complete only when a reviewer can compare the final four subsections and any therapy instructions against the raw source capture and account for every source claim.

### 6B. Transfer Source-Specific Context Completely

The same preservation standard applies outside the therapeutic section. Do not assume that a fact is optional because it is historical, symbolic, poetic, commercial, or placed in a `Wist je dat...` block.

Before finalizing, compare the page against the source-coverage inventory and confirm that:

- historical and cultural claims retain their dates, places, people, objects, and uncertainty where present;
- name-origin explanations retain each meaningful linguistic step and alternate name;
- symbolic associations, runes, zodiac entries, religious associations, and trade meanings are represented;
- source-specific “Did You Know” items are present, including items that repeat or extend the therapy section;
- source disclaimers and responsibility statements are preserved or clearly represented in `Source Notes`;
- practical instructions are retained as source tradition and are not silently converted into repository advice;
- omissions caused by source access are explicitly marked as missing or conditional.

Do not replace several distinct source details with a broad sentence such as “the stone has a rich history” or “the stone supports wellbeing.”

### 6C. Extract Therapeutic Concepts For The Graph

After the source-attributed therapeutic prose is complete, run the five-pass coverage workflow in [therapeutic-concept-model.md](/Users/yveslangeraert/Documents/Edelstenen/therapeutic-concept-model.md). Do not treat a small seed vocabulary as complete.

For each concept:

- choose the correct dimension and concept kind;
- capture candidates before normalizing synonyms;
- create or reuse a canonical note under `concepts/<dimension>/`;
- add a source-qualified `associated_with` relationship in frontmatter;
- add or update the concept note's human-readable `## Related Gemstones` list;
- add an inline wikilink only where it improves navigation;
- preserve distinctions between body areas, symptoms, systems, feelings, and mental processes;
- do not infer concepts from modern medical knowledge or mineral chemistry;
- do not use `treats`, `cures`, or `prevents` as relationship language.

Use the controlled model in [therapeutic-concept-model.md](/Users/yveslangeraert/Documents/Edelstenen/therapeutic-concept-model.md). The concept layer is an index over the source prose, not a replacement for it.

### 7. Validate That Semoea Content Was Not Summarised

Compare the Markdown file against the source article.

Minimum checks:

- every Semoea `h2` section exists in the Markdown output
- every Semoea `h3` subsection exists in the Markdown output
- all health subsections are present: spiritual, mental, emotional, physical, or explicitly marked missing
- every source therapeutic bullet or distinct claim has a corresponding Markdown bullet, table row, or explicitly mapped sentence
- the therapeutic overview preserves all source themes rather than only the dominant theme
- all therapy recipes, oils, elixirs, crystal-water instructions, cleansing/charging instructions, placements, dosage language, and warnings are represented or explicitly marked missing
- no medical condition, body area, chakra, emotional state, material, or source qualifier has been dropped from the therapeutic section
- the final therapeutic section is checked against the raw therapeutic coverage map, not only against the page headings
- all paragraphs have equivalent content in the Markdown output
- all Semoea bullet/list items have equivalent bullets or table rows
- all source-page `Weblinks` / `Webtips` entries are present in `## Sources`
- all `Wist je dat...` entries are present
- all source-specific historical, symbolic, trade, naming, and cultural claims are present or explicitly mapped as unavailable
- all source disclaimers, responsibility statements, and professional-care guidance are represented in the page or `Source Notes`
- all source-specific dates, quantities, locations, named people, animals, objects, and institutions are preserved where present
- every extracted mental, emotional, and physical concept is source-mapped and dimension-checked
- every candidate is marked mapped, intentionally unmapped, or blocked
- every concept relationship uses source-tradition scope and non-medical relation language
- every concept note links back to the gemstones that carry the relationship
- all images are recorded in `Images Mentioned`
- no content was shortened into a broad summary
- empty spec elements are still present
- overview contains the source page's descriptive opening
- overview does not read like a fixed generated checklist
- later sections add structure or depth rather than simply repeating overview prose

If content has been summarized by dropping facts, sections, images, links, or list items, restore the missing detail before moving on.

### 8. Validate Composition Again

Run a second composition-focused validation before adding outside sources.

Check:

- the Semoea source formula is present exactly in `Chemical composition, source notation`
- the normalized formula matches the source formula chemically
- subscripted numbers are represented with `<sub>` tags
- plus signs, parentheses, comma-separated substitutions, and trace elements are preserved
- the scientific name / mineral species is present or explicitly marked as pending external validation
- mineral group / family and chemical class are present or explicitly marked as pending external validation
- composition-related comments elsewhere in the page are not lost

Do not proceed if the formula is ambiguous. Mark the ambiguity in `Formula notes` and resolve it using high-quality sources in the next step.

### 9. Add At Least Two High-Quality External Sources

For each gemstone, add at least two high-quality sources beyond Semoea.

Preferred source types:

| Source type | Examples |
|---|---|
| Mineralogical databases | Mindat, Webmineral, RRUFF, Handbook of Mineralogy |
| Encyclopedic references | Encyclopaedia Britannica, curated museum or university pages |
| Gemological references | GIA, Gem-A, International Gem Society |
| Scientific or museum collections | Smithsonian, Natural History Museum, university mineral collections |

Avoid low-quality or circular sources when validating scientific facts:

- SEO crystal-healing pages
- unsourced shop product pages
- AI-generated content farms
- pages that copy Semoea or Wikipedia without attribution

Add external sources in the `## Sources` table or a dedicated source-notes subsection if needed. Keep Semoea's original `Weblinks` / `Webtips` entries intact.

### 10. Cross-Validate Scientific And Historical Claims

Use the external sources to validate:

- scientific name / mineral species
- chemical composition
- mineral group / family
- chemical class
- hardness
- crystal system
- density
- transparency, luster, cleavage, fracture
- known varieties and trade names
- historical or cultural claims where external sources cover them

When sources disagree, do not silently choose one. Add a short note in the relevant section explaining the difference and cite the sources.

### 11. Validate Composition With External Sources

Give composition one more dedicated review using the high-quality external sources.

Check:

| Question | Required outcome |
|---|---|
| Does Semoea's formula match a recognized mineral species? | Confirm or note the discrepancy |
| Does the formula need a group-level explanation? | Add it to `Formula notes` |
| Are trace elements coloring agents or substitutions? | Record the distinction |
| Is the gemstone a variety rather than a mineral species? | State the species and variety relationship |
| Are trade names scientifically imprecise? | Clarify in `Varieties / trade names` or `Formula notes` |
| Do external sources use a different formula style? | Preserve Semoea's formula and add the alternate style with citation |

Composition should finish as the most carefully validated part of the file.

### 12. Refine Once With Reliable Knowledge

Perform one final refinement iteration using reliable mineralogical or gemological knowledge.

This refinement may:

- clarify terminology
- add missing scientific context
- correct translation issues
- improve table consistency
- improve the voice so the stone is the subject and source credit stays in source sections
- distinguish mineral species from gemstone variety
- add a concise note where Semoea is poetic, historical, therapeutic, or trade-oriented

This refinement must not:

- remove Semoea content
- replace Semoea structure
- flatten nuance into a summary
- add unsupported therapeutic claims
- hide source disagreements

### 13. Final Composition Refinement

End the refinement with one final composition check.

Required final state:

- scientific name / mineral species is filled
- mineral group / family is filled
- chemical class is filled where reliable sources support it
- Semoea formula is preserved exactly
- normalized Markdown formula is readable and chemically equivalent
- trace elements, substitutions, inclusions, and trade-name caveats are captured
- formula notes cite or name the reliable source used for validation

If any of these cannot be completed, leave the field present and write a specific reason, not a blank.

### 14. Final File Check

Before considering the gemstone complete, verify:

- the file follows [gemstone-spec.md](/Users/yveslangeraert/Documents/Edelstenen/gemstone-spec.md)
- all required headings exist
- all required tables exist
- empty elements from the spec still exist
- Semoea content has not been summarized
- at least two high-quality external sources are included
- composition has passed both Semoea and external-source validation
- source links are clickable and human-readable
- claims added during refinement are backed by reliable sources

### 14A. Therapeutic Graph Verification

Treat therapeutic concept extraction as its own evidence-backed editorial pass after the therapeutic prose is stable:

1. Create or update `concept-coverage/<english-slug>.md` from the complete prose.
2. Capture candidates sentence by sentence before looking at existing graph links.
3. Review mental, emotional, and physical candidates with the specialist references in `skills/therapeutic-concept-extractor/references/`.
4. Preserve multi-word qualifiers and named conditions when they carry meaning.
5. Manifest mapped candidates in frontmatter, inline prose, and reciprocal concept notes.
6. Record intentional exclusions and source-section differences in the register.
7. Run `python3 scripts/validate_therapeutic_concepts.py gemstones/<slug>.md`.
8. Mark the register `Status: reconciled` only after the command passes and the human register review is complete.

The validator is a structural guardrail, not a semantic oracle. A passing command does not excuse a shallow candidate capture.

## Completion Checklist

Use this checklist per gemstone:

- [ ] Gemstone selected from the menu file
- [ ] Semoea page visited
- [ ] Full article DOM read in source order
- [ ] Raw content captured before editing
- [ ] Composition extracted with exact Semoea notation
- [ ] Scientific identity table filled
- [ ] Markdown file created from the full spec
- [ ] Empty spec elements preserved
- [ ] Semoea content transferred without summarising
- [ ] Therapeutic coverage map created before rewriting
- [ ] Every therapeutic source claim transferred or explicitly marked missing
- [ ] Therapeutic recipes, instructions, warnings, and qualifiers preserved
- [ ] Therapeutic section compared against the raw coverage map
- [ ] Source-coverage inventory created before rewriting
- [ ] Historical, symbolic, naming, trade, and cultural claims checked against the source inventory
- [ ] Source disclaimers and responsibility statements preserved
- [ ] Therapeutic concepts extracted into the controlled graph vocabulary
- [ ] Therapeutic concept links and source relationships validated
- [ ] Concept notes contain matching human-readable gemstone links
- [ ] Non-summary validation completed
- [ ] Composition revalidated against Semoea
- [ ] At least two high-quality external sources added
- [ ] Scientific claims cross-validated
- [ ] Composition validated against external sources
- [ ] One reliable-knowledge refinement pass completed
- [ ] Final composition refinement completed
- [ ] Final file check completed
- [ ] Therapeutic coverage register created from complete prose
- [ ] Candidate phrases captured before normalization
- [ ] Multi-concept sentences and multi-word concepts reviewed
- [ ] Every candidate has a final mapped, intentionally unmapped, or blocked state
- [ ] Therapeutic graph validator passes
- [ ] Register status is reconciled only when all human and machine checks pass

### Source Access And Media Status

Record the source-access mode in the page's `## Source Notes` and validation notes:

- `direct HTML`: the primary page was retrieved and read directly;
- `indexed full text`: the page was read from a reliable indexed rendering when direct retrieval was blocked;
- `partial indexed text`: only part of the source was available and the page remains conditional;
- `blocked`: do not complete the page from memory or unsupported secondary summaries.

Image labels and captions recovered from indexed text are not image URLs. Mark an image URL as `Not recovered from indexed source result.` until the exact URL has been verified. Do not infer asset paths from naming conventions.

## Batch Expansion Protocol

When creating multiple gemstone files, use [gemstone-expansion-plan.md](/Users/yveslangeraert/Documents/Edelstenen/gemstone-expansion-plan.md) as the batch-level contract.

- Work in batches of three to five deliberately diverse gemstones.
- Read and capture every primary source before writing the corresponding page.
- Treat the per-page checklist above as a hard quality floor.
- Compare each completed batch with the pilot pages for structure, source coverage, composition handling, and writing voice.
- Record omissions, conflicts, rework, and specification changes in a batch audit.
- Change the specification only between batches, never silently during page creation.
- Recheck an affected pilot page after any specification change.
- Stop expansion when the primary source is inaccessible, composition is unresolved, or repeated one-off exceptions indicate contract drift.

Throughput is not a completion criterion. Evidence, traceability, and structural consistency are.
