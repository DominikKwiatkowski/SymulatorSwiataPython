from Organizmy.Rosliny import Rosliny
from Organizmy.Ziemia import Ziemia
from Organizmy.organizm import Organizm


class BarszczSosnowskiego(Rosliny):

    def __init__(self, pozycjax, pozycjay, swiat):
        super(BarszczSosnowskiego, self).__init__(10, pozycjax, pozycjay, swiat, 'B', "red")

    def ZrobDziecko(self, pozycjax, pozycjay):
        dziecko = BarszczSosnowskiego(pozycjax, pozycjay, self.swiat)
        self.swiat.DodMapa(pozycjax, pozycjay, dziecko)

    def CzyTrujacy(self):
        return True

    def Kolizja(self, wrog: Organizm, atakujacy):
        if (self.sila > wrog.sila):
            self.swiat.mapa[self.pozycjax][self.pozycjay] = Ziemia(self.swiat, self.pozycjax, self.pozycjay)
            self.Usuniecie()
            if wrog.literka != 'Y':
                wrog.swiat.mapa[wrog.pozycjax][wrog.pozycjay] = Ziemia(wrog.swiat, wrog.pozycjax, wrog.pozycjay)
                wrog.Usuniecie()

    def Akcja(self):
        tab = self.swiat.GetSasiadow(self)
        for point in tab:
            if point.x != -1:
                if self.swiat.mapa[point.x][point.y].CzyZwierze():
                    self.swiat.mapa[point.x][point.y].Usuniecie()
                    self.swiat.mapa[point.x][point.y] = Ziemia(self.swiat, point.x, point.y)
        super(BarszczSosnowskiego, self).Akcja()
