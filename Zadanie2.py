

def uni_list (text: str) -> list[int]:
    result = []
    for symbol in set(text):
        result.append(ord(symbol))

    return sorted(result, reverse=True)

uni_list('Каждый охотник хочет знать, где сидит фазан')
