class Device:

    def __init__(self, brand: str, type_of_device: str, year_of_manufacture: int, measurement_limit: int):
        self.brand = brand
        self.type_of_device = type_of_device
        self.year_of_manufacture = year_of_manufacture
        self.measurement_limit = measurement_limit

    def __str__(self):
        return f"Device brand: {self.brand}, type: {self.type_of_device}," \
               f" year of m.: {self.year_of_manufacture}, m. limit: {self.measurement_limit}"

    def __eq__(self, other):
        if self.brand == other.brand:
            if self.type_of_device == other.type_of_device:
                if self.year_of_manufacture == other.year_of_manufacture:
                    if self.measurement_limit == other.measurement_limit:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if self.brand < other.brand:
            return True
        elif self.brand == other.brand:
            if self.type_of_device < other.type_of_device:
                return True
            elif self.type_of_device == other.type_of_device:
                if self.year_of_manufacture < other.year_of_manufacture:
                    return True
                elif self.year_of_manufacture == other.year_of_manufacture:
                    if self.measurement_limit < other.measurement_limit:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        if self.brand > other.brand:
            return True
        elif self.brand == other.brand:
            if self.type_of_device > other.type_of_device:
                return True
            elif self.type_of_device == other.type_of_device:
                if self.year_of_manufacture > other.year_of_manufacture:
                    return True
                elif self.year_of_manufacture == other.year_of_manufacture:
                    if self.measurement_limit > other.measurement_limit:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
