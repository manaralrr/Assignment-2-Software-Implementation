# Assignment-2-Software-Implementation
## Introduction
The Louvre Museum's software application aims to revolutionize visitor experiences and streamline internal operations. By integrating advanced features such as comprehensive artwork management, dynamic visitor management, and flexible ticketing options, the application seeks to enhance accessibility and engagement. Through meticulous curation of detailed artwork catalogues and seamless ticket purchasing processes, visitors can enjoy a personalized and immersive museum experience. Moreover, the system's ability to manage exhibitions, tours, and special events ensures efficient operation and resource utilization. Overall, the software promises to elevate the Louvre Museum's status as a cultural beacon while optimizing its daily functioning.

## UML Class Diagram
![Untitled Diagram drawio-10](https://github.com/manaralrr/Assignment-2-Software-Implementation/assets/160352954/2b96bc02-c38a-485c-8777-2bef65b8208a)
## Class Descriptions
### 1.	Artwork Class
Attributes: <br>
•	title: The title of the artwork.<br>
•	artist: The name of the artist who created the artwork.<br>
•	date_of_creation: The year when the artwork was created.<br>
•	historical_significance: A brief description of the historical significance of the artwork.<br>
•	location: The location of the artwork within the museum (e.g., permanent gallery, exhibition hall, outdoor space).<br>
Behaviour: The class provides a method to retrieve all artworks currently in the museum's collection.<br>
Purpose: Manages information about the museum's artworks, facilitating cataloguing and retrieval

### 2.	Exhibition Class
Attributes: <br>
•	name: The name of the exhibition.<br>
•	location: The location of the exhibition within the museum.<br>
•	start_date: The start date of the exhibition.<br>
•	end_date: The end date of the exhibition.<br>
Behaviour: The class provides a method to retrieve all exhibitions currently open or scheduled at the museum.<br>
Purpose: Manages information about museum exhibitions, enabling tracking and promotion of current and upcoming exhibitions.

### 3.	Visitor Class
Attributes: <br>
•	name: The name of the visitor.<br>
•	age: The age of the visitor.<br>
•	national_id: The national identification number of the visitor.<br>
•	ticket_type: The type of ticket purchased by the visitor (e.g., adult, child, student, senior).<br>
•	purchased_items: A list of tickets purchased by the visitor.<br>
Behaviour: The class provides a method to display a payment receipt for all tickets purchased by the visitor.<br>
Purpose: Manages information about museum visitors, including ticket purchases and demographic data.

### 4.	Ticket Class
Attributes: <br>
•	ticket_type: The type of ticket (e.g., adult, child, student, senior).<br>
•	price: The price of the ticket.<br>
•	event: The event associated with the ticket (if applicable).<br>
•	exhibition: The exhibition associated with the ticket (if applicable).<br>
•	tour: The tour associated with the ticket (if applicable).<br>
Behaviour: The class provides methods to calculate the ticket price based on the visitor's type and to apply VAT (value-added tax) to the ticket price.<br>
Purpose: Manages information about tickets purchased by visitors, including pricing and associated events or exhibitions.

### 5.	Event Class
Attributes: <br>
•	name: The name of the event.<br>
•	location: The location of the event within the museum.<br>
•	start_date: The start date of the event.<br>
•	end_date: The end date of the event.<br>
•	ticket_price: The price of a ticket for the event.<br>
Behaviour: The class provides a method to retrieve all events currently scheduled at the museum.<br>
Purpose: Manages information about museum events, enabling promotion and ticket sales for special events.

### 6.	Tour Class
Attributes: <br>
•	date: The date of the tour.<br>
•	guide: The guide leading the tour.<br>
•	visitor_group: The group of visitors participating in the tour.<br>
•	exhibition: The exhibition associated with the tour.<br>
Behaviour: None specified in the initial description.<br>
Purpose: Represents a guided tour offered by the museum, linking visitors with exhibitions and guides.

## Relationships
•	Artwork-Exhibition Relationship: An exhibition can feature multiple artworks, and an artwork can be part of multiple exhibitions. This is represented by a many-to-many association between Artwork and Exhibition using an association class Exhibition Artwork.<br>
•	Ticket-Visitor Relationship: A visitor can purchase multiple tickets, and each ticket is associated with one visitor. This is represented by a one-to-many association between Ticket and Visitor.<br>
•	Ticket-Event Relationship: A ticket is associated with either an event, an exhibition, or a tour. This is represented by three separate associations with multiplicity 0...1 between Ticket and Event, Ticket and Exhibition, and Ticket and Tour.<br>
•	Ticket Pricing Logic: The pricing logic is not explicitly modelled, but it is assumed that the Ticket class will have methods to calculate the price based on the visitor's age, ticket type, and any discounts applicable.

## Learnings
This project offers a profound learning experience in software development for museums and cultural institutions. It requires understanding complex requirements, such as managing artwork catalogues, organizing exhibitions, and handling visitor interactions. Implementing these features demands a deep dive into object-oriented programming principles, database management, and user interface design. Additionally, this project fosters insights into the nuances of cultural heritage management, emphasizing the importance of accurate documentation and accessibility. Moreover, it underscores the significance of user experience in enhancing visitor engagement and satisfaction. Overall, this project provides a holistic learning journey, encompassing technical skills, domain knowledge, and a user-centric approach to software development.
