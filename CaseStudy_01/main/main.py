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


def main():
    connection_string = DBPropertyUtil.get_connection_string()
    db_conn_util = DBConnUtil()
    '''
    customer_service = CustomerService(db_conn_util,connection_string)
    
    customer_id = 1
    customer_data = customer_service.GetCustomerById(customer_id)
    print("Customer Data:", customer_data)
    
    username='priya_sharma'
    customer_data1 = customer_service.GetCustomerByUsername(username)
    print("Customer Data:", customer_data1)
    
    customer_data2 = {
        'first_name': 'Aniket',
        'last_name': 'Biyani',
        'email': 'anixbiyani@example.com',
        'phone_number': '7020905391',
        'address': 'Latur',
        'username': 'aniket',
        'password': 'Aniket@123',
        'registration_date': '2024-01-01'}

    customer_service.RegisterCustomer(customer_data2)
    updated_customer_data = {
        'customer_id': 12,
        'first_name': 'Abhi',
        'last_name': 'Surya',
        'email': 'abhi.surya@example.com',
        'phone_number': '766676743',
        'address': 'Mumbai',
        'username': 'abhi_102',
        'password': 'abhi@123',
        'registration_date': '2023-01-01'}
   
    customer_service.UpdateCustomer(updated_customer_data)
    
    customer_service.DeleteCustomer(12)
    '''
    '''
    vehicle_service = VehicleService(db_conn_util,connection_string)
    
    vehicle_id = 1
    vehicle_data = vehicle_service.GetVehicleById(vehicle_id)
    print("Vechicle Data:", vehicle_data)
    

    available_vehicles=vehicle_service.GetAvailableVehicles()
    print("Available Vehicles:")
    for vehicle in available_vehicles:
        print(vehicle)
    
    new_vehicle_data = {
        'model': 'Sedan',
        'make': 'Toyota',
        'year': 2022,
        'color': 'Blue',
        'registration_number': 'ABC123',
        'availability': True,
        'daily_rate': 50.0
    }
    vehicle_service.AddVehicle(new_vehicle_data)
    
    updated_vehicle_data = {
        'vehicle_id': 12,
        'model': 'swift',
        'make': 'maruti',
        'year': 2021,
        'color': 'Grey',
        'registration_number': 'BM4683',
        'availability': True,
        'daily_rate': 60.0
    }
    
    vehicle_service.UpdateVehicle(updated_vehicle_data)
    
    vehicle_service.RemoveVehicle(12)
    '''
    '''
    reservation_service = ReservationService(db_conn_util, connection_string)
    
    reservation_id = 1

    reservation_data = reservation_service.GetReservationById(reservation_id)
    print("Reservation Data:", reservation_data)
    
    customer_id = 1
    reservations_data = reservation_service.GetReservationsByCustomerId(customer_id)
    print("Reservations Data:", reservations_data)
    
    reservation_data = {
        'customer_id': 1,
        'vehicle_id': 1,
        'start_date': datetime.now(),
        'end_date': datetime.now() + timedelta(days=3),
        'total_cost': Decimal('150.00'),
        'status': 'Confirmed'
    }

    reservation_service.CreateReservation(reservation_data)
    
    updated_reservation_data = {
        'reservation_id': 12,
        'customer_id': 1,
        'vehicle_id': 1,
        'start_date': datetime.now(),
        'end_date': datetime.now() + timedelta(days=5),
        'total_cost': Decimal('200.00'),
        'status': 'Updated'
    }

    reservation_service.UpdateReservation(updated_reservation_data)
    reservation_id_to_cancel = 12

    reservation_service.CancelReservation(reservation_id_to_cancel)

    '''
    '''
    admin_service = AdminService(db_conn_util,connection_string)
    
    admin_id_to_fetch = 1

    admin_data = admin_service.GetAdminById(admin_id_to_fetch)
    print("Admin Data:", admin_data)
    
    admin_username_to_fetch = "john_admin"

    admin_data = admin_service.GetAdminByUsername(admin_username_to_fetch)
    print("Admin Data:", admin_data)

    admin_data_to_register = {
        'first_name': 'Admin',
        'last_name': 'User',
        'email': 'admin@example.com',
        'phone_number': '1234567890',
        'username': 'admin_username',
        'password': 'admin_password',
        'role': 'Admin',
        'join_date': '2024-01-01'
    }
    
    admin_service.RegisterAdmin(admin_data_to_register)

    admin_data_to_update = {
        'admin_id': 12,
        'first_name': 'UpdatedAdmin',
        'last_name': 'UpdatedUser',
        'email': 'updated_admin@example.com',
        'phone_number': '9876543210',
        'password': 'new_admin_password',
    }

    admin_service.UpdateAdmin(admin_data_to_update)
    
    admin_id_to_delete = 12

    admin_service.DeleteAdmin(admin_id_to_delete)
    '''
    '''
    connection_string = DBPropertyUtil.get_connection_string()

    try:
        customer = AuthenticationService.authenticate_customer("john_doe", "new_password",
                                                               connection_string)
        print("Customer authenticated:", customer)

    except AuthenticationException as e:
        print(f"Authentication failed: {str(e)}")
    '''
    '''
    connection_string = DBPropertyUtil.get_connection_string()

    try:
        admin = AuthenticationService.authenticate_admin("shreya_admin", "hashed_password_10",
                                                               connection_string)
        print("Admin authenticated:", admin)

    except AuthenticationException as e:
        print(f"Authentication failed: {str(e)}")
    '''
    '''
    reservation_service = ReservationService(db_conn_util, connection_string)
    vehicle_service = VehicleService(db_conn_util,connection_string)


    reservation_data = reservation_service.GetReservationsList()
    vehicle_data = vehicle_service.GetAvailableVehicles()

    ReportGenerator.generate_reservation_report(reservation_data)
    ReportGenerator.generate_vehicle_report(vehicle_data)
    '''
if __name__ == "__main__":
   main()
