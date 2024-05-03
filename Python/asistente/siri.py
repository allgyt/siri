#se importan Speech para el recnocimiento  acompañado de spacy para
# mejorar el analisis de voz
#pyttsx3 para las respuesta por voz
#Es para la reproduccion de los videos y tambien ayuda a enviar mensajes por whatsapp
import speech_recognition as sr
import pyttsx3
import pywhatkit
#librearia para la web
#import spacy
#libreria para poder entrar al sistema operativo y generar carpetas por ahora
import os

#librerias para codificar
#import pygments as highlight
#from pygments.lexers  import PythonLexer
#from pygments.formatters import TerminalFormatter



#nlp = spacy.load("es_core_news_sm")

# funcion con validaciones para el reconocimiento de voz
def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando comando...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("Dijiste:", command)
        return command
    except sr.UnknownValueError:
        print("Lo siento, no pude entender el audio")
        return None
    except sr.RequestError as e:
        print(f"No se pudieron obtener resultados; {e}")
        return None

#funcion para responder por medio de la voz aquello que se aloje en la parte del speech(reconocimiento)
def respond_with_voice(response_text):
    engine = pyttsx3.init()
    engine.say(response_text)
    engine.runAndWait()
#esta es la parte del spacy para mejorar el analisis de voz
#def analyze_command(command):
    #doc = nlp(command)
    #return "comando analizado" 
    
#aqui inicia la parte del os donde se gestiona la parte de los archivos
#es donde se crea archivo
def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        return f"Carpeta '{folder_name}' creada exitosamente."
    except FileExistsError:
        return f"Carpeta '{folder_name}' ya existe."

#
def list_files(folder_path):
    try: 
        files = os.listdir(folder_path)
        if files:
            return f"Archivos en '{folder_path}': {','.join(files)}"
        else:
            return f"No hay archivos en '{folder_path}'"
    except FileNotFoundError:
        return f"Carpeta '{folder_path}' no encontrada."
    
#Esta es para eliminar carpetas
def delete_folder(folder_name):
    try:
        os.mkdir(folder_name)
        return f"Carpeta '{folder_name}' eliminada exitosamente."   
    except FileNotFoundError:
        return f"Carpeta '{folder_name}' no encontrada"
    except OSError as e:
        return f"Carpeta 'no se pudo eliminar la carpeta '{folder_name}':{e}"

#aqui voy a generar la parte donde codifique por comandos


#def generate_code_snippet(language, intent):
    # Aquí puedes personalizar y expandir para más lenguajes y comandos
#    if language.lower() == "python":
#        if intent.lower() == "hola mundo":
#            code = 'print("Hola, mundo")'
#            return code
#        elif intent.lower() == "ciclo for":
#            code = '''for i in range(5):
#    print(i)'''
#            return code
#        else:
#            return "Lo siento, no entiendo la solicitud."

 #   else:
 #       return "Lo siento, no puedo generar código para ese lenguaje."

#if __name__ == "__main__":
#    while True:
#        user_command = listen_for_command()
#        if "detente" in user_command:
 #           print("Hasta luego.")
 #           break

#        response = generate_code_snippet("python", user_command)
#        print("Código generado:")
#        print(highlight(response, PythonLexer(), TerminalFormatter()))

#        respond_with_voice(response)




#aqui se alojan las respuestas, seria practicamente un diccionario de respuestas para el asistente
#se emplearon if para poder responder y planificar 
def respond_to_command(command):
    if command is None:
        return "Lo siento, no pude entender tu comando."

    if "hola" in command:
        return "¡Hola! ¿En qué puedo ayudarte?"
    elif "reproduce" in command:
        song = command.replace("reproduce", "")
        pywhatkit.playonyt(song)
        return f"Reproduciendo {song} en YouTube."
    elif "busca" in command:
        search_query = command.replace("busca", "")
        pywhatkit.search(search_query)
        return f"Buscando en la web: {search_query}"
    else:
        return "No estoy seguro de cómo responder a eso."

if __name__ == "__main__":
    while True:
        user_command = listen_for_command()
        response = respond_to_command(user_command)
        print("Asistente:", response)
        respond_with_voice(response)
