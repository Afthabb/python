# to prime the prime numbers before a given number

n=int(input("enter a number"))
print ("prime number less than",n,'are:')

for num in range (2,n):
    for i in range (2,num):
        if num%i==0:
            break
    else:
        print(num, end=' ')