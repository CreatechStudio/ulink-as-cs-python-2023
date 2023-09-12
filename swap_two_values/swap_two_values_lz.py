a = int(input("Num A="))
b = int(input("Num B="))

a ^= b
b ^= a
a ^= b

print(f"Num A= {a}  Num B= {b}")
