from io import TextIOWrapper
from details_data import DetailsData
from refactored_file import RefactoredFile


def insert_details_in_the_sorted_way(section: list[DetailsData], details: DetailsData):
    if len(section) == 0:
        section.append(details)
    elif len(section) == 1:
        if section[0].source_index < details.source_index:
            section.append(details)
        else:
            section.insert(0, details)
    else:
        for index, value in enumerate(section):
            if index == len(section) - 1:
                section.append(details)
                break
            if value.source_index < details.source_index and section[index + 1].source_index > details.source_index:
                section.insert(index + 1, details)
                break
    return section


def refactor_section(section, category) -> list[DetailsData]:
    result: list[DetailsData] = []
    lines = section.split('\n')
    del lines[0]
    for record in lines:
        values = list(map(int, record.split(' ')))
        details = DetailsData(values[0], values[1], values[2])
        insert_details_in_the_sorted_way(result, details)

    return result


def refactor_file(my_file: TextIOWrapper) -> RefactoredFile:
    file_sections = my_file.read().split('\n\n')
    result = RefactoredFile()
    for index, (key, _category) in enumerate(result.__dict__.items()):
        if index == 0:
            splitted_seeds = file_sections[index].split(': ')
            result[key] = list(map(int, splitted_seeds[1].split(' ')))
        else:
            current_section = file_sections[index]
            refactored_section = refactor_section(current_section, key)
            result[key] = refactored_section
    return result


def find_destination(seed: int, seed_to_soil: list[DetailsData]) -> int:
    for detail in seed_to_soil:
        if detail.source_index <= seed and detail.source_index + detail.range_length >= seed:
            return detail.destination_index + seed - detail.source_index
    return seed


def find_location(seed: int, refactored_file: RefactoredFile):
    soil = find_destination(seed, refactored_file.seed_to_soil)
    fertilizer = find_destination(soil, refactored_file.soil_to_fertilizer)
    water = find_destination(fertilizer, refactored_file.fertilizer_to_water)
    light = find_destination(water, refactored_file.water_to_light)
    temperature = find_destination(light, refactored_file.light_to_temperature)
    humidity = find_destination(temperature, refactored_file.temperature_to_humidity)
    location = find_destination(humidity, refactored_file.humidity_to_location)
    return location


def find_lowest_location(locations: list[int]):
    lowest_location = locations[0]
    for location in locations:
        if location < lowest_location:
            lowest_location = location
    return lowest_location


def get_result_of_challange():
    with open('./day5/text.txt', 'r', encoding='utf-8') as my_file:
        refactored_file = refactor_file(my_file)
        locations: list[int] = []
        for seed in refactored_file.seeds:
            locations.append(find_location(seed, refactored_file))
        return find_lowest_location(locations)

print(get_result_of_challange())
