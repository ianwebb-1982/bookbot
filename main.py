from stats import count_words
from stats import num_of_characters
from stats import sort_dictionary
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        book = f.read()
    return book

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    text = get_book_text(sys.argv[1])
    num_of_words = count_words(text)
    #print(f"Found {num_of_words} total words")
    char_counts = num_of_characters(text)   
    #print(char_counts)
    sorted_chars = sort_dictionary(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()