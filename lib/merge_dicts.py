def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Start with a copy of dict1
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  # Sum the values if the key is common
        else:
            merged_dict[key] = value  # Add new key-value pairs
    return merged_dict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

# Merge dictionaries
merged_dict = merge_dicts(dict1, dict2)

# Print the result
print("Merged Dictionary:", merged_dict)
