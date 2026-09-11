# Assignment 2 – Case Study Lab Stage 2 Lab Activities SmartCare Requirements Engineering

-----

-----

## Learning Objectives

-----

- Analyse the SmartCare client brief.
- Identify stakeholders and scope.
- Write functional and non-functional requirements.
- Develop user stories and Given-When-Then acceptance criteria.
- Use AI to critique requirements without allowing it to invent stakeholder needs.
- Produce SmartCare Requirements Specification v1.0.

## Part A - Client Brief: AI OFF

-----

SmartCare uses spreadsheets and paper records. Staff report duplicate bookings, difficulty finding patient
information, inconsistent appointment status and limited appointment history. Management wants a small,
maintainable patient, practitioner and appointment system.

> SmartCare needs a system that assist its users in handling appointment bookings as well as keeping patient records and GP availability.

## Part B - Stakeholders and Scope: AI OFF

-----

### Stakeholders 
| Stakeholder | Possible need |
|:---|:---|
| Reception | Prevent duplicate appointment bookings.<br> Access patient records easily.<br> Maintain consistent appointment status information.<br> View practitioner availability.<br> Automate cancellation process.<br> View reliable appointment history. |
| GPs | Access patient records easily.<br> Have consistent appointment status information.<br> View their availability and appointments.<br> View reliable appointment history. |
| Management | Have reliable appointment history.<br> Produce basic operational reports.<br> Have a simple system appropriate for the clinic. |
| Patients | Prevent duplicate appointment bookings.<br> Have consistent appointment information.<br> Cancel appointments.

### Scope 
| ID | Activity | Status |
|:---|:---|:---|
| S-01 | Manage patient information | Confirmed |
| S-02 | Manage GP records | Confirmed |
| S-03 | Manage appointments | Confirmed |
| S-04 | Prevent duplicate bookings | Confirmed |
| S-05 | View appointment availability | Confirmed |
| S-06 | Produce basic operational reports | Confirmed |
| S-07 | Cancel appointment (patient) | Provisional |
| S-08 | Process payment | Out of scope |
| S-09 | Process insurance claim | Out of scope |

## Part C - Functional Requirements: AI OFF

-----

| ID | Description |
|:---|:---|
| FR-01 | The system shall allow staff to create new patient records. |
| FR-02 | The system shall allow staff to view patient information. |
| FR-03 | The system shall allow staff to edit patient information. |
| FR-04 | The system shall allow staff to create GP records. |
| FR-05 | The system shall allow staff to view GP information. |
| FR-06 | The system shall allow staff to record GP availability |
| FR-07 | The system shall allow staff to add an appointment booking. |
| FR-08 | The system shall prevent conflicting appointment bookings. |
| FR-09 | The system shall allow staff to edit appointment details. |
| FR-10 | The system shall keep a history of patient appointments. |
| FR-11 | The system shall generate operational reports for management. |

## Part D - Non-Functional Requirements: AI OFF

-----

| ID | Description | 
|:---|:---|
| NFR-01 | The system shall display requested patient, appointment, or GP information within 2 seconds. |
| NFR-02 | The system shall display a clear error message when the inputing invalid information. |
| NFR-03 | The system shall prevent the application from ending when an invalid input is entered. |
| NFR-04 | The system shall generate operational reports within 1 minute. |

## Part E - User Stories and Acceptance Criteria: AI OFF

-----

### User Stories

1. As a receptionist, I want to create a patient's record so that this information can be reused easily.
2. As a receptionist, I want to create a new appointment booking for a patient with a GP so that this can be recorded in the system.
3. As a receptionist, I want to view GP availability so that I know for when I can book the patient.
4. As a receptionist, I want the system to prevent me from making a booking on an unavailable time so that there will be no double bookings.
5. As a GP, I want to view my upcoming appointments so that I can attend them.

### Acceptance Criteria

US-02 - Create a new appointment booking
- Given a patient record exists, a GP exists, and appointment time is available
- When the receptionist creates an appointment
- Then the appointment should be added to the list of appointments

US-03 - View GP availability
- Given a GP's schedule exists
- When the receptionist views their availability
- Then the system should display the GP's available appointment times

US-04 - Prevent double bookings
- Given a GP already has an appointment at the selected time
- When the receptionist tries to book a patient in on an unavailable time
- The system should reject a booking and display an error message

## Part F - AI Requirements Review: AI ON

-----

Prompt: Act as a software requirements reviewer. Review the SmartCare requirements for ambiguity,
inconsistency, missing clarification questions and testability. Do NOT invent new client requirements. For every
suggestion, state whether it is based on evidence or is only a question/assumption requiring validation.

## Part G - VERIFY the AI Review

-----

Classify each significant AI suggestion as Accepted, Modified, Rejected, or Unverified. Explain the evidence
used.

| AI Suggestion | Status | Explanation | 
| --- | --- | --- |
| "Appointment availability" is ambiguous | Unverified | The case study does not explain what appointment availability is based on. Will need to ask client. |
| Patients listed as stakeholders but no patient-facing requirements | Rejected | Patients are beneficiaries to the functional requirements listed despite not directly using the system. |
| NFR-02 and NFR-03 overlap | Accepted | Both NFR go hand-in hand and will be merged. |            
  
## Part H - Finalise SmartCare v0.2

-----

Submit stakeholder analysis, scope, 8-12 FRs, 4-6 NFRs, 4-6 user stories, acceptance criteria,
assumptions/open questions and selected AI review evidence.

| ID | Description | 
|:---|:---|
| NFR-01 | The system shall display requested patient, appointment, or GP information within 2 seconds. |
| NFR-02 | The system shall prevent the application from ending when an invalid input is entered and display a clear error message when the inputing invalid information. |
| NFR-03 | The system shall generate operational reports within 1 minute. |


## Reflection

In 150-250 words: What did AI notice that you missed? What did AI invent or overreach on? Which requirement
changed after review? Why must requirements have evidence?

There were a bunch of details that AI noticed that I missed. I think this is caused by the fact that as a person, I already have an idea of how it should go and did think of being more specific in the document. However, there were also things that I feel should already be understood/given such as the patients being a stakeholder despite not explicit in the functional requirements. I read through the AI analysis and found that some suggestions can be accepted, some can be rejected, and some need further clarification. One instance of change I had to do was merging some NFR because they go hand-in-hand. Requirements need to have evidence because it explains why features/functions belong in a system. Without evidence, work and complexity could increase despite not being agreed on and vise versa.
