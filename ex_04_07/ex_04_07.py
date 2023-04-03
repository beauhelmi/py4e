# write a grade program using a function that called computegrade that takes a score as its parameter and returns a grade as a string

def computegrade(score): # function definition
    if score >= 90: # if the score is greater than or equal to 90, then return 'A'
        return "A" # return statement
    elif score >= 80: # if the score is greater than or equal to 80, then return 'B'
        return 'B' # return statement
    elif score >= 70: # if the score is greater than or equal to 70, then return 'C'
        return 'C'  # return statement
    elif score >= 60:   # if the score is greater than or equal to 60, then return 'D'
        return 'D' # return statement
    else: # if the score is less than 60, then return 'F'
        return 'F' # return statement
while True: # do while loop to check for valid input
    try: # try block to check for valid input
        score = float(input("Enter score:")) # asking for user input
        if not (0 <= score <= 100): # in this case, the 'not' operator is used to reverse the boolean value of the expression
            print("Score must be between 0-100") # if the score is not between 0-100, then print this message
            continue # continue to the next iteration of the loop
        break # break out of the loop if the score is between 0-100
    except ValueError: # an exception is raised if the user enters a string
        print("Invalid input. Please enter a valid score between 0-100.")

grade = computegrade(score)
print("Your grade is: ", grade)
    
