def power(base, exp):
    if exp == 1:
        return base
    else:
        return (base * power(base, exp-1))

base = int(input("Enter a base: "))
exp = int(input("Enter a exponent: "))
result = power(base,exp)
print('result',result)