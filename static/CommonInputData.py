import InputTakingOffMoments
import Interval


class CommonInputData(object):
    """description of class"""

    runway_count = 2

    special_place_count = 2

    input_taking_off_moments = InputTakingOffMoments(
        [600, 630, 680, 700, 750, 1040, 1290, 1310, 1500, 1580], 
        [660, 750, 790, 850, 880, 940, 1060, 1120, 1200, 1280, 1670, 
	        1700, 1760, 1800, 1900, 2000, 2090, 2150, 2240, 2390, 2500])

    spare_arrival_time_interval = Interval(20, 50)

    permissible_reserve_aircraft_count = { 0: sys.maxsize,
		                                   1: 300,
		                                   2: 240,
		                                   3: 180,
		                                   4: 120,
		                                   5: 10,
		                                   sys.maxsize: 0 }

