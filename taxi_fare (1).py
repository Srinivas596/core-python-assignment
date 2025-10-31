# Taxi Fare Calculation

def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10 * distance
    return base_fare + distance_fare

def total_fare(trips):
    total = 0
    for i, trip in enumerate(trips, start=1):
        fare = calculate_fare(trip)
        print(f"Trip {i}: ${fare}")
        total += fare
    return total


if __name__ == "__main__":
    trips = [5, 10, 3]
    total = total_fare(trips)
    print(f"Total Fare: ${total}")
