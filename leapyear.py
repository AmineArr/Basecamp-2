years = input()
if int(years) / 400:
    print('Leap Year')
elif int(years) / 100:
    print("not a leap year")
elif int(years) / 4:
    print("Leap year")
else:
    print("Not a Leap Year")
