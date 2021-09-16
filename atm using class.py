class bank():
    "the bank of python "
    owner = "likith"
    def __init__(self):
        self.balance = 0
        print("the account  was created ".capitalize)

    def deposit(self):
        amount = int(input("enter the amount to deposit -->"))
        self.balance = self.balance + amount
        print("deposit is sucessful the remaining balance is -->",self.balance,)

    def withdraw(self):
        amount = int(input("enter the amount to withdraw -->"))
        if(self.balance >= amount):
            print("withdraw is sucessful take you amount",amount)
            self.balance = self.balance - amount
            print("the remaining amount is ",self.balance)
        else:
            print("sorry you cant withdraw")

    def enquiry(self):
        print("the balance in your account is ",self.balance)


account = bank()

account.deposit()
account.withdraw()
account.enquiry()





        
