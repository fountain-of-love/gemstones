# Gemstone Expansion Batch Audit: Batch 1

Date: 2026-10-12

## Scope

| Gemstone | File | Status |
|---|---|---|
| Amber | [gemstones/amber.md](/Users/yveslangeraert/Documents/Edelstenen/gemstones/amber.md) | Structurally complete; source read through indexed full text; direct HTML blocked |
| Diamond | [gemstones/diamond.md](/Users/yveslangeraert/Documents/Edelstenen/gemstones/diamond.md) | Structurally complete; source read through indexed full text; direct HTML blocked |
| Lapis lazuli | [gemstones/lapis-lazuli.md](/Users/yveslangeraert/Documents/Edelstenen/gemstones/lapis-lazuli.md) | Structurally complete; indexed full text available; direct HTML blocked |
| Obsidian | [gemstones/obsidian.md](/Users/yveslangeraert/Documents/Edelstenen/gemstones/obsidian.md) | Structurally complete; Dutch index points to Helen met Stenen; direct HTML blocked |
| Turquoise | [gemstones/turquoise.md](/Users/yveslangeraert/Documents/Edelstenen/gemstones/turquoise.md) | Conditional; composition and main facts validated, but primary source and complete media/runic extraction remain unavailable |

## Per-Page Results

| Gemstone | Primary source fully read | Composition validated | External sources | Checklist passed | Notes |
|---|---|---|---|---|---|
| Amber | Indexed full-text result | Yes | 3 | Conditional | Organic resin modeled separately from minerals; direct HTML unavailable. |
| Diamond | Indexed full-text result | Yes | 3 | Conditional | Native carbon and cut-name distinctions preserved; direct HTML unavailable. |
| Lapis lazuli | Indexed full-text result | Yes | 4 | Conditional | Mixed rock modeled separately from lazurite; direct HTML unavailable. |
| Obsidian | Indexed full-text result from Helen met Stenen | Yes | 3 | Conditional | Source ownership is explicit; direct HTML unavailable. |
| Turquoise | Partial indexed/related source material | Yes | 3 | No — source completion required | Runes and exact image inventory remain unresolved. |

## Cross-Page Review

- Structural drift: none in headings, frontmatter, required tables, or validation sections.
- Material-type coverage: organic resin, native element, mixed rock, volcanic glass, and hydrated phosphate were added.
- Composition handling: the shared composition table remains usable, but “ideal mineral formula” needs explicit non-mineral handling for organic and glass materials.
- Naming drift: no unresolved drift found; mixed materials and trade names are called out explicitly.
- Source-quality concerns: direct Semoea HTML returned 403; indexed results were used for four pages, and Turquoise still needs a complete primary-source pass.
- Media concerns: image labels were captured from indexed content, but exact source image URLs require confirmation before treating them as reusable assets.
- Coverage concern: the Lapis Lazuli comparison exposed a general risk beyond therapy compression: source-specific historical, symbolic, naming, trade, “Did You Know,” and disclaimer details can disappear during restructuring unless they are inventoried explicitly.

## Process Decision

- Specification change required: Yes, after the batch review.
- Process change required: Yes, add a primary-source access status and a media-URL verification gate.
- Pilot page recheck required: Yes, after updating the composition and source-access guidance.
- Decision before next batch: Do not start Batch 2 until Turquoise receives a complete source pass and the guessed/unverified media paths in Batch 1 are confirmed or replaced with explicit unavailable markers.

## Quality Decision

Batch 1 is a useful diversity test but is not fully accepted as production-complete. Four pages are conditionally complete and one page remains blocked. The batch successfully exposed two process improvements before further expansion:

1. A page must record whether its primary source was read directly, through indexed full text, or only partially.
2. Image metadata must distinguish a verified URL from an image label recovered from source text.
3. The raw extraction checkpoint must include a source-coverage inventory for historical, symbolic, naming, trade, “Did You Know,” instruction, warning, and disclaimer content.
