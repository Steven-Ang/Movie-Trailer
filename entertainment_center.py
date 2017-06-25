import media
import fresh_tomatoes

# Create multiple movie instances
goodfellas = media.Movie("Goodfellas",
                        "The story of Henry Hill and his life through the teen years into the years of mafia, covering his relationship with wife Karen Hill and his Mob partners Jimmy Conway and Tommy DeVitto in the Italian-American crime syndicate.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNThjMzczMjctZmIwOC00NTQ4LWJhZWItZDdhNTk5ZTdiMWFlXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,669,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=qo5jJpHtI1Y")

godfather = media.Movie("The Godfather",
                        "Widely regarded as one of the greatest films of all time, this mob drama, based on Mario Puzo's novel of the same name, focuses on the powerful Italian-American crime family of Don Vito Corleone (Marlon Brando). When the don's youngest son, Michael (Al Pacino), reluctantly joins the Mafia, he becomes involved in the inevitable cycle of violence and betrayal. Although Michael tries to maintain a normal relationship with his wife, Kay (Diane Keaton), he is drawn deeper into the family business.",
                        "https://movietalkexpress.files.wordpress.com/2015/12/the-godfather.jpeg",
                        "https://www.youtube.com/watch?v=sY1S34973zA")

silence_of_the_lambs = media.Movie("The Silence of The Lambs",
                                   "Jodie Foster stars as Clarice Starling, a top student at the FBI's training academy. Jack Crawford (Scott Glenn) wants Clarice to interview Dr. Hannibal Lecter (Anthony Hopkins), a brilliant psychiatrist who is also a violent psychopath, serving life behind bars for various acts of murder and cannibalism. Crawford believes that Lecter may have insight into a case and that Starling, as an attractive young woman, may be just the bait to draw him out.",
                                   "https://images-na.ssl-images-amazon.com/images/I/410VHPrwUPL._SY450_.jpg",
                                   "https://www.youtube.com/watch?v=RuX2MQeb8UM")

halloween = media.Movie("Halloween",
                        "On a cold Halloween night in 1963, six year old Michael Myers brutally murdered his 17-year-old sister, Judith. He was sentenced and locked away for 15 years. But on October 30, 1978, while being transferred for a court date, a 21-year-old Michael Myers steals a car and escapes Smith's Grove. He returns to his quiet hometown of Haddonfield, Illinois, where he looks for his next victims.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNzk1OGU2NmMtNTdhZC00NjdlLWE5YTMtZTQ0MGExZTQzOGQyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
                        "https://www.youtube.com/watch?v=xHuOtLTQ_1I")

the_shining = media.Movie("The Shining",
                        "Jack Torrance accepts a caretaker job at the Overlook Hotel, where he, along with his wife Wendy and their son Danny, must live isolated from the rest of the world for the winter. But they aren't prepared for the madness that lurks within.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BZWFlYmY2MGEtZjVkYS00YzU4LTg0YjQtYzY1ZGE3NTA5NGQxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
                        "https://www.youtube.com/watch?v=5Cb3ik6zP2I")

evangelion = media.Movie("The End of Evangelion",
                        "NERV faces a brutal attack from SEELE, but with Asuka in a coma, and Shinji in a nervous breakdown, things soon turn into the surreal. This movie provides a concurrent ending to the final two episodes of the show “Neon Genesis Evangelion”.",
                        "https://images-na.ssl-images-amazon.com/images/I/51XFaesw92L.jpg",
                        "https://www.youtube.com/watch?v=IQrXRBh94IA")

# Store all of the movie in an array named "movies"
movies = [goodfellas, godfather, silence_of_the_lambs, halloween, the_shining, evangelion]

# Open a static web page and display all the movies
fresh_tomatoes.open_movies_page(movies)