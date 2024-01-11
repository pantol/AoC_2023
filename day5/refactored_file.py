from decorators import add_getters_setters
from details_data import DetailsData

@add_getters_setters
class RefactoredFile():
    def __init__(self, seeds=[], seed_to_soil=[], soil_to_fertilizer=[], fertilizer_to_water=[], water_to_light=[], light_to_temperature=[], temperature_to_humidity=[], humidity_to_location=[]):
        self.seeds: list[int] = seeds
        self.seed_to_soil: list[DetailsData] = seed_to_soil
        self.soil_to_fertilizer: list[DetailsData] = soil_to_fertilizer
        self.fertilizer_to_water: list[DetailsData] = fertilizer_to_water
        self.water_to_light: list[DetailsData] = water_to_light
        self.light_to_temperature: list[DetailsData] = light_to_temperature
        self.temperature_to_humidity: list[DetailsData] = temperature_to_humidity
        self.humidity_to_location: list[DetailsData] = humidity_to_location

    def __setitem__(self, key, value):
        if key == 'seeds':
            self.seeds = value
        elif key == 'seed_to_soil':
            self.seed_to_soil = value
        elif key == 'soil_to_fertilizer':
            self.soil_to_fertilizer = value
        elif key == 'fertilizer_to_water':
            self.fertilizer_to_water = value
        elif key == 'water_to_light':
            self.water_to_light = value
        elif key == 'light_to_temperature':
            self.light_to_temperature = value
        elif key == 'temperature_to_humidity':
            self.temperature_to_humidity = value
        elif key == 'humidity_to_location':
            self.humidity_to_location = value
        else:
            raise KeyError(f"Invalid key: {key}")
        
    def __str__(self):
        seeds_str = ', '.join(str(detail) for detail in self.seeds)
        seed_to_soil_str = f"[{'], ['.join(str(detail) for detail in self.seed_to_soil)}]"
        soil_to_fertilizer_str = f"[{'], ['.join(str(detail) for detail in self.soil_to_fertilizer)}]"
        fertilizer_to_water_str = f"[{'], ['.join(str(detail) for detail in self.fertilizer_to_water)}]"
        water_to_light_str = f"[{'], ['.join(str(detail) for detail in self.water_to_light)}]"
        light_to_temperature_str = f"[{'], ['.join(str(detail) for detail in self.light_to_temperature)}]"
        temperature_to_humidity_str = f"[{'], ['.join(str(detail) for detail in self.temperature_to_humidity)}]"
        humidity_to_location_str = f"[{'], ['.join(str(detail) for detail in self.humidity_to_location)}]"

        return f"seeds: [{seeds_str}],\nseed_to_soil: [{seed_to_soil_str}]\nsoil_to_fertilizer: [{soil_to_fertilizer_str}]\nfertilizer_to_water: [{fertilizer_to_water_str}]\nwater_to_light: [{water_to_light_str}]\nlight_to_temperature: [{light_to_temperature_str}]\ntemperature_to_humidity: [{temperature_to_humidity_str}]\nhumidity_to_location: [{humidity_to_location_str}]"