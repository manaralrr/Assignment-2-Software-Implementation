from enum import Enum

class Location(Enum):
    PERMANENT_GALLERY = 1
    EXHIBITION_HALL = 2
    OUTDOOR_SPACE = 3

class Artwork:

    artworks = []
    
    def __init__(self, title, artist, date_of_creation, historical_significance, location):
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance
        self.location = location
        Artwork.artworks.append(self)

    def get_all_artworks():
        return Artwork.artworks
