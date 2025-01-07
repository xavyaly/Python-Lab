# Original Dictionary: {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2, 'f': 4}
# Unique Keys and Values Dictionary: {'a': 1, 'b': 2, 'd': 3, 'f': 4}

def ensure_unique_keys_and_values(input_dict):
    unique_dict = {}
    seen_values = set()

    for key, value in input_dict.items():
        if key not in unique_dict and value not in seen_values:
            unique_dict[key] = value
            seen_values.add(value)
    return unique_dict

# Test
input_dict = {
    "a": 1,
    "b": 2,
    "c": 1,  # Duplicate value
    "d": 3,
    "e": 2,  # Duplicate value
    "f": 4
}

unique_dict = ensure_unique_keys_and_values(input_dict)
print("Original Dictionalry: ", input_dict)
print("Uniuq Keys and Values Dictionary: ", unique_dict)