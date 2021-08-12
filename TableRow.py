
def alt_name(name):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            return_value = (name, func(*args, **kwargs))
            return return_value
        return wrapper
    return actual_decorator


class TableRow(object):
    """
    Представление объекта Строки Таблицы. Поля класса определяют столбцы. По сути — это формат выходных данных.
    """

    def __init__(self, aircraft_id, planned_taking_off_moment, possible_taking_off_moment, permitted_taking_off_moment,
                 start_moment, total_motion_time, processing_time, processing_necessity, priority, is_reserved,
                 PS_waiting_time, runway_id, special_place_id):
        self._aircraft_id = aircraft_id
        self._planned_taking_off_moment = planned_taking_off_moment
        self._possible_taking_off_moment = possible_taking_off_moment
        self._permitted_taking_off_moment = permitted_taking_off_moment
        self._start_moment = start_moment
        self._total_motion_time = total_motion_time
        self._processing_time = processing_time
        self._processing_necessity = processing_necessity
        self._priority = priority
        self._is_reserved = is_reserved
        self._PS_waiting_time = PS_waiting_time
        self._runway_id = runway_id
        self._special_place_id = special_place_id

    @property
    @alt_name("Id ВС")
    def t_aircraft_id(self):
        return self._aircraft_id

    @property
    @alt_name("Тплан.")
    def t_planned_taking_off_moment(self):
        return self._planned_taking_off_moment

    @property
    @alt_name("Твозм.")
    def t_possible_taking_off_moment(self):
        return self._possible_taking_off_moment

    @property
    @alt_name("Тразр.")
    def t_permitted_taking_off_moment(self):
        return self._permitted_taking_off_moment

    @property
    @alt_name("Тстарт")
    def t_start_moment(self):
        return self._start_moment

    @property
    @alt_name("Общее время движения")
    def t_total_motion_time(self):
        """
        Общее время движения без учета времени обработки и простоев.
        :return:
        """

        return self._total_motion_time

    @property
    @alt_name("Время обработки")
    def t_processing_time(self):
        return self._processing_time

    @property
    @alt_name("Необходимость обработки")
    def t_processing_necessity(self):
        return self._processing_necessity

    @property
    @alt_name("Приоритет")
    def t_priority(self):
        return self._priority

    @property
    @alt_name("Резервный")
    def t_is_reserved(self):
        return self._is_reserved

    @property
    @alt_name("Время ожидания на ПРДВ")
    def t_PS_waiting_time(self):
        return self._PS_waiting_time

    @property
    @alt_name("Id ВПП")
    def t_runway_id(self):
        return self._runway_id

    @property
    @alt_name("Id Спец.площадки")
    def t_special_place_id(self):
        return self._special_place_id



