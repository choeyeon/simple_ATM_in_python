while True:
    balance = 100000
    print("ATM")
    print("""
    1)      Balance
    2)      Withdraw
    3)      Deposit
    4)      Exit 
    """) 
    try:
        option = int(input("Enter Option "))
    except Exception as e:
        print("Error:", e)
        print("Enter 1, 2, 3 or 4 only")
        continue
    if option==1:
        print("Balance", balance)
    if option==2:
        print("Balance", balance)
        withdraw=float(input("Enter Withdraw amount "))
        if withdraw>0:
            balancenow=(balance-withdraw)
            print("Balance", balancenow)
        elif withdraw>balance:
            print("No funs in accaunt")
        else:
            print("None withdraw made")
    if option==3:
        print("Balance ", balance)
        deposit=float(input("Enter deposit amoun "))
        if deposit>0:
            balancenow=(balance+deposit)
            print("Balance", balancenow)
        else:
            print("None deposit made")
    if option==4:
        exit()