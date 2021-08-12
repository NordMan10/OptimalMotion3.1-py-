from IMassServiceZone import IMassServiceZone
from Interval import Interval


class IMassServiceZoneExtensions(object):
    @staticmethod
    def add_aircraft_interval(aircraft_id, free_interval, zone_intervals):
        if IMassServiceZoneExtensions._check_intervals_intersection(free_interval, zone_intervals):
            raise ValueError("Интервалы пересекаются! Передайте проверенный интервал")

        zone_intervals[aircraft_id] = free_interval

    @staticmethod
    def get_free_interval(interval, zone_intervals):
        new_interval = Interval(interval.start_moment, interval.end_moment)
        for key, value in zone_intervals.items():
            if new_interval.end_moment >= value.start_moment and new_interval.start_moment <= value.end_moment:
                delay = zone_intervals[key].end_moment - interval.start_moment
                new_interval = Interval(interval.start_moment + delay, interval.end_moment + delay)

        return new_interval

    @staticmethod
    def remove_aircraft_interval(aircraft_id, zone_intervals):
        del zone_intervals[aircraft_id]

    @staticmethod
    def _check_intervals_intersection(interval, zone_intervals):
        for key, value in zone_intervals.items():
            if zone_intervals[key].is_intervals_intersects(interval):
                return True

        return False
