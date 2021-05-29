import math

party_size = int(input())
days = int(input())
profit = 0
for day in range(1, days + 1):
    earning_per_day = 50 - 2 * party_size
    profit += earning_per_day
    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5
    if day % 3 == 0:
        profit -= 3 * party_size
    if day % 5 == 0:
        profit += 20 * party_size
    if day % 3 == 0 and day % 5 == 0:
        profit -= 2 * party_size

profit_per_man = math.floor(profit / party_size)

print(f'{party_size} companions received {profit_per_man} coins each.')
