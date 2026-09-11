# SmartCare v0.2 - Requirements Specification Template

-----

-----

## 1. Problem and Scope

-----

### Problem

SmartCare needs a system that assist its users in handling appointment bookings as well as keeping patient records and GP availability.

###  Scope 

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


## 2. Stakeholders 

-----

| Stakeholder | Need | Evidence |
|:---|:---|:---|
| Reception | Prevent duplicate appointment bookings.<br> Access patient records easily.<br> Maintain consistent appointment status information.<br> View practitioner availability.<br> Automate cancellation process.<br> View reliable appointment history. | The case study lists duplicate bookings, difficulty finding records, inconsistent statuses, limited availability visibility, manual cancellations, and unreliable appointment history. |
| GPs | Access patient records easily.<br> Have consistent appointment status information.<br> View their availability and appointments.<br> View reliable appointment history. | The case study highlights problems with patient records, appointment status, practitioner availability, and appointment history. GP access is a reasonable assumption that should be validated. |
| Management | Have reliable appointment history.<br> Produce basic operational reports.<br> Have a simple system appropriate for the clinic. | The case study states that appointment history is unreliable, reports are difficult to produce, and management wants a simple system for a small clinic. |
| Patients | Prevent duplicate appointment bookings.<br> Have consistent appointment information.<br> Cancel appointments. Patients are affected by duplicate bookings, inconsistent appointment information, and manual cancellations, although direct patient use of the system is not stated. |


## 3. Functional Requirements

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

## 4. Non-Functional Requirements

-----

| ID | Description | 
|:---|:---|
| NFR-01 | The system shall display requested patient, appointment, or GP information within 2 seconds. |
| NFR-02 | The system shall prevent the application from ending when an invalid input is entered and display a clear error message when the inputing invalid information. |
| NFR-03 | The system shall generate operational reports within 1 minute. |

## 5. User Stories

-----

US-01: As a receptionist, I want to create a patient's record so that this information can be reused easily. 
US-02: As a receptionist, I want to create a new appointment booking for a patient with a GP so that this can be recorded in the system. 
US-03: As a receptionist, I want to view GP availability so that I know for when I can book the patient. 
US-04: As a receptionist, I want the system to prevent me from making a booking on an unavailable time so that there will be no double bookings. 
US-05: As a GP, I want to view my upcoming appointments so that I can attend them.

## 6. Acceptance Criteria

-----

US-02 - Create a new appointment booking
- GIVEN a patient record exists, a GP exists, and appointment time is available
- WHEN the receptionist creates an appointment
- THEN the appointment should be added to the list of appointments

US-03 - View GP availability
- GIVEN a GP's schedule exists
- WHEN the receptionist views their availability
- THEN the system should display the GP's available appointment times

US-04 - Prevent double bookings
- GIVEN a GP already has an appointment at the selected time
- WHEN the receptionist tries to book a patient in on an unavailable time
- THEN the system should reject a booking and display an error message

Classify each significant AI suggestion as Accepted, Modified, Rejected, or Unverified. Explain the evidence
used.

## 7. Assumptions and Open Questions

-----

## 8. AI Requirements Review Record

-----

| AI Suggestion | Evidence? | Decision | Reason | 
| --- | --- | --- | --- |
| "Appointment availability" is ambiguous | The scope (S‑05) and user stories imply availability is needed, but do not define how it is determined | Unverified | The case study does not explain what appointment availability is based on. Will need to ask client. |
| Patients listed as stakeholders but no patient-facing requirements | Stakeholder needs vs FR list mismatch | Rejected | Patients are beneficiaries to the functional requirements listed despite not directly using the system. |
| NFR-02 and NFR-03 overlap | Both refer to invalid input handling | Accepted | Both NFR go hand-in hand and will be merged. |            
  