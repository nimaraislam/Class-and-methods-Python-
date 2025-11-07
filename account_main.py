from account import Account

def main():
    print("============Transaction============")
    while True:
        while True:
                owner=input("Enter name: ").lower().strip()
                if not owner:
                    print(f"Name is empty.")
                    continue
                break
        my_account = Account(owner,0.00)
        print(f"----Welcome {owner.title()}----")
        while True:
            print("1.Press D for deposit.")
            print("2.Press W for withdraw.")
            print("3.Press B to check balance.")
            print("4.Press Q for exit.")
            input_trn=input("> ").upper().strip()
            if input_trn == "D":
                    try:
                        amount_deposit= input("Enter amount(>0): ").strip()
                        amount_deposit_float=float(amount_deposit)
                        deposit_result = my_account.deposit(amount_deposit_float)
                        if not deposit_result:
                            print(f"Deposit amount cannot be zero or negative.")
                        else:
                            print(f"Your deposit has been done successfully.Your balance is {my_account.get_balance():.2f} kr now.")
                    except ValueError:
                        print(f"Invalid amount.")
            elif input_trn == "W":
                    try: 
                        amount_withdraw= input("Enter amount(>0): ").strip()
                        amount_withdraw_float=float(amount_withdraw)
                        withdraw_result = my_account.withdraw(amount_withdraw_float) 
                        if not withdraw_result:
                            print(f"Withdraw amount cannot be zero or negative.")
                        else:
                            balance = my_account.get_balance()
                            if amount_withdraw_float > balance:
                                print(f"Your withdraw amount cannot be greater than your balance.Your balance is {my_account.get_balance():.2f} kr now.")
                                continue
                            else:
                                print(f"Your deposit has been done successfully.Your balance is {my_account.get_balance():.2f} kr now.")  
                    except ValueError:
                            print(f"Invalid amount.")
            elif input_trn == "B":
                print(f"***Your balance is {my_account.get_balance():.2f} kr now.***")
            elif input_trn == "Q":
                break
            #else :
            #     print("Invalid input.")
        break

if __name__ == "__main__":
    main()