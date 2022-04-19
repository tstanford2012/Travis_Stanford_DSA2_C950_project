class Time:
    total_min: int

    def __init__(self, hours: int = 0, minutes: int = 0) -> None:
        self.total_min = 0
        self.add_min(hours * 60 + minutes)

    @property
    def minutes(self) -> int:
        return self.total_min

    def hours(self) -> int:
        return self.total_min

    def add_min(self, minutes: int) -> None:
        self.total_min += minutes
        self.total_min = self.total_min % (60 * 24)

    def add_hours(self, hours: int) -> None:
        self.add_min(hours * 60)


def time_copy(self) -> Time:
    return Time(self.hours, self.minutes)
