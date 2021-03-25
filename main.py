from dice_throwers import DiceThrower

ready = True
game_type = "savage"

dice_thrower = DiceThrower()

while ready != False:
    dice = input("roll-> ")

    if dice == "exit" or dice == "EXIT":
        ready = False

    result = dice_thrower.parse_dice_string(dice)

    print(result)
