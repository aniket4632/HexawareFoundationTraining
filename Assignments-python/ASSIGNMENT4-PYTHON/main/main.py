from CourierServiceDb import CourierServiceDb


tracking_number = "TN111111"


delivery_history = CourierServiceDb().retrieve_delivery_history(tracking_number)
print(f"Delivery History for Tracking Number {tracking_number}: {delivery_history}")

shipment_status_report = CourierServiceDb().generate_shipment_status_report()
print("Shipment Status Report:")
for order in shipment_status_report:
    print(f"Tracking Number: {order['trackingnumber']}, Status: {order['status']}")

total_revenue = CourierServiceDb().generate_revenue_report()
print(f"Total Revenue: {total_revenue}")


