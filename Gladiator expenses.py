lost_fight = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())
expenses = 0
shield_break = 0

for i in range(1, lost_fight + 1):
    if i % 2 == 0:
        expenses += helmet
    if i % 3 == 0:
        expenses += sword
    if i % 2 == 0 and i % 3 == 0:
        expenses += shield
        shield_break += 1
        if shield_break % 2 == 0:
            expenses += armor

print(f'Gladiator expenses: {expenses:.2f} aureus')
