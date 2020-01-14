import random

from Organizmy.Antylopa import Antylopa
from Organizmy.CyberOwca import CyberOwca
from Organizmy.Czlowiek import Czlowiek
from Organizmy.Lis import Lis
from Organizmy.BarszczSosnowskiego import BarszczSosnowskiego
from Organizmy.WilczeJagody import WilczeJagody
from Organizmy.Ziemia import Ziemia
from Organizmy.Guarana import Guarana
from Organizmy.Mlecz import Mlecz
from Organizmy.Owca import Owca
from Organizmy.Trawa import Trawa
from Organizmy.Wilk import Wilk
from Organizmy.Zolw import Zolw
from swiat import Swiat

swiat = Swiat(20, 20)
swiat.czlowiek = Czlowiek(10, 10, swiat)
swiat.DodMapa(10, 10, swiat.czlowiek)
for i in range(30):
    while 1:
        x = random.randint(0, 19)
        y = random.randint(0, 19)
        tab = ['G', 'M', 'O', 'T', 'W', 'J', 'B', 'Z', 'A', 'L', 'Y']
        organizm = random.choice(tab)
        if (isinstance(swiat.mapa[x][y], Ziemia)):
            if (organizm == 'G'):
                organizm = Guarana(x, y, swiat)
            elif (organizm == 'M'):
                organizm = Mlecz(x, y, swiat)
            elif (organizm == 'O'):
                organizm = Owca(x, y, swiat)
            elif (organizm == 'T'):
                organizm = Trawa(x, y, swiat)
            elif (organizm == 'J'):
                organizm = WilczeJagody(x, y, swiat)
            elif (organizm == 'B'):
                organizm = BarszczSosnowskiego(x, y, swiat)
            elif (organizm == 'L'):
                organizm = Lis(x, y, swiat)
            elif (organizm == 'Z'):
                organizm = Zolw(x, y, swiat)
            elif (organizm == 'A'):
                organizm = Antylopa(x, y, swiat)
            elif (organizm == 'Y'):
                organizm = CyberOwca(x, y, swiat)
            else:
                organizm = Wilk(x, y, swiat)

            swiat.DodMapa(x, y, organizm)
            break

swiat.Wypisz()
