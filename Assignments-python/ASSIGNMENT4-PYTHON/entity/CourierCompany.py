class CourierCompany:
    def __init__(self, CompanyName, CourierDetails=None, EmployeeDetails=None, LocationDetails=None):
        self._CompanyName = CompanyName
        self._CourierDetails = CourierDetails or []
        self._EmployeeDetails = EmployeeDetails or []
        self._LocationDetails = LocationDetails or []

    @property
    def CompanyName(self):
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, new_CompanyName):
        if not new_CompanyName or not isinstance(new_CompanyName, str):
            raise ValueError("Company name must be a non-empty string.")
        self._CompanyName = new_CompanyName

    @property
    def CourierDetails(self):
        return self._CourierDetails

    @CourierDetails.setter
    def CourierDetails(self, new_CourierDetails):
        # Add additional validation for CourierDetails if needed
        self._CourierDetails = new_CourierDetails

    @property
    def EmployeeDetails(self):
        return self._EmployeeDetails

    @EmployeeDetails.setter
    def EmployeeDetails(self, new_EmployeeDetails):
        # Add additional validation for EmployeeDetails if needed
        self._EmployeeDetails = new_EmployeeDetails

    @property
    def LocationDetails(self):
        return self._LocationDetails

    @LocationDetails.setter
    def LocationDetails(self, new_LocationDetails):
        # Add additional validation for LocationDetails if needed
        self._LocationDetails = new_LocationDetails