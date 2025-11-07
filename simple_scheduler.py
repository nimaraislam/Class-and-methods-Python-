import time
class Reminder:
    def __init__(self):
        self.reminder_list = []

    def schedule(self,message,minute):
        if not message:
            return "Message cannot be empty."
        elif minute<0:
            return ("Invalid minute!")
        self.reminder_list.append((message,minute))
        return f"Reminder scheduled for minutes {minute}"
    
    def due(self,current_time):
        due_now = []
        for message,minute in self.reminder_list:
            if minute== current_time:
                due_now.append(message)

        self.reminder_list= [r for r in self.reminder_list if r[1]!=current_time]
        return due_now

my_reminder = Reminder()
print(my_reminder.schedule("Take a break", 5))
print(my_reminder.schedule("Meeting starts", 10))

print(my_reminder.due(5))   # → ['Take a break']
print(my_reminder.due(5))   # → [] (already removed)
print(my_reminder.due(10))