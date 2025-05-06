import sys
from stats import book_stats


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = sys.argv[1]
        book_stats(text)


main()
