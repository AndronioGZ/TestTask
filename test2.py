#==========
#Вопрос 2:
#==========

"""В первом случае использовал list, во втором - deque. При использовании list много времени уходит на удаление первого элемента списка, тогда как в двусторонней очереди отсутствует этот недостаток."""

from collections import deque

BUF_SIZE = 3

class FiFoDeque:
    __buf = deque()
    
    def write(self, message):
        if(self.__buf == None):
            print("ERRinit")
            return -1
        if(len(self.__buf) == BUF_SIZE):
            print("ERRfull")
            return -2
        self.__buf.append(message)
    
    def read(self):
        if(self.__buf == None):
            print("ERRinit")
            return -1
        if(len(self.__buf) == 0):
            print("ERRempty")
            return -3
        return self.__buf.popleft()
        
class FiFoList:
    __buf = []
    
    def write(self, message):
        if(self.__buf == None):
            print("ERRinit")
            return -1
        if(len(self.__buf) == BUF_SIZE):
            print("ERRfull")
            return -2
        self.__buf.append(message)
    
    def read(self):
        if(self.__buf == None):
            print("ERRinit")
            return -1
        if(len(self.__buf) == 0):
            print("ERRempty")
            return -3
        return self.__buf.pop(0)