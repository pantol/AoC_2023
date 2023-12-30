def prepare_line(line: str):
    splitted_line = line.split(':')
    game = splitted_line[0]
    turns = splitted_line[1].split(';')

    max_red = 0
    max_green = 0
    max_blue = 0

    for turn in turns:
        cubes_from_turn = turn.split(',')
        for cube in cubes_from_turn:
            splitted_cube = cube.lstrip().split(' ')
            amount: int = int(splitted_cube[0])
            cube_color: str = splitted_cube[1]
            print(amount, cube_color)
            if (cube_color == 'green' and amount > max_green):
                max_green = amount
            elif cube_color == 'blue' and amount > max_blue:
                max_blue = amount
            elif cube_color == 'red' and amount > max_red:
                max_red = amount

    return {
        'game': game.split(' ')[1],
        'max_red': max_red,
        'max_green': max_green,
        'max_blue': max_blue
    }


def get_result_of_challange():
    with open('./day2/text.txt', 'r', encoding="utf-8") as my_file:
        lines = my_file.read().split('\n')
        result_sum = 0

        for line in lines:
            prepared_object = prepare_line(line)
            print(prepared_object)
            if not prepared_object['max_green'] > 13 and not prepared_object['max_red'] > 12 and not prepared_object['max_blue'] > 14:
                result_sum += int(prepared_object['game'])

        return result_sum


print(get_result_of_challange())
