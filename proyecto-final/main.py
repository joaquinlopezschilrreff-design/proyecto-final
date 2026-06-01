from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import sqlite3

app = Flask(__name__)
app.secret_key = "studymood"

conexion = sqlite3.connect(
    "usuarios.db",
    check_same_thread=False
)

cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    correo TEXT,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS resumenes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT,
    materia TEXT,
    contenido TEXT,
    fecha TEXT
)
""")

conexion.commit()

@app.route("/", methods=["POST", "GET"])
def inicio():

    if request.method == "POST":

        correo = request.form["correo"]
        contraseña = request.form["password"]

        cursor.execute(
            "SELECT * FROM usuarios WHERE correo = ?",
            (correo,)
        )

        usuario = cursor.fetchone()

        if usuario and usuario[3] == contraseña:

            session["usuario"] = usuario[1]
            session["correo"] = usuario[2]

            return redirect("/start")

    return render_template("login.html")


@app.route("/start")
def principal():

    if "usuario" not in session:
        return redirect("/")

    usuario = session["usuario"]

    cursor.execute(
        "SELECT COUNT(*) FROM resumenes WHERE usuario = ?",
        (usuario,)
    )

    cantidad_resumenes = cursor.fetchone()[0]

    cursor.execute(
        "SELECT contenido FROM resumenes WHERE usuario = ?",
        (usuario,)
    )

    resumenes = cursor.fetchall()

    palabras = 0

    for resumen in resumenes:
        palabras += len(resumen[0].split())

    cursor.execute(
        """
        SELECT materia, fecha
        FROM resumenes
        WHERE usuario = ?
        ORDER BY id DESC
        LIMIT 1
        """,
        (usuario,)
    )

    ultimo = cursor.fetchone()

    ultima_materia = "Ninguna"

    if ultimo:
        ultima_materia = ultimo[0]

    return render_template(
        "index.html",
        usuario=usuario,
        cantidad_resumenes=cantidad_resumenes,
        palabras=palabras,
        ultima_materia=ultima_materia
    )



@app.route("/register", methods=["POST", "GET"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        r_correo = request.form["r_correo"]
        r_password = request.form["r_password"]
        r_confirmacion = request.form["r_confirmacion"]

        cursor.execute(
            "SELECT * FROM usuarios WHERE correo = ?",
            (r_correo,)
        )

        usuario_existente = cursor.fetchone()

        if usuario_existente:
            return "Ese correo ya está registrado"

        if r_password != r_confirmacion:
            return "Las contraseñas no coinciden"

        cursor.execute(
            "INSERT INTO usuarios (nombre, correo, password) VALUES (?, ?, ?)",
            (username, r_correo, r_password)
        )

        conexion.commit()

        return redirect("/")

    return render_template("register.html")


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


@app.route("/materias")
def materias():

    if "usuario" not in session:
        return redirect("/")

    return render_template(
        "materias.html",
        usuario=session["usuario"]
    )



@app.route("/materia/<nombre>", methods=["GET", "POST"])
def materia(nombre):

    if "usuario" not in session:
        return redirect("/")

    usuario = session["usuario"]

    if request.method == "POST":

        contenido = request.form["contenido"]

        cursor.execute(
            "DELETE FROM resumenes WHERE usuario = ? AND materia = ?",
            (usuario, nombre)
        )

        fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

        cursor.execute(
            "INSERT INTO resumenes (usuario, materia, contenido, fecha) VALUES (?, ?, ?, ?)",
            (usuario, nombre, contenido, fecha)
        )

        conexion.commit()

    cursor.execute(
        "SELECT contenido FROM resumenes WHERE usuario = ? AND materia = ?",
        (usuario, nombre)
    )

    resumen = cursor.fetchone()

    texto = ""

    if resumen:
        texto = resumen[0]

    return render_template(
        "materia.html",
        usuario=usuario,
        materia=nombre,
        contenido=texto
    )


app.run(debug=True)