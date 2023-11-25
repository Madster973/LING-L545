
# Telugu Noun Morphotactics with HFST

This project involves creating a finite-state transducer (FST) for basic morphotactics of Telugu nouns using the Helsinki Finite-State Technology (HFST) toolkit. It covers the generation of different grammatical cases (nominative, accusative, dative, and genitive) for a set of Telugu nouns.

## Overview

The `.lexc` file in this repository defines the morphological rules for 20 Telugu nouns. These rules are used to generate various forms of each noun, based on the required grammatical case.

## Nouns Covered

The following 20 Telugu nouns are included in the `.lexc` file:

1. ఆకాశం (aakaasham - sky)
2. సూర్యుడు (sooryudu - sun)
3. చంద్రుడు (chandrudu - moon)
4. తార (taara - star)
5. పువ్వు (puvvu - flower)
6. వృక్షం (vruksham - tree)
7. కలం (kalam - pen)
8. పర్వతం (parvatam - mountain)
9. నావ (naava - boat)
10. విమానం (vimaanam - airplane)
11. బస్సు (bassu - bus)
12. పక్షి (pakshi - bird)
13. మేఘం (megham - cloud)
14. వర్షం (varsham - rain)
15. నది (nadi - river)
16. సముద్రం (samudram - ocean)
17. పాఠశాల (paathashaala - school)
18. ఆసుపత్రి (aasupatri - hospital)
19. ఉద్యోగం (udyogam - job)
20. ఆహారం (aahaaram - food)

## File Structure

- `tel.lexc`: Contains the lexical rules for the Telugu nouns.


## Compiling the Lexicon

To compile the `.lexc` file into an HFST transducer, run the following command in your terminal:

```bash
hfst-lexc tel.lexc -o tel.hfst
```

## Generating The FST 

```bash
hfst-fst2txt tel.lexc.hfst | python3 att2dot.py  | dot -Tpng -o tel.lexc.png
```

The above command would be generating a png file which consists of FST diagram.


