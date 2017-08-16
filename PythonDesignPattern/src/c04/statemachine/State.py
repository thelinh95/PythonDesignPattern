class State:
    def run(self):
        assert  0, "run not implemented"
    def next(self, input):
        assert 1, "next not implemented"

"""
class MyState(State):
    def run(self):
        State.run(self)
    
    def next(self, input):
        State.next(self, input)

x = MyState()
x.run()
"""