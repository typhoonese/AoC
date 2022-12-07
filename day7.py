from read_file import read_file_lines
file_lines = read_file_lines("./data/day7.txt")

directories = [[]]
is_moving_back = False
next_dir = ""
directory_sizes = {}
directory_size = 0
for line in file_lines:
    split_command = line.strip().split(" ")
    # build dir tree
    if split_command[1] == "cd":
        directory_size = 0
        next_dir = split_command[2]
        if (next_dir != ".."):
            is_moving_back = False
            directories[-1].append(next_dir)
        elif (next_dir == ".."):
            if not is_moving_back:
                one_back_dir = directories[-1][:-1]
                directories.append(one_back_dir)
                is_moving_back = True
            elif is_moving_back:
                directories[-1].pop()
            continue
    # read file sizes per directory
    else:
        if split_command[0].isdigit():
            current_dir = directories[-1][-1]
            directory_size += int(split_command[0])
            directory_sizes.update({current_dir: directory_size})

# calculate total sizes
total_dir_sizes = {}
for dir_path in directories:
    dir_path = dir_path[::-1]
    for index in range(0, len(dir_path)):
        sub_dir = dir_path[index]
        # the most nested dir path
        if index == 0:
            # if it has any files
            if sub_dir in directory_sizes:
                total_dir_sizes[sub_dir] = directory_sizes[sub_dir]
            # if the directory is empty
            else:
                total_dir_sizes[sub_dir] = 0
        else:
            pre_sub_dir = dir_path[index-1]
            # if the size of other sub dirs of the directory already counted
            if sub_dir in total_dir_sizes:
                total_dir_sizes[sub_dir] += total_dir_sizes[pre_sub_dir]
            # dir and its counted for the first time
            elif sub_dir not in total_dir_sizes:
                sub_dir_size = 0
                # check if dir has any files
                if sub_dir in directory_sizes:
                    sub_dir_size = directory_sizes[sub_dir]
                total_dir_sizes[sub_dir] = sub_dir_size + \
                    total_dir_sizes[pre_sub_dir]

total_dir_size = 0
for dir_path in total_dir_sizes:
    if total_dir_sizes[dir_path] <= 100_000:
        total_dir_size += total_dir_sizes[dir_path]

print("Total dir size: ", total_dir_size)
