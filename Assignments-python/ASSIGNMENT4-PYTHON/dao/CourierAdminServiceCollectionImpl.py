from CourierAdminServiceImpl import CourierAdminServiceImpl
from CourierCompanyCollection import CourierCompanyCollection

class CourierAdminServiceCollectionImpl(CourierAdminServiceImpl):
    def __init__(self, company_obj):
        super().__init__(company_obj)

    def assign_order(self, courier_order, courier_staff_id):
        assigned_orders = super().assign_order(courier_order, courier_staff_id)
        if assigned_orders:
            print(f"Order assigned to courier staff ID {courier_staff_id}: {courier_order}")
        else:
            print(f"Failed to assign order to courier staff ID {courier_staff_id}.")

        return assigned_orders

    def update_order_status(self, tracking_number, new_status):
        super().update_order_status(tracking_number, new_status)
        status = super().get_order_status(tracking_number)
        if status == new_status:
            print(f"Order status updated successfully. New status: {new_status}")
        else:
            print(f"Failed to update order status for tracking number {tracking_number}.")

    def view_orders(self):
        orders = super().get_all_orders()
        if orders:
            print(f"All courier orders: {orders}")
        else:
            print("No courier orders available.")

