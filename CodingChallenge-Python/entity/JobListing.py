from datetime import datetime
from Exception import NegativeSalaryException
class JobListing:
    def __init__(self, JobID, CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType,PostedDate):
        self._JobID = JobID
        self._CompanyID = CompanyID
        self._JobTitle = JobTitle
        self._JobDescription = JobDescription
        self._JobLocation = JobLocation
        self._Salary = Salary
        self._JobType = JobType
        self._PostedDate =PostedDate

    def __init__(self, db_connector):
        self._db_connector = db_connector
    @property
    def JobID(self):
        return self._JobID

    @JobID.setter
    def JobID(self,new_JobID):
        if isinstance(new_JobID, int) and new_JobID > 0:
            self._JobID = new_JobID
        else:
            raise ValueError("JobID must be a positive integer.")

    @property
    def CompanyID(self):
        return self._CompanyID

    @CompanyID.setter
    def CompanyID(self,new_CompanyID):
        if isinstance(new_CompanyID, int) and new_CompanyID > 0:
            self._CompanyID = new_CompanyID
        else:
            raise ValueError("CompanyID must be a positive integer.")

    @property
    def JobTitle(self):
        return self._JobTitle

    @JobTitle.setter
    def JobTitle(self, new_JobTitle):
        if isinstance(new_JobTitle, str) and len(new_JobTitle) > 0:
            self._JobTitle = new_JobTitle
        else:
            raise ValueError("JobTitle must be a non-empty string.")

    @property
    def JobDescription(self):
        return self._JobDescription

    @JobDescription.setter
    def JobDescription(self, new_JobDescription):
        if isinstance(new_JobDescription, str) and len(new_JobDescription) > 0:
            self._JobDescription = new_JobDescription
        else:
            raise ValueError("JobDescription must be a non-empty string.")

    @property
    def JobLocation(self):
        return self._JobLocation

    @JobLocation.setter
    def JobLocation(self, new_JobLocation):
        if isinstance(new_JobLocation, str) and len(new_JobLocation) > 0:
            self._JobLocation = new_JobLocation
        else:
            raise ValueError("JobLocation must be a non-empty string.")

    @property
    def Salary(self):
        return self._Salary

    @Salary.setter
    def Salary(self, new_Salary):
        if isinstance(new_Salary, float) and new_Salary >= 0:
            self._Salary = new_Salary
        else:
            raise NegativeSalaryException

    @property
    def JobType(self):
        return self._JobType

    @JobType.setter
    def JobType(self, new_JobType):
        if isinstance(new_JobType, str) and len(new_JobType) > 0:
            self._JobType = new_JobType
        else:
            raise ValueError("JobType must be a non-empty string.")

    @property
    def PostedDate(self):
        return self._PostedDate

    @PostedDate.setter
    def PostedDate(self, new_PostedDate):
        if isinstance(new_PostedDate, datetime):
            self._PostedDate =new_PostedDate
        else:
            raise ValueError("PostedDate must be a datetime object.")

    def retrieve_job_listings(self):
        try:
            self._db_connector.open_connection()
            query = "SELECT C.CompanyName,J.JobTitle,J.JobDescription,J.JobLocation,J.Salary,J.JobType FROM companies C JOIN Jobs J on J.CompanyID=C.CompanyID "

            with self._db_connector.connection.cursor() as cursor:
                cursor.execute(query)
                job_listings = cursor.fetchall()
                for job in job_listings:
                     company_name,job_title,job_description,job_location,salary,job_type = job
                     print(f"Company Name: {company_name},Job Title: {job_title},JobDescription :{job_description} , JobLocation:{job_location},Salary: {salary},JobType:{job_type}")

        except Exception as e:
            print(f"Error retrieving job listings: {e}")

        finally:
            self._db_connector.close_connection()

    def company_post_job_listing(self,JobID,CompanyID,JobTitle, JobDescription, JobLocation, Salary, JobType):
        try:
            self._db_connector.open_connection()

            query = "INSERT INTO Jobs (JobID,CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)"
            values = (JobID,CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, datetime.now(),)

            with self._db_connector.connection.cursor() as cursor:
                cursor.execute(query, values)

            self._db_connector.connection.commit()
            print("Job listing posted successfully.")

        except Exception as e:
            print(f"Error posting job listing: {e}")

        finally:
            self._db_connector.close_connection()

    def search_job_listings_by_salary_range(self, min_salary, max_salary):
        try:
            self._db_connector.open_connection()
            query = "SELECT J.JobTitle, C.CompanyName, J.Salary FROM Jobs J JOIN Companies C on J.CompanyID=C.CompanyID WHERE J.Salary BETWEEN %s AND %s"
            values = (min_salary, max_salary)

            with self._db_connector.connection.cursor() as cursor:
                cursor.execute(query, values)
                job_listings = cursor.fetchall()
                for job_title,  company_name, salary in job_listings:
                    print(f"Job Title: {job_title},Company Name: {company_name},Salary :{salary}")

        except Exception as e:
            print(f"Error searching job listings: {e}")

        finally:
            self._db_connector.close_connection()
    def Apply(self, applicant_id, cover_letter):
        #similiar method created in create_applicant_profile in Application.py
       pass


    def GetApplicants(self):
        # similiar method created in get_applicants in Application.py
        pass