from DatabaseConnector import DatabaseConnector
from JobListing import JobListing
from JobApplication import JobApplication
from Applicant import Applicant

db_connector = DatabaseConnector(host ="localhost", database ="careerhub", user ="root", password ="Aniket@123")
db_connector.open_connection()

joblisting_manager=JobListing(db_connector)

#joblisting_manager.retrieve_job_listings()

#joblisting_manager.company_post_job_listing(112,14,"Python Developer","Description for PythonDEveloper position in Chennai","Chennai","300000","Full time")

#joblisting_manager.search_job_listings_by_salary_range(100000,400000)

jobapplication_manager=JobApplication(db_connector)

#jobapplication_manager.apply_for_job(164,104,54,"CoverLetter for Network Administrator position in Bangalore")

applicant_manager =Applicant(db_connector)
#applicant_manager.create_applicant_profile(60,"Aniket","Biyani","anixbiyani11@gmail.com","7020905391","Resume for Aniket Biyani")
#applicant_manager.create_profile(61,"Abhi","Surya","abhisurya@gmail.com",7666756432,"REsume for abhi")
applicant_manager.get_applicants(60)
db_connector.close_connection()