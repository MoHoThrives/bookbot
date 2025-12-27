def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def split_dict(char_dict):
    def sort_on(items):
        return items["num"]
    
    dict_list = []
    for char, count in char_dict.items():
        dict_list.append({"char" : char, "num": count})
    
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
    