def count_words(filename):
    with open(filename, "r") as f:
        text = f.read()
    words = text.split()
    return len(words)
