class Ticket:
    def __init__(self, ticket_type, price, event=None, exhibition=None, tour=None):
        self.ticket_type = ticket_type
        self.price = price
        self.event = event
        self.exhibition = exhibition
        self.tour = tour
