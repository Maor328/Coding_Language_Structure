def add_3_dicts(d1, d2, d3):
    # Combine all keys from the three dictionaries without duplicates using a set
    all_keys = set(d1.keys()) | set(d2.keys()) | set(d3.keys())
    new_dict = {}
    
    for k in all_keys:
        vals = []
        for d in (d1, d2, d3):
            # Append the value if the key exists and the value is not already in the list
            if k in d and d[k] not in vals:
                vals.append(d[k])
        # Store the unique values as a tuple
        new_dict[k] = tuple(vals)
        
    return new_dict