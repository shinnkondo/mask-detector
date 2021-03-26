import subprocess
class Announcer:
    def __init__(self, file_path):
        self.file_path = file_path
        pass

    def announce(self):
        subprocess.run(["play", self.file_path], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print("Please wear a mask")