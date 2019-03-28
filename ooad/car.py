from tire import Tire


class Car:
    """
    Docstring for car class
    """

    def __init__(self, engine, tires: list):
        self.engine = engine
        self.tires = tires

    def description(self) -> None:
        print(f'A car with a {self.engine} and {self.tires} tires')

    def wheel_circumference(self) -> float:
        if isinstance(self.tires, list) and isinstance(self.tires[0], Tire) and len(self.tires) > 0:
            return self.tires[0].circumference()
        else:
            return 0
