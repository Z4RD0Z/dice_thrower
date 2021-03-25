from dice_throwers import DiceThrowerFactory

ready = True
game_type = "savage"

dice_thrower = DiceThrowerFactory.create_thrower(game_type)

while ready != False:
    dice = input("roll-> ")

    if dice == "exit" or dice == "EXIT":
        ready = False

    result = dice_thrower.parse_dice_string(dice)

    print(result)
