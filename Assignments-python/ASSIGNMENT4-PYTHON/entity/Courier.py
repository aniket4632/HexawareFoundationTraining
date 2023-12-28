class Courier:
    def __init__(self, CourierID, SenderName, SenderAddress, ReceiverName, ReceiverAddress,
                 Weight, Status, TrackingNumber, DeliveryDate, UserID):
        self._CourierID = CourierID
        self._SenderName = SenderName
        self._SenderAddress = SenderAddress
        self._ReceiverName = ReceiverName
        self._ReceiverAddress = ReceiverAddress
        self._Weight = Weight
        self._Status = Status
        self._TrackingNumber = TrackingNumber
        self._DeliveryDate = DeliveryDate
        self._UserID = UserID

    @property
    def CourierID(self):
        return self._CourierID

    @CourierID.setter
    def CourierID(self, new_CourierID):
        if not isinstance(new_CourierID, int) or new_CourierID <= 0:
            raise ValueError("Courier ID must be a positive integer.")
        self._CourierID = new_CourierID

    @property
    def SenderName(self):
        return self._SenderName

    @SenderName.setter
    def SenderName(self, new_SenderName):
        if not new_SenderName or not isinstance(new_SenderName, str):
            raise ValueError("Sender name must be a non-empty string.")
        self._SenderName = new_SenderName

    @property
    def SenderAddress(self):
        return self._SenderAddress

    @SenderAddress.setter
    def SenderAddress(self, new_SenderAddress):
        if not new_SenderAddress or not isinstance(new_SenderAddress, str):
            raise ValueError("Sender address must be a non-empty string.")
        self._SenderAddress = new_SenderAddress

    @property
    def ReceiverName(self):
        return self._ReceiverName

    @ReceiverName.setter
    def ReceiverName(self, new_ReceiverName):
        if not new_ReceiverName or not isinstance(new_ReceiverName, str):
            raise ValueError("Receiver name must be a non-empty string.")
        self._ReceiverName = new_ReceiverName

    @property
    def ReceiverAddress(self):
        return self._ReceiverAddress

    @ReceiverAddress.setter
    def ReceiverAddress(self, new_ReceiverAddress):
        if not new_ReceiverAddress or not isinstance(new_ReceiverAddress, str):
            raise ValueError("Receiver address must be a non-empty string.")
        self._ReceiverAddress = new_ReceiverAddress

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, new_Weight):
        if not isinstance(new_Weight, (int, float)) or new_Weight <= 0:
            raise ValueError("Weight must be a positive number.")
        self._Weight = new_Weight

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, new_Status):
        self._Status = new_Status

    @property
    def TrackingNumber(self):
        return self._TrackingNumber

    @TrackingNumber.setter
    def TrackingNumber(self, new_TrackingNumber):
        if not new_TrackingNumber or not isinstance(new_TrackingNumber, str):
            raise ValueError("Tracking number must be a non-empty string.")
        self._TrackingNumber = new_TrackingNumber

    @property
    def DeliveryDate(self):
        return self._DeliveryDate

    @DeliveryDate.setter
    def DeliveryDate(self, new_DeliveryDate):
        self._DeliveryDate = new_DeliveryDate

    @property
    def UserID(self):
        return self._UserID

    @UserID.setter
    def UserID(self, new_UserID):
        if not isinstance(new_UserID, int) or new_UserID <= 0:
            raise ValueError("User ID must be a positive integer.")
        self._UserID = new_UserID