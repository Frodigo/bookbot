def num_of_words(text: str) -> str:
    words = text.split()
    num_words = len(words)

    return f"Found {num_words} total words"

def count_characters(content: str) -> dict:
    char_dict = dict()
    for char in content:
        char  = char.lower()

        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def sort_dict(char_dict: dict) -> list[dict]:
    char_list = [{"char": char, "num": count} for char, count in char_dict.items()]
    sorted_list = sorted(char_list, key=lambda x: x["num"], reverse=True)

    return sorted_list
