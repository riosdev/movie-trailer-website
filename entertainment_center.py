import media
import fresh_tomatoes

primer = media.Movie("Primer",
                     "http://img.moviepostershop.com/primer-movie-poster-2004-1010515846.jpg",
                     "https://www.youtube.com/watch?v=3nj5MMURCm8")
movies = [primer]
fresh_tomatoes.open_movies_page(movies)
