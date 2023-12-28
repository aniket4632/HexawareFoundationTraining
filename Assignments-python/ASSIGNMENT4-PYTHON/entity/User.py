class User:
    def __init__(self, UserID, UserName, Email, Password, ContactNumber, Address):
        self._UserID = UserID
        self._UserName = UserName
        self._Email = Email
        self._Password = Password
        self._ContactNumber = ContactNumber
        self._Address = Address

    @property
    def UserID(self):
        return self._UserID

    @UserID.setter
    def UserID(self, new_UserID):
        if not isinstance( new_UserID, int) or  new_UserID <= 0:
            raise  ValueError("User ID must be a positive integer.")
        self._UserID =  new_UserID

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def user_name(self,  new_UserName):
        if not  new_UserName or not isinstance( new_UserName, str):
            raise  ValueError("User name must be a non-empty string.")
        self._UserName =  new_UserName

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self,  new_Email):
        if not isinstance( new_Email, str) or "@" not in  new_Email or "." not in  new_Email:
            raise  ValueError("Invalid email format.")
        self._Email =  new_Email

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self,  new_Password):
        if not isinstance( new_Password, str) or len( new_Password) < 6:
            raise  ValueError("Password must be at least 6 characters long.")
        self._Password =  new_Password

    @property
    def ContactNumber(self):
        return self._ContactNumber

    @ContactNumber.setter
    def ContactNumber(self,  new_ContactNumber):
        if not isinstance( new_ContactNumber, int) or len(str( new_ContactNumber)) != 10:
            raise ValueError("Invalid contact number.")
        self._ContactNumber =  new_ContactNumber
    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self,  new_Address):
        if not  new_Address or not isinstance( new_Address, str):
            raise  ValueError("Address must be a non-empty string.")
        self._Address =  new_Address

