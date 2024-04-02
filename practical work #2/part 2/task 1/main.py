print("Введите переменную t")
t = float(input())

a = t 
b = - 3 * (t-1)
c = t + 4

D = b ** 2 - 4 * a * c 
if D > 0:
    x1 = (-b + D**(1/2)) / 2 * a
    x2 = (-b - D**(1/2)) / 2 * a  
    print("x1 = ", x1)
    print("x2 = ", x2)
elif D == 0:
    x = -b / (2*a)
    print("x = ", x)
elif D < 0:
    print("Корней нет")
