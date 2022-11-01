#employee_list = open("files\example_text_file.txt", "a") - appending
#employee_list = open("files\example_text_file.txt", "w") - writing
employee_list = open("files\example_text_file_1.txt", "x") # creating a new file

employee_list.write("\nOscar - accountant")

employee_list.close()