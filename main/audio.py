import pyaudio
import wave
import keyboard

class AudioRecorder:
    def __init__(self):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024
        self.output_filename = "human.wav"
        self.audio = pyaudio.PyAudio()
        

    def start_recording(self):
        self.frames = []
        stream = self.audio.open(format=self.FORMAT,
                                 channels=self.CHANNELS,
                                 rate=self.RATE,
                                 input=True,
                                 frames_per_buffer=self.CHUNK)
        print("Recording started...")

        while True:
            data = stream.read(self.CHUNK)
            self.frames.append(data)
            if keyboard.is_pressed('space'):
                print('You Pressed Space Key!')
                break

        print("Recording finished.")
        stream.stop_stream()
        stream.close()
        self.save_recording()

    def save_recording(self):
        wave_file = wave.open(self.output_filename, 'wb')
        wave_file.setnchannels(self.CHANNELS)
        wave_file.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        wave_file.setframerate(self.RATE)
        wave_file.writeframes(b''.join(self.frames))
        wave_file.close()

# Usage example:
