coin_weights = {
    "0.05": 325,
    "0.1": 650,
    "0.2": 500,
    "0.5": 800,
    "1": 875,
    "2": 1200,
    "5": 70
}

 

print("-" * 20)
print("Coin Counting System")
print("-" * 20)

print("")

name = input("Please enter the volunteers name: ")
file_names = open('users.txt',  'r')
for i in range(6):
    if file_names.readlines(i+1) == name:
        print(f"Found and logged in as {name}")
    else:
        print(file_names.readlines(i+1))
        print(f"Could not find {name}, please note usernames are case sensitive.")
        options = int(input("Enter 1 to reboot system, or enter 2 to register user. "))




def add_infomation():
    pass



def totaloverview():
    pass


def add_user():
    pass