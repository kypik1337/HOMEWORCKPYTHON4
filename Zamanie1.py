
def print_word(text: str) -> None:
    words_list = sorted(text.split())
    max_len = len(max(words_list, key=len))
    

    for nn, word in enumerate(words_list, 1):
        print(f'{nn} {word:>{max_len}}')

print_word('Каждый охотник хочет знать, где сидит фазан')






