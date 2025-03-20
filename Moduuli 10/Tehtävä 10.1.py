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
                testihissi.kerros_alas()
            elif self.sijainti < kerros:
                testihissi.kerros_ylös()

    def kerros_ylös(self):
        self.sijainti = self.sijainti + 1
        print(f'Hissi on kerroksessa {testihissi.sijainti}.')

    def kerros_alas(self):
        self.sijainti = self.sijainti -1
        print(f'Hissi on kerroksessa {testihissi.sijainti}.')

testihissi = Hissi(1, 7)

print(f'Hissi on kerroksessa {testihissi.sijainti}.')

testihissi.siirry_kerrokseen(6)
print()
testihissi.siirry_kerrokseen(testihissi.alin)