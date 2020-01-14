from Punkt import Punkt
from Organizmy.Ziemia import Ziemia
from Organizmy.organizm import Organizm
import random


class Rosliny(Organizm):

    def __init__(self, sila, pozycjax, pozycjay, swiat, literka, kolor):
        super(Rosliny, self).__init__(0, sila, pozycjax, pozycjay, swiat, literka, kolor)

    def CzyAkcja(self):
        tab = self.swiat.GetSasiadow(self)
        if len(tab) == 0:
            return Punkt()
        if random.randint(0, 10) > 2:
            return Punkt()
        for i in range(10):
            pole = random.choice(tab)
            if isinstance(self.swiat.mapa[pole.x][pole.y], Ziemia):
                return pole
        else:
            return Punkt()

    def Akcja(self):
        punkt = self.CzyAkcja()
        if punkt.x == -1:
            return
        else:
            self.ZrobDziecko(punkt.x, punkt.y)

    def Kolizja(self, wrog: Organizm, atakujacy):
        if self.sila > wrog.sila:
            wrog.Usuniecie()
