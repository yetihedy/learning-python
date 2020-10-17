file_name = input("Enter file name: ")
file_handler = open(file_name)
count=0
total_value=0
for line in file_handler:
    if line.startswith("X-DSPAM-Confidence"):
        count=count+1
        pos=line.find(":")
        num=line[pos+1:]
        value=float(num)
        total_value=total_value+value
print("Average spam confidence:",total_value/count)
