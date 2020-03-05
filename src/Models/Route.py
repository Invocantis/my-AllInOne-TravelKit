import location


class Route:
    def __int__(self, start_point: location, end_point: location, time_arrival, time_departure, duration):
        self.start_point = start_point
        self.end_point = end_point
        self.time_arrival = time_arrival
        self.time_departure = time_departure
        self.duration = duration

