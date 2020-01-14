from Organizmy.Rosliny import Rosliny


class Trawa(Rosliny):

    def __init__(self, pozycjax, pozycjay, swiat):
        super(Trawa, self).__init__(0, pozycjax, pozycjay, swiat, 'T', "green")

    def ZrobDziecko(self, pozycjax, pozycjay):
        dziecko = Trawa(pozycjax, pozycjay, self.swiat)
        self.swiat.DodMapa(pozycjax, pozycjay, dziecko)