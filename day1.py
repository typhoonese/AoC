from read_file import read_file_lines
file_lines = read_file_lines("./data/day1.txt")

top_calories = []
calorie = 0
for line in file_lines:
    if (line != "\n"):
        calorie += int(line)
    elif (line == "\n"):
        top_calories.append(calorie)
        calorie = 0
# append eof if there is no \n
top_calories.append(calorie)
top_calories.sort()
top_calories.reverse()

print(["Puzzle 1: Max calorie count: "], top_calories[0])
print(["Puzzle 2: Max calorie count: "],
      top_calories[0] + top_calories[1] + top_calories[2])
