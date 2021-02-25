print("Enter n and m:")
try:
    string_n, m = input().split()
    sum, quantity = 0, int(m)
    if string_n.isdigit():
        if len(string_n) > quantity:
            for digit in list(string_n[:len(string_n) - int(quantity) - 1:-1]):
                sum += int(digit)
            print("The sum of the last {} digits of number {} is".format(quantity, string_n), sum)
        elif len(string_n) == quantity:
            for digit in string_n:
                sum += int(digit)
            print("The sum of the last {} digits of number {} is".format(quantity, string_n), sum)
        else:
            print("m must be less than number of digits n")
    else:
        print("You've entered not natural number")
except ValueError:
    print("Please enter the second value")

