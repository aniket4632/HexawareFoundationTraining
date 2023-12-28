from CourierUserServiceCollectionImpl import CourierUserServiceCollectionImpl

class CourierUserServiceImpl(CourierUserServiceCollectionImpl):
    def __init__(self, company_obj):
        super().__init__(company_obj)

    def place_order(self, courier_obj):
        super().place_order(courier_obj)
        print(f"Order placed successfully. Tracking Number: {courier_obj.get_tracking_number()}")

    def get_order_status(self, tracking_number):
        status = super().get_order_status(tracking_number)
        if status != "Tracking number not found":
            print(f"Order status for tracking number {tracking_number}: {status}")
        else:
            print(f"Order with tracking number {tracking_number} not found.")
        return status

    def cancel_order(self, tracking_number):
        result = super().cancel_order(tracking_number)
        if result:
            print(f"Order with tracking number {tracking_number} canceled successfully.")
        else:
            print(f"Order with tracking number {tracking_number} not found.")
        return result

    def get_assigned_order(self, courier_staff_id):
        assigned_orders = super().get_assigned_order(courier_staff_id)
        if assigned_orders:
            print(f"Orders assigned to courier staff ID {courier_staff_id}: {assigned_orders}")
        else:
            print(f"No orders assigned to courier staff ID {courier_staff_id}.")
        return assigned_orders