import copy


class InputTakingOffMoments(object):
    """Класс, содержащий набор плановых и разрешенных моментов взлета и методы для работы с ними"""

    def __init__(self, planned_moments, permitted_moments, spare_arrival_time_interval):
        self._ordered_planned_moments = planned_moments
        self._ordered_planned_moments.sort()
        self._ordered_permitted_moments = permitted_moments
        self._ordered_permitted_moments.sort()
        self._last_planned_taking_off_moment_index = -1
        self._last_permitted_taking_off_moment_index = -1
        self._spare_arrival_time_interval = spare_arrival_time_interval

    def get_planned_moments(self):
        return self._last_planned_taking_off_moment_index

    def get_permitted_moments(self):
        return self._last_permitted_taking_off_moment_index

    def get_next_permitted_moment(self):
        self._last_permitted_taking_off_moment_index += 1
        return self._ordered_permitted_moments[self._last_permitted_taking_off_moment_index]

    def get_nearest_permitted_moment(self, possible_moment):
        for i in range(self._last_permitted_taking_off_moment_index + 1, len(self._ordered_permitted_moments)):
            permitted_moment = self._ordered_permitted_moments[i]
            if permitted_moment - self._spare_arrival_time_interval.start_moment >= possible_moment:
                self._last_permitted_taking_off_moment_index = self._ordered_permitted_moments.index(permitted_moment)
                return permitted_moment

        return None

    def get_unused_planned_moments(self):
        unused_planned_moments = copy.deepcopy(self._ordered_planned_moments)

        # unused_planned_moments1 = unused_planned_moments[self._last_planned_taking_off_moment_index + 1:]

        self._last_planned_taking_off_moment_index += len(unused_planned_moments)

        return unused_planned_moments

    def reset_last_planned_taking_off_moment_index(self):
        self._last_planned_taking_off_moment_index = -1

    def reset_last_permitted_taking_off_moment_index(self):
        self._last_permitted_taking_off_moment_index = -1
