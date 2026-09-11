# Stage 1 Lab - Human vs AI: Building Your First SmartCare Prototype

------------

------------

## Learning objectives

------------

- Create and run a simple Python file with basic input,output and processing statements
- Use lists, dictionaries and functions to enhance the Python file
- Build a small SmartCare appointment prototype.
- Use AI as a tutor rather than a replacement.
- Compare human-written and AI-generated code.
- Verify AI-generated code through execution and test inputs.
- Document a short AI-use reflection.

## Files to create and commit in GitHub

------------

stage01/
- smartcare_v01.py
- comparison.md
- reflection.md
- ai_usage.md

## Part A - Understand the Problem: AI OFF

------------

SmartCare needs a small prototype that allows a receptionist to record patient appointments. Each  appointment records patient name, practitioner name and appointment time.
1. **What data must be stored?**\
    patient_name, practitioner_name, and appointment_time.
2. **What functions might be useful?**\
    create_appointment, view_appointment, edit_appointment, cancel_appointment, search_appointment, view_availability
3. **What could go wrong?**\
    duplicate bookings, human errors (typos, misclicks)
4. **What requirements are unclear?**\
    booking durations

## Part B - Build a Human-Written Prototype: AI OFF

------------

### Task 1 : Create and run a simple Python file with basic input,output statements

```python
print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

# First Appointment
patient1_name = 'Alice Smith'
practitioner1_name = 'Dr. John Doe'
appointment1_time = '2024-07-20 10:00 AM'
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time:{appointment1_time}")

# Second Appointment
patient2_name = 'Bob Johnson'
practitioner2_name = 'Dr. Jane Roe'
appointment2_time = '2024-07-20 11:30 AM'
print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time:{appointment2_time}")
```

### Task 1 enhanced : Use lists, dictionaries and functions to enhance the Python file

```python

appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")

print("Welcome to SmartCare: The Clinical Appointment Booking System!")
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')
display_appointments()
```
Limitations:
1. The system does not allow the user to input appointment bookings.
2. The system does not allow the user to cancel appointment bookings.
3. The system does not allow the user to view patient records.
4. When input is added, the system does not prevent double bookings.
5. The system will not list the appointments in chronological order.
6. The system does not have a way to search for specific appointments and will instead just list all of them.

## Part C - Use AI as Tutor: AI ON (Use only UC approved GenAI Tool such as Microsoft Copilot)

--------

Suggested prompt structure:
> Act as a Python tutor.\
> I am learning introductory software technology.\
> Here is a small appointment-booking function.
> 1. Explain what the code does.
> 2. Identify three limitations.
> 3. Suggest improvements.
> 4. Do not rewrite the whole application.
> 5. Ask me two questions to test my understanding.

## Part D - Generate an Alternative: AI ON

--------

Ask AI to create a simple beginner-friendly Python function that stores patient name, practitioner name and appointment time. Explicitly prohibit a database or GUI.

## Part E - Compare Human and AI Versions

| Question | Human version | AI version | 
| --- | --- | --- |
| Easy to understand? | Yes | Yes | 
| Runs successfully? | Yes | No |
| Uses only required features? | Yes | Yes |
| Adds assumptions? | No | Yes |
| Could I explain it? | Yes | Yes |

## Part F - Verify Behaviour

- Normal appointment
- Blank patient name
- Two appointments for the same practitioner/time
- Strange input such as patient_name=None or appointment_time=None

Behaviours could not be verified since the AI-generated code seems to have made the assumption that the code it was asked for was just part of a bigger system. It did not have any way to add entries and such.

## Part G - Improve One Thing

Choose exactly one controlled improvement, for example: if not patient_name: raise ValueError("Patient name cannot be empty")

## Part H - Reflection (150-250 words)

What did you build before using AI?\
What did AI help you understand?\
Did AI make assumptions?\
How did you verify the AI output?\
What engineering work remained for you?

Before using AI, I made a simple program that displayed a list of appointments for the clinic. I was able to complete the tasks on my own, but AI helped me understand what improvements could be made and gave me a deeper understanding on why classes should be used instead of just lists. When using AI to create the code, AI made a lot of assumptions on what already exists. It seems that in order to use AI, you have to be very specific so that it really knows what it should be doing. In that sense, it is still very important for the user to have a lot of knowledge in software engineering, to ensure the code produced will actually act as intended and fit the requirements from the client.
