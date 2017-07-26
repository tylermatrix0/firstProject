#import webbrowser class for the show_trailer method
import webbrowser
#creating movie class
class Movie():
    #initializes the Movie class as a constructor
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        #each self. line, assigns the arguments from initilizing the class and assigns it to the isntance of the class
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    #shows the trailer by using the webbrowser.open class
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
