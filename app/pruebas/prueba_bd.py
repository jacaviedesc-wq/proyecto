from flask import Flask
from BaseDeDatos import ConfiguracionBD  

app = Flask(__name__)

# Inicializar la base de datos
db = ConfiguracionBD(app)

@app.route("/testdb")
def testdb():
    try:
        cursor = db.get_cursor()
        cursor.execute("SELECT NOW();") 
        resultado = cursor.fetchone()
        return f"Conexión exitosa. Hora en MySQL: {resultado[0]}"
    except Exception as e:
        return f"Error de conexión: {e}"

if __name__ == "__main__":
    app.run(debug=True)
