import numpy as np
import pyaudio
import time
import librosa
import warnings
warnings.filterwarnings("ignore")

class AudioHandler(object):
    def __init__(self):
        self.FORMAT = pyaudio.paFloat32
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024 * 2
        self.p = None
        self.stream = None

    def start(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  output=False,
                                  stream_callback=self.callback,
                                  frames_per_buffer=self.CHUNK)

    def stop(self):
        self.stream.close()
        self.p.terminate()

    def callback(self, in_data, frame_count, time_info, flag):
        numpy_array = np.frombuffer(in_data, dtype=np.float32)
        #librosa.feature.mfcc(numpy_array)
        print("Low Low: " + str(librosa.feature.spectral_centroid(numpy_array)[0,0]/100))
        print("Mid Low: " + str(librosa.feature.spectral_centroid(numpy_array)[0,1]))
        print("Mid: " + str(librosa.feature.spectral_centroid(numpy_array)[0,2]))
        print("Mid High: " + str(librosa.feature.spectral_centroid(numpy_array)[0,3]))
        print("High High: " + str(librosa.feature.spectral_centroid(numpy_array)[0,4]))
        
        return None, pyaudio.paContinue

    def mainloop(self):
        while (self.stream.is_active()): # if using button you can set self.stream to 0 (self.stream = 0), otherwise you can use a stop condition
            time.sleep(30.0) #how long to keep reading audio



audio = AudioHandler()
audio.start()     # open the the stream
audio.mainloop()  # main operations with librosa
audio.stop()
