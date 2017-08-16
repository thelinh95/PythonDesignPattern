class Implementation2:
    def f(self,x, y,z):
        print "Implementation.f()" +x +y + z
    def g(self):
        print "Implementation.g()"
    def h(self):
        print "Implementation.h()"
        
class Proxy2(object):
    def __init__(self):
        self.__implementation = Implementation2()
            
    def __getattr__(self, name):
        return getattr(self.__implementation, name)
    
p = Proxy2()
p.f("f", "z", "u"); #p.g(); p.h();