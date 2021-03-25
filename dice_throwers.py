import random
import re


class DiceThrower(object):
    """
  docstring
  """
    def parse_dice_string(self, dice_string):

        dice_number = re.findall(r"(\d+)d", dice_string)
        dice_type = re.findall(r"d(\d+)", dice_string)
        dice_number_type = zip(dice_number, dice_type)

        result = self.launch_dice(dice_number_type)

        return result

    def launch_dice(self, dice_number_type):

        result = []

        for number, d_type in dice_number_type:

            if number != None and d_type != None:
                for n in range(0, int(number)):
                    if d_type == "4":
                        result.append(random.randrange(1, 5))
                    if d_type == "6":
                        result.append(random.randrange(1, 7))
                    if d_type == "8":
                        result.append(random.randrange(1, 9))
                    if d_type == "10":
                        result.append(random.randrange(1, 11))
                    if d_type == "12":
                        result.append(random.randrange(1, 13))
                    if d_type == "20":
                        result.append(random.randrange(1, 21))

        return result
