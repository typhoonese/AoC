from read_file import read_file_lines
file_lines = read_file_lines("./data/day8.txt")

forest = []

for line in file_lines:
    temp_line_elements = []
    line = line.strip()
    for height in line:
        temp_line_elements.append(height)
    forest.append(temp_line_elements)

forest_column_size = len(forest[0])
forest_row_size = len(forest)

# scan the forest
number_of_hidden_trees = 0
scenic_score = 0
for row in range(1, forest_row_size-1):
    for column in range(1, forest_column_size-1):
        current_tree = forest[row][column]
        current_row = forest[row].copy()
        current_column = [sub[column] for sub in forest]

        # what's on left, right, up, down of the current tree
        left = current_row[0:column]
        right = current_row[column+1:]
        up = current_column[0: row]
        down = current_column[row+1:]

        # max of what's on left, right, up, down of the current tree
        left_row_max = max(left)
        right_row_max = max(right)
        up_column_max = max(up)
        down_column_max = max(down)

        # count invisible trees
        if (left_row_max >= current_tree and right_row_max >= current_tree and up_column_max >= current_tree and down_column_max >= current_tree):
            number_of_hidden_trees += 1
        # calculate scenic score for visible trees
        else:
            left_reversed = left.copy()
            left_reversed = left[::-1]
            up_reversed = up.copy()
            up_reversed = up[::-1]

            # left scenic score
            left_scenic_score = 0
            for tree in left_reversed:
                left_scenic_score += 1
                if current_tree > tree:
                    continue
                elif current_tree <= tree:
                    break

            # right scenic score
            right_scenic_score = 0
            for tree in right:
                right_scenic_score += 1
                if current_tree > tree:
                    continue
                elif current_tree <= tree:
                    break

            # up scenic score
            up_scenic_score = 0
            for tree in up_reversed:
                up_scenic_score += 1
                if current_tree > tree:
                    continue
                elif current_tree <= tree:
                    break

            # down scenic score
            down_scenic_score = 0
            for tree in down:
                down_scenic_score += 1
                if current_tree > tree:
                    continue
                elif current_tree <= tree:
                    break

            temp_scenic_score = left_scenic_score * \
                right_scenic_score * up_scenic_score * down_scenic_score

            scenic_score = max(scenic_score, temp_scenic_score)


print("[Puzzle 1]: Total visible trees:", forest_column_size *
      forest_row_size - number_of_hidden_trees)

print("[Puzzle 2]: Max scenic score: ", scenic_score)
