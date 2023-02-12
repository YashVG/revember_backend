from random import choice
import random


# date = '1945'
# numbers = [date]
# add date to first index to show it's correct, then randomise when added to
# question queue in Flutter


def big_difference(date, difference):
    date2 = str(date)
    # check if absolute difference between rearranged dates is more than difference
    # only last two values are swapped, so only compare them

    # if abs(int(str(date[len(str(date))-2:])) - int(str(date[len(str(date))-2:][::-1]))) > difference:
    #     return True
    # else:
    #     return False
    if abs(int(date2[len(date2)-2:]) - int(date2[len(date2)-2:][::-1])) > difference:
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


def generate_easy_dates(date):
    no_list = [date]
    if big_difference(int(date), 15) == True:
        for i in range(3):
            no_list.append(randomiser_method(
                date, 10, 30))  # type: ignore

    else:
        # if rearrangement used, then remove from list and just randomise
        # else randomise if and until you rearrange the values
        fns = [randomiser_method, rearrangment_method]
        for i in range(3):
            if choice(fns) == 1:
                no_list.append(rearrangment_method(
                    date, 10, 30))
                fns.remove(rearrangment_method)
            else:
                if choice(fns) == 1:
                    no_list.append(choice(fns)(date))
                else:
                    no_list.append(choice(fns)(
                        date, 10, 30))
    return no_list


def generate_medium_dates(date):
    no_list = [date]
    if big_difference(int(date), 10) == True:
        for i in range(3):
            no_list.append(randomiser_method(
                date, 7, 20))  # type: ignore
    else:
        # if rearrangement used, then remove from list and just randomise
        # else randomise if and until you rearrange the values
        fns = [randomiser_method, rearrangment_method]
        for i in range(3):
            if choice(fns) == 1:
                no_list.append(rearrangment_method(
                    date, 7, 20))
                fns.remove(rearrangment_method)
            else:
                if choice(fns) == 1:
                    no_list.append(choice(fns)(date))
                else:
                    no_list.append(choice(fns)(
                        date, 7, 20))
    for i in no_list:
        i = str(i)
    return no_list


def generate_hard_dates(date):
    no_list = [date]
    if big_difference(int(date), 5) == True:
        for i in range(3):
            no_list.append(randomiser_method(
                date, 5, 15))  # type: ignore
    else:
        # if rearrangement used, then remove from list and just randomise
        # else randomise if and until you rearrange the values
        fns = [randomiser_method, rearrangment_method]
        for i in range(3):
            if choice(fns) == 1:
                no_list.append(rearrangment_method(
                    date, 5, 15))
                fns.remove(rearrangment_method)
            else:
                if choice(fns) == 1:
                    no_list.append(choice(fns)(date))
                else:
                    no_list.append(choice(fns)(
                        date, 5, 15))
    for i in no_list:
        i = str(i)
    return no_list


# answer_choices = [str(num) for num in numbers]
# print(answer_choices)
