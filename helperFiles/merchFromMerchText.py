# read data from a text file

my_file = open("merch.txt")
# file_str = my_file.read()
# print(file_str)

# file_line = my_file.readline()
# print(file_line)

# file_list = my_file.readlines()
# print(file_list)

itemsAvailable = my_file.readlines()
print(itemsAvailable)

my_file.close()