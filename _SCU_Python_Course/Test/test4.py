class Account:
    def __init__(self):
        self.money=100
    def withdraw(self,):
        num=input("Enter an amount to withdraw:")
        self.money-=int(num)
        print("\n\n")

    def deposit(self):
        num=input("Enter an amount to deposit:")
        self.money+=int(num)
        print("\n\n")
    def check_balance(self):
        print("The balance is "+str(self.money)+'\n\n')
    
accounts = list()
for i in range(10):
    accounts.append(Account())

while 1:
    choice=5
    id=int(input("Enter an id:"))
    if id>=0 and id<10:
        flag = 0
        while flag == 0:
            print("Main menu\n")
            print("1:check balance\n")
            print("2:withdraw\n")
            print("3:deposit\n")
            print("4:exit\n")
            choice=int(input("\nEnter a choice:"))
            if choice == 1:
                accounts[id].check_balance()
            elif choice == 2:
                accounts[id].withdraw()
            elif choice == 3:
                accounts[id].deposit()
            elif choice == 4:
                flag = 1
                print("\n\n")
            else :
                print("choice error\n\n")
