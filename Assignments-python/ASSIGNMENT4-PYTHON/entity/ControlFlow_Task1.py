#TASK 1.1
def check_delivery_status(order_status):
    if order_status == "Delivered":
        print("The order has been delivered.")
    elif order_status == "Processing":
        print("The order is still being processed.")
    elif order_status == "Cancelled":
        print("The order has been cancelled.")
    else:
        print("Invalid order status.")

def main():
    order_status = input("Enter the order status: ")
    check_delivery_status(order_status)

#TASK 1.2
def categorize_parcel(weight):
    category = None

    if weight < 5:
        category = "Light"
    elif 5 <= weight < 10:
        category = "Medium"
    elif weight >= 10:
        category = "Heavy"
    else:
        category = "Invalid weight category."

    return f"The parcel is {category}."

def main1():
    parcel_weight = float(input("Enter the parcel weight (in kg): "))
    print(categorize_parcel(parcel_weight))
#TASK1.3
def authenticate_user(username, password, user_type):
    employee_username = "employee123"
    employee_password = "pass123"
    customer_username = "customer123"
    customer_password = "pass123"

    if user_type == "employee":
        if username == employee_username and password == employee_password:
            return "Welcome, Employee!"
        else:
            return "Invalid credentials for employee. Please try again."
    elif user_type == "customer":
        if username == customer_username and password == customer_password:
            return "Welcome, Customer!"
        else:
            return "Invalid credentials for customer. Please try again."
    else:
        return "Invalid user type. Please enter 'employee' or 'customer'."
def main2():
    user_type = input("Enter user type (employee/customer): ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    result = authenticate_user(username, password, user_type.lower())
    print(result)

#TASK 1.4
shipments = [
    {"destination": 7, "weight": 10},
    {"destination": 10, "weight": 5},
    {"destination": 5, "weight": 8},
]

couriers = [
    {"name": "Courier1", "proximity": 5, "max_capacity": 20, "current_load": 0},
    {"name": "Courier2", "proximity": 8, "max_capacity": 15, "current_load": 0},
]
for shipment in shipments:
    min_distance = float('inf')
    assigned_courier = None

    for courier in couriers:
        distance = abs(shipment["destination"] - courier["proximity"])

        if distance < min_distance and courier["current_load"] + shipment["weight"] <= courier["max_capacity"]:
            min_distance = distance
            assigned_courier = courier
    if assigned_courier:
        assigned_courier["current_load"] += shipment["weight"]
        print(f"Shipment to {shipment['destination']} kg assigned to courier {assigned_courier['name']}.")
    else:
        print(f"No available courier for shipment to {shipment['destination']} kg.")


if __name__=="__main__":
     pass

