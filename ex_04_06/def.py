

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
    

print(greet('en'), 'Glenn')
print(greet('es'), 'Sally')
print(greet('fr'), 'Michael')


# Built-in functions
big = max('Hello World')
# The max() function returns the largest of its arguments
print(big)

def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)
# The len() function returns the length of its argument
# You can use len() to count the number of characters in a string
len('Hello World')

# Type conversion functions
int('32')

# Random numbers
import random # The function random() returns a random float between 0.0 and 1.0


# Exercise 1: run the program on your system and see what numbers you get. Run the program more than once and see what numbers you get.

random.randint(5, 10)
# to choose an element from a sequence at random, you can use choice:
t = [1, 2, 3]
random.choice(t)

# Math functions
# Python has a math module that provides most of the familiar mathematical functions. 
import math
# this statement creates a module object named math
print('math')
# The math module also provides access to the underlying C library functions for floating point math:
print(math.pi)

# Adding new functions
# You can create a new function with the def statement. The function definition creates a function object and assigns it to a name:
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

# Flow of execution
# execution always begins at the first statement of the program
# Statements are executed one at a time, in order from top to bottom

# Parameters and arguments
def print_twice(bruce):
    print(bruce)
    print(bruce)


