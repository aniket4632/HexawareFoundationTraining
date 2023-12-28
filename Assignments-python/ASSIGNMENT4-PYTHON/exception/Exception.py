class TrackingNumberNotFoundException(Exception):
    def __init__(self, message="TrackingNumber Not Found."):
        self.message = message
        super().__init__(self.message)

class InvalidEmployeeIdException(Exception):
    def __init__(self, message="Invalid EmployeeId."):
        self.message = message
        super().__init__(self.message)

