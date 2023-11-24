import sys
import jiwer

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip().split('\n')

def calculate_wer_line_by_line(reference_file, hypothesis_file):
    reference_lines = read_file(reference_file)
    hypothesis_lines = read_file(hypothesis_file)

    if len(reference_lines) != len(hypothesis_lines):
        print("Error: The number of lines in the reference and hypothesis files do not match.")
        sys.exit(1)

    wers = [jiwer.wer(ref, hyp) for ref, hyp in zip(reference_lines, hypothesis_lines)]
    return wers

def main():

    reference_file = sys.argv[1]
    hypothesis_file = sys.argv[2]

    line_wers = calculate_wer_line_by_line(reference_file, hypothesis_file)
    
    for i, wer in enumerate(line_wers, 1):
        print(f"Line {i} WER: {wer:.2f}")

if __name__ == "__main__":
    main()
