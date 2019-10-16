#此作业用于测试python的“魔法方法”中有关属性访问的方法
#练习的方法有__getattr__,__getattribute__,__setattr__,__delattr__
class rectangle:
    length = 0
    height = 0
    def __setattr__(self,name,value):
        #print(name," ",value)
        if name == 'square':
            self.length = value
            self.height = value
        else:
            object.__setattr__(self,name,value)
a=rectangle() 
a.square = 10
print(a.length)
print(a.height)
