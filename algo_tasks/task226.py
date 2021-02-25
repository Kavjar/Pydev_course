import math


def lcm(a, b):
    return (a * b) // math.gcd(a, b)


result = []
print("Enter n and m:")
try:
    n, m = input().split()
    if n.isdigit() and m.isdigit():
        n, m = int(n), int(m)
        lcm = lcm(n, m)
        for i in range(lcm, n * m, lcm):
            result.append(i)
        if not len(result):
            print("There are no such values")
        else:
            print("All common multiples less then {}: ".format(n * m), end='')
            for el in result:
                print(el, end=', ')
    else:
        print("You've entered not natural number")
except ValueError:
    print("Please enter the second value")
