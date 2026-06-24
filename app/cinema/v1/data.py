from app.cinema.v1.schemas import Movie, Showtime

MOVIES = [
    Movie(id=1, title="Inception", director="Christopher Nolan",
          year=2010, genre="Sci-Fi", duration_min=148),
    Movie(id=2, title="The Godfather", director="Francis Ford Coppola",
          year=1972, genre="Crime", duration_min=175),
    Movie(id=3, title="Parasite", director="Bong Joon-ho",
          year=2019, genre="Thriller", duration_min=132),
]

SHOWTIMES = [
    Showtime(id=1, movie_id=1, date="2024-07-01", time="18:00",
             screen="Screen A", available_seats=120),
    Showtime(id=2, movie_id=1, date="2024-07-01", time="21:00",
             screen="Screen A", available_seats=85),
    Showtime(id=3, movie_id=2, date="2024-07-02", time="19:30",
             screen="Screen B", available_seats=200),
    Showtime(id=4, movie_id=3, date="2024-07-03", time="20:00",
             screen="Screen C", available_seats=60),
]
