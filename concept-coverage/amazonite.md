# Amazonite Therapeutic Concept Register

Status: reconciled

This register is the sentence-level checkpoint for Amazonite. It separates source phrases from normalized graph concepts so that a readable sentence can contribute several links without losing its original meaning.

## Mental

| Source phrase | Candidate concepts | Status / decision |
|---|---|---|
| Supports willpower and strengthens the intellect | `mental/willpower`, `mental/intellect` | Mapped |
| Improved blood flow to the brain | `physical/circulation`, `physical/brain` | Mapped; source section is Mental, semantic dimension is Physical |
| Mild psychological complaints | `mental/psychological-complaints` | Mapped as a broad source category |
| ADHD | `mental/adhd` | Mapped as named condition |
| Filtering information passing through the brain | `mental/information-filtering`, `physical/brain` | Mapped; source section is Mental |
| Combining information with intuition | `mental/intuition`, `mental/information-processing` | Mapped as two distinct cognitive concepts |
| Mental calm and clarity | `mental/calm`, `mental/mental-clarity` | Mapped as two distinct mental states |
| Overview | `mental/overview` | Mapped |
| Calmly examining a problem from all sides | `mental/reflective-examination`, `mental/problem-solving` | Mapped as reasoning process plus outcome |

## Emotional

| Source phrase | Candidate concepts | Status / decision |
|---|---|---|
| Calming and balancing extreme mood swings | `emotional/calm`, `emotional/emotional-balance`, `emotional/mood-swings` | Mapped as state plus regulation |
| Feelings of inner division | `emotional/inner-division` | Mapped |
| Sadness | `emotional/sadness` | Mapped |
| Malende gedachten / repetitive thoughts | `mental/rumination` | Mapped; semantic dimension is Mental despite source placement |
| Worries / zorgen | `emotional/worry` | Mapped |
| Fear of losing control | `emotional/fear`, `emotional/loss-of-control` | Mapped as general fear plus specific fear theme |
| Awareness of unconscious bodily functions | `physical/autonomic-functions`, `mental/body-awareness` | Mapped as physical function plus mental awareness; source section is Emotional |
| Incontinence and bed-wetting | `physical/incontinence`, `physical/bed-wetting` | Mapped as distinct symptoms |
| Hyperventilation | `physical/hyperventilation` | Mapped as symptom; source section is Emotional |
| Trauma-softening | `emotional/trauma` | Mapped |
| Negative thoughts | `mental/negative-thoughts` | Mapped separately from worry and rumination; source section is Emotional |
| Frustration and irritation | `emotional/frustration`, `emotional/irritation` | Mapped |
| Spring fatigue / voorjaarsmoeheid | `physical/fatigue` | Mapped; source section remains Emotional |
| Cheerfulness at the end of winter | `emotional/cheerfulness` | Mapped |

## Physical

| Source phrase | Candidate concepts | Status / decision |
|---|---|---|
| Skin and hair complaints | `physical/skin`, `physical/hair` | Mapped as body-area concepts |
| Acne, pimples, itching, flaky skin and lips, psoriasis, fungal infections, swimmer's eczema | `physical/acne`, `physical/itching`, `physical/flaky-skin`, `physical/lips`, `physical/psoriasis`, `physical/fungal-infection`, `physical/swimmers-eczema` | Mapped as explicit source conditions/body areas; all retain `physical/skin` as the broader node |
| Herpes simplex / cold sores | `physical/herpes-simplex` | Mapped as named condition |
| Nervous system and nerve function | `physical/nervous-system` | Mapped |
| Left and right brain hemispheres | `physical/brain-hemispheres` | Mapped separately from general brain |
| Autonomic / vegetative nervous system | `physical/autonomic-nervous-system` | Mapped separately from general nervous system |
| Breathing, heart rhythm, digestion | `physical/breathing`, `physical/heart-rhythm`, `physical/digestion` | Mapped as distinct body functions |
| Hormonal system, pituitary, thymus | `physical/hormonal-system`, `physical/pituitary`, `physical/thymus` | Mapped as system plus named organs |
| Immune system | `physical/immune-system` | Mapped |
| Internal organs and metabolism | `physical/internal-organs`, `physical/metabolism` | Mapped as umbrella body area plus function |
| Liver-related metabolic complaints | `physical/liver`, `physical/metabolism` | Mapped as organ plus function |
| Relaxation | `physical/relaxation` | Mapped under Physical because the source places it there |
| Menstrual cramps and childbirth | `physical/menstrual-cramps`, `physical/childbirth` | Mapped as symptom plus life-event topic |
| Arthrosis and chronic rheumatism | `physical/arthrosis`, `physical/rheumatism` | Mapped as distinct named conditions |
| Heart, blood quality, blood flow, arteries, veins | `physical/heart`, `physical/blood-quality`, `physical/circulation`, `physical/arteries`, `physical/veins` | Mapped as organ, quality, function, and structures |
| Lymph flow | `physical/lymphatic-system` | Mapped |
| Grief-related heart complaints | `emotional/grief`, `physical/heart` | Grief exists; heart pending |
| Osteoporosis, tooth decay, calcium deficiency, calcium deposits | `physical/osteoporosis`, `physical/teeth`, `physical/calcium` | Mapped; calcium deficiency/deposits intentionally share one nutrient concept |
| Strong, chronic, migraine-like, or tension headaches | `physical/headache`, `physical/migraine`, `physical/tension-headache` | Mapped as generic and qualified headache concepts |
| Childhood diseases, including measles and smallpox | `physical/childhood-diseases`, `physical/measles`, `physical/smallpox` | Mapped as category plus named examples |
| Sleep, falling asleep, staying asleep | `physical/sleep`, `physical/insomnia` | Mapped as general function plus sleep condition |
| Down syndrome | `physical/down-syndrome` | Mapped as named condition; source-attributed only |

## Source-specific operational claims

These claims occur in the page’s `Did You Know` section rather than in the three therapeutic subsections. They are still candidates because they describe physical, emotional, or practical use. The graph keeps them source-attributed and does not imply efficacy.

| Source phrase | Candidate concepts | Status / decision |
|---|---|---|
| First-degree burns and sunburn | `physical/burns`, `physical/sunburn` | Mapped as named conditions |
| Limiting scar tissue after surgery | `physical/scar-tissue` | Mapped as tissue condition |
| Rough skin, small wounds, and cracks after hand washing | `physical/rough-skin`, `physical/wounds` | Mapped; source-specific practical use remains in prose |
| RSI-like complaints | `physical/repetitive-strain-injury` | Mapped as condition category |
| Mouse-arm strain | `physical/mouse-arm` | Mapped as named condition |
| Tennis elbow | `physical/tennis-elbow` | Mapped as named condition |
| Carpal tunnel complaints | `physical/carpal-tunnel` | Mapped as named condition |
| Nervousness before sleep | `emotional/nervousness` | Mapped as emotional state |
| Financial or intellectual success, attracting customers, electromagnetic radiation | — | Intentionally unmapped: these are symbolic/operational source details outside the mental, emotional, and physical therapeutic concept scope |

## Reconciliation Rule

Amazonite is concept-complete only while every candidate row has a final status, every mapped concept has reciprocal navigation, and source-specific details remain visible in prose. New source text reopens this register.
