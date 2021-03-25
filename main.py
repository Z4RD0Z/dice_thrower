import random

ready = True

while ready != False:
    dice = input("roll-> ")

    if dice == "exit" or dice == "EXIT":
        ready = False

    numbers = dice.split('d')
    result = []

    print(numbers[0])

    for number in numbers[0]:
        if "d6" in dice:
            result.append(f"{random.randrange(1, 7)}, ")

    print(result)
