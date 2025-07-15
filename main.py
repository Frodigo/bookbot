from stats import num_of_words, count_characters, sort_dict
import sys

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("'Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    content = get_book_text(sys.argv[1])
    print(num_of_words(content))
    counted = count_characters(content)
    report_list = sort_dict(counted)
    print("--------- Character Count -------")

    for item in report_list:
        char = item["char"]
        count = item["num"]

        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")



main()
