from DatabaseConnector import DatabaseConnector
from  Customers import Customers
from Products import Products
from Orders import Orders
from OrderDetails import OrderDetails
from Inventory import Inventory

db_connector = DatabaseConnector(host ="localhost", database ="TechShop", user ="root", password ="Aniket@123")
db_connector.open_connection()
customers_manager= Customers(db_connector)


#customers_manager.create_customer("115","Sudarshan","Biyani", "sudabiyani@gmail.com", "123458759","Latur")

#customers_manager1.update_customer_Info("114", "sidhhant12@gmail.com", "123458907", "Vadgoan,Pune")

#customers_manager2.get_Customer_Details(112)

#customers_manager3.calculate_Total_Orders(102)

products_manager1=Products(db_connector)

#products_manager.get_product_details(1)

#products_manager1.update_Product_Info("11","Dolby 5.2.0 atmos ",2500)

#products_manager2.is_Product_InStock(1)
orders_manager2=Orders(db_connector)

#orders_manager.get_Order_Details(1001)
#orders_manager1.Calculate_Total_Amount(1001)
#orders_manager2.place_order(1015,2015,102,2,2)

orderdetails_manager1=OrderDetails(db_connector)
#orderdetails_manager.get_OrderDetail_Info(2001)
#orderdetails_manager1.update_Quantity(2001,3)
#orderdetails_manager2.Calculate_Subtotal(2001)

inventory_manager=Inventory(db_connector)
#inventory_manager.Get_Product(301)

#inventory_manager1.get_QuantityInStock(301)

#inventory_manager2.add_To_Inventory(20,301)

#inventory_manager3.remove_From_Inventory(20,301)

#inventory_manager4.update_Stock_Quantity(20,301)

#inventory_manager5.Is_Product_Available(20,301)

#inventory_manager6.Get_InventoryValue()

#inventory_manager7.List_LowStock_Products(10)

#inventory_manager8.List_OutOf_StockProducts()

#inventory_manager9.List_All_Products()

db_connector.close_connection()