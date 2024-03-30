class Event:

    events = []
    
    def __init__(self, name, location, start_date, end_date, ticket_price):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.ticket_price = ticket_price
        Event.events.append(self)

    def get_all_events():
        return Event.events
