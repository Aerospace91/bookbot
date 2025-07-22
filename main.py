import sys
from stats import get_num_words, get_num_character, sort_dict

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_character(text)
    sorted_char = sort_dict(num_char)
    
    print("\n============ BOOKBOT ============\n")
    print(f"Analyzing book found at {book_path}\n")
    print("----------- Word Count ----------\n")
    print(f"Found {num_words} total words\n")
    print("--------- Character Count -------\n")
    for char in sorted_char:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}\n")
    print("============= END ===============")    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
    
main()