#!/usr/bin/env python3
"""
Reservation

Create a terminal code that shows the user a list of available rooms 
to rent and the price of each room, this information will be available 
in a text file separated by commas.

`reservation_rooms.txt`
1,Master Suite,500
2,Family Room,200
3,Single Room,100
4,Simple Room,50

The code aks the user's name, the number of the room they want to rent
anf the quanty of days and shows the estimated total value to be paid.

The code should save this choice in another file that have all reservations.

`reservation_reserved.txt`
# client , room, days
Raquel,3,12

If another user tries to rent the same room, the code shou give them a 
message informing that the room is already reserved.
"""

__version__ = "0.1.1"
__author__ = "Raquel Marques"
__license__ = "Unlicense"

import sys
import logging

ROOMS_FILE = "reservation_rooms.txt"
RESERVATION_FILE = "reservation_reserved.txt"

# TODO: Use csv
# TODO: Use function to read files

# Accessing datasets
occupied = {}
try:
    for line in open(RESERVATION_FILE):
        userName, roomCode, roomDays = line.strip().split(",")
        occupied[int(roomCode)] = {
            "clientName": userName,
            "days": int(roomDays)
        }
except FileNotFoundError:
    logging.error(f"File {RESERVATION_FILE} do not exist.")
    sys.exit(1)


rooms = {}
try:
    for line in open(ROOMS_FILE):
        code, name, price = line.strip().split(",")
        rooms[int(code)] = {
            "name": name,
            "price": float(price), # TODO: Decimal (always treat price as DECIMAL)
            "available": False if int(code) in occupied else True
        }
except FileNotFoundError:
    logging.error(f"File {ROOMS_FILE} do not exist.")
    sys.exit(1)

# Main Code
print("Pythonic Hotel Reservation")
print("-" * 52 + "\n")

if len(occupied) == len(rooms):
    print("Pythonic Hotel is full, no rooms available at this time!")
    sys.exit(0)

userName = input("Client Name:")

print("-" * 52)
print("List of Rooms Available")
print()

head = ["Availability", "Room Code", "Description", "Price"]
print(f"{head[0]:<11} - {head[1]:<9} - {head[2]:<12} - $ {head[3]:<9}")
for code, data in rooms.items():
    name = data["name"]
    price = data["price"]
    available = "⛔" if not data["available"] else "🟢"
    #available = data["available"] and "🟢" or "⛔"
    print(f"{available:<11} - {code:<9} - {name:<12} - $ {price:<9.2f}")
print("-" * 52)


try:
    roomCode = int(input("Room number:").strip())
    if not rooms[roomCode]["available"]:
        print(f"Room {roomCode} is not available.")
        sys.exit(0)
except ValueError:
    logging.error("Number is invalid. Use only digits.")
    sys.exit(1)
except KeyError:
    print(f"Room {roomCode} does not exist.")
    sys.exit(0)

try:
    roomDays = int(input("Quantity of Days?:").strip())
except ValueError:
    logging.error("Number is invalid. Use only digits.")
    sys.exit(1)

roomName = rooms[roomCode]["name"]
roomPrice = rooms[roomCode]["price"]
roomAvailable = rooms[roomCode]["available"]

total = roomPrice * roomDays

print(f"{userName} you choose the {name} ({roomCode}) for {roomDays} days "
      f"and that will cost $ {total:.2f}.")

#print((f"{userName},{roomCode},{roomDays}"))
#print(",".join([userName, str(roomCode), str(roomDays)]))

if input("Confirm? [Y/n]").strip().lower() in ("y", "yes"):
    with open("reservation_reserved.txt", "a") as file_:
        file_.write(f"{userName},{roomCode},{roomDays}\n")
