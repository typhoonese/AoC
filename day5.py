from read_file import read_file_lines
file_lines = read_file_lines("./data/day5.txt")


# clean container stacks from empty elements due to transposition
def clean_empty_containers(_containers):
    for container_column in _containers:
        while container_column.count(" ") > 0:
            container_column.remove(" ")


# stack containers on top of a container block
def stack_containers(_to, _moving_containers):
    transposed_containers[_to].extend(_moving_containers)


# find the containers that need to move
def find_moving_containers(_transposed_containers, _number_of_moving_containers, _from):
    first_moving_container_reverse_index = _number_of_moving_containers * -1
    moving_containers = _transposed_containers[_from][first_moving_container_reverse_index:]
    _transposed_containers[_from] = _transposed_containers[_from][:
                                                                  first_moving_container_reverse_index]
    return moving_containers


containers = []
moves = []
number_of_containers = 9
# containers at 1st, 5th, 9th ... index -> nth container is at (n1 + 4)
for line in file_lines:
    # read containers
    if len(line) == number_of_containers*4:
        container_level = ["", line[1], line[5], line[9], line[13],
                           line[17], line[21], line[25], line[29], line[33]]
        containers.insert(0, container_level)
    # read moves
    else:
        line = line.strip().split(" ")
        move = [line[1], line[3], line[5]]
        moves.append(move)

# remove container numbers
containers.pop(0)

# transpose containers
N = len(containers[0])
M = len(containers)
transposed_containers = [[0 for x in range(M)] for y in range(N)]
for outer_index in range(N):
    for inner_index in range(M):
        transposed_containers[outer_index][inner_index] = containers[inner_index][outer_index]
clean_empty_containers(transposed_containers)

for move in moves:
    number_of_moving_containers = int(move[0])
    from_container = int(move[1])
    to_container = int(move[2])

    # puzzle 1 logic
    MOVING_CONTAINERS_AT_ONCE = 1
    for i in range(number_of_moving_containers):
        moving_containers = find_moving_containers(transposed_containers, MOVING_CONTAINERS_AT_ONCE,
                                                   from_container)
        stack_containers(to_container, moving_containers)

    # puzzle 2 logic
    # moving_containers = find_moving_containers(transposed_containers,
    #                                            number_of_moving_containers, from_container)
    # stack_containers(to_container, moving_containers)

print("Top containers of each container column:\n")
for final_containers in transposed_containers:
    print(final_containers[-1])
