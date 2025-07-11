def get_word_count(text: str) -> int:
    return len(text.split())

def get_char_counts(text: str) -> dict[str, int]:
    text = text.lower()
    char_count = {}
    for c in text:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1
    
    return char_count

def get_sorted_chars(char_counts: dict[str, int]) -> list[dict]:
    sorted_chars = []
    for char, count in char_counts.items():
        if char.isalpha():
            sorted_chars.append({"char": char, "num": count})

    sorted_chars.sort(reverse=True, key=lambda x: x["num"])
    return sorted_chars
