from flask import Flask
from flask_cors import CORS
from src.urls import rutas

def crear_app():
    """
    Función para crear y configurar la aplicación Flask
    
    Returns:
        Flask: Aplicación Flask configurada
    """
    app = Flask(__name__)

    # Configurar CORS
    CORS(app, resources={r"/*": {"origins": "*"}})
    
    # Registrar las rutas del Blueprint
    app.register_blueprint(rutas)
    
    return app

def main():
    """
    Función principal para ejecutar el servidor
    """
    app = crear_app()
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
