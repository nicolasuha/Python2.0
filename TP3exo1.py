def Somme():
    print("Please enter a integer: ")
    x = int(input())
    s = 0
    for i in range(x):
        s += x
        x -= 1
    print(s)


def Wait():
    x = int(input("Please, enter a integer: "))
    while x != 100:
        x = int(input("Please, enter a integer: "))


def numbSorting():
    ten = 0
    fifteen = 0
    twenty = 0
    for i in range(9):
        value = int(input(f"Please enter the {i + 1} integer: "))
        while value < 0 or value > 20:
            value = int(input(f"Please enter the {i + 1} integer: "))
        if 0 <= value < 10:
            ten += 1
        elif 10 <= value < 15:
            fifteen += 1
        elif 15 <= value <= 20:
            twenty += 1
        else:
            raise TypeError("Ton algo est faux FDP")
    print(f"There are: {ten} values in the interval [0;10[, {fifteen} in the interval [10;15[ and {twenty} in the "
          f"interval [15;20]")


def XSumCalculator():
    x = int(input("Please, enter an integer > 1 : "))
    n = 1
    s = 0
    while s <= x:
        s += n
        n += 1
    print("The largest valid number is", n - 2)
XSumCalculator()