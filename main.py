def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input("Введите числа a и b (например, \"24 2\"): ").split())

result = gcd(a, b)

print("Наибольший общий делитель чисел", a, "и", b, "=", result)
