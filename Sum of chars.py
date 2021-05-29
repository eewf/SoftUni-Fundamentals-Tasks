n = int(input())
total = 0
for i in range(n):
    symbol = input()
    char = ord(symbol)
    total += char
print(f"The sum equals: {total}")
