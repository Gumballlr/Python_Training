from Bank import *

# Minh = BankAccount(1000, "Minh")

Minh = InterestRewardAcc(5000, "Minh")
Minh.getBalance()
Minh.deposit(100) # 5000+ 100 + 5 = 5210


Ngoc = SavingAcc(1000, "Ngoc")
Ngoc.deposit(100) # 1105
Ngoc.withDraw(200) # -200 -5 =900
Ngoc.transferToAccount(100, Minh) #900 - 100-5 = 795
#Minh = 5105 + 100 +5 = 5210

Minh.transferToAccount(100, Ngoc)
# Minh = 5210 - 100 =5110
# Ngoc = 795 + 100 + 5 = 900