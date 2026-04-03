import.json
import.os
DATA_FILE = "Chairy/shared/seats/_data.json" 
def load_seats():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return data
def save_seats(seats):
    with open(DATA_FILE, "w") as f:
        json.dump(seats, f, indent=2)

        