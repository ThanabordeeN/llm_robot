from main.s2t import speech_recognition 
from main.llm import Robot
from main.audio import AudioRecorder
from main.t2s.edge2txt import edge2s

class AI_Robot_App:
    def __init__(self):
        self.robot = Robot()
        self.audio = AudioRecorder()
        self.s2t = speech_recognition()
        self.e2s = edge2s()

    def run(self):
        while True:
            self.audio.start_recording()
            text = self.s2t.get_text("human.wav")
            print("You said: ", text)
            response = self.robot.gorq(text) #Change to self.rotbot.ollama() if you want to use Ollama model
            bot_speak = response
            bot_speak = bot_speak.replace("*", "")
            print("Robot said: ", bot_speak)
            self.e2s.speak(bot_speak,gender="Female")

if __name__ == "__main__":
    app = AI_Robot_App()
    app.run()
