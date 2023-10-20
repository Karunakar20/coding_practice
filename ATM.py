user = "user"
password = 1234
user_name = input("Enter user name:")
pass_word = int(input("Enter password:"))
amount = 0
s = '''
1. Deposit
2. Withdraw
3. Statement
4. Exit
'''
if user==user_name and password==pass_word:
    while True:
        print(s)
        options = int(input("Enter the option:"))
        if options==1:
            deposit = float(input("Enter the deposit amount:"))
            print("Deposit amount", amount+deposit)
        elif options==2:
            withdraw = float(input("Enter the withdraw amount:"))
            print("Deposit amount", amount-withdraw)
        elif options==3:
            print("Mini-Statement:", amount)
        elif options==4:
            break
else:
    print("Wrong details")
    