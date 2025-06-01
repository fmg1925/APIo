from flask import Flask, render_template
import os

app = Flask(__name__)

apio = 'apio'

apios = {
    "total": 3,
    "especie": "Apium graveolens",
    "reino": "Plantae",
    "division": "Magnoliophyta",
    "clase": "Magnoliopsida",
    "subclase": "Rosidae",
    "orden": "Apiales",
    "familia": "Apiaceae",
    "genero": "Apium",
    "apios": [
    {
      "nombre": "Apio de tallo",
      "nombre_cientifico": "Apium graveolens var. dulce",
      "precio_clp": 1200,
      "color": "verde claro",
      "variedades_comerciales": ["Utah", "Pascal", "Green Bay", "EC-99249-1", "PRL-85-1"]
    },
    {
      "nombre": "Apio nabo",
      "nombre_cientifico": "Apium graveolens var. rapaceum",
      "precio_clp": 2300,
      "color": "blanco con hojas verdes",
      "variedades_comerciales": ["Prinz", "Bola de nieve", "De Reuil", "Diamant", "Gigante de Praga"]
    },
    {
      "nombre": "Apio de hoja",
      "nombre_cientifico": "Apium graveolens var. secalinum",
      "precio_clp": 1500,
      "color": "verde oscuro",
      "variedades_comerciales": ["Variedad asiática 1", "Variedad asiática 2"]
    }
  ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apio', methods=['GET'])
def get_apio():
    return apio

@app.route('/apios', methods=['GET'])
def get_apios():
    return apios
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
