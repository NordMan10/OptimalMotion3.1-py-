class AircraftInputData(object):
    """Набор входных данных, необходимый для каждого ВС."""

    def __init__(self, runway_id, special_place_id, __type, priority,
                 processing_necessity, creation_moments, creation_intervals):
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

        self._runway_id = runway_id
        self._special_place_id = special_place_id
        self._type = __type
        self._priority = priority
        self._processing_necessity = processing_necessity
        self._creation_moments = creation_moments
        self._creation_intervals = creation_intervals

    @property
    def runway_id(self):
        return self._runway_id

    @property
    def special_place_id(self):
        return self._special_place_id

    @property
    def type(self):
        return self._type

    @property
    def priority(self):
        return self._priority

    @property
    def processing_necessity(self):
        return self._processing_necessity

    @property
    def creation_moments(self):
        return self._creation_moments

    @property
    def creation_intervals(self):
        return self._creation_intervals
