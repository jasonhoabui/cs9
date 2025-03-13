class Event:

    def __init__(self, day, time, location):
        self.day = day
        self.time = time
        self.location = location.upper()

    def __eq__(self, rhs):
        return (self.day == rhs.day and self.time == rhs.time and self.location == rhs.location)

    def __str__(self):
        start_hour = self.time[0] // 100
        start_min = self.time[0] % 100
        end_hour = self.time[1] // 100
        end_min = self.time[1] % 100
        start = f"{start_hour:02d}:{start_min:02d}" 
        end = f"{end_hour:02d}:{end_min:02d}" 
        return f"{self.day} {start} - {end}, {self.location}"