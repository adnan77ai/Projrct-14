class computer:
  def __init__(self, cpu, ram):
    self.cpu = cpu
    self.ram = ram

  def config(self):
    print ('config is', self.cpu, self.ram)

com1= computer ('Intel i5', '8gb')
com2 = computer ('Intel i7', '4gb')

com1.config()
com2.config()