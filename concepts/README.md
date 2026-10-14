# Therapeutic concept nodes

The `concepts/` tree is a controlled vocabulary for source-attributed gemstone traditions.

## Directory contract

```text
concepts/
  emotional/<stable-kebab-case-id>.md
  mental/<stable-kebab-case-id>.md
  physical/<stable-kebab-case-id>.md
```

Each note must have frontmatter with:

```yaml
type: therapeutic-concept
dimension: emotional
concept_id: emotional/example
concept_kind: emotional-state
aliases: []
```

It must also contain a short definition and a human-readable `## Related Gemstones` section. The note defines the vocabulary; gemstone-specific evidence belongs on gemstone pages and in their coverage registers.

## Naming rules

- Use a stable, lowercase kebab-case ID.
- Preserve meaningful qualifiers: `mental-clarity`, `tension-headache`, and `autonomic-nervous-system` are not generic `clarity`, `headache`, and `nervous-system`.
- Use aliases for true synonyms or source-language variants, not for unrelated concepts.
- Keep source conditions distinct when the source distinguishes them, unless the register records an intentional umbrella decision.
- Never use the graph node to imply `treats`, `cures`, or medical causation.

## Edge contract

Gemstone frontmatter owns the structured, source-qualified edge:

```yaml
concept: "[[concepts/emotional/fear|fear]]"
relation: associated_with
source: Semoea
scope: source-tradition
```

The concept note owns readable reverse navigation. Both directions are required for a mapped concept.
