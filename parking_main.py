from parking import Parking
def main():
    my_parking = Parking()
    print("-----------Welcome to the parking system--------------")
    print(f"***Parking rate is per hour {my_parking.rate_per_hour} kr.***")
    while True:
        print("1.Press 1 to start parking.")
        print("2.Press 2 to stop parking.")
        print("3.Press 3 to calculate parking charge.")
        print("4.Press 4 to exit.")
        input_parking=input("> ").strip()
        if input_parking == "1":
            try:
                start_time=input("Enter start time(HH.MM,24hr format): ").strip()
                start_time_float= float(start_time)
                if(start_time_float<0):
                    print("Time cannot be negative.")
                    continue
                my_parking.start(start_time_float)
            except ValueError:
                    print("Invalid input")
        elif input_parking == "2":
            try:
                stop_time=input("Enter stop time(HH.MM,24hr format): ").strip()
                stop_time_float= float(stop_time)
                if(stop_time_float<0):
                    print("Time cannot be negative.")
                    continue
                stop_result=my_parking.stop(stop_time_float)
                if stop_result is not None:
                    print(f"**{stop_result}**")
            except ValueError:
                    print("Invalid input.")
        elif input_parking == "3":
             price_result= my_parking.price()
             print(f"**{price_result}**")
        elif input_parking == "4":
             break
        else:
             print("Invalid input.")
             
             


if __name__=='__main__':
    main()