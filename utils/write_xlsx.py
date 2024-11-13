def write_groups_to_file(groups, output_file_prefix):
    for i, group in enumerate(groups):
        output_file = f"{output_file_prefix}_{i + 1}.txt"
        with open(output_file, 'w') as file:
            output_content = ', '.join(f'"{item}"' for item in group)
            file.write(f'[{output_content}]\n')