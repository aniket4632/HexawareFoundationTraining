customers = ["Customer1", "Customer2", "Customer3"]
orders_customer1 = ["Order1A", "Order1B", "Order1C"]
orders_customer2 = ["Order2A", "Order2B"]
orders_customer3 = ["Order3A", "Order3B", "Order3C", "Order3D"]

def display_orders(customer_name):
    orders = globals().get(f"orders_{customer_name.lower()}")
    if orders:
        print(f"Orders for {customer_name}:")
        for order in orders:
            print(order)
    else:
        print("No orders available for the customer.")
def main():
    customer_name = input("Enter customer name: ")

    if customer_name in customers:
        display_orders(customer_name)
    else:
        print("Customer not found.")

if __name__ == "__main__":
    pass

import time
import random
def track_courier(courier_name, current_location, destination):
    print(f"{courier_name} is on the way to {destination}.")

    while current_location != destination:
        current_location += 1
        time.sleep(random.uniform(0.5, 2.0))
        print(f"{courier_name} is now at location {current_location}.")

    print(f"{courier_name} has reached the destination {destination}.")

def main():
    courier_name = input("Enter courier name: ")
    current_location = int(input("Enter current location: "))
    destination = int(input("Enter destination location: "))

    track_courier(courier_name, current_location, destination)

if __name__ == "__main__":
    main()
