import random
import re


class DiceThrower(object):
    def __init__(self, game_type):
        self.game_type = game_type

    def parse_dice_string(self, dice_string):

        dice_number = re.findall(r"(\d+)d", dice_string)
        dice_type = re.findall(r"d(\d+)", dice_string)
        dice_sign = re.findall(r"[\+\.][1-9]", dice_string)
        if dice_sign == []:
            dice_sign.append(0)

        dice_number_type = zip(dice_number, dice_type, dice_sign)

        result = self.launch_dice(dice_number_type)

        if self.game_type == "savage":
            if "cr" not in dice_string and "dm" not in dice_string:
                result.append(f"destiny dice -> {random.randrange(1, 7)}")

        return result

    def launch_dice(self, dice_number_type):

        result = []

        for number, d_type, d_sign in dice_number_type:
            print(f"{number},{d_type},{d_sign}")
            if number != None and d_type != None:

                for n in range(0, int(number)):
                    if d_type == "4":
                        dice_result = random.randrange(1, 5)
                    if d_type == "6":
                        dice_result = random.randrange(1, 7)
                    if d_type == "8":
                        dice_result = random.randrange(1, 9)
                    if d_type == "10":
                        dice_result = random.randrange(1, 11)
                    if d_type == "12":
                        dice_result = random.randrange(1, 13)
                    if d_type == "20":
                        dice_result = random.randrange(1, 21)

                    if d_sign != 0:
                        if '+' in d_sign:
                            print(dice_result)
                            result.append(dice_result +
                                          int(d_sign.replace("+", "")))
                        elif '-' in d_sign:
                            print(dice_result)
                            result.append(dice_result -
                                          int(d_sign.replace("-", "")))
                    else:
                        result.append(dice_result)
        return result
