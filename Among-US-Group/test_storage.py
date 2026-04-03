from storage import load_seats, save_seats

save_seats({"seat_1": "free", "seat_2": "occupied"})
print(load_seats())
