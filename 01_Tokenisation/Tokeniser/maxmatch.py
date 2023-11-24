import sys

def maxmatch(text, dictionary):
    if not text:
        return []

    for i in range(len(text), 0, -1):
        first_word = text[:i]
        remainder = text[i:]

        if first_word in dictionary:
            return [first_word] + maxmatch(remainder, dictionary)

    return [text[0]] + maxmatch(text[1:], dictionary)

def main():

    dictionaryfile = sys.argv[1]

    # Read the dictionary file
    try:
        with open(dictionaryfile, 'r') as file:
            dictionary = set(file.read().splitlines())
    except FileNotFoundError:
        print(f"Dictionary file not found: {dictionaryfile}")
        sys.exit(1)

    # Process each line from standard input
    for line in sys.stdin:
        line = line.strip()
        tokens = maxmatch(line, dictionary)
        print(" ".join(tokens))

if __name__ == "__main__":
    main()
