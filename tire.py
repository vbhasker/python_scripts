import math


class Tire:
    """
    Tire represents a tire that would be used in an automobile
    """

    def __init__(self, tire_type, width, ratio, diameter, brand='', construction='R'):
        self.tire_type = tire_type
        self.width = width
        self.ratio = ratio
        self.diameter = diameter
        self.brand = brand
        self.construction = construction

    def __repr__(self) -> str:
        """
        represents the tire's information in the standard notation
        :return: string with standard notation
        """
        return (f'{self.tire_type}{self.width}/{self.ratio}'
                + f'{self.construction}{self.diameter}')

    def circumference(self) -> float:
        """
        The circumference of the tire in inches.
        :return: circumference in inches
        >>> tire = Tire('P', 205, 65, 15)
        >>> tire.circumference()
        80.1
        """
        total_diameter = self.side_wall_inches() * 2 + self.diameter
        return round(total_diameter * math.pi, 1)

    def side_wall_inches(self) -> float:
        return (self.width * (self.ratio / 100)) / 25.4
