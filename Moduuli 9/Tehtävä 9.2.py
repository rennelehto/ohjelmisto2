'''Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
joka saa parametrinaan nopeuden muutoksen (km/h). Jos nopeuden
muutos on negatiivinen, auto hidastaa. Metodin on muutettava
auto-olion nopeus-ominaisuuden arvoa. Auton nopeus ei saa kasvaa
huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin
+30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän
jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos
-200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää.'''

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



eka = Auto('ABC-123', 142 )

print(f'Rekisterinumero: {eka.rekkari}, huippunopeus: {eka.huippun}, nopeus nyt: {eka.nopeusnyt}, kuljettu matka: {eka.matka}')

eka.kiihdytä(30)
eka.kiihdytä(70)
eka.kiihdytä(50)
print(f'Auton nopeus on {eka.nopeusnyt}.')
eka.kiihdytä(-200)
print(f'Auton nopeus on {eka.nopeusnyt}.')

