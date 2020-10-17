file_name = input("Enter file name: ")
if len(file_name) < 1: file_name = "../../mbox-short.txt"
file_handler = open(file_name)
emails = dict()
for line in file_handler:
    if line.startswith("From "):
        pieces = line.split()
        email = pieces[1]
        emails[email] = emails.get(email,0) + 1
max_v = None
max_k = None
for k,v in emails.items():
    if max_v is None or v > max_v:
        max_k = k
        max_v = v
print(max_k, max_v)
