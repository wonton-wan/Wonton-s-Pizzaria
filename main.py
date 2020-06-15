print("Hailo! and welcome to Wonton's Pizzaria!")
print("What pizza would you like to order")
pizzaOrder=input()
print("What size?")
pizzaSize=input()
print("Do you have any food related allergies?")
print("(If you have no food related allergies type in  none  )")
foodAllergies=input()
if foodAllergies=="none":
  print("Ok")
else:
    print("Thank you for letting me know!We will make sure to not have "+foodAllergies+" near your pizza.")
print("How much would you like to pay for this pizza?")
pizzaPrice=input()
if pizzaPrice=="$0":
  print("You have to pay something!") 
  print("try again.")
  pizzaPrice=input()
else:
    print("Your grand total is "+pizzaPrice+" USD.")
print("Thank you for ordering come back anytime!")