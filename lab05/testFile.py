from Movie import Movie
from MovieCollection import MovieCollection
from MovieCollectionNode import MovieCollectionNode

def test_movie():
    movie = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    assert movie.getMovieName() == "THE GODFATHER"
    assert movie.getDirector() == "DARABONT, FRANK"
    assert movie.getYear() == 1972
    assert movie.getRating() == 9.4

    movie_without_rating = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968)
    assert movie_without_rating.getRating() is None

def test_movie_details():
    movie = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    assert movie.getMovieDetails() == "THE GODFATHER directed by FRANK DARABONT (1972), Rating: 9.4"

    movie_without_rating = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968)
    assert movie_without_rating.getMovieDetails() == "2001: A SPACE ODYSSEY directed by STANLEY KUBRIC (1968), Rating: None"

def test_movie_comparison():
    movie1 = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    movie2 = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968, 9.2)
    movie3 = Movie("The Matrix", "Wachowski, Lana", 1999, 9.1)

    assert (movie1 > movie2) == True
    assert (movie2 > movie3) == False
    assert (movie3 > movie1) == False

def test_movie_collection_node_initialization():
    movie = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    node = MovieCollectionNode(movie)
    assert node.getData() == movie
    assert node.getNext() is None

def test_movie_collection_node_setters():
    movie1 = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    movie2 = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968, 9.2)
    node = MovieCollectionNode(movie1)
    node.setData(movie2)
    node.setNext(MovieCollectionNode(movie1))

    assert node.getData() == movie2
    assert node.getNext().getData() == movie1

def test_movie_collection_initialization():
    mc = MovieCollection()
    assert mc.isEmpty() == True
    assert mc.getNumberOfMovies() == 0

def test_movie_collection_insert():
    mc = MovieCollection()
    movie1 = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    movie2 = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968, 9.2)
    movie3 = Movie("The Matrix", "Wachowski, Lana", 1999, 9.1)

    mc.insertMovie(movie1)
    mc.insertMovie(movie2)
    mc.insertMovie(movie3)

    assert mc.isEmpty() == False
    assert mc.getNumberOfMovies() == 3

def test_movie_collection_get_all_movies():
    mc = MovieCollection()
    movie1 = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    movie2 = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968, 9.2)
    movie3 = Movie("The Matrix", "Wachowski, Lana", 1999, 9.1)

    mc.insertMovie(movie1)
    mc.insertMovie(movie2)
    mc.insertMovie(movie3)

    expected_output = (
        "2001: A SPACE ODYSSEY directed by STANLEY KUBRIC (1968), Rating: 9.2\n"
        "THE GODFATHER directed by FRANK DARABONT (1972), Rating: 9.4\n"
        "THE MATRIX directed by LANA WACHOWSKI (1999), Rating: 9.1\n"
    )
    assert mc.getAllMoviesInCollection() == expected_output

def test_movie_collection_get_movies_by_director():
    mc = MovieCollection()
    movie1 = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    movie2 = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968, 9.2)
    movie3 = Movie("The Matrix", "Wachowski, Lana", 1999, 9.1)

    mc.insertMovie(movie1)
    mc.insertMovie(movie2)
    mc.insertMovie(movie3)

    expected_output = (
        "2001: A SPACE ODYSSEY directed by STANLEY KUBRIC (1968), Rating: 9.2\n"
    )
    assert mc.getMoviesByDirector("Kubric, Stanley") == expected_output

def test_movie_collection_remove_director():
    mc = MovieCollection()
    movie1 = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    movie2 = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968, 9.2)
    movie3 = Movie("The Matrix", "Wachowski, Lana", 1999, 9.1)

    mc.insertMovie(movie1)
    mc.insertMovie(movie2)
    mc.insertMovie(movie3)

    mc.removeDirector("Kubric, Stanley")
    assert mc.getNumberOfMovies() == 2

def test_movie_collection_avg_director_rating():
    mc = MovieCollection()
    movie1 = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    movie2 = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968, 9.2)
    movie3 = Movie("The Matrix", "Wachowski, Lana", 1999, 9.1)

    mc.insertMovie(movie1)
    mc.insertMovie(movie2)
    mc.insertMovie(movie3)

    assert mc.avgDirectorRating("Darabont, Frank") == 9.4
    assert mc.avgDirectorRating("Kubric, Stanley") == 9.2

def test_movie_collection_recursive_search():
    mc = MovieCollection()
    movie1 = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    movie2 = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968, 9.2)
    movie3 = Movie("The Matrix", "Wachowski, Lana", 1999, 9.1)

    mc.insertMovie(movie1)
    mc.insertMovie(movie2)
    mc.insertMovie(movie3)

    assert mc.recursiveSearchMovie("The Godfather", mc.head) == True
    assert mc.recursiveSearchMovie("Inception", mc.head) == False