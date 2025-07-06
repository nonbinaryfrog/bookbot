def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_sorted_dict(dict_char):
    dict_list = []
    for key in dict_char: 
        if key.isalpha():
            new_dict = {}
            new_dict["char"] = key
            new_dict["num"] = dict_char[key]
            dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=lambda d: d["num"])
    return dict_list