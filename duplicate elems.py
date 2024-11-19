list=[]
limit=int(input('enter number of elements to be put in list:'))
for i in range(limit):
    num=int(input("enter element:"))
    list.append(num)

unique_list=[]
for i in list:
    if i not in unique_list:
        unique_list.append(i)
print("orginal list is:",list)
print("thew new list is:", unique_list)