from announcer import Announcer
import sys
import time

def is_line_ok(line):
    return not "without_mask" in line

class Detector:
    def __init__(self, time_interval, check_threshold, announcer):
        self.time_interval = time_interval
        self.check_threshold = check_threshold
        self.announcer = announcer
    
    def watch(self):
        n_ok = 0
        n_wrong = 0
        base_time = time.time()
        for line in sys.stdin:
            print(line, end="")
            if is_line_ok(line):
                n_ok += 1
            else:
                n_wrong += 1
            if time.time() - base_time > self.time_interval:
                ratio = n_wrong / (n_ok + n_wrong)
                if ratio > self.check_threshold:
                    self.announcer.announce()
                n_ok = 0
                n_wrong = 0
                base_time = time.time()

def main():
    d = Detector(time_interval=2, check_threshold=0.5, announcer=Announcer(sys.argv[1], time_interval=5))
    d.watch()

if __name__ == '__main__':
    main()
