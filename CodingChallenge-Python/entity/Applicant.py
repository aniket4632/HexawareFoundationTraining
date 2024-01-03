from Exception import InvalidEmailFormat
class Applicant:
    def __init__(self, ApplicantID, FirstName, LastName, Email, Phone, Resume):
        self._ApplicantID = ApplicantID
        self._FirstName = FirstName
        self._LastName = LastName
        self._Email = Email
        self._Phone = Phone
        self._Resume = Resume

    def __init__(self, db_connector):
        self._db_connector = db_connector
    @property
    def ApplicantID(self):
        return self._ApplicantID

    @ApplicantID.setter
    def ApplicantID(self, new_ApplicantID):
        if isinstance(new_ApplicantID, int) and new_ApplicantID > 0:
            self._ApplicantID = new_ApplicantID
        else:
            raise ValueError("ApplicantID must be a positive integer.")

    @property
    def FirstName(self):
        return self._FirstName

    @FirstName.setter
    def FirstName(self, new_FirstName):
        if isinstance(new_FirstName, str) and len(new_FirstName) > 0:
            self._FirstName = new_FirstName
        else:
            raise ValueError("FirstName must be a non-empty string.")

    @property
    def LastName(self):
        return self._LastName

    @LastName.setter
    def LastName(self, new_LastName):
        if isinstance( new_LastName, str) and len( new_LastName) > 0:
            self._LastName = new_LastName
        else:
            raise ValueError("LastName must be a non-empty string.")

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, new_Email):
        if "@" in new_Email and "." in new_Email:
            self._Email = new_Email
        else:
            raise InvalidEmailFormat
    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, new_Phone):
        if len(new_Phone) == 10 and new_Phone.isdigit():
            self._Phone = new_Phone
        else:
            raise ValueError("Invalid phone number format.")

    @property
    def Resume(self):
        return self._Resume

    @Resume.setter
    def Resume(self, new_Resume):
        self._Resume=new_Resume

    def create_applicant_profile(self, ApplicantID, FirstName, LastName, Email, Phone, Resume):
        try:
            self._db_connector.open_connection()

            query = "INSERT INTO Applicants (ApplicantID, FirstName, LastName, Email, Phone, Resume) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (ApplicantID, FirstName, LastName, Email, Phone, Resume)

            with self._db_connector.connection.cursor() as cursor:
                cursor.execute(query, values)

            self._db_connector.connection.commit()
            print("Applicant profile created successfully.")

        except Exception as e:
            print(f"Error creating applicant profile: {e}")

        finally:
            self._db_connector.close_connection()

    def create_profile(self, ApplicantID, FirstName, LastName, Email, Phone, Resume):
        try:
            self._db_connector.open_connection()

            query = "INSERT INTO Applicants (ApplicantID, FirstName, LastName, Email, Phone, Resume) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (ApplicantID, FirstName, LastName, Email, Phone, Resume)

            with self._db_connector.connection.cursor() as cursor:
                cursor.execute(query, values)

            self._db_connector.connection.commit()
            print("Applicant profile created successfully.")

        except Exception as e:
            print(f"Error creating applicant profile: {e}")

        finally:
            self._db_connector.close_connection()
    def get_applicants(self,ApplicantID):
        try:
            self._db_connector.open_connection()
            query = "SELECT * FROM Applicants where ApplicantID=%s "
            values=(ApplicantID,)
            self._db_connector.cursor.execute(query, values)
            applicants_details = self._db_connector.cursor.fetchone()

            if applicants_details:
                print("Order Details:")
                print(f"Applicant ID:{applicants_details[0]}")
                print(f"FirstName:{applicants_details[1]}")
                print(f"Last Name: {applicants_details[2]}")
                print(f"Email: {applicants_details[3]}")
                print(f"Phone: {applicants_details[4]}")
                print(f"Resume: {applicants_details[5]}")

            else:
                print("Applicant Id not found.")

        except Exception as e:
            print(f"Error getting Applicant details: {e}")

        finally:
            self._db_connector.close_connection()

    def applyfor_job(self):
        # apply for job method is created in job application as it is similar to database tasks
     pass