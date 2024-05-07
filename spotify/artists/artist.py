import string
import json


class Artist:
    def __init__(self, external_urls: string = 'Null', followers: string = 'Null', genres: string = 'Null',
                 href: string = 'Null', id: string = 'Null', images: string = 'Null', name: string = 'Null',
                 popularity: string = 'Null', type: string = 'Null', uri: string = 'Null'):
        self.external_urls = external_urls
        self.followers = followers
        self.genres = genres
        self.href = href
        self.id = id
        self.images = images
        self.name = name
        self.popularity = popularity
        self.type = type
        self.uri = uri

    def __str__(self) -> json:
        output: json = json.dumps({
            'external_urls ' : self.external_urls,
            'followers' : self.followers,
            'genres' : self.genres,
            'href' : self.href,
            'id' : self.id,
            'images' : self.images,
            'name' : self.name,
            'popularity' : self.popularity,
            'type' : self.type,
            'uri' : self.uri
        })
        print(output)
        return output

    def test(self):
        return self.__str__()
