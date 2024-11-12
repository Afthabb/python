limit=int(input('enter a limit:'))
number=int(input('enter a number:'))
smallest= number
smallestnxt=number
largestnxt=number
largest = number
for i in range(limit-1):
    number=int(input('enter a number:'))
    if number < smallest:
        smallest = number
        number < smallestnxt
        smallestnxt=number
    elif number > largest:
        largest = number
        number > largestnxt
        largestnxt=number

print ('smallest number is',smallest,'largest number is',largest)
print ('2nd smallest number is',smallestnxt,'2nd largest number is',largestnxt)

for number in numbers_list:
    if number > first:
        second = first
        first = number
    elif first > number > second:
        second =number