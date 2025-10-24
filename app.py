from flask import Flask
import urllib.request
import urllib.error

app = Flask(__name__)

# Configuración del servicio al que deseas llamar
URL_SERVICIO_EXTERNO = "http://mi-servicio.nicolas-sierra-dev.svc.cluster.local:4000"

@app.route('/', methods=['GET'])
def hello_world():
    # 1. Mensaje base de tu aplicación
    respuesta_base = 'Hola Mundo en Practica'
    # 2. Variable para almacenar la respuesta del servicio externo
    respuesta_externa = ""
    try:
        # Realizar la solicitud GET al servicio externo (con un timeout)
        with urllib.request.urlopen(URL_SERVICIO_EXTERNO, timeout=5) as response:
            
            # Decodificar el contenido de la respuesta a un string
            contenido_servicio = response.read().decode('utf-8').strip()
            
            # Construir el mensaje de éxito
            respuesta_externa = (
                "\n--- Servicio Externo (Éxito) ---\n"
                f"URL: {URL_SERVICIO_EXTERNO}\n"
                f"Código HTTP: {response.status}\n"
                f"Contenido: {contenido_servicio}"
            )

    except urllib.error.URLError as e:
        # Manejar errores de red, DNS o HTTP (4xx/5xx)
        error_msg = f"Error: {e.reason}" if hasattr(e, 'reason') else str(e)
        respuesta_externa = (
            "\n--- Servicio Externo (Error de Conexión) ---\n"
            f"No se pudo conectar a {URL_SERVICIO_EXTERNO}\n"
            f"Mensaje de error: {error_msg}"
        )
    except Exception as e:
        # Manejar otros errores (ej. timeout)
        respuesta_externa = (
            "\n--- Servicio Externo (Otro Error) ---\n"
            f"Ocurrió un error inesperado al llamar al servicio: {str(e)}"
        )

    # 3. Concatenar y retornar la respuesta final
    respuesta_final = respuesta_base + respuesta_externa
    
    # Retorna la respuesta concatenada con el código 200
    return respuesta_final, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
