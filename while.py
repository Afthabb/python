'''pyhton programm to print n
odd numbers
'''


limit=int(input("enter ur limit:"))
count=1
odd_num=1

while count<limit:
    print(odd_num,'\t',end='')
    count+=1
    odd_num+=2