from CaseStudy_01.dao.CustomerService import CustomerService
from CaseStudy_01.dao.VehicleService import VehicleService
from CaseStudy_01.dao.ReservationService import ReservationService
from CaseStudy_01.dao.AdminService import AdminService
from CaseStudy_01.util.DBConnUtil import DBConnUtil
from CaseStudy_01.util.DBPropertyUtil import DBPropertyUtil
from CaseStudy_01.dao.AuthenticationService import AuthenticationService
from CaseStudy_01.exception.Exception import AuthenticationException
from CaseStudy_01.dao.ReportGenerator import ReportGenerator
from datetime import datetime, timedelta
from decimal import Decimal


def display_main_menu():
    print("Main Menu:")
    print("1. Customer Service")
    print("2. Vehicle Service")
    print("3. Reservation Service")
    print("4. Admin Service")
    print("5. Authentication Service")
    print("6. Report Generation")
    print("0. Exit")


def display_customer_menu():
    print("Customer Service:")
    print("1. Get Customer by ID")
    print("2. Get Customer by Username")
    print("3. Register a new Customer")
    print("4. Update Customer information")
    print("5. Delete a Customer")
    print("0. Back to Main Menu")


def display_vehicle_menu():
    print("Vehicle  Service:")
    print("1. Get Vehicle by ID")
    print("2. Get Available Vehicles ")
    print("3. Add Vehicle")
    print("4. Update Vehicle")
    print("5. Remove Vehicle")
    print("0. Back to Main Menu")


def display_reservation_menu():
    print("Reservation Service:")
    print("1. Get Reservation  by ID")
    print("2. Get Reservation by CustomerId")
    print("3. Create Reservation ")
    print("4. Update Reservation ")
    print("5. Cancel Reservation ")
    print("0. Back to Main Menu")


def display_admin_menu():
    print("Admin Service:")
    print("1. Get Admin  by ID")
    print("2. Get Admin  by Username")
    print("3. Register Admin  ")
    print("4. Update Admin  ")
    print("5. Delete Admin ")
    print("0. Back to Main Menu")


def display_authentication_menu():
    print("Authentication Service:")
    print("1. Authenticate Customer")
    print("2. Authenticate Admin")
    print("0. Back to Main Menu")


def display_reportgeneration_menu():
    print("Report Generation:")
    print("1. Generate Reservation Report")
    print("2. Generate Vehicle Report")
    print("0. Back to Main Menu")


