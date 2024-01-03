def prepare_data_from_file(lines: list[str]):
    found_symbols = []
    found_numbers = []
    for index, line in enumerate(lines):
        found_symbols.append([])
        found_numbers.append([])
        number = ''
        for character_index, character in enumerate(line):
            if (character == '.'):
                if (number):
                    found_numbers[index].append({
                        'value': int(number),
                        'start_index': character_index - len(number),
                        'end_index': character_index - 1
                    })
                    number = ''
            elif character.isdigit():
                number += character
            elif character == '*':
                if (number):
                    found_numbers[index].append({
                        'value': int(number),
                        'start_index': character_index - len(number),
                        'end_index': character_index - 1
                    })
                    number = ''
                found_symbols[index].append({
                    'index': character_index,
                    'adjacent_numbers': []
                })
        if (number):
            found_numbers[index].append({
                'value': int(number),
                'start_index': len(line) - len(number),
                'end_index': len(line) - 1
            })
    return {
        'found_numbers': found_numbers,
        'found_symbols': found_symbols
    }


def get_sum_from_prepared_data(prepared_data, max_line_length):
    result = 0

    for line_number, all_numbers_from_line in enumerate(prepared_data['found_numbers']):
        for number in all_numbers_from_line:
            possible_symbols_indexes = []
            if line_number != 0:
                start_index = number['start_index'] - \
                    1 if number['start_index'] - \
                    1 > 0 else number['start_index']
                end_index = number['end_index'] + 1 if number['end_index'] + \
                    1 < max_line_length else number['end_index']
                possible_symbols_indexes.append({
                    'line': line_number - 1,
                    'indexes': [i for i in range(start_index, end_index + 1)]
                })

            current_line_indexes = []
            if (number['start_index'] - 1 > 0):
                current_line_indexes.append(number['start_index'] - 1)
            if (number['end_index'] + 1 < max_line_length):
                current_line_indexes.append(number['end_index'] + 1)
            possible_symbols_indexes.append({
                'line': line_number,
                'indexes': current_line_indexes
            })

            if (line_number + 1 < len(prepared_data['found_symbols'])):
                start_index = number['start_index'] - \
                    1 if number['start_index'] - \
                    1 >= 0 else number['start_index']
                end_index = number['end_index'] + 1 if number['end_index'] + \
                    1 < max_line_length else number['end_index']
                possible_symbols_indexes.append({
                    'line': line_number + 1,
                    'indexes': [i for i in range(start_index, end_index + 1)]
                })

            for possible_symbol_index in possible_symbols_indexes:
                if len(prepared_data['found_symbols'][possible_symbol_index['line']]) > 0:
                    for i_index, i in enumerate(prepared_data['found_symbols'][possible_symbol_index['line']]):
                        if i['index'] in possible_symbol_index['indexes']:
                            prepared_data['found_symbols'][possible_symbol_index['line']
                                                           ][i_index]['adjacent_numbers'].append(number['value'])
    for found_symbols in prepared_data['found_symbols']:
        if len(found_symbols) > 0:
            for symbol in found_symbols:
                if len(symbol['adjacent_numbers']) == 2:
                    result += symbol['adjacent_numbers'][0] * \
                        symbol['adjacent_numbers'][1]
    return result


def get_result_of_challange():
    with open('./day3/text.txt', 'r', encoding="utf-8") as my_file:
        lines = my_file.read().split('\n')

        prepared_data = prepare_data_from_file(lines)
        return get_sum_from_prepared_data(prepared_data, len(lines[0]))


print(get_result_of_challange())
