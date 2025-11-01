from badge_printer import BadgePrinter
def main():
    my_badge_printer = BadgePrinter()
    print("------Badge Printing--------")
    while True:
        input_first_name=input("Enter First Name: ")
        input_last_name=input("Enter Last Name: ")
        result = my_badge_printer.format_name(input_first_name,input_last_name)
        if "empty" in result or "Invalid" in result:
            print(result)
        else:
            print(f"Name : {result}")
            print(f"\n{my_badge_printer.print_badge(result)}")
        print("Do you want to continue?[Y/N]")
        input_continue=input("> ").strip().upper()
        if input_continue == "Y":
            continue
        elif input_continue == "N":
            break
        else:
            print("Invalid input")
            continue


if __name__=="__main__":
    main()
