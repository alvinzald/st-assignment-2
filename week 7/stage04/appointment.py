from datetime import date, time
from enum import Enum

from patient import Patient
from practitioner import Practitioner


class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class Appointment:
    def __init__(
        self,
        appointment_date: date,
        appointment_time: time,
        patient: Patient,
        practitioner: Practitioner
    ):
        self.set_date(appointment_date)
        self.set_time(appointment_time)
        self.set_patient(patient)
        self.set_practitioner(practitioner)

        self.__status = AppointmentStatus.SCHEDULED

    def set_date(self, appointment_date: date):
        if appointment_date is None:
            raise ValueError("Appointment date cannot be empty")
        self.__date = appointment_date

    def get_date(self) -> date:
        return self.__date

    def set_time(self, appointment_time: time):
        if appointment_time is None:
            raise ValueError("Appointment time cannot be empty")
        self.__time = appointment_time

    def get_time(self) -> time:
        return self.__time

    def set_patient(self, patient: Patient):
        if patient is None:
            raise ValueError("Appointment must have a patient")
        self.__patient = patient

    def get_patient(self) -> Patient:
        return self.__patient

    def set_practitioner(self, practitioner: Practitioner):
        if practitioner is None:
            raise ValueError("Appointment must have a practitioner")
        self.__practitioner = practitioner

    def get_practitioner(self) -> Practitioner:
        return self.__practitioner

    def get_status(self) -> AppointmentStatus:
        return self.__status

    def update_status(self, new_status: AppointmentStatus) -> None:
        if self.__status != AppointmentStatus.SCHEDULED:
            raise ValueError(
                "Completed or cancelled appointments cannot change status"
            )

        if new_status not in (
            AppointmentStatus.COMPLETED,
            AppointmentStatus.CANCELLED
        ):
            raise ValueError("Invalid status transition")

        self.__status = new_status

    def check_duplicate(self, other: "Appointment") -> bool:
        return (
            self.__date == other.__date
            and self.__time == other.__time
            and self.__practitioner == other.__practitioner
        )