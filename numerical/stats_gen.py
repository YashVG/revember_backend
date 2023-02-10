import random

# checks if modifieid numerical string can be changed to integer


def is_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def generate_random_number(number):
    random_percentage = float()  # variable declaration to avoid UnboundError
    if is_integer(number) == True:
        random_percentage = random.uniform(-5, 5)
    elif is_integer(number) == False:
        random_percentage = random.uniform(-10, 10)

    random_number = number * (1 + random_percentage/100)
    return random_number


def generate_numerical_answers(value):
    # assumes value will be integer, change later if implementation is different
    answer_choices = [value]
    if len(str(value)) >= 2:
        value = str(value)
       # checks if it's not an integer, and executes percentage-wise generation of numbers
        if is_integer(value) == False:
            for i in range(3):
                answer_choices.append(
                    generate_random_number(float(value)))
        elif is_integer(value) == True:
            for i in range(3):
                truncated_number = str(
                    round(generate_random_number(int(value))))
                answer_choices.append(truncated_number)

        return answer_choices

    # if number is too small, then vary by larger percentage
    elif len(str(value)) < 2:
        value = str(value)
        if is_integer(value) == False:
            for i in range(3):
                answer_choices.append(
                    generate_random_number(float(value)))
        # because the length of the number is less than 2, doing a percentage
        # wise generation won't make sense, hence generating random int vals
        elif is_integer(value) == True:
            # value = int(value)
            # for i in range(3):
            #     rand_int = random.randint(1, 10)
            #     if rand_int not in answer_choices:
            #         answer_choices.append(rand_int)
            possible_numbers = [x for x in range(1, 10) if x != int(value)]
            rand_ints = random.sample(possible_numbers, 3)
            for i in rand_ints:
                answer_choices.append(str(i))

        return answer_choices


print(generate_numerical_answers('123.2'))
print(generate_numerical_answers('12343'))
print(generate_numerical_answers('1'))
