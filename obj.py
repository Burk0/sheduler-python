import time

class Object(object):
    def __init__(self,id,interval):
        self.interval=interval
        self.id = id
        self.time=time.time()

        # print(self.time)




    def getImage(self):
        print("som objekt " + str(self.id) + " s casom " + time.strftime("%H:%M:%S", time.gmtime(time.time())))



    def getKey(self):
        return self.interval