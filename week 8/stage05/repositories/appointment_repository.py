class AppointmentRepository:

    def save(self, appointment):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError