import sys
addresses = {}
fp = open('ip-base.txt')
with fp as f:
    for line in f:
        addresses.update({line.split(" ")[0]:line.split(" ")[1]})

for key in addresses:
    print(key, addresses[key])

fp.close()

n = input("Enter 1 if you want to search an ip or 2 if you want to search a domain: ")

ip =""
domain=""
out=""

if n=='1':
    ip = input("Enter an ip:")
    out=addresses.get(ip,"domain not found")
    if out!="":
        print("Domain name is: " +out)
    else:
        sys.exit("Domain not found!")
elif n=='2':
    domain = input("Enter a domain: ")+"\n"
    found = False
    for key in addresses:
        if domain == addresses[key]:
            print("IP address is: "+key)
            found = True

else:
    sys.exit("Wrong input!")