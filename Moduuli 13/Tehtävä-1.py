from flask import Flask
import math

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    number = int(luku)
    for kerroin in range(2, number, 1):
        if number % kerroin == 0:
            vastaus = 'false'
            break
    else:
        vastaus = 'true'

    tulos = {
        "Number" : number,
        "isPrime" : vastaus
    }

    return tulos

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)