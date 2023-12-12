def word_count(text):
    return len(text.split())


def count_letters(text):
    freq = {}
    for c in text:
        c_lower = c.lower()
        if c_lower in freq:
            freq[c_lower] += 1
        else:
            freq[c_lower] = 1
    return freq


path = "books/frankenstein.txt"
text = ""
with open(path) as f:
    text = f.read()

print(f"--- Begin report of {path} ---")

print(f"{word_count(text)} words found in the document")
cl = count_letters(text)
for k, v in sorted(cl.items(), key=lambda x: x[1], reverse=True):
    if k.isalpha():
        print(f"The {k} character was found {v} times")
