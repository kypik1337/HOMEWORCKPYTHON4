
def sorting_list (my_list: list[int]):
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list [i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                not_sorted = True
    




    pass



data_list = [8, 15, 22, 1, 23, 44, 55, 17]
print(sorting_list(data_list))

