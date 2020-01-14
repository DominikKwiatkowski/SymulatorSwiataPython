from Organizmy.Rosliny import Rosliny
from Organizmy.organizm import Organizm


class Guarana(Rosliny):

    def __init__(self, pozycjax, pozycjay, swiat):
        super(Guarana, self).__init__(0, pozycjax, pozycjay, swiat, 'G', "pink")

    def ZrobDziecko(self, pozycjax, pozycjay):
        dziecko = Guarana(pozycjax, pozycjay, self.swiat)
        self.swiat.DodMapa(pozycjax, pozycjay, dziecko)

    def Kolizja(self,wrog: Organizm,atakujacy):
        wrog.sila +=3
        super(Guarana, self).Kolizja(wrog, atakujacy)
