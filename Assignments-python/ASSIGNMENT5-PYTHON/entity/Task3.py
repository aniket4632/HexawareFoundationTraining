def calculate_ticket_cost(ticket_type, no_of_tickets):
    base_price = 0
    if ticket_type == "Silver":
        base_price = 50
    elif ticket_type == "Gold":
        base_price = 100
    elif ticket_type == "Diamond":
        base_price = 150
    else:
        return "Invalid ticket type. Please choose from 'Silver', 'Gold', or 'Diamond'."

    total_cost = base_price * no_of_tickets
    return f"Total cost for {no_of_tickets} {ticket_type} tickets: ${total_cost}"
def main():

    print("Ticket Options: Silver, Gold, Diamond")

    while True:
        ticket_type = input("Enter the ticket type (type 'Exit' to exit): ")
        if ticket_type.lower() == "exit":
            print("Exiting the ticket booking system. Goodbye!")
            break

        no_of_tickets = int(input("Enter the number of tickets needed: "))
        result = calculate_ticket_cost(ticket_type, no_of_tickets)
        print(result)
if __name__=="__main__":
    main()
