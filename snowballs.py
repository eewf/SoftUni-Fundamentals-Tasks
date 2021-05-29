n = int(input())
highest_value_ball = 0
best_snow = ""
best_time = ""
best_quality = ""
for i in range(n):
    snow = int(input())
    time = int(input())
    quality = int(input())
    value = (snow / time) ** quality
    if value > highest_value_ball:
        highest_value_ball = value
        best_snow = snow
        best_time = time
        best_quality = quality
print(f'{best_snow} : {best_time} = {round(highest_value_ball)} ({best_quality})')