# 🧮 Calculadora Web con Flask

Esta es una aplicación web de calculadora construida con **Flask (Python)**, **HTML**, **CSS** y **JavaScript**. Permite realizar operaciones básicas entre dos números y ofrece una experiencia de usuario interactiva con sonidos y una interfaz amigable.

---

## 🚀 Características

- ✅ Operaciones: suma, resta, multiplicación y división.
- ✅ Diseño responsivo con estilos suaves.
- ✅ Botones numéricos con sonido e interacción visual.
- ✅ Inserción automática de números en el input seleccionado.
- ✅ Muestra del resultado con posibilidad de encadenar operaciones.
- ✅ Manejo de errores como división por cero y entradas no válidas.

---

## 🛠️ Tecnologías utilizadas

- **Python 3**
- **Flask**
- **HTML5**
- **CSS3**
- **JavaScript**
- **Audio** para efectos al presionar botones

---

## 📁 Estructura del proyecto

```
/calculadora-flask
│
├── app.py                      # Lógica del servidor Flask
├── templates/
│   └── index.html              # Plantilla HTML principal
├── static/
│   ├── style.css               # Hoja de estilos principal
│   └── sounds/
│       └── teclas-especiales.mp3  # Sonido de los botones numéricos
└── README.md                   # Este archivo
```

---

## ⚙️ Instalación y ejecución

### 1. Clona el repositorio

```bash
git clone https://github.com/AlexNR0/Calculadora-Python-Flask-
cd Calculadora-Python-Flask-


### 2. (Opcional) Crea un entorno virtual

```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate
```

### 3. Instala Flask

```bash
pip install Flask
pip install -r requirements.txt
```

### 4. Ejecuta la aplicación

```bash
python app.py
```

Luego abre tu navegador y visita:  
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Uso

1. Ingresa un número en el primer campo.
2. Ingresa el segundo número.
3. Selecciona la operación (+, -, *, /).
4. Haz clic en “Operar”.
5. También puedes usar los botones numéricos para insertar valores en los campos activos.
6. El resultado aparecerá debajo y se cargará en el primer campo para seguir operando.

---

## 💡 Posibles mejoras

- Añadir operaciones científicas (potencia, raíz, etc.).
- Historial de operaciones.
- Soporte para teclado físico.
- Interfaz adaptable a móviles.
- Validación de inputs en tiempo real.

---

## 📄 Licencia

Este proyecto es de código abierto y puede ser utilizado libremente con fines educativos y personales.

---

## 👤 Autor

**AlexNR**
🔗 GitHub: [https://github.com/AlexNR0](https://github.com/AlexNR0)
🔗 LinkedIn: [https://www.linkedin.com/in/alejandro-jim%C3%A9nez-d%C3%ADaz-513043345/](https://www.linkedin.com/in/alejandro-jim%C3%A9nez-d%C3%ADaz-513043345/)
