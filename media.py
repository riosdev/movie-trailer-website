class Movie():
    # Creates a Movie instance with a title, an url for the poster image
    # and an url for the movie trailer
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.trailer_youtube_url = trailer_youtube_url
        self.title = title
        self.poster_image_url = poster_image_url
