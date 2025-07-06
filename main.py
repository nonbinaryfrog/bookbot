from stats import get_num_words, get_chars_dict, get_sorted_dict
import sys


def main():
#    book_path = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_dict = get_sorted_dict(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key in sorted_dict:
        print(f'{key["char"]}: {key["num"]}')


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
