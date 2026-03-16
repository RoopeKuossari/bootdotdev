import sys
from stats import words_in_book, count_characters_in_book, sorted_list_of_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = sys.argv[1]
    book_text = get_book_text(file)
    word_count = words_in_book(book_text)
    character_count = count_characters_in_book(book_text)
    sorted_count = sorted_list_of_count(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(word_count)
    print("--------- Character Count -------")
    for char, num in sorted_count:
        print(f"{char}: {num}")
    print("============= END ===============")



if __name__ == "__main__":
    main()