def time_stamp_counter():
    file_name = input("Enter file name: ")
    if len(file_name) < 1: file_name = "../../texts/mbox-short.txt"
    file_handler = open(file_name)
    hours_count = dict()
    for line in file_handler:
        if line.startswith("From "):
            pos = line.find(":")
            hour = line[pos-2:pos]
            hours_count[hour] = hours_count.get(hour, 0) + 1
    hours_sort = list(hours_count.items())
    hours_sort.sort()
    # hours_sorted = sorted([(k,v for k,v in hours_count.items()])
    for k,v in hours_sort:
        print(k,v)
time_stamp_counter()
