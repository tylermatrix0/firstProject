import media
import fresh_tomatoes

#creating each instance of the Movie class
watchmen = media.Movie("Watchmen",
                        "A group of heroes try to save the world",
                        "http://www.watchmencomicmovie.com/posters/watchmen-theatrical-poster-big.jpg",
                        "https://www.youtube.com/watch?v=PVjA0y78_EQ")

solaris = media.Movie("Solaris",
                        "A group of scientists try to communicate with a blue sentient planet",
                        "https://www.cinematerial.com/media/posters/sm/eg/egzj5qa8.jpg?v=1456250428",
                        "https://www.youtube.com/watch?v=rvm7WMbXfeY")

the_matrix = media.Movie("The Matrix",
                        "A man tries to change the depressing fate of humanity after A.I has taken over",
                        "http://www.impawards.com/1999/posters/matrix_ver1_xlg.jpg",
                        "https://www.youtube.com/watch?v=m8e-FF8MsqU")

the_room = media.Movie("The Room",
                        "Some movies are so good you can't come up with the words for a summary",
                        "http://www.impawards.com/2003/posters/room.jpg",
                        "https://www.youtube.com/watch?v=EE6RQ8rC8hc")

land_before_time = media.Movie("The Land Before Time",
                        "A group of dinosaurs embark on the journey of a liftime",
                        "http://www.impawards.com/1988/posters/land_before_time_xlg.jpg",
                        "https://www.youtube.com/watch?v=FBaGXDRNnQI")

first_snow = media.Movie("First Snow",
                        "A man tries to change his fate before the first snow",
                        "https://upload.wikimedia.org/wikipedia/en/9/94/Firstsnowposter.jpg",
                        "https://www.youtube.com/watch?v=Tx9Y_CNeYMY")
#allocating all instances of the movie class into an array
movies = [watchmen, solaris, the_matrix, the_room, land_before_time, first_snow]
#open_movies_page takes an array and converts it to html and css code
fresh_tomatoes.open_movies_page(movies)
