class Interval(object):
    """Представление интервала времени."""

    def __init__(self, start_moment, end_moment):
        self._start_moment = start_moment
        self._end_moment = end_moment

    def get_start_moment(self):
        return self._start_moment

    def get_end_moment(self):
        return self._end_moment

    def is_intervals_intersects(self, other_interval):
        return other_interval.get_end_moment() > self.get_start_moment() and \
               other_interval.get_start_moment() < self.get_end_moment()

    def __add__(self, other):
        return Interval(self.get_start_moment() + other.get_start_moment(),
                        self.get_end_moment() + other.get_end_moment())
