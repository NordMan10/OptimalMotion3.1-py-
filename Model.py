import copy

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
        self._set_PS_waiting_time(ordered_configured_taking_off_aircrafts)

        # Упорядочим список ВС по разрешенным моментам
        ordered_configured_taking_off_aircrafts.sort(key=TakingOffAircraft.sort_by_permitted_moments)

        # Заполняем набор данных о ВС
        for aircraft in ordered_configured_taking_off_aircrafts:
            table_row = self._get_table_row(aircraft)
            table_rows.append(table_row)

        # Возвращаем строки данных для таблицы
        return table_rows

    def _get_ordered_configured_taking_off_aircrafts(self, unused_planned_taking_off_moments):
        # Создаем список ВС
        taking_off_aircrafts = []

        # Создаем упорядоченный список плановых моментов на основе переданного списка
        ordered_planned_taking_off_moments = copy.deepcopy(unused_planned_taking_off_moments)
        ordered_planned_taking_off_moments.sort()

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

    # noinspection PyPep8Naming
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

    def _reconfigure_aircrafts_with_reserve(self, ordered_taking_off_aircrafts):
        # Создаем список использованных индексов
        used_indexes = []

        # Берем каждый ВС
        for i in range(0, len(ordered_taking_off_aircrafts)):
            # Проверяем, использовался ли уже этот индекс ВС
            if i in used_indexes:
                # Если да, то пропускаем его
                continue

            # Если нет, то:

            # Получаем возможный момент ВС
            possible_moment = ordered_taking_off_aircrafts[i].calculating_moments.possible_taking_off

            # Пытаемся получить ближайший к возможному моменту разрешенный момент
            nearest_permitted_moment = CommonInputData.input_taking_off_moments.get_nearest_permitted_moment(possible_moment)
            # Проверяем
            if nearest_permitted_moment is None:
                # Если получили nullptr, значит разрешенный момент не найден
                # Отмечаем это соответствующим значением
                ordered_taking_off_aircrafts[i].calculating_moments.start = -1
                ordered_taking_off_aircrafts[i].calculating_moments.permitted_taking_off = -1
                # И пропускаем это ВС
                continue

            # Если же получили не nullptr, то отмечаем, что это проверенный разрешенный момент
            verified_permitted_moment = nearest_permitted_moment

            # Рассчитываем задержку для текущего ВС, возможный момент которого мы рассматриваем
            start_delay = verified_permitted_moment - possible_moment
            # Рассчитываем момент старта для этого же ВС
            current_aircraft_start_moment = ordered_taking_off_aircrafts[i].calculating_moments.start + start_delay

            # Получаем список стартовых моментов для резервных ВС
            reserve_aircraft_start_moments = self._get_reserve_aircraft_start_moments(verified_permitted_moment, i, ordered_taking_off_aircrafts)

            # Создаем один общий список пар значений <индекс ВС : момент старта> для текущего и резервных ВС
            all_aircraft_start_moments_data = {i: current_aircraft_start_moment}
            [all_aircraft_start_moments_data.update({aircraft_index: start_moment}) for aircraft_index, start_moment in
             reserve_aircraft_start_moments.items()]

            # Задаем моменты старта для текущего и резервных ВС
            self._set_prepared_start_moments(all_aircraft_start_moments_data, ordered_taking_off_aircrafts)

            # Получаем индекс ВС, имеющего наибольший приоритет (среди текущего и резервных ВС)
            most_priority_aircraft_index = self._get_most_priority_aircraft_index(all_aircraft_start_moments_data, ordered_taking_off_aircrafts)

            # Берем каждую пару значений из созданного общего списка ВС
            for aircraft_index, start_moment in all_aircraft_start_moments_data.items():
                # Задаем разрешенный момент
                ordered_taking_off_aircrafts[aircraft_index].calculating_moments.permitted_taking_off = verified_permitted_moment
                # Сравниваем индекс ВС и индекс наиболее приритетного ВС
                if aircraft_index != most_priority_aircraft_index:
                    # Если данное ВС не является наиболее приоритетным => помечаем его как резервное
                    ordered_taking_off_aircrafts[aircraft_index].is_reserve = True
                    # Задаем резервный разрешенный момент (момент взлета, если это ВС останется резервным и не заменит главное ВС)
                    ordered_taking_off_aircrafts[aircraft_index].calculating_moments.reserve_permitted_taking_off = \
                        CommonInputData.input_taking_off_moments.get_next_permitted_moment()

                # Добавляем индекс текущего ВС в список использованных
                used_indexes.append(aircraft_index)

    def _get_reserve_aircraft_start_moments(self, permitted_moment, main_aircraft_index, ordered_taking_off_aircrafts):
        # Создаем словарь с ключами в виде индексов ВС и значениями в виде моментов старта
        reserve_start_moments_data = {}

        # Получаем список возможных моментов взлета
        possible_taking_off_moments = [aircraft.calculating_moments.possible_taking_off for aircraft in ordered_taking_off_aircrafts]

        # Проверяем, есть ли еще возможные моменты
        if main_aircraft_index < len(possible_taking_off_moments) - 1:
            # Определяем допустимое количество резервных ВС
            reserve_aircraft_count = self._get_reserve_aircraft_count(permitted_moment, main_aircraft_index, possible_taking_off_moments)

            for i in range(1, reserve_aircraft_count + 1):
                # Проверяем, есть ли еще возможные моменты и совпадают ли Id ВПП у ВС, которым принадлежат эти моменты
                if main_aircraft_index + 1 < len(possible_taking_off_moments) and \
                        ordered_taking_off_aircrafts[main_aircraft_index].runway_id == ordered_taking_off_aircrafts[
                        main_aircraft_index + i].runway_id:
                    # Берем возможный момент для резервного ВС
                    reserve_aircraft_possible_moment = possible_taking_off_moments[main_aircraft_index + i]

                    # Рассчитываем задержку для момента старта резервного ВС
                    start_delay = permitted_moment - reserve_aircraft_possible_moment
                    # Задаем момент старта для резервного ВС
                    reserve_start_aircraft_moment = ordered_taking_off_aircrafts[main_aircraft_index + i].calculating_moments.start + start_delay

                    # Добавляем момент старта
                    reserve_start_moments_data[main_aircraft_index + i] = reserve_start_aircraft_moment

        # Возаращаем либо пустой, либо заполненный старовыми моментами словарь
        return reserve_start_moments_data

    def _get_reserve_aircraft_count(self, permitted_moment, main_aircraft_index, possible_taking_off_moments):
        # Задаем  начальное количество резервных ВС
        reserve_aircraft_count = 0

        index = 0
        # Определяем максимально возможное количество резервных ВС.
        # Пока имеются возможные моменты и разрешенный момент входит в разрешенный страховочный интервал
        while main_aircraft_index + index < len(possible_taking_off_moments) - 1 and \
                permitted_moment - CommonInputData.spare_arrival_time_interval.start_moment >= \
                possible_taking_off_moments[main_aircraft_index + index]:
            # Увеличиваем количество резервных ВС
            reserve_aircraft_count += 1
            # Увеличиваем индекс
            index += 1

        # Проверяем полученное количество по заданному критерию
        # time_to_last_taking_off_moment = 0
        permitted_time = 0

        while True:
            # По заданному критерию, в зависимости от определенного количества резервных ВС, находим допустимое время простоя резервных ВС
            permissible_reserve_aircraft_count_list = CommonInputData.permissible_reserve_aircraft_count
            for aircraft_count, waiting_time in permissible_reserve_aircraft_count_list.items():
                if reserve_aircraft_count <= aircraft_count:
                    permitted_time = waiting_time
                    break

            # Рассчитываем время простоя (время, которое пройдет с момента взлета первого (основного) ВС до момента взлета последнего резервного ВС)
            time_to_last_taking_off_moment = possible_taking_off_moments[main_aircraft_index + reserve_aircraft_count] - \
                                             possible_taking_off_moments[main_aircraft_index]

            # Если рассчитанное время простоя больше допустимого => уменьшаем количество резервных ВС
            if time_to_last_taking_off_moment > permitted_time:
                reserve_aircraft_count -= 1

            # Повторяем, пока не удовлетровим заданному критерию
            if time_to_last_taking_off_moment <= permitted_time:
                break

        # Возвращаем количество резервных ВС
        return reserve_aircraft_count

    def _set_prepared_start_moments(self, all_aircraft_start_moments_data, ordered_taking_off_aircrafts):
        for aircraft_index, start_moment in all_aircraft_start_moments_data.items():
            ordered_taking_off_aircrafts[aircraft_index].calculating_moments.start = start_moment

    def _get_most_priority_aircraft_index(self, all_aircraft_start_moments_data, ordered_taking_off_aircrafts):
        most_priority_aircraft_index = list(all_aircraft_start_moments_data)[0]

        for aircraft_index, start_moment in all_aircraft_start_moments_data.items():
            if ordered_taking_off_aircrafts[aircraft_index].priority > ordered_taking_off_aircrafts[most_priority_aircraft_index].priority:
                most_priority_aircraft_index = aircraft_index

        return most_priority_aircraft_index

    # noinspection PyPep8Naming
    def _set_PS_waiting_time(self, ordered_configured_taking_off_aircrafts):
        for aircraft in ordered_configured_taking_off_aircrafts:
            # Рассчитываем момент прибытия на ПРДВ
            arrival_to_PS_moment = 0
            if aircraft.processing_necessity:
                arrival_to_PS_moment = aircraft.calculating_moments.start + aircraft.creation_intervals.motion_from_parking_to_SP + \
                                       aircraft.creation_intervals.processing + aircraft.creation_intervals.motion_from_SP_to_PS
            else:
                arrival_to_PS_moment = aircraft.creation_intervals.motion_from_parking_to_PS

            # Рассчитываем время простоя
            if aircraft.is_reserve:
                aircraft.calculating_intervals.PS_delay = aircraft.calculating_moments.reserve_permitted_taking_off - \
                                                          arrival_to_PS_moment - aircraft.creation_intervals.motion_from_PS_to_ES - \
                                                          aircraft.creation_intervals.taking_off
            else:
                aircraft.calculating_intervals.PS_delay = aircraft.calculating_moments.permitted_taking_off - \
                                                          arrival_to_PS_moment - aircraft.creation_intervals.motion_from_PS_to_ES - \
                                                          aircraft.creation_intervals.taking_off

    def _get_table_row(self, aircraft):
        # Рассчитываем общее время движения ВС (без учета времени обработки)
        aircraft_total_motion_time = aircraft.creation_intervals.taking_off + aircraft.creation_intervals.motion_from_PS_to_ES
        if aircraft.processing_necessity:
            aircraft_total_motion_time += aircraft.creation_intervals.motion_from_SP_to_PS + aircraft.creation_intervals.motion_from_parking_to_SP
        else:
            aircraft_total_motion_time += aircraft.creation_intervals.motion_from_parking_to_PS

        # Получаем значение разрешенного момента
        permitted_moment = str(aircraft.calculating_moments.permitted_taking_off) if aircraft.calculating_moments.permitted_taking_off != -1 else \
            "Не найден"
        # Получаем время обработки
        processing_time = str(aircraft.creation_intervals.processing) if aircraft.processing_necessity else "-"
        # Получаем Id Спец. площадки
        special_place_id = str(aircraft.special_place_id) if aircraft.processing_necessity else "-"

        # Извлекаем все оставшиеся необходимые данные из экземпляра ВС и озвращаем указатель на экземпляр класса CTableRow
        return TableRow(str(aircraft.id), str(aircraft.creation_moments.plannee_taking_off), str(aircraft.calculating_moments.possible_taking_off),
                        permitted_moment, str(aircraft.calculating_moments.start), str(aircraft_total_motion_time), str(processing_time),
                        aircraft.processing_necessity, str(aircraft.priority), aircraft.is_reserve, str(aircraft.calculating_intervals.PS_delay),
                        aircraft.runway_id, special_place_id)
