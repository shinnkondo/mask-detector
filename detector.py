from announcer import Announcer
import sys
import time
from collections import Counter

def is_line_ok(line):
    return not "without_mask" in line

WITHOUT_MASK = "without_mask"
WITH_MASK = "with_mask"
MASK_WORN_INCORRECTLY = "incorrectly"
KEYWORDS = [WITHOUT_MASK, MASK_WORN_INCORRECTLY, WITH_MASK]

class Detector:
    def __init__(self, time_interval, check_threshold, announcers):
        self.time_interval = time_interval
        self.check_threshold = check_threshold
        self.announcers = announcers
        self.counter = Counter()
    
    def watch(self):
        n_ok = 0
        n_wrong = 0
        base_time = time.time()
        for line in sys.stdin:
            print(line, end="")
            self.count(line)
            if time.time() - base_time > self.time_interval:
                total = sum([self.counter[keyword] for keyword in KEYWORDS])
                if total == 0:
                    continue
                for keyword in KEYWORDS:      
                    ratio = self.counter[keyword] / total
                    if ratio > self.check_threshold and keyword in self.announcers.keys():
                        self.announcers[keyword].announce()
                self.counter = Counter()
                base_time = time.time()

    def count(self, line):
        for keyword in KEYWORDS:
            if keyword in line:
                self.counter[keyword] += 1


def main():
    d = Detector(time_interval=2, check_threshold=0.3, announcers={WITHOUT_MASK: Announcer(sys.argv[1], time_interval=3), MASK_WORN_INCORRECTLY: Announcer(sys.argv[2], time_interval=3)})
    d.watch()

if __name__ == '__main__':
    main()
