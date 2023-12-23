def remove_eol(line):
    if line.rfind('/n') != -1:
        return line[:line.rfind('/n')]
    else:
        return line


def get_all_numbers_from_line(line):
    result = []

    for character in line:
        if character.isnumeric():
            result.append(character)

    return result


def get_first_and_last_digit(numbers_array):
    return numbers_array[0] + numbers_array[len(numbers_array) - 1]


def sum_of_every_number(numbers_array):
    result = 0
    for number in numbers_array:
        result += int(number)

    return result


def get_result_of_challange():
    with open('text.txt', 'r', encoding="utf-8") as my_file:
        readlines_result = my_file.readlines()
        lines = map(remove_eol, readlines_result)
        result_numbers = []

        for index, line in enumerate(lines):
            all_number_in_line = get_all_numbers_from_line(line)
            result_numbers.append(get_first_and_last_digit(all_number_in_line))

        return sum_of_every_number(result_numbers)


print(get_result_of_challange())
