class Ticket:

    purchased_tickets = []
    
    def __init__(self, ticket_type, price, event=None, exhibition=None, tour=None):
        self.ticket_type = ticket_type
        self.price = price
        self.event = event
        self.exhibition = exhibition
        self.tour = tour

    def calculate_price(ticket_type, is_group=False):
        if is_group:
            return 0.5 * 63  # 50% discount for groups
        elif ticket_type in ["CHILD", "STUDENT", "TEACHER", "SENIOR"]:
            return 0  # Free ticket for children, students, teachers, and seniors
        else:
            return 63  # Default price for adults

    def apply_vat(price):
        return price * 1.05  # Apply 5% VAT

    def get_final_price(self, is_group=False):
        price = self.calculate_price(self.ticket_type, is_group)
        return self.apply_vat(price) if price > 0 else 0  # Apply VAT if not a free ticket

    def purchase_ticket(visitor, ticket_type, is_group=False):
        price = Ticket.calculate_price(ticket_type, is_group)
        final_price = Ticket.apply_vat(price) if price > 0 else 0
        new_ticket = Ticket(ticket_type, final_price)
        Ticket.purchased_tickets.append(new_ticket)
        visitor.purchased_items.append(new_ticket)

    def get_all_purchased_tickets():
        return Ticket.purchased_tickets

