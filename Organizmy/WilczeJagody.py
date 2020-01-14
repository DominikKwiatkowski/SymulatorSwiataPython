from Organizmy.Rosliny import Rosliny
from Organizmy.Ziemia import Ziemia
from Organizmy.organizm import Organizm


class WilczeJagody(Rosliny):

    def __init__(self, pozycjax, pozycjay, swiat):
        super(WilczeJagody, self).__init__(99, pozycjax, pozycjay, swiat, 'J', "purple")

    def ZrobDziecko(self, pozycjax, pozycjay):
        dziecko = WilczeJagody(pozycjax, pozycjay, self.swiat)
        self.swiat.DodMapa(pozycjax, pozycjay, dziecko)

    def CzyTrujacy(self):
        return True

    def Kolizja(self, wrog: Organizm, atakujacy):
        if (self.sila > wrog.sila):
            self.swiat.mapa[self.pozycjax][self.pozycjay] = Ziemia(self.swiat, self.pozycjax, self.pozycjay)
            self.Usuniecie()
        wrog.swiat.mapa[wrog.pozycjax][wrog.pozycjay] = Ziemia(wrog.swiat, wrog.pozycjax, wrog.pozycjay)
        wrog.Usuniecie()
