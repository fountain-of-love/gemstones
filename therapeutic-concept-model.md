# Therapeutic Concept Model

This document defines how mental, emotional, and physical concepts become reusable Obsidian graph nodes without turning source traditions into medical or psychological facts.

## Purpose

Gemstone pages remain readable narrative documents. Their therapeutic sections preserve the source material in full. A second, structured layer makes recurring concepts filterable:

- Which gemstones are associated with fear?
- Which emotional concepts are shared by several stones?
- Which stones combine concentration and sleep associations?
- Which physical systems recur across a mineral family?

The graph layer is an index of source-attributed associations, not a claim that gemstones cause health or psychological outcomes.

## Three Dimensions

| Dimension | Meaning | Examples |
|---|---|---|
| Emotional | Feelings, emotional states, relational patterns, and emotional processing | fear, grief, calm, trust, jealousy, hope |
| Mental | Attention, cognition, learning, perception, motivation, and decision-making | concentration, memory, intuition, clarity, creativity |
| Physical | Body areas, systems, symptoms, functions, and source-mentioned conditions | headache, throat, sleep, circulation, skin, bones |

Physical concepts must retain their kind. `physical/throat` is a body area; `physical/sore-throat` is a symptom; `physical/circulation` is a body function/system. Do not collapse them into one generic health label.

## Canonical Concept Notes

Concept notes live under:

```text
concepts/emotional/<concept>.md
concepts/mental/<concept>.md
concepts/physical/<concept>.md
```

Each note has one canonical identity and may list aliases. A concept note should stay short and define the graph vocabulary, not reproduce every gemstone claim.

```yaml
---
type: therapeutic-concept
dimension: emotional
concept_id: emotional/fear
concept_kind: emotional-state
aliases:
  - phobia
---
```

Every concept note must also contain a human-readable `## Related Gemstones` section. The links are intentionally explicit even though Obsidian can generate backlinks automatically: a reader should be able to open an anger note, understand the concept, and immediately navigate to the gemstones associated with it.

```markdown
## Related Gemstones

- [[Diamond]] — source-tradition association
```

The gemstone-to-concept and concept-to-gemstone directions must agree. When a gemstone relationship is added or removed, update both sides or regenerate the concept-side list during validation.

## Source-Qualified Relationships

Gemstone frontmatter carries the graph edge and its provenance:

```yaml
therapeutic_concepts:
  emotional:
    - concept: "[[concepts/emotional/fear|fear]]"
      relation: associated_with
      source: Semoea
      scope: source-tradition
      source_section: Emotional
```

Use `associated_with` as the default relation. Do not use `treats`, `cures`, or `prevents` in the graph layer. If the source gives a placement, recipe, warning, or condition, keep that detail in the gemstone prose and record it in the page's source notes.

## Extraction Rules

- Create a concept only when it is explicit in the source or is a stable umbrella for several explicit source terms.
- Prefer a small controlled vocabulary over one node for every symptom or synonym.
- Preserve source distinctions: fear is not automatically anxiety; headache is not automatically migraine; throat is not automatically sore throat.
- Link the concept in the relevant therapeutic bullet as well as in frontmatter when the link improves navigation.
- Keep the original source wording and attribution in the gemstone page.
- Do not infer concepts from the stone's mineral chemistry or from modern medical knowledge.
- If the primary source is incomplete, mark the page relationship as conditional rather than inventing concepts.

## Coverage Workflow

Concept extraction is a separate editorial pass, not a by-product of writing the therapeutic prose.

### Pass A: Candidate Capture

Read the completed Spiritual, Mental, Emotional, and Physical sections and capture every explicit candidate phrase. Include repeated concepts, named symptoms, body areas, systems, emotional states, cognitive functions, and usage-related concepts. Do not normalize while capturing.

### Pass B: Classification

For each candidate, record:

| Field | Meaning |
|---|---|
| Source phrase | Exact or faithful phrase from the gemstone page/source |
| Dimension | Mental, emotional, or physical |
| Concept kind | Emotional state, cognition, body area, symptom, body system, body function, condition, or relational theme |
| Source section | The therapeutic subsection where the source placed the phrase |
| Canonical concept | Existing note, new note, or intentionally not mapped |
| Reason | Why the mapping is valid or why the candidate remains unmapped |

