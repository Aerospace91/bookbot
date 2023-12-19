
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    letter_dict = count_letters(text)
    letter_sorted_list = letters_dict_to_sorted_list(letter_dict)
        
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    
    for item in letter_sorted_list:
        if not item["letter"].isalpha():
            continue
        print(f"The '{item['letter']}' letter was found {item['num']} times")
    print("--- End report ---")
        
def word_count(text):
    return len(text.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_letters(text):
    letter_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in letter_dict:
            letter_dict[lowered] += 1
        else:
            letter_dict[lowered] = 1
    return letter_dict
    
def sort_on(d):
    return d["num"]
    
def letters_dict_to_sorted_list(num_letters_dict):
    sorted_list = []
    for ch in num_letters_dict:
        sorted_list.append({"letter": ch, "num": num_letters_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    

main()