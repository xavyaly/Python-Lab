# How do you sort a dictionary by its values? 
SI = {'a': 3, 'b': 1, 'c': 2} 
# SO = {'b': 1, 'c': 2, 'a': 3}

#!/usr/bin/python3

# Sort by values

# values_sort = dict(sorted(SI.items(), key=lambda item:item[1]))
# print(values_sort)

# Sort by keys

keys_sort = dict(sorted(SI.items()))
print(keys_sort)
