def get_num_words(book_string):
    word_lst = book_string.split()
    return len(word_lst)

def get_num_character(book_string):
    book_string = book_string.lower()
    character_dict = {}
    for char in book_string:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict