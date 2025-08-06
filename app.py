import os
from flask import Flask, redirect, render_template, request, session, url_for
from dotenv import load_dotenv

load_dotenv()

app = Flask (__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')

@app.route('/', methods = ['GET', 'POST'])
def calculadora():
    resultado = None
    if request.method == 'POST':

        a = float(request.form['a'])
        b = float(request.form['b'])
        operador = request.form['operador']
        
        if operador == '+':
            resultado = a + b
        elif operador == '-':
            resultado = a - b
        elif operador == '*':
            resultado = a * b
        elif operador == '/':
            resultado = a / b if b != 0 else 'Error: No se puede dividir por cero'

        session ["ultimo_resultado"] = resultado
        return redirect(url_for('calculadora'))
    
    resultado = session.get("ultimo_resultado", None)
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)