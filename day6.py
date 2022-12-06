from read_file import read_file_lines
file_lines = read_file_lines("./data/day6.txt")


# change for puzzle 1 and puzzle 2.
# marker length for puzzle 1 = 4 and puzzle 2 = 14
marker_length = 14
# len(file_lines) = 1
for line in file_lines:
    index = 0
    # puzzle 1 & puzzle 2
    while index < len(line)-marker_length:
        signal = set()
        marker = line[index:index+marker_length]
        for char in marker:
            signal.add(char)
        if len(signal) == marker_length:
            print("signal: ", signal, "index: ",
                  index + marker_length)
            break
        index += 1
