from artwork import Artwork, Location
from exhibition import Exhibition
from visitor import Visitor, TicketType
from ticket import Ticket
from event import Event
from tour import Tour


# Create a new artwork
new_artwork = Artwork("New Artwork Title", "New Artist", 2024, "Description", Location.PERMANENT_GALLERY)

# Get all artworks in the museum
all_artworks = Artwork.get_all_artworks()
for artwork in all_artworks:
    print(artwork.title)


# Create a new exhibition
new_exhibition = Exhibition("New Exhibition Name", "Exhibition Hall", "2024-04-01", "2024-06-30")

# Create a new event
new_event = Event("New Event Name", "Event Location", "2024-04-15", "2024-04-30", 50)

# Get all exhibitions and events in the museum
all_exhibitions = Exhibition.get_all_exhibitions()
all_events = Event.get_all_events()
for exhibition in all_exhibitions:
    print(exhibition.name)
for event in all_events:
    print(event.name)


# Create a visitor
visitor = Visitor("John Doe", 30, "12345", TicketType.ADULT, [])

# Purchase a ticket for an event
Ticket.purchase_ticket(visitor, TicketType.ADULT)

# Get all purchased tickets
all_purchased_tickets = Ticket.get_all_purchased_tickets()
for ticket in all_purchased_tickets:
    print(f"Visitor: {visitor.name}, Ticket Type: {ticket.ticket_type}, Price: {ticket.price}")


# Create a visitor
visitor = Visitor("John Doe", 30, "12345", TicketType.ADULT, [])

# Purchase tickets
Ticket.purchase_ticket(visitor, TicketType.ADULT)
Ticket.purchase_ticket(visitor, TicketType.STUDENT)

# Display payment receipt
receipt = visitor.display_payment_receipt()
print(receipt)
