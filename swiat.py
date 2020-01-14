from Organizmy.Antylopa import Antylopa
from Organizmy.BarszczSosnowskiego import BarszczSosnowskiego
from Organizmy.CyberOwca import CyberOwca
from Organizmy.Czlowiek import Czlowiek
from Organizmy.Guarana import Guarana
from Organizmy.Lis import Lis
from Organizmy.Mlecz import Mlecz
from Organizmy.Owca import Owca
from Organizmy.Trawa import Trawa
from Organizmy.WilczeJagody import WilczeJagody
from Organizmy.Wilk import Wilk
from Organizmy.Zolw import Zolw
from Punkt import Punkt
from Organizmy.Ziemia import Ziemia
from Aplikacja import Aplikacja
from Organizmy.organizm import Organizm


class Swiat:


    def __init__(self, dlugosc, szerokosc):
        self.__iloscTur = 0
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
        self.mapa = [[Ziemia(self, i, j) for i in range(self.dlugosc)] for j in range(self.szerokosc)]
        self.__window = Aplikacja()
        self.__lista = []
        self.__oczekujace = []
        self.__usun = []
        self.__czlowiek = None

    @property
    def czlowiek(self):
        return self.__czlowiek

    @czlowiek.setter
    def czlowiek(self, czlowiek):
        self.__czlowiek = czlowiek

    @property
    def dlugosc(self):
        return self.__dlugosc

    @dlugosc.setter
    def dlugosc(self, dlugosc):
        self.__dlugosc = dlugosc

    @property
    def szerokosc(self):
        return self.__szerokosc

    @szerokosc.setter
    def szerokosc(self, szerokosc):
        self.__szerokosc = szerokosc

    @property
    def iloscTur(self):
        return self.__iloscTur

    @iloscTur.setter
    def iloscTur(self, iloscTur):
        self.__iloscTur = iloscTur

    def Wypisz(self):
        self.__window.DodajSwiat(self)

    def PrzeprowadzTure(self):
        self.iloscTur += 1
        for org in self.__oczekujace:
            self.Dodaj(org)
        self.__oczekujace.clear()
        for i in range(len(self.__lista)):
            if self.__lista[i] != None and self.__lista[i].wiek < self.iloscTur:
                self.__lista[i].Akcja()

        for org in self.__usun:
            if(org in self.__lista):
                self.__lista.remove(org)
        self.__usun.clear()
        self.__window.WypiszPlansze()

    def Zapisz(self):
        plik = open("zapis.txt", 'w')
        for org in self.__oczekujace:
            self.Dodaj(org)
        self.__oczekujace.clear()
        plik.write(str(self.dlugosc) + '\n')
        plik.write(str(self.szerokosc) + '\n')
        plik.write(str(self.iloscTur) + '\n')
        plik.write(str(len(self.__lista)) + '\n')
        for org in self.__lista:
            if org == self.czlowiek:
                plik.write(str(self.czlowiek.literka) + '\n')
                plik.write(str(self.czlowiek.pozycjax) + '\n')
                plik.write(str(self.czlowiek.pozycjay) + '\n')
                plik.write(str(self.czlowiek.sila) + '\n')
                plik.write(str(self.czlowiek.moc) + '\n')
            else:
                plik.write(str(org.literka) + '\n')
                plik.write(str(org.pozycjax) + '\n')
                plik.write(str(org.pozycjay) + '\n')
                plik.write(str(org.sila) + '\n')
        plik.close()

    def WczytajOrganizm(self, organizm, x, y, sila):
        if (organizm == 'G'):
            organizm = Guarana(x, y, self)
        elif (organizm == 'M'):
            organizm = Mlecz(x, y, self)
        elif (organizm == 'O'):
            organizm = Owca(x, y, self)
        elif (organizm == 'T'):
            organizm = Trawa(x, y, self)
        elif (organizm == 'J'):
            organizm = WilczeJagody(x, y, self)
        elif (organizm == 'B'):
            organizm = BarszczSosnowskiego(x, y, self)
        elif (organizm == 'L'):
            organizm = Lis(x, y, self)
        elif (organizm == 'Z'):
            organizm = Zolw(x, y, self)
        elif (organizm == 'A'):
            organizm = Antylopa(x, y, self)
        elif (organizm == 'Y'):
            organizm = CyberOwca(x, y, self)
        else:
            organizm = Wilk(x, y, self)
        self.DodMapa(x, y, organizm)
        organizm.sila = sila

    def Wczytaj(self):
        plik = open("zapis.txt", 'r')
        self.__lista.clear()
        self.__usun.clear()
        self.__oczekujace.clear()
        self.dlugosc = int(plik.readline())
        self.szerokosc = int(plik.readline())
        self.mapa = [[Ziemia(self, i, j) for i in range(self.dlugosc)] for j in range(self.szerokosc)]
        self.iloscTur = int(plik.readline())
        dlugosc = int(plik.readline())
        for i in range(dlugosc):
            literka = plik.readline()
            pozycjax = int(plik.readline())
            pozycjay = int(plik.readline())
            sila = int(plik.readline())
            if literka[0] == 'C':
                moc = int(plik.readline())
                self.czlowiek = Czlowiek(pozycjax, pozycjay, self)
                self.czlowiek.sila = sila
                self.czlowiek.moc = moc
                self.DodMapa(pozycjax,pozycjay, self.czlowiek)
            else:
                self.WczytajOrganizm(literka[0], pozycjax, pozycjay, sila)
        self.__window.WypiszPlansze()

    def GetSasiadow(self, org: Organizm):
        tab = []
        if org.pozycjax > 0:
            x = org.pozycjax - 1
            tab.append(Punkt(x, org.pozycjay))
        if org.pozycjax + 1 < self.dlugosc:
            tab.append(Punkt(org.pozycjax + 1, org.pozycjay))
        if org.pozycjay > 0:
            tab.append(Punkt(org.pozycjax, org.pozycjay - 1))
        if org.pozycjay + 1 < self.szerokosc:
            tab.append(Punkt(org.pozycjax, org.pozycjay + 1))

        return tab

    def DodajNowy(self, org: Organizm):
        if (isinstance(org, Ziemia)):
            return
        self.__oczekujace.append(org)

    def Dodaj(self, org: Organizm):
        if (isinstance(org, Ziemia)):
            return
        for i in range(len(self.__lista)):
            if (self.__lista[i].inicjatywa < org.inicjatywa):
                self.__lista.insert(i, org)
                return
        self.__lista.append(org)

    def Usun(self, org: Organizm):
        self.__usun.append(org)

    def DodMapa(self, pozycjax, pozycjay, org: Organizm):
        self.mapa[pozycjax][pozycjay] = org
