name1 = input()
name2 = input()
score1 = 0
score2 = 0

list = ["TRUE", "LOVE"]

for i in name1:
    i = i.upper()
    if i in list[0]:
        score1 += 1
    if i in list[1]:
        score2 += 1

for i in name2:
    i = i.upper()
    if i in list[0]:
        score1 += 1
    if i in list[1]:
        score2 += 1

score = score1 * 10 + score2

print(f"Your score is {score}. ")

match score:
    case _ if score < 10 or score > 90:
        print("You are together like mentos and coke. ")
    case _ if 40 < score < 50:
        print("You are alright together. ")
