def count_words(all_words):
    split_words = all_words.split()
    return len(split_words)

def count_characters(all_words):
    character_dict = {}
    lower_words = all_words.lower()
    for x in lower_words:
        if x not in character_dict:
            character_dict[f"{x}"] = 1
        else:
            character_dict[f"{x}"] += 1
    return character_dict

def sort_on(items):
    return items["num"]


def sort_characters(letter_dictionary):
    
    list_dicts = []
    for letter in letter_dictionary:
        sorter_dict = {}
        count = letter_dictionary[letter]
        sorter_dict["char"] = letter
        sorter_dict["num"] = count
        if letter.isalpha() == False:
            pass
        else:
            list_dicts.append(sorter_dict)
    list_dicts.sort(reverse=True, key=sort_on)

    return list_dicts
    









# letter_list.append(f"char: {letter}, num: {letter_dictionary[letter]}")
