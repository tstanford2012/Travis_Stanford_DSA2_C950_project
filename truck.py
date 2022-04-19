from typing import List

from package import Package
from time import Time


class Truck:
    truck_id: int
    truck_capacity: int
    mph: int
    departure_time: Time
    packages: List[Package] = []

    def __init__(self, truck_id: int) -> None:
        self.truck_id = truck_id
        self.truck_capacity = 16
        self.mph = 18
        self.departure_time = Time(8)
        self.current_time = Time()
        self.packages: List[Package] = []
