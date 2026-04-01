n = int(input("Enter the number: "))
prod = 1

while n > 0:
    prod *= n
    n -= 1

print("The factorial of the number is", prod)
