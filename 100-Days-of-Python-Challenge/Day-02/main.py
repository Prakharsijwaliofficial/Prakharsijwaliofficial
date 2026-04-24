print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip1 = bill * (tip/100)
each_person = (bill + tip1) / people

print(f"Each people should pay: ${each_person}")
