class student:
  def __init__(self, name, roll):
    self.name = name
    self.roll = roll
    
  def show(self):
    print (self.name, self.roll)
    lap.show()
  
  class laptop:
    def __init__(self):
      self.ram = 16
      self.brand = "AMD"
      self.cpu = 'ryzen'
    
    def show(self):
      print (self.brand, self.cpu, self.ram)

s1 = student ('adnan', 1)
s2 = student ('sakib', 2)
lap = student.laptop()

s1.show()


    