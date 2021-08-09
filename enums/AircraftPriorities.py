import enum


@enum.unique
class AircraftPriorities(enum.Enum):
    """Перечисление вариантов значений для приоритета ВС."""

    DEFAULT = 1,
    MEDIUM = 2,
    HIGH = 3
