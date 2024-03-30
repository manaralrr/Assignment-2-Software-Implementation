class Exhibition:

    exhibitions = []
    
    def __init__(self, name, location, start_date, end_date):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        Exhibition.exhibitions.append(self)

    def get_all_exhibitions():
        return Exhibition.exhibitions
