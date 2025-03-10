sides = input()
side_one= sides.split(",")[0]
side_two= sides.split(",")[1]
side_three= sides.split(",")[2]
print(side_one, side_three, side_two)

first_side= side_one.split("=")[1]
second_side= side_two.split("=")[1]
third_side= side_three.split("=")[1]
print(first_side, second_side, third_side)