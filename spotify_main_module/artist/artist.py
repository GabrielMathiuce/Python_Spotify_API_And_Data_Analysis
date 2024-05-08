import string
import json


class Artist:
    __external_urls: string
    __followers: string
    __genres: string
    __href: string
    __id: string
    __images: string
    __name: string
    __popularity: string
    __type: string
    __uri: string

    def __init__(self, external_urls='None', followers='None', genres='None', href='None', id='None', images='None', name='None', popularity='None', type='None', uri='None'):
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
            'external_urls': self.external_urls,
            'followers': self.followers,
            'genres': self.genres,
            'href': self.href,
            'id': self.id,
            'images': self.images,
            'name': self.name,
            'popularity': self.popularity,
            'type': self.type,
            'uri': self.uri
        })
        print(output)
        return output

    def test(self):
        return self.__str__()
