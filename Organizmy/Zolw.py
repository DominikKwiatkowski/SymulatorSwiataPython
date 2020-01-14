import random

from Organizmy.Zwierzeta import Zwierzeta


class Zolw(Zwierzeta):

    def __init__(self, pozycjax, pozycjay, swiat):
        super(Zolw, self).__init__(1, 2, pozycjax, pozycjay, swiat, 'Z', "dark green")

    def ZrobDziecko(self, pozycjax, pozycjay):
        dziecko = Zolw(pozycjax, pozycjay, self.swiat)
        self.swiat.DodMapa(pozycjax, pozycjay, dziecko)

    def Akcja(self):
       if random.randint(0,3) == 0:
           super(Zolw, self).Akcja()

    def CzyOdbil(self, wrog):
        if(wrog.sila<5):
            return True
        return False
