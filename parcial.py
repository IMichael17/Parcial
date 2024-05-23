import os
from flask import Flask, send_file, request, render_template

datos = [
    {
        "nombre": "Juan Pérez",
        "contacto": "123456789",
        "email": "juan@example.com",
        "mensaje": "Hola, ¿cómo estás?"
    },
    {
        "nombre": "María García",
        "contacto": "987654321",
        "email": "maria@example.com",
        "mensaje": "Necesito más información"
    },
    {
        "nombre": "Pedro Gómez",
        "contacto": "456789123",
        "email": "pedro@example.com",
        "mensaje": "Gracias por tu ayuda"
    },
    {
        "nombre": "Ana Sánchez",
        "contacto": "789123456",
        "email": "ana@example.com",
        "mensaje": "Me interesa tu servicio"
    },
    {
        "nombre": "Luis Ramírez",
        "contacto": "321654987",
        "email": "luis@example.com",
        "mensaje": "Tengo una pregunta"
    }
]
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def formulario():
    # if request.method == 'POST':
    #     nombre = request.form['nombre']
    #     contacto = request.form['contacto']
    #     email = request.form['email']
    #     mensaje = request.form['mensaje']
    #     print(f'nombre ingresado: {nombre}')
    #     datos[{'nombre':nombre, 'contacto':contacto, 'email':email, 'mensaje':mensaje}]
    return send_file('formulario.html')

@app.route('/mostrar')
def mostrar():
    return render_template('mostrar.html',datos=datos)

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
