# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# This program finds the sum of all the multiples of 3 or 5 below a given positive integer.
while True:
    try:
        n = int(input('Please type in a natural number: '))
    except ValueError:
        print('Invalid input')
        continue
    if n <= 0:
        print('Invalid input')
        continue
    break

sum = 0
print("List of all the natural numbers below " +str(n)+ " that are mult. of 3 & 5:")

for i in range(n):
    if i%3==0 or i%5==0:
        print(i)
        sum += i
print("The sum of these multiples is " +str(sum))
