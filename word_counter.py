import sys
from utils import count_words

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python word_counter.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    word_count = count_words(input_file)

    with open(output_file, "w") as f:
        f.write(f"Word count for {input_file}: {word_count}\n")

    print(f"✅ Worker finished. Result written to {output_file}")
