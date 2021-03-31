from dice_throwers import DiceThrowerFactory, SavageDiceThrower, Cthulhu
from collections import Counter


def test_create_SavageThrower():
    dice_thrower = DiceThrowerFactory.create_thrower("Savage")
    assert isinstance(dice_thrower, SavageDiceThrower)


def test_create_CthulhuThrower():
    dice_thrower = DiceThrowerFactory.create_thrower("Cthulhu")
    assert isinstance(dice_thrower, CthulhuDiceThrower)


def test_result_is_list(game_type):
    dice_thrower = DiceThrowerFactory.create_thrower(game_type)
    result = dice_thrower.parse_dice_string("1d6")

    assert isinstance(result, list) == True


def test_has_destinyDice(game_type):
    dice_thrower = DiceThrowerFactory.create_thrower(game_type)
    result = dice_thrower.parse_dice_string("1d6")
    assert any("destiny dice" in string for string in result)


def test_check_total_without_mod(game_type):
    dice_thrower = DiceThrowerFactory.create_thrower(game_type)
    result = dice_thrower.parse_dice_string("2d6")
    assert any("total without mod" in string for string in result)
    assert sum('total without mod' in string for string in result) == 1


def test_check_total_with_mod(game_type):
    dice_thrower = DiceThrowerFactory.create_thrower(game_type)
    result = dice_thrower.parse_dice_string("2d6+1")
    assert any("total with mod" in string for string in result)
    assert sum('total with mod' in string for string in result) == 1


def test_multiple_dice_type_without_mod(game_type):
    dice_thrower = DiceThrowerFactory.create_thrower(game_type)
    result = dice_thrower.parse_dice_string("2d6+1 2d4")
    assert any("total with mod" in string for string in result)
    assert sum('total with mod' in string for string in result) == 1


def test_multiple_dice_type_with_mod(game_type):
    dice_thrower = DiceThrowerFactory.create_thrower(game_type)
    result = dice_thrower.parse_dice_string("2d6+1 2d3+1")
    assert any("total with mod" in string for string in result)
    assert sum('total with mod' in string for string in result) >= 2


def test_cthulhu_action_dice(game_type):
    dice_thrower = DiceThrowerFactory.create_thrower("Cthulhu")
    result = dice_thrower.parse_dice_string("action"):
    assert any("result -> " in result)
    