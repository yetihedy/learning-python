# write a function that asks for a file and
# for each line in that file finds each line that contains
# an IP address wrapped in a square bracket ([000.000.000.000])
# (for all IPs, the number of digits between each dot
# is between 1 and 3 [0, 00, or 000]),
# extracts each ip address and splits it up into
# a tuple of 4 numbers
# EG: "123.4.0.89" -> (123, 4, 0, 89)
# and returns a sorted list of all such tuples.
# NOTE: a sorted tuple compared from left to right
# EG: [(0,0,0,0), (0,0,0,2), (0,0,1,0)] (ascending order)
# BONUS: return only unique tuples, sorted.
file_name = input("File name: ")
if len(file_name) < 1: file_name = "../../texts/mbox-short.txt"
file_handler = open(file_name)
ip_tuples = list()
for line in file_handler:
    if "[" and "]" in line:
        brkt_start_i = line.find("[")
        brkt_end_i = line.find("]")
        brkt_contents = line[brkt_start_i+1:brkt_end_i].split(".")
        if len(brkt_contents) == 4:
            valid = True
            for i in brkt_contents:
                if not (len(i) > 0 and len(i) < 4):
                    valid = False
            if valid == False:
                continue
            brkt_contents = [int(i) for i in brkt_contents]
            brkt_contents = tuple(brkt_contents)
            ip_tuples.append(brkt_contents)
ip_sorted = sorted(ip_tuples)
ip_unique = list()
for ip in ip_sorted:
    if ip not in ip_unique:
        ip_unique.append(ip)
print(ip_unique)
