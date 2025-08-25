import sys
from utils import count_words

if __name__ == "__main__":
    file_name = "data.txt"
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    print(f"Worker received n={n}")
    result = count_words(file_name) * n
    print(f"Result: {result}")
