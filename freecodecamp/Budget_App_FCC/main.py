import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")                  # NAME OF CATEGORY
food.deposit(1000, "initial deposit")           # DEPOSIT
food.withdraw(10.15, "groceries")               # WITHDRAW
food.withdraw(15.89,                            # WITHDRAW
              "restaurant and more food for dessert")
print(food.get_balance())                       # GET BALANCE
clothing = budget.Category("Clothing")          # NAME OF CATEGORY
food.transfer(50, clothing)                     # TRANSFER
clothing.withdraw(25.55)                        # WITHDRAW
clothing.withdraw(100)                          # WITHDRAW
auto = budget.Category("Auto")                  # NAME OF CATEGORY
auto.deposit(1000, "initial deposit")           # DEPOSIT
auto.withdraw(15)                               # WITHDRAW no description

print(food)                                     # PRINT CATEGORY food
print(clothing)                                 # PRINT CATEGORY clothing
print(auto)                                     # PRINT CATEGORY auto

print(create_spend_chart([food, clothing, auto]))

# Run unit tests automatically
main(module='test_module', exit=False)