from .ICustomerService import ICustomerService
from CaseStudy_01.exception.Exception import CustomerNotFoundException


class CustomerService(ICustomerService):
    def __init__(self, db_conn_util, connection_string):
        self._db_conn_util = db_conn_util
        self._connection_string = connection_string

    def GetCustomerById(self, customer_id):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM Customer WHERE CustomerID = %s", (customer_id,))
            customer_data = cursor.fetchone()

            if customer_data:
                return customer_data
            else:
                raise CustomerNotFoundException(f"Customer with ID {customer_id} not found.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()

    def GetCustomerByUsername(self, username):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("SELECT CustomerID, Password FROM Customer WHERE Username = %s", (username,))
            customer_data1 = cursor.fetchone()

            if customer_data1:
                customer_dict = {
                    'CustomerID': customer_data1[0],
                    'Password': customer_data1[1]
                }
                return customer_dict
            else:
                raise CustomerNotFoundException(f"Customer with FirstName {username} not found.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()

    def RegisterCustomer(self, customer_data):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO Customer (FirstName, LastName, Email, PhoneNumber, Address, Username,
                 Password, RegistrationDate)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                customer_data['first_name'],
                customer_data['last_name'],
                customer_data['email'],
                customer_data['phone_number'],
                customer_data['address'],
                customer_data['username'],
                customer_data['password'],
                customer_data['registration_date']
            ))

            connection.commit()
            print("Customer registered successfully.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()

    def UpdateCustomer(self, customer_data):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE Customer
                SET FirstName = %s, LastName = %s, Email = %s, PhoneNumber = %s, Address = %s, 
                Username = %s, Password = %s
                WHERE CustomerID = %s
            """, (
                customer_data['first_name'],
                customer_data['last_name'],
                customer_data['email'],
                customer_data['phone_number'],
                customer_data['address'],
                customer_data['username'],
                customer_data['password'],
                customer_data['customer_id']
            ))

            connection.commit()
            print("Customer updated successfully.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()

    def DeleteCustomer(self, customer_id):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("DELETE FROM Customer WHERE CustomerID = %s", (customer_id,))

            connection.commit()
            print(f"Customer with ID {customer_id} deleted successfully.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()
