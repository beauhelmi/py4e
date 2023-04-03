# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate

def computepay(hours, rate):
    print("In computepay", hours, rate)
    if hours > 40 :
        print("You have worked Overtime")
        regularpay = rate * hours
        overtimepay = (hours - 40.0) * (rate * 0.5)
        total_rate = regularpay + overtimepay
        print("Your Regular Pay amount is:", regularpay)
        print("You Overtime Pay amount is:", overtimepay)
    else :
        print("You have work Regular hours")
        total_rate = rate * hours
        print("Your Regular pay amount is:",total_rate)
    return total_rate

hours = input('Enter Hours: ')
rate = input("Enter Rate: ")
fhours = float(hours)
frate = float(rate)
fullpay = computepay(fhours, frate)

print("You full payment is:", fullpay)