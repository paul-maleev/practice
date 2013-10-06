import sys

print("Enter a year: ")

str = input()
if not str.isdigit():
    print("Please enter a numeric value")
    sys.exit(0)
year = int(str)

if year%4==0:
    if year%100:
        if year%400:
            print(year.__str__()+" is a leap year")
        else:
            print(year.__str__()+" isn\'t a leap year")
    else:
        print(year.__str__()+" is a leap year")
else:
    print(year.__str__()+" isn\'t a leap year")
