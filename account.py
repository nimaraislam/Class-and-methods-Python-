class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = float(balance)#0.00

    def deposit(self,amount):
        if amount <= 0.00:
            return False
        else:
            self.balance += amount
            return True
    
    def withdraw(self,amount):
        if amount <= 0.00:
            return False
        elif amount > self.balance:
             return False
        else:
            self.balance -= amount
            return True
        
    def get_balance(self):
        return round(self.balance,2)
        

    