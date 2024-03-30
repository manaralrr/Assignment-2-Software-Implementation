# Assignment-2-Software-Implementation
## Introduction
The Louvre Museum's software application aims to revolutionize visitor experiences and streamline internal operations. By integrating advanced features such as comprehensive artwork management, dynamic visitor management, and flexible ticketing options, the application seeks to enhance accessibility and engagement. Through meticulous curation of detailed artwork catalogues and seamless ticket purchasing processes, visitors can enjoy a personalized and immersive museum experience. Moreover, the system's ability to manage exhibitions, tours, and special events ensures efficient operation and resource utilization. Overall, the software promises to elevate the Louvre Museum's status as a cultural beacon while optimizing its daily functioning.

## UML Class Diagram
![Untitled Diagram drawio-10](https://github.com/manaralrr/Assignment-2-Software-Implementation/assets/160352954/2b96bc02-c38a-485c-8777-2bef65b8208a)
## Class Descriptions
### 1.	Artwork Class
Attributes: 
•	title: The title of the artwork.
•	artist: The name of the artist who created the artwork.
•	date_of_creation: The year when the artwork was created.
•	historical_significance: A brief description of the historical significance of the artwork.
•	location: The location of the artwork within the museum (e.g., permanent gallery, exhibition hall, outdoor space).
Behaviour: The class provides a method to retrieve all artworks currently in the museum's collection.
Purpose: Manages information about the museum's artworks, facilitating cataloguing and retrieval

### 2.	Exhibition Class
Attributes: 
•	name: The name of the exhibition.
•	location: The location of the exhibition within the museum.
•	start_date: The start date of the exhibition.
•	end_date: The end date of the exhibition.
Behaviour: The class provides a method to retrieve all exhibitions currently open or scheduled at the museum.
Purpose: Manages information about museum exhibitions, enabling tracking and promotion of current and upcoming exhibitions.

### 3.	Visitor Class
Attributes: 
•	name: The name of the visitor.
•	age: The age of the visitor.
•	national_id: The national identification number of the visitor.
•	ticket_type: The type of ticket purchased by the visitor (e.g., adult, child, student, senior).
•	purchased_items: A list of tickets purchased by the visitor.
Behaviour: The class provides a method to display a payment receipt for all tickets purchased by the visitor.
Purpose: Manages information about museum visitors, including ticket purchases and demographic data.

### 4.	Ticket Class
Attributes: 
•	ticket_type: The type of ticket (e.g., adult, child, student, senior).
•	price: The price of the ticket.
•	event: The event associated with the ticket (if applicable).
•	exhibition: The exhibition associated with the ticket (if applicable).
•	tour: The tour associated with the ticket (if applicable).
Behaviour: The class provides methods to calculate the ticket price based on the visitor's type and to apply VAT (value-added tax) to the ticket price.
Purpose: Manages information about tickets purchased by visitors, including pricing and associated events or exhibitions.

### 5.	Event Class
Attributes: 
•	name: The name of the event.
•	location: The location of the event within the museum.
•	start_date: The start date of the event.
•	end_date: The end date of the event.
•	ticket_price: The price of a ticket for the event.
Behaviour: The class provides a method to retrieve all events currently scheduled at the museum.
Purpose: Manages information about museum events, enabling promotion and ticket sales for special events.

### 6.	Tour Class
Attributes: 
•	date: The date of the tour.
•	guide: The guide leading the tour.
•	visitor_group: The group of visitors participating in the tour.
•	exhibition: The exhibition associated with the tour.
Behaviour: None specified in the initial description.
Purpose: Represents a guided tour offered by the museum, linking visitors with exhibitions and guides.

## Relationships
•	Artwork-Exhibition Relationship: An exhibition can feature multiple artworks, and an artwork can be part of multiple exhibitions. This is represented by a many-to-many association between Artwork and Exhibition using an association class Exhibition Artwork.
•	Ticket-Visitor Relationship: A visitor can purchase multiple tickets, and each ticket is associated with one visitor. This is represented by a one-to-many association between Ticket and Visitor.
•	Ticket-Event Relationship: A ticket is associated with either an event, an exhibition, or a tour. This is represented by three separate associations with multiplicity 0...1 between Ticket and Event, Ticket and Exhibition, and Ticket and Tour.
•	Ticket Pricing Logic: The pricing logic is not explicitly modelled, but it is assumed that the Ticket class will have methods to calculate the price based on the visitor's age, ticket type, and any discounts applicable.

## Learnings
This project offers a profound learning experience in software development for museums and cultural institutions. It requires understanding complex requirements, such as managing artwork catalogues, organizing exhibitions, and handling visitor interactions. Implementing these features demands a deep dive into object-oriented programming principles, database management, and user interface design. Additionally, this project fosters insights into the nuances of cultural heritage management, emphasizing the importance of accurate documentation and accessibility. Moreover, it underscores the significance of user experience in enhancing visitor engagement and satisfaction. Overall, this project provides a holistic learning journey, encompassing technical skills, domain knowledge, and a user-centric approach to software development.
