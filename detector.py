import sys
import time
def announce():
    print("Please wear a mask")
    pass

def is_line_ok(line):
    return not "without_mask" in line

class Detector:
    def __init__(self, time_interval, check_threshold):
        self.time_interval = time_interval
        self.check_threshold = check_threshold
    
    def watch(self):
        n_ok = 0
        n_wrong = 0
        base_time = time.time()
        for line in sys.stdin:
            if is_line_ok(line):
                n_ok += 1
            else:
                n_wrong += 1
            if time.time() - base_time > self.time_interval:
                ratio = n_wrong / (n_ok + n_wrong)
                if ratio > self.check_threshold:
                    announce()
                n_ok = 0
                n_wrong = 0
                base_time = time.time()

def main():
    CHECK_THRESHOLD = 0.5
    TIME_INTERVAL = 5.0
    d = Detector(TIME_INTERVAL, CHECK_THRESHOLD)
    d.watch()





    

if __name__ == '__main__':
    main()
