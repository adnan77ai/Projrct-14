class student:
  def __init__(self,m1,m2,m3):
    self.m1 = m1
    self.m2 = m2
    self.m3 = m3

  def avg(self):
    return (self.m1 + self.m2 + self.m3)/3

s1 = student (3, 24, 48)
s2 = student (50, 75, 25)

print (s1.avg())
print (s2.avg())