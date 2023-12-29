literal_digits = ["one", "two", "three", "four",
                  "five", "six", "seven", "eight", "nine"]


def find_first_occurence(line: str) -> int:
    for index, character in enumerate(line):
        if character.isdigit():
            return character
        for digit_index, digit in enumerate(literal_digits):
            if line.find(digit, index) == index:
                return digit_index+1


def find_last_occurence(line: str) -> int:
    for index, character in enumerate(''.join(reversed(line))):
        if character.isdigit():
            return character
        for digit_index, digit in enumerate(literal_digits):
            if ''.join(reversed(line)).find(''.join(reversed(digit)), index) == index:
                return digit_index+1


def get_result_of_challange():
    with open('text.txt', 'r', encoding="utf-8") as my_file:
        lines = my_file.read().split('\n')

        sums_array = []

        for line in lines:
            first = (find_first_occurence(line))
            second = (find_last_occurence(line))
            sums_array.append(int(str(first) + str(second)))
        return sum(sums_array)


print(get_result_of_challange())
