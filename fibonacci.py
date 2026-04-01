n = int(input("Enter the value of N: "))

if n == 0:
    print("The Fibonacci Series up to", n, "th term:")
    print(0)
else:
    second_last = 0
    last = 1
    print("The Fibonacci Series up to", n, "th term:")
    print(second_last, last, end=" ")

    for i in range(2, n + 1):
        cur = last + second_last
        second_last = last
        last = cur
        print(cur, end=" ")
