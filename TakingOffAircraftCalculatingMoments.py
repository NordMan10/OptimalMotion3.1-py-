class TakingOffAircraftCalculatingMoments(object):
    """Набор рассчитываемых моментов для взлетающего ВС."""

    def __init__(self):
        self._possible_taking_off = 0
        self._permitted_taking_off = 0
        self._reserve_permitted_taking_off = 0
        self._start = 0

    @property
    def possible_taking_off(self):
        return self._possible_taking_off

    @possible_taking_off.setter
    def possible_taking_off(self, value):
        self._possible_taking_off = value

    @property
    def permitted_taking_off(self):
        return self._permitted_taking_off

    @permitted_taking_off.setter
    def permitted_taking_off(self, value):
        self._permitted_taking_off = value

    @property
    def reserve_permitted_taking_off(self):
        return self._reserve_permitted_taking_off

    @reserve_permitted_taking_off.setter
    def reserve_permitted_taking_off(self, value):
        self._reserve_permitted_taking_off = value

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value

