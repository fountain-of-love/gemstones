# Gemstone Process Proof Run: First Five Files

Date: 2026-08-26

Process used: [gemstone-process.md](/Users/yveslangeraert/Documents/Edelstenen/gemstone-process.md)

Spec used: [gemstone-spec.md](/Users/yveslangeraert/Documents/Edelstenen/gemstone-spec.md)

## Scope

The proof run created five gemstone files:

| Gemstone | File | Status |
|---|---|---|
| Amethyst | [gemstones/amethyst.md](/Users/yveslangeraert/Documents/Edelstenen/gemstones/amethyst.md) | fuller proof-run transfer |
| Moonstone | [gemstones/moonstone.md](/Users/yveslangeraert/Documents/Edelstenen/gemstones/moonstone.md) | fuller proof-run transfer |
| Malachite | [gemstones/malachite.md](/Users/yveslangeraert/Documents/Edelstenen/gemstones/malachite.md) | fuller proof-run transfer |
| Rock crystal | [gemstones/rock-crystal.md](/Users/yveslangeraert/Documents/Edelstenen/gemstones/rock-crystal.md) | fuller proof-run transfer |
| Amazonite | [gemstones/amazonite.md](/Users/yveslangeraert/Documents/Edelstenen/gemstones/amazonite.md) | fuller proof-run transfer |

## Important Copyright Boundary

The process goal says to validate that content has not been summarized. In practice, the files must preserve Semoea's structure and factual coverage, but they cannot reproduce full Semoea article prose verbatim. For the proof run, "not summarized" means:

- all Semoea sections are represented
- all required spec sections and tables remain present
- scientific properties are copied as factual values
- composition notation is preserved exactly
- long article prose is paraphrased or represented as detailed factual coverage
- the body uses an observational voice about the stone, while source credit remains in source sections

## Per-Gemstone Process Trace

### Amethyst

| Step | Result |
|---|---|
| Source page visited | Yes: https://www.semoea.nl/edelstenen/amethist.html |
| DOM read | `.com-content-article.item-page`, `.astroid-article-text`, `.eigens`, `.vooreigens`, `h1`, `h2`, `h3`, `Weblinks`, `.wistjedat`, image captions |
| Spec file created | Yes |
| Empty elements preserved | Yes: missing luster is explicit |
| Non-summary validation | Strong factual coverage, paraphrased |
| External sources | Mindat, GIA, Webmineral |
| Final refinement | Added quartz-variety framing and color-center composition note |

Composition checkpoint:

| Field | Value |
|---|---|
| Semoea source notation | SiO<sub>2</sub> + (Fe, Al, Ti, Na, Li). |
| Normalized notation | SiO<sub>2</sub> + (Fe, Al, Ti, Na, Li) |
| Scientific identity | Quartz, variety amethyst |
| Validation | Mindat and GIA confirm SiO<sub>2</sub>; trace Fe/color-center explanation added |

### Moonstone

| Step | Result |
|---|---|
| Source page visited | Yes: https://www.semoea.nl/edelstenen/maansteen.html |
| DOM read | `.com-content-article.item-page`, `.astroid-article-text`, `.eigens`, `.vooreigens`, `h1`, `h2`, `h3`, `Weblinks`, `.wistjedat`, image captions |
| Spec file created | Yes |
| Empty elements preserved | Yes: missing caption is explicit |
| Non-summary validation | Strong factual coverage, paraphrased |
| External sources | GIA, Mindat, Mindat classification discussion |
| Final refinement | Added feldspar-variety caveat and adularescence explanation |

Composition checkpoint:

| Field | Value |
|---|---|
| Semoea source notation | (Na,K)AlSi<sub>3</sub>O<sub>8</sub> + Ca, Fe, Ba, Rb, Sr |
| Normalized notation | (Na,K)AlSi<sub>3</sub>O<sub>8</sub> + Ca, Fe, Ba, Rb, Sr |
| Scientific identity | Feldspar-group gemstone variety; commonly orthoclase/adularia with albite lamellae |
| Validation | GIA confirms orthoclase/albite layering; Mindat material shows classification caveats |

