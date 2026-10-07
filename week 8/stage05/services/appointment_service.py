from datetime import date, time

from domain.appointment import Appointment, AppointmentStatus
from domain.patient import Patient
from domain.practitioner import Practitioner


class AppointmentService:

    def __init__(self, appointment_repository):
        self.appointment_repository = appointment_repository

    def check_duplicate(
        self,
        practitioner: Practitioner,
        appointment_date: date,
        appointment_time: time
    ):
        appointments = self.appointment_repository.get_all()

        for appointment in appointments:
            if (
                appointment.get_practitioner() == practitioner
                and appointment.get_date() == appointment_date
                and appointment.get_time() == appointment_time
                and appointment.get_status() != AppointmentStatus.CANCELLED
            ):
                return True

        return False

    def book_appointment(
        self,
        patient: Patient,
        practitioner: Practitioner,
        appointment_date: date,
        appointment_time: time
    ):
        if self.check_duplicate(
            practitioner,
            appointment_date,
            appointment_time
        ):
            raise ValueError(
                "Practitioner already has an appointment at this time."
            )

        appointment = Appointment(
            appointment_date,
            appointment_time,
            patient,
            practitioner
        )

        self.appointment_repository.save(appointment)

        return appointment

    def get_appointments(self):
        return self.appointment_repository.get_all()

    def change_appointment_status(self, appointment, new_status):
        appointment.update_status(new_status)