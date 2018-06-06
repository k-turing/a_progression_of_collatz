#collatz

def collatz(number):
    while number != 1:
        if number % 2 == 0:
            return int(number / 2)
        else:
            return int(3 * number + 1)

try:
    number = int(input("put a integer"))
    if number == 1:
        print("it's aleady 1")
    else:
        while number != 1:
            number = collatz(number)
            print(number)

except ValueError:
    print("you have to put integer")            