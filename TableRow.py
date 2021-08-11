class TableRow(object):
    def __init__(self, aircraft_id, planned_taking_off_moment, possible_taking_off_moment, permitted_taking_off_moment,
                 start_moment, total_motion_time, processing_time, processing_necessity, priority, is_reserved,
                 PS_waiting_time, runway_id, special_place_id):
        self.t_aircraft_id = aircraft_id
        self.t_planned_taking_off_moment = planned_taking_off_moment
        self.t_possible_taking_off_moment = possible_taking_off_moment
        self.t_permitted_taking_off_moment = permitted_taking_off_moment
        self.t_start_moment = start_moment
        self.t_total_motion_time = total_motion_time
        self.t_processing_time = processing_time
        self.t_processing_necessity = processing_necessity
        self.t_priority = priority
        self.t_is_reserved = is_reserved
        self.t_PS_waiting_time = PS_waiting_time
        self.t_runway_id = runway_id
        self.t_special_place_id = special_place_id

    @property
    def aircraft_id(self):
        return self.t_aircraft_id

    @property
    def planned_taking_off_moment(self):
        return self.t_planned_taking_off_moment

    @property
    def possible_taking_off_moment(self):
        return self.t_possible_taking_off_moment

    @property
    def permitted_taking_off_moment(self):
        return self.t_permitted_taking_off_moment

    @property
    def start_moment(self):
        return self.t_start_moment

    @property
    def total_motion_time(self):
        return self.t_total_motion_time

    @property
    def processing_time(self):
        return self.t_processing_time

    @property
    def processing_necessity(self):
        return self.t_processing_necessity

    @property
    def priority(self):
        return self.t_priority

    @property
    def is_reserved(self):
        return self.t_is_reserved

    @property
    def PS_waiting_time(self):
        return self.t_PS_waiting_time

    @property
    def runway_id(self):
        return self.t_runway_id

    @property
    def special_place_id(self):
        return self.t_special_place_id
