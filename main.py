from dice_throwers import DiceThrowerFactory
from cli import type_list
import inquirer

ready = True
game_type = inquirer.prompt(type_list)
print(game_type)
dice_thrower = DiceThrowerFactory.create_thrower(game_type['game'])

while ready != False:
    dice = input("roll-> ")

    if dice == "exit" or dice == "EXIT":
        ready = False

    result = dice_thrower.parse_dice_string(dice)

    print(result)
