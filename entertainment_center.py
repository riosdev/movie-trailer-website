import media
import fresh_tomatoes

primer = media.Movie("Primer",
                     "http://img.moviepostershop.com/primer-movie-poster-2004-1020240454.jpg",
                     "https://www.youtube.com/watch?v=3nj5MMURCm8")

the_big_sick = media.Movie("The Big Sick",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BZWM4YzZjOTEtZmU5ZS00ZTRkLWFiNjAtZTEwNzIzMDM5MjdmXkEyXkFqcGdeQXVyNDg2MjUxNjM@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                           "https://www.youtube.com/watch?v=jcD0Daqc3Yw")

arrival = media.Movie("Arrival",
                      "https://ichef.bbci.co.uk/news/660/cpsprodpb/48CA/production/_90843681_890a8bd8-6501-11e6-aefa-e8609c477948_486x.jpg",
                      "https://www.youtube.com/watch?v=tFMo3UJ4B4g")

transcendence = media.Movie("Transcendence",
                            "https://img.fstatic.com/nKey_fXQv0fuE8hjdMXPSuCUCq8=/fit-in/290x478/smart/https://cdn.fstatic.com/media/movies/covers/2014/06/transcendence-a-revolucao_t67938_1.jpg",
                            "https://www.youtube.com/watch?v=VCTen3-B8GU")

the_adjustment_bureau = media.Movie("The Adjustment Bureau",
                                    "http://moviereviews.s3.amazonaws.com/2015/10/30/09/49/02/997/u7hg03e6GEa8mjQePFy7TkZRQ61.jpg",
                                    "https://www.youtube.com/watch?v=wZJ0TP4nTaE")

limitless = media.Movie("Limitless",
                        "http://cdn.collider.com/wp-content/uploads/limitless-uk-movie-poster.jpg",
                        "https://www.youtube.com/watch?v=4TLppsfzQH8")

in_time = media.Movie("In Time",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUyNDAxMjY0OF5BMl5BanBnXkFtZTgwNTM2NDAwMjI@._V1_SY500_CR0,0,337,500_AL_.jpg",
                      "https://www.youtube.com/watch?v=fdadZ_KrZVw")

happy_feet = media.Movie("Happy Feet",
                         "https://fontmeme.com/images/Happy-Feet-Poster.jpg",
                         "https://www.youtube.com/watch?v=aIBsnOyJB7Y")
# Gather all movie objects in a list
movies = [primer, arrival, the_big_sick, happy_feet,
          transcendence, the_adjustment_bureau, limitless, in_time]
fresh_tomatoes.open_movies_page(movies)

#
#
#
#
