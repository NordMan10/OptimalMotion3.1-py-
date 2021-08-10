class TakingOffAircraftCreationIntervals(object):
    """Набор интервалов, получаемых во входных данных для взлетающего ВС."""

    def __init__(self, motion_from_parking_to_PS, motion_from_PS_to_ES, motion_from_parking_to_SP,
                 motion_from_SP_to_PS, processing, taking_off):
        """Constructor.

        Keyword arguments:
        motion_from_parking_to_PS -- Время руления от парковки до ПРДВ.
        motion_from_PS_to_ES -- Время руления от ПРДВ до ИСП.
        motion_from_parking_to_SP -- Время руления от парковки до Спец. площадки.
        motion_from_SP_to_PS -- Время руления от Спец. площадки до ПРДВ.
        processing -- Время обработки.
        taking_off -- Время взлета.
        """
        self._motion_from_parking_to_PS = motion_from_parking_to_PS
        self._motion_from_PS_to_ES = motion_from_PS_to_ES
        self._motion_from_parking_to_SP = motion_from_parking_to_SP
        self._motion_from_SP_to_PS = motion_from_SP_to_PS
        self._processing = processing
        self._taking_off = taking_off

    @property
    def motion_from_parking_to_PS(self):
        return self._motion_from_parking_to_PS

    @property
    def motion_from_PS_to_ES(self):
        return self._motion_from_PS_to_ES

    @property
    def motion_from_parking_to_SP(self):
        return self._motion_from_parking_to_SP

    @property
    def motion_from_SP_to_PS(self):
        return self._motion_from_SP_to_PS
    @property
    def processing(self):
        return self._processing

    @property
    def taking_off(self):
        return self._taking_off
