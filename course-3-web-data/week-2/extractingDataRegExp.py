import re
file_handler = open("../../texts/regex_sum_1014888.txt")
nums = list()

def double_loop():
    for line in file_handler:
        num_strs = re.findall("[0-9]+", line)
        if len(num_strs) == 0:
            continue
        for i in num_strs:
            nums.append(int(i))
    return sum(nums)

def single_loop():
    num_strs = re.findall("[0-9]+", file_handler.read())
    for i in num_strs:
        nums.append(int(i))
    return sum(nums)

# print(double_loop())

print(sum([int(i) for i in re.findall('[0-9]+',open("../../texts/regex_sum_1014888.txt").read())]))
