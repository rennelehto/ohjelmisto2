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
        self.matka = self.nopeusnyt * tunnit

autoja = []

for auto in autoja