import random


class DataRandomizer(object):
    """description of class"""

    @staticmethod
    def get_randomized_value(value, dispersion, step):
        if (dispersion == 0 or step == 0):
            return value

        minValue = value - (value * float(dispersion) / 100)
        maxValue = value + (value * float(dispersion) / 100)

        possibleValues = []

        possibleValue = minValue
        while possibleValue <= maxValue:
            possibleValues.append(possibleValue)
            possibleValue += step

        randomValueIndex = random.randrange(len(possibleValues))
        return possibleValues[randomValueIndex]