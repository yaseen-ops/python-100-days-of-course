#
# try:
#     file = open("file.txt")   # trying to open a file which is not exists, throws error
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sdfsdfsd"])  # Try to get the value for a key which is not exists, throws error
# except:
#     file = open("file.txt", "w")    # If try throws error, this code will be ran
#     file.write("something")
#

try:
    file = open("file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["sfsdsdfsd"])
    # print(a_dictionary["key"])
except FileNotFoundError:  # Particular save the exception of file not found and run below for that error only
    file = open("file.txt", "w")  # If try throws error, this code will be ran
    file.write("something")
# except KeyError:
except KeyError as error_message:   # Save the error as error message
    # print("The key doesn't exists")
    print(f"The key {error_message} doesn't exists")
else:    # when the try is success this one runs
    content = file.read()
    print(content)
finally:   # No matter whatever this one surely runs
    file.close()
    print("File is closed")

