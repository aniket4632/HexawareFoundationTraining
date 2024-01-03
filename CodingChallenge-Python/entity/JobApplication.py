from datetime import datetime

class JobApplication:
    def __init__(self, ApplicationID, JobID, ApplicantID, ApplicationDate, CoverLetter):
        self._ApplicationID = ApplicationID
        self._JobID = JobID
        self._ApplicantID = ApplicantID
        self._ApplicationDate = ApplicationDate
        self._CoverLetter = CoverLetter

    def __init__(self, db_connector):
        self._db_connector = db_connector
    @property
    def ApplicationID(self):
        return self._ApplicationID

    @ApplicationID.setter
    def ApplicationID(self, new_ApplicationID):
        if isinstance(new_ApplicationID, int) and new_ApplicationID > 0:
            self._ApplicationID = new_ApplicationID
        else:
            raise ValueError("ApplicationID must be a positive integer.")

    @property
    def JobID(self):
        return self._JobID

    @JobID.setter
    def JobID(self, new_JobID):
        if isinstance(new_JobID, int) and new_JobID > 0:
            self._JobID = new_JobID
        else:
            raise ValueError("JobID must be a positive integer.")

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
    def ApplicationDate(self):
        return self._ApplicationDate

    @ApplicationDate.setter
    def ApplicationDate(self, new_ApplicationDate):

        if isinstance(new_ApplicationDate, datetime):
            self._ApplicationDate = new_ApplicationDate
        else:
            raise ValueError("Invalid datetime format.")

    @property
    def CoverLetter(self):
        return self._CoverLetter

    @CoverLetter.setter
    def CoverLetter(self, new_CoverLetter):
        if isinstance(new_CoverLetter, str) and len(new_CoverLetter) > 0:
            self._CoverLetter = new_CoverLetter
        else:
            raise ValueError("CoverLetter must be a non-empty string.")

    def apply_for_job(self,ApplicationID, JobID, ApplicantID, CoverLetter):
        try:
            self._db_connector.open_connection()
            ApplicationDate = datetime.now()


            query = "INSERT INTO Applications (ApplicationID, JobID,ApplicantID,ApplicationDate, CoverLetter) VALUES (%s, %s, %s, %s,%s)"
            values = (ApplicationID, JobID, ApplicantID, ApplicationDate, CoverLetter)

            with self._db_connector.connection.cursor() as cursor:
                cursor.execute(query, values)

            self._db_connector.connection.commit()
            print("Application submitted successfully.")

        except Exception as e:
            print(f"Error applying for the job: {e}")

        finally:
            self._db_connector.close_connection()
