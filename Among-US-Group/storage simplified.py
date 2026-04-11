import json
import os

# SAVE: Turn the dictionary into text and write it to a file
seats = {"seat_A1": "free", "seat_A2": "occupied", "seat_A3": "free", "seat_A4": "occupied", "seat_A5": "free", "seat_A6": "occupied", "seat_A7": "free", "seat_A8": "occupied", "seat_A9": "free", "seat_A10": "occupied"}
text = json.dumps(seats)
file = open("seats.json", "w")
file.write(text)
file.close()

# LOAD: Read the text from the file and turn it back into a dictionary
file = open("seats.json", "r")
text = file.read()
file.close()
seats = json.loads(text)

print(seats)
