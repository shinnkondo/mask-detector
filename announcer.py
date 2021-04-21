import subprocess
import time
class Announcer:
    def __init__(self, file_path, time_interval=5):
        self.file_path = file_path
        self.interval = time_interval
        self.last_played = 0
        pass

    def  announce(self):
        if time.time() - self.last_played < self.interval:
            return
        print("Annoucement: Please wear a mask")

        subprocess.Popen(["play", self.file_path], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        self.last_played = time.time()
        