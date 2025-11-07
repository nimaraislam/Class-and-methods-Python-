from simple_scheduler import Reminder

def main():
    my_reminder = Reminder()
    print("---------Schedule System-------------")
    while True:
        print("1. Press A to add a reminder")
        print("2. Press D to check due reminders")
        print("3. Press Q to exit")
        input_option = input("> ").strip().upper()
        if input_option == "A":
            input_message=input("Enter message: ").capitalize().strip()
            while True:
                try:
                    input_minute=input("Enter minutes: ")
                    input_minute_int = int(input_minute)
                except ValueError:
                    print("Invalid minute.")
                break
            result = my_reminder.schedule(input_message,input_minute_int)
            print(result)
        #if input_option == "D":

        

if __name__ == "__main__":
        main()