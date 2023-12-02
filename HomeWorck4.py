# 1. Напишите функцию для транспонирования матрицы
# my_matrix = [[1, 2, 3, 4], [10, 20, 30, 40], [100, 200, 300, 400]]
# def transponir(matrix):
#     new_matrix = []
#     for i in range(len(matrix[0])):
#         new_matrix.append(list())
#         for j in range(len(matrix)):
#             new_matrix[i].append(matrix[j][i])
#     return new_matrix


# print(transponir(my_matrix))


# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.
# def create_argument_dict(**args) -> dict:
#     argument_dict = {}
#     for key, value in args.items():
#         try:
#             hash(value)
#         except TypeError:
#             value = str(value)
#         argument_dict[value] = key
#     return argument_dict


# result = create_argument_dict(args1='value', args2=[1, 4, 6], args3={4: 3, '2': 'One'})
# print(result)
# 3. Возьмите задачу о банкомате из семинара 
# 2. Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


import decimal
decimal.getcontext().prec = 2
CMD_DEPOSIT = 'p'
CMD_WITHDRAW = 's'
CMD_EXIT = 'e'
RICHNESS_SUM = decimal.Decimal(5_000_000)
RICHNESS_PRECENT = decimal.Decimal(10) / decimal.Decimal(100)
WITHDRAW_PRECENT = decimal.Decimal(15) / decimal.Decimal(1000)
ADD_PRECENT = decimal.Decimal(3) / decimal.Decimal(100)
MULTIPLACITY = 50
MIN_REMOVAL = 30
MAX_REMOVAL = 600
COUNT_OPER = 3
LOG = []
LOG_COMMAND = 'l'


account = decimal.Decimal(0)
count_operacion = 0

while True:
    command = input(f' Лог по лицевомцу счету - {LOG_COMMAND} Пополнить - {CMD_DEPOSIT}, Снять - {CMD_WITHDRAW}, Выйти - {CMD_EXIT}:= ')
    if command == LOG_COMMAND:
        print(LOG)
    if command == CMD_EXIT:
        print(f'Возьмите карту, на которой:={account} y.e.')
        break
    if account > RICHNESS_SUM:
        percrnt = account * RICHNESS_PRECENT
        account -= percrnt
        print(f' Вычтен налог на верхний предел богатства:={percrnt}, y.e.  \n' 
            f'На остатке:={account}')
        LOG.append(account)
    if  command in (CMD_DEPOSIT, CMD_WITHDRAW):
        ammaunt = 1
        while ammaunt % 50 != 0:
            ammaunt = int(input(f' Введите суммуб кратную {MULTIPLACITY}:= '))
    if command == CMD_DEPOSIT:
        account += ammaunt
        count_operacion += 1
        print(f'пополнение карты на := {ammaunt},  на карте {account} денег.')
        LOG.append(account)
    elif command == CMD_WITHDRAW:
        withdraw_tax = ammaunt * WITHDRAW_PRECENT
        withdraw_tax = (MIN_REMOVAL if withdraw_tax < MIN_REMOVAL else
                        MAX_REMOVAL if withdraw_tax > MAX_REMOVAL else withdraw_tax)
        if account >= ammaunt + withdraw_tax:
            count_operacion += 1
            account -= (ammaunt + withdraw_tax)
            print(f'Снятие с карты {ammaunt} y.e. \n Коммиссия за снятие {withdraw_tax}\n'
                  f'На карте осталось {account}y.e')
            LOG.append(account)
        else:
            print(f' Недостаточно средств для выполнения операции \n'
                  f'Сумма снятия {ammaunt}y.e., Коммиссия за перевод {withdraw_tax}\n'
                  f'На карте осталось {account} y.e.')
            LOG.append(account)
    if count_operacion and count_operacion % COUNT_OPER == 0:
        bonus_percent = account * ADD_PRECENT
        account += bonus_percent
        print(f'На сч>т начислено {ADD_PRECENT} % {bonus_percent} y.e.\n'
              f' Итого на карте {account} y.e.')
        LOG.append(account)







