class TableRow(object):
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
    def aircraft_id(self):
        return self._aircraft_id

    @property
    def planned_taking_off_moment(self):
        return self.planned_taking_off_moment

    @property
    def possible_taking_off_moment(self):
        return self.possible_taking_off_moment

    @property
    def permitted_taking_off_moment(self):
        return self.permitted_taking_off_moment

    @property
    def start_moment(self):
        return self.start_moment

    @property
    def total_motion_time(self):
        return self.total_motion_time

    @property
    def processing_time(self):
        return self._processing_time

    @property
    def processing_necessity(self):
        return self._processing_necessity

    @property
    def priority(self):
        return self.priority

    @property
    def is_reserved(self):
        return self.is_reserved

    @property
    def PS_waiting_time(self):
        return self.PS_waiting_time

    @property
    def runway_id(self):
        return self.runway_id

    @property
    def special_place_id(self):
        return self.special_place_id
