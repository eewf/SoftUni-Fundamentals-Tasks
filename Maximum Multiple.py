import sys
divisor = int(input())
bound = int(input())
max_x = -sys.maxsize
for x in range(bound + 1):
    if x % divisor == 0:
        if 0 < x <= bound:
            max_x=x
print(max_x)
