import unittest
from unittest.mock import MagicMock
from CaseStudy_01.dao.AuthenticationService import AuthenticationService
from CaseStudy_01.exception.Exception import AuthenticationException
from CaseStudy_01.dao.CustomerService import CustomerService
from CaseStudy_01.dao.VehicleService import VehicleService



class TestAuthenticationService(unittest.TestCase):
    def setUp(self):
        self.customer_service = MagicMock()
        self.db_conn_util = MagicMock()
        self.connection_string = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': 'Aniket@123',
            'database': 'carconnect'
        }
        self.customer_service1 = CustomerService(self.db_conn_util,self.connection_string)
        self.auth_service = AuthenticationService(self.customer_service, self.db_conn_util, self.connection_string)
        self.vehicle_service = VehicleService(self.db_conn_util,self.connection_string)

    '''
    def test_authenticate_customer_with_invalid_credentials(self):
        self.customer_service.GetCustomerByUsername.return_value = None

        with self.assertRaises(AuthenticationException):
            self.auth_service.authenticate_customer("john_doe", "password",self.connection_string)
    '''
    '''
    def test_update_customer_information(self):

        self.customer_service.GetCustomerById = MagicMock(return_value={
            'CustomerID': 1,
            'FirstName': 'John',
            'LastName': 'Doe',
            'Email': 'john.doe@example.com',
            'PhoneNumber': '1234567890',
            'Address': '123 Main St',
            'Username': 'john_doe',
            'Password': 'old_password',
            'RegistrationDate': '2022-01-01'
        })

        updated_customer_data = {
            'CustomerID': 1,
            'FirstName': 'John',
            'LastName': 'Doe',
            'Email': 'john.doe@example.com',
            'PhoneNumber': '9876543210',
            'Address': '123 Main St',
            'Username': 'john_doe',
            'Password': 'old_password',
            'RegistrationDate': '2022-01-01'
        }
        self.customer_service.UpdateCustomer = MagicMock(return_value=updated_customer_data)

        result = self.customer_service.UpdateCustomer(updated_customer_data)
        self.assertEqual(result, updated_customer_data)
    '''
    '''
    def test_add_new_vehicle(self):

        new_vehicle_data = {
            'VehicleID': 1,
            'Brand': 'Toyota',
            'Model': 'Camry',
            'Year': 2022,
            'RegistrationPlate': 'ABC123',
            'Color': 'Blue',
            'Type': 'Sedan',
            'Availability': True
        }
        self.vehicle_service.AddVehicle = MagicMock(return_value=new_vehicle_data)

        result = self.vehicle_service.AddVehicle(new_vehicle_data)
        self.assertEqual(result, new_vehicle_data)
    '''
    '''
    def test_update_vehicle_details(self):
        updated_vehicle_data = {
            'VehicleID': 1,
            'Brand': 'Updated Brand',
            'Model': 'Updated Model',
            'Year': 2023,
            'RegistrationPlate': 'XYZ789',
            'Color': 'Red',
            'Type': 'SUV',
            'Availability': True
        }
        self.vehicle_service.UpdateVehicle = MagicMock(return_value=updated_vehicle_data)

        result = self.vehicle_service.UpdateVehicle(updated_vehicle_data['VehicleID'], updated_vehicle_data)
        self.assertEqual(result, updated_vehicle_data)
    '''
    '''
    def test_get_available_vehicles(self):
        available_vehicles = [
            {
                'VehicleID': 1,
                'Brand': 'Toyota',
                'Model': 'Camry',
                'Year': 2022,
                'RegistrationPlate': 'ABC123',
                'Color': 'Blue',
                'Type': 'Sedan',
                'Availability': True
            },
            {
                'VehicleID': 2,
                'Brand': 'Honda',
                'Model': 'Civic',
                'Year': 2021,
                'RegistrationPlate': 'XYZ789',
                'Color': 'Silver',
                'Type': 'Sedan',
                'Availability': True
            }
        ]
        self.vehicle_service.GetAvailableVehicles = MagicMock(return_value=available_vehicles)
        result = self.vehicle_service.GetAvailableVehicles()
        self.assertEqual(result, available_vehicles)
    '''
    '''
    def test_get_all_vehicles(self):
        all_vehicles = [
            {
                'VehicleID': 1,
                'Brand': 'Toyota',
                'Model': 'Camry',
                'Year': 2022,
                'RegistrationPlate': 'ABC123',
                'Color': 'Blue',
                'Type': 'Sedan',
                'Availability': True
            },
            {
                'VehicleID': 2,
                'Brand': 'Honda',
                'Model': 'Civic',
                'Year': 2021,
                'RegistrationPlate': 'XYZ789',
                'Color': 'Silver',
                'Type': 'Sedan',
                'Availability': True
            }
        ]
        self.vehicle_service.GetAllVehicles = MagicMock(return_value=all_vehicles)
        result = self.vehicle_service.GetAllVehicles()
        self.assertEqual(result, all_vehicles)
    '''
if __name__ == '__main__':
    unittest.main()

