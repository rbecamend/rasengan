def read_strings_from_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]
