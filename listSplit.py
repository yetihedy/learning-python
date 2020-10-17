file_name = input("Enter file name: ")
file_handler = open(file_name)
words_list = list()
for line in file_handler:
    line.rstrip()
    pieces = line.split()
    for word in pieces:
        if word in words_list:
            continue
        words_list.append(word)
words_list.sort()
print(words_list)
