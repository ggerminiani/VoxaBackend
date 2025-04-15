import speech_recognition as sr


def transcrever_audio(caminho_audio):
    recognizer = sr.Recognizer()

    with sr.AudioFile(caminho_audio) as source:
        audio_data = recognizer.record(source)
        texto = recognizer.recognize_google(audio_data, language='pt-BR')  # Português-BR
        return texto
