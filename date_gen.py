from random import choice
import random


# add date to first index to show it's correct, then randomise when added to
# question queue in Flutter


def big_difference(date, difference):
    date2 = str(date)
    # check if absolute difference between rearranged dates is more than difference
    # only last two values are swapped, so only compare them

    if abs(int(date2[len(date2)-2:]) - int(date2[len(date2)-2:][::-1])) > difference:
        return True
    else:
        return False

# adding parameters bypass Python parameter error, and supercedes error handling
# therefore answer choices are generated without error messages


def rearrangment_method(userInput, l, u):
    # dates may be 3 or 2 numbers in length in special circumstances
    # hence list slicing and reversing last two char numbers
    finalDate = userInput[:-2]
    lastNumbers = [userInput[-2], userInput[-1]][::-1]
    for i in lastNumbers:
        finalDate += i
    return finalDate


def randomiser_method(userInput, l, u):
    userInput = int(userInput)
    rangeOfDate = random.randint(l, u)
    return (userInput+rangeOfDate) or (userInput-rangeOfDate)


def generate_easy_dates(date):
    noList = [date]
    if big_difference(int(date), 15) == True:
        for i in range(3):
            noList.append(randomiser_method(
                date, 10, 30))  # type: ignore

    else:
        # if rearrangement used, then remove from list and just randomise
        # else randomise if and until you rearrange the values
        fns = [randomiser_method, rearrangment_method]
        for i in range(3):
            if choice(fns) == 1:
                noList.append(rearrangment_method(
                    date, 10, 30))
                fns.remove(rearrangment_method)
            else:
                if choice(fns) == 1:
                    noList.append(choice(fns)(date))
                else:
                    noList.append(choice(fns)(
                        date, 10, 30))
    return noList


def generate_medium_dates(date):
    noList = [date]
    if big_difference(int(date), 10) == True:
        for i in range(3):
            noList.append(randomiser_method(
                date, 7, 20))  # type: ignore
    else:
        # if rearrangement used, then remove from list and just randomise
        # else randomise if and until you rearrange the values
        fns = [randomiser_method, rearrangment_method]
        for i in range(3):
            if choice(fns) == 1:
                noList.append(rearrangment_method(
                    date, 7, 20))
                fns.remove(rearrangment_method)
            else:
                if choice(fns) == 1:
                    noList.append(choice(fns)(date))
                else:
                    noList.append(choice(fns)(
                        date, 7, 20))
    for i in noList:
        i = str(i)
    return noList


def generate_hard_dates(date):
    noList = [date]
    if big_difference(int(date), 5) == True:
        for i in range(3):
            noList.append(randomiser_method(
                date, 5, 15))  # type: ignore
    else:
        # if rearrangement used, then remove from list and just randomise
        # else randomise if and until you rearrange the values
        fns = [randomiser_method, rearrangment_method]
        for i in range(3):
            if choice(fns) == 1:
                noList.append(rearrangment_method(
                    date, 5, 15))
                fns.remove(rearrangment_method)
            else:
                if choice(fns) == 1:
                    noList.append(choice(fns)(date))
                else:
                    noList.append(choice(fns)(
                        date, 5, 15))
    for i in noList:
        i = str(i)
    return noList
