class PreparedLine:
    def __init__(self, card: str, winning_numbers: list[int], my_numbers: list[int]):
        self.card = card
        self.winning_numbers = winning_numbers
        self.my_numbers = my_numbers
        self.card_counter = 1

    def __str__(self):
        return f"card: {self.card}, 'winning_numbers': {self.winning_numbers}, 'my_numbers': {self.my_numbers}, 'bonus_cards': {self.card_counter}"


def convert_list_to_int(text: str) -> int:
    return int(text)


def prepare_line(line: str) -> PreparedLine:
    splitted_line = line.split(': ')
    card_number = splitted_line[0].split(
        ' ')[len(splitted_line[0].split(' ')) - 1]
    # print(f'"{card_number}"')
    numbers = splitted_line[1].split(' | ')
    mapped_winning_numbers = map(convert_list_to_int, filter(
        lambda x: x != '', numbers[0].split(' ')))
    mapped_my_numbers = map(convert_list_to_int, filter(
        lambda x: x != '', numbers[1].split(' ')))

    return PreparedLine(card_number, list(mapped_winning_numbers), list(mapped_my_numbers))


def count_my_winning_cards(prepared_line: PreparedLine):
    my_winning_cards = 0
    for my_number in prepared_line.my_numbers:
        if my_number in prepared_line.winning_numbers:
            my_winning_cards += 1
    return my_winning_cards


def calculate_bonus_cards(prepared_lines: list[PreparedLine]):
    for prepared_line_index, prepared_line in enumerate(prepared_lines):
        my_winning_cards = count_my_winning_cards(prepared_line)
        for counter in range(0, prepared_line.card_counter):
            for my_winning_card_counter in range(1, my_winning_cards+1):
                if len(prepared_lines) > prepared_line_index + my_winning_card_counter:
                    prepared_lines[prepared_line_index +
                                   my_winning_card_counter].card_counter += 1

    return prepared_lines


def calculate_sum(prepared_lines: list[PreparedLine]):
    result = 0

    for prepared_line in prepared_lines:
        result += prepared_line.card_counter

    return result


def get_result_of_challange():
    with open('./day4/text.txt', 'r', encoding='utf-8') as my_file:
        lines = my_file.read().split('\n')
        prepared_lines = []

        for line in lines:
            prepared_lines.append(prepare_line(line))

        prepared_lines = calculate_bonus_cards(prepared_lines)

        return calculate_sum(prepared_lines)


print(get_result_of_challange())
