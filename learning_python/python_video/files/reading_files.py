# modes
# r - read
# r+ - read and write
# w - write
# a - append(only adding new information to the end of the file)

employee_list = open("files\example_text_file.txt", "r")

print(employee_list.readable())

print(employee_list.read())


# print(employee_list.readline())
# print(employee_list.readlines()[1])

for employee in employee_list.readlines():
    print(employee)
 
employee_list.close()
