from abc import ABC, abstractmethod


class Organizm(ABC):

    def __init__(self, inicjatywa, sila, pozycjax, pozycjay, swiat, literka, kolor):
        self.__wiek = swiat.iloscTur
        self.__inicjatywa = inicjatywa
        self.__sila = sila
        self.__pozycjay = pozycjay
        self.__pozycjax = pozycjax
        self.__swiat = swiat
        self.__kolor = kolor
        self.__literka = literka
        self.swiat.DodajNowy(self)

    @property
    def sila(self):
        return self.__sila

    @sila.setter
    def sila(self, sila):
        self.__sila = sila

    @property
    def swiat(self):
        return self.__swiat

    @swiat.setter
    def swiat(self, swiat):
        self.__swiat = swiat

    @property
    def pozycjax(self):
        return self.__pozycjax

    @pozycjax.setter
    def pozycjax(self, pozycjax):
        self.__pozycjax = pozycjax

    @property
    def pozycjay(self):
        return self.__pozycjay

    @pozycjay.setter
    def pozycjay(self, pozycjay):
        self.__pozycjay = pozycjay

    @property
    def inicjatywa(self):
        return self.__inicjatywa

    @inicjatywa.setter
    def inicjatywa(self, inicjatywa):
        self.__inicjatywa = inicjatywa

    @property
    def wiek(self):
        return self.__wiek

    @wiek.setter
    def wiek(self, wiek):
        self.__wiek = wiek

    @property
    def kolor(self):
        return self.__kolor

    @property
    def literka(self):
        return self.__literka

    def CzyOdbil(self, wrog):
        return False

    def CzyZwial(self):
        return False

    def Usuniecie(self):
        self.swiat.Usun(self)
        self.wiek = self.swiat.iloscTur + 100

    @abstractmethod
    def Akcja(self):
        pass

    @abstractmethod
    def Kolizja(self, wrog, atakujacy):
        pass

    @abstractmethod
    def ZrobDziecko(self, pozycjax, pozycjay):
        pass

    @abstractmethod
    def CzyAkcja(self):
        pass

    def CzyTrujacy(self):
        return False

    def CzyZwierze(self):
        return False
