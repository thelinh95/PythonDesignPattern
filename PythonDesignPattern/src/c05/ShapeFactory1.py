from __future__ import generators
import random

class Shape(object):
  # Create based on class name:
  
  #@classmethod
  #def factory(cls,type):
  
  def factory(type):    
    #return eval(type + "()")
    if type == "Circle": return Circle()
    if type == "Square": return Square()
    assert 1, "Bad shape creation: " + type
  
  factory = staticmethod(factory)
  
class Circle(Shape):
  def draw(self): print "Circle.draw"
  def erase(self): print "Circle.erase"
  
class Square(Shape):
  def draw(self): print "Square.draw"
  def erase(self): print "Square.erase"

   
# Generate shape name strings:
# linh ref thinking in java generator pattern for random
def shapeNameGen(n):
  types = Shape.__subclasses__()
  for i in range(n):
    yield random.choice(types).__name__

#book code
"""    
shapes = \
  [ Shape.factory(i) for i in shapeNameGen(7)]
"""

#linh code use map feature
shapes = map(Shape.factory, shapeNameGen(7))


for shape in shapes:
  shape.draw()
  shape.erase()  