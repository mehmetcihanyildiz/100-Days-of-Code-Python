print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

tip_as_percent = tip / 100

total_tip_amount = bill * tip_as_percent

total_bill = bill + total_tip_amount

split_number = int(input("How many people to split the bill? "))

bill_per_person = total_bill / split_number

final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")

