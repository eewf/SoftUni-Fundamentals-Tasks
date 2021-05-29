age = int(input())
drink = " "
if age <= 14:
    person = "Kid"
    drink = "toddy"
elif 14 < age <= 18:
    person = "Teen"
    drink = "coke"
elif 18 < age <= 21:
    person = 'Young adult'
    drink = "beer"
else:
    person = 'Adult'
    drink = "whisky"
print(f'drink {drink}')
