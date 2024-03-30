from enum import Enum

class TicketType(Enum):
    ADULT = 1
    CHILD = 2
    STUDENT = 3
    TEACHER = 4
    SENIOR = 5

class Visitor:
    def __init__(self, name, age, national_id, ticket_type, purchased_items):
        self.name = name
        self.age = age
        self.national_id = national_id
        self.ticket_type = ticket_type
        self.purchased_items = purchased_items
