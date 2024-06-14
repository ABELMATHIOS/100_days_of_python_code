print('welcom to the tip calculator!')
total_bill = float(input('What was the total bill? $'))
total_num_of_people = int(input('how many people to split the bill? '))
tip = float(input('How much tip would you like to give 10, 12, or 15? '))
tip_in_percent = total_bill * tip/100
bill_to_pay = total_bill + tip_in_percent
bill_amount = bill_to_pay/total_num_of_people

final_bill_to_pay = "{:.2f}".format(bill_amount)

print(f'Each person should pay: ${final_bill_to_pay}')