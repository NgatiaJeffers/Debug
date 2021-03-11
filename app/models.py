class Album:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self, topalbums):
        self.topalbums = topalbums


    def artist(self, id, name, url, urlToImage, playcount, listeners):
        self.id = id
        self.name = name
        self.url = url
        self.urlToImage = urlToImage
        self.playcount = playcount
        self.listeners = listeners

class Tracks:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self, id, name, url, urlToImage, playcount, listeners):
        self.id = id
        self.name = name
        self.url = url
        self.urlToImage = urlToImage
        self.playcount = playcount
        self.listeners = listeners