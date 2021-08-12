from IMassServiceZone import IMassServiceZone
from Interval import Interval


class IMassServiceZoneExtensions(object):
    """
    Класс, содержащий реализацию общих методов для интерфейса IMassServiceZone.

    Класс, содержащий реализацию общих методов для интерфейса зоны массового обслуживания (IMassServiceZone).
    Описание данного интерфейса см. в определении интерфейса IMassServiceZone
    """

    @staticmethod
    def add_aircraft_interval(aircraft_id, free_interval, zone_intervals):
        """
        Добавляет переданный интервал в список интервалов зоны, если он не пересекается с существующими интервалами.
	    Подразумевается, что был передан свободный (не пересекающийся интервал), который был возвращен методом GetFreeInterval().

        :param aircraft_id: Id ВС
        :param free_interval: Рассчитанный свободный интерва
        :param zone_intervals: Список существующих интервалов зоныл
        """

        if IMassServiceZoneExtensions._check_intervals_intersection(free_interval, zone_intervals):
            raise ValueError("Интервалы пересекаются! Передайте проверенный интервал")

        zone_intervals[aircraft_id] = free_interval

    @staticmethod
    def get_free_interval(interval, zone_intervals):
        """
        Проверяет, можно ли добавить переданный интервал в список уже существующих интервалов зоны без пересечений с ними.
	    Если можно, то возвращает копию переданного интервала. Если нельзя, то рассчитывает новый, непересекающийся интервал.

        :param interval:  Интервал, который нужно проверить.
        :param zone_intervals: Список существующих интервалов зоны.
        :return: Свободный, непересекающийся с существующими интервалами зоны, интервал.
        """

        new_interval = Interval(interval.start_moment, interval.end_moment)
        for key, value in zone_intervals.items():
            if new_interval.end_moment >= value.start_moment and new_interval.start_moment <= value.end_moment:
                delay = zone_intervals[key].end_moment - interval.start_moment
                new_interval = Interval(interval.start_moment + delay, interval.end_moment + delay)

        return new_interval

    @staticmethod
    def remove_aircraft_interval(aircraft_id, zone_intervals):
        """
        Удаляет из списка интервалов занимания зоны интервал, принадлежащий ВС, Id которого был передан.

        :param aircraft_id: Id ВС, интервал которого нужно удалить.
        :param zone_intervals: Список существующих интервалов зоны.
        """

        del zone_intervals[aircraft_id]

    @staticmethod
    def _check_intervals_intersection(interval, zone_intervals):
        """
        Проверяет пересечение переданного интервала с набором существующих интервалов.

        :param interval: Интервал, который нужно проверить.
        :param zone_intervals: Список существующих интервалов зоны.
        :return: Значение bool, определяющее наличие пересечения.
        """

        for key, value in zone_intervals.items():
            if zone_intervals[key].is_intervals_intersects(interval):
                return True

        return False
