

class CourierUserServiceCollectionImpl:
    def __init__(self, company_obj):
        self.company_obj = company_obj

    def place_order(self, courier_obj):
        self.company_obj.get_courier_details().append(courier_obj)


    def get_order_status(self, tracking_number):
        for courier in self.company_obj.get_courier_details():
            if courier.get_tracking_number() == tracking_number:
                return courier.get_status()
        return "Tracking number not found"

    def cancel_order(self, tracking_number):
        courier_details = self.company_obj.get_courier_details()
        for courier in courier_details:
            if courier.get_tracking_number() == tracking_number:
                courier_details.remove(courier)
                return True
        return False

    def get_assigned_order(self, courier_staff_id):
        return None
