num_hours1 = int(input('Введите часы: '))
num_min1 = int(input('Введите минуты: '))
num_sec1 = int(input('Введите секунды: '))
num_hours2 = int(input('Введите часы: '))
num_min2 = int(input('Введите минуты: '))
num_sec2 = int(input('Введите секунды: '))
result1 = num_hours1*3600 + num_min1*60 + num_sec1
result2 = num_hours2*3600 + num_min2*60 + num_sec2
result3 = result2 - result1
print(result3)