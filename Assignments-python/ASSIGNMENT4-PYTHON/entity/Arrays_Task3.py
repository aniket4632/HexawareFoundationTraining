import time
import random

class Parcel:
    def __init__(self, parcel_id):
        self.parcel_id = parcel_id
        self.tracking_history = []

    def add_location_update(self, location):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.tracking_history.append({"timestamp": timestamp, "location": location})

def track_parcel(parcel, destination):
    print(f"Parcel {parcel.parcel_id} is on the way to {destination}.")

    while parcel.tracking_history[-1]["location"] != destination:
        new_location = parcel.tracking_history[-1]["location"] + 1
        parcel.add_location_update(new_location)
        time.sleep(random.uniform(0.5, 2.0))
        print(f"Parcel {parcel.parcel_id} is now at location {new_location}.")

    print(f"Parcel {parcel.parcel_id} has reached the destination {destination}.")

def main():
    parcel_id = input("Enter parcel ID: ")
    starting_location = int(input("Enter starting location: "))
    destination = int(input("Enter destination location: "))

    parcel = Parcel(parcel_id)
    parcel.add_location_update(starting_location)
    track_parcel(parcel, destination)

    print(f"\nTracking History for Parcel {parcel.parcel_id}:")
    for update in parcel.tracking_history:
        print(f"{update['timestamp']} - Location: {update['location']}")

if __name__ == "__main__":
    pass


import sys

class Courier:
    def __init__(self, name, proximity):
        self.name = name
        self.proximity = proximity

def find_nearest_courier(order_location, couriers):
    min_distance = sys.maxsize
    nearest_courier = None

    for courier in couriers:
        distance = abs(order_location - courier.proximity)
        if distance < min_distance :
            min_distance = distance
            nearest_courier = courier

    return nearest_courier

def main():
    couriers = [
        Courier("Courier1", 5 ),
        Courier("Courier2", 8 ),
        Courier("Courier3", 12)
    ]

    order_location = int(input("Enter order location: "))

    nearest_courier = find_nearest_courier(order_location, couriers)

    if nearest_courier:
        print(f"The nearest available courier is {nearest_courier.name}.")
    else:
        print("No available courier for the order.")

if __name__ == "__main__":
    main()
