from random import randint


def boardinggames(how_many_dice, type_of_dice=6, modification_value=0):
    dicetype = [3, 4, 6, 8, 10, 12, 100]
    numofroll = []
    try:
        if type_of_dice not in dicetype:
            raise Exception
        for x in range(how_many_dice):
            numofroll.append(randint(1, how_many_dice))
        return sum(numofroll) + modification_value
    except Exception:
        print("Choose another type of dice")
        return None


def string_for_function(description):
    try:
        how_many_dice = int(description.split("D")[0])
        if "+" in description:
            type_of_dice = int(description.split("D")[1].split("+")[0])
            modification_value = int(description.split('+')[1])
        elif "-" in description:
            type_of_dice = int(description.split('D')[1].split('-')[0])
            modification_value = -1 * int(description.split('-')[1])
        else:
            type_of_dice = int(description.split('D')[1])
            modification_value = 0
            print(how_many_dice, type_of_dice, modification_value)
        return boardinggames(how_many_dice, type_of_dice=6, modification_value=0)
    except ValueError:
        print("Check value and try again")
    return None
