def split_into_groups(data, group_size):
    return [data[i:i + group_size] for i in range(0, len(data), group_size)]