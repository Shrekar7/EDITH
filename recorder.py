import sounddevice
import speech_recognition as sr
from scipy.io.wavfile import write
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

fs=4410
second=takeCommand()
print("Recording...\n")
record_voice=sounddevice.rec(int(second * fs),samplerate= fs,channels=2)
sounddevice.wait()
write("out.wav",fs,record_voice)
print("Finished...\n please check it...")