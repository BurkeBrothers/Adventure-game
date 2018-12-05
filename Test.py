import time
import json
import StoreItems
from StoreItems import *

x = .5

with open("User.json", 'r') as f:
    commands = json.load(f)
with open("User.json", 'r') as f:
    money = json.load(f)
current_commands = commands["User"]["Test"]["InstalledCommands"]

for program, price in Store_Items.items():
    print(f"{program:<10} | ${price}")
    #
    # if program in current_commands:
    #     print(f"{program} is in players inventory")
    # else:
    #     print(f"{program} is not in players inventory")


def store():
    while True:
        print("\nWhat do you want to buy?\n")
        time.sleep(x)
        choice = input(">> ")
store()
