for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!')

for letter in 'hola':
    print(letter)

print('Guess and Check algorithm')
# cube = 8
cube = -28
for guess in range(abs(cube) + 1):
    if guess ** 3 >= abs(cube):
        break

if guess ** 3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess

    print('Cube root of ' + str(cube) + ' is ' + str(guess))

# Week 2 - Problems

print("Problem 1")
# Paste your code into this box
s = 'azcbobobegghakl'
count = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for i in s:
    if i in vowels:
        count += 1
print('Number of vowels: ', count)

print('Problem 2')
count = 0
count_bob = 0
s = 'azcbobobegghakl'
for i in s:
    count += 1
    if i == 'b':
        # check the next 2 letters
        if s[count: count + 2] == 'ob':
            count_bob += 1

print('Number of times bob occurs is: ', count_bob)

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# n the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc
print('Problem 3')
last_letter = None
current_substring = ''
longest_substring = ''

# s = 'azcbobobegghakl'
s = 'abcbcd'

for i in s:
    print('value of letter: ', i, ' is ', ord(i))

    if last_letter is None or ord(i) >= ord(last_letter):
        current_substring += i
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
    else:
        current_substring = i

    last_letter = i

print(longest_substring)


print('\n', 'approximate solution algorithm')
cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1

print('num_guesses = ', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of ', cube)
else:
    print(guess, 'is close to the cube root of', cube)



x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2 - x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))



print('Bisection Search algorithm or Binary Search')
# if not close enough, is guess too big or too small?
x = 25
epsilon = 0.01
num_guesses = 0
low = 1.0
high = x
ans = (high + low) / 2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print('num_guesses = ' + str(num_guesses))
print(str(ans) + ' is close to square root of ' + str(x))
