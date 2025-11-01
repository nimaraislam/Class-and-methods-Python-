from queue_management import TicketQueue
def main():
    my_ticket_Queue = TicketQueue()
    print("---------Queue Management System(FIFO)---------")
    while True:
        print("1. Press 1 to for generate a ticket")
        print("2. Press 2 to for deque")
        print("3. Press 3 to see all tickets")
        print("4. Press 4 to exit.")
        input_option=input("> ").strip()
        if input_option == "1":
            print("----Issues-----")
            print("Passowrd reset")
            print("Billing problem")
            print("Network issue")
            print("Subcription cancel")
            input_ticket=input("Enter your issue: ").strip().lower()
            result = my_ticket_Queue.enqueue(input_ticket)
            if result is None:
                  print("Ticket is empty.")
            else:
                 print(f"Your ticket for '{input_ticket.capitalize()}' has been generated successfully.\nYour queue number is '{result}'.")
        if input_option == "2":
            print("Process Next Ticket?[Y/N]")
            input_continue=input("> ").strip().upper()
            if input_continue == "Y":
                result_dequeue = my_ticket_Queue.dequeue()
                if result_dequeue is None:
                    print("The support queue is currently empty. No new cases to process.")
                else:
                    print(f"Process has been done.Your next case is: {result_dequeue}")
            elif input_continue == "N":
                break
                
                
            if input_option == "4":
                break




if __name__=="__main__":
    main()