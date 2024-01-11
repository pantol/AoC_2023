def add_getters_setters(cls):
    for attribute_name in cls.__dict__:
        if not attribute_name.startswith("_"):
            add_getter_setter(attribute_name)(cls)
    return cls


def add_getter_setter(attribute):
    def decorator(cls):
        def getter(self):
            return getattr(self, f"_{attribute}")

        def setter(self, value):
            setattr(self, f"_{attribute}", value)

        setattr(cls, f"get_{attribute}", getter)
        setattr(cls, f"set_{attribute}", setter)

        return cls

    return decorator