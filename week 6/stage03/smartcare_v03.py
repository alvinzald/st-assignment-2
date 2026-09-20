class Patient:
    def __init__(self, name):
        self.id = None
        self.name = name

    def set_name(self, name):
        pass

    def get_name(self):
        pass


class Practitioner:
    def __init__(self, name):
        self.id = None
        self.name = name
        self.availability = []

    def set_name(self, name):
        pass

    def get_name(self):
        pass

    def add_availability(self):
        pass

    def remove_availability(self):
        pass

    def get_availability(self):
        pass


class Appointment:
    def __init__(self, date, time, patient, practitioner):
        self.id = None
        self.date = date
        self.time = time
        self.status = None
        self.patient = patient
        self.practitioner = practitioner

    def update_status(self):
        pass

    def check_duplicate(self):
        pass

appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    """Store a basic appointment using only Python lists and dictionaries."""

    # Basic validation
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    if not practitioner_name:
        raise ValueError("Practitioner name cannot be empty")
    if not appointment_time:
        raise ValueError("Appointment time cannot be empty")

    # Create a dictionary to represent one appointment
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    # Store it in the list
    appointments.append(appointment)

    print("Appointment booked successfully!")


def show_appointments():
    """Display all stored appointments."""
    if not appointments:
        print("No appointments recorded.")
        return

    for appt in appointments:
        print(f"Patient: {appt['patient']} | Practitioner: {appt['practitioner']} | Time: {appt['time']}")
