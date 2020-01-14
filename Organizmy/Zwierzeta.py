import random

from Punkt import Punkt
from Organizmy.Ziemia import Ziemia
from Organizmy.organizm import Organizm


class Zwierzeta(Organizm):

    def __init__(self, inicjatywa, sila, pozycjax, pozycjay, swiat, literka, kolor):
        super(Zwierzeta, self).__init__(inicjatywa, sila, pozycjax, pozycjay, swiat, literka, kolor)

    def Akcja(self):
        punkt = self.CzyAkcja()
        if punkt.x == -1:
            return
        elif isinstance(self.swiat.mapa[punkt.x][punkt.y], Ziemia):
            self.swiat.mapa[self.pozycjax][self.pozycjay] = Ziemia(self.swiat, self.pozycjax, self.pozycjay)
            self.pozycjay = punkt.y
            self.pozycjax = punkt.x
            self.swiat.mapa[self.pozycjax][self.pozycjay] = self
        else:
            self.Kolizja(self.swiat.mapa[punkt.x][punkt.y], True)

    def Kolizja(self, wrog: Organizm, atakujacy):
        if wrog.literka == self.literka:
            tab = self.swiat.GetSasiadow(self)
            for punkt in tab:
                if (punkt.x >= 0):
                    if (isinstance(self.swiat.mapa[punkt.x][punkt.y], Ziemia)):
                        self.ZrobDziecko(punkt.x, punkt.y)
                        return
            if (atakujacy):
                wrog.Kolizja(self, False)
        elif wrog.CzyOdbil(self):
            return
        elif atakujacy == False and self.sila <= wrog.sila:
            return
        else:
            pozycjax = wrog.pozycjax
            pozycjay = wrog.pozycjay
            if wrog.CzyZwial() and atakujacy:
                self.swiat.mapa[self.pozycjax][self.pozycjay] = Ziemia(self.swiat, self.pozycjax, self.pozycjay)
                self.pozycjax = pozycjax
                self.pozycjay = pozycjay
                self.swiat.mapa[self.pozycjax][self.pozycjay] = self
            elif self.CzyZwial():
                return
            else:
                if self.sila > wrog.sila:
                    wrog.Kolizja(self, False)
                    self.swiat.mapa[self.pozycjax][self.pozycjay] = Ziemia(self.swiat, self.pozycjax, self.pozycjay)
                    if atakujacy:
                        self.pozycjax = pozycjax
                        self.pozycjay = pozycjay
                        self.swiat.mapa[self.pozycjax][self.pozycjay] = self
                    wrog.Usuniecie()
                elif self.sila == wrog.sila:
                    if (atakujacy):
                        wrog.Kolizja(self, False)
                        self.swiat.mapa[self.pozycjax][self.pozycjay] = Ziemia(self.swiat, self.pozycjax,
                                                                               self.pozycjay)
                        self.pozycjax = pozycjax
                        self.pozycjay = pozycjay
                        self.swiat.mapa[self.pozycjax][self.pozycjay] = self
                        wrog.Usuniecie()
                else:
                    wrog.Kolizja(self, False)

    def CzyZwierze(self):
        return True

    def CzyAkcja(self):
        tab = self.swiat.GetSasiadow(self)
        if (len(tab) == 0):
            return Punkt()
        return random.choice(tab)
