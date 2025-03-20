'''Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman ja
ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin
numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.'''

class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.sijainti = self.alin

    def siirry_kerrokseen(self, kerros):
        if kerros > self.ylin:
            kerros = self.ylin
        elif kerros < self.alin:
            kerros = self.alin
        while self.sijainti != kerros:
            if self.sijainti > kerros:
                self.kerros_alas()
            elif self.sijainti < kerros:
                self.kerros_ylös()

    def kerros_ylös(self):
        self.sijainti = self.sijainti + 1
        print(f'Hissi on kerroksessa {self.sijainti}.')

    def kerros_alas(self):
        self.sijainti = self.sijainti -1
        print(f'Hissi on kerroksessa {self.sijainti}.')

class Talo:
    def __init__(self, ylin, alin, lkm):
        self.ylin = ylin
        self.alin = alin
        self.lkm = lkm
        self.talon_hissit = []
        for h in range(lkm):
            a = Hissi(1, 7)
            self.talon_hissit.append(a)

    def aja_hissiä(self, nro, kerros):
        print(f'Hissi nro {nro} lähtee kerroksesta {self.talon_hissit[nro-1].sijainti}.')
        self.talon_hissit[nro-1].siirry_kerrokseen(kerros)


talo1 = Talo(7, 1, 3)

talo1.aja_hissiä(3, 5)