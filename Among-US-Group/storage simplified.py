import json
import os

# SAVE: Turn the dictionary into text and write it to a file
seats = {"seat_1": "free", "seat_2": "occupied"}
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