### Pass C: Normalization

Merge only true synonyms or stable umbrella terms. Keep distinct concepts separate when the source distinguishes them. For example, `fear`, `worry`, `headache`, `migraine`, `throat`, and `sore throat` should not be merged automatically.

### Pass D: Manifestation

Add the concept to gemstone frontmatter, link its first meaningful prose occurrence, create or reuse the canonical concept note, and update that note's `## Related Gemstones` section.

### Pass E: Reconciliation

Compare the candidate register, gemstone frontmatter, inline links, and concept-note reverse links. Every candidate must end in one of three states:

- `mapped`: represented by a canonical concept and reciprocal links;
- `intentionally unmapped`: retained in prose with a documented reason, such as an overly specific one-off phrase;
- `blocked`: awaiting primary-source access or a vocabulary decision.

An unreviewed candidate is a quality failure. A page is not concept-complete merely because it has several links.

## Query Surfaces

The concept notes support three complementary navigation modes:

1. Local graph: open a concept note and see connected gemstone pages.
2. Global graph: include `gemstones` and one dimension path such as `concepts/emotional` in the graph search/filter.
3. Dataview: list pages whose structured frontmatter contains a selected concept or dimension.

Example Dataview query:

```dataview
TABLE name_en AS Gemstone, therapeutic_concepts.emotional AS Emotional
FROM "gemstones"
WHERE contains(therapeutic_concepts.emotional, "[[concepts/emotional/fear|fear]]")
SORT name_en ASC
```

If a Dataview installation does not resolve nested link objects consistently, retain a parallel stable ID field such as `emotional/fear` for querying while keeping the wikilink for graph navigation.

## Quality Gate

A concept extraction pass is complete only when:

- every extracted concept is traceable to a source claim;
- the dimension and concept kind are correct;
- every concept note links back to its related gemstones in readable prose;
- gemstone-side and concept-side relationships agree;
- the page still contains the complete source-attributed prose;
- the relationship uses a non-medical relation such as `associated_with`;
- missing or conditional source access is visible;
- concept notes do not become an unreviewed synonym dump.
- every explicit candidate in the coverage register is mapped, intentionally unmapped, or blocked;
- no dimension is treated as complete based only on link count.

## Evidence And Review Contract

The model has four deliberately separate artifacts:

| Artifact | Authority | Purpose |
|---|---|---|
| Gemstone therapeutic prose | Human-readable source-preservation layer | Keeps the complete attributed claim and its context visible. |
| `concept-coverage/<slug>.md` | Editorial evidence layer | Records every candidate phrase and the normalization decision. |
| Gemstone `therapeutic_concepts` frontmatter | Structured edge layer | Makes source-qualified relationships queryable. |
| `concepts/<dimension>/<id>.md` | Controlled vocabulary layer | Gives humans a reusable node with reverse navigation. |

These layers must agree, but they are not interchangeable. A frontmatter link cannot substitute for source prose; a concept note cannot substitute for the candidate register; and a register row cannot be considered mapped until the graph edge and reverse navigation exist.

### Candidate state machine

```text
captured -> classified -> mapped
                    \-> intentionally unmapped
                    \-> blocked
```

`captured` and `classified` are working states only. A register may be called `reconciled` only when no row remains in either state and no mapped edge fails structural validation.

### Review questions for each sentence

1. What explicit mental, emotional, physical, practical, or named-condition terms are present?
2. Are multiple concepts hiding in one phrase?
3. Does the source subsection differ from the semantic dimension?
4. Is the qualifier meaningful enough to preserve as a multi-word node?
5. Is the candidate explicit in the source, or has it been inferred?
6. If it is not mapped, is the reason recorded in the register and retained in prose?

### Verification command

Run the structural validator after manifestation and before declaring completion:

```bash
python3 scripts/validate_therapeutic_concepts.py gemstones/<slug>.md
```

This catches broken graph mechanics. It intentionally does not replace human source review; the register is the evidence that a human actually performed that review.
