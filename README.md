# 🔐 Login Web con Flask / Flask Web Login

> A modern web login & register page built with Flask, HTML and CSS | Página de login y registro web moderna hecha con Flask, HTML y CSS

---

## 🇪🇸 Español

### 📋 Descripción
Aplicación web de autenticación desarrollada con Python y Flask. Incluye login y registro de usuarios con credenciales guardadas en JSON, manejo de errores, redirección, dashboard post-login y una interfaz moderna con diseño oscuro y animación de borde.

### ⚙️ Tecnologías usadas
- **Python 3**
- **Flask** — framework web
- **HTML/CSS** — interfaz de usuario
- **Jinja2** — motor de plantillas
- **JSON** — base de datos local
- **HASH256** - contraseñas con hash256
- **Google Fonts (Jost)** — tipografía

### 🚀 Cómo instalarlo y usarlo

**1. Cloná el repositorio:**
```bash
git clone https://github.com/luninpotrer-png/login-web-flask.git
cd login-web-flask
```

**2. Instalá Flask:**
```bash
pip install flask
```

**3. Ejecutá el programa:**
```bash
python app.py
```

**4. Abrí el navegador en:**
```
http://127.0.0.1:5000
```

### 📁 Estructura del proyecto
```
login-web-flask/
├── app.py
├── gestor_datos.py
├── templates/
│   ├── login.html
│   ├── register.html
│   └── bienvenido.html
└── static/
    └── style.css
```

### 🗺️ Rutas disponibles
| Ruta | Método | Descripción |
|------|--------|-------------|
| `/` | GET | Redirige al login |
| `/login` | GET, POST | Inicio de sesión |
| `/register` | GET, POST | Registro de usuario |
| `/bienvenido` | GET | Dashboard post-login |

### ✨ Características
- Login con validación de credenciales
- Registro de nuevos usuarios guardado en JSON
- Dashboard con nombre de usuario, fecha de acceso y estado
- Animación de borde con gradiente cónico
- Diseño oscuro moderno con fuente Jost
- Manejo de errores en login y registro

### 👨‍💻 Sobre el autor
Soy Owen, estudiante de Ingeniería Informática en Perú, autodidacta apasionado por la programación y la ciberseguridad. Este es mi quinto proyecto personal antes de mi etapa universitaria, el primero con interfaz web usando Flask. Actualmente entrenando en TryHackMe con enfoque en análisis forense y seguridad defensiva.

---

## 🇬🇧 English

### 📋 Description
A web authentication app built with Python and Flask. Includes login and user registration with credentials stored in JSON, error handling, redirection, post-login dashboard and a modern dark UI with animated border effect.

### ⚙️ Technologies used
- **Python 3**
- **Flask** — web framework
- **HTML/CSS** — user interface
- **Jinja2** — template engine
- **JSON** — local database
- **HASH256** - passwords with hash256
- **Google Fonts (Jost)** — typography

### 🚀 How to install and use

**1. Clone the repository:**
```bash
git clone https://github.com/luninpotrer-png/login-web-flask.git
cd login-web-flask
```

**2. Install Flask:**
```bash
pip install flask
```

**3. Run the program:**
```bash
python app.py
```

**4. Open your browser at:**
```
http://127.0.0.1:5000
```

### 📁 Project structure
```
login-web-flask/
├── app.py
├── gestor_datos.py
├── templates/
│   ├── login.html
│   ├── register.html
│   └── bienvenido.html
└── static/
    └── style.css
```

### 🗺️ Available routes
| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Redirects to login |
| `/login` | GET, POST | User login |
| `/register` | GET, POST | User registration |
| `/bienvenido` | GET | Post-login dashboard |

### ✨ Features
- Login with credential validation
- New user registration saved to JSON
- Dashboard with username, access date and status
- Animated border with conic gradient
- Modern dark UI with Jost font
- Error handling for login and register

### 👨‍💻 About the author
I'm Owen, a Computer Engineering student from Peru, self-taught and passionate about programming and cybersecurity. This is my fifth personal project before my steep university, the first one with a web interface using Flask. Currently training on TryHackMe with a focus on digital forensics and defensive security.

---

> ⚠️ **Importante / Important:** Agrega `datos.json` al `.gitignore` antes de subir / Add `datos.json` to `.gitignore` before pushing


> ⭐ Si te gustó el proyecto no olvides dejar una estrella / If you liked the project don't forget to leave a star!

