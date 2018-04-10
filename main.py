import time

import obj
from threading import Thread, active_count
from myThread import myThread
from operator import itemgetter, attrgetter
from collections import OrderedDict

def main():
    thread_list = []
    my_dict = {}
    my_dict[0] = obj.Object(0,20)
    my_dict[1] = obj.Object(1, 50)
    my_dict[2] = obj.Object(2, 70)
    my_dict[3] = obj.Object(3, 40)

    # print(my_dict)
    #prve spustenie
    for key,value in my_dict.items():
        t = Thread(target=value.getImage,)
        t.start()
        # print(active_count())
        thread_list.append(t)
        value.time+=value.interval


    mainThread = myThread(my_dict)
    mainThread.start()

    # print(active_count())

    # for t in thread_list:
    #     t.join()

    # print(active_count())
#
#     getShotThread = Thread(target=shed(my_dict))
#     getShotThread.start()
#
#
# # def shed(my_dict):
# #     threadList = []
# #     print("Vykonavam shed")
# #     minTime = 80000000000000
# #     now = time.time()
# #     for key,value in my_dict.items():
# #         if(value.time == now):
# #             t = Thread(target=value.getImage,)
# #             t.start()
# #
# #             value.time=now+value.interval
# #     for key,value in my_dict.items():
# #         if(value.time - now < minTime):
# #             minTime = value.time - now
# #     # mainThread.sleep(minTime)
# #     time.sleep(minTime)

if __name__ == '__main__':
	main()