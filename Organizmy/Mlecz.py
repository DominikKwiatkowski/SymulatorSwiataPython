from Organizmy.Rosliny import Rosliny


class Mlecz(Rosliny):

    def __init__(self, pozycjax, pozycjay, swiat):
        super(Mlecz, self).__init__(0, pozycjax, pozycjay, swiat, 'M', "yellow")

    def ZrobDziecko(self, pozycjax, pozycjay):
        dziecko = Mlecz(pozycjax, pozycjay, self.swiat)
        self.swiat.DodMapa(pozycjax, pozycjay, dziecko)

    def Akcja(self):
        super(Mlecz, self).Akcja()
        super(Mlecz, self).Akcja()
        super(Mlecz, self).Akcja()
