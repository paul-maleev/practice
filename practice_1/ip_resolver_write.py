addresses = {}
fp = open('ip-base.txt')
with fp as f:
    for line in f:
        addresses.update({line.split(" ")[0]:line.split(" ")[1]})

for key in addresses:
    print(key, addresses[key])

fp.close()
print("Enter a new ip and domain name pair!\n ")
ip = input("Enter a new ip: ")
domain = input("Enter a domain name: ")
pair = ip+' '+domain+'\n'
fp = open('ip-base.txt','a')
fp.write(pair)
fp.close()