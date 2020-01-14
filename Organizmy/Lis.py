import random

from Organizmy.Zwierzeta import Zwierzeta
from Punkt import Punkt


class Lis(Zwierzeta):

    def __init__(self, pozycjax, pozycjay, swiat):
        super(Lis, self).__init__(7, 3, pozycjax, pozycjay, swiat, 'L', "orange")

    def ZrobDziecko(self, pozycjax, pozycjay):
        dziecko = Lis(pozycjax, pozycjay, self.swiat)
        self.swiat.DodMapa(pozycjax, pozycjay, dziecko)

    def CzyAkcja(self):
        tab = self.swiat.GetSasiadow(self)
        if (len(tab) == 0):
            return Punkt()
        while len(tab) > 0:
            punkt = random.choice(tab)
            tab.remove(punkt)
            if self.swiat.mapa[punkt.x][punkt.y].sila <= self.sila:
                return punkt
        return Punkt()
