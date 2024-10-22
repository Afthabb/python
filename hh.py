temp = float(input("Enter temperature:"))
ch=input("is your choice in Celsius or Fahrenheit C/F?")
if ch=="c" or ch=='C':
    fahrenheit = (temp * 5/9) + 32
    print(temp," degree Celsius is equal to ",fahrenheit," degree Fahrenheit.")
else:
    cels = 5/9*(temp-32)
    print(temp," degree fahrenheit is equal to ",cels," degree Celsius.")
