# go through a file
# (default texts/mbox-short.txt if none provided)
# and find every email "Author:" line
# take those with a "*.edu" email domain
# return the domain with the highest number of
# distinct email addresses

def most_popular_edu_email():
    filename = input("enter file: ")
    if len(filename) < 1: filename = "texts/mbox-short.txt"
    filehandler = open(filename)
    domainsedu = dict()
    for line in filehandler:
        if line.startswith("Author:"):
            words = line.split()
            email = words[1]
            if email.endswith(".edu"):
                domainsedu[email] = None # just tracking unique keys
            else:
                continue
    print(domainsedu)
    pop_domainsedu = dict()
    for i in domainsedu:
        hostdomain = i.split("@")
        domain = hostdomain[1]
        pop_domainsedu[domain] = pop_domainsedu.get(domain,0)+1
    largestV = None
    largestK = None
    for k,v in pop_domainsedu.items():
        if largestV is None or v > largestV:
            largestV = v
            largestK = k
    print("The most popular domain.edu is",largestK)


# go through a file
# (default texts/mbox-short.txt if none provided)
# and find every email "Author:" line
# take those with a "umich.edu" email domain
# return the email address using this domain
# that has authored the most emails,
# and the number of emails it authored

def chattiest_umich_email():
    file = input('enter file: ')
    if len(file) < 1: file = 'texts/mbox-short.txt'
    file_handler = open(file)
    umich = dict()
    for line in file_handler:
        line = line.strip()
        if line.startswith('Author:') and line.endswith('umich.edu'):
            words = line.split()
            domain = words[1]
            umich[domain] = umich.get(domain,0) + 1
    big_key = None
    big_value = None
    for key,value in umich.items():
        if big_value is None or value > big_value:
            big_value = value
            big_key = key
    print("email:",big_key, "frequency:",big_value)

# most_popular_edu_email()
# chattiest_umich_email()
