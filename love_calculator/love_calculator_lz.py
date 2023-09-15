name1 = input("Enter name 1: ")
name2 = input("Enter name 2: ")

score = 0

list_words = ["TRUE", "LOVE"]

for i in name1:
    i = i.upper()
    if i in list_words[0]:
        score += 10
    if i in list_words[1]:
        score += 1

for i in name2:
    i = i.upper()
    if i in list_words[0]:
        score += 10
    if i in list_words[1]:
        score += 1

print(f"Your score is {score}. ")

match score:
    case _ if score < 10 or score > 90:
        print("You are together like mentos and coke. ")
    case _ if 40 < score < 50:
        print("You are alright together. ")
