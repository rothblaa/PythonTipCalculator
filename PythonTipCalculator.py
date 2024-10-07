
#tasks
#-------------------------------

#make a tip calculator
#display a welcome message
print("Welcome to the tip calculator!")

#input for total bill
bill = float(input("What was the total bill?\n $"))

#input for how much tip you'd like to give: 10, 12, or 15
tip = int(input("How much tip would you like to leave?\n"))
monetizedTip = float(1 + (tip / 100))

#input for how many people will split the bill
people = int(input("How many people are going to split the bill?\n"))

#logic to figure out the total
totalBillPerPerson = (bill / people) * monetizedTip

#give the total number each person should pay rounded to 2 decimal places 
finalAmount = round(totalBillPerPerson, 2)
print(f"The total each person needs to pay is: ${finalAmount}")


