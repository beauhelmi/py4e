hours = input("Enter Hours:") # input() function always returns a string
rate = input("Enter Rate:") # input() function always returns a string 
try: # try to convert the input to a float
    total_hours = float(hours) # if it fails, the except block will run
    total_rate = float(rate) # if it fails, the except block will run
except: # if the try block fails, this block will run instead
    print("Error, please enter numeric input") # print an error message
    quit()  # quit the program if the input is not numeric
    print("Total Hours:", total_hours) # this line will not run if the input is not numeric
if total_hours > 40 : # if working hours is more than 40 hours
    print("You have worked Overtime") # print overtime message
    regularpay = total_rate * total_hours # calculate regular pay
    overtimepay = (total_hours - 40.0) * (total_rate * 0.5) #  calculation for overtime pay
    total_rate = regularpay + overtimepay #  calculation for total pay
    print("Your Regular Pay amount is:", regularpay) #  print regular pay
    print("You Overtime Pay amount is:", overtimepay) #  print overtime pay

else: #  if working hours is less than 40 hours
    print("You work Regular hours") #  print regular hours message
    total_rate = total_rate * total_hours # calculation for regular pay

print("You full payment is:",total_rate) # print total pay

