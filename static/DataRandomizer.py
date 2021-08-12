import random


class DataRandomizer(object):
    """Класс для рандомизации значений"""

    @staticmethod
    def get_randomized_value(value, dispersion, step):
        """
        Возвращает случайное число с заданным шагом и разбросом от среднего значения.

        :param value: Среднее значение.
        :param dispersion: Разброс в процентах.
        :param step: Шаг в единицах передаваемой величины.
        :return: Целое число.
        """

        if dispersion == 0 or step == 0:
            return value

        min_value = value - (value * float(dispersion) / 100)
        max_value = value + (value * float(dispersion) / 100)

        possible_values = []

        possible_value = min_value
        while possible_value <= max_value:
            possible_values.append(possible_value)
            possible_value += step

        random_value_index = random.randrange(len(possible_values))
        return possible_values[random_value_index]