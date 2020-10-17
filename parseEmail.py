file_name = input("Enter file name: ")
file_handler = open(file_name)
count = 0
for line in file_handler:
    if line.startswith("From "):
        email = line.split()
        print(email[1])
        count = count+1
print("There were", count, "lines in the file with From as the first word")
