import datetime
import time
count = 0

accepted_values = [100, 200, 500, 1000, 2000, 5000, 1, 2]

coin_values = {
    "2": ["£2", "£20", "120", 12.00],
    "1": ["£1", "£20", "175", 8.75],
    "5000": ["50P", "£10", "160", 8],
    "2000": ["20P", "£10", "250", 5],
    "1000": ["10P", "£5", "325", 6.5],
    "500": ["5P", "£5", "325", 3.25],
    "200": ["2P", "£1", "356", 7.12],
    "100": ["1P", "£1", "456", 3.56]
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

for i in range(6):
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


def coin_validation():
    coin_type = input("What money value was collected today? (5p, 10p, 20p, 50p, £1, £2): ")
    try:        
        coin_type = coin_type.replace('p', '')
        coin_type = int(coin_type)
        coin_type = coin_type * 100
        if coin_type not in accepted_values:
            print("COIN TYPE NOT FOUND")
            coin_validation()

    except:
        coin_type = coin_type.replace('£', '')
        coin_type = int(coin_type)

    if coin_type not in accepted_values:
                print("COIN TYPE NOT FOUND")
                coin_validation()

    return coin_type

print("-" * 20)
print("Coin Counting System")
print("-" * 20)

name = input("Enter name of user: ")
coin_type = coin_validation()
coin_weight = coin_values[str(coin_type)][2]
bag_weight = input(f"How much does the bag weigh? Expected weight is {coin_weight} grams: ")

bag_weight = int(bag_weight)
coin_weight = int(coin_weight)
coin_type = str(coin_type)

if bag_weight > coin_weight:
    print(f"Bag is {bag_weight - coin_weight} grams heavier than expected. ")
    print(f"Please remove {round((bag_weight - coin_weight) / (coin_values[coin_type][3]))} coins from the bag.")
elif bag_weight < coin_weight:
    print(f"Bag is {coin_weight - bag_weight} grams lighter than expected. ")
    print(f"Please add {abs(round((bag_weight - coin_weight) / (coin_values[coin_type][3])))} coins to the bag.")

else:
    print("Bag is correct weight.")
