#TASK 4 .9
class ParcelTracker:
    def __init__(self):
        self.tracking_data = [
            ["123456", "In transit"],
            ["789012", "Out for delivery"],
            ["345678", "Delivered"],
            ["901234", "In transit"]
        ]
    def track_parcel(self, tracking_number):
        for parcel in self.tracking_data:
            if parcel[0] == tracking_number:
                status = parcel[1]
                if status == "In transit":
                    print(f"Parcel {tracking_number} is currently in transit.")
                elif status == "Out for delivery":
                    print(f"Parcel {tracking_number} is out for delivery.")
                elif status == "Delivered":
                    print(f"Parcel {tracking_number} has been delivered.")
                return

        print(f"Parcel {tracking_number} not found in the tracking system.")
def main():
    parcel_tracker = ParcelTracker()
    while True:
        tracking_number = input("Enter parcel tracking number (or 'exit' to quit): ")

        if tracking_number.lower() == 'exit':
            break

        parcel_tracker.track_parcel(tracking_number)

if __name__ == "__main__":
   pass
#TASK 4.10
import re

def validate_customer_information(data, detail):
    if detail == "name":
        if data.isalpha() and data.istitle():
            return True
        else:
            return False
    elif detail == "address":
        if data.isalnum() or not any(char.isalnum() or char.isspace() for char in data):
            return True
        else:
            return False
    elif detail == "phone_number":
        phone_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
        if phone_pattern.match(data):
            return True
        else:
            return False
    else:
        return False

def main1():
    customer_name = input("Enter customer name: ")
    if validate_customer_information(customer_name, "name"):
        print("Valid name.")
    else:
        print("Invalid name.")

    customer_address = input("Enter customer address: ")
    if validate_customer_information(customer_address, "address"):
        print("Valid address.")
    else:
        print("Invalid address.")

    customer_phone_number = input("Enter customer phone number (format: ###-###-####): ")
    if validate_customer_information(customer_phone_number, "phone_number"):
        print("Valid phone number.")
    else:
        print("Invalid phone number.")

if __name__ == "__main__":
    pass
#TASK 4.11
def format_address(street, city, state, zip_code):

    formatted_street = ' '.join(word.capitalize() for word in street.split())
    formatted_city = city.title()
    formatted_state = state.capitalize()
    formatted_zip_code = str(zip_code).zfill(5)
    formatted_address = f"{formatted_street}, {formatted_city}, {formatted_state} {formatted_zip_code}"

    return formatted_address
def main2():
    print("Enter the address")
    street_input = input("Enter street: ")
    city_input = input("Enter city: ")
    state_input = input("Enter state: ")
    zip_code_input = input("Enter zip code: ")

    formatted_address = format_address(street_input, city_input, state_input, zip_code_input)
    print("Formatted Address:", formatted_address)
if __name__ == "__main__":
    pass
#TASK #4.12
def generate_order_confirmation(customer_name, order_number, delivery_address, expected_delivery_date):
    email_content = f"Dear {customer_name},\n\n"
    email_content += f"Thank you for your order! Your order number is {order_number}.\n"
    email_content += f"We will deliver your items to the following address:\n{delivery_address}\n"
    email_content += f"Expected delivery date: {expected_delivery_date}\n\n"
    email_content += "Thank you for choosing our services. If you have any questions, feel free to contact us.\n\n"
    email_content += "Best regards,\nThe Delhivery Company"

    return email_content
def main3():
    customer_name = input("Enter the Customer name")
    order_number = int(input("Enter the order number"))
    delivery_address = input("Enter the address")
    expected_delivery_date = input("Enter the Expected Delievery date")

    confirmation_email = generate_order_confirmation(customer_name, order_number, delivery_address, expected_delivery_date)

    print("Generated Order Confirmation Email:\n")
    print(confirmation_email)
if __name__ == "__main__":
    pass


#TASK 4.13
def calculate_shipping_cost(source_address,destination_address,parcel_weight):
    rate_per_km=5

    if(parcel_weight<=5):
        rate_Of_weight=10
    else:
        rate_Of_weight=20
    distance=destination_address-source_address
    rate=distance*rate_per_km+rate_Of_weight
    return rate


def main4():
    source_address =float(input("Enter the source address location point in number: "))
    destination_address = float(input("Enter the destination location Point: "))
    parcel_weight = float(input("Enter the parcel weight in pounds: "))
    shipping_cost = calculate_shipping_cost(source_address,destination_address,parcel_weight)
    print(f"Shipping cost: Rs{shipping_cost:.2f}")

if __name__ == "__main__":
    pass

#TASK 4.14
import random
import string

def generate_secure_password(length=12):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    password = (
        random.choice(uppercase_letters)
        + random.choice(lowercase_letters)
        + random.choice(digits)
        + random.choice(special_characters)
    )
    for _ in range(length - 4):
        password += random.choice(all_characters)
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password
def main5():
    secure_password = generate_secure_password()
    print("Generated Password:", secure_password)
if __name__ == "__main__":
    pass
#TASK 4.15
def find_similar_addresses(target_address, addresses_list):
    similar_addresses = []
    target_address_lower = target_address.lower()
    for address in addresses_list:
        address_lower = address.lower()

        if target_address_lower in address_lower or address_lower in target_address_lower:
            similar_addresses.append(address)

    return similar_addresses
def main5():
    target_address = "123 Main St, Cityville, USA"
    addresses_list = [
        "123 Main St, Cityville, USA",
        "124 Main St, Cityville, USA",
        "456 Broad St, Townsville, USA",
        "789 Oak St, Villagetown, USA",
    ]

    similar_addresses = find_similar_addresses(target_address, addresses_list)
    print(f"Target Address: {target_address}")
    print("Similar Addresses:")
    for similar_address in similar_addresses:
        print(similar_address)
if __name__ == "__main__":
    main5()