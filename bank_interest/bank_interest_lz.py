money = float(input("Enter money:"))
year = int(input("Enter year:"))
rate = float(input("Enter rate:"))

print(f"Interest={money*((1+rate)**year)-money}")
