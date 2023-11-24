# MaxMatch Tokenization for Japanese Text
This README provides an overview of the MaxMatch algorithm's implementation and performance for tokenizing Japanese text using the Universal Dependencies (UD) Japanese GSD Treebank.

## Implementation
The MaxMatch algorithm is a simple, left-to-right longest-match algorithm used for tokenizing text, particularly effective for languages like Japanese that do not use spaces to separate words.

### Usage Instructions
Clone the UD Treebank Repository:

`1.` Clone the UD Treebank Repository:
```bash
git clone https://github.com/UniversalDependencies/UD_Japanese-GSD
cd UD_Japanese-GSD
```
`2.` Extract a Dictionary:
```
bash
Copy code
awk '$0 !~ /^#/ && NF > 1 {print $2}' ja_gsd-ud-train.conllu | sort | uniq > dictionary.txt
```

`3.` Run MaxMatch Algorithm:

Python script **maxmatch.py** reads sentences from standard input, tokenizes them using the dictionary, and outputs words separated by newlines.
Example:
```bash
Copy code
cat original_sentence.txt | python maxmatch.py dictionary.txt > tokenized_output.txt
```

`4.` Calculate Word Error Rate (WER):

Use a Python script with the jiwer library to calculate WER.
Example:
```bash
Copy code
python wer.py original_sentence.txt tokenized_output.txt
```

## Performance Evaluation
The MaxMatch algorithm's performance was evaluated based on WER. The WER values ranged from 7% to 40%, indicating varying levels of accuracy across different sentences. You can find the WER for all the lines in **percentage.txt** file


### Examples

- **Successful Segmentation (Low WER):**
  - **Original**: "先生の理想は限りなく高い。"
  - **Segmented**: "先生 の 理想 は 限りなく 高い 。"
  - **WER**: 7%
  - **Analysis**: Accurate segmentation with low error rate.

- **Problematic Segmentation (High WER):**
  - **Original**: "そうだったらいいなあとは思いますが,日本学術会議の会長談話について“当会では,標記の件について,以下のように考えます。”"
  - **Segmented**: "そう だっ たら いい なあ と は 思い ます が , 日本 学術 会議 の 会長 談話 に つい て “ 当会 で は , 標記 の 件 に つい て , 以下 の よう に 考え ます 。 ”"
  - **WER**: 40%
  - **Analysis**: Struggled with complex structures leading to high error rate.

### General Observations
* The algorithm performs better with simpler sentences.
* Higher WERs are often associated with complex sentence structures.
* Rule-based and non-contextual, MaxMatch can face limitations with context-sensitive segmentation.