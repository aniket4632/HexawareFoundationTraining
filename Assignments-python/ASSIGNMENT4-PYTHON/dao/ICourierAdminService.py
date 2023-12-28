from abc import ABC, abstractmethod

class ICourierAdminService(ABC):
    @abstractmethod
    def assignOrder(self, courierOrder, courierStaffId):
        pass

    @abstractmethod
    def updateOrderStatus(self, trackingNumber, newStatus):
        pass

    @abstractmethod
    def viewOrders(self):
        pass
