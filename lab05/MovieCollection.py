class MovieCollection:

    def __init__(self):
        self.head = head

    def isEmpty(self):
        return self.head == None

    def getNumberOfMovies(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def insertMovie(self, movie):
        pass

    def getAllMoviesInCollection(self):
        total = ""
        current = self.head
        while current != None:
            total += current.getData().getMovieDetails() + "\n"
            current = current.getNext()
        return total

    def getMoviesByDirector(self, director):
        pass

    def removeDirector(self, director):
        pass

    def avgDirectorRating(self, director):
        pass

    def recursiveSearchMovie(self, movieName, movieNode):
        if movieNode == None:
            return False
        elif movieNode.getData().getMovieName() = movieName.upper():
            return True
        else:
            return self.recursiveSearchMovie(movieName, movieNode.next)