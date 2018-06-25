from random import choice
class album(object):

    def __init__(self, list, artist, label, year):
        self.list = list
        self.artist = artist
        self.label = label
        self.year = year

    def rand_album(self,list):
        choice(self.list)

class song(object):

    def __init__(self, title, artist, file, time, genre):
        self.title = title
        self.artist = artist
        self.file = file
        self.time = time
        self.genre = genre

    def play(self, title, go = " "):
        self.go = go
        go = raw_input("What to you want to do?")
        if go.lower() == "play":
            return True
        else:
            return False

    def rand_song(self, title):
        choice(self.title)

class play_list(object):

    def __init__(self, title,  )
