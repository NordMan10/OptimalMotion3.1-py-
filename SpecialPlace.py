from IMassServiceZone import IMassServiceZone
from IMassServiceZoneExtensions import IMassServiceZoneExtensions


class SpecialPlace(IMassServiceZone):
    """"""

    def __init__(self, __id = 0):
        self._id = __id
        self._processing_intervals = {}

    @property
    def id(self):
        return self._id

    def add_aircraft_interval(self, aircraft_id, free_interval):
        IMassServiceZoneExtensions.add_aircraft_interval(aircraft_id, free_interval,
                                                         self._processing_intervals)

    def get_free_interval(self, new_interval):
        return IMassServiceZoneExtensions.get_free_interval(new_interval, self._processing_intervals)

    def remove_aircraft_interval(self, aircraft_id):
        IMassServiceZoneExtensions.remove_aircraft_interval(aircraft_id, self._processing_intervals)

    def reset(self):
        self._processing_intervals.clear()
