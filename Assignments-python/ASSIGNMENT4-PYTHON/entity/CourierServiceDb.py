from DBConnection import DBConnection

import mysql.connector
from mysql.connector import Error

class CourierServiceDb:
    connection = None

    def __init__(self):
        if CourierServiceDb.connection is None:
            CourierServiceDb.connection = DBConnection.get_connection()
            if CourierServiceDb.connection is None:
                print("Database connection is not established.")

    def insert_order(self, courier_order):
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = "INSERT INTO courier (tracking_number, status) VALUES (%s, %s)"
            data = (courier_order.tracking_number, courier_order.status)
            cursor.execute(query, data)
            CourierServiceDb.connection.commit()
            print("Order inserted successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def update_courier_status(self, tracking_number, new_status):
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = "UPDATE courier_orders SET status = %s WHERE tracking_number = %s"
            data = (new_status, tracking_number)
            cursor.execute(query, data)
            CourierServiceDb.connection.commit()
            print("Courier status updated successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def retrieve_orders(self):
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = "SELECT * FROM courier_orders"
            cursor.execute(query)
            orders = cursor.fetchall()
            return orders
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def retrieve_delivery_history(self, tracking_number):
        try:
            cursor = CourierServiceDb.connection.cursor(dictionary=True)  # Set dictionary=True
            query = "SELECT * FROM delivery_history WHERE tracking_number = %s"
            data = (tracking_number,)
            cursor.execute(query, data)
            delivery_history = cursor.fetchall()
            return delivery_history
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def generate_shipment_status_report(self):
        try:
            cursor = CourierServiceDb.connection.cursor(dictionary=True)
            query = "SELECT trackingnumber, status FROM courier"
            cursor.execute(query)
            shipment_status_report = cursor.fetchall()
            return shipment_status_report
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def generate_revenue_report(self):
        try:
            cursor = CourierServiceDb.connection.cursor(dictionary=True)  # Set dictionary=True
            query = "SELECT SUM(amount) as total_revenue FROM payment"
            cursor.execute(query)
            revenue_report = cursor.fetchone()
            return revenue_report['total_revenue'] if revenue_report and 'total_revenue' in revenue_report else 0
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()


