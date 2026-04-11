import json
import os

# SAVE: Turn the dictionary into text and write it to a file
seats = {"seat_1": "free", "seat_2": "occupied", "seat_3": "free", "seat_4": "occupied", "seat_5": "free", "seat_6": "occupied", "seat_7": "free", "seat_8": "occupied", "seat_9": "free", "seat_10": "occupied"}
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
