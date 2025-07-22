def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"{word_count(text)} words found in the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(book_string):
    word_lst = book_string.split()
    return len(word_lst)

main()

