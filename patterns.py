import threading

class DemoThread(threading.Thread):
    def __init__(self):
        super(DemoThread, self).__init__()
    def run(self):
        print("test")

#t1 = DemoThread()
#t2 = DemoThread()

#thread1.start() # This actually causes the thread to run
#thread2.start()
#thread1.join()  # This waits until the thread has completed
#thread2.join()
