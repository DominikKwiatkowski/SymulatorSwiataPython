import random

from Organizmy.Ziemia import Ziemia
from Organizmy.Zwierzeta import Zwierzeta


class Antylopa(Zwierzeta):

    def __init__(self, pozycjax, pozycjay, swiat):
        super(Antylopa, self).__init__(4, 4, pozycjax, pozycjay, swiat, 'A', "gray")

    def ZrobDziecko(self, pozycjax, pozycjay):
        dziecko = Antylopa(pozycjax, pozycjay, self.swiat)
        self.swiat.DodMapa(pozycjax, pozycjay, dziecko)

    def Akcja(self):
        super(Antylopa, self).Akcja()
        if (self.swiat.mapa[self.pozycjax][self.pozycjay] == self):
            super(Antylopa, self).Akcja()

    def CzyZwial(self):
        if random.randint(0, 1) == 0:
            tab = self.swiat.GetSasiadow(self)
            if (len(tab) == 0):
                return False
            while len(tab) > 0:
                punkt = random.choice(tab)
                tab.remove(punkt)
                if isinstance(self.swiat.mapa[punkt.x][punkt.y], Ziemia):
                    self.swiat.mapa[self.pozycjax][self.pozycjay] = Ziemia(self.swiat, self.pozycjax, self.pozycjay)
                    self.pozycjax = punkt.x
                    self.pozycjay = punkt.y
                    self.swiat.mapa[self.pozycjax][self.pozycjay] = self
                    return True
            return False
