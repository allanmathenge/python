from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2200, "Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposit(500)
Dave.withdraw(100)
Sara.withdraw(200)

Dave.transfer(22000, Sara)
Dave.transfer(200, Sara)

Jim = InterestRewardAcct(1000, "Jim")

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(1200, Dave)

Blaze = SavingsAcct(1000, "Blaze")

Blaze.getBalance()

Blaze.deposit(100)

Blaze.transfer(10000, Sara)
