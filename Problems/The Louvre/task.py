class Painting:
    location = 'Louvre'

    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year


input_title = input()
input_artist = input()
input_year = input()
painting = Painting(input_title, input_artist, input_year)
print(f'"{painting.title}" by {painting.painter} ({painting.year}) hangs in the {painting.location}.')
