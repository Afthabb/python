#to check if  a program is prime number or not


num =int(input("enter a number"))
for i in range (2,num):
    if num%1==0:
        print("the number is not prime",num)
        break
else:
    print("the number is prime",num)