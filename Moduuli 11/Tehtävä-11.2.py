'''Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. Sähköautolla on
ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden
ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman
kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden
polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus, käske autoja
ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

lisäksi: akun kulutus, jos ehtii'''

import random

class Auto:
    def __init__(self, rekkari, huippun):
        self.rekkari = rekkari
        self.huippun = huippun
        self.nopeusnyt = 80
        self.matka = 0

    def kiihdytä(self, vauhti):
        if self.nopeusnyt + vauhti < 0:
            self.nopeusnyt = 0
        elif self.nopeusnyt + vauhti > self.huippun:
            self.nopeusnyt = self.huippun
        else:
            self.nopeusnyt += vauhti

    def kulje(self, tunnit):
        self.matka += (self.nopeusnyt * tunnit)

    def tulosta(self):
        print(f'Auto: {self.rekkari}, Kuljettu matka: {self.matka}')

class Sähköauto(Auto):
    def __init__(self, rekkari, huippun, akkukapasiteetti):
        super().__init__(rekkari, huippun)
        self.akkukapasiteetti = akkukapasiteetti

    def tulosta(self):
        super().tulosta()

class Polttomoottoriauto(Auto):
    def __init__(self, rekkari, huippun, tankin_tilavuus):
        super().__init__(rekkari, huippun)
        self.tankin_tilavuus = tankin_tilavuus

    def tulosta(self):
        super().tulosta()




def aika_kuluu():
    for au in autot:
        kiih = random.randint(-10, 15)
        au.kiihdytä(kiih)
        au.kulje(3)


autot = []
autot.append(Polttomoottoriauto("ACD-123", 165, 32.3))
autot.append(Sähköauto("ABC-15", 180, 52.5))


aika_kuluu()


for a in autot:
    a.tulosta()

