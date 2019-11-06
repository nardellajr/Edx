
x = int(input("enter an integer: "))

if x % 2 == 0:
    print('')
    print('even')
else:
    print('')
    print('Odd')

print('Done with conditional')




n = input("You are in the woods. Enter left or right to get out: ")

while n == 'left':
    print('Your still in the woods')
    n = input("You are still the woods. Enter left or right to get out: ")

print("You entered right, Yay! you're out of the woods")


num = 5

if num > 2:
    print(num)
    num -= 1
print(num)


for i in range(10, 2, -2):
    print(i)

divisor = 2
for num in range(0, 10, 2):
    print(num/divisor)