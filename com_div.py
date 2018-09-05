while True:
    from math import gcd
    i = input('Type in the two numbers you want to know the Greatest Common Divisor of. ')
    r = list(map(int, i.split(',')))
    result = gcd(r[0], r[1])
    print(result)
