import random


def ran(n):
    
    n = int(input("enter your guess-->"))

    x = random.randint(0, 11)

    if n == x:
        print("Your guess is correct the element is", x)

    else:
        print("Your guess is wrong the element is ", x)
        ran(n)


print("")
n = int(input("enter your guess-->"))
ran(n)
