from flask import Flask, render_template, request, jsonify

import pymysql

app = Flask(__name__)

try:
    print("Intentando conectar a la base de datos...")
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="escuela2"
    )
    print("Conexión exitosa con la base de datos.")

except Exception as e:
    print(f"Error al conectar con la base de datos: {e}")

# Definimos rutas
@app.route('/')
def mostrar_alumnos():
    # Rellenar template

    # Cargar contenidos
    cursor = db.cursor()
    cursor.execute("SELECT * FROM alumno")
    alumnos = cursor.fetchall()
    cursor.close()
    return render_template('index.html', alumnos=alumnos)

@app.route('/submit', methods=['POST'])
def submit():
    if db is None:
        return "Error: No hay base de datos activa"
    name = request.form['name']
    age = request.form['age']
    course = request.form['course']

    cursor = db.cursor()
    cursor.execute(f"INSERT INTO alumno (nombre, edad, curso) VALUES ('{name}', {age}, '{course}º')")
    db.commit()
    cursor.close()

    return redirect(url_for('mostrar_alumnos'))

if __name__ == '__main__':
    app.run(debug=True)