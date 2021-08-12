from static.ProgramConstants import ProgramConstants
from TakingOffAircraftCalculatingMoments import TakingOffAircraftCalculatingMoments
from TakingOffAircraftCalculatingIntervals import TakingOffAircraftCalculatingIntervals


class TakingOffAircraft(object):
    """"""

    next_taking_off_aircraft_id = ProgramConstants.start_id_value

    def __init__(self, input_data):
        self._id = self.get_new_unique_id()
        self._type = input_data.type
        self._priority = input_data.priority
        self._runway_id = input_data.runway_id
        self._special_place_id = input_data.special_place_id
        self._creation_moments = input_data.creation_moments
        self._calculating_moments = TakingOffAircraftCalculatingMoments()
        self._creation_intervals = input_data.creation_intervals
        self._calculating_intervals = TakingOffAircraftCalculatingIntervals()
        self._processing_necessity = input_data.processing_necessity

        self._is_reserve = False

# <editor-fold desc="Getters and setter">
    @property
    def id(self):
        return self._id

    @property
    def type(self):
        return self._type

    @property
    def priority(self):
        return self._priority

    @property
    def runway_id(self):
        return self._runway_id

    @property
    def special_place_id(self):
        return self._special_place_id

    @property
    def creation_moments(self):
        return self._creation_moments

    @property
    def calculating_moments(self):
        return self._calculating_moments

    @property
    def creation_intervals(self):
        return self._creation_intervals

    @property
    def calculating_intervals(self):
        return self._calculating_intervals

    @property
    def processing_necessity(self):
        return self._processing_necessity

    @property
    def is_reserve(self):
        return self._is_reserve

    @is_reserve.setter
    def is_reserve(self, value):
        self._is_reserve = value
    # </editor-fold>

    def get_new_unique_id(self):
        result = TakingOffAircraft.next_taking_off_aircraft_id
        TakingOffAircraft.next_taking_off_aircraft_id += 1

        return result

    @staticmethod
    def sort_by_possible_moments(aircraft):
        return aircraft.calculating_moments.possible_taking_off

    @staticmethod
    def sort_by_permitted_moments(aircraft):
        return aircraft.calculating_moments.permitted_taking_off
