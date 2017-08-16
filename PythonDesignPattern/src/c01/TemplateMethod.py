from __builtin__ import super
class ApplicationFramework:
    def __init__(self):
        print "super construction\n"    
        self.__templateMethod()
               
    def __templateMethod(self):     
        self.customize1()
        self.customize2()      
    
    # test override method        
    def customize1(self):
        print "super: Nudge, nudge, wink, wink!\n",
    def customize2(self):
        print "super: Say no more, Say no more!\n"
            
   # Create a "application":
class MyApp(ApplicationFramework):
    
    def __init__(self):
        ApplicationFramework.__init__(self)           
        print "derive construction\n"
        print "run init here\n"
       
    def customize1(self):       
        print "Nudge, nudge, wink, wink!\n",
    def customize2(self):
        print "Say no more, Say no more!\n"

class ChildApp(MyApp):
    pass

#x = MyApp()
y = ChildApp()




