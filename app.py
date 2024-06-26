import os
from flask import Flask, request, render_template

app = Flask(__name__)

datos = [
    
    {
        "nombre": "Michael Ayala",
        "contacto": "987654321",
        "email": "mario@example.com",
        "mensaje": "Necesito más información"
    },
    {
        "nombre": "Messi Ayala",
        "contacto": "789123456",
        "email": "Messi@example.com",
        "mensaje": "Me interesa tu servicio"
    }
    
]

@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contacto = request.form['contacto']
        email = request.form['email']
        mensaje = request.form['mensaje']
        datos.append({'nombre': nombre, 'contacto': contacto, 'email': email, 'mensaje': mensaje})
    return render_template('formulario.html')

@app.route('/mostrar')
def mostrar():
    return render_template('mostrar.html', datos=datos)

def main():
    app.run(port=int(os.environ.get('PORT', 5000)))

if __name__ == "__main__":
    main()
