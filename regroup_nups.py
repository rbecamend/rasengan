from peewee import *

db = PostgresqlDatabase ('.db')

class Nup (Model):
    id = PrimaryKeyField()
    class Meta: database = db

def read_strings_from_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def write_groups_to_file(groups, output_file_prefix):
    for i, group in enumerate(groups):
        output_file = f"{output_file_prefix}_{i + 1}.txt"
        with open(output_file, 'w') as file:
            output_content = ', '.join(f'"{item}"' for item in group)
            file.write(f'[{output_content}]\n')

def split_into_groups(data, group_size):
    return [data[i:i + group_size] for i in range(0, len(data), group_size)]

def main():
    input_file = r'C:\Users\rebec\Downloads\rebeca.txt'
    output_file_prefix = 'output_strings'
    group_size = 100

    strings = read_strings_from_file(input_file)
    groups = split_into_groups(strings, group_size)
    write_groups_to_file(groups, output_file_prefix)

if __name__ == "__main__":
    main()