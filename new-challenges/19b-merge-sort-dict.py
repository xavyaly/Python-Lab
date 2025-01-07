#!/usr/bin/python3

# Two dictionaries
dict1 = {'b': 3, 'a': 1, 'c': 2}
dict2 = {'f': 6, 'e': 5, 'd': 4}

# Merge dictionaries
merged_dict = {**dict1, **dict2}

# Sort merged dictionary by keys
sorted_merged_dict = dict(sorted(merged_dict.items()))

print("Merged and sorted by keys:", sorted_merged_dict)


