'''
Corrie Stewart
Program sums all digits entered by a user
Date: 11/4/18
'''

def main():
    int = eval(input("Enter an integer: "))
    print("The sum of the digits you entered is: ", sumDigits(int))

def sumDigits(n):
    if n % 10 == 0:
        print("final n: ", n)
        return n
    else:
        print("n at this iteration: ", n)
        return sumDigits(n // 10) + (n % 10)

main()
