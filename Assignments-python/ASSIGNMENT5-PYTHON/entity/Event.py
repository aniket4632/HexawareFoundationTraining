from datetime import date, time

class EventType:
    MOVIE = 'Movie'
    SPORTS = 'Sports'
    CONCERT = 'Concert'

class Event:
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, ticket_price, event_type):
        self._event_name = event_name
        self._event_date = self._validate_date(event_date)
        self._event_time = self._validate_time(event_time)
        self._venue_name = venue_name
        self._total_seats = self._validate_positive_integer(total_seats, "Total seats")
        self._available_seats = self._total_seats
        self._ticket_price = self._validate_decimal(ticket_price, "Ticket price")
        self._event_type = self._validate_event_type(event_type)
        self.booked_tickets = 0

    @property
    def event_name(self):
        return self._event_name

    @event_name.setter
    def event_name(self, new_event_name):
        if not new_event_name or not isinstance(new_event_name, str):
            raise ValueError("Event name must be a non-empty string.")
        self._event_name = new_event_name

    @property
    def event_date(self):
        return self._event_date

    @event_date.setter
    def event_date(self, new_event_date):
        self._event_date = self._validate_date(new_event_date)

    @property
    def event_time(self):
        return self._event_time

    @event_time.setter
    def event_time(self, new_event_time):
        self._event_time = self._validate_time(new_event_time)

    @property
    def venue_name(self):
        return self._venue_name

    @venue_name.setter
    def venue_name(self, new_venue_name):
        if not new_venue_name or not isinstance(new_venue_name, str):
            raise ValueError("Venue name must be a non-empty string.")
        self._venue_name = new_venue_name

    @property
    def total_seats(self):
        return self._total_seats

    @total_seats.setter
    def total_seats(self, new_total_seats):
        self._total_seats = self._validate_positive_integer(new_total_seats, "Total seats")
        self._available_seats = min(self._total_seats, self._available_seats)

    @property
    def available_seats(self):
        return self._available_seats

    @property
    def ticket_price(self):
        return self._ticket_price

    @ticket_price.setter
    def ticket_price(self, new_ticket_price):
        self._ticket_price = self._validate_decimal(new_ticket_price, "Ticket price")

    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, new_event_type):
        self._event_type = self._validate_event_type(new_event_type)

    def _validate_date(self, event_date):
        date_parts = event_date.split('-')

        if len(date_parts) == 3:
            try:
                year, month, day = map(int, date_parts)
                return date(year, month, day)
            except ValueError:
                raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
        else:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

    def _validate_time(self, event_time):
        time_parts = event_time.split(':')

        if len(time_parts) == 2:
            try:
                hour, minute = map(int, time_parts)
                return time(hour, minute)
            except ValueError:
                raise ValueError("Invalid time format. Please use HH:MM.")
        else:
            raise ValueError("Invalid time format. Please use HH:MM.")

    def _validate_positive_integer(self, value, field_name):
        if isinstance(value, int) and value > 0:
            return value
        elif isinstance(value, str) and value.isdigit() and int(value) > 0:
            return int(value)
        else:
            raise ValueError(f"{field_name} must be a positive integer.")
    def _validate_decimal(self, value, field_name):
        try:
            float_value = float(value)
            if float_value >= 0:
                return float_value
            else:
                raise ValueError(f"{field_name} must be a non-negative decimal.")
        except ValueError:
            raise ValueError(f"Invalid {field_name}.")

    def _validate_event_type(self, event_type):
        if event_type in (EventType.MOVIE, EventType.SPORTS, EventType.CONCERT):
            return event_type
        else:
            raise ValueError("Invalid event type. Please choose from 'Movie', 'Sports', or 'Concert'.")


    def calculate_total_revenue(self):
        return self.booked_tickets * self._ticket_price

    def get_booked_no_of_tickets(self):
        return self.booked_tickets

    def book_tickets(self, num_tickets):
        if num_tickets <= self._available_seats:
            self.booked_tickets += num_tickets
            self._available_seats -= num_tickets
            print(f"{num_tickets} tickets booked successfully!")
        else:
            print("Sorry, not enough available seats.")

    def cancel_booking(self, num_tickets):
        if num_tickets <= self.booked_tickets:
            self.booked_tickets -= num_tickets
            self._available_seats += num_tickets
            print(f"{num_tickets} tickets canceled.")
        else:
            print("Invalid number of tickets to cancel.")

    def display_event_details(self):
        print(f"Event: {self._event_name}")
        print(f"Date: {self._event_date}")
        print(f"Time: {self._event_time}")
        print(f"Venue: {self._venue_name}")
        print(f"Total Seats: {self._total_seats}")
        print(f"Available Seats: {self._available_seats}")
        print(f"Ticket Price: ${self._ticket_price}")
        print(f"Event Type: {self._event_type}")
'''
event_date = "2023-12-31"
event_time = "20:00"
my_event = Event("Concert Night", event_date, event_time, "Music Hall", 1000, 50.0, EventType.CONCERT)

my_event.display_event_details()
my_event.book_tickets(5)
my_event.display_event_details()
my_event.cancel_booking(2)
my_event.display_event_details()
'''
