from Organizmy.Zwierzeta import Zwierzeta


class Wilk(Zwierzeta):

    def __init__(self, pozycjax, pozycjay, swiat):
        super(Wilk, self).__init__(5, 9, pozycjax, pozycjay, swiat, 'W', "black")

    def ZrobDziecko(self, pozycjax, pozycjay):
        dziecko = Wilk(pozycjax, pozycjay, self.swiat)
        self.swiat.DodMapa(pozycjax, pozycjay, dziecko)
