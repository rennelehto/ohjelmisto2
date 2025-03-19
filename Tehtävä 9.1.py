'''Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus,
tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa
ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin. Uuden auton
nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma,
jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta
pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.'''

class Auto:
    autojen_määrä = 0
    def __init__(self, rekkari, huippun):
        self.rekkari = rekkari
        self.huippun = huippun
        self.nopeusnyt = 0
        self.matka = 0
        Auto.autojen_määrä += 1

eka = Auto('ABC-123', '142 km/h' )

print(f'Rekisterinumero: {eka.rekkari}, huippunopeus: {eka.huippun}, nopeus nyt: {eka.nopeusnyt}, kuljettu matka: {eka.matka}')