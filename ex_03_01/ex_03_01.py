hours = input("Enter Hours:") # input() function always returns a string
rate = input("Enter Rate:")
total_hours = float(hours)
total_rate = float(rate)
print("Total Hours:", total_hours)
if total_hours > 40:
    print("You have worked Overtime")
    regularpay = total_rate * total_hours
    overtimepay = (total_hours - 40.0) * (total_rate * 0.5)
    total_rate = regularpay + overtimepay
    print("Your Regular Pay amount is:", regularpay)
    print("You Overtime Pay amount is:", overtimepay)

else:
    print("You work Regular hours")
    total_rate = total_rate * total_hours
print("You full payment is:",total_rate)
