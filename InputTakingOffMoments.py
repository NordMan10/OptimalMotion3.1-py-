import static.CommonInputData


class InputTakingOffMoments(object):
    """description of class"""

    def __init__(self, planned_moments, permitted_moments):
        self._ordered_planned_moments = planned_moments.sort()
        self._ordered_permitted_moments = permitted_moments.sort()
        self._last_planned_taking_off_moment_index = -1
        self._last_permitted_taking_off_moment_index = -1


    def get_planned_moments(self):
        return self._last_planned_taking_off_moment_index


    def get_permitted_moments(self):
        return self._last_permitted_taking_off_moment_index 


    def get_next_permitted_moment(self):
        self._last_permitted_taking_off_moment_index += 1
        return self._ordered_permitted_moments[self._last_permitted_taking_off_moment_index]


    def get_nearest_permitted_moment(self, possible_moment):
        for i in range(self._last_permitted_taking_off_moment_index, len(self._ordered_permitted_moments)):
            permitted_moment = self._ordered_permitted_moments[i]
            if (permitted_moment - CommonInputData.get_spare_arrival_time_interval.get_start_moment() >= possible_moment):
                self._last_permitted_taking_off_moment_index = self._ordered_permitted_moments.index(permitted_moment)

                return permitted_moment