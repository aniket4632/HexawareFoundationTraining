class Company:
    def __init__(self, CompanyID, CompanyName, Location):
        self._CompanyID = CompanyID
        self._CompanyName = CompanyName
        self._Location = Location

    def __init__(self, db_connector):
        self._db_connector = db_connector
    @property
    def CompanyID(self):
        return self._CompanyID

    @CompanyID.setter
    def CompanyID(self, new_CompanyID):
        if isinstance(new_CompanyID, int) and new_CompanyID > 0:
            self._CompanyID = new_CompanyID
        else:
            raise ValueError("CompanyID must be a positive integer.")

    @property
    def CompanyName(self):
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, new_CompanyName):
        if isinstance(new_CompanyName, str) and len(new_CompanyName) > 0:
            self._CompanyName = new_CompanyName
        else:
            raise ValueError("CompanyName must be a non-empty string.")

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, new_Location):
        if isinstance(new_Location, str) and len(new_Location) > 0:
            self._Location =  new_Location
        else:
            raise ValueError("Location must be a non-empty string.")
    def Post_job(self):
        #similiar method done in joblisting as company_post_job_listing
        pass


