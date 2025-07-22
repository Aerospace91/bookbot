from collections import Counter

def get_num_words(book_string):
    word_lst = book_string.split()
    return len(word_lst)

def get_num_character(book_string):
    book_string = book_string.lower()
    return dict(Counter(book_string))

def sort_dict(char_dict):
    char_lst = []
    def sort_on(items):
        return items["num"]
    
    for char in char_dict:
        char_lst.append({"char": char, "num": char_dict[char]})
    
    char_lst.sort(reverse=True, key=sort_on)
    return char_lst