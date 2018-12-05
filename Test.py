import time
import json
import StoreItems
from StoreItems import *

x = .5

with open("Bank.json", 'r') as f:
    bank = json.load(f)
with open("Commands.json", 'r') as f:
    commands = json.load(f)

for program, price in Store_Items.items():
    print(f"{program} | ${price}")

current_commands = commands["Test"]["InstalledCommands"]

for command in current_commands.items():
    print(*command)


