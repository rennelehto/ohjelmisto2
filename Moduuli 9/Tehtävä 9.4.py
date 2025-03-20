'''Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan
seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin
välein seuraavat toimenpiteet:

    Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan
    väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
    Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.

Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan
kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.'''

import random

class Auto:
    autojen_määrä = 0
    def __init__(self, rekkari, huippun):
        self.rekkari = rekkari
        self.huippun = huippun
        self.nopeusnyt = 0
        self.matka = 0
        Auto.autojen_määrä += 1

    def kiihdytä(self, vauhti):
        if self.nopeusnyt + vauhti < 0:
            self.nopeusnyt = 0
        elif self.nopeusnyt + vauhti > self.huippun:
            self.nopeusnyt = 142
        else:
            self.nopeusnyt = self.nopeusnyt + vauhti

    def kulje(self, tunnit):
        self.matka = self.matka + (self.nopeusnyt * tunnit)

autoja = []

for i in range(1, 11):

    autoja.append(f'auto{i}')
    nop = random.randint(100, 200)
    autoja[i-1] = Auto(f'ABC-{i}', nop)

#print(autoja[0].huippun)
#print(Auto.autojen_määrä)
'''x = 0
for a in autoja:
    print(f'Rekisterinumero: {autoja[x].rekkari}, huippunopeus: {autoja[x].huippun} km/h, nopeus nyt: {autoja[x].nopeusnyt} km/h, kuljettu matka: {autoja[x].matka} km.')
    x +=1'''

matka = 0
while matka < 10000:
    for a in autoja:
        kiih = random.randint(-10, 15)
        a.kiihdytä(kiih)
        a.kulje(1)
        if a.matka > matka:
            matka = a.matka

else:
    z = 0
    print(f'{'Rekisteritunnus':15} {'Huippunopeus':>15} {'Hetkellinen nopeus':>20} {'Kuljettu matka':>15}')
    for a in autoja:

        print(f'{autoja[z].rekkari:>15}{autoja[z].huippun:15}{autoja[z].nopeusnyt:20} {autoja[z].matka:15}')
        z +=1