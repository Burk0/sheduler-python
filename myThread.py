#!/usr/bin/python3

import threading
import time
import sys

class myThread(threading.Thread):
    def __init__(self,my_dict):
        threading.Thread.__init__(self)
        self.my_dict=my_dict

    def run(self):
        while(True):
            print("Vykonavam shed")
            minTime = 80000000000000
            now = time.time()
            for key, value in self.my_dict.items():
                # print("vykonavam sa " + str(value.time)+ " " + str(now))
                if (value.time <= now):
                    print("nasiel som")
                    t = threading.Thread(target=value.getImage, )
                    t.start()

                    value.time = now + value.interval
            # print("Aktivne " ,threading.active_count())
            for key, value in self.my_dict.items():
                if (value.time - now < minTime):
                    # print( str(value.time) + " " + str(now))
                    minTime = value.time - now
            # mainThread.sleep(minTime)
            print("MINTIME " + str(minTime))
            time.sleep(minTime)