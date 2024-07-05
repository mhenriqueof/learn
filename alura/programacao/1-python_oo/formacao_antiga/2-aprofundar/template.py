class Info:
    def __init__(self, name, year):
        self._name    = name.title()
        self.year     = year
        self._likes   = 0

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name.title()
    
    @property
    def likes(self):
        return self._likes
    
    def give_like(self):
        self._likes += 1
    
    def __str__(self):
        return f'Name  | {self.name}\nYear  | {self.year}\nLikes | {self._likes}\n'
    
        
class Movie(Info):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration
    
    def __str__(self):
        return f'Name | {self.name}\nYear | {self.year}\nDuration | {self.duration} minutes\nLikes | {self._likes}\n'
        
        
class Serie(Info):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons  = seasons
    
    def __str__(self):
        return f'Name | {self.name}\nYear | {self.year}\nSeasons | {self.seasons} {"seasons" if self.seasons > 1 else "season"}\nLikes | {self._likes}\n'

    
class Playlist:
    def __init__(self, name, titles):
        self.name   = name
        self._titles = titles
    
    def __getitem__(self, item):
        return self._titles[item]

    def __len__(self):
        return len(self._titles)
        
    @property
    def titles(self):
        return self._titles
    
    
lotr = Movie('the lord of the rings', 2001, 210)
severance = Serie('severance', 2022, 1)
walle = Movie('wall-e', 2008, 110)
mrobot = Serie('mr. robot', 2015, 4)

lotr.give_like()
lotr.give_like()
lotr.give_like()
severance.give_like()
walle.give_like()
walle.give_like()
walle.give_like()
mrobot.give_like()
mrobot.give_like()

movies_series = [lotr, severance, walle, mrobot]
playlist_weekend = Playlist('Weekend', movies_series)

print(f'{len(playlist_weekend)} titles.\n')

for watch in playlist_weekend:
    print(watch)
