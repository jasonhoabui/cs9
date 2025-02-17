from MovieCollectionNode import MovieCollectionNode
from Movie import Movie

class MovieCollection:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getNumberOfMovies(self):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.getNext()
        return count

    def insertMovie(self, movie):
        newNode = MovieCollectionNode(movie)
        if self.head is None or movie < self.head.getData():
            newNode.setNext(self.head)
            self.head = newNode
            return

        current = self.head
        while current.getNext() and current.getNext().getData() < movie:
            current = current.getNext()

        newNode.setNext(current.getNext())
        current.setNext(newNode)

    def getAllMoviesInCollection(self):
        current = self.head
        movies = ""
        while current != None:
            movies += current.getData().getMovieDetails() + "\n"
            current = current.getNext()

        return movies

    def getMoviesByDirector(self, director):
        movies = ""
        current = self.head
        while current != None:
            if current.getData().getDirector() == director.upper():
                movies += current.getData().getMovieDetails() + "\n"
            current = current.getNext()
        return movies

    def removeDirector(self, director):
        current = self.head
        previous = None
        
        while current != None and current.getData().getDirector() == director.upper():
            self.head = current.getNext()
            current = self.head

        while current != None:
            if current.getData().getDirector() == director.upper():
                previous.setNext(current.getNext())
            else:
                previous = current
            current = current.getNext()

    def avgDirectorRating(self, director):
        director = director.upper()
        total_rating = 0
        count = 0
        current = self.head
        while current:
            movie = current.getData()
            if movie.getDirector() == director and movie.getRating() is not None:
                total_rating += movie.getRating()
                count += 1
            current = current.getNext()
        return round(total_rating / count, 2) if count > 0 else None

    def recursiveSearchMovie(self, movieName, movieNode):
        if movieNode is None:
            return False
        if movieNode.getData().getMovieName().lower() == movieName.lower():
            return True
        return self.recursiveSearchMovie(movieName, movieNode.getNext())
