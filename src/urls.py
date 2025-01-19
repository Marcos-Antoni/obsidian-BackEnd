from flask import Blueprint, request, jsonify

from src.prompt_templates import SYSTEM_SEPARATOR, SYSTEM_CORRECTOR
from src.utils import process_ollama_request

# Crear un Blueprint para las rutas
rutas = Blueprint('rutas', __name__)

@rutas.route('/separador', methods=['POST'])
def separador():
    """
    Ruta que recibe un texto y devuelve texto separado en JSON
    
    Returns:
        JSON: Objeto con texto separado
    """
    return process_ollama_request(SYSTEM_SEPARATOR)

@rutas.route('/corrector', methods=['POST'])
def corrector():
    """
    Ruta que recibe un texto y devuelve texto corregido en JSON
    
    Returns:
        JSON: Objeto con texto corregido
    """
    return process_ollama_request(SYSTEM_CORRECTOR)
