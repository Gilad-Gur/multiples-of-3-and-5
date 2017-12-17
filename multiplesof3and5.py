# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# This program finds the sum of all the multiples of 3 or 5 below a given positive integer.
def user_input():
    while True:
        try:
            n = input('Please type in a natural number: ')
            if (n=='q'):
                break
            else:
                n=int(n)
            break
        except ValueError:
            print('Invalid input')
            continue
        if n <0:
            print('Invalid input')
            continue

    return n



def sumDivisibleBy(div,n):
    p = (n-1) // div
    sum = (div*p*(p+1))//2
    return sum



def main():
    while True:
        n=user_input()
        if (n=='q'):
            break
        print(sumDivisibleBy(5,n)+sumDivisibleBy(3,n)-sumDivisibleBy(15,n))
        print('do it again!!!')



main()
