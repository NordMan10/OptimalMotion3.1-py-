

class IMassServiceZone(object):
    """Определяет методы зоны массового облуживания."""

    def get_free_interval(self, new_interval):
        pass

    def add_aircraft_interval(self, aircraft_id, free_interval):
        pass

    def remove_aircraft_interval(self, aircraft_id):
        pass

    def reset(self):
        pass
