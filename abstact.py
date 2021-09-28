


from abc import ABC, abstractmethod

class hello(ABC):
    @abstractmethod
    def method(Self):
        return 0


class hi(hello):
    n = 10
    def __init__(self):
        self.hello = 20

    def method(Self):
        print("hello word")


n1 = hi()


