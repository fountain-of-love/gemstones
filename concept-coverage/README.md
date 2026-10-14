# Therapeutic concept coverage

This folder is the evidence layer between a gemstone’s therapeutic prose and its Obsidian graph edges.

## One register per gemstone

Create `concept-coverage/<gemstone-slug>.md` alongside the gemstone page. Copy [the template](./_template.md), then fill it from the completed source-attributed prose—not from memory and not from the links already present.

The register is deliberately more detailed than frontmatter. One source sentence may produce several candidates, and one candidate may be intentionally grouped or excluded. This is where that reasoning remains inspectable.

## Required lifecycle

1. Capture source phrases exactly or faithfully, before normalization.
2. Record the source subsection and semantic dimension separately.
3. Assign a concept kind and candidate canonical ID.
4. Decide one final state: `mapped`, `intentionally unmapped`, or `blocked`.
5. For `mapped`, verify the canonical note, gemstone frontmatter edge, inline prose link, and reciprocal gemstone link.
6. For `intentionally unmapped`, preserve the source phrase in prose and record why it is outside scope, too specific, or better represented as source detail.
7. For `blocked`, record the missing evidence or vocabulary decision. A blocked register cannot be complete.

## Completion states

Use one of these document statuses:

| Status | Meaning | May the gemstone be called concept-complete? |
|---|---|---|
| `draft` | Capture or classification is still underway. | No |
| `reconciliation` | Manifestation and reciprocal-link checks are underway. | No |
| `reconciled` | Every candidate has a final state and all mapped edges pass validation. | Yes |
| `conditional` | The source was partial or blocked; the page must say what remains unknown. | No |

`reconciled` does not mean every phrase became a graph node. It means every phrase has an explicit, reviewable decision.

## Machine-checkable contract

The validator at `scripts/validate_therapeutic_concepts.py` checks:

- the gemstone page exists and has `therapeutic_concepts` entries;
- every frontmatter concept target exists;
- every concept relationship has `relation`, `source`, and `scope`;
- the coverage register exists and contains no unresolved `Pending` rows;
- every mapped frontmatter concept has a concept note;
- every concept note has `## Related Gemstones` and a reciprocal gemstone link;
- the register is not marked `reconciled` while it still contains blocked or pending work.

Run it from the repository root:

```bash
python3 scripts/validate_therapeutic_concepts.py gemstones/amazonite.md
```

The validator checks structure and graph integrity. It cannot decide whether a human captured every nuance in a source sentence; that remains the purpose of the register review.
