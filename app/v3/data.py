from app.v3.schemas import Artwork, Gallery, GalleryLocation, ArtistDetail, Exhibition

ARTWORKS = [
    Artwork(id=1, title="The Starry Night",
            artist=ArtistDetail(id=101, name="Vincent van Gogh", nationality="Dutch"),
            created_at="1889-06-01",
            medium="Oil on canvas",
            description="A swirling night sky over a village.",
            tags=["impressionism", "night", "landscape"]),
    Artwork(id=2, title="Girl with a Pearl Earring",
            artist=ArtistDetail(id=102, name="Johannes Vermeer", nationality="Dutch"),
            created_at="1665-01-01",
            medium="Oil on canvas",
            tags=["portrait", "baroque"]),
    Artwork(id=3, title="The Persistence of Memory",
            artist=ArtistDetail(id=103, name="Salvador Dali", nationality="Spanish"),
            created_at="1931-01-01",
            medium="Oil on canvas",
            description="Melting clocks in a dreamlike landscape.",
            tags=["surrealism", "dreamscape"]),
]

GALLERIES = [
    Gallery(id=1, title="Impressionist Hall",
            location=GalleryLocation(city="New York", country="USA",
                                     address="123 Museum Mile, Manhattan"),
            opening_hours="Tue-Sun 10:00-18:00",
            curator="Dr. Emily Chen"),
    Gallery(id=2, title="Modern Masters Wing",
            location=GalleryLocation(city="Paris", country="France",
                                     address="7 Avenue de la Bourdonnais"),
            curator="Prof. Henri Dubois"),
]

EXHIBITIONS = [
    Exhibition(id=1, name="Dreams and Visions",
               start_date="2024-03-01", end_date="2024-06-30",
               gallery_id=1, artwork_ids=[1, 3]),
]
