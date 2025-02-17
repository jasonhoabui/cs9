class Movie:

    def __init__(self, movieName, director, year, rating=None):
        self.movieName = movieName.upper()
        self.director = director.upper()
        self.year = year
        self.rating = rating

    def getMovieName(self):
        return self.movieName

    def getDirector(self):
        return self.director

    def getYear(self):
        return self.year

    def getRating(self):
        return self.rating

    def getMovieDetails(self):
        last_name, first_name = self.director.split(", ")
        director_firstLast = f"{first_name} {last_name}"
        return "{} directed by {} ({}), Rating: {}"\
               .format(self.movieName, director_firstLast, self.year, self.rating)

    def __gt__(self,rhs):
        if self.director != rhs.director:
            return self.director > rhs.director

        if self.year != rhs.year:
            return self.year > rhs.year

        return self.movieName > rhs.movieName