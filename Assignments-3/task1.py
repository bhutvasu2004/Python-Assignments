def fun(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fun(n-1)

n = int(input("Enter Number : "))
print(f"Factorial of {n} is : ",fun(n))