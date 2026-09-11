# Why Software Engineering Still Matters
*Stage 1 | Introducing Software Technology Case Study with Python and Guided AI use*

------------

------------

## Learning goals

------------

- Explain why software engineering is broader than coding.
- Identify stakeholders in a simple software problem.
- Recognise missing requirements.
- Critically evaluate AI-generated feature suggestions.
- Explain why AI output should not automatically be treated as correct.

## Activity 1 - Think-Pair-Share (10 minutes)

------------

If ChatGPT or Copilot can produce a 100-line Python application very quickly, what knowledge does a software engineer still need?

1. Software engineers need to understand the business problem so that they can design the software according to the user requirements.\
2. Software engineers need to know how to test, debug, and verify codes.\
3. Software engineers need to ensure that the program can be maintained and is secure.

## Activity 2 - Is This Software Engineering? (10 minutes)

------------

Scenario A: A student writes a 50-line Python calculator.<br>
Scenario B: A team develops a payroll system used by 5,000 employees.<br>
Scenario C: An AI assistant generates a simple appointment application from one prompt.<br>

| Scenario | Programming? | Software Engineering? | Why? |
|---|---|---|---|
| A | Yes | No | Code is being written to create an application but does not involve software engineering practices such as requirements analysis, documentation, and maintenance. |
| B | Yes | Yes | The team not only writes code but also handle requirement analysis, system architecture, testing, security, and maintenance. |
| C | No | Yes | The user does not write code so it is not programming, but it may be software engineering because the user would have needed to understand the requirements and deployment in order to get the AI assistant to generate this application. |

## Activity 3 - SmartCare Problem Analysis (20 minutes)

------------

Client statement: SmartCare Community Clinic currently uses spreadsheets and paper records to manage patients and appointments. The clinic wants  new software to improve these processes.

### Task 1 - Identify stakeholders

| Stakeholder | What do they need? |
|:---|:---|
| Reception | Prevent duplicate appointment bookings.<br> Access patient records easily.<br> Maintain consistent appointment status information.<br> View practitioner availability.<br> Automate cancellation process.<br> View reliable appointment history. |
| GPs | Access patient records easily.<br> Have consistent appointment status information.<br> View their availability and appointments.<br> View reliable appointment history. |
| Management | Have reliable appointment history.<br> Produce basic operational reports.<br> Have a simple system appropriate for the clinic. |
| Patients | Prevent duplicate appointment bookings.<br> Have consistent appointment information.<br> Cancel appointments.

### Task 2 - Identify current problems

1. Duplicate appointment bookings.
2. Difficulty locating patient records.
3. Inconsistent appointment status information.
4. Limited visibility of practitioner availability.
5. Manual cancellation processes.
6. Lack of reliable appointment history.
7. Difficulty producing basic operational reports.

### Task 3 - Ask client questions

1. Who are the users of the system? If the patient are also users of the system, can they also manage their appointments with the application or just view?
2. What patient information needs to be stored by the system?
3. What appointment information needs to be collected by the system? Are there pre-determined duration for each appointment such as 15-minute short consultations? What about reasons for booking/cancellation?
4. What information do we keep for each health practitioner?
5. What kind of operational reports does the management want the system to produce?
6. Assuming the system can be used by different types of users, who can create the accounts for login? Can each patient create their account or does the admin staff have to create it for them?

## Activity 4 - Critique an AI Response (15 minutes)

------------

An AI assistant suggests: appointment management; facial-recognition login; AI diagnosis recommendations; patient search; online payment; practitioner schedule view; insurance processing; automatic treatment-plan generation.

| Suggestion | Client evidence? | In Scope? | Decision |
|:---|:---|:---|:---|
| Appointment management | Yes | Yes | Include this feature. |
| Facial recognition login | No | No | Do not include. |
| AI diagnosis recommendations | No | No | Do not include. |
| Patient search | Yes | Yes | Include this feature. |
| Online payment | No | No | Do not include. | 
| Practitioner schedule view | Yes | Yes | Include this feature. |
| Insurance processing | No | No | Do not include. |
| Treatment-plan generation | No | No | Do not include. |

## Exit Question

------------

Write one activity that a software engineer must perform and that cannot safely be delegated entirely to AI.

- Software engineers must review and validate AI-generated code to ensure that the AI actually hits the requirements needed by the client.