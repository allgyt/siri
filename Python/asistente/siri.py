import speech_recognition as sr
import pyttsx3
import pywhatkit

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
