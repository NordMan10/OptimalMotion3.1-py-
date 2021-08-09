class AircraftInputData(object):
    """description of class"""

    def __init__(self, runwayId, specialPlaceId, type, priority,
		         processingIsNeeded, creationMoments, creationIntervals):
        """Constructor.

        Keyword arguments:
        runwayId -- Id ВПП.
        specialPlaceId -- Id Спец. площадки.
        type -- Тип ВС.
        priority -- Приоритет ВС.
        processingIsNeeded -- Флаг необходимости противообледенительной обработки.
        creationMoments -- Моменты ВС, задающиеся при создании ВС.
        creationIntervals -- Интервалы ВС, задающиеся при создании ВС.
        """

        self.runwayId = runwayId
        self.specialPlaceId = specialPlaceId
        self.type = type
        self.priority = priority
        self.processingIsNeeded = processingIsNeeded
        self.creationMoments = creationMoments
        self.creationIntervals = creationIntervals

    def GetRunwayId(self):
        return self.runwayId

    def GetSpecialPlaceId(self):
        return self.specialPlaceId

    def GetType(self):
        return self.type

    def GetPriority(self):
        return self.priority

    def GetProcessingNecessity(self):
        return self.processingIsNeeded

    def GetCreationMoments(self):
        return self.creationMoments

    def GetCreationIntervals(self):
        return self.creationIntervals