from app.v1.schemas import Artwork, Gallery

ARTWORKS = [
    Artwork(id=1, title="The Starry Night", artist="Vincent van Gogh",
            year=1889, medium="Oil on canvas"),
    Artwork(id=2, title="Girl with a Pearl Earring", artist="Johannes Vermeer",
            year=1665, medium="Oil on canvas"),
    Artwork(id=3, title="The Persistence of Memory", artist="Salvador Dali",
            year=1931, medium="Oil on canvas"),
]

GALLERIES = [
    Gallery(id=1, name="Impressionist Hall", location="New York, USA", capacity=150),
    Gallery(id=2, name="Modern Masters Wing", location="Paris, France", capacity=200),
]
