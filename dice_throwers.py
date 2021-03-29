import random
import re


class DiceThrower(object):
    def parse_dice_string(self, dice_string):
        dice_number = re.findall(r"(\d+)d", dice_string)
        dice_type = re.findall(r"d(\d+)", dice_string)
        dice_sign = re.findall(r"[\+\.][1-9]", dice_string)
        if dice_sign == []:
            for number in dice_number:
                dice_sign.append(0)

        dice_number_type = zip(dice_number, dice_type, dice_sign)
        result = self.launch_dice(dice_number_type)

        return result

    def launch_dice(self, dice_number_type):

        result = []

        for number, d_type, d_sign in dice_number_type:

            if number != None and d_type != None:
                total = 0
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

                    total += dice_result

                    result.append(f"raw dice -> {dice_result}")

                if d_sign != 0:
                    if '+' in d_sign:
                        result.append(
                            f"total with mod-> {total + int(d_sign.replace('+', ''))}"
                        )
                    elif '-' in d_sign:
                        result.append(
                            f"total with mod-> {total - int(d_sign.replace('+', ''))}"
                        )
                else:
                    result.append(f"total without mod -> {total}")

        return result


class SavageDiceThrower(DiceThrower):
    def parse_dice_string(self, dice_string):
        result = super().parse_dice_string(dice_string)

        if "cr" not in dice_string and "dm" not in dice_string:
            result.append(f"destiny dice -> {random.randrange(1, 7)}")

        return result


class DiceThrowerFactory(object):
    @staticmethod
    def create_thrower(game_type):
        if game_type == "Savage":
            return SavageDiceThrower()
        elif game_type == "Cthulhu":
            pass
