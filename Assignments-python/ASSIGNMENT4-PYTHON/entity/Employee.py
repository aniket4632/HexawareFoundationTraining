class Employee:
    def __init__(self, EmployeeID, EmployeeName, Email, ContactNumber, Role, Salary):
        self._EmployeeID = EmployeeID
        self._EmployeeName = EmployeeName
        self._Email = Email
        self._ContactNumber = ContactNumber
        self._Role = Role
        self._Salary = Salary

    @property
    def EmployeeID(self):
        return self._EmployeeID

    @EmployeeID.setter
    def EmployeeID(self, new_EmployeeID):
        if not isinstance(new_EmployeeID, int) or new_EmployeeID <= 0:
            raise ValueError("Employee ID must be a positive integer.")
        self._EmployeeID = new_EmployeeID

    @property
    def EmployeeName(self):
        return self._EmployeeName

    @EmployeeName.setter
    def EmployeeName(self, new_EmployeeName):
        if not new_EmployeeName or not isinstance(new_EmployeeName, str):
            raise ValueError("Employee name must be a non-empty string.")
        self._EmployeeName = new_EmployeeName

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, new_Email):
        # Add Email format validation if needed
        if not new_Email or not isinstance(new_Email, str):
            raise ValueError("Email must be a non-empty string.")
        self._Email = new_Email

    @property
    def ContactNumber(self):
        return self._ContactNumber

    @ContactNumber.setter
    def ContactNumber(self, new_ContactNumber):
        if not isinstance(new_ContactNumber, int) or len(str(new_ContactNumber)) != 10:
            raise ValueError("Invalid contact number.")
        self._ContactNumber = new_ContactNumber

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, new_Role):
        if not new_Role or not isinstance(new_Role, str):
            raise ValueError("Role must be a non-empty string.")
        self._Role = new_Role

    @property
    def Salary(self):
        return self._Salary

    @Salary.setter
    def Salary(self, new_Salary):
        if not isinstance(new_Salary, (int, float)) or new_Salary < 0:
            raise ValueError("Salary must be a non-negative number.")
        self._Salary = new_Salary