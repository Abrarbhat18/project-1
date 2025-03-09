import time

class ATM:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_number, pin, balance=0):
        if account_number in self.accounts:
            print("Account already exists!")
        else:
            self.accounts[account_number] = {'pin': pin, 'balance': balance}
            print("Account created successfully!")
    
    def authenticate(self, account_number, pin):
        if account_number in self.accounts and self.accounts[account_number]['pin'] == pin:
            return True
        else:
            print("Invalid account number or PIN!")
            return False
    
    def deposit(self, account_number, amount):
        if amount > 0:
            self.accounts[account_number]['balance'] += amount
            print(f"Deposited {amount}. New Balance: {self.accounts[account_number]['balance']}")
        else:
            print("Invalid deposit amount!")
    
    def withdraw(self, account_number, amount):
        if amount > 0 and self.accounts[account_number]['balance'] >= amount:
            self.accounts[account_number]['balance'] -= amount
            print(f"Withdrawn {amount}. New Balance: {self.accounts[account_number]['balance']}")
            receipt = input("Do you want to print a receipt? (yes/no): ").strip().lower()
            if receipt == 'yes':
                self.print_receipt(account_number, amount)
        else:
            print("Insufficient balance or invalid amount!")
    
    def check_balance(self, account_number):
        print(f"Available Balance: {self.accounts[account_number]['balance']}")
    
    def print_receipt(self, account_number, amount):
        print("\n********** ATM RECEIPT **********")
        print(f"Account Number: {account_number}")
        print(f"Withdrawn Amount: {amount}")
        print(f"Remaining Balance: {self.accounts[account_number]['balance']}")
        print("Thank you for using our ATM!")
        print("*********************************")

def main():
    atm = ATM()
    
    while True:
        print("\n1. Create Account\n2. Login & Use ATM\n3. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            acc_num = input("Enter new account number: ")
            pin = input("Set a 4-digit PIN: ")
            atm.create_account(acc_num, pin)
        
        elif choice == '2':
            acc_num = input("Enter account number: ")
            pin = input("Enter PIN: ")
            if atm.authenticate(acc_num, pin):
                while True:
                    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Logout")
                    option = input("Select an option: ")
                    if option == '1':
                        amount = float(input("Enter amount to deposit: "))
                        atm.deposit(acc_num, amount)
                    elif option == '2':
                        amount = float(input("Enter amount to withdraw: "))
                        atm.withdraw(acc_num, amount)
                    elif option == '3':
                        atm.check_balance(acc_num)
                    elif option == '4':
                        print("Logging out...")
                        time.sleep(1)
                        break
                    else:
                        print("Invalid option!")
        
        elif choice == '3':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option! Try again.")

if __name__ == "__main__":
    main()
