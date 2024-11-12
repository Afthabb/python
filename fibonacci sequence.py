#fibonacci sequence

num=int(input("Enter a number: "))
n1 , n2= 0,1
count =0

if num<=0:
    print ('enter postive number')
elif num==1:
    print(n1)
else:
    print("fibonacci sequence:")
    while count < num:
        print(n1)
        totaln=n1+n2
        n1=n2
        n2=totaln
        count+=1