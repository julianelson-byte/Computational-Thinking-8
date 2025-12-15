sour_points = 0
salty_points = 0
sweet_points = 0

answer1 = input("Which breakfest food do you perfer A plain greek yogurt, B bacon, or C sugar cereals ")
if answer1 == "A":
    sour_points += 1
elif answer1 == "B":
    salty_points += 1
elif answer1 == "C":
    sweet_points += 1

answer2 = input("Would you rather eat A a bucket of lemon juice B a bucket of salt, or C a bucket of sugar")
if answer2 == "A":
    sour_points += 1
elif answer2 == "B":
    salty_points += 1
elif answer2 == "C":
    sweet_points += 1

answer3 = input("What is your favorite soup A clam chowder B ")