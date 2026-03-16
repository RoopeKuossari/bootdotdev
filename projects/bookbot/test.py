def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def words_in_book(book_text):
    char = book_text.lower()
    
    return char

def main():
    file = "./books/frankenstein.txt"
    book_text = get_book_text(file)
    word_count = words_in_book(book_text)
    character_count = words_in_book(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(word_count)
    print("--------- Character Count -------")
    for char in character_count:
        print(f"{char}: {character_count[char]}")
    print("============= END ===============")


if __name__ == "__main__":
    main()