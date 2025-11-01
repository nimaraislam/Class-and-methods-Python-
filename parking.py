import math


class Parking:
    def __init__(self,rate_per_hour=20.00):
        self.rate_per_hour=20.00
        self.start_time=None
        self.stop_time=None

    def start(self,time):
        self.start_time=round(float(time),2)

    def stop(self,time):
        if self.start_time == None:
            return "You need to set start time."
        self.stop_time =round(float(time),2) 
            
    def price(self):
        if self.start_time == None:
            return "You need to set start time."
        elif self.stop == None:
            return "You need to set stop time."
        elif self.stop_time < self.start_time:
            self.stop_time =round(float(self.stop_time + 24),2)  
        duration = round((self.stop_time - self.start_time),2)
        hours = math.ceil(duration)
        price = self.rate_per_hour*hours
        return f"You have to pay {price:.2f} kr for {hours:.2f} hours."
    



