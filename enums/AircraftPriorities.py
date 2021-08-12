from enum import IntEnum


class AircraftPriorities(IntEnum):
    """Перечисление вариантов значений для приоритета ВС."""

    DEFAULT = 1,
    MEDIUM = 2,
    HIGH = 3
