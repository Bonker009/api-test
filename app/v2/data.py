from app.v2.schemas import Artwork, Gallery, GalleryLocation

ARTWORKS = [
    Artwork(id=1, title="The Starry Night", artist_name="Vincent van Gogh",
            year=1889, medium="Oil on canvas",
            description="A swirling night sky over a village."),
    Artwork(id=2, title="Girl with a Pearl Earring", artist_name="Johannes Vermeer",
            year=1665, medium="Oil on canvas"),
    Artwork(id=3, title="The Persistence of Memory", artist_name="Salvador Dali",
            year=1931, medium="Oil on canvas",
            description="Melting clocks in a dreamlike landscape."),
]

GALLERIES = [
    Gallery(id=1, name="Impressionist Hall",
            location=GalleryLocation(city="New York", country="USA",
                                     address="123 Museum Mile, Manhattan"),
            opening_hours="Tue-Sun 10:00-18:00"),
    Gallery(id=2, name="Modern Masters Wing",
            location=GalleryLocation(city="Paris", country="France",
                                     address="7 Avenue de la Bourdonnais")),
]
