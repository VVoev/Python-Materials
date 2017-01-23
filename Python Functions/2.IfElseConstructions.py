num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

def f(x):
    return {
        'one': 1,
        'two': 2,
        'three':3,
        'four':4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine':9
    }[x]
print(f('eight'))