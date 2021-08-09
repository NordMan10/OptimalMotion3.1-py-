class TakingOffAircraftCreationMoments(object):
    """Набор моментов, получаемых во входных данных для взлетающего ВС."""

    def __init__(self, plannedTakingOff = 0):
        """Constructor.

        Keyword arguments:
        plannedTakingOff -- плановый момент вылета (по умолчанию = 0)
        """
        self.plannedTakingOff = plannedTakingOff

    def GetPlannedTakingOff(self):
        return self.plannedTakingOff
