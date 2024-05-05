def main():
    book_path = "books/frankestein.txt"
    text = get_text(book_path)

    num_words = get_num_words(text)
    chars_dict = count_letters(text)
    print(f"--- Starting report of {book_path} ---")
    print(f"{num_words} words found within the document\n")
    sorted_chars_dict = sorted(chars_dict.items(), key=lambda x: x[1], reverse=True)
    print(sorted_chars_dict)

def get_num_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    chars = {}
    for c in text:
        c_lowered = c.lower()
        if c_lowered in chars:
            chars[c_lowered] += 1
        else:
            chars[c_lowered] = 1
    return chars
            
def get_text(path):
    with open(path) as f:
        return f.read()

main()