from Organizmy.Ziemia import Ziemia
from Organizmy.Zwierzeta import Zwierzeta
from Kierunek import Kierunek
from Punkt import Punkt


class Czlowiek(Zwierzeta):


    def __init__(self, pozycjax, pozycjay, swiat):
        super(Czlowiek, self).__init__(4, 5, pozycjax, pozycjay, swiat, 'C', "blue")
        self.__moc = -4
        self.__cel: Kierunek = Kierunek.Stay

    def ZrobDziecko(self, pozycjax, pozycjay):
        pass

    def SpalWszystko(self):
        tab = self.swiat.GetSasiadow(self)
        for point in tab:
            if point.x != -1 and not isinstance(self.swiat.mapa[point.x][point.y], Ziemia):
                self.swiat.mapa[point.x][point.y].Usuniecie()
                self.swiat.mapa[point.x][point.y] = Ziemia(self.swiat, point.x, point.y)

    def CzyAkcja(self):
        if self.cel == Kierunek.Up and self.pozycjax > 0:
            return Punkt(self.pozycjax - 1, self.pozycjay)
        elif self.cel == Kierunek.Down and self.pozycjax + 1 < self.swiat.dlugosc:
            return Punkt(self.pozycjax + 1, self.pozycjay)
        elif self.cel == Kierunek.Left and self.pozycjay > 0:
            return Punkt(self.pozycjax, self.pozycjay - 1)
        elif self.cel == Kierunek.Right and self.pozycjay + 1 < self.swiat.szerokosc:
            return Punkt(self.pozycjax, self.pozycjay + 1)
        else:
            return Punkt()

    def Akcja(self):
        if (self.moc > 0):
            self.SpalWszystko()
        super(Czlowiek, self).Akcja()
        self.cel = Kierunek.Stay
        if (self.moc > 0):
            self.SpalWszystko()
        self.__moc = self.moc - 1

    @property
    def cel(self):
        return self.__cel

    @property
    def moc(self):
        return self.__moc

    @moc.setter
    def moc(self, moc):
        self.__moc = moc

    @cel.setter
    def cel(self, cel):
        self.__cel = cel

    def Uzycie(self):
        if (self.moc < -4):
            self.__moc = 5
