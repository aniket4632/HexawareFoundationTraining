class CourierCompanyCollection:
    def __init__(self, companyName):
        self.companyName = companyName
        self.courierDetails = []
        self.employeeDetails = []
        self.locationDetails = []

    

    def get_courier_details(self):
        return self.courierDetails

    def get_employee_details(self):
        return self.employeeDetails

    def get_location_details(self):
        return self.locationDetails
