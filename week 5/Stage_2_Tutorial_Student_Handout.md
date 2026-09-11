# Assignment 2 Case Study Stage 2 Tutorial From Problems to Requirements

-----

-----

## Learning goals

-----

- Analyse stakeholders.
- Distinguish functional and non-functional requirements.
- Recognise ambiguity and unsupported requirements.
- Define scope.
- Develop user stories and acceptance criteria.
- Critique AI-generated requirements.

## Activity 1 - Stakeholder Map

-----

| Stakeholder | Need | Potential Conflict
|:---|:---|:---| 
| Reception | Prevent duplicate appointment bookings.<br> Access patient records easily.<br> Maintain consistent appointment status information.<br> View practitioner availability.<br> Automate cancellation process.<br> View reliable appointment history. | May change bookings that affect GP schedule. |
| GPs | Access patient records easily.<br> Have consistent appointment status information.<br> View their availability and appointments.<br> View reliable appointment history. | May change their availability despite a booking already existing. |
| Management | Have reliable appointment history.<br> Produce basic operational reports.<br> Have a simple system appropriate for the clinic. | May want automatically generated monthly reports which will make the system more complex. |
| Patients | Prevent duplicate appointment bookings.<br> Have consistent appointment information.<br> Cancel appointments. | May want to manage their own bookings without going through the receptionist. |

## Activity 2 - Functional or Non-Functional?

-----

- [X] Functional - The system shall allow staff to cancel an appointment.
- [X] Non-functional - The system should remain responsive for the course-scale dataset.
- [X] Functional - The system shall retain cancelled appointments.
- [X] Non-functional - Core business logic should be independently testable.
- [X] Functional - The system shall search for a patient by ID.

## Activity 3 - Repair Ambiguous Requirements

-----

1. *The system should be easy to use.*\
Problem: "easy to use" is subjective and immeasurable.\
Clarification question: How can "easy to use" be measured?
2. *Patient search should be fast.*\
Problem: "Fast" is vague and does not have a standard measure\
Clarification question: How quickly should search results appear?
3. *The system should securely manage data.*\
Problem: "Securely" is also vague and does not state security requirements\
Clarification question: What measures are needed to consider the data management to be secure?
4. *Appointments should normally be easy to cancel.*\
Problem: "Easy" is again subjective\
Clarification question: In what conditions can and cannot be canceled? How long should it take?

## Activity 4 - AI Requirements Audit

-----

Classify each suggestion: Confirmed / Assumption requiring validation / Unsupported / Out of scope.

| AI suggestion | Classification | Evidence / reason |
| --- | --- | --- |
| Patients receive SMS reminders. | Out of scope | Patient notifications are not included in the case study. |
| Facial recognition login | Out of scope | This feature is too advanced/complicated for the system. The case did not even specify login capabilities. |
| Receptionists create appointments | Confirmed | The case mentions that receptionist should be able to record patient appointments. |
| Online payment | Out of scope | Payment and insurance handling are not included in the case. The focus is on handling appointment management. |
| Practitioners view schedules | Assumption requiring validation | Practitioner availability is crucial to the system but does not specify how the GPs themselves will use the system. |
| AI recommends treatments | Out of scope | The system does not go beyond simple clinic appointment management. |
| Cancelled appointments remain in history | Assumption requiring validation | The case study requires appointment history and the functiont o cancel appointments, but does not explicitly mention keeping cancelled appointments in its history. |

## Exit question

-----

Why is 'Ai suggested it' not sufficient evidence for a requirement?

> AI suggestions can be totally different from what the client wants. Evidence should be supported by the requirements based on client and stakeholder needs.
 
