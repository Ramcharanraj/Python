"""
Author : K.Ram chandran
Date : 21-12-2021
Time : 1 PM
Title : Stop Watch Program

"""

import time
def time_convert(sec):
    mins = sec // 60
   
    hours = mins // 60
   

    print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))

input("Press Enter to start")
start_time = time.time()
input("Press Enter to stop")
end_time = time.time()
time_lapsed = end_time - start_time
time_convert(round(time_lapsed))
