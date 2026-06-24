from app.cinema.v2.schemas import Movie, Showtime, ShowtimeVenue

MOVIES = [
    Movie(id=1, title="Inception", director="Christopher Nolan",
          release_year=2010, genre="Sci-Fi", duration_min=148, rating=8.8),
    Movie(id=2, title="The Godfather", director="Francis Ford Coppola",
          release_year=1972, genre="Crime", duration_min=175, rating=9.2),
    Movie(id=3, title="Parasite", director="Bong Joon-ho",
          release_year=2019, genre="Thriller", duration_min=132, rating=8.5),
]

SHOWTIMES = [
    Showtime(id=1, movie_id=1, date="2024-07-01", time="18:00",
             venue=ShowtimeVenue(screen="Screen A", hall="Main Hall", capacity=120)),
    Showtime(id=2, movie_id=1, date="2024-07-01", time="21:00",
             venue=ShowtimeVenue(screen="Screen A", hall="Main Hall", capacity=120)),
    Showtime(id=3, movie_id=2, date="2024-07-02", time="19:30",
             venue=ShowtimeVenue(screen="Screen B", hall="Grand Hall", capacity=200)),
    Showtime(id=4, movie_id=3, date="2024-07-03", time="20:00",
             venue=ShowtimeVenue(screen="Screen C", hall="Studio", capacity=60)),
]
