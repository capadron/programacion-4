from flask import Flask, jsonify

app = Flask(__name__)

from inmunizacion import porcentaje


@app.route('/inmunizacion')
def getPorcentaje():
    return jsonify({"porcentaje": porcentaje, "mensaje": "Inmunizacion contra el Sarampion (Porcentaje de ninos entre 12 y 23 meses de edad"})
if __name__ == '__main__':
    app.run(debug=True, port=4000)
