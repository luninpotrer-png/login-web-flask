from gestor_datos import cargar_datos, guardar_datos, hashear
from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import time
from collections import defaultdict


app = Flask(__name__)
app.secret_key="olada"

@app.route("/")
def inicio():
    return redirect("/login")

intentos = defaultdict(int)
bloqueados = {}

LIMITE = 3
TIEMPO = 30

@app.route("/login", methods = ["GET","POST"])
def login():
    usuarios = cargar_datos()
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]
        if usuario in bloqueados:
            tiempo_restante = TIEMPO - (time.time() - bloqueados[usuario])
            if tiempo_restante > 0:
                return render_template("login.html",error=f"Bloqueado, espera {int(tiempo_restante)} segundos")
            else:
                del bloqueados[usuario]
                intentos[usuario] = 0

        if usuario in usuarios and usuarios[usuario] == hashear(password):
            session["usuario"]=usuario
            return redirect("/bienvenido")
        else:
            intentos[usuario] += 1
            if intentos[usuario] >= LIMITE:
                bloqueados[usuario] = time.time()
                return render_template("login.html",error=f"Cuenta Bloqueada espere {TIEMPO} segundos")
            return render_template("login.html",error = f"credenciales incorrectas, intentos: {intentos[usuario]}/{LIMITE}")
    return render_template("login.html",error = None)

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "POST":
        usuario = request.form["usuario_register"]
        password = request.form["password_register"]
        usuarios = cargar_datos()
        if usuario in usuarios:
            return render_template("register.html",exist_user="este usuario ya existe")
        else:
            usuarios[usuario] = hashear(password)
            guardar_datos(usuarios)
            return redirect("/login")
    return render_template("register.html",exist_user=None)

@app.route("/bienvenido")
def bienvenido():
    if "usuario" not in session:
        return redirect("/login")
    return render_template("bienvenido.html",nombre=session["usuario"],cantidad_users=len(cargar_datos()),acceso=datetime.now().strftime("%d/%m/%Y"),estado="Activo")



if __name__ == "__main__":
    app.run(debug=True)
