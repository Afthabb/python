'''
pythion program to check if a number is positive
or negative
'''

num=int(input("enter a number:"))
if num>0:
    print("number",num,"is positive")
elif num==0:
    print("given number is neither positive nor negative")
elif num<0:
    print("given number",num,"is negative")