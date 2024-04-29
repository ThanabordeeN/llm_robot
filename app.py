from main.s2t import speech_recognition
from main.llm import Robot
from main.audio import AudioRecorder
from main.t2s import AI_Robot
import time
from pygame import mixer
import os

class AI_Robot_App:
    def __init__(self):
        self.robot = Robot()
        self.robot_speak = AI_Robot()
        self.audio = AudioRecorder()
        self.s2t = speech_recognition()

    def run(self):
        while True:
            self.audio.start_recording()
            self.audio.save_recording()
            text = self.s2t.get_text("human.wav")
            print("You said: ", text)
            response = self.robot.chat(text)
            bot_speak = response
            print("Robot said: ", bot_speak)
            self.robot_speak.generate_sound(bot_speak)
            mixer.init()
            mixer.music.load("AI.wav")
            mixer.music.play()
            while mixer.music.get_busy():  # wait for music to finish playing
                time.sleep(1)
            mixer.quit()
            os.remove("AI.wav")
            os.remove("human.wav")

if __name__ == "__main__":
    app = AI_Robot_App()
    app.run()
