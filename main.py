from stats import get_num_words, count_letters, report
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    s = get_book_text(book_path)
    num_words = get_num_words(s)
    #print(f"{num_words} words found in the document")
    letter_count = count_letters(s)
    #print(f"{letter_count}")
    report(book_path, num_words, letter_count)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()