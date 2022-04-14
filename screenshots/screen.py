""" Screenshot code"""

import time

class MyTimer():
    """ Start """
    def __init__(self):
        """ Self """
        self.unit   = ["year(s)","month(s)","day(s)","hour(s)","minute(s)","second(s)"]
        self.prompt = "Haven't started yet. "
        self.lasted = []
        self.begin  = 0
        self.end    = 0

    def __str__(self):
        return self.prompt
    __repr__ = __str__

    def start(self):
        """ Start """
        self.begin = time.localtime()
        print("Please use stop() to stop timing.")
        print("Start timing.")

    def stop(self):
        """ Stop """
        if not self.begin:
            print("Please use start() to start timing.")
        else:
            self.end = time.localtime()
            self._calc()
            print("Stop timing.")

    def _calc(self):
        """ Inner method """
        self.lasted = []
        self.prompt = "The time interval is "
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + " " + self.unit[index] + "."
        print(self.prompt)
        self.begin = 0
        self.end   = 0

## Result Example

