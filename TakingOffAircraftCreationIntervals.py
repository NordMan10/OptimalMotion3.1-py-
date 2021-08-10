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
        self.motion_from_parking_to_PS = motion_from_parking_to_PS
        self.motion_from_PS_to_ES = motion_from_PS_to_ES
        self.motion_from_parking_to_SP = motion_from_parking_to_SP
        self.motion_from_SP_to_PS = motion_from_SP_to_PS
        self.processing = processing
        self.taking_off = taking_off


    def get_motion_from_parking_to_PS(self):
        return self.motion_from_parking_to_PS

    def get_motion_from_PS_to_ES(self):
        return self.motion_from_PS_to_ES

    def get_motion_from_parking_to_SP(self):
        return self.motion_from_parking_to_SP

    def get_motion_from_SP_to_PS(self):
        return self.motion_from_SP_to_PS

    def get_processing(self):
        return self.processing

    def get_taking_off(self):
        return self.taking_off
