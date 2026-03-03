from gestor_datos import cargar_datos, guardar_datos
from flask import Flask,render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def inicio():
    return redirect("/login")
@app.route("/login", methods = ["GET","POST"])
def login():
    usuarios = cargar_datos()
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]
        if usuario in usuarios and usuarios[usuario] == password:
            return render_template("bienvenido.html",nombre = usuario,cantidad_users= len(usuarios),acceso=datetime.now().strftime("%d/%m/%Y"),estado="Activo")
        else:
            return render_template("login.html",error = "credenciales incorrectas")
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
            usuarios[usuario] = password
            guardar_datos(usuarios)
            return redirect("/login")
    return render_template("register.html",exist_user=None)

if __name__ == "__main__":
    app.run(debug=True)
