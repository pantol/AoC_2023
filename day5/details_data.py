from decorators import add_getters_setters


@add_getters_setters
class DetailsData():
    def __init__(self, destination_index: int = 0, source_index: int = 0, range_length: int = 0):
        self.destination_index: int = int(destination_index)
        self.source_index: int = int(source_index)
        self.range_length: int = int(range_length)
    
    def _setitem__(self, key, value):
        if key == 'start_index':
            self.destination_index = value
        elif key == 'source_index':
            self.source_index = value
        elif key == 'range_length':
            self.range_length = value
        else:
            raise KeyError(f"Invalid key: {key}")
       
    def __str__(self):
        return f"start_index: {self.destination_index}, source_index: {self.source_index}, range_length: {self.range_length}"