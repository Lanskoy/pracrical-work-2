print("Введите число от -11 до -5 или от 1 до 2")

x = float(input())

if x >= -11 and x < -5 or x > 1 and x < 2:
    print("Х попал в промежуток")
else:
    print("X не попал в промежуток")