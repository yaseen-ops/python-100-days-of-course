# file = open("file.txt")
# print(file)
# content = file.read()
# print(content)
# # File closing is required to relax your computer resource once the job is done, it is mandatory though
# file.close()

# OR use the below methodology, where file closing not required
with open("file.txt") as file:
    content = file.read()
    print(content)

# # Write in a file, by default open file is set to be read only, we can add "w" to write or
# # "a" to append the data
# with open("file.txt", mode="a") as file:
#     file.write("\nThis line written through Python")


with open("new_file.txt", mode="w") as file:
    file.write("New file created through Python")