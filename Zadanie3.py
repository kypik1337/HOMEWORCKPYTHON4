def renge_unicode (text: str) -> dict[str, int]:
    first, second = map(int, text.split())
    result = {}
    for number in range(min(first, second), max(first, second) + 1):
        result [chr(number)] = number

    return result


print(renge_unicode('1 10'))