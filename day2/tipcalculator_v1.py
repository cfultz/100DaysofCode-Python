print("Welcome to the Tip Calculator Python Script")

bill = float(input("What was the total bill? $ " ))
tip = int(input("What percentage tip would you like to give? 15, 20, or 25? "))
folks = int(input("How many folks are splitting this bill? "))

bill_with_tip = tip / 100 * bill + bill

pay_per_person = bill / folks
pay_per_person = round(pay_per_person, 2)
pay_per_person = "{:.2f}".format(pay_per_person)

print(f"Each person should pay: ${pay_per_person}")
