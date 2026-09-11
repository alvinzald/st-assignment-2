#
# # task 1
# # Create and run a simple Python file with basic input,output statements
#
# print("Welcome to SmartCare: Community Clinic Appointment Booking System!")
#
# # First Appointment
# patient1_name = 'Alice Smith'
# practitioner1_name = 'Dr. John Doe'
# appointment1_time = '2024-07-20 10:00 AM'
# print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time:{appointment1_time}")
#
# # Second Appointment
# patient2_name = 'Bob Johnson'
# practitioner2_name = 'Dr. Jane Roe'
# appointment2_time = '2024-07-20 11:30 AM'
# print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time:{appointment2_time}")

# # task1enhanced
# # Use lists, dictionaries and functions to enhance the Python file
#
# appointments = []
#
# def book_appointment(patient_name, practitioner_name, appointment_time):
#     if not patient_name:
#         raise ValueError("Patient name cannot be empty")
#     appointment = {
#         "patient": patient_name,
#         "practitioner": practitioner_name,
#         "time": appointment_time
#     }
#     appointments.append(appointment)
#
# def display_appointments():
#     if not appointments:
#         print("No appointments recorded.")
#         return
#     for appointment in appointments:
#         print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")
#
# print("Welcome to SmartCare: The Clinical Appointment Booking System!")
# book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
# book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')
# display_appointments()

# from Microsoft Copilot

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
