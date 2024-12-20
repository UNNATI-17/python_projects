print('Welcome to the Tip calculator!')
total_bill=float(input('what was the total bill?\n'))
tip=int(input('How much tip would you like to give? 10,12, or 15?\n'))
people=int(input('How many people to split the bill?'))
pay=(((total_bill*tip)/100)+total_bill)/people
final_amount=round(pay,2)
print('Each person should pay:\n',final_amount)
