data = str(input("Enter a string: "))
str_len = len(data.lower())
file_name = open("data.txt", "w")
file_data = file_name.write(str(str_len))