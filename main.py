from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

options = Menu()
enough = CoffeeMaker()
cash = MoneyMachine()
power = 1

while(power):
# Ask customer what they want
  drink=input(f"What would you like to have : {options.get_items()}: ")

# reportfunctionality
  if drink=="report":
    enough.report()
    cash.report()
  elif drink=="off":
    print("The machine is switchg off")
    power = 0

  else:
# check if resources are sufficient  
    choice = options.find_drink(drink)
    if((enough.is_resource_sufficient(choice))):
    #askformoney
      fund = cash.make_payment(choice.cost)
      if(fund):
        enough.make_coffee(choice)   












#process coins 
#add money
#deductingredients
#makecoffee
#askcustomerwhattheywant