def words_in_book(book_text):
    words = book_text.split()
    count = len(words)
    return f"Found {count} total words"

def count_characters_in_book(book_text):
    lower = book_text.lower()
    count = {}
    for char in lower:
        if not char.isalpha():
            continue

        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def sorted_list_of_count(count):
    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return sorted_count
