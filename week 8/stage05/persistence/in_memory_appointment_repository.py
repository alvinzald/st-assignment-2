from repositories.appointment_repository import AppointmentRepository

class InMemoryAppointmentRepository(AppointmentRepository):

    def __init__(self):
        self.appointments = []

    def save(self, appointment):
        self.appointments.append(appointment)

    def get_all(self):
        return list(self.appointments)