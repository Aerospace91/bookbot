from collections import Counter

def get_num_words(book_string):
    word_lst = book_string.split()
    return len(word_lst)

def get_num_character(book_string):
    book_string = book_string.lower()
    return dict(Counter(book_string))