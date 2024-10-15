def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_counts = count_characters(text)

    print("----- Begin of Report -----")
    print(f"there are {num_words} words in the document")
    print_char_report(char_counts)
    print("----- End of Report -----")

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    import string
    lowercase = text.lower()
    # Only consider letters a-z
    letters = string.ascii_lowercase
    char_dict = {}
    char_dict = {char: lowercase.count(char) for char in letters if char in lowercase}
    return  char_dict

def print_char_report(char_counts):
    # Sort the characters in revers Order
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_chars[:]:
        print(f"The '{char}' character was found {count} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()



main()