from math import fabs

from Organizmy.BarszczSosnowskiego import BarszczSosnowskiego
from Organizmy.Zwierzeta import Zwierzeta
from Organizmy.organizm import Organizm
from Punkt import Punkt


class CyberOwca(Zwierzeta):

    def __init__(self, pozycjax, pozycjay, swiat):
        super(CyberOwca, self).__init__(4, 11, pozycjax, pozycjay, swiat, 'Y', "cyan")

    def ZrobDziecko(self, pozycjax, pozycjay):
        dziecko = CyberOwca(pozycjax, pozycjay, self.swiat)
        self.swiat.DodMapa(pozycjax, pozycjay, dziecko)

    def CzyAkcja(self):
        odleglosc = self.swiat.szerokosc * self.swiat.dlugosc
        org: Organizm = None
        for i in range(self.swiat.dlugosc):
            for j in range(self.swiat.szerokosc):
                if isinstance(self.swiat.mapa[i][j], BarszczSosnowskiego):
                    if (fabs(self.pozycjax - i) + fabs(self.pozycjay - j) < odleglosc):
                        org = self.swiat.mapa[i][j]
                        odleglosc = fabs(self.pozycjax - i) + fabs(self.pozycjay - j)
        if org == None:
            return super(CyberOwca,self).CzyAkcja()
        if (self.pozycjax > org.pozycjax):
            return Punkt(self.pozycjax - 1, self.pozycjay)
        elif (self.pozycjax < org.pozycjax):
            return Punkt(self.pozycjax + 1, self.pozycjay)
        elif (self.pozycjay > org.pozycjay):
            return Punkt(self.pozycjax, self.pozycjay - 1)
        elif (self.pozycjay < org.pozycjay):
            return Punkt(self.pozycjax, self.pozycjay + 1)
        else:
            return Punkt()

    def CzyZwierze(self):
        return False
