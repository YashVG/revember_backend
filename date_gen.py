from random import choice
import random


date = '1945'
numbers = [date]
# add date to first index to show it's correct, then randomise when added to
# question queue in Flutter

difference = 15
lower_range = 10
upper_range = 30


def big_difference(date, difference):
    # check if absolute difference between rearranged dates is more than 15
    # only last two values are swapped, so only compare them
    if abs(int(date[len(date)-2:]) - int(date[len(date)-2:][::-1])) > difference:
        return True
    else:
        return False


# adding parameters bypass Python parameter error, and supercedes error handling
# therefore answer choices are generated without error messages
def rearrangment_method(user_input, l, u):
    # dates may be 3 or 2 numbers in length in special circumstances
    # hence list slicing and reversing last two char numbers
    final_date = user_input[:-2]
    last_numbers = [user_input[-2], user_input[-1]][::-1]
    for i in last_numbers:
        final_date += i
    return final_date


def randomiser_method(user_input, l, u):
    user_input = int(user_input)
    range_of_date = random.randint(l, u)
    return (user_input+range_of_date) or (user_input-range_of_date)


for i in range(1, 4):

    if big_difference(date, difference) == True:
        for i in range(3):
            numbers.append(randomiser_method(
                date, lower_range, upper_range))  # type: ignore

    else:
        # if rearrangement used, then remove from list and just randomise
        # else randomise if and until you rearrange the values
        fns = [randomiser_method, rearrangment_method]
        for i in range(3):
            if choice(fns) == 1:
                numbers.append(rearrangment_method(
                    date, lower_range, upper_range))
                fns.remove(rearrangment_method)
            else:
                if choice(fns) == 1:
                    numbers.append(choice(fns)(date))
                else:
                    numbers.append(choice(fns)(date, lower_range, upper_range))

    difference -= 4
    lower_range -= 5
    upper_range -= 5

answer_choices = [str(num) for num in numbers]
print(answer_choices)
