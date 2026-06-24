from app.cinema.v3.schemas import Movie, Showtime, ShowtimeVenue, DirectorDetail, Booking

MOVIES = [
    Movie(id=1, title="Inception",
          director=DirectorDetail(name="Christopher Nolan", nationality="British-American"),
          release_year=2010, genres=["Sci-Fi", "Thriller", "Action"],
          duration_min=148, rating=8.8,
          cast=["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"]),
    Movie(id=2, title="The Godfather",
          director=DirectorDetail(name="Francis Ford Coppola", nationality="American"),
          release_year=1972, genres=["Crime", "Drama"],
          duration_min=175, rating=9.2,
          cast=["Marlon Brando", "Al Pacino", "James Caan"]),
    Movie(id=3, title="Parasite",
          director=DirectorDetail(name="Bong Joon-ho", nationality="South Korean"),
          release_year=2019, genres=["Thriller", "Drama", "Comedy"],
          duration_min=132, rating=8.5,
          cast=["Song Kang-ho", "Lee Sun-kyun", "Cho Yeo-jeong"]),
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

BOOKINGS = [
    Booking(id=1, showtime_id=1, customer_name="Alice Chen", seats=2, confirmed=True),
    Booking(id=2, showtime_id=3, customer_name="Bob Martinez", seats=4, confirmed=True),
    Booking(id=3, showtime_id=4, customer_name="Carol Smith", seats=1, confirmed=False),
]
