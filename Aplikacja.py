from tkinter import *
from Kierunek import Kierunek
from Organizmy.Antylopa import Antylopa
from Organizmy.BarszczSosnowskiego import BarszczSosnowskiego
from Organizmy.CyberOwca import CyberOwca
from Organizmy.Guarana import Guarana
from Organizmy.Lis import Lis
from Organizmy.Mlecz import Mlecz
from Organizmy.Owca import Owca
from Organizmy.Trawa import Trawa
from Organizmy.WilczeJagody import WilczeJagody
from Organizmy.Wilk import Wilk
from Organizmy.Zolw import Zolw


class Aplikacja(Frame):

    def __init__(self):
        canvas = None
        __swiat = None
        print("okno")

    def DodajSwiat(self, swiat):
        window = Tk()
        self.__swiat = swiat
        self.UruchomOkno(window)
        window.mainloop()

    def WypiszPlansze(self):
        print("Wypisuje")
        self.canvas.delete(all)
        for i in range(self.__swiat.dlugosc):
            for j in range(self.__swiat.szerokosc):
                self.canvas.create_rectangle(30 + j * 30, 35 + i * 30, 30 + 30 * self.__swiat.szerokosc,
                                             35 + 30 * self.__swiat.dlugosc, fill=self.__swiat.mapa[i][j].kolor)
        self.canvas.pack()

    def UruchomOkno(self, window):
        window.title("Dominik Kwiatkowski 175454")
        window.geometry("1280x720")
        window.resizable(0, 0)

        self.canvas = Canvas(window, height=1500, width=1000)
        self.canvas.bind('<Button-1>', lambda ev: self.Menu(window))
        self.WypiszPlansze()
        self.WypiszButton(window)

    def WypiszButton(self, window):
        b1 = Button(window, text="Nowa Tura", command=lambda: self.callbackB1(), height=50, width=50)
        b1.place(bordermode=OUTSIDE, height=30, width=100, x=0, y=0)
        b2 = Button(window, text="Zapisz", command=self.callbackB2, height=50, width=50)
        b2.place(bordermode=OUTSIDE, height=30, width=100, x=110)
        b3 = Button(window, text="Wczytaj", command=self.callbackB3, height=50, width=50)
        b3.place(bordermode=OUTSIDE, height=30, width=100, x=220)
        window.bind('<Left>', lambda ev: self.lewaStrzalka())
        window.bind('<Right>', lambda ev: self.prawaStrzalka())
        window.bind('<Up>', lambda ev: self.GornaStrzalka())
        window.bind('<Down>', lambda ev: self.DolnaStrzalka())
        window.bind('<n>', lambda ev: self.Umiejetnosc())

    def Menu(self, window):
        def ok():
            organizm = variable.get()
            if (organizm == 'Guarana'):
                organizm = Guarana(x, y, self.__swiat)
            elif (organizm == 'Mlecz'):
                organizm = Mlecz(x, y, self.__swiat)
            elif (organizm == 'Owca'):
                organizm = Owca(x, y, self.__swiat)
            elif (organizm == 'Trawa'):
                organizm = Trawa(x, y, self.__swiat)
            elif (organizm == 'Wilcze Jagody'):
                organizm = WilczeJagody(x, y, self.__swiat)
            elif (organizm == 'Barszcz Sosnowskiego'):
                organizm = BarszczSosnowskiego(x, y, self.__swiat)
            elif (organizm == 'Lis'):
                organizm = Lis(x, y, self.__swiat)
            elif (organizm == 'Zolw'):
                organizm = Zolw(x, y, self.__swiat)
            elif (organizm == 'Antylopa'):
                organizm = Antylopa(x, y, self.__swiat)
            elif (organizm == 'Cyber Owca'):
                organizm = CyberOwca(x, y, self.__swiat)
            else:
                organizm = Wilk(x, y, self.__swiat)
            self.__swiat.mapa[x][y].Usuniecie()
            self.__swiat.DodMapa(x, y, organizm)
            self.WypiszPlansze()
            button.destroy()
            w.destroy()

        x = int((window.winfo_pointery() - window.winfo_rooty() - 35) / 30)
        y = int((window.winfo_pointerx() - window.winfo_rootx() - 168) / 30)
        if x < 0 or y < 0 or x > self.__swiat.dlugosc or y > self.__swiat.szerokosc:
            return
        lista = ["Antylopa", "Barszcz Sosnowskiego", "Cyber Owca", "Guarana", "Lis", "Mlecz", "Owca", "Trawa",
                 "Wilcze Jagody", "Wilk", "Zolw"]
        variable = StringVar(window)
        variable.set(lista[0])
        w = OptionMenu(window, variable, *lista)
        w.place(bordermode=OUTSIDE, height=30, width=150, x=1000)
        button = Button(window, text="OK", command=ok)
        button.place(bordermode=OUTSIDE, height=30, width=100, x=1000, y=50)

    def callbackB1(self):
        self.__swiat.PrzeprowadzTure()

    def callbackB2(self):
        self.__swiat.Zapisz()

    def callbackB3(self):
        self.__swiat.Wczytaj()

    def Umiejetnosc(self):
        self.__swiat.czlowiek.Uzycie()

    def lewaStrzalka(self):
        self.__swiat.czlowiek.cel = Kierunek.Left
        self.__swiat.PrzeprowadzTure()

    def prawaStrzalka(self):
        self.__swiat.czlowiek.cel = Kierunek.Right
        self.__swiat.PrzeprowadzTure()

    def GornaStrzalka(self):
        self.__swiat.czlowiek.cel = Kierunek.Up
        self.__swiat.PrzeprowadzTure()

    def DolnaStrzalka(self):
        self.__swiat.czlowiek.cel = Kierunek.Down
        self.__swiat.PrzeprowadzTure()
