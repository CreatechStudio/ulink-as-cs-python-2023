age = int(input("Your age now: "))
year = 90 - age
month = year * 12
day = round(year * 365.25)
week = round(day / 7)
print(f"You have {day} days, {week} weeks, and {month} months left.")
