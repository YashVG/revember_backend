from random import choice
import random


date = '1945'
numbers = [date]
# add date to first index to show it's correct, then randomise when added to
# question queue in Flutter


def big_difference(date):
    # check if absolute difference between rearranged dates is more than 15
    # only last two values are swapped, so only compare them
    if abs(int(date[len(date)-2:]) - int(date[len(date)-2:][::-1])) > 15:
        return True
    else:
        return False


def rearrangment_method(user_input):
    # dates may be 3 or 2 numbers in length in special circumstances
    # hence list slicing and reversing last two char numbers
    final_date = user_input[:-2]
    last_numbers = [user_input[-2], user_input[-1]][::-1]
    for i in last_numbers:
        final_date += i
    return final_date


def randomiser_method(user_input):
    user_input = int(user_input)
    rnge_of_date = random.randint(5, 20)
    return user_input+rnge_of_date or user_input-rnge_of_date


if big_difference(date) == True:
    for i in range(3):
        numbers.append(randomiser_method(date))  # type: ignore

else:
    fns = [rearrangment_method, randomiser_method]
    for i in range(3):
        if choice(fns) == rearrangment_method:
            numbers.append(choice(fns)(date))
            fns.remove(rearrangment_method)
        else:
            numbers.append(choice(fns)(date))

answer_choices = [str(num) for num in numbers]
print(answer_choices)
