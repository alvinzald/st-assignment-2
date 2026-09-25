from datetime import date, time, datetime

from patient import Patient
from practitioner import Practitioner
from appointment import Appointment, AppointmentStatus


patients = []
practitioners = []
appointments = []


def book_appointment(
    patient: Patient,
    practitioner: Practitioner,
    appointment_date: date,
    appointment_time: time
):
    appointment = Appointment(
        appointment_date,
        appointment_time,
        patient,
        practitioner
    )

    appointments.append(appointment)
    print("Appointment booked successfully!")


def show_appointments():
    if not appointments:
        print("No appointments recorded.")
        return

    for index, appointment in enumerate(appointments):
        print(
            f"{index + 1}. "
            f"Patient: {appointment.get_patient().get_name()} | "
            f"Practitioner: {appointment.get_practitioner().get_name()} | "
            f"Date: {appointment.get_date()} | "
            f"Time: {appointment.get_time()} | "
            f"Status: {appointment.get_status().value}"
        )


def change_appointment_status():
    if not appointments:
        print("No appointments recorded.")
        return

    show_appointments()

    try:
        choice = int(input("Choose an appointment: "))

        appointment = appointments[choice - 1]

        print("\n1. Completed")
        print("2. Cancelled")

        status_choice = input("Choose new status: ")

        if status_choice == "1":
            appointment.update_status(AppointmentStatus.COMPLETED)

        elif status_choice == "2":
            appointment.update_status(AppointmentStatus.CANCELLED)

        else:
            print("Invalid status option.")
            return

        print("Appointment status updated successfully.")

    except (ValueError, IndexError) as error:
        print(error)


while True:
    print("\nSmartCare")
    print("1. Create patient")
    print("2. Create practitioner")
    print("3. Book appointment")
    print("4. Show appointments")
    print("5. Change appointment status")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        try:
            name = input("Enter patient name: ")

            patient = Patient(name)
            patients.append(patient)

            print("Patient created successfully.")

        except ValueError as error:
            print(error)

    elif choice == "2":
        try:
            identifier = input("Enter practitioner identifier: ")
            name = input("Enter practitioner name: ")
            specialty = input("Enter practitioner specialty: ")

            practitioner = Practitioner(
                identifier,
                name,
                specialty
            )

            practitioners.append(practitioner)

            print("Practitioner created successfully.")

        except ValueError as error:
            print(error)

    elif choice == "3":
        patient_name = input("Enter patient name: ")
        practitioner_name = input("Enter practitioner name: ")

        patient = None
        practitioner = None

        for current_patient in patients:
            if current_patient.get_name() == patient_name:
                patient = current_patient

        for current_practitioner in practitioners:
            if current_practitioner.get_name() == practitioner_name:
                practitioner = current_practitioner

        if patient is None:
            print("Patient not found.")
            continue

        if practitioner is None:
            print("Practitioner not found.")
            continue

        try:
            date_input = input("Enter appointment date (YYYY-MM-DD): ")
            time_input = input("Enter appointment time (HH:MM): ")

            appointment_date = datetime.strptime(
                date_input,
                "%Y-%m-%d"
            ).date()

            appointment_time = datetime.strptime(
                time_input,
                "%H:%M"
            ).time()

            book_appointment(
                patient,
                practitioner,
                appointment_date,
                appointment_time
            )

        except ValueError as error:
            print(error)

    elif choice == "4":
        show_appointments()

    elif choice == "5":
        change_appointment_status()

    elif choice == "6":
        print("Goodbye.")
        break

    else:
        print("Invalid option.")