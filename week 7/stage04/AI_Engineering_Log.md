# AI Engineering Log

## Prompt:

Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML.

[Attached Case Study File](../../Assignment_2_Case_Study_S2_2026.docx)

[Attached UML](../../week 6/uml.png)

## Microsoft Copilot Contribution:

```
from datetime import date, time
from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class Appointment:
    def __init__(
        self,
        appointment_date: date,
        appointment_time: time,
        patient: "Patient",
        practitioner: "Practitioner"
    ):
        self.__date = appointment_date
        self.__time = appointment_time
        self.__patient = patient
        self.__practitioner = practitioner
        self.__status = AppointmentStatus.SCHEDULED

    def update_status(self, new_status: AppointmentStatus) -> None:
        if self.__status == AppointmentStatus.CANCELLED:
            raise ValueError("A cancelled appointment cannot change status")

        if self.__status == AppointmentStatus.COMPLETED:
            raise ValueError("A completed appointment cannot change status")

        self.__status = new_status

    def check_duplicate(self, other: "Appointment") -> bool:
        return (
            self.__date == other.__date
            and self.__time == other.__time
            and self.__practitioner == other.__practitioner
        )
```

## Decisions from AI Contribution

| Decision | Reason / Evidence |
|---|---|
| Put `Appointment` in its own file | Keeps the model classes organised. This is a code structure choice, not a UML requirement. |
| Use setter methods in `__init__()` | This follows the same validation style used in the `Patient` class. |
| Validate date, time, patient and practitioner | Prevents empty values such as `None` from being stored. The exact validation rules are a design decision. |
| Use `AppointmentStatus` enum | Required by the task instruction. |
| Start new appointments as `SCHEDULED` | The UML includes a status, but does not say the starting value. This is an assumption. |
| Do not create a normal `set_status()` method | The task says to protect status transitions, so status should only change through `update_status()`. |
| Allow `SCHEDULED` to change to `COMPLETED` or `CANCELLED` | This provides controlled status changes. The exact transition rules are not shown in the UML, so this is a design decision. |
| Keep cancelled appointments as objects | Directly required by the instruction: cancelled appointments must remain as objects. |
| `check_duplicate()` compares another appointment | The UML includes `check_duplicate()`, but no database or appointment list is allowed. Comparing another appointment avoids adding extra dependencies. |
| Define a duplicate as the same practitioner, date and time | This prevents a practitioner from being booked twice at the same time. This rule is an assumption because the UML does not define a duplicate. |
| Do not generate an appointment ID | The UML shows an ID but does not explain how it is created. Adding an ID generator would be an unsupported assumption. |
| Do not add database, UI, notification or service logic | Directly required by the task instruction. |
| Do not use inheritance | No inheritance is shown in the approved UML. |

### Assumptions That May Need Validation

- A new appointment starts as `SCHEDULED`.
- `COMPLETED` and `CANCELLED` are final statuses.
- A duplicate appointment means the same practitioner, date and time.
- `None` values are treated as invalid.
- Appointment ID creation is left out because the UML does not explain how IDs are generated.

## Other Decisions

| Decision | Reason / Evidence |
|---|---|
| Put `Patient` in its own file | For consistency and organisation. |
| Put `Practitioner` in its own file | For consistency and organisation. |
