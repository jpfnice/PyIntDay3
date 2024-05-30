
class StackEmptyError(Exception):
    pass

class Stack:
    
    def __init__(self, size):
        self.__maxsize=size
        self.__content=[]
        
    def push(self, element):
        if len(self.__content) < self.__maxsize:
            self.__content.append(element)
        else:
            #import sys
            #print("The stack is full", file=sys.stderr)
            raise Exception("Stack full")
    
    def __len__(self):
        return  self.__content.__len__()
    
    def pop(self):
                
        if len(self.__content) != 0:
            return self.__content.pop()
        else:
            raise StackEmptyError("Stack empty")
        
    def maxSize(self):
        return self.__maxsize
    
    def isEmpty(self):
        return len(self.__content) == 0
    
    def __str__(self):
        return f"({len(self.__content)}/{self.__maxsize}) {self.__content}"



if __name__ == "__main__":
    s=Stack(3)
    s.push(10)
    s.push(20)
    s.push(45)
    print(s)

