quantity = int(input())
days = int(input())
ornament_set = 2  # dollars
tree_skirt = 5
tree_garlands = 3
tree_lights = 15
spend_money = 0
christmas_spirit = 0

for day in range(1, days+1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        spend_money += ornament_set * quantity
        christmas_spirit += 5
    if day % 3 == 0:
        spend_money += (tree_skirt + tree_garlands) * quantity
        christmas_spirit += 13
    if day % 5 == 0:
        spend_money += tree_lights * quantity
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit+=30
    if day % 10 == 0:
        christmas_spirit -= 20
        spend_money += (tree_skirt + tree_garlands + tree_lights)
if days % 10 ==0:
    christmas_spirit -= 30

print(f'Total cost: {spend_money}')
print(f'Total spirit: {christmas_spirit}')
