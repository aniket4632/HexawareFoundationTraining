from CourierUserServiceImpl import CourierUserServiceImpl
from Courier import Courier

class CourierAdminServiceImpl(CourierUserServiceImpl):
    def __init__(self, company_obj):
        super().__init__(company_obj)

    def assign_order(self, courier_order, courier_staff_id):

        assigned_orders = super().get_assigned_order(courier_staff_id)
        if not assigned_orders:
            assigned_orders = []
        assigned_orders.append(courier_order)
        print(f"Order assigned to courier staff ID {courier_staff_id}: {courier_order}")

        return assigned_orders

    def update_order_status(self, tracking_number, new_status):
        status = super().get_order_status(tracking_number)
        if status != "Tracking number not found":
            print(f"Updating order status for tracking number {tracking_number} to {new_status}")
        else:
            print(f"Order with tracking number {tracking_number} not found.")

    def view_orders(self):
        orders = super().get_all_orders()
        if orders:
            print(f"All courier orders: {orders}")
        else:
            print("No courier orders available.")
