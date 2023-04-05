
# counter variable
zork = 0
print('Before', zork)
for thing in (9, 41, 12, 3, 74, 15):
    zork = zork + 1
    print(zork, thing)
print('After', zork)

# summing in a loop

zork = 0
print("Before", zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
    print(zork, thing)
print("After", zork)

# finding the Average in a Loop

count = 0
sum = 0
print("Before", count, sum)
for value in (9, 41, 12, 3, 74, 15) :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("After", count, sum, sum / count)

# filtering in a Loop
print('Before')
for value in (9, 41, 12, 3, 74, 15):
    if value > 20:
        print("Large number", value)
print("After")
