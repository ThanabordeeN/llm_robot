import pyaudio
import wave
import audioop
import time
class AudioRecorder:
    def __init__(self):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024
        self.audio = pyaudio.PyAudio()
        self.threshold = 1000  # Set the threshold

    def start_recording(self):
        self.frames = []
        while True:
            stream = self.audio.open(format=self.FORMAT,
                                    channels=self.CHANNELS,
                                    rate=self.RATE,
                                    input=True,
                                    frames_per_buffer=self.CHUNK)
            print("Recording started...")
            start_time = None

            while True:
                data = stream.read(self.CHUNK)
                self.frames.append(data)
                
                # Calculate the RMS of the audio data
                rms = audioop.rms(data, 2)  # Here '2' is the width of the sample

                # Check if the RMS exceeds the threshold
                if rms > self.threshold:
                    print("Sound detected!")
                    start_time = None  # Reset the start time
                elif rms < self.threshold:
                    if start_time is None:
                        start_time = time.time()  # Start the timer
                    elif time.time() - start_time > 2:  # If 2 seconds have passed
                        print("No sound detected for 2 seconds, stopping...")
                        print("Recording finished.")
                        stream.stop_stream()
                        stream.close()
                        recording_length = len(self.frames) * self.CHUNK / self.RATE
                        print(f"Recording length: {recording_length:.2f} seconds")
                        if recording_length > 2.5:
                            self.save_recording('human.wav')
                        else:
                            self.save_recording('no_detect.wav')
                        self.frames = []
                        break
                

                



    def save_recording(self, output_filename=None):
        wave_file = wave.open(output_filename, 'wb')
        wave_file.setnchannels(self.CHANNELS)
        wave_file.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        wave_file.setframerate(self.RATE)
        wave_file.writeframes(b''.join(self.frames))
        wave_file.close()

# Usage example:
audio = AudioRecorder()
audio.start_recording()
