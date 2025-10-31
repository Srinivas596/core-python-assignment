# Movie Ticket Booking System

def available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

def book_seat(booked_seats, seat_no):
    if seat_no in booked_seats:
        print(f"Seat {seat_no} is already booked.")
    else:
        booked_seats.append(seat_no)
    return booked_seats

def cancel_seat(booked_seats, seat_no):
    if seat_no in booked_seats:
        booked_seats.remove(seat_no)
    else:
        print(f"Seat {seat_no} is not booked.")
    return booked_seats


if __name__ == "__main__":
    total_seats = 10
    booked_seats = [2, 5, 7]
    book_seat_no = 3
    cancel_seat_no = 5

    booked_seats = book_seat(booked_seats, book_seat_no)
    booked_seats = cancel_seat(booked_seats, cancel_seat_no)
    print("Available seats:", available_seats(total_seats, booked_seats))
