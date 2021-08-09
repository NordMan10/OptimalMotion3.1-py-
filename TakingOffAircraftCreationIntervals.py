class TakingOffAircraftCreationIntervals(object):
    """Набор интервалов, получаемых во входных данных для взлетающего ВС."""

    def __init__(self, motionFromParkingToPS, motionFromPSToES, motionFromParkingToSP,
	             motionFromSPToPS, processing, takingOff):
        """Constructor.

        Keyword arguments:
        motionFromParkingToPS -- Время руления от парковки до ПРДВ. 
        motionFromPSToES -- Время руления от ПРДВ до ИСП.
        motionFromParkingToSP -- Время руления от парковки до Спец. площадки.
        motionFromSPToPS -- Время руления от Спец. площадки до ПРДВ.
        processing -- Время обработки.
        takingOff -- Время взлета.
        """
        self.motionFromParkingToPS = motionFromParkingToPS
        self.motionFromPSToES = motionFromPSToES
        self.motionFromParkingToSP = motionFromParkingToSP
        self.motionFromSPToPS = motionFromSPToPS
        self.processing = processing
        self.takingOff = takingOff


    def GetMotionFromParkingToPS(self):
        return self.motionFromParkingToPS

    def GetMotionFromPSToES(self):
        return self.motionFromPSToES

    def GetMotionFromParkingToSP(self):
        return self.motionFromParkingToSP

    def GetMotionFromSPToPS(self):
        return self.motionFromSPToPS

    def GetProcessing(self):
        return self.processing

    def GetTakingOff(self):
        return self.takingOff
