class InvalidEmailFormat(Exception):
    def __init__(self, message="Invalid email format. Please enter a valid email address."):
        self.message = message
        super().__init__(self.message)

class NegativeSalaryException(Exception):
    def __init__(self, message="Salary cannot be negative. Please enter a valid salary."):
        self.message = message
        super().__init__(self.message)

class FileUploadException(Exception):
    def __init__(self, message="Error during file upload."):
        self.message = message
        super().__init__(self.message)

class DeadlineExceededException(Exception):
    def __init__(self, message="Application deadline has passed. Applications are no longer accepted."):
        self.message = message
        super().__init__(self.message)

class DatabaseConnectionException(Exception):
    def __init__(self, message="Error connecting to the database. Please try again later."):
        self.message = message
        super().__init__(self.message)

