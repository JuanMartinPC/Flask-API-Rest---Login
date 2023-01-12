from flask import Flask, jsonify, request
from sqlinterface import Conexion 
import os


# La api está diseñada para funcionar con una base de datos 
# que tenga una columna "Usuario" y una columna "Contraseña".

# Usuario y Contraseña son los parametros que hay que usar para la consulta.
# Por ejemplo data?Usuario=<<nombre del usuario>>&Contraseña=<<contraseña de ese usuario>>


app = Flask(__name__)

def comprobacion(x,y):
    if x==y:
        return True
    else:
        return False


@app.route("/data", methods=["GET"])
def message():
    
    usuario = request.args.get('Usuario')
    pswrd = request.args.get('Contraseña')
    
    # Acá van los nombres de la base de datos y la tabla
    conexion = Conexion('tabla_api_juego', 'Login')

    data = conexion.consulta('select {} from {} where {}="{}"'.format('Contraseña', conexion.tabla, 'Usuario', usuario))
    nueva_data = [x[0] for x in data]
    salida = {'verificacion':comprobacion(pswrd,nueva_data[0])}
    return jsonify(salida)

if __name__=='__main__':

    try:
        app.run(host='127.0.0.1',port=8000)

    except Exception as e:
        print(e)
        print("Setear variables de entorno ip y puerto")