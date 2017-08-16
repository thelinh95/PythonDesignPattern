#: c01:NewSingleton.py

class OnlyOne(object):
  class __OnlyOne:
    def __init__(self):
      self.val = None
    def __str__(self):
      return `self` + self.val
  instance = None
  def __new__(cls): # __new__ always a classmethod
    if not OnlyOne.instance:
      OnlyOne.instance = OnlyOne.__OnlyOne()
    return OnlyOne.instance
  def __getattr__(self, name):
    return getattr(self.instance, name)
  def __setattr__(self, name):
    return setattr(self.instance, name)

x = OnlyOne()
x.val = 'sausage'
print x
y = OnlyOne()
y.val = 'eggs'
print y
z = OnlyOne()
z.val = 'spam'
print z
print x
print y
#<hr>
output = '''
<__main__.__OnlyOne instance at 0x00798900>sausage
<__main__.__OnlyOne instance at 0x00798900>eggs
<__main__.__OnlyOne instance at 0x00798900>spam
<__main__.__OnlyOne instance at 0x00798900>spam
<__main__.__OnlyOne instance at 0x00798900>spam
'''

#Alex Martelli makes the observation that what we really want with a Singleton is to have a single set of state data for all objects. That is, you could create as many objects as you want and as long as they all refer to the same state information then you achieve the effect of Singleton. He accomplishes this with what he calls the Borg7, which is accomplished by setting all the __dict__s to the same static piece of storage: Add Comment


#: c01:BorgSingleton.py
# Alex Martelli's 'Borg'

class Borg:
  _shared_state = {}
  def __init__(self):
    self.__dict__ = self._shared_state

class Singleton(Borg):
  def __init__(self, arg):
    Borg.__init__(self)
    self.val = arg
  def __str__(self): return self.val

x = Singleton('sausage')
print x
y = Singleton('eggs')
print y
z = Singleton('spam')
print z
print x
print y
print `x`
print `y`
print `z`
output = '''
sausage
eggs
spam
spam
spam
<__main__.Singleton instance at 0079EF2C>
<__main__.Singleton instance at 0079E10C>
<__main__.Singleton instance at 00798F9C>
'''
#:~