import decimal

def list_od_bonuses(names: list[str], bets: list[int], rewards: list[str]) -> dict[str, decimal.Decimal]:
    result = {}
    for names, bets, rewards in zip(names, bets,rewards):
        result[names] = bets * decimal.Decimal(rewards[ : -1]) / 100
    return result
n = ['nadia', 'alex', 'boba']
b = [20000, 30000, 332]
c = ['5.5', '6.3', '7.1']
print(list_od_bonuses(n, b, c))




