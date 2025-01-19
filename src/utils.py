from flask import request, jsonify
from src.ollama_service import llamar_ollama

def process_ollama_request(system_prompt):
    """
    Generic function to process Ollama requests with a given system prompt.
    
    Args:
        system_prompt (str): The system prompt to use with Ollama
    
    Returns:
        tuple: JSON response and status code
    """
    # Verificar que se envió JSON
    if not request.is_json:
        return jsonify({"error": "Debe enviar un JSON"}), 400
    
    # Obtener el texto del request con manejo de errores
    texto_recibido = request.json.get('text', '')
    
    # Llamar a Ollama con el sistema de prompt
    texto_procesado = llamar_ollama(texto_recibido, system_prompt)
    
    # Devolver el texto procesado en formato JSON
    return jsonify({
        "texto_original": texto_recibido,
        "texto_procesado": texto_procesado
    }), 200
