sour_points = 0
salty_points = 0
sweet_points = 0

answer1 = input("Which breakfest food do you perfer A plain greek yogurt, B bacon, or C sugar cereals ")
if answer1 == "A" or answer1 == "a":
    sour_points += 1
elif answer1 == "B":
    salty_points += 1
elif answer1 == "C":
    sweet_points += 1

answer2 = input("Would you rather eat A a bucket of lemon juice, B a bucket of salt, or C a bucket of sugar ")
if answer2 == "A":
    sour_points += 1
elif answer2 == "B":
    salty_points += 1
elif answer2 == "C":
    sweet_points += 1

answer3 = input("What is your favorite soup A clam chowder, B tortilla soup, or C sweet potato soup  ")
if answer3 == "A":
    sour_points += 1
elif answer3 == "B":
    salty_points += 1
elif answer3 == "C":
    sweet_points +=1

answer4 = input("what is your favorite snack A salt and vinegar chips, B pickles, or C candy ")
if answer4 == "A":
    sour_points += 1
elif answer4 == "B":
    salty_points += 1
elif answer4 == "C":
    sweet_points += 1

answer5 = input("What is your favorite condiment A mustard, B soy sauce, or C ketchup ")
if answer5 == "A":
    sour_points += 1
elif answer5 == "B":
    salty_points += 1
elif answer5 == "C":
    sweet_points += 1

# End: three lines different types of points
if sour_points > salty_points and sour_points > sweet_points:
    print("Wow you must really like sour things!")
elif salty_points > sour_points and salty_points > sweet_points:
    print("Wow you must really like salty stuff!")
elif sweet_points > salty_points and sweet_points > sour_points:
    print("Wow you must really like sweet things!")