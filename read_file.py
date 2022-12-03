def read_file_lines(file_path):
    file_path = file_path
    file = open(file_path, 'r')
    file_lines = file.readlines()
    return file_lines
