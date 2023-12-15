# Constraint Grammar

#### DELIMITERS
- **`.`** : Sentences are delimited by periods.

#### LISTS
- **FINITE**: Includes words with the feature `VerbForm=Fin`, representing finite verbs.
- **THE**: Includes the definite article "the".
- **INF**: Includes words with the feature `VerbForm=Inf`, representing infinitive verbs.
- **PREP**: Includes common English prepositions such as "of" and "in".
- **NOMINAL**: Includes nouns (`NOUN`) and proper nouns (`PROPN`).
- **REL**: Includes the word "that" when used as a relative pronoun.
- **CS**: Includes the word "that" when used as a conjunctive subordinator.
- **ADJ**: Represents adjectives.
- **ADV**: Represents adverbs.
- **NOUN**: Represents nouns.
- **VERB**: Represents verbs.
- **COLLECTIVE_NOUN**: Includes words like "majority" that can refer to a collective entity but are treated as singular.

#### RULES

1. **REMOVE FINITE IF (-1 THE)**:
   - Removes the finite verb reading if the word is immediately preceded by "the". This rule helps in cases where a word can be either a noun or a verb, and "the" indicates it's more likely a noun.

2. **REMOVE INF IF (NOT -1 PREP)**:
   - Removes the infinitive reading of a verb if it is not immediately preceded by a preposition. This rule is based on the typical structure of English infinitive phrases, which often follow prepositions.

3. **SELECT ADV IF (1C VERB)**:
   - Selects the adverb reading if the word is immediately followed by a verb. This rule is used to disambiguate words that can be both adverbs and other parts of speech, based on their position relative to a verb.

4. **SELECT REL IF (-1 NOMINAL) (0 REL OR CS) (1 FINITE)**:
   - Selects the reading of "that" as a relative pronoun if it follows a noun or proper noun (nominal) and is followed by a finite verb. This rule helps to disambiguate the use of "that" in relative clauses.

# Output:
```bash
"<At>"
        "at" ADP
"<the>"
        "the" DET Definite=Def PronType=Art
        "the" DET Definite=Def PronType=Art Typo=Yes
        "to" PART Typo=Yes
        "_" X
"<start>"
        "start" NOUN Number=Sing
;       "start" VERB VerbForm=Inf REMOVE:21
;       "start" VERB Mood=Ind Number=Plur Person=1 Tense=Pres VerbForm=Fin REMOVE:20
;       "start" VERB Mood=Ind Number=Plur Person=3 Tense=Pres VerbForm=Fin REMOVE:20
;       "start" VERB Mood=Ind Number=Sing Person=2 Tense=Pres VerbForm=Fin REMOVE:20
;       "start" VERB Mood=Imp Person=2 VerbForm=Fin REMOVE:20
"<of>"
        "of" ADP
        "of" SCONJ
        "of" ADP Typo=Yes
"<the>"
        "the" DET Definite=Def PronType=Art
        "the" DET Definite=Def PronType=Art Typo=Yes
        "to" PART Typo=Yes
        "_" X
"<century>"
        "century" NOUN Number=Sing
"<,>"
        "," PUNCT
        "," PUNCT Foreign=Yes
        "." PUNCT

"<the>"
        "the" DET Definite=Def PronType=Art
        "the" DET Definite=Def PronType=Art Typo=Yes
        "to" PART Typo=Yes
        "_" X
"<majority>"
        "majority" NOUN Number=Sing
"<of>"
        "of" ADP
        "of" SCONJ
        "of" ADP Typo=Yes
"<English>"
        "English" ADJ Degree=Pos SELECT:25
        "English" ADJ Degree=Pos Number=Sing SELECT:25
;       "English" PROPN Number=Sing SELECT:25
"<people>"
        "person" NOUN Number=Plur
        "people" NOUN Number=Sing
"<worked>"
        "work" VERB Mood=Ind Number=Sing Person=3 Tense=Past VerbForm=Fin
        "work" VERB Mood=Ind Number=Plur Person=3 Tense=Past VerbForm=Fin
        "work" VERB Tense=Past VerbForm=Part
        "work" VERB Mood=Ind Number=Sing Person=1 Tense=Past VerbForm=Fin
"<in>"
        "in" SCONJ
        "in" ADP
        "in" ADV Degree=Pos
        "in" X
        "in" ADP Typo=Yes
"<the>"
        "the" DET Definite=Def PronType=Art
        "the" DET Definite=Def PronType=Art Typo=Yes
        "to" PART Typo=Yes
        "_" X
"<countryside>"
        "countryside" NOUN Number=Sing
"<economy>"
        "economy" NOUN Number=Sing
"<.>"
        "." PUNCT
        "." PUNCT Typo=Yes

```
