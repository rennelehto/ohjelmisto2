import random

class Auto:
    def __init__(self, rekkari, huippun):
        self.rekkari = rekkari
        self.huippun = huippun
        self.nopeusnyt = 0
        self.matka = 0

    def kiihdytä(self, vauhti):
        if self.nopeusnyt + vauhti < 0:
            self.nopeusnyt = 0
        elif self.nopeusnyt + vauhti > self.huippun:
            self.nopeusnyt = self.huippun
        else:
            self.nopeusnyt = self.nopeusnyt + vauhti

    def kulje(self, tunnit):
        self.matka += self.nopeusnyt * tunnit




#tämä tehtävä
class Kilpailu:
    def __init__(self, nimi, pituus, autolista):
        self.nimi = nimi
        self.pituus = pituus
        self.autolista = autolista
        self.autoja = []
        self.aika = 0

        for i in range(autolista+1):
            self.autoja.append(f'auto{i}')
            huippun = random.randint(100, 200)
            self.autoja[i - 1] = Auto(f'ABC-{i}', huippun)


    def tunti_kuluu(self):
        for a in self.autoja:
            kiih = random.randint(-10, 15)
            a.kiihdytä(kiih)
            a.kulje(1)
            self.aika = self.aika + 1


    def tulosta_tilanne(self):
        print(f'{'Rekisteritunnus':15} {'Huippunopeus':>15} {'Hetkellinen nopeus':>20} {'Kuljettu matka':>15}')
        for a in kisa.autoja:
            print(f'{a.rekkari:>15}{a.huippun:15}{a.nopeusnyt:20} {a.matka:15}')


    def kilpailu_ohi(self):
        for a in self.autoja:
            if  a.matka >= self.pituus:
                kisa.tulosta_tilanne()





kisa = Kilpailu('Suuri romuralli', 8000, 10)
#print(kisa.autoja)
#kisa.tulosta_tilanne()

while not kisa.kilpailu_ohi():

    kisa.tunti_kuluu()
    print('Tunti kului.')
    kisa.kilpailu_ohi()
    print('Onko kisa ohi?')
    if kisa.aika %10:
        kisa.tulosta_tilanne()
kisa.tulosta_tilanne()

