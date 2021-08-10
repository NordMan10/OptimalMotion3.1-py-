from IMassServiceZone import IMassServiceZone
from Interval import Interval


class IMassServiceZoneExtensions(object):
    @staticmethod
    def add_aircraft_interval(self, aircraft_id, free_interval, zone_intervals):
        if self._check_intervals_intersection(free_interval, zone_intervals):
            raise ValueError("Интервалы пересекаются! Передайте проверенный интервал")

        zone_intervals[aircraft_id] = free_interval

    @staticmethod
    def get_free_interval(self, interval, zone_intervals):
        new_interval = Interval(interval.get_start_moment(), interval.end_moment())
        for key, value in zone_intervals.items():
            delay = zone_intervals[key].end_moment() - interval.get_start_moment()
            new_interval = Interval(interval.get_start_moment() + delay, interval.end_moment() + delay)

        return new_interval

    @staticmethod
    def remove_aircraft_interval(self, aircraft_id, zone_intervals):
        del zone_intervals[aircraft_id]

    @staticmethod
    def _check_intervals_intersection(self, interval, zone_intervals):
        for key, value in zone_intervals.items():
            if zone_intervals[key].is_intervals_intersects(interval):
                return True

        return False
