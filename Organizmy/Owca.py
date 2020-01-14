from Organizmy.Zwierzeta import Zwierzeta


class Owca(Zwierzeta):

    def __init__(self, pozycjax, pozycjay, swiat):
        super(Owca, self).__init__(4, 4, pozycjax, pozycjay, swiat, 'O', "white")

    def ZrobDziecko(self, pozycjax, pozycjay):
        dziecko = Owca(pozycjax, pozycjay, self.swiat)
        self.swiat.DodMapa(pozycjax, pozycjay, dziecko)