def main():
    connection_string = DBPropertyUtil.get_connection_string()
    db_conn_util = DBConnUtil()
    customer_service = CustomerService(db_conn_util, connection_string)
    vehicle_service = VehicleService(db_conn_util, connection_string)
    reservation_service = ReservationService(db_conn_util, connection_string)
    admin_service = AdminService(db_conn_util, connection_string)

    while True:
        display_main_menu()
        main_choice = input("Enter your choice (0-6): ")

        if main_choice == '0':
            print("Thankyou !! Signing out the Car Connect System.")
            break
        elif main_choice == '1':
            while True:
                display_customer_menu()
                customer_choice = input("Enter your choice (0-5): ")

                if customer_choice == '0':
                    break
                elif customer_choice == '1':
                    customer_id = int(input("Enter customer ID: "))
                    customer_data = customer_service.GetCustomerById(customer_id)
                    print("Customer Data:", customer_data)
                elif customer_choice == '2':
                    username = input("Enter customer username: ")
                    customer_data = customer_service.GetCustomerByUsername(username)
                    print("Customer Data:", customer_data)
                elif customer_choice == '3':
                    customer_data = {
                        'first_name': input("Enter first name: "),
                        'last_name': input("Enter last name: "),
                        'email': input("Enter email: "),
                        'phone_number': input("Enter phone number: "),
                        'address': input("Enter address: "),
                        'username': input("Enter username: "),
                        'password': input("Enter password: "),
                        'registration_date': input("Enter registration date (YYYY-MM-DD): ")
                    }
                    customer_service.RegisterCustomer(customer_data)
                elif customer_choice == '4':
                    customer_id_to_update = int(input("Enter customer ID to update: "))
                    customer_data_to_update = {
                        'customer_id': customer_id_to_update,
                        'first_name': input("Enter updated first name: "),
                        'last_name': input("Enter updated last name: "),
                        'email': input("Enter updated email: "),
                        'phone_number': input("Enter updated phone number: "),
                        'address': input("Enter updated address: "),
                        'username': input("Enter updated username: "),
                        'password': input("Enter updated password: "),
                        'registration_date': input("Enter updated registration date (YYYY-MM-DD): ")
                    }
                    customer_service.UpdateCustomer(customer_data_to_update)
                elif customer_choice == '5':
                    customer_id_to_delete = int(input("Enter customer ID to delete: "))
                    customer_service.DeleteCustomer(customer_id_to_delete)
                else:
                    print("Invalid choice. Please enter a valid option.")
        elif main_choice == '2':
            while True:
                display_vehicle_menu()
                vehicle_choice = input("Enter your choice (0-5): ")
                if vehicle_choice == '0':
                    break
                elif vehicle_choice == '1':
                    vehicle_id_to_get = int(input("Enter vehicle ID to get: "))
                    vehicle_data_to_get = vehicle_service.GetVehicleById(vehicle_id_to_get)

                    if vehicle_data_to_get:
                        print("\nVehicle Data:", vehicle_data_to_get)
                    else:
                        print(f"No vehicle found with ID {vehicle_id_to_get}.")

                elif vehicle_choice == '2':
                    available_vehicles = vehicle_service.GetAvailableVehicles()

                    if available_vehicles:
                        print("\nAvailable Vehicles:")
                        for vehicle in available_vehicles:
                            print(vehicle)
                    else:
                        print("No available vehicles.")

                elif vehicle_choice == '3':
                    new_vehicle_data = {
                        'model': input("Enter model: "),
                        'make': input("Enter make: "),
                        'year': int(input("Enter year: ")),
                        'color': input("Enter color: "),
                        'registration_number': input("Enter registration number: "),
                        'availability': True,
                        'daily_rate': float(input("Enter daily rate: "))
                    }
                    vehicle_service.AddVehicle(new_vehicle_data)

                elif vehicle_choice == '4':
                    vehicle_id_to_update = int(input("Enter vehicle ID to update: "))
                    updated_vehicle_data = {
                        'vehicle_id':vehicle_id_to_update,
                        'model': input("Enter updated model: "),
                        'make': input("Enter updated make: "),
                        'year': int(input("Enter updated year: ")),
                        'color': input("Enter updated color: "),
                        'registration_number': input("Enter updated registration number: "),
                        'availability': True,
                        'daily_rate': float(input("Enter updated daily rate: "))
                    }
                    vehicle_service.UpdateVehicle(updated_vehicle_data)
                else:
                    print("Invalid choice. Please enter a valid option.")
        elif main_choice == '3':
            while True:
                display_reservation_menu()
                reservation_choice = input("Enter your choice (0-5): ")
                if reservation_choice == '0':
                    break
                elif reservation_choice == '1':
                    reservation_id_to_get = int(input("Enter reservation ID to get: "))
                    reservation_data_to_get = reservation_service.GetReservationById(reservation_id_to_get)

                    if reservation_data_to_get:
                        print("\nReservation Data:", reservation_data_to_get)
                    else:
                        print(f"No reservation found with ID {reservation_id_to_get}.")

                elif reservation_choice == '2':
                    customer_id_to_get_reservations = int(input("Enter customer ID to get reservations: "))
                    reservations_data_by_customer = reservation_service.GetReservationsByCustomerId(
                        customer_id_to_get_reservations)

                    if reservations_data_by_customer:
                        print("\nReservations Data:")
                        for reservation in reservations_data_by_customer:
                            print(reservation)
                    else:
                        print(f"No reservations found for customer ID {customer_id_to_get_reservations}.")

                elif reservation_choice == '3':
                    reservation_data_to_create = {
                        'customer_id': int(input("Enter customer ID: ")),
                        'vehicle_id': int(input("Enter vehicle ID: ")),
                        'start_date': datetime.now(),
                        'end_date': datetime.now() + timedelta(
                            days=int(input("Enter reservation duration (in days): "))),
                        'total_cost': Decimal(input("Enter total cost: ")),
                        'status': input("Enter reservation status: ")
                    }
                    reservation_service.CreateReservation(reservation_data_to_create)

                elif reservation_choice == '4':
                    reservation_id_to_update = int(input("Enter reservation ID to update: "))
                    updated_reservation_data = {
                        'reservation_id': reservation_id_to_update,
                        'customer_id': int(input("Enter updated customer ID: ")),
                        'vehicle_id': int(input("Enter updated vehicle ID: ")),
                        'start_date': datetime.now(),
                        'end_date': datetime.now() + timedelta(
                            days=int(input("Enter updated reservation duration (in days): "))),
                        'total_cost': Decimal(input("Enter updated total cost: ")),
                        'status': input("Enter updated reservation status: ")
                    }
                    reservation_service.UpdateReservation(updated_reservation_data)

                elif reservation_choice == '5':
                    reservation_id_to_cancel = int(input("Enter reservation ID to cancel: "))
                    reservation_service.CancelReservation(reservation_id_to_cancel)
                else:
                    print("Invalid choice. Please enter a valid option.")
        elif main_choice == '4':
            while True:
                display_admin_menu()
                admin_choice = input("Enter your choice (0-5): ")
                if admin_choice == '0':
                    break
                if admin_choice == '1':
                    admin_id_to_get = int(input("Enter admin ID to get: "))
                    admin_data_to_get = admin_service.GetAdminById(admin_id_to_get)

                    if admin_data_to_get:
                        print("\nAdmin Data:", admin_data_to_get)
                    else:
                        print(f"No admin found with ID {admin_id_to_get}.")

                elif admin_choice == '2':
                    admin_username_to_get = input("Enter admin username to get: ")
                    admin_data_by_username = admin_service.GetAdminByUsername(admin_username_to_get)

                    if admin_data_by_username:
                        print("\nAdmin Data:", admin_data_by_username)
                    else:
                        print(f"No admin found with username {admin_username_to_get}.")

                elif admin_choice == '3':
                    admin_data_to_register = {
                        'first_name': input("Enter first name: "),
                        'last_name': input("Enter last name: "),
                        'email': input("Enter email: "),
                        'phone_number': input("Enter phone number: "),
                        'username': input("Enter username: "),
                        'password': input("Enter password: "),
                        'role': input("Enter role: "),
                        'join_date': input("Enter join date (YYYY-MM-DD): ")
                    }
                    admin_service.RegisterAdmin(admin_data_to_register)

                elif admin_choice == '4':
                    admin_id_to_update = int(input("Enter admin ID to update: "))
                    admin_data_to_update = {
                        'admin_id': admin_id_to_update,
                        'first_name': input("Enter updated first name: "),
                        'last_name': input("Enter updated last name: "),
                        'email': input("Enter updated email: "),
                        'phone_number': input("Enter updated phone number: "),
                        'password': input("Enter updated password: "),
                    }
                    admin_service.UpdateAdmin(admin_data_to_update)
                    print("Admin updated successfully.")

                elif admin_choice == '5':
                    admin_id_to_delete = int(input("Enter admin ID to delete: "))
                    admin_service.DeleteAdmin(admin_id_to_delete)
                else:
                    print("Invalid choice. Please enter a valid option.")
        elif main_choice == '5':
            while True:
                display_authentication_menu()
                auth_choice = input("Enter your choice (0-2): ")
                if auth_choice == '0':
                    break
                elif auth_choice == '1':
                    username = input("Enter customer username: ")
                    password = input("Enter customer password: ")

                    try:
                        customer = AuthenticationService.authenticate_customer(username, password, connection_string)
                        print("Customer authenticated:", customer)

                    except AuthenticationException as e:
                        print(f"Authentication failed: {str(e)}")

                elif auth_choice == '2':
                    admin_username = input("Enter admin username: ")
                    admin_password = input("Enter admin password: ")

                    try:
                        admin = AuthenticationService.authenticate_admin(admin_username, admin_password,
                                                                         connection_string)
                        print("Admin authenticated:", admin)

                    except AuthenticationException as e:
                        print(f"Authentication failed: {str(e)}")
                else:
                    print("Invalid choice. Please enter a valid option.")
        elif main_choice == '6':
            while True:
                display_reportgeneration_menu()
                report_choice = input("Enter your choice (0-2): ")
                if report_choice == '0':
                    break
                elif report_choice == '1':
                    reservation_service = ReservationService(db_conn_util, connection_string)
                    reservation_data = reservation_service.GetReservationsList()
                    ReportGenerator.generate_reservation_report(reservation_data)
                    print("Reservation Report generated successfully.")

                elif report_choice == '2':
                    vehicle_service = VehicleService(db_conn_util, connection_string)
                    vehicle_data = vehicle_service.GetAvailableVehicles()
                    ReportGenerator.generate_vehicle_report(vehicle_data)
                    print("Vehicle Report generated successfully.")
                else:
                    print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
