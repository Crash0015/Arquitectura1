from flask import Flask, jsonify

app = Flask(__name__)

# Página principal para redirigir a los usuarios
@app.route('/')
def index():
    return """
    <h1>Bienvenido a mi API REST</h1>
    <p>Endpoints disponibles:</p>
    <ul>
        <li><a href="/api/hola">/api/hola</a> - Devuelve un saludo.</li>
        <li><a href="/swagger.json">/swagger.json</a> - Documentación de la API.</li>
    </ul>
    """

# Endpoint de la API REST
@app.route('/api/hola', methods=['GET'])
def hola_mundo():
    return jsonify({'mensaje': '¡Hola Mundo desde una API REST con Flask y Docker!'})

# Endpoint para la documentación manual (Swagger)
@app.route('/swagger.json', methods=['GET'])
def swagger():
    return jsonify({
        "swagger": "2.0",
        "info": {
            "title": "Mi API REST",
            "description": "Documentación de la API REST.",
            "version": "1.0.0"
        },
        "paths": {
            "/api/hola": {
                "get": {
                    "summary": "Devuelve un saludo",
                    "responses": {
                        "200": {
                            "description": "Respuesta exitosa"
                        }
                    }
                }
            }
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
