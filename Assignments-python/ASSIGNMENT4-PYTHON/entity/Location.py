class Location:
    def __init__(self, LocationID, LocationName, Address):
        self._LocationID = LocationID
        self._LocationName = LocationName
        self._Address = Address

    @property
    def LocationID(self):
        return self._LocationID

    @LocationID.setter
    def LocationID(self, new_LocationID):
        if not isinstance(new_LocationID, int) or new_LocationID <= 0:
            raise ValueError("Location ID must be a positive integer.")
        self._LocationID = new_LocationID

    @property
    def LocationName(self):
        return self._LocationName

    @LocationName.setter
    def LocationName(self, new_LocationName):
        if not new_LocationName or not isinstance(new_LocationName, str):
            raise ValueError("Location name must be a non-empty string.")
        self._LocationName = new_LocationName

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, new_Address):
        if not new_Address or not isinstance(new_Address, str):
            raise ValueError("Address must be a non-empty string.")
        self._Address = new_Address