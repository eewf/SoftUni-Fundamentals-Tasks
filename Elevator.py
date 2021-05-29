import math

people = int(input())
elevator_capacity = int(input())

run = math.ceil(people / elevator_capacity)
print(run)
