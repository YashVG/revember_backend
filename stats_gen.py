import random

# checks if modifieid numerical string can be changed to integer

# there's no difference in the numbers generated for diff %
# because either the values are too obscure or produces duplicates, therefore
# rendering them useless when the user answers the questions


def is_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def generate_random_number(number):
    randomPercentage = float()  # variable declaration to avoid UnboundError
    if is_integer(number) == True:
        randomPercentage = random.uniform(-5, 5)
    elif is_integer(number) == False:
        randomPercentage = random.uniform(-10, 10)

    randomNumber = number * (1 + randomPercentage/100)
    return randomNumber


def generate_numerical_answers(value):
    # assumes value will be integer, change later if implementation is different
    answerChoices = [value]
    if len(str(value)) >= 2:
        value = str(value)
       # checks if it's not an integer, and executes percentage-wise generation of numbers
        if is_integer(value) == False:
            for i in range(3):
                answerChoices.append(
                    generate_random_number(float(value)))
        elif is_integer(value) == True:
            for i in range(3):
                truncated_number = str(
                    round(generate_random_number(int(value))))
                answerChoices.append(truncated_number)

        return answerChoices

    # if number is too small, then vary by larger percentage
    elif len(str(value)) < 2:
        value = str(value)
        if is_integer(value) == False:
            for i in range(3):
                answerChoices.append(
                    generate_random_number(float(value)))
        # because the length of the number is less than 2, doing a percentage
        # wise generation won't make sense, hence generating random int vals
        elif is_integer(value) == True:

            possibleNumbers = [x for x in range(1, 10) if x != int(value)]
            randInts = random.sample(possibleNumbers, 3)
            for i in randInts:
                answerChoices.append(str(i))

        return answerChoices


# print(generate_numerical_answers('123.2'))
# print(generate_numerical_answers('12343'))
# print(generate_numerical_answers('1'))
