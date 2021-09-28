from time import sleep
from threading import *

class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)


t = hello()
k = hi()

t.start()
k.start()
