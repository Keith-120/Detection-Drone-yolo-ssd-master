import sounddevice as sd
import queue
import json
import pyttsx3
import threading
from vosk import Model, KaldiRecognizer
from deep_translator import GoogleTranslator
from requests.exceptions import ReadTimeout, ConnectionError

MODEL_PATH = "model-en"
LANGUE_SOURCE = "en"
LANGUE_CIBLE = "fr"
SAMPLE_RATE = 16000

q = queue.Queue()

print("Chargement du modèle...")
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, SAMPLE_RATE)
recognizer.SetWords(True)

translator = GoogleTranslator(
    source=LANGUE_SOURCE,
    target=LANGUE_CIBLE,
    requests_kwargs={'timeout': 5}
)

# 🔊 Initialisation voix
engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('volume', 1)

print("✅ Modèle chargé")
print("🎤 Parlez maintenant...\n")


def speak_async(text):
    def run():
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run).start()


def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))


try:
    with sd.RawInputStream(
            samplerate=SAMPLE_RATE,
            blocksize=8000,
            dtype="int16",
            channels=1,
            callback=callback
    ):
        while True:
            data = q.get()

            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "").strip()

                if text:
                    print("🗣️ Detecté :", text)

                    try:
                        traduction = translator.translate(text)
                    except:
                        traduction = "Erreur traduction"

                    print("➡️", traduction)
                    print("-" * 30)

                    # 🔊 Lecture audio
                    speak_async(traduction)

except KeyboardInterrupt:
    print("\n🛑 Arrêté")
