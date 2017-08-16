class Implementation:
    def f(self, x):
        print "Implementation.f()" + x
    def g(self,x):
        print "Implementation.g()" + x
    def h(self,x):
        print "Implementation.h()" + x

class Proxy(object):
    def __init__(self):
        self.__implementation = Implementation()
    
    def f(self, name): self.__implementation.f(name)
    def g(self): self.__implementation.g()
    def h(self): self.__implementation.h()
    
    def setImplement(self, newImplement):
        self.__implementation = newImplement

p = Proxy()
p.setImplement(Implementation())

p.f("f"); #p.g("g"); p.h("h")