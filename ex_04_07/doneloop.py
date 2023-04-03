n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')
print(n)
print('Ready or not, here I come!')
n = 0
while n < 3:
    print(n)
    n = n + 1
print('Ready!')
print(n)
print('\n\n\n')

print('Type in done and you shall be done!\n\n\n')

while True:
    line = input('> ')
    if line == 'done' :
        break
    print("You typed: \n", line)
print('Done!')