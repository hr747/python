class engine:
   def __init__(self):
        pass
   def start(self):
     return 'engine start'

class deiver:
   def __init__(self):
      pass
class car:
   def __init__(self):
      self.engine=engine
      self.deiver=deiver
   def start(self):
      self.engine.start()
     