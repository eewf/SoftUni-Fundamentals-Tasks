budget = float(input())
flour = float(input())
colored_eggs = 0
pack_eggs = flour * 0.75
price_of_milk = flour * 1.25
needed_milk = price_of_milk / 4  # Needed milk is 0.250l
cozonac = pack_eggs + flour + needed_milk
cozonacs_quantity = 0
lost_eggs=0
while budget > cozonac:
    budget -= cozonac
    cozonacs_quantity += 1
    colored_eggs+=3
    if cozonacs_quantity % 3 == 0:
        colored_eggs-=cozonacs_quantity-2


print(f'You made {cozonacs_quantity} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
