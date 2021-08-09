import enum


@enum.unique
class AircraftTypes(enum.Enum):
    """Перечисление вариантов значений для типа ВС."""

    LIGHT = 1,
    MEDIUM = 2,
    HEAVY = 3
