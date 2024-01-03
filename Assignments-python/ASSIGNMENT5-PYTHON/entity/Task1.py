def book_tickets(available_tickets, no_of_booking_tickets):
    if available_tickets >= no_of_booking_tickets:
        remaining_tickets = available_tickets - no_of_booking_tickets
        return f"Tickets booked successfully! Remaining tickets: {remaining_tickets}"
    else:
        return "Sorry, not enough tickets available. Ticket booking unsuccessful."

def main():
    available_tickets = int(input("Enter the number of available tickets: "))
    no_of_booking_tickets = int(input("Enter the number of tickets to book: "))

    result = book_tickets(available_tickets, no_of_booking_tickets)
    print(result)

if __name__== "__main__":
    main()
