bankfirst = input("\nThis is the bank. What do you want to do? \n Check Balance (cb) \n Deposit (d) \n Withdraw (w) \n Change Account Info (ca) \n Delete Account (da) \n Modify Account (ma) \n Exit (e) \n\n")
balance = 0
placeholder = True
accountname = "John Doe"

def invalid():
    print("\nThis is not a valid option")

def exit():
   quit()
 
def checkbalance():
    global balance
    global accountname
    print("\n"+ accountname + " your current balance is " + "$" + str(balance))
    
def deposit():
    global balance
    global accountname
    dollar = float(input("\nType the amount you want to deposit "))
    rounddollar = round(dollar, 2)
    balance += rounddollar
    print("\n"+ accountname + " your new balance is " + "$" + str(balance))

def changeaccountinfo():
   global accountname
   accountname = input("\n" + accountname + " set a new username ")
   print("\n" + "Your new username is " + accountname)

def deleteaccount():
   print("\n" + "Your account will be deleted")
   quit()

def withdraw():
    global balance
    global accountname
    dollar = float(input("\nType the amount you want to withdraw "))
    rounddollar = round(dollar, 2)
    balance -= rounddollar
    print("\n"+ accountname + " your new balance is " + "$" + str(balance))

while placeholder:
  
  if bankfirst == "e":
    exit()
    bankfirst = input("\nThis is the bank. What do you want to do? \n Check Balance (cb) \n Deposit (d) \n Withdraw (w) \n Change Account Info (ca) \n Delete Account (da) \n Exit (e) \n\n")

  if bankfirst == "cb":
    checkbalance()
    bankfirst = input("\nThis is the bank. What do you want to do? \n Check Balance (cb) \n Deposit (d) \n Withdraw (w) \n Change Account Info (ca) \n Delete Account (da) \n Exit (e) \n\n")

  if bankfirst == "d":
    deposit()
    bankfirst = input("\nThis is the bank. What do you want to do? \n Check Balance (cb) \n Deposit (d) \n Withdraw (w) \n Change Account Info (ca) \n Delete Account (da) \n Exit (e) \n\n")

  if bankfirst == "w":
    withdraw()
    bankfirst = input("\nThis is the bank. What do you want to do? \n Check Balance (cb) \n Deposit (d) \n Withdraw (w) \n Change Account Info (ca) \n Delete Account (da) \n Exit (e) \n\n")

  if bankfirst == "ca":
    changeaccountinfo()
    bankfirst = input("\nThis is the bank. What do you want to do? \n Check Balance (cb) \n Deposit (d) \n Withdraw (w) \n Change Account Info (ca) \n Delete Account (da) \n Exit (e) \n\n")
  
  if bankfirst == "da":
    deleteaccount()

  if bankfirst != "cb" and bankfirst != "e" and bankfirst != "d" and bankfirst != "w" and bankfirst != "ca" and bankfirst!= "da":
     invalid()
     bankfirst = input("\nThis is the bank. What do you want to do? \n Check Balance (cb) \n Deposit (d) \n Withdraw (w) \n Change Account Info (ca) \n Delete Account (da) \n Exit (e) \n\n") 
     
  bankfirst = bankfirst
