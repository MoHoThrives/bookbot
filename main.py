from stats import count_words, count_chars, split_dict
import sys


def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    character_dict = count_chars(book_text)
    sorted_character_dict = split_dict(character_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzying book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    for d in sorted_character_dict:
        if not d["char"].isalpha():
            continue
        print(f"{d['char']}: {d['num']}")
    print("============= END ===============")
    
    
main()