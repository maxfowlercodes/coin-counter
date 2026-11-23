import datetime
import time
count = 0

accepted_values = [500, 1000, 2000, 5000, 1, 2]

coin_values = {
    "2": ["£2", "£200", "1200"],
    "1": ["£1", "£100", "875"],
    "5000": ["50P", "£50", "800"],
    "2000": ["20P", "£20", "500"],
    "1000": ["10P", "£10", "650"],
    "500": ["5P", "£"
    ""
    ""
    "5", "325"]
}



users = {
    "name": '',
    "correct_totals": '', 
    "close_totals": '',
    "wrong_totals": '',
    "total_value": '',
    "most_recent": ''
}



file = open('system-file.txt')
count = count + 1
line = file.readline()
line = line.strip().split(',') 
length = len(line)

for i in range(36):
    if i == 0:
        users["name"] = line[i]
    elif i == 1:
        users['correct_totals'] = line[i]
    elif i == 2:
        users['close_totals'] = line[i]
    elif i == 3:
        users['wrong_totals'] = line[i]
    elif i == 4:
        users["total_value"] = line[i]
    elif i  == 5:
        users["most_recent"] = line[i]
    else:
        print("Else issues umm")

print("-" * 20)
print("Coin Counting System")
print("-" * 20)

print(users)

name = input("Enter name of user: ")
coin_type = input("What money value was collected today? (5p, 10p, 20p, 50p, £1, £2)")
try:
    coin_type = coin_type.replace('p', '')
    coin_type = int(coin_type)
    coin_type = coin_type * 100
except:
    coin_type = coin_type.replace('£', '')
    coin_type = int(coin_type)
    
if coin_type not in accepted_values:
    print("COIN TYPE NOT FOUND")

bag_weight = input(f"How much does the bag weigh? Expected value: {coin_values[coin_type]}")