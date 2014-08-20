import os
import threading

class SoundThread(threading.Thread):
    def __init__(self,wav_file):
        super(SoundThread,self).__init__()
        self.file = wav_file

    def run(self):
        os.system('aplay -q %s' % self.file)

class Sound():
    def __init__(self,wav_file):
        """ setup to use analog output"""
        os.system('amixer cset numid=3 1')
        os.system('amixer sset PCM Playback 85%')
        self.file = wav_file

    def play(self):
        thread=SoundThread(self.file)
        thread.start()
        thread.join()
        
if __name__ == '__main__':
    thread=SoundThread("1.wav")
    thread.start()
    thread.join()
