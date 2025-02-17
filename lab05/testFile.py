from Movie import Movie
from MovieCollection import MovieCollection
from MovieCollectionNode import MovieCollectionNode

#Movie
def test_MovieInit():
    movie = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    assert movie.getMovieName() == "THE GODFATHER"
    assert movie.getDirector() == "DARABONT, FRANK"
    assert movie.getYear() == 1972
    assert movie.getRating() == 9.4

def test_MovieDetails():
    movie = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    assert movie.getMovieDetails() == "THE GODFATHER directed by FRANK DARABONT (1972), Rating: 9.4"

def test_MovieComparison():
    movie1 = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    movie2 = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968, 9.2)
    assert movie2 > movie1

#MovieCollectionNode
def test_MovieCollectionNodeInit():
    movie = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    node = MovieCollectionNode(movie)
    assert node.getData() == movie
    assert node.getNext() is None

def test_Setters():
    movie1 = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    movie2 = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968, 9.2)
    node = MovieCollectionNode(movie1)
    node.setData(movie2)
    node.setNext(MovieCollectionNode(movie1))
    assert node.getData() == movie2
    assert node.getNext().getData() == movie1

#MovieCollection
def test_MovieCollectionInit():
    mc = MovieCollection()
    assert mc.isEmpty() == True
    assert mc.getNumberOfMovies() == 0

def test_MovieCollectionInsert():
    mc = MovieCollection()
    movie = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    mc.insertMovie(movie)
    assert mc.isEmpty() == False
    assert mc.getNumberOfMovies() == 1

def test_MovieCollectionGetAllMovies():
    mc = MovieCollection()
    movie = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    mc.insertMovie(movie)
    assert mc.getAllMoviesInCollection() == "THE GODFATHER directed by FRANK DARABONT (1972), Rating: 9.4\n"

def test_MovieCollectionGetMoviesByDirector():
    mc = MovieCollection()
    movie = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    mc.insertMovie(movie)
    assert mc.getMoviesByDirector("Darabont, Frank") == "THE GODFATHER directed by FRANK DARABONT (1972), Rating: 9.4\n"

def test_MovieCollectionRemoveDirector():
    mc = MovieCollection()
    movie = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    mc.insertMovie(movie)
    mc.removeDirector("Darabont, Frank")
    assert mc.getNumberOfMovies() == 0

def test_MovieCollectionAvgDirectorRating():
    mc = MovieCollection()
    movie = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    mc.insertMovie(movie)
    assert mc.avgDirectorRating("Darabont, Frank") == 9.4

def test_MovieCollectionRecursiveSearch():
    mc = MovieCollection()
    movie = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    mc.insertMovie(movie)
    assert mc.recursiveSearchMovie("The Godfather", mc.head) == True
    assert mc.recursiveSearchMovie("Inception", mc.head) == False