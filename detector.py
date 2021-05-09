from announcer import Announcer
import sys
import time
from collections import Counter
import argparse

#def is_line_ok(line):
#    return not "without_mask" in line

WITHOUT_MASK = "without_mask"
WITH_MASK = "with_mask"
MASK_WORN_INCORRECTLY = "incorrectly"
KEYWORDS = [MASK_WORN_INCORRECTLY, WITHOUT_MASK, WITH_MASK] # Announcement priority

class Detector:
    def __init__(self, time_interval, check_threshold, announcers):
        self.time_interval = time_interval
        self.check_threshold = check_threshold
        self.announcers = announcers
        self.counter = Counter()
        self.base_time = time.time()
    
    def watch(self):
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
                        break # Only play the first announcement if mixed
                self.counter = Counter()
                base_time = time.time()


    def check(self,line):
        self.count(line)
        if time.time() - self.base_time > self.time_interval:
            total = sum([self.counter[keyword] for keyword in KEYWORDS])
            if total == 0:
                return
            for keyword in KEYWORDS:      
                ratio = self.counter[keyword] / total
                if ratio > self.check_threshold and keyword in self.announcers.keys():
                    self.announcers[keyword].announce()
                    break # Only play the first announcement if mixed
            self.counter = Counter()
            self.base_time = time.time()


    def count(self, line):
        for keyword in KEYWORDS:
            if keyword in line:
                self.counter[keyword] += 1


def main():
    parser = argparse.ArgumentParser("Parse stdin, and make annnouncements based on that.")
    parser.add_argument('--nomaskaudiofile', type=str, default='', help="Audio_file_for_without_mask")
    parser.add_argument('--wrongmaskaudiofile', type=str, default='', help="Audio_file_for_mask_worn_incorrectly")
    parser.add_argument('--detect-interval', default=2.0, type=float, help='In seconds. For which the detector counts the result.')
    parser.add_argument('--detect-threshold', default=0.0, type=float, help='In [0, 1]. If the ratio is above this value, announcement will be made')
    parser.add_argument('--announce-interval', default=5.0, type=float, help='In seconds. The announcer refrain from announce after announcing for this period of time')
    args = parser.parse_args()
    d = Detector(time_interval= args.detect_interval, check_threshold=args.detect_threshold,
    announcers={WITHOUT_MASK: Announcer(args.nomaskaudiofile, time_interval=args.announce_interval), MASK_WORN_INCORRECTLY: Announcer(args.wrongmaskaudiofile, time_interval=args.announce_interval)})
    d.watch()

if __name__ == '__main__':
    main()
