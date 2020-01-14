from Organizmy.organizm import Organizm


class Ziemia(Organizm):

    def __init__(self, swiat, pozycjax, pozycjay):
        super(Ziemia, self).__init__(0, 0, pozycjax, pozycjay, swiat, ' ', "sandy brown")
    def Akcja(self):
        pass
    def Kolizja(self, wrog, atakujacy):
        pass
    def ZrobDziecko(self,pozycjax,pozycjay):
        pass
    def CzyAkcja(self):
        pass
