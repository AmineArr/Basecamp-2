date = input()
month = date.split(",")[0]
day = date.split(",")[1]

exact_month = int(month.split(":")[1].strip(" "))
exact_day = int(day.split(":")[1].strip(" "))

print(exact_month, exact_day)

if exact_month == 12 and exact_day == 5:
    print("sinterklaas")
if exact_month == 12 and exact_day == 25:
    print("Kerstmis")
if exact_month == 12 and exact_day == 31:
    print("Oudjaars")
if exact_month == 1 and exact_day == 1:
    print("Nieuwjaars")
else:
    print("No holiday found on given input")