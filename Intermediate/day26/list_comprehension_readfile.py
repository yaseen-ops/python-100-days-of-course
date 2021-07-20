# with open("file1.txt") as file1:
#     file1_list = []
#     for line in file1.readlines():
#         file1_list.append(line.strip())
#
# with open("file2.txt") as file2:
#     file2_list = []
#     for line in file2.readlines():
#         file2_list.append(line.strip())
#
# # Checking common numbers in both the files
# common_numbers = [int(number) for number in file1_list if number in file2_list]
# print(common_numbers)

# OR

with open("file1.txt") as file1:
    file1_list = file1.readlines()

with open("file2.txt") as file2:
    file2_list = file2.readlines()

# Checking common numbers in both the files
common_numbers = [int(number) for number in file1_list if number in file2_list]
print(common_numbers)