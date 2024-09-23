bool_two = not 3**4 < 4**3
print(bool_two)
# True

bool_three = not 10 % 3 <= 10 % 2
print(bool_three)

bool_four = not 3**2 + 4**2 != 5**2
print(bool_four)

bool_five = not not False
print(bool_five)

bool_one1 = False or not True and True
print(bool_one1)

bool_two2 = False and not True or True
print(bool_two2)

bool_three3 = True and not (False or False)
print(bool_three3)

bool_four4 = not not True or False and not True
print(bool_four4)

bool_five5 = False or not (True and True)
print(bool_five5)

bool_six6 = (2 <= 2) not "Alpha" == "Bravo"
print(bool_six6)