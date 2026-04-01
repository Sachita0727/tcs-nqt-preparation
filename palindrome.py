n = int(input("Enter the number: "))
rev = 0
dummy = n

while n > 0:
    temp = n % 10
    rev = rev * 10 + temp
    n = n // 10

if dummy == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
