import edge_tts
from pygame import mixer

class edge2s:
    """Text to speech using Edge TTS API"""
    def __init__(self):
        pass

    def speak(self, text,gender="Male"):
        """
        text = str : text to speech
        gender = str : Male , Female    
        """
        if gender == "Male":
            VOICE = "th-TH-NiwatNeural"
        elif gender == "Female":
            VOICE = "th-TH-PremwadeeNeural"
        TEXT = text   
        communicate = edge_tts.Communicate(TEXT, VOICE,pitch="-15Hz")
        communicate.save_sync("AI.mp3")
        self.mixer()
    def mixer(self):
        mixer.init()
        mixer.music.load("AI.mp3")
        mixer.music.play()
        while mixer.music.get_busy():
            pass
        mixer.quit()


