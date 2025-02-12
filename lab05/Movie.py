class Movie:

    def __init__(self, movieName, director, year, rating=None):
        self.movieName = movieName.upper()
        self.director = director.upper()
        self.year = year
        self.rating = rating

    def getMovieName(self):
        self.movieName
        return self.movieName

    def getDirector(self):
        name = self.director.split(", ")
        return f"{name[1]} {name[0]}"

    def getYear(self):
        return self.year

    def getRating(self):
        return self.rating
    
    def getMovieDetails(self):
        return "{}, directed by {} ({}), Rating: {}".format(self.movieName, self.getDirector(), self.year, self.rating)

    def __gt__(self, other):
        if self.rating is None and other.rating is None:
            return self.movieName > other.movieName
        if self.rating is None:
            return False
        if other.rating is None:
            return True
        if self.rating != other.rating:
            return self.rating > other.rating
        return self.movieName > other.movieName