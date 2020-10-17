score = input("Enter Score: ")
try:
    inpscr = float(score)
except:
    print('Input numeric value only, try again.')
    quit()
if inpscr<0.0 or inpscr>1.0:
    print('Value out of range, try again.')
    quit()
if inpscr >= 0.9:
    print("A")
elif inpscr >= 0.8:
    print("B")
elif inpscr >= 0.7:
    print('C')
elif inpscr >= 0.6:
    print('D')
else:
    print('F')
