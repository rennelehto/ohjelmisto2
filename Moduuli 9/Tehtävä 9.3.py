'''Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa
tuntimäärässä edennyt. Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.'''

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

eka = Auto('ABC-123', 142 )

eka.kiihdytä(60)
eka.kulje(1.5)

print(eka.nopeusnyt)
print(eka.matka)
