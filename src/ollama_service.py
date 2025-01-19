import ollama

SYSTEM = ""
modelo = 'llama3.1:latest'

def llamar_ollama(texto, system_content=SYSTEM):
    """
    Función para llamar a Ollama usando su librería oficial
    
    Args:
        texto (str): Texto de entrada para procesar
        modelo (str, optional): Modelo de Ollama a usar. Defaults a 'llama3.1:latest'.
    
    Returns:
        str: Respuesta generada por Ollama
    """
    try:
        # Preparar los parámetros de la llamada
        parametros = {
            'model': modelo,
            'messages': [
                # Mensaje de sistema opcional
                {'role': 'system', 'content': system_content},
                {'role': 'user', 'content': texto}
            ]
        }
        
        # Generar respuesta
        respuesta = ollama.chat(**parametros)
        
        # Devolver el contenido de la respuesta
        return respuesta['message']['content']
    
    except Exception as e:
        print(f"Error al llamar a Ollama: {e}")
        return None
