def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    num_words = word_count(book)
    chars_dict = letter_count(book)
    chars_sorted_list = chars_sorted_list_dict(chars_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    
    for item in chars_sorted_list:
        print(f"The '{item["char"]}' character was found {item["num"]} times")
    print("--- End report ---")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(book):
    words = book.split()
    return len(words)

def letter_count(book):
    letters = {}
    book_lower = book.lower()
    for c in book_lower:
        if c in letters:
            letters[c] += 1
        elif c.isalpha():
            letters[c] = 1
            
    return letters

def sort_on(d):
    return d["num"]

def chars_sorted_list_dict(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "num": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()