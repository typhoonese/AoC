from read_file import read_file_lines
file_lines = read_file_lines("./data/day4.txt")

pair_with_larger_coverage = ""
# for counting pairs in puzzle 1
inclusive_count = 0
# for counting pairs in puzzle 2
partial_count = 0


for line in file_lines:
    (first_pair, second_pair) = line.split(',')
    first_pair_split = first_pair.split('-')
    (first_pair_start, first_pair_end) = (
        int(first_pair_split[0]), int(first_pair_split[1]))
    second_pair_split = second_pair.split('-')
    (second_pair_start, second_pair_end) = (
        int(second_pair_split[0]), int(second_pair_split[1]))

    # puzzle 1 logic
    if (second_pair_start >= first_pair_start) and (second_pair_end <= first_pair_end):
        inclusive_count += 1
    elif (first_pair_start >= second_pair_start) and (first_pair_end <= second_pair_end):
        inclusive_count += 1
    # puzzle 2 logic
    elif (second_pair_start <= first_pair_start <= second_pair_end) or (second_pair_start <= first_pair_end <= second_pair_end):
        partial_count += 1
    elif (first_pair_start <= second_pair_start <= first_pair_end) or (first_pair_start <= second_pair_end <= first_pair_end):
        partial_count += 1


print("[Puzzle 1: Number of pairs]: ", inclusive_count)
print("[Puzzle 2: Number of pairs]: ", inclusive_count + partial_count)
