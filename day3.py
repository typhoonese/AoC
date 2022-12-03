from read_file import read_file_lines
file_lines = read_file_lines("./data/day3.txt")

# scoring: a-z gets 1 to 26, A-Z gets 27 to 52


def calculate_priority_score(set_of_items, score):
    for item in set_of_items:
        item_ascii = ord(item)
        if 65 <= item_ascii <= 90:
            score += item_ascii - 38
        elif 97 <= item_ascii <= 122:
            score += item_ascii - 96
    return score


# puzzle 1
total_score = 0
for line in file_lines:
    end_of_first_compartment = len(line)//2
    first_component = line[0:end_of_first_compartment]
    second_component = line[end_of_first_compartment:len(line)]
    mutual_items_set = set()
    for item in first_component:
        if second_component.find(item) >= 0:
            mutual_items_set.add(item)

    total_score = calculate_priority_score(mutual_items_set, total_score)

print("[Puzzle 1: Priority score: ", total_score)

# puzzle 2
number_of_elf_groups = len(file_lines)/3
total_score = 0
for group in range(0, int(number_of_elf_groups)):
    bag_of_elf_1 = file_lines[group*3].strip()
    bag_of_elf_2 = file_lines[group*3+1].strip()
    bag_of_elf_3 = file_lines[group*3+2].strip()

    all_badges_set = set()
    for possible_badge in bag_of_elf_1:
        if bag_of_elf_2.find(possible_badge) > -1 and bag_of_elf_3.find(possible_badge) > -1:
            all_badges_set.add(possible_badge)

    total_score = calculate_priority_score(all_badges_set, total_score)

print("[Puzzle 2: Priority badge score: ", total_score)
