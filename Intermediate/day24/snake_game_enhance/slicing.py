piano_keys = ["a", "b", "c", "d", "e", "f", "g", "h"]

print(piano_keys[2:5])  # slices from c to e, which is from piano_keys[2] to piano_keys[5-1]
print(piano_keys[:5])   # slices from a to e, which is from piano_keys[0] to piano_keys[5-1]
print(piano_keys[2:])   # slices from c to h, which is from piano_keys[2] to piano_keys[n]
print(piano_keys[2:7:2])  # slices from c to g, which is from piano_keys[2] to piano_keys[7-1] with interval of 2
print(piano_keys[::2])  # slices from a to h with the interval of 2
print(piano_keys[::-1])  # Reverse the list, kind of from a to h but takes from h to a (as it is -1)

# Slicing works for TUPLES as well the same way
