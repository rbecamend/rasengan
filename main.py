from utils.read_xlsx import read_strings_from_file
from utils.split_groups_xlsx import split_into_groups
from utils.write_xlsx import write_groups_to_file


def main():
    input_file = r'C:\Users\rebec\Downloads\rebeca.txt'
    output_file_prefix = 'output_strings'
    group_size = 100

    strings = read_strings_from_file(input_file)
    groups = split_into_groups(strings, group_size)
    write_groups_to_file(groups, output_file_prefix)

if __name__ == "__main__":
    main()