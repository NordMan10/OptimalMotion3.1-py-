class Interval(object):
    """Представление интервала времени."""

    def __init__(self, start_moment, end_moment):
        self._start_moment = start_moment
        self._end_moment = end_moment

    @property
    def start_moment(self):
        return self._start_moment

    @property
    def end_moment(self):
        return self._end_moment

    def is_intervals_intersects(self, other_interval):
        return other_interval.end_moment() > self.start_moment() and \
               other_interval.get_start_moment() < self.end_moment()

    def __add__(self, other):
        return Interval(self.start_moment() + other.get_start_moment(),
                        self.end_moment() + other.end_moment())
