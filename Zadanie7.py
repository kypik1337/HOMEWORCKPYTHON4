


def my_lambda(cur_list):
    return sum(cur_list) > 0

# def final_income(my_dict: dict[str, list[int | float]]) -> bool:
#     return all(map(lambda x: sum(x) > 0 , my_dict.values()))


def final_income(my_dict: dict[str, list[int | float]]) -> bool:
    return all([sum(cur_list) > 0 for cur_list in my_dict.values()])







