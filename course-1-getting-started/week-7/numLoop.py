largest = None
smallest = None
inp_num = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            inp_num = int(num)
        except:
            print("Invalid input")
            continue
    if largest is None:
        largest = inp_num
    elif inp_num > largest:
        largest = inp_num
    if smallest is None:
        smallest = inp_num
    elif inp_num < smallest:
        smallest = inp_num

print("Maximum is", largest)
print("Minimum is", smallest)
