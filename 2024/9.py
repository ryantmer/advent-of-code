input = "2333133121414131402"
with open("9-input.txt", "r") as f:
    input = f.readline().strip()

fragmented_file_system = list()
file_id = 0
is_file = True
for bit_count in input:
    if is_file:
        fragmented_file_system.extend([file_id] * int(bit_count))
        file_id += 1
    else:
        fragmented_file_system.extend([None] * int(bit_count))
    is_file = not is_file

print("File system before defragmentation:")
print(fragmented_file_system)

# Part 1
defragmented = list(fragmented_file_system)
swap_pointer = len(defragmented) - 1
for index in range(len((defragmented))):
    if swap_pointer <= index:
        break
    if defragmented[index] is not None:
        continue
    while defragmented[swap_pointer] is None:
        swap_pointer -= 1
    defragmented[index], defragmented[swap_pointer] = defragmented[swap_pointer], defragmented[index]
    swap_pointer -= 1
    # print(defragmented_file_system)

print("File system after defragmentation:")
print(defragmented)
checksum = sum([index * val if val is not None else 0 for index, val in enumerate(defragmented)])
print("Part 1: Checksum is %d" % checksum)

# Part 2
semidefragmented = list(fragmented_file_system)
for file_id in range(int(len(input) / 2), 0, -1):
    if file_id % 10 == 0:
        print("Trying to move file ID %d of %d" % (file_id, int(len(input) / 2)))

    file_start = semidefragmented.index(file_id)
    file_length = sum(x == file_id for x in fragmented_file_system[file_start:file_start + 10]) # Files are max length of 9
    # print("File %d of length %d, starting at %d" % (file_id, file_length, file_start))
    try:
        space_index = "".join(["." if x is None else "X" for x in semidefragmented]).index("." * file_length)
        if space_index > file_start:
            continue
        # print("--> Space for file ID %d at index %d" % (file_id, space_index))
        semidefragmented[space_index:space_index + file_length], semidefragmented[file_start:file_start + file_length] = \
            semidefragmented[file_start:file_start + file_length], semidefragmented[space_index:space_index + file_length]
    except ValueError:
        # print("--> No space for file ID %d" % file_id)
        continue

print("File system after semidefragmentation:")
print(semidefragmented)
checksum = sum([index * val if val is not None else 0 for index, val in enumerate(semidefragmented)])
print("Part 2: Checksum is %d" % checksum)
