from AircraftInputDataGenerator import AircraftInputDataGenerator
from static.ProgramConstants import ProgramConstants
from Runway import Runway
from SpecialPlace import SpecialPlace
from TableRow import TableRow
from TakingOffAircraft import TakingOffAircraft
from Interval import Interval
from static.CommonInputData import CommonInputData


class Model(object):
    """"""

    def __init__(self, runway_count, special_place_count):
        self._runways = []
        self._special_places = []
        # self._aircraft_input_data_generator = AircraftInputDataGenerator()
        self.init_runways(runway_count)
        self.init_special_places(special_place_count)

    @property
    def runways(self):
        return self._runways

    @property
    def special_places(self):
        return self._special_places

    def init_runways(self, runway_count):
        for i in range(ProgramConstants.start_id_value, runway_count + ProgramConstants.start_id_value):
            self.runways.append(Runway(str(i)))

    def init_special_places(self, special_place_count):
        for i in range(ProgramConstants.start_id_value, special_place_count + ProgramConstants.start_id_value):
            self.special_places.append(SpecialPlace(i))

    def get_output_data(self, unused_planned_taking_off_moments):
        # Создаем набор данных о ВС в формате строки таблицы
        table_rows = []

        # Получаем список ВС с заданными возможными и стартовыми моментами, упорядоченный по возможным моментам
        ordered_configured_taking_off_aircrafts = self._get_ordered_configured_taking_off_aircrafts(
            unused_planned_taking_off_moments)

        # Задаем разрешенные моменты и резервные ВС в полученном списке ВС
        self._reconfigure_aircrafts_with_reserve(ordered_configured_taking_off_aircrafts)

        # Для всех ВС задаем время ожидания на ПРДВ
        self.set_PS_waiting_time(ordered_configured_taking_off_aircrafts)

        # Создаем список ВС, упорядоченных по разрешенным моментам
        aircrafts_ordered_by_permitted_moments = ordered_configured_taking_off_aircrafts.sort()

        # Заполняем набор данных о ВС
        for aircraft in ordered_configured_taking_off_aircrafts:
            table_row = self.get_table_row()
            table_rows.append(table_row)

        # Возвращаем строки данных для таблицы
        return table_rows

    def _get_ordered_configured_taking_off_aircrafts(self, unused_planned_taking_off_moments):
        # Создаем список ВС
        taking_off_aircrafts = []

        # Создаем упорядоченный список плановых моментов на основе переданного списка
        ordered_planned_taking_off_moments = unused_planned_taking_off_moments.sort()

        start_delay = 0

        # Берем каждый плановый момент
        for i in range(0, len(ordered_planned_taking_off_moments)):
            # Генерируем входные данные для нового ВС
            aircraft_input_data = AircraftInputDataGenerator. \
                get_aircraft_input_data(ordered_planned_taking_off_moments[i], self.runways)
            # Создаем ВС
            taking_off_aircraft = TakingOffAircraft(aircraft_input_data)
            start_moment = 0

            # Рассчитываем интервал взлета
            taking_off_interval = Interval(taking_off_aircraft.creation_moments.planned_taking_off -
                                           taking_off_aircraft.creation_intervals.taking_off,
                                           taking_off_aircraft.creation_moments.planned_taking_off)

            # Получаем задержку
            start_delay = self._get_runway_start_delay(taking_off_aircraft, taking_off_interval)

            # Если нужна обработка
            if taking_off_aircraft.processing_necessity:
                # Рассчитываем и задаем момент старта при необходимости обработки
                SP_arrive_moment = taking_off_interval.start_moment - taking_off_aircraft.creation_intervals.motion_from_PS_to_ES - \
                                   taking_off_aircraft.creation_intervals.motion_from_SP_to_PS - \
                                   taking_off_aircraft.creation_intervals.processing

                # Получаем задержку
                start_delay += self._get_special_place_start_delay(taking_off_aircraft, SP_arrive_moment)

                start_moment = SP_arrive_moment - taking_off_aircraft.creation_intervals.motion_from_parking_to_SP + \
                               start_delay - CommonInputData.spare_arrival_time_interval.end_moment

            else:
                # Рассчитываем и задаем момент старта при отсутствии необходимости обработки
                start_moment = taking_off_interval.start_moment - taking_off_aircraft.creation_intervals.motion_from_PS_to_ES - \
                               taking_off_aircraft.creation_intervals.motion_from_parking_to_PS + start_delay - \
                               CommonInputData.spare_arrival_time_interval.end_moment

            # Задаем рассчитанный момент старта текущему ВС
            taking_off_aircraft.calculating_moments.start = start_moment
            # Рассчитываем и задаем возможный момент взлета
            taking_off_aircraft.calculating_moments.possible_taking_off = taking_off_aircraft.creation_moments.planned_taking_off + start_delay

            taking_off_aircrafts.append(taking_off_aircraft)

        # Упорядочиваем ВС по возможному моменту
        taking_off_aircrafts.sort(key=TakingOffAircraft.sort_by_possible_moments)

        # Возвращаем упорядоченный список ВС
        return taking_off_aircrafts

    def _get_runway_start_delay(self, taking_off_aircraft, taking_off_interval):
        # Находим ВПП, на которую движется ВС
        this_runway = next(runway for runway in self.runways if runway.id == taking_off_aircraft.runway_id)

        # Получаем свободный интервал от ВПП
        free_runway_interval = this_runway.get_free_interval(taking_off_interval)

        # Добавляем полученный новый интервал в ВПП
        this_runway.add_aircraft_interval(taking_off_aircraft.id, free_runway_interval)

        # Рассчитываем и возвращаем задержку
        return free_runway_interval.start_moment - taking_off_interval.start_moment

    def _get_special_place_start_delay(self, taking_off_aircraft, SP_arrive_moment):
        # Находим Спец. площадку, на которую движется ВС
        this_special_place = next(special_place for special_place in self.special_places if special_place.id ==
                                  taking_off_aircraft.special_place_id)

        # Создаем интервал обработки ВС
        processing_interval = Interval(SP_arrive_moment,
                                       SP_arrive_moment + taking_off_aircraft.creation_intervals.processing)

        # Передаем интервал обработки ВС и получаем свободный интервал от Спец. площадки
        free_SP_interval = this_special_place.get_free_interval(processing_interval)

        # Добавляем полученный новый интервал в Спец. площадку
        this_special_place.add_aircraft_interval(taking_off_aircraft.id, free_SP_interval)

        # Рассчитываем и возвращаем задержку
        return free_SP_interval.start_moment - processing_interval.start_moment

    def _reconfigure_aircrafts_with_reserve(self, ordered_configured_taking_off_aircrafts):
        # Создаем список использованных индексов
        used_indexes = []

        # Берем каждый ВС
        for i in range(0, len(ordered_configured_taking_off_aircrafts)):
            # Проверяем, использовался ли уже этот индекс ВС
            if i in used_indexes:
                # Если да, то пропускаем его
                continue

            # Если нет, то:

            # Получаем возможный момент ВС
            possible_moment = ordered_configured_taking_off_aircrafts[i].calculating_moments.possible_taking_off

            # Пытаемся получить ближайший к возможному моменту разрешенный момент
            nearest_permitted_moment = CommonInputData.input_taking_off_moments.get_nearest_permitted_moment(possible_moment)

