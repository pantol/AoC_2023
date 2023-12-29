from typing import Literal


literal_digits = ["one", "two", "three", "four",
                  "five", "six", "seven", "eight", "nine"]


def my_reversed(text: str):
    return ''.join(reversed(text))


def find_occurence(line: str, starting_position: Literal['first', 'last']):
    converted_line = line
    converted_literal_digits = literal_digits
    if (starting_position == 'last'):
        converted_line = my_reversed(line)
        converted_literal_digits = map(my_reversed, literal_digits)

    for index, character in enumerate(converted_line):
        if character.isdigit():
            return character
        for digit_index, digit in enumerate(converted_literal_digits):
            if line.find(digit, index) == index:
                return digit_index+1


def get_result_of_challange():
    with open('./day1/text.txt', 'r', encoding="utf-8") as my_file:
        lines = my_file.read().split('\n')

        sums_array = []

        for line in lines:
            first = (find_occurence(line, 'first'))
            second = (find_occurence(line, 'last'))
            sums_array.append(int(str(first) + str(second)))
        return sum(sums_array)


print(get_result_of_challange())
