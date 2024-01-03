class PreparedLine:
    def __init__(self, card: str, winning_numbers: list[int], my_numbers: list[int]):
        self.card = card
        self.winning_numbers = winning_numbers
        self.my_numbers = my_numbers

    def __str__(self):
        return f"card: {self.card}, 'winning_numbers': {self.winning_numbers}, 'my_numbers': {self.my_numbers}"


def convert_list_to_int(text: str) -> int:
    return int(text)


def prepare_line(line: str) -> PreparedLine:
    splitted_line = line.split(': ')
    card = splitted_line[0]
    numbers = splitted_line[1].split(' | ')
    mapped_winning_numbers = map(convert_list_to_int, filter(
        lambda x: x != '', numbers[0].split(' ')))
    mapped_my_numbers = map(convert_list_to_int, filter(
        lambda x: x != '', numbers[1].split(' ')))

    return PreparedLine(card.split(' ')[1], list(mapped_winning_numbers), list(mapped_my_numbers))


def calculate_points(prepared_line: PreparedLine):
    points = 0
    for my_number in prepared_line.my_numbers:
        if my_number in prepared_line.winning_numbers:
            points = points * 2 if points > 0 else 1
    return points


def get_result_of_challange():
    with open('./day4/text.txt', 'r', encoding='utf-8') as my_file:
        lines = my_file.read().split('\n')
        result = 0

        for line in lines:
            prepared_line = prepare_line(line)
            result += calculate_points(prepared_line)

        return result


print(get_result_of_challange())
