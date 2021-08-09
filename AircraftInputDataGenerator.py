import random

import enums.AircraftPriorities
import enums.AircraftTypes
import static.ProgramConstants
import static.CommonInputData
import AircraftInputData
import TakingOffAircraftCreationMoments
import TakingOffAircraftCreationIntervals
import static.DataRandomizer
#from AircraftInputData import * // ? Проверь, можно ли импортировать так


class AircraftInputDataGenerator(object):
    """Класс для генерации входных данных для каждого ВС."""

    pass 


    @staticmethod
    def get_aircraft_input_data(self, planned_taking_off_moment, runways):
        runway_id = str(runways[random.randrange(ProgramConstants.start_id_value, len(runways))].id)
        special_place_id = random.randrange(ProgramConstants.start_id_value, CommonInputData.space_place_count + 1)

        aircraft_type = random.choice(list(AircraftTypes)).name

        priority = _get_aircraft_priority()
        processing_necessity = _get_processing_necessity()

        creation_moments = TakingOffAircraftCreationMoments(planned_taking_off_moment)
        creation_intervals = _get_taking_off_aircraft_creation_intervals()

        return AircraftInputData(runway_id, special_place_id, aircraft_type, priority, processing_necessity, 
		creation_moments, creation_intervals);


    @staticmethod
    def _get_aircraft_priority(self):
        priority = 0

        priority_value = random.randrange(0, 11)
        if (priority_value == 1):
            priority = AircraftPriorities.HIGH
        elif (priority_value < 4):
            priority = AircraftPriorities.MEDIUM
        else:
            priority = AircraftPriorities.DEFAULT

        return priority


    @staticmethod
    def _get_processing_necessity(self):
        processing_necessity_variants = [True, False]
        return processing_necessity_variants[random.randrange(len(processing_necessity_variants))]


    @staticmethod
    def _get_taking_off_aircraft_creation_intervals(self):
        motion_from_parking_to_PS = DataRandomizer.get_randomized_value(ProgramConstants.motion_from_parking_to_PS, 25, 15)
        motion_from_PS_to_ES = DataRandomizer.get_randomized_value(ProgramConstants.motion_from_PS_to_ES, 25, 15)
        motion_from_parking_to_SP = DataRandomizer.get_randomized_value(ProgramConstants.motion_from_parking_to_SP, 25, 15)
        motion_from_SP_to_PS = DataRandomizer.get_randomized_value(ProgramConstants.motion_from_SP_to_PS, 25, 15)
        processing_time = DataRandomizer.get_randomized_value(ProgramConstants.processing_time, 25, 15)
        taking_off_interval = DataRandomizer.get_randomized_value(ProgramConstants.taking_off_interval, 25, 15)

        return TakingOffAircraftCreationIntervals(motion_from_parking_to_PS, motion_from_PS_to_ES, motion_from_parking_to_SP, 
                                                  motion_from_SP_to_PS, processing_time, taking_off_interval);
