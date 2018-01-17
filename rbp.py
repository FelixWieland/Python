import threading
import os
import ctypes
import requests

#---------------------------------
class DemoThread(threading.Thread):
     def __init__(self):
         super(DemoThread, self).__init__()
     def run(self):
        print("Demo")

def main():
    t1 = DemoThread()
    t2 = DemoThread()

    #thread1.start() # This actually causes the thread to run
    #thread2.start()
    #thread1.join()  # This waits until the thread has completed
    #thread2.join()
#---------------------------------
if __name__ == '__main__':
    main()
