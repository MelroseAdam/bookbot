from stats import count_words
from stats import count_characters
from stats import sort_characters
import sys


def main():
    full_book = get_book_text(f"{sys.argv[1]}")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(full_book)} total words")
    print("--------- Character Count -------")
    unsorted_characters = (count_characters(full_book))
    sorted_final_dict = sort_characters(unsorted_characters)
    for final_sorted in sorted_final_dict:
        print(f"{final_sorted["char"]}: {final_sorted["num"]}")
    print("============= END ===============")

def get_book_text(text):
    with open(f"{text}") as t:
        book_contents = t.read()
    return book_contents


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()
