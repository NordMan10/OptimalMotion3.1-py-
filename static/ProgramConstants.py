class ProgramConstants(object):
    """Константные значения, общие для всей программы."""

    # Начальное значение Id для зон массового обслуживания.
    start_id_value = 1

    # Время руления от парковки до ПРДВ.
    motion_from_parking_to_PS = 240

    # Время руления от ПРДВ до ИСП.
    motion_from_PS_to_ES = 40

    # Время руления от парковки до Спец. площадки.
    motion_from_parking_to_SP = 120

    # Время руления от Спец. площадки до ПРДВ.
    motion_from_SP_to_PS = 120

    # Время взлета.
    processing_time = 240

    # Время обработки.
    taking_off_interval = 30
