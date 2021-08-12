import random

from enums.AircraftPriorities import AircraftPriorities
from enums.AircraftTypes import AircraftTypes
from static.ProgramConstants import ProgramConstants
from static.CommonInputData import CommonInputData
from AircraftInputData import AircraftInputData
from TakingOffAircraftCreationMoments import TakingOffAircraftCreationMoments
from TakingOffAircraftCreationIntervals import TakingOffAircraftCreationIntervals
from static.DataRandomizer import DataRandomizer


class AircraftInputDataGenerator(object):
    """Класс для генерации входных данных для каждого ВС.

    Генерирует входные данные для конкретного ВС, используя заранее созданные данные из классов CProgramConstants, CCommonInputData,
    а также данные, прописаные напрямую в методах.
    """

    @staticmethod
    def get_aircraft_input_data(planned_taking_off_moment, runways):
        """
        Составляет набор входящих данных для ВС по указанному плановыму моменту.

        :param planned_taking_off_moment: Список плановых моментов
        :param runways: Список ВПП
        :return: Входные данные для ВС в виде экземпляра класса CAircraftInputData.
        """

        runway_id = str(runways[random.randrange(0, len(runways))].id)
        special_place_id = random.randrange(ProgramConstants.start_id_value, CommonInputData.special_place_count + 1)

        aircraft_type = random.choice(list(AircraftTypes)).name

        priority = AircraftInputDataGenerator._get_aircraft_priority()
        processing_necessity = AircraftInputDataGenerator._get_processing_necessity()

        creation_moments = TakingOffAircraftCreationMoments(planned_taking_off_moment)
        creation_intervals = AircraftInputDataGenerator._get_taking_off_aircraft_creation_intervals()

        return AircraftInputData(runway_id, special_place_id, aircraft_type, priority, processing_necessity,
                                 creation_moments, creation_intervals)

    @staticmethod
    def _get_aircraft_priority():
        """
        Определяет значение приритета для ВС с неравномерным распределением.

        :return: Значение приоритета в виде int.
        """

        priority = AircraftPriorities.DEFAULT

        priority_value = random.randrange(0, 11)
        if priority_value == 1:
            priority = AircraftPriorities.HIGH
        elif priority_value < 4:
            priority = AircraftPriorities.MEDIUM

        return priority

    @staticmethod
    def _get_processing_necessity():
        """
        Определяет признак необходимости обработки, генерируемый случайным образом.

        :return: Значение bool, определяющее необходимость обработки.
        """

        processing_necessity_variants = [True, False]
        return processing_necessity_variants[random.randrange(len(processing_necessity_variants))]

    @staticmethod
    def _get_taking_off_aircraft_creation_intervals():
        """
        Создает набор интервалов для ВС в виде экземпляра класса CTakingOffAircraftCreationIntervals
	    (нужен, пока данные для каждого ВС не будут передаваться другим способом).
	    Значения интервалов задаются с некоторым разбросом от среднего значения.

        :return: Набор интервалов для ВС.
        """

        motion_from_parking_to_PS = DataRandomizer.\
            get_randomized_value(ProgramConstants.motion_from_parking_to_PS, 25, 15)

        motion_from_PS_to_ES = DataRandomizer.get_randomized_value(ProgramConstants.motion_from_PS_to_ES, 25, 15)

        motion_from_parking_to_SP = DataRandomizer.\
            get_randomized_value(ProgramConstants.motion_from_parking_to_SP, 25, 15)

        motion_from_SP_to_PS = DataRandomizer.get_randomized_value(ProgramConstants.motion_from_SP_to_PS, 25, 15)

        processing_time = DataRandomizer.get_randomized_value(ProgramConstants.processing_time, 25, 15)

        taking_off_interval = DataRandomizer.get_randomized_value(ProgramConstants.taking_off_interval, 25, 15)

        return TakingOffAircraftCreationIntervals(motion_from_parking_to_PS, motion_from_PS_to_ES,
                                                  motion_from_parking_to_SP,
                                                  motion_from_SP_to_PS, processing_time, taking_off_interval)
