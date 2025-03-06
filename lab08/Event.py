class Event:

    def __init__(self, day, time, location):
        self.day = day
        self.time = time
        self.location = location

    def __eq__(self, rhs):
        return 

    def __str__(self):
        return f"{self.day} {self.time}, {self.location}"