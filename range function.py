num=int(input("enter a num:"))
sum=0
for i in range(2,num):
    if num%i==0:
        sum=sum+1
    else:
        sum=sum
if sum==0:
    print("the given is prime number")
else:
    print("not prime")