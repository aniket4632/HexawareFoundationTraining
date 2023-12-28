class Payment:
    def __init__(self, PaymentID, CourierID, Amount, PaymentDate):
        self._PaymentID = PaymentID
        self._CourierID = CourierID
        self._Amount = Amount
        self._PaymentDate = PaymentDate

    @property
    def PaymentID(self):
        return self._PaymentID

    @PaymentID.setter
    def PaymentID(self, new_PaymentID):
        if not isinstance(new_PaymentID, int) or new_PaymentID <= 0:
            raise ValueError("Payment ID must be a positive integer.")
        self._PaymentID = new_PaymentID

    @property
    def CourierID(self):
        return self._CourierID

    @CourierID.setter
    def CourierID(self, new_CourierID):
        if not isinstance(new_CourierID, int) or new_CourierID <= 0:
            raise ValueError("Courier ID must be a positive integer.")
        self._CourierID = new_CourierID

    @property
    def Amount(self):
        return self._Amount

    @Amount.setter
    def Amount(self, new_Amount):
        if not isinstance(new_Amount, (int, float)) or new_Amount < 0:
            raise ValueError("Amount must be a non-negative number.")
        self._Amount = new_Amount

    @property
    def PaymentDate(self):
        return self._PaymentDate

    @PaymentDate.setter
    def PaymentDate(self, new_PaymentDate):
        self._PaymentDate = new_PaymentDate