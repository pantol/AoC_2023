def remove_eol(line):
    if line.rfind('/n') != -1:
        return line[:line.rfind('/n')]
    else:
        return line


def get_number(line):
    result = {}

    first_number = {
        "index": None,
        "value": None
    }

    last_number = {
        "index": None,
        "value": None
    }

    literal_digits = ["one", "two", "three", "four",
                      "five", "six", "seven", "eight", "nine"]

    print(line)
    for digit_index, digit in enumerate(literal_digits):
        print(digit)
        print(line.count(digit))
        # TODO: bład jest taki, że w tej pętli zawsze i tak pobierane jest pierwsze wystąpienie danego słowa
        for count in range(line.count(digit)):
            index = line.find(digit)
            print(index)
            if index != -1:
                if first_number["index"] is None or first_number["index"] >= index:
                    first_number["index"] = index
                    first_number["value"] = str(digit_index+1)
                if last_number["index"] is None or last_number["index"] <= index:
                    last_number["index"] = index
                    last_number["value"] = str(digit_index+1)

    for index, character in enumerate(line):
        if character.isnumeric():
            if first_number["index"] is None or first_number["index"] >= index:
                first_number["index"] = index
                first_number["value"] = character
            if last_number["index"] is None or last_number["index"] <= index:
                last_number["index"] = index
                last_number["value"] = character

    return first_number["value"] + last_number["value"]


def get_first_and_last_digit(numbers_array):
    return numbers_array[0] + numbers_array[-1]


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

        for line in lines:
            result_numbers.append(get_number(line))

        print(result_numbers)

        return sum_of_every_number(result_numbers)


print(get_result_of_challange())
