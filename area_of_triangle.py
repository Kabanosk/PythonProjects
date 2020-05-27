from math import pow
class TriangleArea():

  def heronFormula(self,a,b,c):
    if a + b <= c or b + c <= a or c + a <= b:
      return "It is not a triangle!"
    else : 
      return pow((a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c),0.5)/4

  def basicFormula(self,a,h):
    return a*h/2 

  def sineFormula(self,a,b,sine):
    if 1 < sine and 0 > sine:
      return "sine never be greater than 1 or smaller then 0! (in triangle*)"
    else :
      return a*b*sine/2