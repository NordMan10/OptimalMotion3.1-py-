class TakingOffAircraftCalculatingIntervals(object):
    """Набор рассчитываемых интервалов для взлетающего ВС."""

    def __init__(self):
        self._PS_delay = 0

    @property
    def PS_delay(self):
        return self._PS_delay

    @PS_delay.setter
    def PS_delay(self, value):
        self._PS_delay = value

