class TakingOffAircraftCreationMoments(object):
    """Набор моментов, получаемых во входных данных для взлетающего ВС."""

    def __init__(self, planned_taking_off = 0):
        """Constructor.

        Keyword arguments:
        planned_taking_off -- плановый момент вылета (по умолчанию = 0)
        """
        self.planned_taking_off = planned_taking_off

    def get_planned_taking_off(self):
        return self.planned_taking_off