### Malachite

| Step | Result |
|---|---|
| Source page visited | Yes: https://www.semoea.nl/edelstenen/malachiet.html |
| DOM read | Headings and `Eigenschappen` block |
| Spec file created | Yes |
| Empty elements preserved | Yes: unavailable fields remain explicit |
| Non-summary validation | Detailed factual coverage, paraphrased |
| External sources | Mindat, Webmineral, USGS |
| Final refinement | Added ideal formula vs Semoea additive notation distinction |

Composition checkpoint:

| Field | Value |
|---|---|
| Semoea source notation | Cu<sub>2</sub>(CO<sub>3</sub>)(OH)<sub>2</sub> + H<sub>2</sub>O + (Ca, Fe) |
| Normalized notation | Cu<sub>2</sub>(CO<sub>3</sub>)(OH)<sub>2</sub> + H<sub>2</sub>O + (Ca, Fe) |
| Scientific identity | Malachite |
| Validation | Mindat, Webmineral, and USGS confirm ideal malachite as Cu<sub>2</sub>(CO<sub>3</sub>)(OH)<sub>2</sub>; Semoea additions preserved as source notation |

### Rock Crystal

| Step | Result |
|---|---|
| Source page visited | Yes: https://www.semoea.nl/edelstenen/bergkristal.html |
| DOM read | Headings and `Eigenschappen` block |
| Spec file created | Yes |
| Empty elements preserved | Yes: unavailable fields remain explicit |
| Non-summary validation | Detailed factual coverage, paraphrased |
| External sources | Mindat, Webmineral |
| Final refinement | Added rock crystal as colorless quartz variety |

Composition checkpoint:

| Field | Value |
|---|---|
| Semoea source notation | SiO<sub>2</sub> |
| Normalized notation | SiO<sub>2</sub> |
| Scientific identity | Quartz, variety rock crystal |
| Validation | Semoea, Mindat, and Webmineral agree on SiO<sub>2</sub> |

### Amazonite

| Step | Result |
|---|---|
| Source page visited | Yes: https://www.semoea.nl/edelstenen/amazoniet.html |
| DOM read | Headings and `Eigenschappen` block |
| Spec file created | Yes |
| Empty elements preserved | Yes: unavailable fields remain explicit |
| Non-summary validation | Detailed factual coverage, paraphrased |
| External sources | Mindat, Geology.com, Museum Wales, SciELO |
| Final refinement | Added microcline/K-feldspar variety framing and Pb color-cause caveat |

Composition checkpoint:

| Field | Value |
|---|---|
| Semoea source notation | K[AlSi<sub>3</sub>O<sub>8</sub>] + Cu, Na, Pb |
| Normalized notation | K[AlSi<sub>3</sub>O<sub>8</sub>] + Cu, Na, Pb |
| Scientific identity | Microcline, variety amazonite |
| Validation | Mindat and Geology.com confirm K-feldspar / microcline formula KAlSi<sub>3</sub>O<sub>8</sub>; Pb is strongly supported as color-related |

## Process Findings

- The spec works well for composition-heavy extraction.
- `## Scientific Identity` is the right place for formula disagreements and variety/species distinctions.
- Full article extraction is slower than composition extraction; the proof run shows a useful two-stage approach: first lock structure and chemistry, then complete long-form Semoea factual transfer.
- The process should explicitly distinguish "not summarized" from "not copied verbatim"; factual coverage can be complete while wording remains original.

## Process Adjustment Applied

[gemstone-process.md](/Users/yveslangeraert/Documents/Edelstenen/gemstone-process.md) now clarifies:

- "not summarised" means no facts, sections, links, images, or list items are omitted
- long Semoea prose should be paraphrased rather than copied verbatim
- the body should use an observational voice about the stone
- Semoea should be credited as the primary source in source sections, not repeated as the sentence subject throughout the file
