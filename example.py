from tire import Tire
from snow_tire import SnowTire
from car import Car

tire = Tire('P', 205, 65, 15)
tires = [tire, tire, tire, tire]

honda = Car(engine='4-cylinder', tires=tires)
honda.description()
print(honda.wheel_circumference())
print(f'Each tire circumference is {tire.circumference()}')

tire = SnowTire('P', 205, 65, 15, 2)
tires = [tire, tire, tire, tire]

toyota = Car(engine='4-cylinder', tires=tires)
toyota.description()
print(toyota.wheel_circumference())
