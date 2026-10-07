## Reflection

Document one AI suggestion accepted, one modified and one rejected/deferred

> The AI suggestions this week appears to be more relevant to the case than the suggestions given the previous weeks.
> Instead of getting suggestions that were obviously too much for the system, it gave me some suggestions that I really had to consider for the system.
> 
> One of the tasks I accepted was to return a copy of the list of appointments instead of returning the list of appointments itself.
> I accepted it because it fits the standard of encapsulation across the system and will prevent outside-functions to alter the list without going through validation.
> 
> A suggestion given to me that I had to modify was to create a separate ConsoleUI class to encapsulate the presentation layer.
> However, I did not think a class was necessary for this, and I ended up just using functions but in a separate .py file.
> 
> Then, I rejected the suggestion of using ABC and @abstractmethod to avoid unnecessary complexity.
> 
> Additionally, I asked it to give me a suggestion regarding an issue I've been thinking about: we have a duplicate checker, but it will not prevent an appointment being booked a minute later.
> It suggested I define how long each appointment should be, and then check the new appointment's starting time against the duration window from existing appointments.
> However, I decided to skip this for now until the case study is more clear in terms of the duration of each appointment and the adding of practitioner's availabilities.