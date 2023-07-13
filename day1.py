#Part 1 (find the largest sum i.e. calories in the data seperated by new lines)
fhand = open("adventofcode.com_2022_day_1_input.txt")
text = fhand.read()

largest = []
split_on_dbln = text.split("\n\n")
for calories in split_on_dbln:

    largest.append(sum(list(map(int, calories.splitlines()))))
highest_calorie = max(largest)
print(highest_calorie)

#Part 2
# copy_lst = largest.copy()
# three_highest_calories = 0
# for i in range(3):
#     high_cal = max(copy_lst)
#     three_highest_calories += high_cal
#     copy_lst.remove(high_cal)
#     continue
# print(three_highest_calories)
               #OR MORE PYTHONIC
print(sum(sorted(largest, reverse=True)[0:3]))
