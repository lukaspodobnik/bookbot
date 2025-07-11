import sys
from stats import get_word_count, get_char_counts, get_sorted_chars

def get_book_text(path: str) -> str:
    with open(path) as f:
        book_text = f.read()
    
    return book_text

def print_report(book_path: str, word_count: int, sorted_chars: list[dict]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_count in sorted_chars:
        print(f"{char_count['char']}: {char_count['num']}")

    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    char_counts = get_char_counts(book_text)
    sorted_chars = get_sorted_chars(char_counts)

    print_report(book_path, word_count, sorted_chars)

main()