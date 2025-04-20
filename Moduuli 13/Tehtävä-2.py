from flask import Flask
import mysql.connector
#http://127.0.0.1:3000/kentt%C3%A4/EFHK
app = Flask(__name__)
@app.route('/kenttä/<ICAO>')
def koodi(ICAO):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{ICAO}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            vastaus = {
                "ICAO": ICAO,
                "Name": rivi[0],
                "Municipality": rivi[1]
            }

        return vastaus

yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='python',
        password='1232',
        autocommit=True
)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)